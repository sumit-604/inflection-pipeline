# A5 ADVERSARY / COMPLETENESS AUDIT: PARACABLES | Q2 FY27

Agent: A5 adversary | model: claude-opus-5-5 | run date: 28-Oct-2026.
Review under audit: work/review_paracables_q2fy27.md (1,161 lines, read in full).
Inputs read: the 4 A1 fulltexts (results 713 lines, concall 627, deck 563, release 127; all read in full), the 4 A1 structured files (targeted reads and greps), and the 4 A2 ledgers.
Not read: source PDFs, anything under inputs/, A3 notes, orchestrator commentary, the Notion snapshot. Notion-anchored statements in the review are memory. This audit does not test them.
Anchor key: RES / CC / PPT / PR l.### = the results / concall / deck / press-release fulltext line. REV l.### = review line. LED-RES / LED-CC / LED-PPT / LED-PR l.### = ledger line. RES-STR / PPT-STR l.### = structured-file line.

Note: sections 0-4 and the first YAML block are the loop 0 audit. Line numbers there refer to the review as it stood before correction loop 1. The loop 1 re-audit is the last section, and its YAML block governs.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate, run first)

DELIVERABLE-COMPLETENESS: (1) narrative PRESENT (REV l.993-1010; 16 lines, inside the 10-20 band) | (2) sector PRESENT (REV l.1012-1024) | (3) business model PRESENT (REV l.1026-1041) | (4) competition PRESENT (REV l.1043-1054) | (5) forward map PRESENT (REV l.1056-1072; 10 dated catalysts, each with a bull fork and a bear fork, plus the make-or-break reading at l.1058-1059).

Gate result: PASS. Each of the five parts has real content. None is a placeholder.

---

## 1. COVERAGE AUDIT

Method. I ran a fresh pass over each fulltext and diffed my counts against the A2 count tests. Then I checked the ID range of each structured file against the ledger range. Last, I checked ledger rows and A3 finding IDs against the review.

