# A5 ADVERSARY / COMPLETENESS AUDIT: Aurum PropTech Ltd (AURUM), Q2 FY27

Agent: A5 adversary | model: claude-opus-5-5 | run date: 2026-10-17
This file holds three records: the run-1 audit, the Loop 1 re-audit and the Loop 2 re-audit (final, operator-approved). Earlier records are unchanged. The final YAML block in this file is the Loop 2 block.

---

# RUN 1 RECORD (loop_iteration 0)

Under audit: work/review_aurum_q2fy27.md (A4, 742 lines).
Inputs read: A4 review; A1 fulltexts (results, presentation, press release); A1 structured extractions (3); A2 ledgers (3).
Not read (by rule): source PDFs, anything under inputs/, A3 forensics files, work/notion-thesis.md.
Anchor key: RES / DECK / PR Lnnn = A1 fulltext line (same key as A4). REV Lnnn = A4 review line. Rs Cr = INR lakhs x0.01.
Scope limit: NOTION-anchored inputs in A4 (Rs85 SOTP base FV, CMP Rs236, Rs174.25 Cr goodwill baseline, trigger wording) are outside the A5 input set. They are taken as given. Only the arithmetic built on them is checked.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Heading in review | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | "### 1. SUMMARY NARRATIVE" (REV L610) | 12 lines, about 270 words (REV L611-L622). Inside the 10-20 line band. | PRESENT |
| 2. Sector intelligence | "### 2. SECTOR INTELLIGENCE" (REV L624) | 5 bullets with tiers and anchors (REV L625-L629). | PRESENT |
| 3. Business-model intelligence | "### 3. BUSINESS-MODEL INTELLIGENCE" (REV L631) | 6 bullets (REV L632-L637). | PRESENT |
| 4. Competition intelligence | "### 4. COMPETITION INTELLIGENCE" (REV L639) | 6 bullets (REV L640-L645). | PRESENT |
| 5. Forward map | "### 5. FORWARD MAP" (REV L647) | Make-or-break reading plus 8 catalysts. Every catalyst has a bull fork and a bear fork (REV L648-L660). | PRESENT |

Gate result: PASS. All five parts are present and carry real content.

---

## 1. COVERAGE AUDIT

Method. I ran a fresh enumeration over each A1 fulltext (the spine), then diffed it against the A2 ledger. I walked every ledger ID range to confirm each structured ID is referenced once. Then I checked that each ledger row is cited in A4 or covered by A4's explicit "Unreviewed rows: none" statement (REV L18).

### 1A. Results (RES, 1,075 lines; structured R001-R1728)

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Notes | 34 (17 consolidated + 17 standalone) | 34. Consolidated at RES L525, L526, L545, L558, L566, L573, L583, L591, L596, L599, L602, L606, L608, L624, L664, L665, L666. Standalone at RES L941, L943, L945, L959, L968, L976, L987, L996, L1000, L1003, L1006, L1010, L1012, L1027, L1066, L1067, L1068. | none (all 34 cited individually in REV 0D, L70-L103) | PASS |
| Line items | 354 | 354 = consolidated P&L 45 (L308-L356), segment 27 (L367-L394), BS 47 (L403-L451), CF 52 (L460-L517), discontinued 30 (L630-L663); standalone P&L 29 (L783-L813), BS 42 (L822-L865), CF 53 (L874-L931), discontinued 29 (L1033-L1065). Cells: 1,381, ties to A2. | none | PASS |
| Agenda items (board letter units) | 14 | 14 letter units; one true agenda item (results approval, RES L34-L36). | none | PASS |
| Auditor paragraphs | 11 keys | 12 paragraph units (consolidated paras 1-6 + signature; standalone paras 1-4 + signature). AP01 merges consolidated paras 1 and 2. All units covered. | none | PASS (STYLE S10) |
| Entities (auditor table) | 16 Sr rows / 15 IDs | 16 Sr rows (RES L229-L244); Locon listed twice (L238, L243); 15 distinct. | none | PASS |
| Entities (note 2 list) | annotation says "Note 2 lists 14 entities" | 15 lines (RES L528, L530-L543). A2's own keying: 6 ENTITY rows (R1580-R1585) + 9 MISSING rows (MS01-MS09) = 15. | n/a | CONTRADICTION (A2-C2) |
| Signatures | 10 | 10 (RES L46, L49, L668, L670-L672, L1070, L1072-L1074). | none | PASS |
| Press-release rows (pp. 2-4) | 44 | 44. | none | PASS |
| Table qualifiers | 20 | 20. | none | PASS |
| MISSING-from-structured rows | 9 (MS01-MS09) | 9 note-2 duplicates with no ENTITY row. No other unit absent. Consolidated note 3 and note 5 units are present but mis-anchored (STYLE S1). | n/a | PASS |
| Structured ID coverage | 1,728 of 1,728 | Contiguity walk: R001-R159 (agenda, PR rows, auditor paras, notes, SG01-SG02), R160-R1540 (354 line items, boundaries checked at every table change), R1541-R1728 (agenda, entities, notes, forward, dates, qualifiers). No gap, no double key. | none | PASS |

### 1B. Presentation (DECK, 1,082 lines; structured R001-R367)

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Slides (pdf pages) | 38 | 38 [page N] markers (DECK L17-L1061). | none | PASS |
| Numbers | 192 | Every data-bearing number on pp. 4-30 matches a row (e.g. p6 L169/L173/L177 = 20 units = R056-R075; p30 = 34 cells = R265-R298). Four biography tokens have no row (STYLE S7). | none | PASS |
| Entities / forward / dates / qualifiers | 94 / 26 / 27 / 28 | Spot recount: 12 named leaders p36-p37 = 12 rows; 7 directors = 7 rows; 10 timeline dates p16 = 10 rows. Totals tie to A1 header (367). | none | PASS |
| Structured ID coverage | 367 of 367 | Section 2 of the ledger lists R001-R367 contiguously. | none | PASS |

### 1C. Press release (PR, 173 lines; structured R001-R096)

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Pages | 4 | 4. | none | PASS |
| Numbers | 47 | 47 = p1 BSE code + 2 letter dates (3); p2 headline 4 + table 9 + quote 4 + streak 1 (18); p3 20; p4 5 + BSE code (6). | none | PASS |
| Dates / entities / forward / qualifiers | 11 / 22 / 7 / 9 | Ties to A1 header 96. | none | PASS |
| Structured ID coverage | 96 of 96 | All ranges in ledger sections 2-6. | none | PASS |

Coverage result: orphan rows none; rows missing from the ledger none. One CONTRADICTION in an A2 count annotation (A2-C2). Anchor and keying defects are STYLE (S1, S10).

---

## 2. ARITHMETIC AUDIT

Every statement cell in A4 tables 1-C (22 rows x 6 periods) and 1-S (17 rows x 6 periods) was re-read against RES L308-L356 and RES L783-L813. Zero cell mismatches. Derived metrics recomputed below from raw lakh figures.

| # | Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|---|
| 1 | Op EBITDA Q2 FY27 (Rev - Emp - Other) | 33.86 | 13,019 - 3,416 - 6,217 = 3,386 = 33.86; cross-check 660 + 2,806 + 632 - 712 = 3,386 | RES L308, L312, L315; L317, L314, L313, L309 | PASS |
| 2 | Op EBITDA Q1 FY27 / Q2 FY26 | 30.33 / 19.97 | 3,033 / 1,997 | RES L308-L317 | PASS |
| 3 | Op EBITDA H1 FY27 / H1 FY26 / FY26 | 64.19 / 31.35 / 88.18 | 6,419 / 3,135 / 8,818 | RES L308-L317 | PASS |
| 4 | Op EBITDA margin Q2 FY27 / Q1 / Q2 FY26 / H1 FY27 / H1 FY26 / FY26 | 26.01 / 27.12 / 25.14 / 26.52 / 21.64 / 23.14% | 26.008 / 27.119 / 25.139 / 26.521 / 21.638 / 23.139% | derived | PASS |
| 5 | Margin change YoY / QoQ | +87 / -111 bps | +86.9 / -111.1 bps | derived | PASS |
| 6 | Reported EBITDA (6 periods) | 40.98 / 37.50 / 25.05 / 78.48 / 44.87 / 119.52 | 4,098 / 3,750 / 2,505 / 7,848 / 4,487 / 11,952 | RES L317, L313, L314; ties DECK L828 | PASS |
| 7 | Core PBT ex-OI (6 periods) | (0.52) / (4.86) / (11.47) / (5.37) / (30.72) / (42.42) | 660-712 / 231-717 / -639-508 / 892-1,429 / -1,720-1,352 / -1,108-3,134 | RES L317, L309 | PASS |
| 8 | Core PBT incl. associate | (0.30) / (5.87) / (14.02) / (6.16) / (33.27) / (46.30) | 682-712 etc. | RES L319, L309 | PASS |
| 9 | OI / PBT Q2 / Q1 / H1 FY27 | 104.4 / 551.5 / 175.8% | 712/682, 717/130, 1,429/813 | RES L309, L319 | PASS |
| 10 | ETR Q2 / Q1 / H1 FY27 / Q2 FY26 / H1 FY26 / FY26 | 37.1 / 126.2 / 51.4 / 12.3 / 9.4 / 22.3% | 253/682, 164/130, 418/813, -110/-894, -186/-1,975, -333/-1,496 | RES L324, L319 | PASS |
| 11 | Current-tax rate Q2 / Q1 / H1 | 56.9 / 227.7 / 84.1% | 388/682, 296/130, 684/813 | RES L321 | PASS |
| 12 | PAT margin (6 periods) | 3.30 / (0.30) / (9.87) / 1.63 / (12.35) / (3.05)% | 429/13,019 etc. | RES L325, L308 | PASS |
| 13 | Op EBITDA after lease payments Q2 FY27 / Q2 FY26 | 9.61 (7.4%) / (1.31) | 33.86 - 24.25 = 9.61 (7.38%); 19.97 - 21.28 = (1.31) | DECK L834 | PASS |
| 14 | Revenue YoY / QoQ | +63.9% / +16.4% | 13,019/7,944 = 1.6389; 13,019/11,184 = 1.1641 | RES L308 | PASS |
| 15 | Op EBITDA YoY | +69.6% | 3,386/1,997 = 1.6955 | derived | PASS |
| 16 | D&A / FC / OI YoY | +12.6 / -3.1 / +40.2% | 2,806/2,492; 632/652; 712/508 | RES L314, L313, L309 | PASS |
| 17 | EBIT Q2 FY27 / Q2 FY26 | 5.80 / (4.95) | 3,386 - 2,806; 1,997 - 2,492 | derived | PASS |
| 18 | Distribution share of revenue increase | 42.53 of 50.75 = 83.8% | 4,253 / 5,075 = 83.80% | RES L368, L308 | PASS |
| 19 | Segment YoY Distribution / Rental / Capital | +156.4 / +10.0 / +260.8% | 6,972/2,719; 5,614/5,105; 433/120 | RES L367-L369 | PASS |
| 20 | Distribution segment margin Q2 FY27 / Q1 / Q2 FY26 | 16.3 / 14.2 / 20.3% | 1,139/6,972 = 16.34; 797/5,594 = 14.25; 551/2,719 = 20.26 | RES L368, L374 | PASS |
| 21 | Segment mix Distribution / Rental / Capital | 53.6 / 43.1 / 3.3% | 53.55 / 43.12 / 3.33% | RES L367-L370 | PASS |
| 22 | Q1 FY26 derived revenue / margin / core PBT | 65.44 / 17.39% / (19.25) | 14,488-7,944; (3,135-1,997)/6,544; -3,072+1,147 | RES L308-L317 | PASS |
| 23 | H2 FY26 derived revenue / margin / core PBT | 236.21 / 24.06% / (11.70) | 38,109-14,488; 5,683/23,621; -4,242+3,072 | RES L308-L317 | PASS |
| 24 | H1 FY27 average revenue; Q2 premium | 121.02; 7.6% | 24,203/2 = 12,101.5; 13,019/12,101.5 = 1.0758 | RES L308 | PASS |
| 25 | PAT bridge components | +12.76, +1.13, (3.14), +0.20, +2.04, +2.77, (3.63) = +12.13 | 50.75 x 25.139% = 12.76; 0.869% x 130.19 = 1.13; sum = 12.13 | RES L325 | PASS |
| 26 | PAT bridge shares | 105.2 / 9.3 / -25.9 / 1.6 / 16.8 / 22.8 / -29.9% | each / 12.13 | derived | PASS |
| 27 | Core-to-PAT gap bridge | 10.95 + 2.04 + 2.77 - 3.63 = 12.13 | same | RES L309, L318, L324 | PASS |
| 28 | OI reverts to Q2 FY26 level | PBT before associate 4.56 | 6.60 - 7.12 + 5.08 = 4.56 | derived | PASS |
| 29 | H1 non-recurring OI | 7.41 Cr = 51.9% | 451 + 267 + 23 = 741; 741/1,429 = 51.85% | RES L470, L472, L473, L309 | PASS (OI placement inferred; CF income adjustments sum to Rs13.82 Cr of Rs14.29 Cr OI, so the inference holds) |
| 30 | Standalone Op EBITDA (6 periods) | (3.48) / (2.88) / (2.62) / (6.36) / (5.45) / (14.03) | 6-201-153 etc. | RES L783, L787, L790 | PASS |
| 31 | Standalone core PBT / OI-PBT / ETR | (4.76) / 231.9% / 26.0% (Q2) and all periods | 361-837; 837/361; 94/361 | RES L784, L792, L795 | PASS |
| 32 | SA vs Cons PAT gap (6 periods) | 1.62 (+60.7%) / (2.28) (-117.5%) / (9.33) (-626.2%) / (0.66) (-14.3%) / (20.15) (-891.6%) / (17.38) (-302.3%) | 429-267 = 162, 162/267 = 60.67% etc. | RES L325, L796 | PASS |
| 33 | CFO / PAT H1 FY27 | 15.41x | 60.85 / 3.95 = 15.41 | RES L486, L325 | PASS |
| 34 | Lease-adjusted CFO H1 FY27 / H1 FY26 | 13.06 / (21.76) | 60.85-47.77-0.02; 25.40-30.05-17.11 | RES L486, L501, L502 | PASS |
| 35 | Lease-adjusted CFO / PAT | 3.31x | 13.06 / 3.95 = 3.306 | derived | PASS |
| 36 | FCF / lease-adjusted FCF H1 FY27 (H1 FY26) | 52.10 / 4.31 (16.04 / (31.12)) | 60.85-8.75; 13.06-8.75 (25.40-9.36; -21.76-9.36) | RES L488 | PASS |
| 37 | WC change sum H1 FY27 / H1 FY26 | (13.95) / (9.50) | 180+720-3,446+476+90+585 = -1,395; ties 7,112-1,395 = 5,717 | RES L475-L483 | PASS |
| 38 | Receivable days Sep-26 / Mar-26 | 36.4 / 50.0 | 48.11/242.03 x 183 = 36.38; 52.22/381.09 x 365 = 50.02 | RES L418 | PASS |
| 39 | Payable days Sep-26 / Mar-26 | 119.8 / 61.1 | 73.66/112.48 x 183 = 119.84; 32.15/192.13 x 365 = 61.08 | RES L442-L443 | PASS |
| 40 | Net cash ex-leases Sep-26 / Mar-26 | (190.81) / (139.23) | 0.80-83.16-64.63-43.82; 1.73-17.54-63.46-59.96 | RES L417-L420, L434, L440 | PASS |
| 41 | Net debt incl. leases | 26.10 / 83.80 | -190.81+216.91; -139.23+223.03 | RES L435, L441 | PASS |
| 42 | Lease cash / CFO | 0.79x | 47.79 / 60.85 = 0.785 | RES L501-L502, L486 | PASS |
| 43 | Goodwill / OE; GW + intangibles / OE; net tangible OE | 54.2% / 94.7% / 54.15 (Mar-26 40.9% / 58.9%) | 549.45/1,013.65; 959.50/1,013.65; 1,013.65-959.50 | RES L405, L406, L431 | PASS |
| 44 | Deferred tax swing | 78.10 | 27.66 + 50.44 | RES L411, L437 | PASS |
| 45 | Other current liabilities change | +95.74 | 104.61 - 8.87 | RES L447 | PASS |
| 46 | External loan yield | about 42% annualised | 2.01 x 2 / 9.52 = 42.2% | RES L421, L467 | PASS |
| 47 | Locon identifiable net assets | 115.78 | 458.06 - 342.28 | RES L559, L405 | PASS |
| 48 | Locon net tangible liabilities | "in the region of Rs120 Cr" | 115.78 - 319.07 + 78.10 = (125.19), under A4's own assumption | RES L406, L411, L437 | STYLE (S2) |
| 49 | Swap effective price | Rs231.42 | 45,806 lakh / 1,97,93,309 shares = Rs231.42 | RES L559-L560 | PASS |
| 50 | Warrant aggregate / 25% / balance | 118.02 / 29.51 / 88.52 | 51,00,000 x 231.421; 2,950.62 lakh; 11,802.47 - 2,950.62 = 8,851.85 lakh | RES L566-L570 | PASS |
| 51 | Warrant dilution | up to 5.3% | 51.00 / 963.2 lakh = 5.29% | RES L349 (4,816 lakh / Rs5) | PASS |
| 52 | Implied weighted shares Q1 / Q2 / H1 | about 767 / 867 / 865 lakh | 4,552/5.93 = 767.6; 451/0.52 = 867.3; 4,552/5.26 = 865.4 | RES L337, L339, L351, L353 | PASS |
| 53 | Possible Q2 EPS understatement | about 11% | expected about 769.3 lakh (765 + 197.93 x 2/92); 451/769.3 = 0.586 vs 0.52 = 11.3% | RES L349, L351, L559 | PASS |
| 54 | Q2 capitalisation / Op EBITDA | 11.0% | 374 / 3,386 = 11.05% | RES L603 | PASS |
| 55 | Deck Adjusted EBITDA | 15.44 | 40.98 + 1.21 - 2.50 - 24.25 = 15.44 | DECK L828-L835 | PASS |
| 56 | Deck expense ratio | 69.9% to 70.2% | 61.25/87.66 = 69.87%; 96.33/137.31 = 70.15% | DECK L826-L827 | PASS |
| 57 | Lease payments YoY; per-bed lease cost | +14.0%; about +32% | 24.25/21.28 = 1.1396; 1.1396/0.86 = +32.5% | DECK L834, L169 | PASS |
| 58 | Total income growth, deck basis / continuing | +56.6% / +62.5% | 137.31/87.66 = 1.5664; 13,731/8,452 = 1.6246 | DECK L826; RES L310 | PASS |
| 59 | Deck Rs5.95 Cr removed from segments | 6.32 - 0.37 = 5.95 | 632 - 37 = 595 | RES L379-L380 | PASS |
| 60 | Step 6.5 annualised base | 520.76 / 17.16 / (2.08) | 130.19 x 4; 4.29 x 4; 0.52 x 4 | RES L308, L325 | PASS |
| 61 | H1 operating EBIT | 7.86 | 64.19 - 56.33 | RES L314 | PASS |
| 62 | Issue price vs base FV | 2.7x | 231.42 / 85 = 2.72 | RES L560; Rs85 is a NOTION input | PASS (arithmetic only) |
| 63 | Standalone net worth rise | 510.21 | 1,11,339 - 60,318 = 51,021 lakh | RES L848 | PASS |

