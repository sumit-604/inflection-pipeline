# A3 FORENSIC NOTES: Tatva Chintan Pharma Chem Limited (TATVA), Q2 FY27, doctype: results

Agent: A3 forensic notes | model: claude-opus-5-5 | run date: 2026-10-20
Inputs read: A1 structured (R001-R1090, 1,090 rows, 100%), A1 fulltext (653 lines, 100%), A2 ledger (457 lines, 100%), notion-brief.md sections 4, 7, 8 (memory, not evidence), companies/TATVA.md ACTIVE TRIPWIRES (memory, not evidence). No prior-quarter fulltext supplied. Source PDF and inputs/ not opened.
Units: Rs million as printed (x0.1 = Rs Cr). "Line" = A1 fulltext line number. All arithmetic is A3's own, from cited lines.

## 0. LEDGER RECONCILIATION (100%)

| Ledger section | Structured IDs | Read at fulltext line | Result |
|---|---|---|---|
| 0 Footing | all statement rows | 145-332, 447-620 | A2 footing re-performed on CFO, CFF, equity roll, EPS. Agrees except EPS rounding (A3-13). |
| 1 Notes | R1008-R1018, R1043-R1048 | 345-371, 633-643 | read verbatim |
| 1 Qualifiers | R977-R1007, R1019-R1042 | 37-643 | read; R1005/R1040 LABEL_ANOMALY confirmed |
| 2 Cons P&L | R029-R239 (+R1049-R1054) | 145-183 | read, all values match |
| 2 Cons BS | R244-R307 (+R1055-R1066) | 201-248 | read, all values match |
| 2 Cons CF | R310-R460 (+R1067-R1069) | 264-332 | read, all values match |
| 2 Note 5 table | R466-R495 | 362-366 | read; equals std P&L |
| 2 Std P&L | R508-R652 (+R1070-R1075) | 447-475 | read, all values match |
| 2 Std BS | R657-R716 (+R1076-R1087) | 492-537 | read, all values match |
| 2 Std CF | R719-R866 (+R1088-R1090) | 553-620 | read, all values match |
| 2 ZERO_STANDING | 29 lines, 69 cells | per register | each judged under F1 |
| 3 Other numbers | 67 rows | 19-650 | read |
| 4 Agenda | R006-R009, R876-R878, R920-R922 | 19-68 | read (F13) |
| 5 Annexures | none | - | none present |
| 6 Auditor paras | R012-R024, R497-R505, R880-R890, R925-R926, R954-R955, R980-R985, R1019-R1021 | 70-131, 383-433 | read (F4, F5, F14) |
| 7 Entities | R873-R916 | 23-651 | read (F15) |
| 8 Signatures | R010-R011, R023-R024, R503, R880, R889, R902, R906, R915, R923-R926, R953, R955, R976 | 60-652 | read |
| 9 Dates / Forward | R917-R976 | 19-652 | read (F6) |
| 10 Supplement | R1049-R1090 | 155-560 | read |

