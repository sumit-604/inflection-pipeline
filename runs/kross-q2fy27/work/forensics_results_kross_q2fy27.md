# FORENSICS (doctype: results) KROSS Q2 FY27 — Kross Limited, standalone, Rs Millions
Agent: A3 forensic notes | model claude-opus-5-5 | date 2026-10-19
Inputs read: A1 structured (runs/kross-q2fy27/extracted/kross-results-q2fy27-structured.md), A1 fulltext (runs/kross-q2fy27/extracted/kross-results-q2fy27-fulltext.md), A2 ledger (runs/kross-q2fy27/work/ledger_results_kross_q2fy27.md), Notion transcription (runs/kross-q2fy27/work/notion-thesis.md, memory not evidence). Prior-quarter fulltext: none supplied. Source PDF and inputs/ not opened.
Line numbers below are A1 fulltext lines (L###). Pages 4, 6, 7 cite the image transcription (L410-519); the corrupted text layer (L152-405) is not used for values.

## 0. LEDGER RECONCILIATION
- Ledger IDs: 372 (R001-R372). Rows read at cited line: 372. Reconciled: 100%.
- R001-R068 checked one by one against the cited fulltext line (identity, dates, notes, auditor paragraphs, qualifiers): all present at the cited line. R035 partner name sits at L129 (garbled "Abhishek Agarv'nll"), "Partner" at the cited L130: no impact.
- R008-R027, R030 (SUPERSEDED): text-layer values compared with image rows R069/R159/R183/R189/R212/R283; image rows govern. R068 RESOLVED accepted.
- R069-R372 read at L412-L519: every structured value matches its transcription line.
- Ledger section 9 question (FOOTING_GAP H1 vs Q1+Q2): answered at F14-01.

## 1. FINDINGS TABLE
| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|--|--|--|--|--|--|--|
| F1-01 | F1 | R289, R290, R233, R234, R307 | L478, L448, L487 | "Allowances for expected credit loss :: - \| -" | AMBIGUOUS | Trade receivables rose to 2,062.91 (L448) from 1,971.69. They are 28% of total assets (7,355.04, L454). Neither half carries an ECL charge. The line exists for credit-loss provisioning that has not been booked. A future ageing-driven ECL charge would fall straight into PAT. Ask for receivables ageing and the balance-sheet ECL allowance. |
| F1-02 | F1 | R347, R348, R345, R253, R254, R263, R264, R349 | L507, L506, L458, L463, L508 | "Repayment of Long-term borrowings :: - \| -27.65" | AMBIGUOUS | H1 FY27 shows zero term-loan repayment, against 27.65 in H1 FY26. Non-current borrowings rose 291.42 to 779.38 (+487.96). That equals the LT proceeds exactly (L506), so no LT debt moved to current maturities in H1. Reading A: the new loans carry a moratorium past Sep-2027, and repayments start near commissioning. Reading B: current maturities are not reclassified at interim. Separating observation: the repayment schedule and moratorium end date. Ask for both. |
| F1-03 | F1 | R339, R340, R221, R222 | L503, L442 | "Investment in shares :: - \| -" | NEUTRAL-FACT | The template keeps an "Investment in shares" line, nil in both halves. Non-current investments are flat at 49.62. Note 5 (L243) says there is no subsidiary, associate or JV, so this is a minority holding of unnamed nature. Low priority. Identify it at the FY27 AR. |
| F6-01 | F6 | R044, R028, R029, R052, R053, R043, R040 | L238-L241 | "The proposed allotment is currently pending in-principle approval from the Stock Exchanges" | FORWARD-SIGNAL | 15,00,000 shares plus 15,00,000 warrants. Board approval 31-Aug-2026, shareholder postal ballot 30-Sep-2026. Not allotted at the 17-Oct board date. Paid-up is unchanged at 322.55 (L434, L455). Full conversion dilutes 4.65% of the 64.51 Mn pre-issue shares (322.55 / FV Rs 5). Equity alone is 2.33%. A basic-diluted EPS spread opens once warrants are allotted. The filing gives no price and names no allottees. Notion (memory) carries Rs 212 and the four non-promoter names as open items. |
| F8-01 | F8 | R143, R145, R146, R141, R142, R144, R147-R152, R259, R260 | L424, L425, L461 | "(6a)(ii) Current tax for earlier years :: - \| - \| 1.16 \| - \| 1.16 \| 1.16" | NEUTRAL-FACT | The earlier-years tax line is non-zero in the comparative Q2 FY26 (1.16). It is nil in FY27. It explains part of the 31.65% Q2 FY26 ETR. Deferred tax is a charge in every period: Q2 13.15, H1 17.86. The DTL rose 96.29 to 114.23 (+17.94 = 17.86 P&L + 0.08 OCI tax). That is a liability build from tax depreciation on capex, not a DTA credit, so there is no ETR step-up risk. Q2 ETR is 26.96%, 179 bps above the 25.17% statutory rate. |
| F12-01 | F12 | R215, R216, R213, R214, R327, R345, R349, R253, R263, R325, R105, R106, R287, R355 | L439, L438, L497, L506, L508, L496, L418, L511 | "Capital work in progress :: 549.16 \| 160.00" | FORWARD-SIGNAL | CWIP rose 3.43x in six months. Capex was 591.60 (L497). About 205 was capitalised (PPE +143.07 plus D&A 62.34) and 389.16 is still in CWIP. Debt funded it: gross borrowings rose 523.65 to 1,171.36 (+647.71 = 487.96 LT + 159.75 ST, an exact tie). CFO was only 47.28. Net debt rose 269.91 to 889.12. Net debt/equity went from 0.06 to 0.17, before any preferential cash. Capitalising the CWIP will step up D&A and finance cost in the P&L. P&L finance cost (H1 47.03, L418) equals cash interest paid (47.03, L511), so any capitalised interest sits inside capex. Ask for the capitalised borrowing cost and which projects make up the 549.16. |
| F12-02 | F12 | R241, R242, R311, R312 | L452, L489 | "CA (2c) Other current assets :: 543.19 \| 304.30" | AMBIGUOUS | +238.89 (+78.5%) in H1. This is the largest single working-capital use: 238.88 of the 403.94 absorbed (L484 minus L494). The H1 FY26 build was smaller (121.16). The filing gives no breakdown. Candidate readings: GST input credit on the 591.60 capex (reverses as credit is used), supplier advances (a WC build), or export/incentive receivables. Ask for the components. |
| F12-03 | F12 | R273, R274, R271, R272, R317, R319 | L468, L467, L492, L493 | "CL (3b) Other current liabilities :: 6.73 \| 45.46" | AMBIGUOUS | Other current liabilities fell 85%. Other financial liabilities fell 42% (124.73 to 72.31). Together they released 91.15 of funding. Reading A: customer advances or statutory dues unwound (WC deterioration). Reading B: capital creditors or one-off accruals were paid (neutral). This is the falling-liability case of the F12 rule. Ask what unwound. |
| F12-04 | F12 | R233, R234, R307, R072, R073, R074 | L448, L412, L487 | "CA (2b)(ii) Trade receivables :: 2,062.91 \| 1,971.69" | AMBIGUOUS | Debtor days depend on the basis. Sep-26 on H1 FY27 revenue: 90.0 days (2,062.91 / 4,194.31 x 183). Mar-26 on FY26 revenue: 106.9 days (1,971.69 / 6,732.01 x 365), so falling. Mar-26 on H2 FY26 revenue (6,732.01 - 2,702.75 = 4,029.26; x 182): 89.1 days, so flat. Receivables absorbed 91.22 in H1 FY27, against a 177.74 release in H1 FY26. The fall on the first basis comes from revenue growth in the denominator, not from collections. Conservative reading: debtor days are not shown to fall. This is leg 2 of re-engage trigger 1. |
| F12-05 | F12 | R325, R162, R301, R321, R363, R364, R370, R361 | L496, L427, L484, L494, L515, L518 | "Net cash flow from operating activities :: 47.28 \| 50.92" | CONFIRMATORY-NEGATIVE | H1 CFO/PAT is 14.3% (47.28 / 331.63). PAT rose 77% YoY but CFO fell. Working capital absorbed 403.94 of the 547.57 pre-WC operating profit. Opening cash of 44.40 (L514) confirms on filed evidence the Rs 4.4 cr that Notion carried as SECONDARY. H1 FY26 had 390.60 in deposits (L518). FY27 H1 holds 5.51. |
| F12-06 | F12 | R075, R076, R078, R299, R293, R129 | L413, L483, L480, L422 | "(2) Other income :: 21.73 \| 3.92 \| 10.47" | AMBIGUOUS | Q2 other income is 5.5x Q1. It is 8.1% of Q2 PBT and 19.5% of the QoQ PBT increase (17.81 of 91.27). In H1, interest (6.63) plus FVTPL gains (4.59) explain 11.22 of 25.65. The other 14.43 is unexplained, and most of it falls in Q2 since Q1 was 3.92. Q2 EBITDA margin is 13.02% without other income and 13.94% with it. The ~14% trigger threshold sits between the two. Ask what the 14.43 is (forex, export incentive, scrap, write-back). |
| F12-07 | F12 | R069-R071, R087-R089, R093-R095, R099-R101, R117-R119 | L412, L415, L416, L417, L420 | "(4a) Cost of materials consumed :: 1,339.24 \| 1,016.06 \| 691.21" | AMBIGUOUS | Materials plus inventory change take a rising share of revenue: 56.10% in Q2 FY27, 55.21% in Q1, 53.77% in Q2 FY26, 54.29% in FY26. The QoQ margin gain (12.23% to 13.02%) came from operating leverage, not gross margin. Employee cost fell to 4.56% from 5.58%, other expense to 26.33% from 26.97%. The filed numbers do not show the steel and conversion pass-through recovery. Ask whether the retrospective steel settlement (Notion: ~15-Jul) was booked in Q2, and in which line. |
| F14-01 | F14 | R093, R094, R096, R129, R130, R132, R159, R160, R162, R123, R124, R126, R189, R190, R192, R065 | L416, L422, L427, L421, L432, L564-L566, L246 | "(4b) Changes in inventories of FG and WIP :: -20.46 \| 1.65 \| 12.80 \| -20.46" | AMBIGUOUS | H1 FY27 does not foot to Q1+Q2. PBT is 449.46 against 447.81, PAT 331.63 against 329.98, total expenses 3,770.50 against 3,772.15, each off by 1.65. The cause: H1 inventory change (-20.46) equals Q2 alone. Q2 EPS 3.08 equals H1 EPS minus Q1 EPS (5.14 - 2.06). It also equals (H1 PAT - Q1 PAT) / 64.51 Mn = 198.51 / 64.51. The Q2 column PAT (196.86) gives 3.05. Reading A: Q2 inventory change should be -22.11, so Q2 PBT is understated by 1.65 (271.19). Reading B: H1 should be -18.81, so H1 is overstated and Q2 EPS is derived wrong. Reading C: Q1 was restated within H1 under Note 6 ("regrouped/restated where necessary", L246), but the Q1 column was left as published. The amount is immaterial (0.6% of Q2 PBT). The flaw is in the integrity of the filing. Separating observation: the 9M FY27 column in the Q3 filing, or a management answer. |
| F14-02 | F14 | R061, R066, R048 | L226, L114-L115, L81, L148 | "The Statutory auditors have expressed an unmodified review opinion on these results" | NEUTRAL-FACT | Note 1 calls the limited review an "opinion". The review report says "Accordingly, we do not express an audit opinion" (L114-L115) and gives a conclusion only. Two title mismatches: the Statement title (L148) reads "for the Half year ended" though it carries quarter columns. The review report (L81) says "Standalone", and the Statement never does. Each point is immaterial on its own. Together they are a governance data point on drafting care. |
| F14-03 | F14 | R031, R032, R043 | L240-L241, L23 | "namely Bombay Stock Exchange Limited and National Stock Exchange Limited" | NEUTRAL-FACT | Note 4 names the exchanges differently from the covering letter, which says "BSE Limited" and "National Stock Exchange of India Limited" (L23). This is an entity-name inconsistency across the same filing, in the note that carries the one live corporate action. |

## 2. CHECKLIST SCORECARD
| check | status | basis |
|--|--|--|
| F1 | FINDING | 18 ZERO_STANDING rows reviewed (ledger 2a). The ECL nil (F1-01) and zero LT repayment (F1-02) carry forward weight. Investment in shares is F1-03. The rest is benign: earlier-years tax nil, P&L Other Equity blank in quarter columns (Reg 33 year-end convention), PPE/RoU disposal nil, IPO proceeds line nil (IPO was in FY25). |
| F2 | N.A. | Standalone only. Note 5 (L243): "does not have any subsidiary/associate/joint venture company", so no consolidated statement exists to decompose. |
| F3 | N.A. | No subsidiaries (Note 5, L243), so no shell test. No Going Concern EoM. |
| F4 | PASS | The review report has 4 paragraphs (L90-L124), with no Other Matters and no component auditors. 0% of PAT rests on unreviewed numbers. |
| F5 | PASS | No EoM and no Going Concern language. The conclusion is unmodified (L117-L124). A verbatim QoQ diff was not possible: no prior-quarter fulltext was supplied. Limitation stated. |
| F6 | FINDING | Lexicon hits: Note 4 "approved", "subsequently approved", "proposed allotment ... pending in-principle approval" (L238-L241). Note 7 "will be available" (L248), letter "will also be made available" (L49). "commenced" (L52) is the meeting time, a false positive. One live commitment: F6-01. |
| F7 | PASS | None of the hedge-lexicon phrases ("may sometimes", "could have an effect", "no assurance", "subject to", "evaluating", "exploring", "in discussions", "endeavour") appear in Notes 1-7 (L224-L249). The SRE 2410 scope sentence (L113-L114) is standard boilerplate, not a notes hedge. |
| F8 | FINDING | ETR: Q2 26.96%, Q1 25.33%, Q2 FY26 31.65%, H1 FY27 26.22%, H1 FY26 26.90%, FY26 26.42%, against 25.17% statutory. Deferred tax is a charge in every period (a DTL build, no DTA shield). Earlier-years tax 1.16 appears in the comparatives (F8-01). |
| F9 | PASS | OCI remeasurement: Q2 0.16, Q1 0.16, Q2 FY26 -0.55, FY26 0.64 (L428). No quarter swing exceeds the full prior year. The identical Q1/Q2 values point to an accrual, not a fresh valuation. Immaterial. |
| F10 | PASS | Paid-up is 322.55 in all 6 columns (L434) and at both balance-sheet dates (L455). Basic equals diluted EPS in every period (L432-L433), so the spread is zero. The pending dilution is at F6-01. The Q2 EPS tie problem is at F14-01. |
| F11 | PASS | 322.55 + 4,906.97 = 5,229.52 (L455-L457). Other equity roll-forward: 4,575.10 + TCI 331.87 = 4,906.97, an exact tie. So no dividend, no share application money and no other reserve movement in H1. No third-party net-worth figure is in context to reconcile. |
| F12 | FINDING | Note 3 (L233-L236) gives a single segment, so the entity statements are the segment statements. Findings: CWIP build funded by debt (F12-01), working-capital lines (F12-02/03/04), cash conversion (F12-05), segment results (F12-06/07). |
| F13 | PASS | Results-only agenda (L41-L47): no AR, AGM, dividend, director, auditor, ESOP or fund-raise item. The meeting ran 116 minutes (L52). The preferential issue appears only in Note 4 (see F6-01). |
| F14 | FINDING | Cross-column footing and EPS tie (F14-01). "Opinion" against "conclusion" and title mismatches (F14-02). Exchange names (F14-03). |
| F15 | PASS | The entity list is empty (Note 5, "as at September 30, 2026", L243). No prior-quarter list was supplied for a diff; the check rests on Note 5's assertion. Limitation stated. |
| F16 | N.A. | Doctype is results, not a presentation. |
| F17 | N.A. | Doctype is results; there is no transcript to audit for silence. The Notion checklist is mapped to this filing in section 4, for information only. |

## 3. COMMITMENT REGISTER (F6)
| commitment | implied date | note/turn ref | status word |
|--|--|--|--|
| Allot 15,00,000 equity shares on a preferential basis | Not dated in the filing. Runs from the BSE/NSE in-principle approval date. The ICDR allotment window is an external rule; verify. | Note 4, L238-L241 | initiated (board 31-Aug-2026, shareholders 30-Sep-2026, exchange approval pending at 17-Oct-2026) |
| Allot 15,00,000 convertible warrants (conversion terms not in filing; Notion memory: 18 months, 25% upfront) | Same as above; conversion date not in filing | Note 4, L238-L241 | initiated |
| Results to be placed on the company website | At filing, 17-Oct-2026 | Note 7, L248-L249; letter L49-L50 | completed (ministerial) |

Prior-quarter status transitions: not testable, since no prior fulltext was supplied. Note 4 is new this quarter: its 31-Aug board date falls after the Q1 results.

## 4. NOTION CHECKLIST EVIDENCE MAP (information only; F17 N.A. on results; A4 rules)
| checklist item (Notion, memory) | what this filing shows | line |
|--|--|--|
| Trigger 1 leg 1: Q2 EBITDA margin above ~14% | Without other income: 306.00 / 2,350.92 = 13.02%. With other income: 13.94%. Q1 was 12.23% and Q2 FY26 11.27% (same method). The figure clears neither the >=14% gate nor the <=12.5% bear line. | L412, L413, L418, L419, L422 |
| Trigger 1 leg 2: debtor days falling | Depends on the basis: 106.9 to 90.0 days on full-year revenue, 89.1 to 90.0 days on like-for-like half-year revenue. Not shown to fall (F12-04). | L448, L412 |
| Limited Review Report qualification | None. The conclusion is unmodified. | L117-L124, L226 |
| FY27 base needs ~13.2% margin over Q2-Q4 | Q2 printed 13.02% without other income | as above |
| HP moulding line commissioned (Sept-2026) | Not disclosed. CWIP +389.16 net in H1. The project mix is not given. | L439 |
| H1 CFO and cash | CFO 47.28; cash 63.19; other bank balances 195.08; Mar-26 cash 44.40 (now filed) | L496, L449, L450, L514 |
| Aug-2026 preferential allotted? | No. Pending exchange in-principle approval. Paid-up 322.55. No share application money in equity (other equity roll ties to TCI). | L240, L455, L456 |
| Seamless tube funding (debt vs equity) | H1 LT borrowing +487.96 and ST +159.75. The filing does not name the project. | L506, L508 |
| Open verification list (AR cash flow, segment split, top-5 customers, extruded beam, allottee identity) | Not in this filing | none |

Reference facts: Q2 revenue +79.6% YoY and +27.5% QoQ (L412). Q2 PAT +143.5% YoY (L427).

## 5. YAML BLOCK (copy at runs/kross-q2fy27/work/blocks/a3-results.yaml)

```yaml
stage: A3-forensics
company: "KROSS"
quarter: "Q2 FY27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/kross-q2fy27/work/forensics_results_kross_q2fy27.md"
ledger_reconciled_pct: 100        # 372 of 372 ledger IDs read at cited line
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: PASS
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F1-01", check: "F1", line: "L478, L448, L487", classification: "AMBIGUOUS", implication: "Zero ECL charge both halves while receivables rise to 2,062.91 (28% of assets); latent provisioning hit to PAT; ask ageing and BS allowance"}
  - {id: "F1-02", check: "F1", line: "L507, L506, L458, L463", classification: "AMBIGUOUS", implication: "Nil LT repayment H1 FY27; NCL borrowings +487.96 equals LT proceeds, no current-maturity reclass; moratorium vs interim practice; ask repayment schedule"}
  - {id: "F1-03", check: "F1", line: "L503, L442", classification: "NEUTRAL-FACT", implication: "Non-current investment 49.62 flat, not a subsidiary/associate; identify at AR"}
  - {id: "F6-01", check: "F6", line: "L238-L241", classification: "FORWARD-SIGNAL", implication: "15,00,000 shares + 15,00,000 warrants pending exchange in-principle approval at 17-Oct; 4.65% dilution on 64.51 Mn shares; diluted EPS spread opens on allotment"}
  - {id: "F8-01", check: "F8", line: "L424, L425, L461", classification: "NEUTRAL-FACT", implication: "Earlier-years tax 1.16 in Q2 FY26 comparative; deferred tax is a DTL build (+17.94), no DTA shield; Q2 ETR 26.96% vs 25.17%"}
  - {id: "F12-01", check: "F12", line: "L439, L497, L506, L508, L496, L418, L511", classification: "FORWARD-SIGNAL", implication: "CWIP 160.00 to 549.16; capex 591.60 debt-funded (borrowings +647.71 exact tie, CFO 47.28); net debt 269.91 to 889.12; D&A and finance cost step-up on capitalisation; ask capitalised interest and CWIP project mix"}
  - {id: "F12-02", check: "F12", line: "L452, L489", classification: "AMBIGUOUS", implication: "Other current assets +238.89 (+78.5%), largest WC use; GST credit on capex vs supplier advances; ask components"}
  - {id: "F12-03", check: "F12", line: "L468, L467, L492, L493", classification: "AMBIGUOUS", implication: "Other current liabilities -85%, other financial liabilities -42% (91.15 released); customer-advance unwind vs capital creditors paid; ask"}
  - {id: "F12-04", check: "F12", line: "L448, L412, L487", classification: "AMBIGUOUS", implication: "Debtor days 106.9 to 90.0 on FY basis but 89.1 to 90.0 on like-for-like half-year basis; trigger-1 leg 2 not shown to pass"}
  - {id: "F12-05", check: "F12", line: "L496, L427, L484, L494, L514", classification: "CONFIRMATORY-NEGATIVE", implication: "H1 CFO/PAT 14.3%; WC absorbed 403.94 of 547.57; Mar-26 cash 44.40 now filed"}
  - {id: "F12-06", check: "F12", line: "L413, L483, L480, L422", classification: "AMBIGUOUS", implication: "Other income 21.73 vs 3.92 QoQ; 14.43 of H1 OI unexplained; Q2 EBITDA margin 13.02% ex-OI vs 13.94% incl, straddling ~14% trigger; ask nature"}
  - {id: "F12-07", check: "F12", line: "L412, L415, L416, L417, L420", classification: "AMBIGUOUS", implication: "Material intensity 56.10% Q2 vs 55.21% Q1 vs 53.77% Q2 FY26; margin gain from operating leverage, not pass-through; ask whether steel settlement booked in Q2"}
  - {id: "F14-01", check: "F14", line: "L416, L422, L427, L432, L564-L566, L246", classification: "AMBIGUOUS", implication: "H1 does not foot to Q1+Q2 by 1.65 (inventory change); Q2 EPS 3.08 ties to H1 less Q1, Q2 PAT 196.86 implies 3.05; three readings; separate at Q3 9M column"}
  - {id: "F14-02", check: "F14", line: "L226, L114-L115, L81, L148", classification: "NEUTRAL-FACT", implication: "Note 1 calls the limited review an opinion; letter says no audit opinion; title mismatches; drafting-care data point"}
  - {id: "F14-03", check: "F14", line: "L240-L241, L23", classification: "NEUTRAL-FACT", implication: "Exchange names in Note 4 differ from covering letter"}
forward_signals: ["F6-01", "F12-01"]
ambiguous: ["F1-01", "F1-02", "F12-02", "F12-03", "F12-04", "F12-06", "F12-07", "F14-01"]
commitments:
  - {commitment: "Preferential allotment of 15,00,000 equity shares", implied_date: "on BSE/NSE in-principle approval; not dated in filing", ref: "Note 4, L238-L241", status_word: "initiated"}
  - {commitment: "Allotment of 15,00,000 convertible warrants", implied_date: "on BSE/NSE in-principle approval; conversion date not in filing", ref: "Note 4, L238-L241", status_word: "initiated"}
  - {commitment: "Results placed on company website", implied_date: "17-Oct-2026", ref: "Note 7, L248; letter L49", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Trigger 1 does not pass on filed evidence; A4 rules. Leg 1: Q2 EBITDA margin 13.02% ex other income, 13.94% including it. The ~14% line sits between the two, so the nature of the unexplained 14.43 of H1 other income (F12-06) decides the borderline reading. Leg 2: debtor days fall only on a full-year denominator inflated by 80% YoY growth; like-for-like half-year days are flat at ~90 (F12-04). Margin gain came from operating leverage while material intensity rose (F12-07), so pass-through recovery is not visible. The balance sheet carries the forward story: CWIP 3.4x, borrowings 2.2x, CFO/PAT 14%, no LT repayment yet and no current-maturity reclass (F1-02), all before the preferential cash lands. F14-01 is immaterial in size, but the Q2 PBT, PAT and EPS columns cannot all be right; the Q3 9M column will separate the readings. No prior-quarter fulltext, so F5/F15 diffs rest on this filing alone."
```
