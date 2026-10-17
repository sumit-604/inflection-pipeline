# A5 AUDIT: Eimco Elecon (India) Limited (EIMCOELECO) | Q2 FY27

Run: /run-quarterly A5 adversary | Model: claude-opus-5-5 | Date: 2026-10-17
Inputs read: A4 review (work/review_eimcoeleco_q2fy27.md, 577 lines); A1 fulltexts and structured files for results, presentation and press release; A2 ledgers (3). The source PDFs and inputs/ were not opened. A3 notes were not read.
Anchor key: `res / pres / pr Lnnn` = line in the A1 fulltext (results / presentation / press release). `rev Lnnn` = line in the A4 review. `[d]` = A5 arithmetic on filed numbers. Amounts are Rs crore unless marked lakhs.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

Plain-language brief at rev L440-493.

| Part | Heading (rev line) | Status | Content check |
|---|---|---|---|
| 1 Summary narrative | L444 | present | 14 lines (L445-458). Inside the 10-20 line band. |
| 2 Sector intelligence | L460 | present | Coal, metals, construction, payer mix. Each line anchored and tiered. |
| 3 Business-model intelligence | L468 | present | Products, single segment, installed base, distributor cost, treasury, named disclosure gaps. |
| 4 Competition intelligence | L478 | present | Peer names marked INFERENCE and PENDING LIVE VERIFICATION. Strengths, weaknesses, one risk to watch. |
| 5 Forward map | L485 | present | 7 dated catalysts (30 Oct 2026, 14 Feb 2027, every quarter, H2 FY27, next deck, 30 Apr 2027, 30 May 2027). Each has a bull fork and a bear fork. |

Gate result: PASS. All five parts are present and carry real content.

---

## 1. COVERAGE AUDIT

Method: a fresh pass over each A1 FULLTEXT (page markers, note headers, statement lines, number tokens per slide), then a diff against the A2 ledgers, then a check of each ledger row against the A4 review.

Page markers (grep `^\[page N\]`): results 11, presentation 39, press release 4. These match the A1 headers.
Notes (grep over res L187-328): Notes 1-5 at res L188-194, Note 6 at res L266, an unnumbered cash-flow Note at res L328. Total 7.
Structured row IDs (grep `R###`): results 470, presentation 946, press release 92. These match each ledger's `ids_in_structured`.

### 1A. Results (res fulltext)

| Category | A2 count | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Notes | 7 | 7 (res L188, L191, L192, L193, L194, L266, L328) | none | PASS |
| Line items | 99 (98 + M001) | 99: P&L 27 (res L154-186), BS 36 (res L204-265 incl. 2 trade-payable sub-lines), CF 36 (res L273-326 incl. financing total L322) | none | PASS |
| Zero-standing | 11 | 11 (R091, R110-R112, R150 Sep-26 cell, R179, R180, R287, R393, R468, R469) | none | PASS |
| Agenda items | 2 | 2 (res L35, L41) | none | PASS |
| Auditor paragraphs | 4 | 4 (res L94, L100, L108, L119) | none | PASS |
| Entities | 29 | 29 (R375-R403; no named person, body or firm in the fulltext is absent) | none | PASS |
| Annexures | 3 | 3 (A res L79, B res L457, C res L481) | none | PASS |
| Signatures | 4 | 4 (CS res L70-76; auditor partner res L125-136; ED res L331-339; CFO letter res L521-522) | none | PASS |
| Mgmt numbers (embedded release) | 10 | 10 (res L394-413: 57, 33, 70.9%, 108.8%, 11, 18.8%, 8, 46.5%, 18-20%, 133) | none | PASS |
| Chart labels | 36 | 36 (res L355-384) | none | PASS |
| MISSING_FROM_STRUCTURED | M001 (financing total, res L322) | M001 confirmed. No other value-bearing line is absent from the structured file. | none | PASS |

### 1B. Presentation (pres fulltext)

| Category | A2 count | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Slides | 39 | 39 | none | PASS |
| Slide numbers | 748 | 748. Per-slide recount: s15 34, s16 19, s17 10, s18 149, s19 146, s20 48, s24 5, s28 8, s29 7, s31 4, s36 81, s37 145, s38 48. Remaining slides sum to 44. | none | PASS |
| Line items | 130 | 139 physical table lines. A2 merges 9 same-label rows: NC and current Investments, Borrowings, Lease Liability and Provisions on slides 19 and 37 (8), plus the duplicate PBT Margin row on slide 18 (1). Every cell ID is referenced. No row is lost. | none | PASS (convention note S06) |
| Zero-standing | 93 | 93 (s18 10, s19 37, s20 1, s28 1, s36 4, s37 38, s38 2) | none | PASS |
| Entities | 73 | 73 (R749-R821, continuous) | none | PASS |
| Forward | 18 | 18 (R822-R839, continuous) | none | PASS |
| Dates | 72 | 72 (R840-R911, continuous) | none | PASS |
| Footnotes / qualifiers | 35 | 35 (R912-R946, continuous) | none | PASS |

