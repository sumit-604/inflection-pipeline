# A3 FORENSIC NOTES — United Foodbrands Limited (UFBL) — Q1 FY27 — doctype: PRESENTATION

Source extract: `extract_presentation_ufbl_q1fy27.txt` (39 slides / 1,205 lines)
Ledger reconciled: `ledger_presentation_ufbl_q1fy27.md` — 100% of rows read at cited lines
(39 slide rows + 17 P&L line items + 37 balance-sheet line items + 11 footnotes + 8 zero-standing items).
No prior-quarter ledger supplied (`NO_PRIOR_LEDGER`); no prior thesis / Notion checklist (NEW uncovered name).
Every number in this deck is CONSOLIDATED, without adjustment for minority interest of Red Apple Kitchen
Consultancy, Blue Planet Foods and Willow Gourmet (disclaimer, lines 92-95).

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A1 | F1 | T2 asset row 24 / T4 #2 | 1022 (slide 32) | "Investments — 121" (Mar-26 dash, Mar-25 121) | AMBIGUOUS | ₹121 Mn non-current investment fully exited/written off/reclassified in FY26. No cash-flow or note in a deck; ask where it went and whether a gain/loss hit the P&L. |
| A2 | F1 | T4 #8 | 444-467 (slide 16) | "Qualitative feedback is converted into quantitative index across restaurants" | AMBIGUOUS | An entire slide is framed on Guest Satisfaction Index yet the GSI number itself is never disclosed. Named-metric-with-no-value is a "dog that didn't bark"; ask for the score and its trend. |
| A3 | F6 | T1 slide 4 | 122 (slide 4) | "Plan to reach 400–425 by FY30" | FORWARD-SIGNAL | Dated store-count commitment: 266 today -> 400-425 by FY30 = ~134-159 net new stores over ~4 years (~34-40% growth off base). Trackable promise for Role 5; funding/ capex implications (see A10, A1). |
| A4 | F6 | T1 slide 38 | 1197 (slide 38) | "Operating leverage expected to drive profitability as scale increases" | FORWARD-SIGNAL | Management explicitly pins future profitability on operating leverage, i.e. it is NOT there yet (FY26 PBT was (683) Mn). Sets a testable margin-expansion expectation. |
| A5 | F7 | T3 #6 / T1 slide 29 | 275 (slide 10), 900 (slide 29) | "temporary GCC inflationary pressures"; "Resilient performance amid macro headwinds" | AMBIGUOUS | International gross margin fell 320 bps YoY (72.8%->69.6%) and ROM 24.4%->18.7% QoQ; management pre-labels the hit "temporary" and excludes it from the unit-economics table. Ask whether Q2 GCC margin has recovered. |
| A6 | F8 | T2 P&L rows 10-12 / BS row 27 | 993 (slide 31), 1025 (slide 32) | "TAX EXPENSE ... 1 ... (3)"; "Deferred tax assets (net) 596" | FORWARD-SIGNAL | Q1FY27 ETR ~4.2% on PBT 24 vs 25.17% statutory (~21 pp shield); FY25/FY26 carried tax credits on losses. ₹596 Mn net DTA + accumulated losses (Other equity 3,431->2,908) mean ETR steps up toward statutory once profits scale = future EPS drag not visible in "adjusted" optics. |
| A7 | F14 | T1 slide 12 / T2 sub-head | 314 (slide 12), 998 (slide 31) | "Cumulative App Downloads (IN ₹ MN)"; "ADJUSTED PROFITABILIY *" | NEUTRAL-FACT | App-download count mislabelled as currency (₹ Mn); "PROFITABILIY" misspelled. Individually immaterial; cumulatively a deck-QC / drafting-discipline data point on a first-covered name. |
| A8 | F16 | T1 slide 24 vs slides 5/25 | 748 (slide 24), 133 (slide 5), 786 (slide 25) | slide 24 chart: "...FY26 [28.7%] Q1FY27 [4.7%]"; slide 5: "28.7% In Q1FY27"; slide 25: "+28.7%" | AMBIGUOUS | **Internal contradiction.** The prominent headline "SSSG 28.7% in Q1FY27" (slides 4/5/25) conflicts with the 12-year SSSG chart (slide 24) which puts 28.7% against FY26 and shows Q1FY27 SSSG at only 4.7%. Either the headline is against a depressed Q1FY26 base (SSSG then -3.4%) while the chart uses a normalised base, or a chart mis-map. Reconcile the two bases before trusting the 28.7% growth story. |
| A9 | F16 | T1 slides 4/5/6/7 | 111, 144, 179 | "Q1 FY27 annualized revenue of ₹17,036 Mn" | AMBIGUOUS | Headline scale is a single weak-then-strong quarter x4 (4,259 x 4 = 17,036), presented as run-rate on the cover, glance, segment and evolution slides. Annualising the strongest quarter flatters vs FY26 reported revenue of 13,387 Mn. |
| A10 | F16 | T3 #4/#5/#6 | 153, 274, 275 | "*BBQ International unit economics are based on H2 FY26, excluding temporary GCC inflationary pressures in Q1 FY27" | AMBIGUOUS | Unit-economics table mixes bases: BBQ India & Premium CDR on "Q1FY27 matured portfolio", but International on H2FY26 with a current headwind stripped out. Non-uniform, matured-only, headwind-excluded basis flatters the returns/payback grid the equity story rests on. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | Basis (one line) |
|---|---|---|
| F1 ZERO-VALUE STANDING ITEMS | FINDING | Investments 121->nil with no explanation (line 1022, A1); GSI slide with no GSI value (444-467, A2). Deferred-tax-liab nil->3 (1024) and margin-row blank YoY% cells are benign sign-flip artifacts. |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Deck is consolidated-only (lines 92-95); no standalone column exists to decompose. |
| F3 SHELL-ENTITY DETECTION | N.A. | No standalone vs consolidated cost lines in a presentation; cannot compare. NCI 82->110 (line 1016) is the only minority footprint. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor "Other Matters" paragraph in an investor deck. |
| F5 GOING CONCERN / EoM SCOPE | N.A. | No auditor EoM / going-concern paragraph in a presentation; no prior deck to diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | Dated store-count commitment "400-425 by FY30" (122, A3); "operating leverage expected to drive profitability" (1197, A4). |
| F7 HEDGE PHRASE MINING | FINDING | International margin pre-hedged "temporary" / "resilient amid macro headwinds" (275, 900, A5). Base FLS disclaimer (74-90) is boilerplate. |
| F8 TAX FORENSICS | FINDING | ETR ~4.2% vs 25.17% statutory; ₹596 Mn DTA; persistent loss-period tax credits => future ETR step-up (993, 1025, A6). |
| F9 OCI FORENSICS | N.A. | Deck P&L stops at PAT; no OCI / actuarial line disclosed. |
| F10 SHARE COUNT & DILUTION | PASS | Equity share capital flat 195/195 (line 1014); no EPS or warrant/ESOP count carried. Non-cash ESOP add-back (1005) signals a live pool but no share-count change this period. |
| F11 RESERVES / NET WORTH TIE-OUT | PASS | Other equity + share capital + NCI = Total equity: Mar-26 2,908+195+110=3,213 (ties); Mar-25 3,431+195+82=3,708 vs 3,709 (₹1 Mn rounding). No third-party number to reconcile. |
| F12 SEGMENT FORENSICS | N.A. | Deck gives segment revenue/network/ROM but no segment assets/liabilities; the asset-vs-liability accretion test cannot be run. |
| F13 BOARD OUTCOME BEYOND RESULTS | N.A. | Investor deck carries no board-meeting outcome, AGM notice, or director term/appointment dates (slide 34 lists board with no DIN/dates). |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Unit-label anomaly "App Downloads (IN ₹ MN)" (314) and "ADJUSTED PROFITABILIY" typo (998); cumulatively a QC data point (A7). |
| F15 ENTITY LIST DIFFS | N.A. | No prior-quarter consolidation list supplied (`NO_PRIOR_LEDGER`); three minority entities named (92-93) cannot be diffed. Open item flagged for A4. |
| F16 DROPPED / REFRAMED DISCLOSURES | FINDING | SSSG 28.7% vs 4.7% Q1FY27 contradiction (A8); annualised single-quarter run-rate framing (A9); non-uniform matured/H2FY26 unit-economics basis (A10). Dropped-slide diff not possible without prior deck. |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype is presentation, not transcript; no prior monitoring checklist exists (new name). |