Rows read: 1,090 of 1,090. Orphans: none. Structured-vs-fulltext value mismatches found: 0.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R095-R100, R574-R579 | 158, 460; notes 345-371, 633-643 | "6 Exceptional items \| - \| 13.18 \| - \| 13.18 \| - \| -" | AMBIGUOUS | The Q1 charge of 13.18 (Rs 1.32 Cr) now sits in the H1 column too. It is identical in standalone and consolidated, so the parent booked it. Neither note set explains it. This is the second filing with no disclosure, and the Q1 question is still OPEN. Ask: nature, cash or non-cash, tax treatment, and recurrence. |
| A3-02 | F1 | R410-R412, R416, R292-R293, R248-R249 | 315, 317, 240, 203 | "Proceeds from long-term borrowings \| - \| - \| 60.40" / "Net proceeds from short-term borrowings \| 501.27" | FORWARD-SIGNAL | The long-term borrowing line is nil for H1. Short-term borrowings rose 1,153.63 to 1,655.30 (+501.67). Over the same H1, CWIP rose 233.48 to 428.27 (+194.79) and capex was 308.45. Short money now funds both the build and working capital. Expect a term-loan draw or a refinance (the AGM ceiling was raised to Rs 1,000 Cr, per memory). Ask about the funding mix and tenor for Dahej-III. |
| A3-03 | F2 | R125-R130, R484-R489 | 164, 365 | "9 Profit for the period/year (7-8) \| 214.51 \| 159.81 \| 99.17" vs "Net profit/(loss) after tax \| 153.87 \| 104.46 \| 89.41" | FORWARD-SIGNAL | The cons-minus-std PAT gap (subsidiaries plus eliminations) as % of std PAT: Q2 FY26 10.9%, Q1 FY27 53.0%, Q2 FY27 39.4%. That is +28.5pp YoY and -13.6pp QoQ, so both moves exceed 5pp. H1 FY27 44.9% vs H1 FY26 17.7%. Last year's gap was 24.94 in H1 FY26 but only 4.78 in H2 FY26 (FY26 29.72 less H1 24.94). Subsidiary profit is lumpy and has fallen at year end before. Ask whether a year-end transfer-pricing or URP true-up drove the H2 FY26 drop. |
| A3-04 | F2 | R508-R573, R1070-R1075 | 447-459 | "5 Profit before exceptional items and tax (3-4) \| 204.37 \| 154.12 \| 123.43" | FORWARD-SIGNAL | Parent operating EBITDA (PBT pre-exc + finance + D&A - other income): Q2 FY26 18.22%, Q1 FY27 16.38%, Q2 FY27 15.05%. H1 FY27 15.60% vs H1 FY26 16.08%. Group Q2 is 18.72%. The group margin holds only through the subsidiaries, while the manufacturing entity's margin falls 3 quarters running. Parent gross margin was 47.3% in Q2 vs 54.7% in Q1. The Q1 parent FG/WIP build of 389.35 flattered Q1. |
| A3-05 | F2 | R035-R040, R514-R519 | 146, 448 | "2 Other income \| 27.05 \| 40.33 \| 7.94 \| 67.38 \| 21.63" (std) vs "17.54 \| 27.80 \| 10.08 \| 45.34 \| 21.63" (cons) | AMBIGUOUS | Std other income exceeds cons by 9.51 in Q2, 12.53 in Q1 and 22.04 in H1 FY27. The two were equal in H1 FY26 (21.63 each). Consolidation eliminates a new intra-group income stream in FY27, which could be interest, commission, a dividend from a subsidiary, or FX on intercompany balances. The parent's reported profit includes it. Ask what it is and whether it is contractual. |
| A3-06 | F3 | R047-R082 vs R526-R561, R053-R058 vs R532-R537, R262-R263 vs R675-R676, R1065-R1066 vs R1086-R1087 | 149-154 vs 451-456; 150 vs 452; 215 vs 506; 244 vs 533 | "Employee benefits expense \| 182.29" (cons) vs "182.30" (std); "Purchases of stock-in-trade \| - \| -" (std) | AMBIGUOUS | The cons-minus-std differences are: materials -0.01, employee cost -0.01, finance cost 0.00, D&A +0.02 (Q2), borrowings identical. So the US and EU subsidiaries have no plant, no payroll and no debt. They are trading entities: third-party purchases 20.43, other expenses 34.50, inventory 245.02 and cash 53.31 at 30-Sep. Yet they earn 28.3% of Q2 and 31.0% of H1 group PAT. Intercompany proxies: std receivables exceed cons by 104.94 at Sep (246.88 at Mar). Std other current liabilities exceed cons by 168.94 at Sep (161.67 at Mar), which could be advances from the subsidiaries. There is no going-concern or EoM paragraph, so this is about profit location, not cleanup. Ask about the subsidiaries' substance, the transfer-pricing method, and the intercompany debtor days (memory sub-trigger: >90 days). |
| A3-07 | F8 | R256-R257, R669-R670, R586-R597, R113-R118 | 209, 500, 463, 464 | "Deferred tax assets (net) \| 7.65 \| 81.68"; "Current tax \| 17.69 \| - \|" | FORWARD-SIGNAL | P&L ETR is normal (cons H1 25.21%, std H1 25.19%, statutory 25.17%). But deferred tax is a persistent charge: std H1 deferred 69.29 = 79.7% of std tax, std Q1 current tax nil. Std DTA fell 81.68 to 7.65 (-74.03) and cons DTA 95.67 to 19.21. The cash shield was 2,007 bps of std H1 PBT (1,433 bps cons). At ~35/qtr the residual 7.65 runs out in Q3 FY27. From then, cash tax rises by about 35 per quarter with no change in P&L ETR. This is a CFO headwind at a time CFO is negative. |
| A3-08 | F13 | R008-R010, R922, R1008 | 50, 41, 60 | "The Meeting commenced at 11:30 A.M. and concluded at 03:45 P.M." | AMBIGUOUS | 4 h 15 min against one disclosed item, results approval. Line 41 says Audit Committee and Board met "in their respective meetings held on 19 October 2026", which explains part of the time. The letter shows no AR, AGM, dividend, director, auditor or fund-raise item. The CS signed at 15:48:12 (line 60). Context outside the filing (task message): the earnings call was cancelled 56 min before its start. Ask whether the board discussed any matter not disclosed under Reg 30. |
| A3-09 | F14 | R407-R409 vs R816-R818; R355 vs R764; R298-R299 vs R707-R708 | 314, 603, 282, 571, 243, 532 | "Dividend paid \| (46.78)" (cons) vs "Dividend paid \| (8.55)" (std); "(19.71)" vs "(57.95)" | AMBIGUOUS | Both equity rolls deduct the full dividend (cons 46.78, std 46.79 = Rs 2/share x 23.392 mn). The parent is the only payer, because the subsidiaries are wholly owned. Std "other current financial liabilities" change is (57.95) vs cons (19.71). The difference is 38.24, which matches the dividend gap of 38.23, and the balance-sheet line is identical in both (92.81 / 126.75). So the same outflow sits in financing (cons) and in operating (std). Read on cons classification, std CFO is -47.46, not -85.70. Bear read: if the std treatment is right, cons CFO is -75.00, not -36.76. Ask which classification is correct and what the 38.24 is (unpaid dividend account, TDS on dividend, or other). |
| A3-10 | F14 | R1018, R1048, R376-R378 | 371, 643, 289 | "Figures for the previous periods/year have been reclassified/rearranged/regrouped"; "(36.76) \| 133.81 \| 314.89" | AMBIGUOUS | The reclassification notes give no amounts and no lines. The FY26 audited column shows cons CFO 314.89 (74.9% of PAT 420.54). Memory holds "FY26 CFO ~Rs 35 Cr, 83% of PAT", about 349. The ~34 gap could be a reclassification or a memory basis difference. Verify against the FY26 AR cash flow before the CFO trend is used. Ask which prior-period lines moved and by how much. |
| A3-11 | F14 | R1009, R1044, R983, R985, R1021 | 350-351, 635, 98, 115, 413 | "who has expressed an unmodified opinion" vs "Accordingly, we do not express an audit opinion." | NEUTRAL-FACT | The notes call a limited-review conclusion an "opinion" in both entities. Common boilerplate, individually immaterial, logged as a governance data point. |
| A3-12 | F14 | R428-R430, R837-R839, R1005, R1040, R431, R466, R1014 | 321, 610, 322, 362 vs 447/449 | "Net decrease in cash and cash equivalents D=(A+B+C) \| 49.52"; "Total income from operations (Net) \| 2,074.84" | NEUTRAL-FACT | The "Net decrease" caption sits on positive values (cons 49.52 and 13.37, std 38.79). The half-year statement uses "beginning of the year" captions. Note 5 labels std revenue (2,074.84, line 447) as "Total income", while std total income is 2,101.89 (line 449). These are drafting lapses. |
| A3-13 | F14 | R634, R638, R641, R645 | 472, 473 | "Basic \| 6.57 \| 4.47 \| 3.82 \| 11.04 \| 6.01 \| 16.71" | NEUTRAL-FACT | Std Q2 PAT 153.87 / 23.392 mn = 6.578 (rounds to 6.58), and H1 FY26 140.74 / 23.392 = 6.017 (rounds to 6.02). The cons EPS rounds normally, e.g. 4.2395 prints 4.24. The cause is either truncation in the std statement or an A1 transcription error, since page 10 was transcribed by hand. Re-verify the two cells against the page image. Immaterial. |