### 1C. Press release (pr fulltext)

| Category | A2 count | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Pages | 4 | 4 | none | PASS |
| Slide numbers | 50 | 50 (36 chart labels pr L64-93; 10 ED-remark numbers pr L104-123; 4 identifiers pr L24, L155, L164) | none | PASS |
| Entities | 14 | 14 | none | PASS |
| Forward | 7 | 7 | none | PASS |
| Dates | 14 | 14 | none | PASS |
| Qualifiers | 7 | 7 | none | PASS |

### 1D. Ledger rows against the A4 review
A4 states range-level review of results R001-R470 plus M001, presentation R001-R946 and press release R001-R092 (rev L13). It also cites all 7 notes one by one in Step 0D (rev L50-60), and every A2 data correction (R150, R014, R153, R242, R267, the H1 FY26 investing misalignment, M001) at rev L17-21. Every ledger ID falls inside a stated range. Orphan rows: none. Missing from ledger: none.
Two row groups covered by the range statement carry an unstated bear: R155/R156 (current investments) and R061-R072 (distributor and other expenses). These go under Audit 3, not here as orphans.

Coverage result: PASS. No loop to A2 or A3.

---

## 2. ARITHMETIC AUDIT

All values recomputed from the lakhs statement (res L154-326) or deck cells as cited. "Rounding" = a 1 bp or 0.01 pp gap caused by A4 working from rounded parts.