Arithmetic result: no mismatch above rounding. One approximation (row 48) is logged as STYLE.

---

## 3. ADVERSARIAL READ

The three most positive claims in A4, each attacked from the same extract.

### BC1. "Trajectory: RECOVERING. Core loss narrows every reading" (REV L272); EBIT "Turned positive" (REV L242); re-entry metric "core PBT ex-OI above zero" (REV L486, L499)

Strongest bear counter. Note 11 says the group capitalised Rs3.74 Cr in Q2 and Rs7.11 Cr in H1 of "cost incurred on its own product team and management team" into intangibles (RES L602-L604). Q1 capitalisation is therefore Rs3.37 Cr (7.11 - 3.74). With that cost expensed:
- Q2 FY27 core PBT ex-OI = (0.52) - 3.74 = Rs(4.26) Cr.
- Q1 FY27 core PBT ex-OI = (4.86) - 3.37 = Rs(8.23) Cr.
- H1 FY27 core PBT ex-OI = (5.37) - 7.11 = Rs(12.48) Cr.
These figures are before the amortisation of earlier capitalised development inside D&A, which is not disclosed. Q2 FY26 capitalisation is not in the filing, so the YoY comparison on this basis is ND.

The remaining Rs0.52 Cr gap to breakeven is 14% of one quarter's capitalisation. A change in capitalisation alone can carry the re-entry metric across zero. The direction still improves (8.23 to 4.26). "RECOVERING" survives. "Near breakeven" does not. A4 records the capitalisation in note C11 (REV L80) but never applies it to the core-PBT reading, the trigger reading, or the Step 8C metric.

Survives: YES. Graft into Step 3, Step 8C (report the metric before and after capitalised development) and the summary narrative. Type: MISSING.

### BC2. "The share issues priced Aurum at Rs231.42. That is 2.7 times the Rs85 base value on record" (REV L622); watchlist item 9 "price GREEN" (REV L420)

Strongest bear counter, three parts.
- Warrants are an option, not a sale. AREDL paid 25%, Rs29.51 Cr. The balance of Rs88.52 Cr "shall be payable by AREDL at the time of exercise", and AREDL "may exercise ... at its option, within a period of 18 months" (RES L569-L571). The promoter holds an 18-month call at Rs231.421 for 25% down. If the price falls below the strike, the balance will probably not come. The price test applies with certainty to Rs29.51 Cr, not Rs118.02 Cr.
- The 2.7x is the market's premium to the operator's FV, not a premium the buyers negotiated. Rs231.42 is about 1.9% below the CMP on A4's own file (Rs236, REV L36): 231.42 / 236 = 0.981.
- The acquisition probe (mandatory, below) shows that the swap's accretion cannot be tested.

Survives: YES. Graft beside the bull line in the brief and in watchlist item 9. Type: MISSING.

### BC3. "Cash looks better. After lease payments, operating cash was Rs13.06 Cr in H1, against Rs(21.76) Cr" (REV L616); lease-adjusted FCF "First positive half" (REV L315); net cash "+51.58 ... Improving" (REV L323-L324)

Strongest bear counter.
- H1 FY27 CFO includes an income-tax refund of Rs3.40 Cr and interest on the refund of Rs0.28 Cr (RES L484-L485), Rs3.68 Cr in total. Without them, lease-adjusted CFO is Rs9.38 Cr and lease-adjusted FCF is Rs0.63 Cr. H1 FY26 carried Rs1.75 Cr of the same items (1.34 + 0.41), so its ex-refund figure is Rs(23.51) Cr. The "first positive half" is positive by Rs0.63 Cr before a one-time refund.
- Net cash ex-leases rose Rs51.58 Cr. Rs22.20 Cr of that is cash acquired with Locon (RES L511). Rs24.05 Cr is discontinued-operations net cash, mostly the Navi Mumbai building sale (RES L506-L508: investing +77.55, financing (60.60)). Together Rs46.25 Cr is 89.7% of the increase. A4 names the Locon cash but not the building-sale cash.
- The direction still improves on every basis. INDETERMINATE-WITH-DIRECTION stands.

Survives: YES, as qualifiers. Graft into the Step 5 rows (REV L311, L315, L323) and the summary line (REV L616). Type: MISSING.

### MANDATORY ACQUISITION-ECONOMICS PROBE

Housing.com (Locon Solutions), acquired 29-Sep-2026, all-stock.
- Multiple: Rs458.06 Cr consideration (RES L559) / Locon PAT NOT FOUND in any extract = multiple NOT COMPUTABLE. The deck gives no Housing.com revenue, EBITDA or PAT (DECK L255-L382). The release gives none (PR L58-L89).
- Price structure: goodwill added Rs342.28 Cr = 74.7% of the consideration (RES L405). Identifiable net assets Rs115.78 Cr rest on Rs319.07 Cr of provisional intangibles (RES L406, L563). Net tangible position about Rs(125.19) Cr [derived; assumes all H1 movement in goodwill, intangibles and deferred tax is Locon].
- Quality markers. Debt: consolidated borrowings fell from Rs1.73 Cr to Rs0.80 Cr (RES L434, L440), so Locon added no material bank debt. Cash: Rs22.20 Cr acquired (RES L511). ROCE: NOT FOUND. Customer tenure: NOT FOUND. The deck offers only a +28% 5-year CAGR in core collections FY21-FY26 and an FY26 collection mix of 61% brokers, 30% developers, 9% DIY [MGMT; DECK L333, L372-L382]. Balance-sheet footprint: Distribution segment liabilities rose Rs273.73 Cr QoQ against Distribution segment assets up Rs159.74 Cr (RES L384, L390). Unallocable corporate assets rose Rs571.50 Cr (RES L386), consistent with goodwill held outside the segments [INFERENCE].
- Dilution: 1,97,93,309 new shares = 20.5% of the 963.2 lakh shares in issue at 30-Sep (RES L349, L559).
- Why the price reads as "cheap" and whether the year is a peak: neither question can be asked, because no earnings year is disclosed. The swap is accretive to existing holders only if Housing.com is worth more than the intrinsic value given up: 1,97,93,309 x Rs85 = Rs168.24 Cr at the base FV on file. That test is untestable while Locon earnings are NOT FOUND.
- Bear reading survives. A4 carries most of the substance (REV L353, L592-L593, Q2 and Q4 at REV L512, L514). A4 never states the multiple as NOT COMPUTABLE and never links the 74.7% goodwill share to its bull line. Grafted under BC2.

PropTiger (FY26), all-stock.
- Multiple: Rs86.45 Cr consideration (RES L574, L581) / PropTiger PAT NOT FOUND = NOT COMPUTABLE.
- Quality markers: ND. The Distribution segment margin fell from 20.3% to 16.3% YoY with a full quarter of PropTiger inside (RES L368, L374). That fits a lower-margin PropTiger [INFERENCE; no brand split].
- A4 Q9 and Q10 (REV L519-L520) already ask for the split. No further graft beyond the NOT COMPUTABLE statement.

---

## FINDINGS (tagged)