## 2. CHECKLIST SCORECARD

| Check | Status | Basis (one line) |
|---|---|---|
| F1 Zero-value standing items | FINDING | 29 lines judged. NCI lines (173, 176, 179, 229) are template lines for wholly-owned subsidiaries. Std purchases of stock-in-trade nil (452) feeds F3. Std Q1 current tax nil (463) feeds F8. Grant, investment, cash-credit and dividend nils are timing. Findings: exceptional item (A3-01) and long-term borrowing nil vs short-term surge (A3-02). |
| F2 S vs C decomposition | FINDING | Revenue gap Q2 98.36 / Q1 203.53 / Q2 FY26 76.53. PBT gap Q2 85.03 = revenue +98.36, other income -9.51, purchases +20.43, inventory change -51.11, other expenses +34.50. PAT gap %std PAT moved +28.5pp YoY and -13.6pp QoQ (A3-03, A3-04, A3-05). |
| F3 Shell-entity detection | FINDING | Materials, employee cost, finance cost and borrowings are identical, and D&A is within 0.02. The subsidiaries are non-manufacturing trading entities with 28-31% of group PAT. No GC/EoM to reconcile (A3-06). |
| F4 Unaudited contribution | PASS | Cons review report para 5 (lines 103-107) lists all 3 entities. There is no Other Matter paragraph, no component auditor and no management-certified entity, so the unreviewed contribution is Rs 0 / 0% of PAT. No prior-quarter trend possible. |
| F5 Going concern / EoM scope | PASS | No EoM, GC or Other Matter in either report (paras 115-121, 413-418). Both conclusions are unmodified. No prior-quarter extract to verbatim-diff. Re-test next quarter. |
| F6 Forward-commitment mining | PASS | The lexicon sweep found "shall be" (47, 368, 641, website availability only), "commenc" (50, meeting time) and "has been" (347, 350, 633, review/approval done). No business commitment in the notes. 3 administrative rows registered. |
| F7 Hedge mining | PASS | No hedge phrase in the notes. "subjected to limited review" (350, 635) is not a hedge. "might be identified" (97, 410) is auditor SRE 2410 boilerplate. |
| F8 Tax forensics | FINDING | ETR cons Q2 25.88 / Q1 24.30 / Q2 FY26 27.42 / H1 25.21 / FY26 26.23%; std Q2 24.71 / Q1 25.88 / H1 25.19%. No earlier-years line. Persistent deferred charges are running the DTA down to 7.65, so cash tax steps up (A3-07). |
| F9 OCI forensics | PASS | Actuarial (line 166): Q2 0.62, Q1 0.61, H1 1.23 vs FY26 2.45. No single quarter exceeds the prior full year. The reclassifiable FCTR line (168) is 4.11 / (3.65), inside FY26 30.46. |
| F10 Share count / dilution | PASS | Paid-up 233.92 in every period (183, 474). Basic = diluted in every period, both entities, so the spread is nil. Rounding note logged as A3-13. |
| F11 Net worth tie-out | PASS | Cons 233.92 + 7,912.59 = 8,146.51 (226-230). Std 233.92 + 7,560.83 = 7,794.75 (517-519). FY26 other equity ties to the P&L line (184, 475). No revaluation reserve and no NCI. No third-party net worth figure in context to reconcile. |
| F12 Segment forensics | PASS | Single reportable segment, specialty chemicals (357, 639). No segment assets or liabilities are published. Product-line splits exist only in the deck. |
| F13 Board outcome | FINDING | Results was the only agenda item, with no AR, AGM, record date, director term or enabling resolution. The 4 h 15 min meeting has no explained driver (A3-08). |
| F14 Drafting inconsistencies | FINDING | Dividend CF classification split (A3-09), unquantified reclassification (A3-10), "opinion" vs "conclusion" (A3-11), captions and Note 5 label (A3-12), std EPS rounding (A3-13). The R1035 heading difference (552 vs 263) is trivial. |
| F15 Entity list diffs | PASS | 3 entities: holding, Tatva Chintan USA Inc. (WOS), Tatva Chintan Europe B.V. (WOS) (105-107). No change is detectable inside the filing. No prior-quarter extract, so A4 should confirm against the FY26 AR list. |
| F16 Presentation disclosures | N.A. | Results doctype. |
| F17 Concall silence audit | N.A. | Results doctype, and no transcript exists. Per the task message (not a filed line), the 19-Oct call was cancelled, so all 8 checklist items went unanswered by management this quarter. The filed numbers for each item are in section 4. |

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| Results information made available on company website | on filing, 19 Oct 2026 | cover letter, line 47 | initiated |
| Consolidated results available on BSE, NSE and company website | on filing, 19 Oct 2026 | cons Note 6, line 368 | initiated |
| Standalone results available on BSE, NSE and company website | on filing, 19 Oct 2026 | std Note 5, line 641 | initiated |