| # | Metric | A4 value | Recomputed [d] | Source line | Status |
|---|---|---|---|---|---|
| 1 | Q2 FY27 total-expense tie | 4,824.54 lakhs | 4,824.54 | res L158-167 | PASS |
| 2 | Operating EBITDA (Q2 FY26 / Q1 FY27 / Q2 FY27 / FY26 / H1 FY26 / H1 FY27) | 5.22 / 14.25 / 10.74 / 42.97 / 17.53 / 24.99 | 522.04 / 1,424.71 / 1,074.35 / 4,297.10 / 1,753.07 / 2,499.06 lakhs | res L155, L163, L164, L168 | PASS |
| 3 | Operating EBITDA margin | 15.71 / 18.38 / 18.92 / 18.62 / 17.39 / 18.61% | 15.707 / 18.378 / 18.916 / 18.623 / 17.391 / 18.605% | + res L154 | PASS |
| 4 | Reported EBITDA | 9.49 / 22.01 / 12.63 / 59.98 / 29.89 / 34.64 | 949.26 / 2,200.65 / 1,263.41 / 5,997.57 / 2,989.46 / 3,464.06 lakhs | res L163, L164, L168 | PASS |
| 5 | Core PBT (PBT - OI) | 2.62 / 11.86 / 8.55 / 33.35 / 12.94 / 20.41 | 262.00 / 1,185.91 / 855.18 / 3,335.17 / 1,294.14 / 2,041.09 lakhs | res L155, L168 | PASS |
| 6 | OI / PBT | 62.0 / 39.6 / 18.1 / 33.8 / 48.9 / 32.1% | 61.99 / 39.55 / 18.10 / 33.77 / 48.86 / 32.10% | res L155, L168 | PASS |
| 7 | Effective tax rate | 22.36 / 21.61 / 24.99 / 23.12 / 21.62 / 22.79% | 22.359 / 21.612 / 24.994 / 23.121 / 21.622 / 22.787% | res L168, L173 | PASS |
| 8 | PAT margin | 16.10 / 19.84 / 13.79 / 16.78 / 19.68 / 17.28% | 16.100 / 19.837 / 13.790 / 16.777 / 19.675 / 17.280% | res L154, L174 | PASS |
| 9 | Gross margin, filing basis | 71.75 / 54.14 / 59.88 / 57.13 / 62.70 / 56.57% | 71.753 / 54.137 / 59.880 / 57.132 / 62.701 / 56.565% | res L154, L158-160 | PASS |
| 10 | Distributor comp / revenue | 11.85 / 11.23 / 5.57 / 11.48 / 11.62 / 8.84% | 11.852 / 11.231 / 5.573 / 11.478 / 11.622 / 8.839% | res L154, L165 | PASS |
| 11 | Other Expenses / revenue | 19.81 / 14.69 / 22.29 / 14.01 / 17.89 / 17.91% | 19.811 / 14.694 / 22.288 / 14.007 / 17.892 / 17.905% | res L154, L166 | PASS |
| 12 | Distributor + Other / revenue | 31.66 / 25.92 / 27.86 / 25.48 / 29.51 / 26.75% | 31.663 / 25.925 / 27.861 / 25.485 / 29.514 / 26.744% | res L154, L165-166 | PASS (H1 FY27: rounding, S02) |
| 13 | Employee cost / revenue | 17.90 / 7.47 / 9.76 / 9.54 / 11.46 / 8.44% | 17.897 / 7.475 / 9.759 / 9.538 / 11.460 / 8.441% | res L154, L162 | PASS |
| 14 | Release EBITDA cross-check | 18.92%, +105.8% | 18.916%; 1,074.35 / 522.04 = +105.8% | res L403-404 | PASS |
| 15 | Deck "Other Expenses" = distributor + other | 16 = 3.17 + 12.66; 20 = 8.71 + 11.39 | 15.83; 20.10 (also Q2 FY26 10.52 vs 11; H1 FY27 35.92 vs 36) | pres L391 | PASS |
| 16 | Q2 YoY: revenue / op EBITDA / margin / D&A / finance / EBIT ex-OI / OI / core PBT / PBT / PAT / EPS | +70.9% / +105.8% / +321 bps / -15.1% / -25.5% / 2.78 to 8.67, +211.6% / -55.7% / +226.4% / +51.5% / +46.4% / +46.3% | +70.89% / +105.80% / +320.9 bps / -15.05% / -25.55% / 278.40 to 867.39, +211.56% / -55.75% / +226.40% / +51.51% / +46.37% / +46.34% | res L154-185 | PASS |
| 17 | H1 YoY: revenue / op EBITDA / margin / OI / core PBT / PBT / PAT / EPS | +33.2% / +42.6% / +122 bps / -22.0% / +57.7% / +18.8% / +17.0% / +17.0% | +33.25% / +42.55% / +121.5 bps / -21.95% / +57.72% / +18.79% / +17.03% / +17.05% | res L154-185 | PASS (margin: rounding, S02) |
| 18 | Q2 margin decomposition: GM / employee / manufacturing / distributor + other / net | -1,187 / -814 / -315 / -380 / +321 bps | -1,187.3 / -813.8 / -314.3 / -380.2 / +320.9 bps | res L154, L158-166 | PASS (mfg: rounding, S02). See Audit 3, claim 2, for the reading. |
| 19 | Q2 ETR change and cost | +263 bps; 0.28 | +263.6 bps; 27.52 lakhs | res L168, L173 | PASS (rounding, S02) |
| 20 | Step 3 derived quarters: Q1 FY26 revenue / margin / core PBT; H2 FY26 revenue / margin / core PBT per quarter; Q1 FY27 vs H2 avg and YoY; Q2 FY26 QoQ | 67.57 / 18.22% / 10.32; 129.94 / 19.58% / 10.21; +19.3%, +14.7%; -50.8% | 6,756.99 / 18.219% / 1,032.14; 12,994.02 / 19.578% / 1,020.52; +19.32%, +14.73%; -50.81% | res L154-168 | PASS |
| 21 | Q2 FY27 QoQ: revenue / op EBITDA / core PBT / OI / PBT / PAT | -26.7 / -24.6 / -27.9 / -75.6 / -46.8 / -49.1% | -26.73 / -24.59 / -27.89 / -75.63 / -46.77 / -49.07% | res L154-174 | PASS |
| 22 | H2 FY26 share of FY26 revenue | 56.3% | 56.31% | res L154 | PASS |
| 23 | H2 FY27 threshold and order-book cover | 173.1; 77% | 129.94 x 1.33246 = 173.14; 133 / 173.14 = 76.8% | res L154, L374 | PASS |
| 24 | Q2 PAT bridge (lakhs) | 370.07 + 182.24 + 36.68 + 4.19 - 238.16 - 79.38 - 27.52 = 248.12 | identical; ties to 783.24 - 535.12 = 248.12; tax parts tie to 261.00 - 154.10 = 106.90 | res L155-174 | PASS |
| 25 | H1 PAT bridge | 5.83 / 1.63 / 0.13 / -0.12 / -2.71 / -1.03 / -0.35 = 3.38 | 582.83 / 163.16 / 12.88 / -11.92 / -271.39 / -102.83 / -35.02 = 337.71 lakhs | res L154-174 | PASS |
| 26 | OI-reversion PBT / PAT; core PAT both years | 12.82 / 9.62; 6.41 vs 2.03 (+215%) | 1,282.40 / 961.88; 641.43 vs 203.42 (+215.3%) | res L155, L168, L173 | PASS |
| 27 | Ex-deferred H1 ETR | 25.91% | 779.00 / 3,006.09 = 25.91% | res L170, L168 | PASS |
| 28 | DTL roll | 7.70 to 6.76 | 770.36 to 676.36; -94.00 = H1 deferred credit | res L239, L172 | PASS |
| 29 | CFO; CFO / PAT | 1.84 (-69.6%); 0.08x / 0.30x / 0.57x | 183.78 (-69.59%); 0.079 / 0.305 / 0.571 | res L174, L300 | PASS |
| 30 | FCF FY26; H1 FY27 | (38.44); (0.28) | -3,844.02; -27.70 lakhs | res L300, L303 | PASS |
| 31 | Working-capital change, H1 FY27 / H1 FY26 / FY26 | (15.76) / (6.08) / (11.31) | -1,575.83 / -607.73 / -1,130.96; each ties L285 to L296 | res L285-296 | PASS |
| 32 | Receivable / inventory / payable days; CCC | 114.7 to 123.9; 400.4 to 361.2; 65.1 to 81.2; 450.0 to 403.9 | 114.66 to 123.89; 400.44 to 361.22; 65.05 to 81.18; 450.05 to 403.93 | res L154, L158-160, L214, L217, L252-257 | PASS |
| 33 | PPE change; CWIP change | +47.44 (+74.0%); -1.12 | +4,744.12 (+74.00%); -111.66 lakhs | res L204, L205 | PASS |
| 34 | Net debt ex-investments | 3.55 to 5.75 | 355.25 to 574.53 lakhs | res L218-219, L235, L243-244 | PASS |
| 35 | Net cash incl. investments | (200.98) to (207.03), +6.05 | 20,098.40 to 20,703.04 lakhs, +604.64 | + res L209, L216 | PASS |
| 36 | Investments / total assets; investment roll | 212.78, 37.95%; 8.24 = 1.03 + 7.21 | 21,277.57 / 56,061.09 = 37.95%; 823.92 = 102.75 + 721.17 | res L209, L216, L224, L278, L305 | PASS |
| 37 | FV gains share of H1 OI | 74.7% | 721.17 / 965.00 = 74.73% | res L155, L278 | PASS |
| 38 | Receivables / inventories / OCFL / OCL movement | +18.70 (+25.8%) / +6.96 (+6.4%) / +110% / -17.7% | +1,869.58 (+25.79%) / +695.56 (+6.41%, ties CF L289) / +110.5% / -17.74% | res L214, L217, L260, L261 | PASS |
| 39 | Current ratio Sep-26; NFAT TTM | 3.53; 2.22 | 22,558.10 / 6,399.17 = 3.525; 264.26 / 119.03 (PPE + CWIP + intangibles) = 2.220. The deck FY26 NFAT 3.1 ties on the same basis (230.75 / 74.21 = 3.11). | res L204-207, L223, L264; pres L376-377 | PASS |
| 40 | FY23-FY26 OCF / PAT | 74 / 149 = 0.50x | 0.497 | pres L713, L762 | PASS |
| 41 | FY26 revenue fall | -6.6% "(247 to 231)" | 230.75 / 247 = -6.58%; 231 / 247 = -6.48% | pres L697; res L154 | PASS (rounding basis, S02) |
| 42 | TTM revenue / op EBITDA / OI / core PBT / PAT / EPS | 264.26 / 50.43 (19.08%) / 14.29 / 40.82 / 42.09 / 72.97 | 26,426.05 / 5,043.09 (19.08%) / 1,429.08 / 4,082.12 / 4,209.04 lakhs / Rs 72.97 | res L154-185 | PASS |
| 43 | Net cash per share; book value per share | Rs 358.9; Rs 846.7 | 20,703.04 / 57.684 = 358.90; 48,841.06 / 57.684 = 846.70 | res L181, L231 | PASS |
| 44 | Order book / TTM revenue; months of cover | 0.50x; about 6 months | 0.503x; 6.04 months | res L374 | PASS |
| 45 | Q2 margin at Q1 distributor rate | 13.3% | (1,074.35 - 321.36) / 5,679.72 = 13.26% | res L154, L165 | PASS |
| 46 | Implied FY26 DPS vs FY25 | Rs 4.00 vs Rs 5.00 | (46,173.87 + 2,321.09 - 48,264.22) / 57.684 = Rs 4.00; 288.21 / 57.684 = Rs 5.00 | res L174, L230, L319 | PASS |
| 47 | Letter-to-disclosure gap | 38 days | 5 Sep to 13 Oct 2026 = 38 days | res L486, L32 | PASS |
| 48 | Spares share under one chart reading | 35% vs 48% | 20 / 57 = 35.1%; 16 / 33 = 48.5% | res L363-367 | PASS |
| 49 | Deck vs computed EBITDA margin gap | "0.1-0.3 pp" | 0.08 pp (Q1 FY27) to 0.32 pp (FY26) | pres L393, L704 | PASS (S03) |
| 50 | Cash-flow totals | (A), (B), (C) and A+B+C used as filed | H1 FY27 183.78 - 119.92 - 0.93 = 62.93; FY26 2,210.89 - 2,178.57 - 128.42 = -96.10; H1 FY26 604.44 - 364.39 - 327.09 = -87.04 | res L300-326 | PASS |
| 51 | Balance-sheet ties and the R150 correction | R150 sits at 31.03.26; Sep-26 cell blank | NCA Sep-26 = 33,502.99 without R150; Mar-26 = 31,717.32 with it; CA Sep-26 = 22,558.10 with inventories 11,547.54 | res L204-224 | PASS |
| 52 | Statutory dates | 14 Feb 2027; 30 May 2027; 30 Apr 2027 | 45 days after 31 Dec 2026; 60 days after 31 Mar 2027; six months after 30 Oct 2026 | statute (A4 marks PENDING LIVE VERIFICATION) | PASS |