| ID | Type | Agent | Finding | Evidence | Fix |
|---|---|---|---|---|---|
| A4-F1 | FACTUAL | A4 | A4 calls the "fourth consecutive quarter of positive PBT" claim "true on reported PBT" (REV L254) and "true only after other income" (REV L612). The extract verifies only Q1 FY27 (Rs1.30 Cr) and Q2 FY27 (Rs6.82 Cr). Q3 and Q4 FY26 singly are not in the corpus. A4's own Step 3 says "Q3 and Q4 singly ND" (REV L267). | RES L319: FY26 (1,496), H1 FY26 (1,975), so H2 FY26 combined = +4.79 Cr; singly ND | Say: "verified for Q1 and Q2 FY27 only; H2 FY26 combined continuing PBT +Rs4.79 Cr; Q3 and Q4 FY26 singly ND". The "false on the core test" half stands. |
| A4-F2 | FACTUAL | A4 | The brief says "The 840 bps rise in Adjusted EBITDA margin comes from shrinking that leased base, not from scale" (REV L634). Lease payments rose 14.0% YoY. About 711 of the 833 bps unrounded gain comes from lease payments falling from 25.1% to 18.0% of adjusted income, because adjusted income grew 59.0%. Emp + other gave 77 bps and the ESOP add-back 45 bps. The gain is income growth (mostly Distribution, which carries no co-living leases) over a rising lease bill. The same bullet calls Rs24.25 Cr "the main cost" of Rental. That figure is the group lease bill on the consolidated build-up, and A4's own Q12 (REV L522) asks for the split. | DECK L823, L827, L831, L834, L835: 21.28/84.80 = 25.09%; 24.25/134.81 = 17.99%; 134.81/84.80 = 1.590 | Replace with the decomposition. Label the Distribution attribution [INFERENCE]. Call the Rs24.25 Cr a group figure. Optional: Rs4.62 Cr of the Rs15.44 Cr Adjusted EBITDA is non-RoU other income (134.81 - 130.19; DECK L823, RES L308). |
| A4-F3 | FACTUAL | A4 | Notes table C2 says note 2 lists "14 entities" (REV L71). Note 2 lists 15 (K2V2, Liv, Monk Tech Labs, HelloWorld Tech, Integrow, Aurum Analytica, Monk Tech Venture, YieldWiseX, Cuneate, NestAway Tech, Bonds Brain, NestAway Mena, PropTiger, HelloWorld Living, Locon). | RES L528, L530-L543 | Change to 15. The HelloWorld Living point stands (15 in note 2 vs 14 subsidiaries/associate in the auditor list). |
| A4-C1 | CONTRADICTION | A4 | The brief tags "Most of that growth came from PropTiger" as [FILED] (REV L611) and the Distribution margin fall "as PropTiger scaled" as [FILED, derived] (REV L633). A4 itself records organic ex-PropTiger growth as ND (REV L252), watchlist item 2 as UNKNOWN with "No entity split" (REV L413), and Q9 as unanswered (REV L519). | RES L368 gives Distribution only; no brand split in RES, DECK or PR | Retag both as [INFERENCE: Distribution +Rs42.53 Cr = 83.8% of the increase; PropTiger consolidated from 25-Sep-2025; no brand split]. |
| A2-C2 | CONTRADICTION | A2 | Ledger count-test line says "Note 2 lists 14 entities, 9 lack ENTITY rows: MS01-MS09" (ledger_results L11). A2's own keying gives 6 ENTITY rows (R1580-R1585) + 9 MISSING rows = 15. A4 inherited the 14 (A4-F3). | RES L528-L543; ledger_results L22, L539-L547 | Change the annotation to 15. No row or ID changes. A3 has nothing new to review from this fix. |
| A4-M1 | MISSING | A4 | BC1 bear counter (capitalised development against the core-PBT trajectory and the re-entry metric) is not in the review. | RES L603 | Graft per BC1. |
| A4-M2 | MISSING | A4 | BC2 bear counter (warrant optionality; issue at about market; Housing.com multiple NOT COMPUTABLE; 74.7% goodwill; 20.5% dilution) is not attached to the bull line or item 9. | RES L405, L559, L569-L571, L349 | Graft per BC2 and the probe. |
| A4-M3 | MISSING | A4 | BC3 bear counter (Rs3.68 Cr tax refund in CFO; Rs46.25 Cr of the net cash rise from building-sale and acquired cash) is not in Step 5 or the brief. | RES L484-L485, L506-L508, L511 | Graft per BC3. |

---

## VERDICT (run 1)

INCOMPLETE.

- Failing agents: A2 (one CONTRADICTION, annotation only) and A4 (three FACTUAL, one CONTRADICTION, three MISSING).
- Loop back to: A2, the earliest failing agent. The A2 change adds no rows or IDs, so A3 has nothing new to review. A4 then applies F1, F2, F3, C1 and grafts M1, M2, M3.
- Unaffected: the deliverable gate (PASS), coverage (no orphan, no missing row), and arithmetic (no mismatch above rounding). None of the findings moves the proposed Decision Status. Each one makes AVOID firmer, not weaker.

---

## STYLE NOTES (run 1; logged, no loop)

| ID | Agent | Note | Fix |
|---|---|---|---|
| S1 | A1 / A2 | Consolidated-context rows carry standalone anchors. R106 (consolidated, actual RES L549) is anchored at L949. R119-R121 and R125-R128 (consolidated note 5, actual RES L566-L569) are anchored at L968 / L972. R1663 (consolidated, actual RES L569) is anchored at L972. A2 keys them under N-S3 / N-S5, so N-C5 shows only 2 IDs. R080 (note 8 content, RES L594) is keyed under N-C9. No ID is orphaned. Values are identical across each consolidated/standalone pair, and A4 cites the correct lines. | Re-anchor and re-key on the next A1/A2 run. |
| S2 | A4 | Locon net tangible liabilities "in the region of Rs120 Cr" (REV L353). On A4's own assumption the figure is 115.78 - 319.07 + 78.10 = Rs(125.19) Cr. | Show the arithmetic and the assumption. |
| S3 | A4 | FN-01 (3.1% vs -3.2%) can be narrowed. The deck's own build-up gives 2.65 / 84.80 = 3.1% (DECK L823, L835), and +840 bps ties to 3.1%. Slide 29's -3.2% is contradicted by its own rows, most likely a sign error. | Say so in Q11 and FLAG-8. |
| S4 | A4 | Ledger cross-check R019 is not resolved in the text. Slide 3's "Others 11" equals Capital revenue 4.33 + other income 7.12 = 11.45 (DECK L108; RES L309, L369). The headline income bar shows other income as a business bar. FLAG-6 already carries the substance. | One line under FLAG-8. |
| S5 | A4 | The first forward-map catalyst, "H1 RPT disclosure (due with the half-year results)" (REV L653), has no absolute date. | Give a date with an [INFERENCE: Reg 23(9)] tag. |
| S6 | A4 | "That interest eliminates on consolidation" (REV L214). Up to Rs2.01 Cr of loan interest survives consolidation (RES L467). | Say "mostly eliminates". |
| S7 | A1 | Four biography number tokens in the deck have no row: "three patents" (DECK L994), "40 under 40" (L1002), "10K Startup" (L1033), "nearly a decade" (L1040). They are immaterial and leave no category gap. | None required. |
| S8 | A4 | Trivial A1/A2 annotations go unmentioned. SG08: the signature at 12:33:37 falls after the 12:30 meeting end (RES L38, L46). Deck R336 vs R355: Shetye 18 vs 15 years (DECK L928, L1024). PR R064: only the ED is quoted. No finding is expected. | Optional one-line "reviewed, no finding" list. |
| S9 | A4 | The HelloWorld Living year is OCR-truncated in the fulltext ("December 31. 202", RES L542). A4's 2025 rests on A1's image-verified row R1639. | Cite R1639. |
| S10 | A2 | AP01 merges consolidated auditor paras 1 and 2, so 12 paragraph units sit under 11 keys. All are covered. | None required. |

Run-1 YAML block (superseded; kept for the record):