There is no business, capex, product or funding commitment anywhere in the filing.

## 4. MONITORING-CHECKLIST NUMERIC READOUT (filed numbers only; tests from memory; A3 does not grade the thesis)

| Test (memory) | Filed arithmetic (lines) | Value | vs memory line |
|---|---|---|---|
| H1 CFO (trigger a) | cons CFO (289) | -36.76 (H1 FY26 +133.81) | negative on revenue +59.9% YoY H1 (145) |
| CFO / EBITDA | -36.76 / 729.85 | -5.0% cons; std -15.5% (-85.70 / 552.58) | bear band <30% |
| Cash before tax | line 287 | 7.37 = 1.0% of EBITDA; WC absorbed 727.30 = 99.0% of pre-WC profit 734.67 | - |
| FCF | CFO - capex (289, 291) | -345.21; funded by short-term debt +501.27 (317) | - |
| Receivable days, cons | 1,783.77 (215) | H1 basis 84.9 d; TTM basis (TTM rev 6,498.53) 100.2 d; Q2 annualised 74.9 d; 31-Mar 85.9 d | far below 185; at or above 100 on TTM only |
| Receivable days, std | 1,888.71 (506) | H1 basis 97.6 d; TTM (6,254.39) 110.2 d; Q2 annualised 83.1 d; 31-Mar 105.7 d | below 185; above 100 on TTM |
| Trigger (a) arithmetic | - | CFO<0 yes; revenue rising yes; days >185 no | depends on operator ruling 50 (185 vs 90/100) |
| EBITDA margin, cons | (PBT pre-exc + fin + D&A - OI) / rev | Q2 18.72%, Q1 19.33%, H1 18.99%, Q2 FY26 17.99%, FY26 18.42% | below 20-22% band for 2nd quarter; above 18% red |
| Gross margin, cons | rev - (materials + purchases + inventory change) | Q2 51.1%, Q1 54.9%, H1 52.8% vs H1 FY26 52.9%; H1 FG/WIP build credit 413.60 (151) | margin leans on the inventory build |
| Net debt / EBITDA | (1,655.30 + 44.65 - 106.79 - 45.26) / TTM EBITDA 1,265.98 | 1,547.90 / 1,265.98 = 1.22x (31-Mar 1.20x) | above 0.65x |
| Standalone PBT | line 461 | Q2 204.37 (Rs 20.4 Cr); H1 345.31 | above Rs 5-10 Cr |
| Parent share of group PAT | 365 / 164 | Q2 71.7%, Q1 65.4%, H1 69.0% (FY26 92.9%) | above 50% |
| Q1 exceptional 13.18 | 158, 460 | still no note | OPEN (A3-01) |
| Annualised ROCE (A3 basis: EBIT / (equity + debt - cash)) | (513.69 + 47.90) x 2 / 9,694.41 | 11.6% H1 annualised | above 8% floor (basis differs from memory) |