Arithmetic result: PASS. No mismatch above rounding. Every rounding gap is 1 bp or 0.01 pp and changes no conclusion (S02, S03).

---

## 3. ADVERSARIAL READ

The three most positive claims in the A4 review, each tested against the same extract.

### Claim 1. Core operating PBT +226.4% YoY: "the cleanest test passes"; "the operating quarter is real at the core-PBT line"
Where: rev L139, L149, L431.
Strongest bear counter: The +226% is a base effect. Q2 FY26 core PBT of Rs 2.62 cr is the trough of the series. That quarter's revenue fell 50.8% QoQ [d, res L154]. In level terms, Q2 FY27 core PBT of Rs 8.55 cr sits below Q1 FY26 (Rs 10.32 cr), the H2 FY26 quarterly average (Rs 10.21 cr) and Q1 FY27 (Rs 11.86 cr) [d, res L155, L168]. On the less distorted measures, core PBT grew +57.7% in H1 and +22.4% on TTM (Rs 40.82 cr vs FY26 Rs 33.35 cr) [d]. Q2 FY27 fails A4's own 8C bull bar of Rs 10.21 cr and sits on its bear bar of Rs 8.55 cr (rev L354-355). Also, the distributor-rate drop alone is Rs 3.57 cr: at the Q2 FY26 rate of 11.85%, Q2 FY27 distributor comp would be 673.15 lakhs, not 316.53 lakhs. That is 60% of the Rs 5.93 cr YoY core-PBT gain [d, res L154, L165]. A4 calls this line unexplained.
Survives: YES. Step 3 shows the levels and says "not as a step-up" (rev L169). The verdict line and Step 2 still headline +226% with no TTM or run-rate qualifier.
Graft (A4): add to the VERDICT line, Step 2 diagnostic 3 and the summary at rev L448: "+226% is off a trough base. TTM core PBT grew 22.4% and H1 grew 57.7%. Q2 FY27's Rs 8.55 cr is below the Rs 10.21 cr H2 FY26 quarterly average. 60% of the YoY gain equals the distributor-rate drop."
Type: MISSING.