```yaml
stage: A5-adversary
company: "AURUM"
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
  - claim: "Core loss narrows every reading to Rs(0.52) Cr; EBIT positive; re-entry metric core PBT ex-OI > 0 (REV L242, L272, L486, L499)"
    counter: "Rs3.74 Cr of own team cost capitalised in Q2 (Rs7.11 Cr H1). Expensed basis: Q2 core PBT Rs(4.26) Cr, Q1 Rs(8.23) Cr, H1 Rs(12.48) Cr. The Rs0.52 Cr gap to zero is 14% of one quarter's capitalisation, so capitalisation alone can carry the re-entry metric across zero. Direction still improves."
    source_line: "RES L602-L604"
    type: MISSING
  - claim: "Share issues priced Aurum at Rs231.42 = 2.7x the Rs85 base FV; watchlist item 9 price GREEN (REV L420, L622)"
    counter: "Warrants: only Rs29.51 Cr (25%) paid; Rs88.52 Cr at AREDL's option within 18 months, an 18-month call to the promoter. Rs231.42 is about 1.9% below CMP Rs236 on file. Housing.com Rs458.06 Cr / PAT NOT FOUND = multiple NOT COMPUTABLE; goodwill 74.7% of price; 20.5% dilution; accretion untestable."
    source_line: "RES L349, L405, L559-L560, L566-L571"
    type: MISSING
  - claim: "Cash looks better: lease-adjusted CFO Rs13.06 Cr vs Rs(21.76) Cr; first positive lease-adjusted FCF half; net cash +Rs51.58 Cr (REV L311, L315, L323, L616)"
    counter: "H1 CFO includes Rs3.40 Cr tax refund + Rs0.28 Cr refund interest; ex-refund lease-adjusted CFO Rs9.38 Cr and FCF Rs0.63 Cr. Rs46.25 Cr (89.7%) of the net cash rise is building-sale cash (Rs24.05 Cr) and Locon cash acquired (Rs22.20 Cr)."
    source_line: "RES L484-L485, L506-L508, L511"
    type: MISSING
findings_by_type:
  factual:
    - "A4-F1: 'fourth consecutive positive PBT is true on reported PBT' (REV L254, L612) is unverifiable for Q3 and Q4 FY26 singly; only Q1-Q2 FY27 verified; H2 FY26 combined continuing PBT +Rs4.79 Cr (RES L319)"
    - "A4-F2: brief L634 says the 840 bps comes from shrinking the leased base, not scale; lease payments rose 14.0% (DECK L834); about 711 of 833 bps came from lease payments falling from 25.1% to 18.0% of adjusted income on +59.0% income; Rs24.25 Cr is a group figure, not Rental-only"
    - "A4-F3: notes table C2 says note 2 lists 14 entities (REV L71); RES L528-L543 lists 15"
  missing:
    - "A4-M1: graft BC1, capitalised development (RES L603) against the core-PBT trajectory, trigger reading and Step 8C metric"
    - "A4-M2: graft BC2, warrant optionality (RES L569-L571), issue at about market, Housing.com multiple NOT COMPUTABLE, 74.7% goodwill, 20.5% dilution"
    - "A4-M3: graft BC3, Rs3.68 Cr tax refund in H1 CFO (RES L484-L485) and Rs46.25 Cr building-sale and acquired cash in the net cash rise (RES L506-L511)"
  contradiction:
    - "A4-C1: PropTiger attribution tagged [FILED] at REV L611 and L633 contradicts A4's own ND/UNKNOWN organic split (REV L252, L413, L519); retag [INFERENCE]"
    - "A2-C2: ledger_results L11 says note 2 lists 14 entities; A2's own keying gives 6 ENTITY rows (R1580-R1585) + 9 MISSING rows = 15 (RES L528-L543)"
  style:
    - "S1 (A1/A2): consolidated rows R106, R119-R121, R125-R128, R1663 anchored to standalone lines L949/L968/L972 and keyed under N-S3/N-S5; R080 keyed under N-C9; no orphan, values identical"
    - "S2 (A4): Locon net tangible 'region of Rs120 Cr' recomputes to Rs(125.19) Cr on A4's assumption; show arithmetic"
    - "S3 (A4): FN-01 narrows; deck build-up gives 2.65/84.80 = 3.1%; slide 29 -3.2% is self-contradicted"
    - "S4 (A4): slide 3 'Others 11' = Capital 4.33 + OI 7.12 (ledger R019 cross-check) not stated"
    - "S5 (A4): first forward-map catalyst lacks an absolute date"
    - "S6 (A4): standalone loan interest 'eliminates'; up to Rs2.01 Cr survives (RES L467)"
    - "S7 (A1): four deck biography number tokens unstructured (DECK L994, L1002, L1033, L1040); immaterial"
    - "S8 (A4): trivial annotations SG08, deck R336/R355, PR R064 unmentioned"
    - "S9 (A4): HelloWorld Living year OCR-truncated at RES L542; cite R1639"
    - "S10 (A2): AP01 merges consolidated auditor paras 1 and 2"
loop_back_to: "A2"
gap: "Loop A2 then A4. A2: fix ledger_results L11 note-2 entity count 14 to 15 (annotation only; no row or ID change; A3 has nothing new to review). A4: (F1) restate the four-quarter PBT streak as verified for Q1-Q2 FY27 only, H2 FY26 combined +Rs4.79 Cr, Q3/Q4 singly ND (REV L254, L612); (F2) replace brief L634 margin mechanism with the decomposition, lease payments +14.0%, about 711 of 833 bps from lease payments falling from 25.1% to 18.0% of adjusted income, Rs24.25 Cr is a group figure (DECK L823-L835); (F3) C2 note 2 = 15 entities (REV L71); (C1) retag PropTiger attribution [INFERENCE] at REV L611 and L633; graft M1 capitalised development Rs3.74 Cr Q2 against core PBT and Step 8C (RES L603), M2 warrant option, Housing.com multiple NOT COMPUTABLE, 74.7% goodwill, 20.5% dilution (RES L349, L405, L559, L569-L571), M3 Rs3.68 Cr tax refund in CFO and Rs46.25 Cr building-sale plus Locon cash in net cash (RES L484-L485, L506-L511)."
style_notes:
  - "S1: re-anchor consolidated rows R106, R119-R121, R125-R128, R1663 and re-key under N-C3/N-C5; move R080 to N-C8"
  - "S2: show Locon net tangible arithmetic (115.78 - 319.07 + 78.10 = -125.19)"
  - "S3: state that the deck build-up resolves FN-01 to 3.1%"
  - "S4: note that slide 3 'Others 11' folds OI 7.12 into a business bar"
  - "S5: date the H1 RPT catalyst"
  - "S6: 'mostly eliminates' for standalone loan interest"
  - "S7: deck biography tokens unstructured, immaterial"
  - "S8: list SG08, R336/R355, R064 as reviewed, no finding"
  - "S9: cite R1639 for the HelloWorld Living date"
  - "S10: AP01 merges two auditor paragraphs"
analyst_note: "Arithmetic is clean: every 1-C and 1-S cell and every derived metric recomputes within rounding. Coverage is clean: 1,728, 367 and 96 IDs walk contiguously into the ledgers, category counts match a fresh fulltext pass, and no orphan or missing row exists. The failures are in A4's reading, not its maths. Two statements give management claims more support than the extract does. The four-quarter PBT streak is half unverifiable. The brief's lease mechanism is wrong: lease payments rose 14%, and the margin gain is income growth over the lease bill, mostly Distribution. Three bull lines need their bear qualifier. The Rs0.52 Cr core loss sits beside Rs3.74 Cr of capitalised staff cost. The Rs231.42 price is certain for only Rs29.51 Cr, and the Housing.com multiple is NOT COMPUTABLE with 74.7% of the price in goodwill. The first positive lease-adjusted half is Rs0.63 Cr before a Rs3.68 Cr tax refund. None of this changes AVOID; each point makes it firmer. The A2 loop is a one-word annotation fix. NOTION-anchored inputs were outside A5's input set and were taken as given."
```

---

# LOOP 1 RE-AUDIT (loop_iteration 1)

Under audit: revised work/review_aurum_q2fy27.md (A4 loop 1, 768 lines) and work/blocks/a4.yaml (loop_iteration 1); corrected ledger_results_aurum_q2fy27.md (L11).
Inputs: the same A1 fulltexts, A1 structured files and A2 ledgers as run 1. Source PDFs, inputs/, A3 forensics and the Notion copy were not opened.
REV Lnnn below refers to the loop-1 review.

## L1-0. DELIVERABLE-COMPLETENESS AUDIT

| Brief part | Location in revised review | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | REV L630-L643 | 13 lines, inside the 10-20 line band. | PRESENT |
| 2. Sector intelligence | REV L645-L650 | 5 bullets, unchanged. | PRESENT |
| 3. Business-model intelligence | REV L652-L659 | 7 bullets, lease bullet rewritten. | PRESENT |
| 4. Competition intelligence | REV L661-L667 | 6 bullets, unchanged. | PRESENT |
| 5. Forward map | REV L669-L682 | Make-or-break reading (now on both capitalisation bases) plus 8 catalysts, each with a bull and a bear fork. The RPT catalyst now carries a date (16-Oct-2026, [INFERENCE: Reg 23(9)]). | PRESENT |

Gate result: PASS.

## L1-1. COVERAGE AUDIT

| Check | Result | Status |
|---|---|---|
| Ledger change | ledger_results L11 now reads "Note 2 lists 15 entities (6 with ENTITY rows R1580-R1585, 9 without): MS01-MS09". Header L3 unchanged: 1,728 of 1,728 IDs, orphan_ids []. No row or ID was added or removed. | PASS |
| Presentation and press-release ledgers | Unchanged since run 1 (367 of 367; 96 of 96). | PASS |
| Fresh enumeration | Same fulltexts; run-1 counts stand: 34 notes, 354 line items, 38 + 4 pages, 1,381 cells. | PASS |
| Ledger rows vs review | Preamble unchanged (REV L14-L18). The revision adds an explicit "reviewed with no finding" line for SG08, deck R336/R355 and PR R064 (REV L26) and resolves ledger R019 (REV L582). | PASS |
| Orphan rows / missing from ledger | none / none | PASS |

## L1-2. ARITHMETIC AUDIT (new or changed figures)

| # | Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|---|
| L1 | Q1 FY27 capitalisation | 3.37 | 711 - 374 = 337 | RES L603 | PASS |
| L2 | Core PBT ex-OI, capitalisation expensed, Q1 / Q2 / H1 | (8.23) / (4.26) / (12.48) | -486-337; -52-374; -537-711 | RES L309, L317, L603 | PASS |
| L3 | EBIT Q2 with capitalisation expensed | 2.06 | 5.80 - 3.74 | derived | PASS |
| L4 | Capitalisation vs core loss | 7.2x; gap = 14% of one quarter | 3.74 / 0.52 = 7.19; 0.52 / 3.74 = 13.9% | derived | PASS |
| L5 | Annualised core PBT, expensed basis | (17.04) | 4.26 x 4 | derived | PASS |
| L6 | Reading B H1, expensed basis | (5.60) | 1.51 - 7.11 = (5.60) | RES L317, L470-L473, L603 | PASS (arithmetic). The conclusion drawn from it is L1-F1 below. |
| L7 | Tax refund + refund interest H1 FY26 / H1 FY27 | 1.75 / 3.68 (+1.93) | 134 + 41; 340 + 28 | RES L484-L485 | PASS |
| L8 | Lease-adjusted CFO ex refunds | (23.51) / 9.38 (+32.89) | -21.76-1.75; 13.06-3.68 | derived | PASS |
| L9 | Lease-adjusted CFO / PAT ex refunds | 2.37x | 9.38 / 3.95 = 2.375 | RES L325 | PASS |
| L10 | Lease-adjusted FCF ex refunds | (32.87) / 0.63 (+33.50) | -31.12-1.75; 4.31-3.68 | derived | PASS |
| L11 | One-time share of net cash rise; underlying rise | 46.25 = 89.7%; about 5.33 | 24.05 + 22.20 = 46.25; 46.25 / 51.58 = 89.67%; 51.58 - 46.25 = 5.33 | RES L508, L511 | PASS |
| L12 | Goodwill share of Locon price; share-count addition; value given at Rs85 | 74.7%; 20.5%; 168.24 | 342.28 / 458.06; 197.93 / 963.2; 1,97,93,309 x 85 | RES L349, L405, L559 | PASS |
| L13 | Locon net tangible position | (125.19) | 115.78 - 319.07 + 78.10 | RES L405, L406, L411, L437, L559 | PASS (closes S2) |
| L14 | Adjusted EBITDA margin decomposition | about 833 bps; about 711 bps from lease intensity 25.1% to 18.0%; income +59.0%, lease bill +14.0% | 15.44/134.81 - 2.65/84.80 = 8.33 pp; 21.28/84.80 = 25.09%, 24.25/134.81 = 17.99%; 1.590; 1.140 | DECK L823-L835 | PASS |
| L15 | Non-RoU OI inside Adjusted EBITDA | 4.62 | 134.81 - 130.19 | DECK L823; RES L308 | PASS |
| L16 | Slide 3 "Others 11" | 11.45 | 4.33 + 7.12 | DECK L108; RES L309, L369 | PASS |
| L17 | Issue price vs CMP on file | about 1.9% below | 231.42 / 236 = 0.981 | RES L560; NOTION input | PASS |
| L18 | H2 FY26 combined continuing PBT | +4.79 | -14.96 - (-19.75) | RES L319 | PASS |

Arithmetic mismatches above rounding: none.

## L1-3. ADVERSARIAL READ (on the revised review)

The run-1 bull lines now carry their counters. I took the three most positive claims that remain in the revised text and attacked each from the extract again.

### L1-BC1. "Trajectory: RECOVERING ... On an expensed-development basis the direction still improves" (REV L276)

Strongest bear counter: the Q2 revenue step-up includes about 2 days of Locon P&L of undisclosed size, and Q2 FY26 capitalisation is ND, so the YoY change on the expensed basis cannot be read. Both points are already in the revised review (REV L179, L273, L300). Survives as a new graft: NO. The counter is carried.

### L1-BC2. Watchlist item 6 "Distribution EBITDA margin ... 16.3% ... GREEN (basis caveat; YoY decline noted)" (REV L431); brief "Distribution earns the profit: segment result Rs11.39 Cr, a 16.3% margin" (REV L654)

Strongest bear counter. Segment results exclude a block of corporate operating cost. In Q2 FY27, total continuing segment results were Rs12.77 Cr (RES L376) and consolidated operating EBIT was Rs5.80 Cr (Rev - Emp - Other - D&A; RES L308, L312, L314, L315). That leaves Rs6.97 Cr of cost outside the segments. The segment table ties: other income 7.12 + associate 0.22 - 6.97 = 0.37 = the "un-allocable ... net of other income" line (RES L380).
- Allocated by revenue share (53.55% for Distribution) [INFERENCE: allocation key not filed], Distribution's result is 11.39 - 3.73 = Rs7.66 Cr = 11.0% of revenue.
- On the same key, Q1 FY27 is 8.4% (unallocated 8.55 - 2.05 = 6.50; 50.0% share) and Q2 FY26 is 12.9% (unallocated 0.88 + 4.95 = 5.83; 34.2% share).
- The Notion threshold is an EBITDA margin of 12% or more. Segment D&A is not disclosed, so the EBITDA test cannot be computed in either direction.
GREEN rests on a pre-corporate-cost result. A loaded result sits below 12% in both FY27 quarters. Survives: YES. Graft into item 6 (status should read NOT DETERMINABLE on the named basis, or AMBER with this caveat) and into the brief bullet. Rental on the same key: 0.93 - 3.01 = Rs(2.08) Cr, which supports item 5's AMBER. Type: MISSING.
This claim was in the run-1 text unchanged. My run-1 selection of the three most positive claims did not reach it. It is raised now because the revised review's earlier bull lines are qualified, so it is one of the strongest unqualified positives left.

### L1-BC3. Competition "it now owns both the consumer portal (Housing.com) and the developer tools ... Few rivals hold both ends [INFERENCE]" (REV L662)

Strongest bear counter. The deck's own FY26 collection split for Housing.com is 61% agents/brokers, 30% developers and 9% DIY (DECK L333) [MGMT]. The overlap with Aurum's developer tools (Sell.do, Analytica, PropTiger) therefore covers about 30% of the portal's collections. The 61% broker slice is a different customer. The seller, REA India, owned both Housing.com and PropTiger and exchanged both for Aurum stock (RES L558-L559, L573-L574) [INFERENCE: a prior owner held a large part of "both ends" and exited]. Integration is undated (REV L601, M12). Survives: YES, as a qualifier. Graft one line into competition bullet 1. Type: MISSING.

### Acquisition-economics probe

The revised review carries the probe in full (REV L360-L367: both deals NOT COMPUTABLE, 74.7% goodwill share, 20.5% addition, Rs168.24 Cr value given, net tangible Rs(125.19) Cr). Closed.

## L1-4. CLOSURE OF RUN-1 FINDINGS

| ID | Type | Closed? | Evidence in revised files |
|---|---|---|---|
| A4-F1 | FACTUAL | CLOSED | REV L258 and L632: streak verified for Q1-Q2 FY27 only; H2 FY26 combined +Rs4.79 Cr; Q3/Q4 singly ND. |
| A4-F2 | FACTUAL | CLOSED | REV L655-L656: group lease bill +14.0%; about 711 of about 833 bps from lease intensity 25.1% to 18.0% on +59.0% income; group figure, not Rental-only; Distribution attribution tagged [INFERENCE]. Q12 aligned (REV L537). |
| A4-F3 | FACTUAL | CLOSED | REV L74: note 2 = 15 entities, listed by name. |
| A4-C1 | CONTRADICTION | CLOSED | REV L631 and L654 now [INFERENCE]; aligned at REV L78, L241, L256, L287. |
| A2-C2 | CONTRADICTION | CLOSED | ledger_results L11 now says 15 entities. |
| A4-M1 | MISSING | CLOSED | REV L83, L179, L187, L246, L248, L272-L279, L426, L461, L474, L501, L514-L516, L547, L564, L609, L634. |
| A4-M2 | MISSING | CLOSED | REV L60, L76, L77, L360-L367, L434, L564, L612, L617, L640-L643. |
| A4-M3 | MISSING | CLOSED | REV L86, L313-L322, L330-L331, L370, L373, L610, L637-L638. |
| Run-1 STYLE S2, S3, S4, S5, S6, S8, S9 | STYLE | Applied | REV L367, L536, L578, L582, L590, L218, L657, L26, L74. |
| Run-1 STYLE S1, S7, S10 | STYLE | Open, as logged | A1/A2 anchor and keying notes. No loop by rule. |

## L1-5. NEW FINDINGS INTRODUCED OR SURFACED IN LOOP 1