Status count: FINDING x6 (F1, F6, F7, F8, F14, F16); PASS x2 (F10, F11); N.A. x9 (F2, F3, F4, F5, F9, F12, F13, F15, F17). No blanks — GATE A3 pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | slide/line ref | status word |
|---|---|---|---|
| Reach 400-425 restaurants (from 266) | FY30 | slide 4 / line 122 | planned ("Plan to") |
| Operating leverage to drive profitability as scale increases | undated | slide 38 / line 1197 | expected |
| (context, third-party) AMC households to double | 10-12 years | slide 14 / line 392 | market projection — NOT a company commitment |

---

## NOTES FOR A4 (management-question seeds)

- **Priority (A8):** Force a reconciliation of the two Q1FY27 SSSG figures — 28.7% (headline, slides 5/25) vs 4.7% (12-year chart, slide 24, where 28.7% is tagged to FY26). Which base is each measured against, and what is the true like-for-like Q1FY27 SSSG?
- **A10 / A5:** Why are International unit economics shown on an H2FY26 basis with Q1FY27 GCC inflation excluded, while the other two segments use Q1FY27? Has GCC margin recovered in Q2?
- **A1:** What happened to the ₹121 Mn non-current Investments that went to nil, and did it produce a P&L item?
- **A6:** At what run-rate profitability does the ₹596 Mn DTA start unwinding and ETR normalise toward 25%?
- **A2:** Disclose the GSI score and its trend.
- Open item carried from A2: obtain the Q4 FY26 / Q1 FY26 UFBL deck and run the F15/F16 dropped-slide + entity-list diff.