| Doc | Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | Numbered notes | 20 | 20. SA 7 (RES l.330-363); CO 9 (RES l.625-665; note 1 is OCR'd as "4" at l.625); CF 4 (RES l.325-326, l.620-622) | none | PASS |
| Results | Note sub-items | 6 | 6 (SA 4a-c RES l.337-357; CO 5a-c RES l.634-653) | none | PASS |
| Results | Footnotes | 2 | 2 (asterisk RES l.356, l.652) | none | PASS |
| Results | Line items | 237 (235 structured + 2 lines M001-M004) | 237: P&L 34 + 34, balance sheet 37 + 37, cash flow 36 + 36, segment 23. The 10 use-of-proceeds rows sit under notes | none | PASS |
| Results | Agenda items | 2 | 2 (RES l.76, l.78) | none | PASS |
| Results | Auditor paragraphs | 11 | 11. SA 4 (RES l.114-137); CO 6 numbered + 1 SEBI-circular paragraph (RES l.385-433) | none | PASS |
| Results | Consolidation entities | 2 subsidiaries + 1 divested | 3 (RES l.407-408, l.658) | none | PASS |
| Results | Signature blocks | 4 rows | 5 physical blocks (RES l.88-93, l.138-145, l.365-373, l.434-442, l.666-672). One ledger row carries both auditor blocks (LED-RES l.400) | none | PASS (counting convention) |
| Results | Structured IDs vs ledger | 989 + M001-M004 | Structured R001-R993 (RES-STR l.6). R990-R993 equal M001-M004 (LED-RES l.342-345; RES-STR l.1013-1017) | none | PASS. Ledger header is stale (S1) |
| Concall | Participants | 13 | 13: 4 management (CC l.41-43); 9 analysts (9 "next question" hand-offs, CC l.186-592) | none | PASS |
| Concall | Turns | 88 | 88 (I spot-checked boundaries at T26, T37, T40, T46, T55, T62, T79, T81-T84) | none | PASS |
| Concall | Analyst turns | 35 | 35 (my per-analyst tally is 2+2+4+3+2+8+6+5+3) | none | PASS |
| Concall | Substantive analyst turns | 27 (5 ACK_ONLY, 3 INTRO_TURN) | 32. Only T31, T35 and T66 are acknowledgement-only | n/a | FAIL: X1 |
| Concall | NUMBER rows | 122 | Every numeric management line has a row. No gap found | none | PASS |
| Concall | Structured IDs vs ledger | 377 | 377 | none | PASS |
| Deck | Slides | 37 | 37 ([page 1] to [page 37]) | none | PASS |
| Deck | Slide 28 numeric cells | 94 + 1 duplicate (before the addendum) | 96 (PPT l.416-429) | n/a | 2 dropped by A1; restored as R523, R524 |
| Deck | Slide 30 numeric cells | 43 | 44 (PPT l.447-459, including 2 dashes) | n/a | 1 dropped; restored as R525 |
| Deck | Slide 29 numeric cells | 50 | 50 (PPT l.433-444; 10 rows x 5 years) | none | PASS |
| Deck | Structured IDs vs ledger | 522 (LED-PPT l.3-5) | Structured R001-R525 (PPT-STR l.3, l.539-542) | R523, R524, R525 absent from the ledger | FAIL: M1 |
| Release | Pages | 3 | 3 | none | PASS |
| Release | Snapshot cells / tiles | 72 / 11 | 72 (PR l.89-97, 9 rows x 8) / 11 (PR l.68-70) | none | PASS |
| Release | Structured IDs vs ledger | 157 | 157 | none | PASS |
| All | Ledger rows absent from A4 | n/a | None. The blanket statement covers 993 of 993, 377, 522 and 157 rows: "No ledger row is unreviewed" (REV l.25-32). All 20 notes are in the 0D table (REV l.81-94). 31 analyst turns are in 4A (REV l.644-673) | none | PASS |
| All | A3 findings cited in the A4 body | 65 claimed incorporated (REV l.39, YAML l.1088) | 61 have a body citation. RES-A3-01, CC-A3-12, PPT-A3-11 and PR-A3-06 appear only in the range lines (REV l.35-38) and the YAML list | n/a | FAIL: M4 |

**M1 detail (MISSING, loop to A2).** The deck structured file now runs R001-R525. A1 added R523 (20.4%, PPT l.425), R524 (85.3%, PPT l.426) and R525 (FY26 investments dash, PPT l.453) after A3 (PPT-STR l.539-548). These are the H1 YoY cells for depreciation and finance cost, and the second FY26 dash on slide 30. The deck ledger stops at R522. A4 read and used the three rows, but says they "are not ledger rows" (REV l.30). A4 cannot waive the A2 gate. Root cause: the deck slide_numbers count test grepped the structured file, not the fulltext (LED-PPT l.10). So it could not see what A1 dropped. The results ledger did sweep the fulltext and caught M001-M004. Fix: append the three rows, set the header to 525, and set the slide 28 and slide 30 row counts to 99 and 45. A3 needs no re-run, because the rows add no claim A3 has not seen.

**X1 detail (CONTRADICTION, A2 then A4).** The concall ledger flags T26, T37 and T55 as INTRO_TURN, and T40 and T46 as ACK_ONLY (LED-CC l.123, l.128, l.136, l.129, l.132). Each of these turns holds a substantive question:
- T26 asks about the firmness of the Rs 731 Cr book and the cancellation risk (CC l.288-291).
- T37 asks about order-book visibility past 3-4 months (CC l.342-344).
- T40 asks the HTLS execution timeline (CC l.368-369).
- T46 asks about the FY29 Rs 1,200 Cr capacity (CC l.403-405).
- T55 asks about margin amid commodity volatility (CC l.436-437).

A4 0C carries "27 substantive (A2: 5 ACK_ONLY, 3 INTRO_TURN)" (REV l.520). A4's own 4A table covers 31 turns in 30 rows, including T37, T40, T46 and T55 (REV l.644-673). It also books T26's question under T28 (REV l.652). The correct count is 32.

**M4 detail (MISSING, A4).** The review claims all 65 A3 findings are incorporated. Four IDs have no body citation. A5 does not read A3, so I cannot test whether their content is present without the ID. Fix: cite each ID where it is used, or mark it "reviewed, no change".

---

## 2. ARITHMETIC AUDIT

I recomputed every value below from the raw fulltext numbers. SA = standalone, CO = consolidated.

| Metric | A4 value (REV line) | Recomputed | Source line | Status |
|---|---|---|---|---|
| Op EBITDA Q2 FY27 SA (PBT + D + Fin - OI) | 40.91 (l.161) | 32.39 + 4.43 + 7.89 - 3.80 = 40.91 | RES l.162, l.169-170, l.173 | PASS |
| Op EBITDA Q1 FY27 / Q2 FY26 / H1 FY26 / H1 FY27 / FY26 SA | 34.74 / 5.71 / 20.87 / 75.65 / 65.73 | 34.74 / 5.71 / 20.87 / 75.65 / 65.73 | RES l.162-173 | PASS |
| Op margin Q2 FY27 / Q2 FY26 / H1 FY27 / FY26 SA | 7.30 / 1.34 / 6.94 / 3.44% | 7.300 / 1.335 / 6.942 / 3.437% | RES l.161 | PASS |
| Op EBITDA and margin, CO Q2 FY26 / H1 FY26 / FY26 | 6.20, 1.45% / 21.36, 2.43% / 66.33, 3.47% | 6.20, 1.449% / 21.36, 2.430% / 66.33, 3.467% | RES l.457-469 | PASS |
| Reported EBITDA Q2 FY27 / H1 FY27 / FY26 SA | 44.71 / 82.54 / 117.50 | 44.71 / 82.54 / 117.50 | RES l.169-173 | PASS |
| Core PBT (PBT - OI) Q2 FY26 / Q2 FY27 / H1 FY27 SA | (2.13) / 28.59 / 52.04 | (2.13) / 28.59 / 52.04 | RES l.162, l.173 | PASS |
| OI / PBT Q2 FY26 SA; CO | 112.0%; 110.3% | 111.95%; 110.34% | RES l.162, l.173, l.458, l.469 | PASS |
| ETR Q2 FY27 / H1 FY27 / FY26 SA; H1 FY26 CO | 25.16 / 25.44 / 25.91%; 26.15% | 8.15/32.39 = 25.16%; 14.99/58.93 = 25.44%; 21.07/81.31 = 25.91%; 11.24/42.99 = 26.15% | RES l.177-178, l.473-474 | PASS |
| PAT margin Q2 FY27 / H1 FY27 SA | 4.33 / 4.03% | 4.326 / 4.032% | RES l.185 | PASS |
| Gross margin Q2 FY26 / Q2 FY27 SA | 26.82 / 25.35% | 1 - 312.91/427.57 = 26.82%; 1 - 418.36/560.40 = 25.35% | RES l.165-166 | PASS |
| YoY margin bridge (GM / employee / other exp) | -147 / +13 / +730 = +596 bps (l.238) | -147.0 / +13.4 / +730.1 = +596.5 bps | RES l.165-171 | PASS |
| Revenue YoY SA / CO | +31.07 / +30.93% (l.224) | +31.07 / +30.93% | RES l.161, l.457 | PASS |
| Op EBITDA YoY SA / CO | +616.5 / +559.8% | +616.5 / +559.8% | as above | PASS |
| PAT YoY SA; EPS YoY SA | +82.8%; +68.2% | +82.81%; +68.18% | RES l.185, l.201 | PASS |
| Finance cost YoY; D&A YoY SA | +96.8%; +15.7% | +96.76%; +15.67% | RES l.169-170 | PASS |
| SA-CO PAT gap % (Q2 FY26 / H1 FY26 / FY26) | -0.08 / -1.58 / -0.81% (l.193-196) | -0.075 / -1.581 / -0.813% | RES l.185, l.481 | PASS |
| Pipes net revenue = CO-SA revenue gap, Q2 FY26 | 0.43 (l.198) | 3.69 - 3.26 = 0.43 = 428.00 - 427.57 | RES l.684, l.686 | PASS |
| PAT bridge: revenue / margin / D&A / Fin / OI / tax | +1.77 / +33.43 / -0.60 / -3.88 / -16.15 / -3.59 = +10.98 (l.265-273) | 132.83 x 1.3355% = 1.77; 560.40 x 5.965% = 33.43; sum to PBT 14.57; 14.57 - 3.59 = 10.98 = 24.24 - 13.26 | RES l.161-185 | PASS |
| Tax split: higher PBT / ETR change | -3.73 / +0.14 | 14.57 x 25.59% = 3.73; 32.39 x 0.43 pp = 0.14 | RES l.177-178 | PASS |
| Run-rate PAT ex-OI annualised | 85.6 (l.279) | 28.59 x 0.7484 x 4 = 85.58 | derived | PASS |
| Implied weighted shares Q2 FY27 / Q2 FY26 | 32.76 / 30.14 Cr (l.75) | 24.24/0.74 = 32.76; 13.26/0.44 = 30.14 | RES l.185, l.201 | PASS (EPS rounding noted by A4) |
| Fully diluted shares | 33.44 Cr | 32,72,39,473 + 72,00,000 = 33.44 Cr | RES l.344, l.361 | PASS |
| Warrant money paid / balance | 7.56 / 22.68 | 72,00,000 x 10.50 = 7.56; x 31.50 = 22.68 | RES l.345, l.351 | PASS |
| Use of proceeds unutilised | 26.66 | 92.39 + 7.56 + 0.10 - 73.39 = 26.66 | RES l.350-355 | PASS |
| CFO / PAT H1 FY27; H1 FY26 SA | -0.73x; -1.86x | -31.89/43.94 = -0.726; -60.02/32.26 = -1.861 | RES l.185, l.305 | PASS |
| FCF H1 FY27 / H1 FY26 | (73.19) / (85.03) | -31.89 - 41.30; -60.02 - 25.01 | RES l.305, l.307 | PASS |
| WC change H1 FY27 / H1 FY26 | (104.45) / (111.92) | sum of RES l.296-301 both columns; 77.23 - 104.45 = -27.22 | RES l.294-302 | PASS |
| Receivable days FY26 / H1 ann. / TTM / Q2 ann. | 78.9 / 66.1 / 67.9 / 64.3 | 413.40/1,912.16 x 365 = 78.91; 394.79/2,179.6 = 66.11; /2,123.52 = 67.86; /2,241.6 = 64.28 | RES l.234, l.161 | PASS |
| Inventory days / payable days (on COGS) | 72.1 to 73.5 / 49.8 to 31.8 | 284.91/1,441.74 = 72.13, 329.46/1,636.00 = 73.50; 196.61/1,441.74 = 49.78, 142.49/1,636.00 = 31.79 | RES l.231, l.260-263, l.165-166 | PASS |
| CCC FY26 / H1 FY27 | 101.3 / 107.8 | 101.26 / 107.82 | derived | PASS |
| Gross borrowings / D/E | 131.96 / 0.143 | 20.68 + 111.28 = 131.96; /920.01 = 0.1434 | RES l.246, l.250, l.257 | PASS |
| Net debt incl. / excl. other bank balances (H1; FY26) | 46.17 / 95.30; 82.66 / 111.01 | 131.96 - 10.33 - 49.13 - 26.33 = 46.17; 131.96 - 10.33 - 26.33 = 95.30; 115.77 - 4.76 - 28.35 = 82.66; 115.77 - 4.76 = 111.01 | RES l.233-236, l.250, l.257 | PASS |
| Equity roll-forward | 920.02 vs 920.01 | 778.07 + 44.04 + 97.67 + 0.24 = 920.02 | RES l.195, l.246, l.293, l.317 | PASS |
| Capex visibility (PPE adds + CWIP; residual vs other NCA) | ~11.5; ~29.8 vs 29.78 | -1.80 + (8.86 - 0.79 ROU - 0.04 intangibles) + (1.74 - 0.04) = 7.93; + 3.59 = 11.52; 41.30 - 11.52 = 29.78 | RES l.220-223, l.228, l.283, l.289, l.307, l.309 | PASS |
| Cash tax coverage; 16.26 - 4.67 | 29%; 11.59 | 28.7%; 11.59 (= closing CTL) | RES l.177, l.267, l.304 | PASS |
| ROCE H1 annualised (average / closing CE) | 13.7% / 12.7% | 133.58 / ((893.84 + 1,051.97)/2) = 13.73%; /1,051.97 = 12.70% | RES l.246, l.250, l.257, l.691 | PASS |
| Fully diluted run-rate EPS; P/E at Rs 59.6 | 2.90 / 2.63; 20.6x / 22.7x | 96.96/33.44 = 2.900; 87.88/33.44 = 2.628; 20.55x / 22.68x | derived | PASS |
| FY27 H2 need at +15 / +18 / +20%; H2 YoY | 1,109.18 / 1,166.55 / 1,204.79; +7.3 / +12.9 / +16.5% | same; H2 FY26 base 1,033.72 | RES l.161 | PASS |
| QoQ revenue Q2 FY27; Q2 FY26 (vs derived Q1 FY26) | +5.9%; -5.2% | +5.86%; 427.57/450.87 = -5.17% | RES l.161 | PASS |
| Exports H1 YoY; Q2 QoQ | -17.9%; +2.0% | 313.1/381.5 = -17.93%; 158.1/155.0 = +2.00% | PPT l.271, l.274; CC l.145-146 | PASS |
| US Rs 700 Cr vs 30% of FY27 revenue | 660-688 | 0.30 x 2,198.98 to 2,294.59 = 659.7 to 688.4 | CC l.149, l.595 | PASS |
| Rs 5,000 Cr FY31 CAGR from FY26 | 21.2% | (5,000/1,912.16)^(1/5) = 1.2120 | CC l.329 | PASS |
| EBITDA CAGR incl. OI / operating FY22-FY26 | 48.5% / 34.0% | (117.5/24.2)^(1/4) = 48.4%; (65.7/20.4)^(1/4) = 34.0% | PPT l.435-437 | PASS |
| OI share of reported EBITDA, Q2 FY26 / Q2 FY27 | 78% / 8.5% | 19.95/25.66 = 77.7%; 3.80/44.71 = 8.50% | RES l.162 | PASS |
| Release margins on total income | 7.9% EBITDA, 4.3% PAT | 44.71/564.20 = 7.92%; 24.24/564.20 = 4.30% | PR l.94-96 | PASS |
| Revenue per tonne FY26 | Rs 6.45 lakh | 1,912.16 Cr / 29,664 t = Rs 6.45 lakh | PPT l.214; RES l.161 | PASS |
| Credibility ratio; specificity; quantified share | 50%; 0.73; 62.5% | 1.5/3; 16/22; 20/32 | REV l.608-622, l.768, l.568 | PASS (arithmetic only; see X2 on the scoring) |
| Q&A share of call | ~69% | (58:11 - 17:03) / 3,563 s = 69.3% | CC l.182, l.613 | PASS |

Result: zero mismatches above rounding. A4's tables tie to the filed rows.

---

## 3. ADVERSARIAL READ

### P1. "Operating recovery is real and filed": 7.30% margin, core PBT 28.59 vs (2.13), all PAT growth operating; operating leg STRENGTHENED (REV l.278, l.955, l.958)
- **Strongest bear counter.** All of the +596 bps YoY gain comes from one line. Other expenses fell from 23.17% to 15.87% of revenue (+730 bps), and gross margin fell 147 bps (RES l.165-171). No document gives the reason.
- **Survives?** Yes. **Already in A4** (REV l.238, l.955, l.999, flag l.1145, Q12 l.459). No graft needed.
- **Secondary probe that does not survive.** H1 FY27 carries an unrealised FX gain of 2.66 and a derivative loss of 0.81 (RES l.287, l.291), in undisclosed lines. The net +1.85 is 2.4% of H1 operating EBITDA. It is also smaller than the H1 FY26 net of +3.12 (RES l.287, l.291). So it cannot explain the YoY gain.

### P2. Receivable days fell from 78.9 to about 66; "the receivable leg reads as timing" (REV l.294, l.316, l.399)
- **Strongest bear counter.** Receivables fell 18.61, but the payables paydown (54.16) and the inventory build (44.55) swamp that fall (RES l.296-300). Finance cost runs at 23.9% of period-end reported debt, annualised. That rate points to discounting outside the debt lines, which would flatter receivable days (RES l.169, l.250, l.257). Other bank balances rose 20.78 (RES l.236) and may be margin money.
- **Survives?** Yes. **Already in A4** (REV l.241, l.303, l.316, Q6 l.453, missing-evidence list l.960). No graft needed.

### P3. "Against the only references on file, the operating print lands at or above them": ROCE at the ~13% destination, PAT run-rate inside Rs 80-110 Cr, margin on the path to 7.83% (REV l.360, l.409, l.423)
- **Strongest bear counter (ROCE).** The 13.7% sits on a pre-build base. About Rs 266.6 Cr of the Rs 300 Cr Narmadapuram plan (PPT l.211; about Rs 33.4 Cr visible, REV l.317) still has to enter capital employed before the plant earns. Partial start is Q1 FY28 (CC l.166), and 220 kV will not carry the plant's revenue in its first two years (CC l.418). At H1-annualised EBIT of 133.58, capital employed of 1,051.97 + 266.6 = 1,318.6 gives about 10.1%. The match with the destination is a pre-capex reading. ROCE dips during the build and recovers only as the plant ramps.
- **Survives?** Yes. **Not in A4.** The review says "At the destination on file" (l.360) and "Upward" (l.409). **Graft (M2):** add one line to 6A, the 6.5 Pillar 1 row and 8A-W.
- The PAT-range and margin-path legs: the "hopeful / not achieved" hedge (CC l.454-455) and the Q3 clawback strip are already in A4 (l.209, l.407). No further graft.

### MANDATORY ACQUISITION / STAKE-BUY ECONOMICS PROBE
The documents describe two purchases. The deck says the company "acquired Narmadapuram land" (PPT l.139-144). The filing records a stake buy: 2,19,97,664 preferential shares to non-promoters and 72,00,000 promoter warrants, all at Rs 42 (RES l.337-347).
- **Land.** The extract does not state the consideration. It gives only 31 acres inside a Rs 300 Cr project (PPT l.211). No earnings multiple can be computed: NOT FOUND. No graft beyond that.
- **Stake buy at Rs 42.**
  - On earnings: 21.3x FY26 SA EPS of 1.97 (RES l.201); 15.2x H1 FY27 annualised EPS of 2.76 (1.38 x 2); 14.2x Q2 run-rate EPS of 2.96.
  - On book: 1.49x post-issue book of Rs 28.11 (920.01 Cr / 32.72 Cr shares, RES l.246, l.361); 1.65x pre-issue book of Rs 25.49.
  - Quality markers: FY26 ROE 7.7% (60.24 / 778.07). The price was set on trough earnings, so it is not cheap on trailing numbers.
- **Bear reading.** Non-promoters paid in full. Promoters paid 25%. The deck gives a 30-Sep market cap of Rs 1,845 Cr on 32,72,39,473 shares (PPT l.548-550), which is Rs 56.4 a share. At that price the warrants are Rs 14.4 a share in the money. That is about Rs 10.4 Cr of intrinsic value against Rs 7.56 Cr paid (RES l.345). Conversion pays Rs 22.68 Cr for stock worth about Rs 40.6 Cr. So conversion is the rational arbitrage and signals little conviction. Non-conversion while in the money is the informative outcome.
- **Can the extract show the price was fair?** No. The extract does not show the June pricing-date price.
- **Survives?** Yes. A4 treats conversion as the bull fork and as a skin-in-the-game test (REV l.373, l.469, l.1070, l.980). **Graft (M3):** state the issue multiples and the in-the-money value, and reframe the bull fork and the watchlist #6 threshold.

---

## 4. OTHER FINDINGS (judgment and fact checks; Rule J symmetry)

**X2 (CONTRADICTION, A4). The credibility score hangs on the harshest reading of one cell.**
- Commitment 5 reads "US: quarterly improvement, 'strong demand pull Q2 onwards'". It is scored MISSED, 0 points (REV l.612).
- Yet the same datum, exports +2.0% QoQ (CC l.145-146; PPT l.271), is booked as "confirming evidence" for US recovery in 6D (REV l.396). It also meets the "quarterly improvement" leg of the commitment.
- The review cannot separate US from total exports (Section D item 5, REV l.937).

Three readings, and the ratio under each:

| Reading of commitment 5 | Ratio |
|---|---|
| PARTIALLY DELIVERED | 2.0/3 = 66.7% |
| UNCLEAR (excluded) | 1.5/2 = 75% |
| MISSED (A4's choice) | 1.5/3 = 50% |

Only MISSED puts the ratio under the 60% line that triggers Grade C and OVERPROMISER (REV l.622, l.789, l.892-894). Those flags flow into the Key Notes payload (l.487) and the YAML flags (l.1149).

Commitment 1 at PARTIAL is generous in the other direction: MISSED would give 33%.

Fix: rescore commitment 5 and state the basis, or show the 33% to 75% sensitivity next to the 50%. If the score moves, carry the change to Grade, archetype, 8E and the Key Notes line.

**F1 (FACTUAL, A4; low severity). The data-centre "inconsistency" is not in the extract.**
- The review calls it an internal call inconsistency that the opening says approvals are "established" while the Q&A says they are "progressing" (REV l.571, l.944).
- Deck slide 22 reconciles the two: "Established approvals with leading data-centre developers" and "Approvals with other leading developers are progressing" (PPT l.336-339). The call follows the same split (CC l.118-121, l.489-492).
- Fix: drop the item from the Step 1 diagnostics and Section D item 12. Keep Q25 (REV l.472) as a request for numbers.

---

## VERDICT (loop 0)

**INCOMPLETE.**

| ID | Type | Agent | Exact gap |
|---|---|---|---|
| M1 | MISSING | A2 | Deck ledger lacks R523, R524, R525 (PPT l.425, l.426, l.453). The ledger header must read 525 |
| X1 | CONTRADICTION | A2, then A4 | A2 must re-flag T26, T37, T55, T40 and T46 as substantive. A4 must restate the substantive count from 27 to 32 (REV l.520) and re-anchor 4A row 9 to T26 |
| X2 | CONTRADICTION | A4 | The commitment 5 MISSED score conflicts with 6D's confirming evidence. Grade C and OVERPROMISER rest on the harshest of three readings |
| M2 | MISSING | A4 | Surviving ROCE pre-build counter is not grafted |
| M3 | MISSING | A4 | Surviving warrant-economics counter (mandatory probe) is not grafted |
| F1 | FACTUAL | A4 | The data-centre "inconsistency" is not supported by the extract (PPT l.336-339) |
| M4 | MISSING | A4 | RES-A3-01, CC-A3-12, PPT-A3-11 and PR-A3-06 are claimed as incorporated but have no body citation |

Loop order: A2 first (ledger patches only), then A4. A3 needs no re-run, because no new claim reaches A3. Arithmetic is clean: no A4 table number changes, except the X1 count and any X2 rescore.

---

## STYLE NOTES (logged; no re-run)

- S1 (A2). The results ledger header "ids_in_structured: 989" (LED-RES l.5) is stale against structured R001-R993 (RES-STR l.6). Add the cross-reference R990-R993 = M001-M004.
- S2 (A2). Concall ledger topic labels are wrong for two turns. T62 is the new-entrant competition question (CC l.505-511), not "margin profile". T79 is the US exports Rs 700-800 Cr question (CC l.593-594), not "funding capex" (LED-CC l.139, l.147).
- S3 (A4). The label "Operating EBIT (= W&C segment result)" (REV l.171) holds only for the FY27 columns. FY26 differs: SA 1.88 vs W&C 1.98, 13.51 vs 13.71, 50.57 vs 50.77 (RES l.691).
- S4 (A4). "no capex to date" (REV l.214, l.846) reads as zero spend, but capex paid is 41.30 (RES l.307) and CWIP is 3.59 (RES l.221). Write "no capex-to-date figure disclosed".
- S5 (A4). The 42.76 build is finished goods, WIP and scrap (RES l.166). It is not "finished goods" or "finished stock" (REV l.295, l.316, l.1002).
- S6 (A4). The brief says "the new entrant one analyst named" (REV l.1049). The analyst did not name it (CC l.506), and the review says so elsewhere (l.748, l.814, l.1054).
- S7 (A4). The forward-map bear fork "Start moves to H1 FY28 or later" (REV l.1069) does not mark a slip, because H1 FY28 contains the guided Q1 FY28. Write "Q2 FY28 or later".
- S8 (A4). "Family concentration: three Agarwals" (REV l.513) states a family link that the extract does not show. The deck spells the promoters "Aggarwal" (PPT l.486) and the CFO "Agarwal" (PPT l.500). Tag the claim as memory or [INFERENCE].
- S9 (A4). In "A one-off tariff refund will lift Q3 profit [MGMT]" (REV l.1007), the direction is inferred from garbled ASR (CC l.444-446). Tag it [INFERENCE]. The strip-it-out logic holds for either sign.
- S10 (A4). The sector brief says industry growth is not disclosed (REV l.1024). Deck slide 12 gives the India W&C market as $23.1bn (2026) to $35.6bn (2031), a 9.0% CAGR (PPT l.176-178; third-party sources l.193). Add it, tagged [MGMT citing third party].
- S11 (A4). Management said "substantial portion of this is the supply portion" about the HTLS book (CC l.384-385, ASR). The review leaves this qualifier out of 4A row 13 (l.656), Q19 (l.466) and the brief's model-drift lines (l.1036-1037).
- S12 (A4). The garbled soft statement "expects to have a positive cash flow" (CC l.237-238) is not cited. The Q5 bear answer "no commitment" (REV l.452) should cite it as untested.

---

Loop 0 YAML block (superseded by the loop 1 block at the end of this file):

```yaml
stage: A5-adversary
company: "PARACABLES"
quarter: "Q2 FY27"
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
    - "PPT R523: slide 28 depreciation H1 YoY 20.4% (PPT l.425)"
    - "PPT R524: slide 28 finance cost H1 YoY 85.3% (PPT l.426)"
    - "PPT R525: slide 30 investments FY26 dash (PPT l.453)"
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "ROCE 13.7% sits at the ~13% destination on file (REV l.360, l.409, l.423)"
    counter: "Pre-build base. About Rs 266.6 Cr of the Rs 300 Cr Narmadapuram plan enters capital employed before the plant earns (partial start Q1 FY28; 220 kV not major for two years). H1-annualised EBIT 133.58 over CE 1,051.97 + 266.6 = 1,318.6 gives about 10.1%. The destination match is a pre-capex reading."
    source_line: "PPT l.211; RES l.246, l.250, l.257, l.691; CC l.166, l.418"
    type: MISSING
  - claim: "Promoter warrant conversion is a bull fork and skin-in-the-game test (REV l.373, l.469, l.980, l.1070)"
    counter: "At the deck 30-Sep market cap Rs 1,845 Cr on 32,72,39,473 shares (Rs 56.4), the 72 lakh warrants at Rs 42 are Rs 14.4 in the money: about Rs 10.4 Cr intrinsic on Rs 7.56 Cr paid; conversion buys about Rs 40.6 Cr of stock for Rs 22.68 Cr. Conversion is rational arbitrage with little conviction signal; non-conversion is the informative outcome. Issue price = 21.3x FY26 EPS 1.97, 15.2x H1-annualised EPS 2.76, 1.49x post-issue book Rs 28.11. Land consideration NOT FOUND."
    source_line: "RES l.201, l.246, l.343-347, l.361; PPT l.139-144, l.548-550"
    type: MISSING
findings_by_type:
  factual:
    - "F1 (A4): data-centre approvals called an internal inconsistency (REV l.571, l.944); deck slide 22 reconciles established vs progressing (PPT l.336-339; CC l.118-121, l.489-492). Drop it from Step 1 diagnostics and Section D item 12."
  missing:
    - "M1 (A2): deck ledger lacks structured rows R523, R524, R525 (PPT-STR l.539-542; LED-PPT l.3-5). The count test grepped the structured file, not the fulltext (LED-PPT l.10)."
    - "M2 (A4): surviving ROCE pre-build counter not grafted into 6A, 6.5 Pillar 1 and 8A-W."
    - "M3 (A4): surviving warrant and stake-buy economics counter (mandatory probe) not grafted into watchlist #6, Q22 and the forward-map warrant row."
    - "M4 (A4): RES-A3-01, CC-A3-12, PPT-A3-11 and PR-A3-06 are claimed as incorporated (REV l.35-39, l.1088) but have no body citation."
  contradiction:
    - "X1 (A2 then A4): ledger flags T26, T37, T55 INTRO_TURN and T40, T46 ACK_ONLY (LED-CC l.123-136), but each holds a substantive question (CC l.288-291, l.342-344, l.436-437, l.368-369, l.403-405). A4 0C says 27 substantive (REV l.520) while its 4A covers 31 turns (REV l.644-673). The correct count is 32."
    - "X2 (A4): commitment 5 scored MISSED (REV l.612) while 6D books the same +2.0% QoQ exports as confirming evidence (REV l.396). PARTIAL gives 66.7% and UNCLEAR gives 75%; only MISSED gives the 50% that sets Grade C and OVERPROMISER (REV l.622, l.789, l.487, l.1149)."
  style:
    - "S1 (A2): results ledger header 989 stale vs R001-R993"
    - "S2 (A2): concall topic labels wrong for T62 and T79"
    - "S3 (A4): Operating EBIT = W&C segment label holds for FY27 columns only"
    - "S4 (A4): 'no capex to date' wording"
    - "S5 (A4): 42.76 is FG, WIP and scrap, not finished goods"
    - "S6 (A4): new entrant was not named by the analyst"
    - "S7 (A4): bear fork 'H1 FY28' should read 'Q2 FY28'"
    - "S8 (A4): family-concentration claim untagged; deck spellings differ"
    - "S9 (A4): Q3 refund direction needs an [INFERENCE] tag"
    - "S10 (A4): sector brief omits deck slide 12 market data"
    - "S11 (A4): HTLS 'substantial portion is supply' qualifier omitted"
    - "S12 (A4): soft 'positive cash flow' statement (CC l.237-238) not cited"
loop_back_to: "A2"
gap: "A2 first, then A4; A3 needs no re-run. A2: append deck rows R523-R525 (header 522 to 525) and re-flag concall T26, T37, T55, T40, T46 as substantive. A4: restate substantive turns from 27 to 32 and re-anchor 4A row 9 to T26 (CONTRADICTION); rescore commitment 5 or show the 33-75% credibility sensitivity, and carry it to Grade, archetype and the Key Notes payload (CONTRADICTION); graft the ROCE pre-build counter and the warrant-economics probe (MISSING); drop the data-centre inconsistency (FACTUAL); cite or mark RES-A3-01, CC-A3-12, PPT-A3-11, PR-A3-06 (MISSING)."
```

---

## RE-AUDIT (loop 1)

Scope. This re-audit covers correction loop iteration 1 of 1. I read the revised review's CORRECTION LOOP 1 LOG (REV l.1084-1096) and every section it names. I also read the revised deck and concall ledgers in full at the changed lines. I did not re-read the source or A3. Line numbers in this section refer to the revised files.

### R0. Deliverable completeness (re-check)
All five brief parts are still present and non-empty: narrative REV l.1004-1019 under its heading at l.1002 (16 lines, inside 10-20), sector l.1021-1033, business model l.1035-1051, competition l.1053-1064, forward map l.1066-1082. The changed brief lines (l.1017, l.1050, l.1080) carry real content. Gate: PASS.

### R1. Closure of loop 0 findings

| ID | Type | Closed? | Evidence in the revised files |
|---|---|---|---|
| M1 | MISSING (A2) | PARTIAL | Closed at row level. The header reads 525 of 525 (LED-PPT l.5). The count test reads 407 (l.10). R523-R525 sit in section 2 with the correct pages and lines (l.471-473), and R525 is in the ZERO_STANDING register (l.608). **Not closed in the section 1 slide index:** see the new item C1 below |
| X1 | CONTRADICTION (A2, A4) | YES | Concall ledger: T26, T37, T40, T46, T55 are re-flagged QUESTION_CONFIRMED with correct topics (LED-CC l.123-136). The count test reads 35 = 32 substantive + 3 ACK_ONLY (l.10). Review: preamble l.29 and 0C l.525 read 32. 4A row 9 is re-anchored to T26 and T28 (l.659). 4A has 30 rows covering 32 turns, and the grade tally (1+13+6+8+1+1 = 30) is unchanged |
| X2 | CONTRADICTION (A4) | YES | Commitment 5 is rescored PARTIALLY DELIVERED, with the basis, the MISSED reading and the separating observation (l.617-619). 3B now reads 1 delivered, 2 partial, 2 unclear, 2.0 points, 66.7% (l.625, l.629). The 33-75% sensitivity is stated (l.629). The change is carried to 3C, 3D, 6E, 8E, the Concall Verdict, the Key Notes payload, Section E, the brief and the YAML flags. A sweep for "OVERPROMISER", "Grade C" and "50%" finds them only inside the sensitivity statements (l.629, l.796, l.1017) |
| M2 | MISSING (A4) | YES | The ROCE pre-build counter is grafted at 6A l.363 and l.365, at 6.5 Pillar 1 l.414, at 8A-W l.428, in Key Notes l.492, in the brief l.1050 and in the YAML flag l.1178. Each place states the two readings and the observation that separates them |
| M3 | MISSING (A4) | YES | The stake-buy economics are grafted at 0C l.78, watchlist #6 l.378, Q22 l.474, 8F Q10 l.895, monitorable 13 l.989, the forward map l.1080 and the YAML flag l.1179. The land consideration and the pricing-date price are stated NOT FOUND |
| F1 | FACTUAL (A4) | YES | The claim is withdrawn at the Step 1 diagnostics (l.576) and Section D item 12 (l.953). The Q25 rationale is rebuilt as a request for numbers (l.477) |
| M4 | MISSING (A4) | YES | Each ID now has a body citation: RES-A3-01 at l.99; CC-A3-12 at l.12, l.576, l.942; PPT-A3-11 at l.919, l.956; PR-A3-06 at l.14, l.931, l.944. The index line is at l.40 |

### R2. Coverage (re-check of changed ledgers)

| Ledger | Check | Ledger value | My count | Status |
|---|---|---|---|---|
| Deck | IDs referenced at row level | 525 (LED-PPT l.5, l.17) | Structured R001-R525 | PASS |
| Deck | LAYOUT-flagged rows | 210 (l.16, l.619) | 210 row-level LAYOUT_ lines; the 211th grep hit is the file note at PPT-STR l.5 | PASS |
| Deck | ZERO_STANDING | 3 (l.15, l.606-608) | 3 | PASS |
| Deck | Slide 25 index row | "R156..R525 (24)" (l.49) | 24 rows; the last ID on slide 25 is R522 (p25 L374). R525 is a slide 30 row (LED-PPT l.473) | FAIL: C1 |
| Deck | Slide 28 index row | "R201..R514 (97)" (l.52) | 99 structured rows on page 28 (R201-R295, R513, R514, R523, R524) | FAIL: C1 |
| Deck | Slide 30 index row | "R346..R518 (44)" (l.54) | 45 structured rows on page 30 (44 plus R525) | FAIL: C1 |
| Concall | Analyst-turn flags | 32 substantive + 3 ACK_ONLY | 32 + 3 | PASS |
| Results, release | Unchanged in loop 1 | n/a | n/a | PASS (S1 still open) |

**C1 (CONTRADICTION, A2; new in loop 1, residual of M1).** Section 1 of the deck ledger disagrees with its own section 2 rows in three cells:
- Slide 25 range end reads R525. It should read R522, because R525 is on page 30 (l.473).
- Slide 28 reads 97 rows. It should read 99, adding R523 and R524.
- Slide 30 reads 44 rows. It should read 45, adding R525.

My loop 0 M1 fix asked for the slide 28 and slide 30 counts. The slide 25 error was introduced in loop 1.

Materiality: low. All 525 IDs are referenced at row level, and the coverage guarantee holds. Nothing in the review depends on the slide index, so A3 and A4 are unaffected.

Why it is not STYLE: the fix changes numbers and one row placement in the ledger, and the prompt says a finding that changes a number is never STYLE.

### R3. Arithmetic (new numbers in changed sections)

| Metric | A4 value (revised REV line) | Recomputed | Source line | Status |
|---|---|---|---|---|
| Issue price multiples | 21.3x / 15.2x / 14.2x; 1.49x book Rs 28.11 (l.78) | 42/1.97 = 21.32; 42/2.76 = 15.22; 42/2.96 = 14.19; 920.01/32.7239 = 28.11; 42/28.11 = 1.494 | RES l.201, l.246, l.361 | PASS |
| Warrant in-the-money value | Rs 56.4; Rs 14.4; ~Rs 10.4 Cr; ~Rs 40.6 Cr (l.78) | 1,845/32.7239 = 56.38; 14.38 x 0.72 Cr = 10.35; 56.38 x 0.72 = 40.59 | PPT l.548-550; RES l.345 | PASS |
| ROCE pre-build | 33.4; 266.6; 1,318.6; ~10.1% (l.365) | 3.59 + 29.8 = 33.4; 300 - 33.4 = 266.6; 1,051.97 + 266.6 = 1,318.6; 133.58/1,318.6 = 10.13% | RES l.221, l.228, l.246-257; PPT l.211 | PASS |
| Credibility after rescore | 2.0 points; 66.7%; 75% (UNCLEAR); 50% (MISSED); 33% (with commitment 1 also MISSED); 6.7 pp above the line (l.625, l.629) | (1.0+0.5+0.5)/3; (1.0+0.5)/2; 1.5/3; 1.0/3; 66.7 - 60 | REV l.613-617 | PASS |
| Exports QoQ basis | 158.1 vs 155.0, +2.0% (l.617) | 313.1 - 158.1 = 155.0; +2.00% | CC l.145-146; PPT l.271 | PASS |
| Concall revenue split | 402.3 + 158.1 = 560.4 (l.12, l.942) | 560.4 | CC l.145, l.153 | PASS |

Result: zero mismatches above rounding.

### R4. Adversarial read of the changed sections
- **New positive claim: "Grade B, matches B on file, no downgrade candidate" (l.629, l.639).**
  - Bear counter: the ratio sits 6.7 pp above the line on n = 3. One harsher score takes it to Grade C. US-only exports cannot be split from the total.
  - Does it survive? Yes, but A4 already carries it: the sensitivity, the separating observation and the "provisional" tag are at l.619, l.629, l.796 and l.1017. No graft needed.
- **Symmetry check on commitment 4.** It is scored DELIVERED (l.616) while its date leg is UNCLEAR. Commitment 5 failed one of its two legs. Commitment 4's open leg is not yet due. So the two scorings are consistent, and no finding arises.
- **New text that rests on inference.**
  - 0D note answer 2 says "the parent carries its two subsidiaries at nil (l.225)". RES l.225 is the non-current Investments line at 0.00, and it does not name the subsidiaries.
  - The same answer says "the next use of the exceptional line is most likely ... struck off".
  - Both are untagged inferences. Logged as S13. They change no number or conclusion.

### R5. Re-audit verdict

**INCOMPLETE.** One open non-STYLE item remains.

| ID | Type | Agent | Exact gap |
|---|---|---|---|
| C1 (residual of M1) | CONTRADICTION | A2 | Deck ledger section 1 slide index (LED-PPT l.49, l.52, l.54): slide 25 range end should read R522, not R525; slide 28 should read 99 rows, not 97; slide 30 should read 45 rows, not 44. Three cells. No effect on row-level coverage, A3 or A4 |

The loop cap is reached at iteration 1 of 1. Under the remediation cap, C1 goes to the operator as an open item. It is the only non-STYLE item left. M2, M3, X1, X2, F1 and M4 are closed.

### R6. Style notes (loop 1)
- S1 and S2 (A2) remain open. The results ledger header is stale, and the concall topic labels for T62 and T79 are still wrong (LED-CC l.139, l.147).
- S3 to S12 (A4) remain open and unchanged, because the loop log states no other section changed. Current lines: S5 at l.1011, S6 at l.1059, S7 at l.1079, S8 at l.518, S9 at l.1016, S10 at l.1033.
- S13 (A4, new). Tag the two inferences in 0D note answer 2 (REV l.99) as [INFERENCE]. These are the subsidiaries carried at nil and the next exceptional item expected at a shell strike-off.

```yaml
stage: A5-adversary
company: "PARACABLES"
quarter: "Q2 FY27"
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
surviving_bear_counters: []
loop0_closure:
  M1: "PARTIAL: R523-R525 referenced at row level and header 525 (LED-PPT l.5, l.471-473); slide index not refreshed (see C1)"
  X1: "CLOSED: 32 substantive turns in ledger (LED-CC l.10, l.123-136) and review (REV l.29, l.525, l.659)"
  X2: "CLOSED: commitment 5 rescored PARTIAL with basis and 33-75% sensitivity (REV l.617-629), carried to grade, archetype, payload and flags"
  M2: "CLOSED: ROCE pre-build counter grafted (REV l.363, l.365, l.414, l.428, l.492, l.1050)"
  M3: "CLOSED: stake-buy and warrant economics grafted (REV l.78, l.378, l.474, l.895, l.989, l.1080)"
  F1: "CLOSED: data-centre inconsistency withdrawn (REV l.576, l.953, l.477)"
  M4: "CLOSED: RES-A3-01, CC-A3-12, PPT-A3-11, PR-A3-06 cited in body (REV l.12, l.14, l.99, l.576, l.919, l.931, l.942, l.944, l.956)"
findings_by_type:
  factual: []
  missing: []
  contradiction:
    - "C1 (A2; residual of M1): deck ledger section 1 slide index disagrees with its section 2 rows. Slide 25 range ends R525, but R525 is a page 30 row; it should end R522 (LED-PPT l.49, l.473). Slide 28 shows 97 rows; structured page 28 has 99 with R523, R524 (l.52). Slide 30 shows 44 rows; structured page 30 has 45 with R525 (l.54). Row-level coverage holds; A3 and A4 unaffected."
  style:
    - "S1 (A2): results ledger header 989 stale vs R001-R993 (open)"
    - "S2 (A2): concall topic labels wrong for T62 and T79 (open)"
    - "S3-S12 (A4): open and unchanged from loop 0"
    - "S13 (A4, new): two untagged inferences in 0D note answer 2 (REV l.99)"
loop_back_to: "A2"
gap: "C1 only (CONTRADICTION, A2): in the deck ledger section 1, set slide 25 range end to R522, slide 28 count to 99 and slide 30 count to 45 (LED-PPT l.49, l.52, l.54). Three cells; row-level coverage of 525 IDs holds; A3 and A4 need no change. Loop cap reached (iteration 1 of 1): route to the operator as an open item."
style_notes:
  - "S1: add an R990-R993 = M001-M004 cross-reference and refresh the results ledger header"
  - "S2: fix the concall ledger topic labels for T62 (new-entrant competition) and T79 (US exports)"
  - "S3-S12: carried open from loop 0; see the STYLE NOTES section"
  - "S13: tag the subsidiaries-at-nil and next-exceptional-item statements in 0D note answer 2 (REV l.99) as [INFERENCE]"
analyst_note: "Loop 1 closed six of seven items in full. X1: the concall ledger and the review now read 32 substantive turns. X2: commitment 5 is rescored PARTIAL with its basis, the MISSED reading and the separating observation. The ratio is 66.7%, Grade B, with the 33-75% sensitivity carried to every dependent section. No Grade C or OVERPROMISER text remains outside the sensitivity lines. M2 and M3: both counters are grafted, and their arithmetic ties. F1 is withdrawn. M4: all four A3 IDs are cited. M1 is closed at row level: R523-R525 are referenced and the header reads 525. But the slide index was not refreshed, and the slide 25 range end now points at a slide 30 row. That residual is a three-cell bookkeeping fix. It changes no coverage result and nothing in the review. It does change numbers in the ledger, so the rules do not let me call it STYLE. The loop cap is reached, so it goes to the operator as the only open item."
```