| ID | Type | Agent | Finding | Evidence | Fix |
|---|---|---|---|---|---|
| L1-F1 | FACTUAL | A4 | The M1 graft adds the claim that, with capitalised development expensed, trigger 1 "fires under either reading" (REV L450) and "fires under both readings" (REV L608, L749, L765; blocks/a4.yaml L63, L79). The extract does not support this for Reading B. Trigger 1 needs two consecutive negative quarters. On Reading B with capitalisation expensed, Q1 is at most Rs(1.06) Cr (2.31 - 3.37, less Q1 one-time OI) and is negative. Q2 is Rs2.86 Cr (6.60 - 3.74) less the Q2 one-time OI, and A4 itself says that Q2 split is ND (REV L449). Q2's sign is therefore unknown. Only H1 is shown negative (at most Rs(5.60) Cr). REV L608 also says "Reading B ... unresolved for Q2" in the same sentence. | RES L317, L470-L473, L603; REV L449 | Restate in all six places: "Reading B stays unresolved for Q2 on both bases. With capitalisation expensed, Q2 turns negative if the Q2 one-time OI exceeds Rs2.86 Cr (against Rs6.60 Cr on the reported basis). Q1 is negative on that basis." Trigger 1 still fires on the pre-named Reading A, so the proposed Decision Status does not change. |
| L1-M1 | MISSING | A4 | The L1-BC2 bear counter (Rs6.97 Cr of Q2 corporate cost outside the segments; Distribution's loaded result margin 11.0%, Q1 8.4%; EBITDA test not determinable) is not in watchlist item 6 or the brief. | RES L308, L312, L314-L315, L367-L368, L374, L376, L380 | Graft per L1-BC2. |
| L1-M2 | MISSING | A4 | The L1-BC3 bear counter (developers are 30% of Housing.com FY26 collections, so the "both ends" overlap covers about 30%) is not in competition bullet 1. | DECK L333 | Graft per L1-BC3. |

## L1-6. STYLE NOTES (loop 1; logged, no loop)

| ID | Agent | Note | Fix |
|---|---|---|---|
| L1-S1 | A4 | "Up; pre-lease-rent (Ind AS 116); after Rs3.74 Cr capitalised staff cost" (REV L242) can be read either way. | Say "flattered by Rs3.74 Cr of capitalised staff cost". |
| L1-S2 | A4 | The brief's expensed core loss of Rs4.26 Cr (REV L634) drops the caveat stated at REV L187: the figure is before amortisation of earlier capitalised development, which is ND. | Add the four-word caveat. |
| L1-S3 | A4 | REV L643 ends with one [FILED] tag. "That price is about the market price" rests on the Notion CMP, not a filing. | Tag that clause [prior Notion]. |
| L1-S4 | A1 / A2 | Run-1 S1, S7 and S10 remain open as logged. | None required this loop. |

## L1-7. VERDICT (loop 1)

INCOMPLETE.

- All eight run-1 items are closed: F1, F2, F3, C1, C2, M1, M2, M3.
- Gate PASS. Coverage PASS. Arithmetic: no mismatch above rounding.
- One new FACTUAL came in with the M1 graft (L1-F1). Two surviving bear counters on unchanged positive claims (L1-M1, L1-M2).
- Loop back to: A4 only. No ledger or extraction change is needed, so A2 and A3 have nothing to re-run.
- None of the three items moves the proposed Decision Status. L1-F1 removes an overstatement in the bear direction. L1-M1 and L1-M2 add qualifiers to bull lines.

Loop 1 YAML block (superseded by the Loop 2 block; kept for the record):

```yaml
stage: A5-adversary
company: "AURUM"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
loop_iteration: 1
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
  - claim: "Watchlist item 6 Distribution margin 16.3% GREEN; brief 'Distribution earns the profit' (REV L431, L654)"
    counter: "Segment results exclude Rs6.97 Cr of Q2 corporate operating cost (segment results 12.77 less operating EBIT 5.80; ties to the un-allocable line 7.12 + 0.22 - 6.97 = 0.37). On a revenue-share allocation [INFERENCE], Distribution's result margin is 11.0% in Q2 FY27 and 8.4% in Q1 FY27, below the 12% line. Segment D&A is ND, so the named EBITDA test is not determinable."
    source_line: "RES L308, L312, L314-L315, L367-L368, L374, L376, L380"
    type: MISSING
  - claim: "Competition: Aurum now owns both the consumer portal and the developer tools; few rivals hold both ends (REV L662)"
    counter: "Housing.com FY26 collections are 61% agents/brokers, 30% developers, 9% DIY [MGMT], so the developer-tool overlap covers about 30% of the portal's collections. The seller REA India held Housing.com and PropTiger together and exchanged both for Aurum stock [INFERENCE]."
    source_line: "DECK L333; RES L558-L559, L573-L574"
    type: MISSING
loop1_closure:
  - "A4-F1 CLOSED: REV L258, L632"
  - "A4-F2 CLOSED: REV L655-L656, L537"
  - "A4-F3 CLOSED: REV L74"
  - "A4-C1 CLOSED: REV L631, L654 (aligned L78, L241, L256, L287)"
  - "A2-C2 CLOSED: ledger_results L11"
  - "A4-M1 CLOSED: REV L179, L248, L272-L279, L426, L501, L514-L516, L547, L609, L634"
  - "A4-M2 CLOSED: REV L60, L76-L77, L360-L367, L434, L612, L617, L640-L643"
  - "A4-M3 CLOSED: REV L313-L322, L330-L331, L370, L373, L610, L637-L638"
findings_by_type:
  factual:
    - "L1-F1: REV L450, L608, L749, L765 and blocks/a4.yaml L63, L79 say trigger 1 fires under both readings with capitalisation expensed; Reading B Q2 on that basis is Rs2.86 Cr (6.60 - 3.74) less a Q2 one-time OI that is ND (REV L449), so its sign is unknown; only Q1 (at most Rs(1.06) Cr) and H1 (at most Rs(5.60) Cr) are shown negative (RES L317, L470-L473, L603)"
  missing:
    - "L1-M1: graft L1-BC2 into watchlist item 6 and brief L654; Rs6.97 Cr Q2 corporate cost outside segments; loaded Distribution margin 11.0% (Q1 8.4%, Q2 FY26 12.9%); EBITDA test not determinable (RES L376, L380)"
    - "L1-M2: graft L1-BC3 into competition bullet 1 (REV L662); developers are 30% of Housing.com FY26 collections (DECK L333)"
  contradiction: []
  style:
    - "L1-S1 (A4): REV L242 'after Rs3.74 Cr capitalised staff cost' is ambiguous; say 'flattered by'"
    - "L1-S2 (A4): brief REV L634 drops the 'before amortisation of earlier capitalised development (ND)' caveat stated at REV L187"
    - "L1-S3 (A4): REV L643 [FILED] tag covers 'about the market price', which rests on the Notion CMP; tag [prior Notion]"
    - "L1-S4 (A1/A2): run-1 S1, S7, S10 remain open as logged"
loop_back_to: "A4"
gap: "Loop A4 only (no ledger or extraction change). (L1-F1) In REV L450, L608, L749, L765 and blocks/a4.yaml L63, L79, replace 'fires under both/either reading(s)' with: Reading B stays unresolved for Q2 on both bases; with capitalisation expensed, Q2 turns negative only if the Q2 one-time OI exceeds Rs2.86 Cr (6.60 - 3.74), against Rs6.60 Cr reported; Q1 is negative on that basis (at most Rs(1.06) Cr); H1 at most Rs(5.60) Cr. Trigger 1 still fires on Reading A. (L1-M1) Graft into watchlist item 6 (REV L431) and brief L654: the 16.3% is before Rs6.97 Cr of Q2 corporate operating cost outside the segments (segment results 12.77 less operating EBIT 5.80; RES L376, L380); a revenue-share allocation [INFERENCE] gives 11.0% (Q1 8.4%, Q2 FY26 12.9%), below the 12% line; segment D&A ND, so the EBITDA test is not determinable; restate the status as NOT DETERMINABLE or AMBER. (L1-M2) Graft into competition bullet 1 (REV L662): Housing.com FY26 collections are 61% brokers, 30% developers, 9% DIY (DECK L333), so the developer-tool overlap covers about 30%."
style_notes:
  - "L1-S1: REV L242 say 'flattered by Rs3.74 Cr of capitalised staff cost'"
  - "L1-S2: add the amortisation caveat to the brief's Rs4.26 Cr figure"
  - "L1-S3: tag the CMP clause at REV L643 [prior Notion]"
  - "L1-S4: run-1 A1/A2 STYLE S1, S7, S10 stay open as logged"
analyst_note: "Loop 1 closes all eight run-1 items. F1, F2, F3, C1 and C2 are fixed, and grafts M1-M3 are in place with correct arithmetic. Every new derived figure recomputes. One new FACTUAL came in with the M1 graft. The review now says trigger 1 fires under both readings once capitalisation is expensed. Reading B for Q2 on that basis is Rs2.86 Cr less a Q2 one-time OI figure the filing does not split, so its sign is unknown. Only Q1 and H1 are shown negative. Trigger 1 still fires on the pre-named Reading A, so AVOID is unaffected; the fix is one sentence in six places. The fresh adversarial pass found two unqualified positives with surviving counters. Both sit in unchanged text that my run-1 selection did not reach. Distribution's GREEN 16.3% margin excludes Rs6.97 Cr of quarterly corporate cost, and a revenue-share allocation gives 11.0%. The 'both ends' competition claim covers only the 30% developer slice of Housing.com collections. Both are one-line grafts. A1/A2 STYLE items S1, S7, S10 stay open as logged."
```

---

# LOOP 2 RE-AUDIT (loop_iteration 2; final, operator-approved, no further loop)

Under audit: revised work/review_aurum_q2fy27.md (A4 loop 2, 770 lines) and work/blocks/a4.yaml (loop_iteration 2). No ledger or extraction change.
Scope (coordinator instruction): the changed passages plus the deliverable gate. No full arithmetic sweep, because no changed figure is new. Every figure in the changed passages was recomputed in loop 1 (table L1-2). The one reworded bound ("at most +Rs1.51 Cr", REV L449) is checked below.
REV Lnnn below refers to the loop-2 review.

## L2-0. DELIVERABLE-COMPLETENESS AUDIT

| Brief part | Location | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | REV L631-L644 | 13 lines. The capitalisation line now carries the amortisation caveat (L635). The CMP clause is tagged [prior Notion] (L644). | PRESENT |
| 2. Sector intelligence | REV L646-L651 | 5 bullets, unchanged. | PRESENT |
| 3. Business-model intelligence | REV L653-L661 | 8 bullets. New L656 carries the corporate-cost qualifier on the Distribution margin. | PRESENT |
| 4. Competition intelligence | REV L663-L669 | 6 bullets. L664 now carries the 30% developer-overlap qualifier. | PRESENT |
| 5. Forward map | REV L671-L684 | Unchanged. Make-or-break reading plus 8 catalysts, each with a bull and a bear fork. | PRESENT |

Gate result: PASS.

## L2-1. CLOSURE OF LOOP-1 FINDINGS

| ID | Type | Closed? | Evidence |
|---|---|---|---|
| L1-F1 | FACTUAL | CLOSED | REV L450 now reads: Reading B "stays unresolved for Q2 on both bases"; Q2 turns negative only if Q2 one-time OI exceeds Rs2.86 Cr (6.60 - 3.74), against Rs6.60 Cr reported; Q1 at most Rs(1.06) Cr (2.31 - 3.37); H1 at most Rs(5.60) Cr; "Trigger 1 still fires on Reading A". Same wording at REV L608 and L751, in the A4 analyst note (REV L768) and in blocks/a4.yaml L63 and L80. A grep of both files for "both readings", "either reading" and "fires under" returns nothing. REV L442 now labels FIRED "on Reading A, the pre-named basis". |
| L1-M1 | MISSING | CLOSED | Watchlist item 6 (REV L431) carries the Rs6.97 Cr corporate-cost counter, the 11.0% / 8.4% / 12.9% loaded margins [INFERENCE] and segment D&A ND. Its status is now "NOT DETERMINABLE / AMBER". The 6B summary is re-counted consistently: 3 RED, 4 AMBER, 1 GREEN, 1 UNKNOWN = 9 (REV L436). Brief L655-L656 carry the qualifier with tiers. A new FLAG-8 (REV L615, L758; a4.yaml L70) records it. |
| L1-M2 | MISSING | CLOSED | Competition bullet 1 (REV L664) adds the FY26 collection split, 61% brokers / 30% developers / 9% DIY [MGMT; DECK L333], and states that the developer tools touch about 30% of the portal's collections [INFERENCE]. The supporting REA inference from L1-BC3 was not grafted. That point was optional and is logged as STYLE L2-S1. |
| L1-S1 | STYLE | Applied | REV L242 "flattered by Rs3.74 Cr of capitalised staff cost". |
| L1-S2 | STYLE | Applied | REV L635 "before amortisation of earlier capitalised cost (not disclosed)". |
| L1-S3 | STYLE | Applied | REV L644 "[prior Notion: CMP Rs236]". |

## L2-2. CHECK FOR NEW FACTUAL / MISSING / CONTRADICTION IN THE CHANGED PASSAGES

| Changed passage | Check | Result |
|---|---|---|
| REV L449 "H1 is at most +Rs1.51 Cr" | One-time OI is "at least" Rs7.41 Cr, so H1 Reading B is at most 8.92 - 7.41 = Rs1.51 Cr. The bound now runs the right way. | No finding |
| REV L450 Reading B bounds | 6.60 - 3.74 = 2.86; 2.31 - 3.37 = (1.06); 1.51 - 7.11 = (5.60). All agree with loop-1 table L1-2. | No finding |
| REV L431 item 6 status | NOT DETERMINABLE / AMBER is consistent with the counter: the named EBITDA basis cannot be computed, and the loaded result basis is below 12%. Figures match loop-1 recomputation (6.97; 11.0%; 8.4%; 12.9%). | No finding |
| REV L436 6B summary | Counts re-tallied to 9 items. Item 6 moved from GREEN to AMBER. | No finding |
| REV L606-L623 flag list | FLAG-8 was inserted and later flags were renumbered (9-16). A grep for "FLAG-" followed by a digit finds no numbered cross-reference in the review or a4.yaml, so nothing points at a stale number. | No finding |
| REV L655-L656, L664 tiers | The filed-derived parts are tagged [FILED, derived]. The allocation and overlap readings are tagged [INFERENCE]. The collection split is tagged [MGMT]. | No finding |
| REV L768 / a4.yaml L80 analyst notes | Identical text in both files. Consistent with the body; no stale claim. | No finding |
| blocks/a4.yaml vs embedded review YAML | FLAG-TRIGGER-1 and FLAG-SEGMENT MARGIN BASIS strings match (a4.yaml L63, L70; REV L751, L758). | No finding |

New FACTUAL / MISSING / CONTRADICTION: none.
Coverage: no ledger or extraction change. Loop-1 coverage result stands (no orphan rows, nothing missing from the ledger).
Arithmetic: no mismatch above rounding in the changed passages.
Adversarial read: the changed passages add bear qualifiers only; they contain no new positive claim to attack. The loop-1 counters L1-BC2 and L1-BC3 are grafted. Per the coordinator's scope, no new unchanged-text selection was run this loop.

## L2-3. STYLE NOTES (loop 2; logged, no loop)

| ID | Agent | Note | Fix |
|---|---|---|---|
| L2-S1 | A4 | The optional supporting point from L1-BC3 is not in the competition bullet: REA India held Housing.com and PropTiger together and exchanged both for Aurum stock (RES L558-L559, L573-L574) [INFERENCE]. The required 30% qualifier is in. | Optional, next quarter. |
| L2-S2 | A4 | The same revenue-share key also puts Rental at Rs(2.08) Cr (0.93 - 3.01). That would support item 5's AMBER, but it is not stated at REV L430. | Optional. |
| L2-S3 | A1 / A2 | Run-1 S1, S7 and S10 remain open as logged. | Re-anchor and re-key on the next A1/A2 run. |

## L2-4. VERDICT (loop 2, final)

COMPLETE.

- All loop-1 non-STYLE findings are closed: L1-F1, L1-M1, L1-M2.
- All run-1 non-STYLE findings were closed in loop 1 and remain closed: A4-F1, F2, F3, C1, A2-C2, M1, M2, M3.
- No new FACTUAL, MISSING or CONTRADICTION. Deliverable gate PASS.
- Remaining items are STYLE only (L2-S1 to L2-S3). They are logged and trigger no re-run.
- The review may proceed to the Notion save step through the operator-approval gate. The proposed Decision Status (AVOID, unchanged) is not affected by any finding across the three audits.

```yaml
stage: A5-adversary
company: "AURUM"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
loop_iteration: 2
verdict: COMPLETE
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
surviving_bear_counters: []
loop2_closure:
  - "L1-F1 CLOSED: REV L442, L450, L608, L751, L768; blocks/a4.yaml L63, L80; no 'both readings' / 'either reading' / 'fires under' text remains in either file"
  - "L1-M1 CLOSED: REV L431 (item 6 NOT DETERMINABLE / AMBER), L436, L615, L655-L656, L758; blocks/a4.yaml L70"
  - "L1-M2 CLOSED: REV L664 (61/30/9 collection split, DECK L333; overlap about 30% [INFERENCE])"
  - "L1-S1, L1-S2, L1-S3 applied: REV L242, L635, L644"
  - "Run-1 A4-F1, F2, F3, C1, A2-C2, M1, M2, M3 closed in loop 1 and still closed"
findings_by_type:
  factual: []
  missing: []
  contradiction: []
  style:
    - "L2-S1 (A4): optional REA inference from L1-BC3 not grafted (RES L558-L559, L573-L574); the required 30% qualifier is in"
    - "L2-S2 (A4): Rental on the same revenue-share key is Rs(2.08) Cr (0.93 - 3.01); not stated at REV L430; optional"
    - "L2-S3 (A1/A2): run-1 S1, S7, S10 remain open as logged"
loop_back_to: ""
gap: ""
style_notes:
  - "L2-S1: optionally add the REA 'held both, exchanged both' inference to competition bullet 1"
  - "L2-S2: optionally state Rental's loaded result Rs(2.08) Cr under watchlist item 5"
  - "L2-S3: re-anchor consolidated rows R106, R119-R121, R125-R128, R1663; re-key under N-C3/N-C5; move R080 to N-C8; deck bio tokens and AP01 merge stay logged"
analyst_note: "Loop 2 is scoped to the changed passages and the deliverable gate, per the operator-approved final loop. L1-F1 is closed. Reading B is now stated as unresolved for Q2 on both bases, with the Rs2.86 Cr threshold, the Q1 and H1 bounds, and trigger 1 firing on Reading A only. No stale 'both readings' text remains in the review or in a4.yaml. L1-M1 is closed. Watchlist item 6 moves to NOT DETERMINABLE / AMBER with the Rs6.97 Cr corporate-cost counter, and the 6B summary is re-counted. L1-M2 is closed with the 30% developer-overlap line. The changed passages add only bear qualifiers with correct tiers and figures, so they introduce no new FACTUAL, MISSING or CONTRADICTION. Three STYLE notes remain, and none loops. The proposed Decision Status (AVOID, unchanged) was never affected by any finding across run 1, loop 1 and loop 2."
```