### Claim 2. The +321 bps margin gain is "operating leverage on a fixed cost base"; "the rise came from fixed costs spread over more sales"
Where: rev L148, L182 (Step 4 margin row tagged Recurring, operating leverage), L349 (8B), L450 (summary), A4 analyst_note.
Strongest bear counter, from A4's own decomposition (recomputed, row 18): gross margin -1,187 bps, employee +814 bps, manufacturing +314 bps. The fixed-cost lines (+1,128 bps) do not cover the gross-margin fall. Subtotal: -59 bps. Without the distributor plus other line, Q2 FY27 operating EBITDA margin would be about 15.11%, below Q2 FY26's 15.71% [d, res L154, L158-166]. All of the +321 bps rests on that one line (+380 bps). That line is not fixed-cost leverage:
- Other Expenses rose 92.3% (Rs 6.58 cr to Rs 12.66 cr) while revenue rose 70.9%. That is negative leverage [d, res L154, L166].
- Compensation to Distributors fell 19.6% in rupees (Rs 3.94 cr to Rs 3.17 cr) while revenue rose 70.9% [d, res L165]. A cost named for distributors fell against volume.
- Note 4 says comparatives "have been regrouped / rearranged wherever necessary, to make them comparable" (res L193). The regrouped comparatives still show 11.2% (Q1 FY27) and 11.9% (Q2 FY26). A Q2 reclassification would normally appear in regrouped comparatives. So the filed text leans against A4's Q3 bull answer (reclass, EBITDA unaffected, rev L368) and toward a like-for-like drop.
Survives: YES. The decomposition numbers are A4's own, but the attribution drawn from them is not supported.
Graft (A4): reword rev L148, L182, L349, L450 and the analyst_note. Suggested text: "Fixed-cost leverage (employee, manufacturing) only offset the gross-margin fall; net -59 bps. The whole +321 bps came from the distributor plus other line, which is unexplained." Add the Note 4 point to Q3 and to flag 5.
Type: FACTUAL (the review's conclusion is not supported by the arithmetic).

### Claim 3. "Large treasury book": net cash including investments Rs 207.03 cr (+Rs 6.05 cr) = Rs 358.9 per share; the borrowing "points to tight operating liquidity, not to a funding need"
Where: rev L233, L246, L317.
Strongest bear counter: The liquid part of the treasury fell in H1.
- Current investments fell from Rs 13.86 cr to Rs 2.81 cr, -79.7% (res L216). Non-current rose from Rs 190.68 cr to Rs 209.96 cr (res L209).
- Liquid net cash (current investments + cash + bank - borrowings) moved from +Rs 11.86 cr at Mar-26 to -Rs 1.53 cr at Sep-26 [d, res L216, L218, L219, L243]. On a liquid basis the company is now net borrowed.
- 98.7% of the Rs 212.78 cr book is non-current, with composition undisclosed (res L209).
- The +Rs 6.05 cr rise in net cash including investments is smaller than the Rs 7.21 cr fair-value and sale gains (res L278). Without MTM, net cash fell about Rs 1.17 cr [d].
- H1 CFO of Rs 1.84 cr did not cover capex of Rs 2.11 cr (res L300, L303). The Rs 2.32 cr dividend (res L319) was in effect funded by Rs 2.87 cr of new borrowing (res L315), not by the treasury.
Survives: YES. A4 Q14 and Q16 ask the right questions (rev L379, L381). The review states neither the liquid-position swing nor the MTM share of the net-cash rise. The Rs 358.9 per share figure is flagged for /fttcp without that caveat.
Graft (A4): add to the Step 5 net-cash rows and mandatory answer (rev L232-233, L246) and to the Step 6.5 treasury bullet (rev L317).
Type: MISSING.

### Mandatory acquisition-economics probe
Not triggered. A grep for `acqui|stake|takeover|amalgamat|merger|purchase consideration|share purchase|business transfer` over the three fulltexts hits only director biographies (pres L196, L215, L224) and "stakeholders" (pres L112; res L410, L444; pr L119, L153). No acquisition, purchase of a business or stake buy is described.
Nearest analog, tested: the unnamed Rs 47.44 cr capitalisation (res L204, L211). FY26 capex payments of Rs 60.55 cr (res L303) = 1.82x FY26 core PBT (Rs 33.35 cr) and 1.56x FY26 PAT (Rs 38.71 cr) [d]. Incremental revenue or earnings from the asset: NOT FOUND. No earnings multiple exists to stress-test. A4 Q4 and Q5 (rev L369-370) already ask for the asset class, date and D&A charge. No graft.

---

## FINDINGS (tagged)

| ID | Type | Loop | Finding |
|---|---|---|---|
| A5-F01 | FACTUAL | A4 | rev L447: "The company shows a Q1-high, Q2-low, H2-heavy pattern in both years [FILED]." H2 FY27 is not filed. The filing supports only Q2 < Q1 in both years (33.24 < 67.57; 56.80 < 77.52) and H2 = 56.3% of revenue for FY26 alone [d, res L154]. This sentence carries the seasonal read of the -26.7% QoQ, so it is not STYLE. Fix: "Q2 was below Q1 in both years. H2 was 56.3% of FY26 revenue (one year observed)." |
| A5-F02 | FACTUAL | A4 | Margin attribution (Audit 3, claim 2). Fixed-cost lines net -59 bps against the gross-margin fall. The whole +321 bps is the distributor plus other line. Note 4 leans against the reclass reading. |
| A5-M01 | MISSING | A4 | Core-PBT base-effect qualifier (Audit 3, claim 1). |
| A5-M02 | MISSING | A4 | Treasury liquidity qualifier (Audit 3, claim 3). |

No CONTRADICTION findings. No A2 or A3 findings.

---

## VERDICT

**INCOMPLETE.** Loop back to A4.
Gap: graft three surviving bear counters and fix two unsupported claims:
1. (FACTUAL, A5-F01) rev L447 "H2-heavy ... in both years [FILED]" is unsupported. H2 FY27 is not filed.
2. (FACTUAL, A5-F02) The "fixed-cost leverage" margin attribution is contradicted by the decomposition: GM -1,187 + employee +814 + manufacturing +314 = -59 bps. All of the +321 bps rests on the distributor plus other line (+380 bps). Note 4 (res L193) leans against the reclass reading.
3. (MISSING, A5-M01) Core PBT +226% needs the base-effect qualifier: TTM +22.4%, H1 +57.7%. Q2 FY27 Rs 8.55 cr is below the H2 FY26 average of Rs 10.21 cr and Q1 FY26 of Rs 10.32 cr. 60% of the YoY gain equals the distributor-rate drop.
4. (MISSING, A5-M02) Treasury: liquid net cash went from +Rs 11.86 cr to -Rs 1.53 cr. Current investments fell 79.7%. The net-cash rise of Rs 6.05 cr is below the Rs 7.21 cr FV gains. The H1 dividend was in effect funded by borrowing.
Coverage and arithmetic are clean. The brief gate passes. These are grafts, not a rework.

---

## STYLE NOTES (logged, no loop)

- S01: rev L461 anchors "Demand comes from underground coal and metal mines, plus construction piling" to `pres L428-434`. Those lines are slide 19 balance-sheet rows. The cited text is res L428-434 (or pr L137-143). Fix the prefix.
- S02: Rounding-basis artefacts. None changes a conclusion. H1 margin +122 bps (precise +121.5); manufacturing -315 bps (-314.3); Q2 ETR +263 bps (+263.6); H1 FY27 distributor plus other 26.75% (26.74%); FY26 revenue "-6.6% (247 to 231)" (231 / 247 = -6.5%; -6.6% uses the filed 230.75). Compute from lakhs, or state the rounded basis.
- S03: rev L122 says deck margins run "0.1-0.3 pp below". The actual range is 0.08 pp (Q1 FY27) to 0.32 pp (FY26).
- S04: rev L210 "vs 25.17% statutory" has no provenance marker. The rate is statute, not filing, and the company's tax-regime election is NOT FOUND in these files. Mark it "[statute, not in filing]".
- S05: rev L446 "Q2 FY26 revenue had fallen 50.8% from the quarter before it [FILED]" is derived (H1 FY26 less Q2 FY26). Tag it [FILED, derived].
- S06: The presentation ledger counts 130 line items under a merge convention: 8 same-label NC and current rows on slides 19 and 37, plus 1 duplicate PBT Margin row on slide 18. Physical table lines are 139. Every ID is referenced and no row is lost. A2 should state the convention in the count line.
- S07: A4 coverage is a range-level "reviewed" statement (rev L13), not row-level "reviewed, no finding" marking. Accepted, because every ID falls inside a stated range. Row-level marking would make the next audit cheaper.
- S08: Rule J balance on the CFO flag. ED Kamlesh Shah is an FCA with about 27 years in financial operations and treasury (pres L212-217). He is the evident interim cover, and the resignation letter is addressed to him (res L489). The flag stands because no successor is named. The forward map could state the mitigant.

---

```yaml
stage: A5-adversary
company: "EIMCOELECO"
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
  - claim: "Core operating PBT +226.4% YoY; 'the cleanest test passes'; 'the operating quarter is real at the core-PBT line' (rev L139, L149, L431)"
    counter: "Base effect. Q2 FY26 core PBT Rs 2.62 cr is the trough. Q2 FY27 Rs 8.55 cr is below Q1 FY26 Rs 10.32 cr, the H2 FY26 quarterly average Rs 10.21 cr and Q1 FY27 Rs 11.86 cr, and fails A4's own 8C bull bar. Less distorted growth: H1 +57.7%, TTM +22.4% (Rs 40.82 cr vs Rs 33.35 cr). 60% of the Rs 5.93 cr YoY gain equals the distributor-rate drop alone (Rs 3.57 cr at the Q2 FY26 rate of 11.85%)."
    source_line: "res L154, L155, L165, L168 [d]"
    type: MISSING
  - claim: "The +321 bps margin gain is 'operating leverage on a fixed cost base'; 'the rise came from fixed costs spread over more sales' (rev L148, L182, L349, L450, A4 analyst_note)"
    counter: "A4's own decomposition: GM -1,187 bps + employee +814 + manufacturing +314 = -59 bps. Without the distributor plus other line, Q2 FY27 margin is about 15.11%, below Q2 FY26 15.71%. All of the +321 bps rests on that line (+380 bps). Other Expenses rose 92.3% vs revenue +70.9%. Compensation to Distributors fell 19.6% in rupees (Rs 3.94 cr to Rs 3.17 cr). Note 4 says comparatives are regrouped to be comparable, yet Q1 FY27 and Q2 FY26 still show 11.2% and 11.9%, so the filed text leans against the reclass reading."
    source_line: "res L154, L158-166, L193 [d]"
    type: FACTUAL
  - claim: "'Large treasury book': net cash incl. investments Rs 207.03 cr (+Rs 6.05 cr) = Rs 358.9 per share; borrowing 'not a funding need' (rev L233, L246, L317)"
    counter: "The liquid treasury fell. Current investments went from Rs 13.86 cr to Rs 2.81 cr (-79.7%). Liquid net cash (current investments + cash + bank - borrowings) moved from +Rs 11.86 cr to -Rs 1.53 cr. 98.7% of the book is non-current, composition undisclosed. The +Rs 6.05 cr net-cash rise is below the Rs 7.21 cr FV and sale gains (about -Rs 1.17 cr without MTM). H1 CFO Rs 1.84 cr did not cover capex Rs 2.11 cr, so the Rs 2.32 cr dividend was in effect funded by Rs 2.87 cr of new borrowing."
    source_line: "res L209, L216, L218, L219, L243, L278, L300, L303, L315, L319 [d]"
    type: MISSING
findings_by_type:
  factual:
    - "A5-F01: rev L447 'Q1-high, Q2-low, H2-heavy pattern in both years [FILED]' is unsupported. H2 FY27 is not filed. Only Q2 < Q1 is filed for both years (33.24 < 67.57; 56.80 < 77.52), and H2 = 56.3% applies to FY26 only (res L154 [d]). Loop A4."
    - "A5-F02: The 'fixed-cost leverage' margin attribution (rev L148, L182, L349, L450, analyst_note) is contradicted by the decomposition. Fixed-cost lines net -59 bps against the GM fall. The entire +321 bps is the distributor plus other line, and Note 4 leans against the reclass reading (res L154, L158-166, L193 [d]). Loop A4."
  missing:
    - "A5-M01: The core PBT +226% headline (rev L139, L149, L431) lacks the base-effect qualifier: TTM +22.4%, H1 +57.7%. Q2 FY27 Rs 8.55 cr is below Q1 FY26 Rs 10.32 cr and the H2 FY26 average Rs 10.21 cr. 60% of the YoY gain equals the distributor-rate drop (res L154-168 [d]). Loop A4."
    - "A5-M02: The treasury liquidity qualifier is absent from Step 5 and Step 6.5 (rev L233, L246, L317). Liquid net cash went from +Rs 11.86 cr to -Rs 1.53 cr. Current investments fell 79.7%. The net-cash rise of Rs 6.05 cr is below the Rs 7.21 cr FV gains. The H1 dividend was in effect funded by borrowing (res L209-219, L243, L278, L300-319 [d]). Loop A4."
  contradiction: []
  style:
    - "S01: rev L461 anchor 'pres L428-434' points to slide 19 balance-sheet rows. The cited text is res L428-434 (or pr L137-143)."
    - "S02: Rounding-basis artefacts, no conclusion change: H1 margin +122 vs +121.5 bps; manufacturing -315 vs -314.3 bps; Q2 ETR +263 vs +263.6 bps; H1 FY27 distributor plus other 26.75% vs 26.74%; FY26 revenue -6.6% labelled '(247 to 231)', which computes to -6.5%."
    - "S03: rev L122 'deck margins run 0.1-0.3 pp below'. The actual range is 0.08 to 0.32 pp."
    - "S04: rev L210 '25.17% statutory' has no provenance marker. It is statute, not filing, and the tax-regime election is NOT FOUND."
    - "S05: rev L446 'Q2 FY26 revenue had fallen 50.8% [FILED]' is derived. Tag it [FILED, derived]."
    - "S06: The presentation ledger line_items count of 130 merges 9 same-label rows. Physical table lines are 139. All IDs are referenced. A2 should state the convention."
    - "S07: A4 coverage is a range-level 'reviewed' statement (rev L13), not row-level 'reviewed, no finding'. Accepted."
    - "S08: CFO flag balance (Rule J). ED Kamlesh Shah is an FCA with about 27 years in financial operations and treasury (pres L212-217), the evident interim cover. The flag stands."
loop_back_to: "A4"
gap: "Fix 2 FACTUAL claims and graft 3 surviving bear counters. (1) rev L447 'H2-heavy in both years [FILED]' is unsupported: H2 FY27 is not filed. (2) The 'fixed-cost leverage' attribution (rev L148, L182, L349, L450, analyst_note) is contradicted: GM -1,187 + employee +814 + mfg +314 = -59 bps, so all of the +321 bps rests on the distributor plus other line (+380 bps); add the Note 4 point (res L193) to Q3. (3) Core PBT +226% needs the base-effect qualifier: TTM +22.4%, H1 +57.7%, Q2 Rs 8.55 cr below the H2 FY26 average Rs 10.21 cr, and 60% of the YoY gain is the distributor-rate drop. (4) Treasury (rev L233, L246, L317): liquid net cash went from +Rs 11.86 cr to -Rs 1.53 cr, current investments fell 79.7%, the net-cash rise of Rs 6.05 cr is below the Rs 7.21 cr FV gains, and the H1 dividend was in effect funded by Rs 2.87 cr of borrowing."
style_notes:
  - "S01: change the rev L461 anchor prefix from pres to res (res L428-434)."
  - "S02: compute bps and pp deltas from lakhs, or state the rounded basis."
  - "S03: restate the deck margin gap as 0.08-0.32 pp."
  - "S04: mark 25.17% as [statute, not in filing]; regime election NOT FOUND."
  - "S05: tag the Q2 FY26 -50.8% QoQ as [FILED, derived]."
  - "S06: A2 to state the same-label merge convention in the presentation line_items count (130 merged, 139 physical)."
  - "S07: row-level 'reviewed, no finding' marking would make the next audit cheaper."
  - "S08: forward map M1 and Q8 could name the ED (FCA, about 27 years in finance) as the evident interim."
analyst_note: "Coverage and arithmetic are clean. Fresh counts tie on all three documents. 52 metric groups recompute within rounding. Every cash-flow and balance-sheet total ties, and A4 handles the R150 correction and the H1 FY26 investing misalignment correctly. The loop is about reading, not numbers. A4's own decomposition shows the fixed-cost lines only offset the gross-margin fall. Without the distributor plus other line, the YoY margin fell 59 bps. So the Q2 margin and most of the core-PBT gain hang on one unexplained line. Note 4's regrouping language makes the reclass reading weaker, not stronger. The +226% core PBT is off a trough base; TTM growth is +22.4%. In H1 the liquid part of the treasury turned into net debt, and the dividend was in effect paid from new borrowing. That matters before the Rs 358.9 per share figure reaches /fttcp. These are grafts, not a rework. The PROCEED WITH FLAGS verdict can stand once they are in. The documents describe no acquisition, so the probe is not triggered. One A4 correction cycle should close all four items."
```