## 5. A4 HAND-OFF (questions from FORWARD-SIGNAL and AMBIGUOUS findings)
A3-01 exceptional nature; A3-02 funding mix and tenor; A3-03 H2 true-up risk in subsidiary profit; A3-04 driver of the parent margin decline; A3-05 intra-group other income; A3-06 subsidiary substance, transfer pricing, intercompany debtor days; A3-07 cash-tax step-up timing; A3-08 undisclosed board matters and the call cancellation; A3-09 dividend CF classification; A3-10 reclassification amounts. The call was cancelled, so all of these go by IR email or to the rescheduled call.

```yaml
stage: A3-forensics
company: "TATVA"
quarter: "Q2 FY27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/tatva-q2fy27/work/forensics_results_tatva_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: PASS
  F5: PASS
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: PASS
  F12: PASS
  F13: FINDING
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "158, 460", classification: "AMBIGUOUS", implication: "Q1 exceptional charge 13.18 booked by parent, still no note in second filing; nature, cash, tax, recurrence unknown"}
  - {id: "A3-02", check: "F1", line: "315, 317, 240, 203", classification: "FORWARD-SIGNAL", implication: "LT borrowing nil in H1 while ST debt +501.67 and CWIP +194.79; capex and WC funded short, term-loan draw or refinance expected"}
  - {id: "A3-03", check: "F2", line: "164, 365", classification: "FORWARD-SIGNAL", implication: "Cons-minus-std PAT gap 10.9% to 39.4% of std PAT YoY (+28.5pp), 53.0% to 39.4% QoQ; gap fell to 4.78 in H2 FY26, year-end true-up risk"}
  - {id: "A3-04", check: "F2", line: "447-459", classification: "FORWARD-SIGNAL", implication: "Parent EBITDA margin 18.22% to 16.38% to 15.05% over 3 quarters while group holds 18.72% via subsidiaries"}
  - {id: "A3-05", check: "F2", line: "146, 448", classification: "AMBIGUOUS", implication: "Std other income exceeds cons by 22.04 in H1 FY27 vs nil in H1 FY26; new intra-group income in parent profit"}
  - {id: "A3-06", check: "F3", line: "149-154, 451-456, 452, 215, 506, 244, 533", classification: "AMBIGUOUS", implication: "Subsidiaries have no materials, payroll or debt yet earn 28.3% Q2 / 31.0% H1 of group PAT; intercompany receivable and liability proxies 104.94 and 168.94"}
  - {id: "A3-07", check: "F8", line: "209, 500, 463, 464", classification: "FORWARD-SIGNAL", implication: "Std DTA 81.68 to 7.65; deferred tax 79.7% of std H1 tax; shield exhausts Q3 FY27, cash tax up about 35 per quarter"}
  - {id: "A3-08", check: "F13", line: "50, 41, 60", classification: "AMBIGUOUS", implication: "4h15m meeting with results as only disclosed item; call cancelled after filing (external context)"}
  - {id: "A3-09", check: "F14", line: "314, 603, 282, 571, 243, 532", classification: "AMBIGUOUS", implication: "Dividend 38.24 sits in financing (cons) and operating (std); std CFO -47.46 on cons basis; bear read cons CFO -75.00"}
  - {id: "A3-10", check: "F14", line: "371, 643, 289", classification: "AMBIGUOUS", implication: "Reclassification unquantified; FY26 column CFO 314.89 vs memory ~349; verify at FY26 AR before trending CFO"}
  - {id: "A3-11", check: "F14", line: "350-351, 635, 98", classification: "NEUTRAL-FACT", implication: "Notes call a limited-review conclusion an opinion; drafting data point"}
  - {id: "A3-12", check: "F14", line: "321, 610, 322, 362", classification: "NEUTRAL-FACT", implication: "Net decrease caption on positive values; year captions in half-year statement; Note 5 labels revenue as total income"}
  - {id: "A3-13", check: "F14", line: "472, 473", classification: "NEUTRAL-FACT", implication: "Std EPS 6.57 and 6.01 vs computed 6.578 and 6.017; truncation or transcription, re-verify page 10 image"}
forward_signals: ["A3-02", "A3-03", "A3-04", "A3-07"]
ambiguous: ["A3-01", "A3-05", "A3-06", "A3-08", "A3-09", "A3-10"]
commitments:
  - {commitment: "Results information on company website", implied_date: "2026-10-19", ref: "cover letter line 47", status_word: "initiated"}
  - {commitment: "Consolidated results on BSE, NSE, company website", implied_date: "2026-10-19", ref: "cons Note 6 line 368", status_word: "initiated"}
  - {commitment: "Standalone results on BSE, NSE, company website", implied_date: "2026-10-19", ref: "std Note 5 line 641", status_word: "initiated"}
gate_a3: pass
blank_checks: []
analyst_note: "Cash is the main message. Group H1 CFO is -36.76 on revenue +59.9%. Working capital absorbed 99% of pre-WC operating profit, funded by +501.27 short-term debt. Receivable days are 85-100, far under the 185 line, so trigger (a) turns on operator ruling 50, not on the arithmetic. Two items can move the CFO read: the 38.24 dividend classification split (A3-09; bear read cons CFO -75.00) and the unquantified reclassification (A3-10). Profit quality: subsidiaries with no staff, plant or debt now earn 28-31% of group PAT, while parent EBITDA margin fell to 15.1%. The subsidiary gap fell to 4.78 in H2 FY26, so a year-end true-up is a live risk. Cash tax steps up from Q3: standalone DTA is down to 7.65. The 19-Oct call was cancelled (task message, not a filed line), so no checklist item got a management answer; A4 should treat all eight as unanswered. Pages 2-8 and 10-14 are manual image transcriptions; A3-13 is the one cell to re-verify."
```
