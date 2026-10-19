# A4 MERGED REVIEW: Tatva Chintan Pharma Chem Limited (TATVA), Q2 FY27 (quarter and half year ended 30-Sep-2026)

Agent: A4 analyst | model: claude-opus-5-5 | run date: 2026-10-20 | Loop iteration 1 (A5 findings F1, C1, M1-M3, S1-S6 applied; change log after the closing YAML)
Protocol loaded: frameworks/Quarterly_Results_Review_Protocol_v1_4.md (Role 4). Role 5 NOT loaded: no transcript exists (call cancelled, see the Role 5 slot).
Documents merged: results filing (14 pp, standalone + consolidated), updated investor presentation (42 pp), earnings-call cancellation notice (1 p).
This review is one merged file: Steps 0 to 5, then Steps 5.5 to 9, the Role 5 slot, questions, monitorables, the plain-language brief, the closing YAML and the Loop 1 change log. It supersedes parts/review_tatva_q2fy27.part2.md.

Anchor convention. "RES L###" = line in runs/tatva-q2fy27/extracted/tatva-results-q2fy27-fulltext.md. "PPT L###" = line in the presentation fulltext. "NTC L##" = line in the notice fulltext. R-ids are A1 structured rows. Filing units are Rs million; this review converts to Rs Crore (x0.1) unless a cell says "Mn". "[memory]" = Notion brief or companies/TATVA.md, never anchored evidence. "[A4 computation]" = arithmetic on cited filed cells. ND = not disclosed in the supplied documents.

A3 finding ID prefixes: RES- (results forensics), PPT- (presentation forensics), NTC- (notice forensics).

---

## LEDGER RECONCILIATION PREAMBLE

Ledger contains 13 notes / 0 turns / 42 slides. All 13 notes, all 42 slides and all 1,856 structured rows reviewed (results 1,090 rows incl. supplement R1049-R1090, 241 line items, 69 ZERO_STANDING cells; presentation 738 rows incl. 24 superseded IDs read as non-evidence; notice 28 rows). A2 gate_a2: pass on all three ledgers; orphan IDs: none; MISSING_FROM_STRUCTURED: closed (results supplement), none (presentation, notice). A3 reconciled 100% on all three.

Findings incorporated: RES-A3-01, RES-A3-02, RES-A3-03, RES-A3-04, RES-A3-05, RES-A3-06, RES-A3-07, RES-A3-08, RES-A3-09, RES-A3-10, RES-A3-11, RES-A3-12, RES-A3-13; PPT-A3-P-01 to PPT-A3-P-20 (20 findings); NTC-A3-01, NTC-A3-02, NTC-A3-03, NTC-A3-04, NTC-A3-05. Total 38.

Pipeline data-integrity items carried (none blocks this stage; none needs the source):
- RES-A3-13: standalone EPS cells 6.57 (Q2) and 6.01 (H1 FY26) are below the computed 6.578 and 6.017. Truncation or manual-transcription error on image page 10. Re-verify against the page image. Immaterial.
- A2 LABEL_ANOMALY (R1005, R1040): the "Net decrease in cash and cash equivalents" caption sits on positive values (RES L321, L610). Reviewed, no finding (drafting lapse, RES-A3-12).
- PPT PN-1 to PN-4 (A3 presentation pipeline notes): p26 ESS "165" printed twice with one row; R578 anchor at L751 should be L763; R031/R032 off by one line; p15/p16 right-hand block layout-scrambled but all subtotals tie.
- NTC: A1 anchors R015, R023, R026 are one line off (L45, L34, L34). All quotes verbatim.
- Correction to PPT-A3-P-01 (its timing came from memory): the filed notice shows the call was cancelled at 16:03:53 IST (NTC L58-59). The original deck was signed at 18:05:26 (PPT L17). So the call never took place and no ratio was quoted live on either deck basis. The "ratios quoted on the call" risk in PPT-A3-P-01 is void. The restatement finding itself stands.

---

## STEP 0: PRE-FLIGHT

### 0A. Notion page (fetched live by the orchestrator 2026-10-19; read-only; memory, not evidence)

| Item | Value on page [memory] |
|---|---|
| Decision Status (verified first) | **WATCHLIST / AVOID. Not held.** Position size "None; small 2-3% ceiling only if zone reached intact". Avg cost ND. |
| One-line thesis | "Real recovery undone by an unreachable price." |
| Prior run (2026-07-12) | Gate PROCEED WITH CAVEATS (FLAG-CASH INDETERMINATE leaning structural); valuation AVOID; FTTCP DEEP WATCH +3/8; Devil's advocate WEAKENED BUT ALIVE |
| Entry zone | Properties: Entry Price Max Rs 147, MoS Rs 118 (Amendment 4.5 refresh). Page verdict block still shows Rs 97-121 / MoS Rs 97 and flags itself stale. CMP Rs 1,841 (14-Oct) = 12.5x entry max. |
| Four-pillar (4.5 refresh) | Pillar 1 ROCE 13.51% blend (40% pre-depression 22.45%, 30% FY28 8.5%, 30% current 6.6%); base PE 14.26x; cash multiplier 0.80x; Pillar 3 +0x; sector cap 35x; Track 1 RRM 9.4x governs, Track 2 11.4x |
| Bear / Base / Bull projections | **No full table on page.** Present: Track 1 FV Rs 201 / 287 / 409; FY28 ROCE 6.3% / 8.5% / 10.6%. Ruling 51 pending (FV Rs 237 or Rs 287). |
| Thesis-broken conditions | (a) H1 FY27 CFO negative on rising revenue with receivable days above 185; (b) ROCE fails to clear 8% by FY28; sub-trigger: own-subsidiary debtor days >90; Q1 8D: reassess if new-mix ROCE ceiling <12% over trailing 4 quarters |
| Q2 separating metric | Bull: CFO/EBITDA >70% AND receivable days <=90. Bear: CFO negative OR CFO/EBITDA <30% AND receivable days >100 |
| Pending operator rulings | **50: receivable-days line for trigger (a), 185 days or the 90/100-day bands (flag only, not resolved here).** 51: FV Rs 237 or Rs 287. |
| Monitoring checklist | 8 items (scored in Step 6B) |
| Prior questions | Q1 Step 8.5 (8), updated Q2 list (8), AR Section J (8), Q1 call guidance log (17 items) (scored in Step 6) |

### 0B. Units
All filing figures are "Indian Rupees in million, except per share data" (RES L140 R986; L442 R1022). The deck uses Rs Mn (PPT header L7). Conversion: Rs Mn x 0.1 = Rs Cr. Per-share data in Rs, no conversion.

### 0C. Share count
Paid-up equity Rs 233.92 Mn (Rs 23.392 Cr) in every period, both entities (RES L183 R234-R239; L474 R647-R652). Shares outstanding 2,33,92,055 (PPT L1070 R700). No split, bonus, rights, ESOP, QIP or buyback from Q2 FY26 to Q2 FY27. Basic = diluted in every column. Reported EPS = share-adjusted EPS.

### 0D. Notes extraction (all numbered notes, both entities, plus the unexplained statement line)

| Note # | Subject | What it says (1 sentence) | Rs Cr impact | Period affected | Comparability impact |
|---|---|---|---|---|---|
| Cons 1 (RES L345-348) | Approval | Audit Committee reviewed, Board approved on 19-Oct-2026. | nil | Q2 FY27 | None |
| Cons 2 (RES L350-351) | Review | Limited review by statutory auditors "who has expressed an unmodified opinion". | nil | Q2/H1 FY27 | None. Drafting: a review gives a conclusion, not an opinion (RES-A3-11). |
| Cons 3 (RES L353-355) | Basis | Ind AS, Sec 133, Reg 33. | nil | all | None |
| Cons 4 (RES L357) | Segment | One reportable segment, specialty chemicals; no Ind AS 108 disclosure. | nil | all | No segment P&L or assets. Product split exists only in the deck. |
| Cons 5 (RES L359-366) | Standalone key numbers | Restates standalone revenue, PBT, PAT, TCI; equals the standalone P&L. Labels revenue "Total income from operations (Net)". | nil | all | None (label lapse, RES-A3-12) |
| Cons 6 (RES L368-369) | Website | Results on BSE, NSE and company site. | nil | n/a | None |
| Cons 7 (RES L371) | Reclassification | Prior-period figures "reclassified/rearranged/regrouped ... wherever necessary". No amounts, no lines. | ND | prior periods | **Unquantified.** FY26 filed CFO Rs 31.49 Cr differs from memory "~Rs 35 Cr" (RES-A3-10). Treat prior-period comparisons as subject to an unknown reclass. |
| Std 1-6 (RES L633-643) | Approval, review, basis, segment, website, reclassification | Mirror cons notes 1-4, 6, 7. | nil / ND | as above | As above |
| Statement line 6 (RES L158, L460) | Exceptional items | Rs 1.32 Cr (13.18 Mn) charge in Q1 FY27, carried in the H1 column, nil in Q2 FY27 and all FY26 columns. **No note explains it in either entity.** | -1.32 (pre-tax) | Q1 FY27, H1 FY27 | Normalise Q1 and H1 PBT. Tax effect ND, so post-tax normalisation is ND. Second filing with no disclosure (RES-A3-01, PPT-A3-P-04). |

Answers to the four 0D questions: (1) Cons 7 and the exceptional line change comparisons; (2) Q1/H1 PBT are shown pre- and post-exceptional below; (3) the exceptional is presented as one-off, nature ND; (4) no note changes a thesis assumption directly, but a second filing with no exceptional-item note is a disclosure data point.

**Auditor opinion check.** Both reports are limited reviews under SRE 2410 with unmodified conclusions; "we do not express an audit opinion" (RES L98 cons; L410-418 std). No Emphasis of Matter, no Other Matter, no Going Concern paragraph (RES-A3 F5 PASS). All three entities (holding, Tatva Chintan USA Inc., Tatva Chintan Europe B.V.) are inside the review scope (RES L103-107); unreviewed contribution Rs 0 (RES-A3 F4 PASS).

### 0E. Business type
Standard operating business (specialty chemicals manufacturer; one reportable segment, RES L357). Standard Steps 1 and 5 apply. Archetype per signed mental model: ND (Mental Model signed: ND on page [memory]).

**Filing timeline (all filed timestamps).** This sequence matters for NTC-A3-02.

| Time 19-Oct-2026 (IST) | Event | Anchor |
|---|---|---|
| 13-Oct-2026 | Call intimated for 19-Oct 17:00 | NTC L34-36 |
| 11:30 to 15:45 | Audit Committee and Board meetings (4 h 15 min, one disclosed item) | RES L50, L40-41 |
| 15:48:12 | Results letter signed, Ref 00054 | RES L60, L19 |
| 16:03:53 | Call cancellation signed, Ref 00055, "unforeseen circumstances", no new date | NTC L58-59, L18, L39-40 |
| 17:00 | Scheduled call start (did not take place) | NTC L36 |
| 18:05:26 | Original deck signed, Ref 00056 | PPT L17 |
| 20:54:24 | Updated deck signed, Ref 00057; RoE and Debt/EBITDA restated | PPT L17, L23, L65-66 |

Reading: results were approved and signed 15 minutes before the cancellation. The filed timestamps rule out the "results not ready" bear reading of NTC-A3-02. Two readings remain: a logistics event (neutral) or a choice not to take live questions on numbers just filed (bear). The separating observation is whether the company names a cause and a new date. The CMD message in the deck opens "Good evening, ladies and gentlemen" (PPT L111). It reads as the call script [INFERENCE], and the company filed it two hours after it cancelled the call.

Checkpoint: Notion fetched with Decision Status, units identified, share count unchanged, all notes extracted, auditor conclusion verified, business type stated.

---

## STEP 1: DATA EXTRACTION TABLE (CONSOLIDATED, Rs Cr)

Columns: Q2 FY26 = quarter ended 30.09.2025; Q1 FY27 = quarter ended 30.06.2026; Q2 FY27 = quarter ended 30.09.2026. FY[YY-1] = FY26 audited. FY[YY] = FY27, not complete, so ND. H1 columns added because Q2 is a half-year filing. All cells from RES p4 at the line shown.

| Line item (RES line) | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|
| Revenue from operations (L145) | 123.52 | 167.06 | 217.32 | 240.38 | 384.38 | 505.86 | ND |
| Other income (L146) | 1.01 | 2.78 | 1.75 | 2.16 | 4.53 | 3.55 | ND |
| Total income (L147) | 124.52 | 169.84 | 219.07 | 242.54 | 388.91 | 509.41 | ND |
| Cost of materials consumed (L149) | 61.99 | 105.41 | 114.05 | 125.88 | 219.46 | 262.75 | ND |
| Purchases of stock-in-trade (L150) | 1.24 | 1.40 | 2.04 | 2.53 | 3.45 | 6.49 | ND |
| Change in inventories (L151) | (8.36) | (31.52) | (9.84) | (15.20) | (41.36) | (44.71) | ND |
| Employee benefits expense (L152) | 14.95 | 16.74 | 18.23 | 29.03 | 34.97 | 62.93 | ND |
| Finance costs (L153) | 0.51 | 2.08 | 2.71 | 0.92 | 4.79 | 2.85 | ND |
| Depreciation and amortisation (L154) | 9.05 | 10.57 | 10.79 | 18.02 | 21.36 | 36.85 | ND |
| Other expenses (L155, R1049-R1054) | 31.49 | 42.73 | 52.15 | 58.59 | 94.88 | 125.23 | ND |
| Total expenses (L156) | 110.86 | 147.41 | 190.13 | 219.78 | 337.54 | 452.40 | ND |
| PBT before exceptional (L157) | 13.66 | 22.43 | 28.94 | 22.76 | 51.37 | 57.01 | ND |
| Exceptional items (L158) | nil | 1.32 | nil | nil | 1.32 | nil | ND |
| Profit before tax (L159) | 13.66 | 21.11 | 28.94 | 22.76 | 50.05 | 57.01 | ND |
| Tax expense (L163) | 3.75 | 5.13 | 7.49 | 6.20 | 12.62 | 14.96 | ND |
| of which current tax (L161) | 2.48 | 1.01 | 4.44 | 4.34 | 5.45 | 11.97 | ND |
| of which deferred tax (L162) | 1.27 | 4.12 | 3.05 | 1.85 | 7.17 | 2.99 | ND |
| PAT (L164) | 9.92 | 15.98 | 21.45 | 16.57 | 37.43 | 42.05 | ND |
| EPS reported, Rs (L181) | 4.24 | 6.83 | 9.17 | 7.08 | 16.00 | 17.98 | ND |
| EPS share-adjusted, Rs | 4.24 | 6.83 | 9.17 | 7.08 | 16.00 | 17.98 | ND |

**Derived metrics (consolidated) [A4 computation; Mn inputs from the lines above].** Operating EBITDA uses PBT before exceptional items so the Q1 one-off does not distort the trend; the post-exceptional figure is in brackets.

| Derived metric | Formula | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|---|
| Operating EBITDA (Rs Cr) | PBT pre-exc + D&A + Fin - OI | 22.22 | 32.30 (30.98 post-exc) | 40.69 | 39.55 | 72.99 (71.67 post-exc) | 93.16 | ND |
| Operating EBITDA margin | / Revenue | 17.99% | 19.33% | 18.72% | 16.45% | 18.99% | 18.42% | ND |
| Reported EBITDA (Rs Cr) | PBT pre-exc + D&A + Fin | 23.22 | 35.08 | 42.44 | 41.71 | 77.52 | 96.71 | ND |
| Core PBT ex-OI (Rs Cr) | PBT pre-exc - OI | 12.66 | 19.65 | 27.19 | 20.60 | 46.84 | 53.46 | ND |
| Other income / PBT | OI / PBT pre-exc | 7.38% | 12.39% | 6.06% | 9.50% | 8.83% | 6.23% | ND |
| Effective tax rate | Tax / reported PBT | 27.42% | 24.30% | 25.88% | 27.22% | 25.21% | 26.23% | ND |
| PAT margin | PAT / Revenue | 8.03% | 9.57% | 9.87% | 6.89% | 9.74% | 8.31% | ND |
| Gross margin | (Rev - materials - purchases - inv change) / Rev | 55.58% | 54.93% | 51.11% | 52.90% | 52.77% | 55.61% | ND |
| Material cost / revenue | (L149+L150+L151) / Rev | 44.42% | 45.07% | 48.89% | 47.10% | 47.23% | 44.39% | ND |
| Employee cost / revenue | L152 / Rev | 12.10% | 10.02% | 8.39% | 12.08% | 9.10% | 12.44% | ND |
| Other expenses / revenue | L155 / Rev | 25.50% | 25.58% | 24.00% | 24.38% | 24.68% | 24.76% | ND |

Cross-check: deck operating EBITDA Q2 407 / Q1 323 / Q2 FY26 222 / H1 730 / H1 FY26 395 Mn (PPT L328 R118-R124) match 406.89 / 322.96 / 222.15 / 729.85 / 395.45 Mn. Deck PAT margin 9.9% Q2 (R150) matches 9.87%.

### STEP 1 (STANDALONE, Rs Cr; RES p10)

| Line item (RES line) | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|
| Revenue from operations (L447) | 115.86 | 146.70 | 207.48 | 225.04 | 354.19 | 496.30 | ND |
| Other income (L448) | 0.79 | 4.03 | 2.71 | 2.16 | 6.74 | 3.53 | ND |
| Total income (L449) | 116.66 | 150.74 | 210.19 | 227.21 | 360.92 | 499.82 | ND |
| Cost of materials consumed (L451) | 61.99 | 105.41 | 114.05 | 125.88 | 219.46 | 262.75 | ND |
| Purchases of stock-in-trade (L452) | nil | nil | nil | nil | nil | nil | ND |
| Change in inventories (L453) | (10.32) | (38.94) | (4.73) | (19.24) | (43.67) | (31.79) | ND |
| Employee benefits expense (L454) | 14.95 | 16.74 | 18.23 | 29.03 | 34.97 | 62.93 | ND |
| Finance costs (L455) | 0.51 | 2.08 | 2.71 | 0.92 | 4.79 | 2.85 | ND |
| Depreciation and amortisation (L456) | 9.05 | 10.57 | 10.79 | 18.02 | 21.36 | 36.84 | ND |
| Other expenses (L457, R1070-R1075) | 28.14 | 39.47 | 48.70 | 53.20 | 88.17 | 113.08 | ND |
| Total expenses (L458) | 104.31 | 135.32 | 189.75 | 207.81 | 325.08 | 446.66 | ND |
| PBT before exceptional (L459) | 12.34 | 15.41 | 20.44 | 19.40 | 35.85 | 53.17 | ND |
| Exceptional items (L460) | nil | 1.32 | nil | nil | 1.32 | nil | ND |
| Profit before tax (L461) | 12.34 | 14.09 | 20.44 | 19.40 | 34.53 | 53.17 | ND |
| Tax expense (L465) | 3.40 | 3.65 | 5.05 | 5.32 | 8.70 | 14.08 | ND |
| of which current tax (L463) | 2.14 | nil | 1.77 | 3.36 | 1.77 | 10.07 | ND |
| of which deferred tax (L464) | 1.26 | 3.65 | 3.28 | 1.97 | 6.93 | 4.02 | ND |
| PAT (L466) | 8.94 | 10.45 | 15.39 | 14.07 | 25.83 | 39.08 | ND |
| EPS reported, Rs (L472) | 3.82 | 4.47 | 6.57 | 6.01 | 11.04 | 16.71 | ND |
| EPS share-adjusted, Rs | 3.82 | 4.47 | 6.57 | 6.01 | 11.04 | 16.71 | ND |

| Derived metric (standalone) | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|
| Operating EBITDA (Rs Cr) | 21.11 | 24.03 | 31.23 | 36.18 | 55.26 | 89.33 | ND |
| Operating EBITDA margin | 18.22% | 16.38% | 15.05% | 16.08% | 15.60% | 18.00% | ND |
| Reported EBITDA (Rs Cr) | 21.90 | 28.06 | 33.94 | 38.34 | 62.00 | 92.86 | ND |
| Core PBT ex-OI (Rs Cr) | 11.55 | 11.38 | 17.73 | 17.23 | 29.11 | 49.64 | ND |
| Other income / PBT pre-exc | 6.43% | 26.17% | 13.24% | 11.15% | 18.80% | 6.64% | ND |
| Effective tax rate | 27.56% | 25.88% | 24.71% | 27.44% | 25.19% | 26.49% | ND |
| PAT margin | 7.72% | 7.12% | 7.42% | 6.25% | 7.29% | 7.87% | ND |
| Gross margin | 55.41% | 54.69% | 47.31% | 52.62% | 50.37% | 53.46% | ND |

### STANDALONE VS CONSOLIDATED GAP (first-class metric; RES-A3-03 to RES-A3-06)

| Metric (Rs Cr unless %) | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | H2 FY26 (derived) |
|---|---|---|---|---|---|---|---|
| Revenue gap, cons - std (L145 - L447) | 7.65 | 20.35 | 9.84 | 15.34 | 30.19 | 9.56 | (5.78) |
| Operating EBITDA gap | 1.11 | 8.27 | 9.46 | 3.37 | 17.73 | 3.83 | 0.46 |
| Other income gap, std - cons (L448 - L146) | (0.21) | 1.25 | 0.95 | nil | 2.20 | (0.02) | (0.02) |
| PAT gap, cons - std (L164 - L466) | 0.98 | 5.54 | 6.06 | 2.49 | 11.60 | 2.97 | 0.48 |
| **PAT gap as % of standalone PAT** | **10.9%** | **53.0%** | **39.4%** | **17.7%** | **44.9%** | **7.6%** | 1.9% |
| PAT gap as % of consolidated PAT (subsidiary share) | 9.8% | 34.6% | 28.3% | 15.1% | 31.0% | 7.1% | 1.9% |
| Parent share of group PAT | 90.2% | 65.4% | 71.7% | 84.9% | 69.0% | 92.9% | 98.1% |
| Standalone operating EBITDA margin | 18.22% | 16.38% | 15.05% | 16.08% | 15.60% | 18.00% | 19.60% |

Movement test: the gap moved +28.5 pp YoY (10.9% to 39.4% of std PAT) and -13.6 pp QoQ (53.0% to 39.4%). Both exceed 5 pp. In H2 FY26 the gap collapsed to Rs 0.48 Cr (1.9% of standalone PAT) and the revenue gap turned negative (Rs -5.78 Cr). Subsidiary profit has fallen at year end before (RES-A3-03).

Shell-entity read (RES-A3-06): cons-minus-std materials Rs 0.00 Cr, employee cost Rs 0.00 Cr, finance cost Rs 0.00 Cr, borrowings identical (RES L234/L240 vs L523/L529). The US and EU subsidiaries carry no plant, no payroll and no debt. They hold third-party purchases Rs 2.04 Cr (Q2), other expenses Rs 3.45 Cr (Q2), inventory Rs 24.50 Cr (RES L213 minus L504) and cash Rs 5.33 Cr at 30-Sep. Yet they earn 28.3% of Q2 group PAT. Intercompany proxies: std receivables exceed cons by Rs 10.49 Cr at 30-Sep (Rs 24.69 Cr at 31-Mar); std other current liabilities exceed cons by Rs 16.89 Cr (RES L533 vs L244). Intercompany debtor days: ND (sales to subsidiaries not disclosed); the >90-day sub-trigger cannot be tested from the filing.

Parent margin (RES-A3-04): standalone operating EBITDA margin was 18.22% in Q2 FY26 and averaged 19.60% in H2 FY26 (derived: FY26 minus H1 FY26). It then fell in each of the last two quarters, to 16.38% (Q1 FY27) and 15.05% (Q2 FY27). Q3 and Q4 FY26 standalone quarters individually are ND. Standalone gross margin fell 738 bps QoQ (54.69% to 47.31%) and 810 bps YoY (55.41% to 47.31%). The group margin of 18.72% holds only through the subsidiaries. Standalone other income exceeds consolidated by Rs 2.20 Cr in H1 FY27, against nil in H1 FY26 (RES-A3-05). So a new intra-group income stream sits in parent profit and drops out on consolidation. Its nature is ND.

Checkpoint: extraction complete for both entities; every cell a line-anchored number or ND.

---

## STEP 2: Q2 YoY COMPARISON (Q2 FY27 vs Q2 FY26)

### Consolidated

| Metric | Q2 FY26 | Q2 FY27 | YoY change | Verdict |
|---|---|---|---|---|
| Revenue from operations (L145) | 123.52 | 217.32 | +75.9% | Strong. Record quarter (PPT L114). |
| Operating EBITDA | 22.22 | 40.69 | +83.2% | Strong in rupees |
| Operating EBITDA margin | 17.99% | 18.72% | +74 bps | Flat to slightly up YoY; below the 20-22% guide band [memory] |
| Depreciation (L154) | 9.05 | 10.79 | +19.2% | Scaling well below revenue: no absorption deficit |
| Finance costs (L153) | 0.51 | 2.71 | +434.3% | Debt-funded working capital; scaling far faster than revenue |
| EBIT (operating, Op EBITDA - D&A) | 13.16 | 29.90 | +127.1% | Strong |
| Other income (L146) | 1.01 | 1.75 | +74.0% | Small (6.06% of PBT) |
| **Core operating PBT (PBT pre-exc - OI)** | **12.66** | **27.19** | **+114.8%** | **Grew in line with PAT; FX line location ND (see diagnostic 6)** |
| Reported PBT (L159) | 13.66 | 28.94 | +111.8% | Strong |
| PAT (L164) | 9.92 | 21.45 | +116.3% | Strong |
| EPS share-adjusted (L181) | 4.24 | 9.17 | +116.3% | Strong |

### Standalone

| Metric | Q2 FY26 | Q2 FY27 | YoY change | Verdict |
|---|---|---|---|---|
| Revenue (L447) | 115.86 | 207.48 | +79.1% | Strong |
| Operating EBITDA | 21.11 | 31.23 | +48.0% | Lags revenue |
| Operating EBITDA margin | 18.22% | 15.05% | -317 bps | **Contracting** |
| Core PBT (L459 - L448) | 11.55 | 17.73 | +53.5% | Lags revenue |
| PAT (L466) | 8.94 | 15.39 | +72.1% | Helped by other income +Rs 1.91 Cr |

### Six diagnostic answers

1. **Revenue YoY.** Yes. Consolidated revenue grew 75.9% YoY (Q2 FY27 Rs 217.32 Cr vs Q2 FY26 Rs 123.52 Cr). H1 grew 59.9% YoY (Rs 384.38 Cr vs Rs 240.38 Cr). The company's FY27 guide is 25-30% [memory, MGMT]. H1 runs at twice the guide; the guide is stale and was not restated (PPT L141 "similar momentum"). Notion base-case revenue projection: ND (no projection table on page).
2. **Margin YoY.** Q2 FY27 operating EBITDA margin of 18.72% vs Q2 FY26 margin of 17.99% = +74 bps YoY. Sequentially it fell 61 bps from 19.33% (Q1 FY27). Material cost rose 447 bps of revenue YoY (44.42% to 48.89%). Employee cost fell 371 bps (12.10% to 8.39%) and other expenses fell 150 bps (25.50% to 24.00%). At group level, operating leverage offset the input-cost hit.
   **Bear counter (A5 M2).** At the parent the offset fails. Standalone Q2 YoY: materials rose from 44.59% to 52.69% of revenue (+810 bps; RES L447, L451, L453). Employee cost fell 411 bps (L454) and other expenses 82 bps (L457), so parent operating EBITDA margin fell 317 bps. The group's +74 bps exists only after adding the subsidiary layer, which has no plant, payroll or debt; its profit gap fell to Rs 0.48 Cr in H2 FY26. Two readings: a real cost squeeze at the factory (bull for the group if the subsidiaries keep earning; bear for the factory), or margin moved to the subsidiaries by transfer price. Both readings make the group offset depend on subsidiary profit holding at year end. Separating observation: H2 FY27 subsidiary profit share at FY27 results (M12), and the answers to Q5 and Q7.
3. **Core operating PBT YoY.** Core PBT ex-OI grew 114.8% YoY (Rs 12.66 Cr to Rs 27.19 Cr), close to reported PAT growth of 116.3%. On this metric the headline growth is real at the consolidated level, subject to the FX-location qualifier in diagnostic 6. At the standalone level core PBT grew 53.5%, well below revenue growth of 79.1%.
4. **Gap between core PBT growth and PAT growth.** Small. Other income +Rs 0.75 Cr; finance cost -Rs 2.20 Cr; ETR fell from 27.42% to 25.88% (+Rs 0.45 Cr to PAT); exceptional nil both quarters. See the Step 4 bridge.
5. **D&A and finance vs revenue.** D&A +19.2% vs revenue +75.9%: no absorption deficit yet (capital work in progress is not yet depreciating). Finance costs +434.3%: short-term borrowings rose Rs 50.17 Cr in H1 (RES L240) to fund working capital and capex. This is the early warning for the capex phase. When Dahej-III commissions (Q3-Q4 FY28 [memory]), D&A and interest both step up before the plant earns.
6. **Other income concentration.** OI was Rs 2.78 Cr in Q1 and Rs 1.75 Cr in Q2. H1 OI of Rs 4.53 Cr already exceeds FY26 OI of Rs 3.55 Cr. The H1 cash flow deducts an unrealised FX gain of Rs 3.91 Cr (RES L268) and interest income of Rs 0.11 Cr (L269). OI composition is ND. If the FX gain sits in OI, most of H1 OI is a non-cash translation gain. At 8.83% of H1 PBT it does not change the trajectory read. The item to watch is the standalone OI excess over consolidated (Rs 2.20 Cr H1, RES-A3-05).
   **Bear counter (A5 M1).** The filing does not disclose the P&L line of the unrealised FX gain (RES L268). If it sits in other expenses, not other income, it is inside operating EBITDA and core PBT: up to Rs 3.91 Cr (8.3%) of H1 core PBT of Rs 46.84 Cr. With the H1 FY26 unrealised loss of Rs 0.43 Cr, the swing is up to Rs 4.33 Cr (16.5%) of the Rs 26.23 Cr H1 core-PBT increase. The Q2 split is ND. Bull reading: FX sits in other income, so core PBT is clean. Bear reading: FX sits in other expenses, so up to one-sixth of the H1 core-PBT increase is a non-cash translation gain. Separating observation: the FY27 annual report note on other income and other expenses (FX line), or a direct answer to Q8.

Checkpoint: YoY table and six answers complete.

---

## STEP 3: SEQUENTIAL QoQ TRAJECTORY (consolidated)

Q1 FY26 = H1 FY26 minus Q2 FY26. Q3 FY26 and Q4 FY26 individually are ND (no Q3 data in the supplied documents). H2 FY26 = FY26 minus H1 FY26, shown as a two-quarter block.

| Quarter | Revenue (Rs Cr) | Op EBITDA margin | Core PBT ex-OI (Rs Cr) | One-offs flagged | QoQ run-rate |
|---|---|---|---|---|---|
| Q1 FY26 (derived, L145/L157/L146) | 116.86 | 14.83% | 7.95 | none in filing | base |
| Q2 FY26 (L145) | 123.52 | 17.99% | 12.66 | none | +5.7% |
| Q3 FY26 | ND | ND | ND | ND | ND |
| Q4 FY26 | ND | ND | ND | ND | ND |
| H2 FY26 block (derived; per-quarter average) | 265.48 (132.74 avg) | 20.19% | 32.86 (16.43 avg) | Cons 7 reclass unquantified | avg +7.5% on Q2 FY26 |
| Q1 FY27 (L145) | 167.06 | 19.33% | 19.65 | Exceptional Rs 1.32 Cr (L158), nature ND; FG/WIP build Rs 31.52 Cr flattered gross margin (L151) | +25.9% on H2 avg |
| Q2 FY27 (L145) | 217.32 | 18.72% | 27.19 | Solvent +60-100% and freight +100% called "temporary" (PPT L135-L141, MGMT) | **+30.1%** |

Diagnostics:
- **Trajectory: stepping up** in revenue and core PBT. Margin plateaued at 18.7-19.3% for two quarters, below the H2 FY26 block average of 20.19%. Revenue steps up while margin slips back from the H2 FY26 level.
- **Distortions.** Q1 FY27 carries the exceptional charge and a large FG/WIP build that lifted Q1 gross margin to 54.93% (consolidated) and 54.69% (standalone). Q2 gross margin of 51.11% is the cleaner reading.
- **H1 average test.** H1 FY27 average quarterly revenue is Rs 192.19 Cr. Q2 revenue of Rs 217.32 Cr exceeds it by 13.1%. Dahej SEZ capacity rose from 461 KL (FY25) to 698 KL (FY26) (PPT L813 R597-R598, layout-scrambled mapping). The run-rate lifted after that addition, so the capex-commissioning test passes for the FY26 additions.
- **Capacity ceiling.** Q2 annualised revenue is Rs 869.28 Cr (217.32 x 4). The Q1 call put the existing-footprint ceiling at Rs 800-850 Cr [memory, MGMT]. Q2 already runs at or above that ceiling (PPT-A3-P-07).
- **Implied Q3 base.** To hold the Q2 run-rate, Q3 FY27 revenue must be at least Rs 217.32 Cr. To hold the margin trajectory management claims ("resume its healthy trajectory", PPT L142), Q3 operating EBITDA margin must be at or above 19.33% (Q1 level), and at least 20.0% to re-enter the guide band.

Checkpoint: QoQ table and diagnostics complete.

---

## STEP 4: OPERATIONAL DECOMPOSITION (PAT bridge, consolidated, Q2 FY27 vs Q2 FY26)

All components in Rs Cr from Mn arithmetic on RES L145-L164. Revenue contribution = change in revenue x prior-year operating margin (17.99%). Margin contribution = current revenue x margin change (+0.74 pp). Tax split = change in PBT at prior ETR (27.42%) plus ETR change on current PBT.

| Component | YoY change (Rs Cr) | Share of PAT change | Recurring? |
|---|---|---|---|
| Revenue contribution to operating EBITDA | +16.87 | 146.3% | Recurring |
| Margin change contribution | +1.60 | 13.9% | Recurring (net of solvent/freight hit) |
| D&A change | -1.74 | -15.1% | Recurring (post-capex) |
| Finance cost change | -2.20 | -19.1% | Recurring (post-debt; rising) |
| Other income change | +0.75 | 6.5% | NON-RECURRING typically |
| Tax on higher PBT at prior ETR | -4.19 | -36.3% | Mixed |
| Effective tax rate change (27.42% to 25.88%) | +0.45 | 3.9% | Mixed |
| Exceptional items | 0.00 | 0.0% | n/a (nil both quarters) |
| **Reported PAT YoY change** | **+11.53** | **100%** | |

Check: the rounded components sum to 11.54; Mn arithmetic gives exactly 115.34 Mn (PAT 214.51 - 99.17).

Mandatory questions:
- **Recurring vs non-recurring share.** Other income after tax at the Q2 ETR is about Rs 0.55 Cr, or 4.8% of the PAT change. About 95% of the YoY PAT change comes from core operations. This share is an upper bound. It assumes non-cash FX sits outside the operating lines (location ND, RES L268).
- **If other income reverts to the prior-year level.** Q2 FY27 PAT would be Rs 20.90 Cr (21.45 - 0.75 x (1 - 0.2588)). The run-rate barely moves.
- **D&A and finance: steady-state or ramping?** Both are still ramping. Finance costs rose from Rs 2.08 Cr (Q1) to Rs 2.71 Cr (Q2) as short-term debt rose; interest paid was Rs 5.00 Cr in H1 (RES L319). D&A is near steady-state for the current asset base (Rs 10.57 Cr Q1, Rs 10.79 Cr Q2). It will step up when capital work in progress capitalises (CWIP Rs 42.83 Cr at 30-Sep, RES L203, project split ND; Dahej-III budget Rs 200 Cr [memory]). The implied steady-state cannot be computed from the filing: ND.
- **Tax adjustments.** Deferred tax is a persistent charge: consolidated H1 deferred tax Rs 7.17 Cr = 56.8% of the H1 tax charge (L162/L163); standalone 79.7% (L464/L465), with standalone Q1 current tax nil (L463). P&L ETR is normal (25.21% consolidated H1 vs 25.17% statutory). The deferred tax asset fell from Rs 9.57 Cr to Rs 1.92 Cr (consolidated, RES L209) and from Rs 8.17 Cr to Rs 0.77 Cr (standalone, L500). At the H1 run-rate the standalone shield ends in Q3 FY27. From then cash tax steps up by about Rs 3.5 Cr a quarter with no change in P&L ETR (RES-A3-07). This is a CFO headwind, not a PAT headwind.

H1 FY27 vs H1 FY26 summary (consolidated): revenue +59.9%, operating EBITDA +84.6% (Rs 39.55 Cr to Rs 72.99 Cr), margin +254 bps (16.45% to 18.99%), core PBT +127.3% (Rs 20.60 Cr to Rs 46.84 Cr), PAT +125.9% (Rs 16.57 Cr to Rs 37.43 Cr) after the Rs 1.32 Cr exceptional charge.

Checkpoint: bridge and answers complete.

---

## STEP 5: CASH QUALITY AND BALANCE SHEET (H1 actuals; Reg 33 half-yearly statements)

The prior-period balance sheet is 31-Mar-2026. The filing gives no 30-Sep-2025 balance sheet, so September-2025 balance-sheet cells are ND. The cash flow prior period is H1 FY26.

### Consolidated

| Metric | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO (RES L289) | H1 FY26 13.38; FY26 31.49 | H1 FY27 **(3.68)** | -17.06 vs H1 FY26 | **RED: negative on revenue +59.9%** |
| CFO / PAT | H1 FY26 80.8%; FY26 74.9% | **-9.8%** | -90.6 pp | Below the lowest Pillar 2 band (0.65x) |
| CFO / operating EBITDA | H1 FY26 33.8%; FY26 33.8% | **-5.0%** | -38.9 pp | Bear side of the Q2 separating metric (<30%) |
| Cash generated before tax (L287) | H1 FY26 19.17 | 0.74 | -18.43 | WC absorbed Rs 72.73 Cr of Rs 73.47 Cr pre-WC profit (99.0%) |
| Capex, PPE incl CWIP (L291) | H1 FY26 56.00; FY26 113.77 | 30.85 | -25.15 vs H1 FY26 | Lower; project split ND |
| FCF (CFO - capex) | H1 FY26 (42.62); FY26 (82.29) | **(34.52)** | +8.10 vs H1 FY26 | Negative for the third half-year running |
| Working capital change (L286) | H1 FY26 (24.32); FY26 (61.93) | (72.73) | -48.41 | Inventories (52.84) L275; receivables (63.93) L276; payables +33.19 L281 |
| Receivable days (consolidated) | 31-Mar 85.9 d (FY26 revenue) | H1 basis 84.9 d; TTM basis 100.2 d; Q2 annualised 74.9 d | flat to +14 d by basis | See ruling-50 flag below |
| Inventory days (on COGS: L149+L150+L151) | 31-Mar 318.7 d | TTM 310.2 d (on revenue: 139.8 d vs 141.5 d) | -8.5 d | High but not rising |
| Payable days (on COGS) | 31-Mar 94.7 d | TTM 106.6 d | +11.9 d | Payables stretched (+Rs 27.28 Cr, L241-L242) |
| Cash conversion cycle | 31-Mar 309.9 d | TTM 303.8 d | -6.1 d | Structurally long (~300 d) |
| PPE (L201) | 574.18 | 558.96 | -15.22 | Depreciation exceeds additions |
| CWIP (L203) | 23.35 | 42.83 | +19.48 | CWIP build; project split ND; no major capitalisation |
| Non-current investments (L207) | 4.00 | 4.00 | nil | FY26 purchase (L295); investee, stake and earnings ND; 0.49% of equity |
| Net debt (L234 + L240 - L216 - L217) | 111.58 | **154.79** | +43.21 | Rising |
| Net debt / TTM operating EBITDA | 1.20x (FY26 93.16) | **1.22x** (TTM 126.60) | +0.02x | RED vs 0.65x band [memory]; 1.06x on H1 annualised EBITDA |
| Short-term share of gross debt | 95.8% (115.36 of 120.37) | 97.4% (165.53 of 169.99) | +1.6 pp | Capex and WC funded short (RES-A3-02) |
| Promoter pledge | ND | ND | ND | Not in the supplied documents; promoter holding 72.02% (PPT R734) |

TTM figures [A4 computation]: TTM revenue = FY26 505.86 - H1 FY26 240.38 + H1 FY27 384.38 = Rs 649.85 Cr; TTM operating EBITDA = 93.16 - 39.55 + 72.99 = Rs 126.60 Cr; TTM COGS = Rs 292.87 Cr.

H1 FY27 sources and uses (consolidated, Rs Cr, from Mn lines L289-L321): uses were CFO outflow 3.68, capex 30.85, other investing 0.49, dividend 4.68, interest paid 5.00 and LT repayment 0.51, about Rs 45.18 Cr net of a Rs 0.02 Cr employee-loan inflow. Net short-term borrowings of +Rs 50.13 Cr (L317) funded them, and cash rose Rs 4.95 Cr (L321).

### Standalone

| Metric | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO (RES L578) | H1 FY26 12.01; FY26 29.17 | **(8.57)** | -20.58 | RED |
| CFO / PAT | 85.3%; 74.6% | -33.2% | | |
| CFO / operating EBITDA | 33.2%; 32.6% | -15.5% | | |
| FCF | (43.99); (84.60) | (39.42) | | |
| WC change (L575) | (23.02); (61.06) | (62.52) | | Receivables (50.00) L565; inventories (54.94) L564 |
| Receivable days (standalone) | 31-Mar 105.7 d | H1 basis 97.6 d; TTM 110.2 d | | Above 100 on both TTM and 31-Mar |
| Inventory days (on COGS) | 31-Mar 267.8 d | TTM 272.9 d | +5.1 d | |
| Payable days (on COGS) | 31-Mar 90.6 d | TTM 103.1 d | +12.5 d | |
| Net debt (L523 + L529 - L507 - L508) | 115.88 | 160.12 | +44.24 | 1.48x std TTM EBITDA (1.30x at 31-Mar) |

**Dividend classification split (RES-A3-09).** Consolidated CFF shows dividend paid Rs 4.68 Cr (L314); standalone CFF shows Rs 0.86 Cr (L603). Both equity rolls deduct the full Rs 2/share dividend (Rs 4.68 Cr). The Rs 3.82 Cr difference sits in "other current financial liabilities" in the standalone operating section ((5.80) L571 vs (1.97) L282). On the consolidated classification, standalone CFO is Rs (4.75) Cr, not Rs (8.57) Cr. On the standalone classification, consolidated CFO is Rs (7.50) Cr, not Rs (3.68) Cr. Conservative bias: consolidated CFO is negative under either treatment. Which is correct: ND.

**Reclassification (RES-A3-10).** The FY26 audited column shows consolidated CFO Rs 31.49 Cr (74.9% of PAT). Memory holds "~Rs 35 Cr, 83% of PAT". The ~Rs 3.4 Cr gap may be the unquantified Note 7 reclassification or a memory basis difference. Verify against the FY26 annual report before trending CFO.

### Mandatory questions

- **Is CFO/PAT meeting the Pillar 2 cash multiplier assumption?** No. The valuation on file uses 0.80x [memory]. H1 FY27 CFO/PAT is -0.10x, below the lowest band (0.65x). FY26 filed was 0.75x and H1 FY26 0.81x. The H1 FY27 reading points to the 0.65x band. Flagged for /fttcp and Role 1 (OR-30); no recompute here.
- **Is the WC drag structural or growth-induced?** Both, and the filing cannot separate them. Growth-induced evidence: receivable days on the H1 basis are flat vs 31-March (84.9 d vs 85.9 d), and inventory days on revenue are flat (139.8 d vs 141.5 d). Revenue grew 59.9%, so rupee WC rose with scale. Structural evidence: CFO/EBITDA was only 33.8% in FY26 and in H1 FY26, before this growth burst. The cash conversion cycle is about 300 days on COGS. Standalone receivable days are above 100 on TTM (110.2 d). Top-3 customers are 79% of receivables and Customer 1 is 36% of revenue and receivables [memory, FY26 AR]. The test "if growth stopped tomorrow, would WC days still be high?": yes, a ~300-day cycle stays high. No rating-agency WC commentary is in the supplied documents (CRISIL upgraded to A-/Stable on 08-Sep [memory, AGENCY]). **Classification: INDETERMINATE-WITH-DIRECTION (leaning structural).** Missing evidence: receivable ageing and overdue split, Customer 1 receivable at 30-Sep, intercompany debtor days, the 30-Sep-2025 balance sheet, and the Note 7 reclass amounts. Per house rule this caps the verdict at PROCEED WITH CAVEATS or below.
- **Did CWIP capitalise as expected?** No major capitalisation was expected. PPE fell Rs 15.22 Cr. The Dahej-III budget is Rs 200 Cr [memory]. CWIP rose Rs 19.48 Cr between 31-Mar and 30-Sep (RES L203). The filing gives no project split, so the Dahej-III share is ND; H1 capex was Rs 30.85 Cr (RES L291).
- **Did net debt move within the projected range?** Notion holds no net-debt projection (ND). Against the 0.65x monitoring band, net debt/EBITDA is 1.22x TTM and rising in rupees (+Rs 43.21 Cr in H1). Finance costs will keep rising until the company draws a term loan for the capex and WC releases.

### Thesis-broken trigger (a): arithmetic read, ruling-50 flag (not resolved)

| Leg | Filed reading | Met? |
|---|---|---|
| H1 FY27 CFO negative | Rs (3.68) Cr consolidated (L289); Rs (8.57) Cr standalone (L578) | **Yes** |
| On rising revenue | +59.9% H1 YoY consolidated (L145) | **Yes** |
| Receivable days above 185 (as written in Notion and companies/TATVA.md) | Consolidated 84.9 d (H1 basis), 100.2 d (TTM), 74.9 d (Q2 annualised); standalone 97.6 d / 110.2 d | **No** on every basis |
| Q2 separating metric, bear: "CFO negative OR CFO/EBITDA <30% AND receivable days >100" | CFO negative: yes. CFO/EBITDA -5.0%: yes. Receivable days >100: consolidated TTM 100.2 d yes (by 0.2 d), H1 basis 84.9 d no; standalone TTM 110.2 d yes | Fires if read as "CFO negative" alone; fires on TTM days if the AND binds; does not fire on H1-basis consolidated days |

**FLAG (operator ruling 50 pending).** On the 185-day line as written, trigger (a) has NOT FIRED: two of three legs are met, and the days leg is far from met. On the 90/100-day bands, the bear side of the Q2 separating metric is met on the CFO leg, and the days leg turns on the day-count basis (TTM vs H1). The checklist itself carries inconsistent baselines: item 1 says "receivable days from ~185", while the 13/14-Oct notes give FY26 consolidated 86 d and standalone 106 d [memory]. A4 does not resolve the ruling. The decision impact is bounded: the name is not held and already carries WATCHLIST / AVOID.

Checkpoint: cash quality table and answers complete.

---

## STEP 5.5: DOWNSTREAM SIGNAL RECONCILIATION

### 5.5A. Tracker pull
**Tracker rows not supplied.** The orchestrator passed no Downstream Signal Tracker rows for TATVA. Signal name, cadence, latest observation, direction and health: ND for every row. The fewer-than-three-signals flag therefore applies: the review cannot show three tracker signals for this company. OR-17 (three EXTERNAL tracker signals per entity at the /fttcp Role 5.5 gate) will need this filled before /fttcp.

### 5.5B. Target vs signal reconciliation
Target reported: STRONG on revenue (+75.9% YoY Q2, RES L145) and profit (+116.3% YoY PAT, L164); WEAK on cash (H1 CFO Rs -3.68 Cr, L289). Signal trajectory: ND (no rows). The four-outcome matrix cannot be applied. The only signal-type evidence in the documents is management commentary, not an independent tracker reading: Euro 7 SDA demand "already translating into a meaningful contribution" (PPT L160-161, MGMT); solvent shortage +60-100% and freight +100% (PPT L136-140, MGMT).

### 5.5C. New signal candidates (payload rows only; written only through the operator-approval write gate)
No row was written. Candidates surfaced by this quarter's documents:
1. **Specialty solvent prices (solvents unnamed by the company)**: event/monthly; tests the "normalise within the third quarter" claim (PPT L141) and Q3 margin. Case: ND (cannot tell if an existing row covers it without the tracker pull).
2. **US and Europe container freight rates**: weekly/monthly; tests the same claim (PPT L139-141).
3. **Euro 7 light-vehicle production and zeolite catalyst demand**: quarterly; tests SDA, now about 45% of Q2 revenue (PPT L1106 R715). Notion already lists an "SDA Euro 7 tailwind" [memory], so this may be Case A (add to existing).
State per protocol: "No new signal written this quarter. Three candidate signals listed for the Role 5.5 Step 4 gate."

### 5.5D. Forward view weighting
With no tracker readings, Step 6 weighs the filed numbers only. The single-quarter print carries more weight than it should. This is a reason for caution, not for confidence.

---

## STEP 6: RECONCILIATION VS THESIS

### 6A. Variance vs Notion projections

| Metric | Bear proj | Base proj | Bull proj | Actual (anchor) | Lands in |
|---|---|---|---|---|---|
| Revenue (FY27) | ND | ND | ND | H1 FY27 Rs 384.38 Cr, +59.9% YoY (RES L145) | Not gradeable: no projection table on the Notion page. vs MGMT guide 25-30% FY27 growth [memory]: AHEAD |
| Operating EBITDA margin (FY27) | ND | ND | ND | H1 18.99%; Q2 18.72% | Not gradeable. vs MGMT guide 20-22% [memory]: BELOW for a second quarter |
| PAT (FY27) | ND | ND | ND | H1 Rs 37.43 Cr (L164); TTM Rs 62.92 Cr | Not gradeable |
| EPS (FY27) | ND | ND | ND | H1 Rs 16.00 (L181); TTM Rs 26.90 | Not gradeable |
| Net debt | ND | ND | ND | Rs 154.79 Cr (L234, L240, L216, L217) | Not gradeable; vs 0.65x band: 1.22x (RED) |
| ROCE | FY28 6.3% | FY28 8.5% | FY28 10.6% | H1 FY27 annualised 11.6% (EBIT incl OI / net capital employed: (51.37 + 4.79) x 2 / 969.44); 10.6% on operating EBIT; TTM 9.5% on closing capital employed | Period and basis mismatch (FY28 projection vs FY27 run-rate): not gradeable. Directionally at or above the FY28 bull figure |

TTM [A4 computation]: PAT 42.05 - 16.57 + 37.43 = Rs 62.92 Cr; EPS 17.98 - 7.08 + 16.00 = Rs 26.90. Net capital employed = equity 814.65 + debt 169.99 - cash and bank 15.21 = Rs 969.44 Cr (RES L230, L234, L240, L216, L217).

**Probability re-weighting rule.** Not testable: the page holds no Bear/Base/Bull P&L table, so no "below bear" count exists. First quarter of the rule for this name. FLAG: the Notion page needs a projection table before Q3 for Step 6A to work.

### 6B. Watchlist item status (Notion 8-item checklist)

| # | Watchlist item | Green threshold | Red threshold | This quarter reading (anchor) | Status |
|---|---|---|---|---|---|
| 1 | Cash conversion | Receivable days from ~185 toward 155-160; OCF/EBITDA positive; ECL vs 61% top-3 | Days above 185 on rising revenue | CFO Rs -3.68 Cr, CFO/EBITDA -5.0% (L289); receivable days 84.9 d H1 / 100.2 d TTM (L215); ECL matrix ND | **RED** on OCF/EBITDA. Days leg below 185 but baseline inconsistent (ruling 50) |
| 2 | ROCE | Clearing 8% in FY27, rising toward 15% | Stuck 6-8% through FY28 | H1 annualised 11.6% (incl OI) / 10.6% (operating); Q1 ~10.9% [memory] | GREEN (basis caveat) |
| 3 | SDA revenue | FY27 >= +20% to Rs 250-300 Cr; new-customer invoicing ~Aug 2026 | Third sequential decline | H1 SDA Rs 154.6 Cr (PPT L614 R531) vs FY26 Rs 204.5 Cr (R530); Q2 SDA about Rs 97 Cr vs Q1 about Rs 57 Cr [derived, see 6D]; new-customer invoicing ND | GREEN on revenue; new-customer leg ND; one quarter |
| 4 | EBITDA margin | Holding 20-22% | Below 18% | Q2 18.72%, H1 18.99% (Step 1) | AMBER (second quarter below band, above red) |
| 5 | Dahej-III milestones | On schedule; equipment PO by Q3 FY27 | Formal extension or overrun | "progressing in line with the planned schedule" (PPT L194, MGMT); CWIP +Rs 19.48 Cr in H1 (project split ND, RES L203); PO status ND | UNKNOWN (milestone not disclosed; no extension disclosed) |
| 6 | Rating; net debt/EBITDA | No downgrade below BBB+/Stable; net debt/EBITDA under ~0.65x | Downgrade; leverage above band | CRISIL A-/Stable & A2+ (PPT L563 R516; AGENCY); net debt/TTM EBITDA 1.22x | GREEN on rating / **RED** on leverage |
| 7 | Standalone PBT; parent share | Std PBT above Rs 5-10 Cr; parent share above 50% | Below | Std Q2 PBT Rs 20.44 Cr (L461); parent share 71.7% Q2, 69.0% H1 | GREEN, with caveat: parent operating margin falling (RES-A3-04) and parent OI includes an intra-group stream (RES-A3-05) |
| 8 | Peer demand tone; promoter pay | Peers (Clean Science, Neogen) flip to recovery; pay realigns with PAT | Peers soft while Tatva claims recovery | No peer or pay data in the supplied documents | UNKNOWN |

Prior-quarter question answer status (protocol rule: track across quarters). No call took place, so no question got a management answer. "Filed number" means the filing now carries a number that bears on the question, without management explanation.

| Q1 FY27 question [memory] | Q2 status | Basis |
|---|---|---|
| 1 Nature of Rs 1.32 Cr exceptional | NOT ADDRESSED (2nd quarter) | No note in either entity (RES L158, L460); deck silent (PPT-A3-P-04) |
| 2 Decompose 484 bps gross margin expansion | PARTIALLY ANSWERED (deck only) | Q2 gross margin fell 382 bps QoQ; deck blames solvents and freight (PPT L136-140, MGMT) |
| 3 Dahej-III funding mix, peak net debt/EBITDA | NOT ADDRESSED | LT borrowing proceeds nil H1 (RES L315) |
| 4 Standalone PBT Rs 14 Cr, parent share 65% driver | NOT ADDRESSED | Filed number: parent share 71.7% Q2 |
| 5 Tax rate 24.3% vs 37.8% sustainable | NOT ADDRESSED | Filed number: H1 ETR 25.21% |
| 6 Receivable days at 30-Jun and WC plan | NOT ADDRESSED (2nd quarter) | Filed number: 30-Sep receivables Rs 178.38 Cr; no plan |
| 7 SDA share 41% to 35% | ANSWERED (Q1) | Q2 share 45% (PPT L1106) |
| 8 Jolva status + semi dispatch | ANSWERED (Q1) | Deck restates "in line with planned schedule" |
| AR Section J items: Customer 1 36%; CFO departure; R&D 1.58%; subsidiary receivables Rs 25 to 61 Cr; Rs 1,000 Cr ceiling; S/C PAT ratio; H1 CFO/EBITDA | NOT ADDRESSED (all) | Deck and filing silent; only filed numbers (R&D H1 1.19%, PPT L1108; CFO/EBITDA -5.0%) |

Governance signal: the exceptional-item, standalone-share and receivable-days questions have now gone two quarters without an answer. Per protocol, log in the Promoter Verdict update (payload in Step 9).

**Q1 call guidance log (17 items) scored against this filing:**

| # | Guidance [memory, MGMT] | Q2 evidence (anchor) | Status |
|---|---|---|---|
| 1 | FY27 revenue growth 25-30% | H1 +59.9% (RES L145); not restated, "similar momentum" (PPT L141) | AHEAD; guide stale |
| 2 | FY27 EBITDA margin 20-22% | H1 18.99%, Q2 18.72%; not restated, "resume its healthy trajectory" (PPT L142) | BEHIND; H2 needs 20.9-24.7% if H2 revenue = 2 x Q2 (PPT-A3-P-07) |
| 3 | ESS FY27 Rs 40-50 Cr | H1 ESS Rs 13.2 Cr (PPT L674 R542, labelled "Q1FY27" but H1 per PPT-A3-P-15) | BEHIND; H2 needs Rs 26.8-36.8 Cr (2.0-2.8x H1) |
| 4 | Three pharma molecules FY27 (2 more by Q3 end) | "our pharma product beginning to contribute" (PPT L174), singular | NOT UPDATED; due 31-Dec-2026 |
| 5 | Pharma molecule revenue FY27 Rs 70-80 Cr | No pharma split; PASC H1 Rs 124.7 Cr includes agro and speciality (PPT L705) | UNVERIFIABLE (ND) |
| 6 | Pharma peak ~Rs 200 Cr | none | NOT TESTABLE |
| 7 | Dahej-III groundbreak 20-Jul-2026 | Delivered per Q1 promise-vs-delivery [memory]; CWIP +Rs 19.48 Cr in H1 (project split ND, RES L203) | DELIVERED (Q1) |
| 8 | Commissioning 21 months official / 18 push | "in line with the planned schedule" (PPT L194) | ON TRACK (claim only) |
| 9 | Dahej-III peak revenue Rs 300 Cr | none | NOT TESTABLE |
| 10 | Semiconductor commercialisation not before Q4 CY2028 | "working patiently to build" (PPT L191) | CONSISTENT |
| 11 | Hybrid battery initial Oct-Nov CY2026 | "progressing towards commercialisation" (PPT L168), no date | WINDOW OPEN; not confirmed |
| 12 | Hybrid battery full-scale late CY2027 | none | NOT TESTABLE |
| 13 | 3-4 year CAGR 20-25% | none | NOT TESTABLE |
| 14 | Target ROCE 20-22% (aspirational) | H1 annualised 11.6% | FAR |
| 15 | Target asset turnover 1.5x | H1 annualised revenue / (PPE + ROU) = 768.75 / 588.80 = 1.31x; Q2 annualised 1.48x (RES L201-L202) | NEAR on Q2 run-rate |
| 16 | Semi pipeline 5 products (1 plant, 1 pilot, 3 dev) | "all five products in our development portfolio" (PPT L185) | CONSISTENT |
| 17 | 8-9 mature products before 2028 | none | NOT TESTABLE |

Score: 1 delivered, 1 ahead, 2 behind, 1 far (#14 ROCE target), 1 near (#15 asset turn), 3 consistent or on track (claim only), 1 window open, 1 not updated, 1 unverifiable, 5 not testable (17 items). Also from the Q1 call [memory]: capacity limit on the existing footprint Rs 800-850 Cr; Q2 annualised revenue is Rs 869.28 Cr.

### 6C. Thesis-broken trigger check

| Thesis-broken condition [memory] | Threshold | Current reading | FIRED? |
|---|---|---|---|
| (a) H1 FY27 CFO negative on rising revenue with receivable days above 185 | All three legs | CFO Rs -3.68 Cr (yes); revenue +59.9% (yes); days 84.9 d H1 / 100.2 d TTM (no) | **NOT FIRED as written.** FLAG: under the 90/100-day bands (ruling 50 pending) the bear separating metric is met on the CFO leg; days leg depends on TTM vs H1 basis. Not resolved by A4. |
| Sub-trigger: own-subsidiary debtor days >90 | >90 d | Intercompany receivable proxy fell from Rs 24.69 Cr to Rs 10.49 Cr (std minus cons receivables, RES L506 vs L215); sales to subsidiaries ND, so days ND | UNKNOWN (not testable) |
| (b) ROCE fails to clear 8% by FY28 | <8% at FY28 | H1 annualised 11.6% / 10.6% operating; TTM 9.5% | NOT FIRED (date not reached; trend above floor) |
| Q1 8D: reassess if new-mix ROCE ceiling <12% over trailing 4 quarters | <12% TTM | TTM ROCE 9.5% on closing capital employed (TTM EBIT incl OI Rs 92.34 Cr / Rs 969.44 Cr); 8.9% on operating EBIT | **CONDITION READING BELOW 12%.** This is a "reassess" line, not an exit. FLAG for /fttcp: destination-PE review |
| Rating downgrade below BBB+/Stable (companies/TATVA.md) | Downgrade | CRISIL A-/Stable (PPT L563) | NOT FIRED |
| Jolva 4th slip past FY27 | Formal slip | "in line with the planned schedule" (PPT L194) | NOT FIRED |
| Peers soft while Tatva claims recovery | Peer tone | ND | UNKNOWN |

TTM EBIT incl OI [A4 computation, Mn arithmetic]: TTM operating EBITDA 1,265.98 Mn - TTM D&A 401.83 Mn (368.47 - 180.24 + 213.60) + TTM OI 59.20 Mn (35.49 - 21.63 + 45.34) = 923.35 Mn = Rs 92.34 Cr. Average capital employed is ND (no 30-Sep-2025 balance sheet), so closing capital employed is used. This understates ROCE in a growth year.

No condition has FIRED on its written terms. The protocol "stop and recommend exit" does not apply; the name is not held in any case.

### 6D. Growth trigger status

Q2 product split [derived]: H1 values are FILED in the deck (PPT L582, L614, L674, L705); Q1 values are [memory] (Notion Q1 reference); Q2 = H1 minus Q1. Shares are the deck image (PPT L1106 R714-R718). Exact Q2 segment revenue is ND in the filings.

| Product line | H1 FY27 (Rs Cr) | Q1 FY27 [memory] | Q2 FY27 derived | Q2 share (R714-R718) | QoQ |
|---|---|---|---|---|---|
| PTC | 88.1 | 42.8 | 45.3 | 21% | +5.8% |
| SDA | 154.6 | 57.8 | 96.8 | 45% | +67.5% |
| ESS | 13.2 | 6.3 | 6.9 | 3% | +9.5% |
| PASC | 124.7 | 58.4 | 66.3 | 30% | +13.5% |
| Others (residual) | 3.8 | 1.8 | 2.0 | 1% | n/a |
| Total | 384.38 (RES L145) | 167.06 | 217.32 | 100% | +30.1% |

SDA supplied about Rs 39.0 Cr of the Rs 50.26 Cr QoQ revenue gain (about 78%), consistent with PPT-A3-P-14.

**Bear counter (A5 M3).** From filed figures alone, H1 SDA of Rs 154.6 Cr at 40% of H1 revenue (PPT L614, L623) and a 45% Q2 share (PPT L1106) imply Q2 SDA of about Rs 97-99 Cr and Q1 of about Rs 56-58 Cr (about 34% of Q1 revenue, close to the FY26 quarterly average of Rs 51.1 Cr). The step-up sits in one quarter. The Euro 7 link is MGMT (PPT L160-L161); no customer, volume or contract data is filed. Bull reading: Euro 7 run-rate demand. Bear reading: a one-quarter order spike or a customer pre-build. Separating observation: Q3 FY27 SDA at or above about Rs 97 Cr (share at least 45% on revenue at or above Rs 217.32 Cr), with new customers named (monitorable M25).

| Trigger [memory] | Original confidence | Confirming evidence | Killing evidence | Updated status |
|---|---|---|---|---|
| SDA Euro 7 demand | ND | SDA H1 Rs 154.6 Cr = 76% of FY26 SDA; Q2 share 45%; "EURO 7 ... already translating into a meaningful contribution" (PPT L160-161) | Step-up sits in one quarter (Q1 about 34% share, Q2 45%); Euro 7 link MGMT only; new-customer leg ND; SDA 45% of Q2 revenue; whether Customer 1 (36% of FY26 revenue [memory]) is an SDA buyer is ND | **FIRED on revenue (one quarter, MGMT attribution); durability unproven** |
| Dahej-III (Jolva) Rs 200 Cr, 344 KL, commissioning Q3-Q4 FY28 | ND | Groundbreak 20-Jul delivered [memory]; "in line with the planned schedule" (PPT L194); CWIP +Rs 19.48 Cr in H1 (project split ND) | No milestone, spend or funding disclosed; no term debt drawn (RES L315) | ON TRACK (claim only) |
| Pharma molecules FY27 Rs 70-80 Cr (3 molecules) | ND | First molecule "beginning to contribute" (PPT L174) | Singular wording; no revenue split; two more due by 31-Dec-2026 | ON TRACK (unconfirmed; bear lean) |
| ESS FY27 Rs 40-50 Cr; hybrid battery Oct-Nov CY2026 | ND | "progressing towards commercialisation" (PPT L168) | ESS Q2 about Rs 6.9 Cr; H1 Rs 13.2 Cr; H2 must be 2.0-2.8x H1; no date in deck | **WEAKENED** |
| Semiconductor (5 products; not before Q4 CY2028) | ND (optionality, unscored) | "all five products ... advancing" (PPT L185-186) | No supply agreement, capex line or revenue; R&D 1.19% of H1 revenue (PPT L1108) | ON TRACK as optionality; no conversion condition met |

Checkpoint: 6A to 6D complete.

---

## STEP 6.5: EXPECTATION LEDGER REVIEW AND A21 BASE REFRESH

**Deferred to /fttcp and Role 1 (operator ruling OR-30).** Pillar-relevant facts flagged for that session (no recompute here):
- A21 run-rate inputs: Q2 FY27 consolidated PAT Rs 21.45 Cr, EPS Rs 9.17 (annualised Rs 36.68); TTM PAT Rs 62.92 Cr, TTM EPS Rs 26.90. H1 includes the Rs 1.32 Cr pre-tax exceptional item (tax effect ND). The business is not seasonal on the evidence, but Q2 carries a solvent/freight cost the company calls temporary, and the location of the Rs 3.91 Cr H1 unrealised FX gain is ND. At CMP Rs 1,841 [memory, 14-Oct] the trailing P/E is 68.4x TTM and 50.2x on Q2 annualised EPS.
- Ledger items whose confirm-by dates fall in the next window: hybrid battery initial supply (Oct-Nov CY2026), two pharma molecules (by 31-Dec-2026), ESS FY27 Rs 40-50 Cr, FY27 EBITDA margin 20-22%. This filing shows none of them as CONFIRMED. The ESS item reads as at risk of MISSED.

## STEP 7: FOUR-PILLAR DESTINATION PE RE-VALIDATION

**Deferred to /fttcp and Role 1 (operator ruling OR-30).** Pillar-relevant facts flagged:

| Pillar / input | On file [memory] | This quarter's fact (anchor) | Direction flagged |
|---|---|---|---|
| Pillar 1 ROCE (FTTCP verdict sole authority) | 13.51% blend; current leg 6.6%; FY28 base 8.5%; ROCE RECOVERING | H1 annualised 11.6% (10.6% operating); TTM 9.5% on closing capital employed | Current leg is stale (6.6% vs 9.5-11.6%): supports RECOVERING; TTM below the 12% reassess line |
| Cash multiplier | 0.80x (cash MIXED, 01-Sep) | H1 CFO/PAT -0.10x; FY26 filed 0.75x; CFO/EBITDA -5.0% | Points down to 0.65x |
| Growth visibility premium | Not stated | Revenue +59.9% H1; Q2 at or above the stated capacity ceiling; SDA step-up one quarter old; Dahej-III revenue not before FY29 [memory] | Near-term growth visibility capped by capacity until FY28-29 |
| Strategic premium | Pillar 3 +0x | No semiconductor conversion condition met (PPT L185-191) | Hold at 0 |
| UA multiplier | Does not apply | No change | Hold |
| Sector cap | 35x specialty chemicals | Single segment specialty chemicals (RES L357) | Hold |
| Leverage (enters cash and risk reads) | 1.20x at FY26 | 1.22x TTM; 97.4% short-term | Flag |
| Hurdle ratio | STOP (base 0.216 vs 1.953) | CMP Rs 1,841 = 12.5x entry max Rs 147 [memory] | No recompute; no evidence the STOP band moves |

---

## STEP 8: POSITION DECISION

Decision Status verified at Step 0A: **WATCHLIST / AVOID, not held.** Branch: **8A-W.**

### 8A-W logic applied
1. Thesis-broken condition FIRED? **No, on the written terms.** Trigger (a) meets two of three legs. Under the pending 90/100-day reading the bear separating metric is met on the CFO leg (ruling 50, flagged, not resolved).
2. Below bear on 2+ metrics? **Not gradeable**: the Notion page holds no Bear/Base/Bull P&L table.
3. Between bear and base / at or above base? Not gradeable for the same reason. Against management guidance: revenue ahead, margin behind, cash far behind.

**Output of the branch:**
- **Updated entry zone:** deferred to Role 1 (OR-30). The page carries two zones (properties Rs 118-147; verdict block Rs 97-121, self-flagged stale). Ruling 51 on FV is open. FLAG: reconcile before the next Notion write.
- **Updated gate:** the Q2 separating metric resolved to the **bear side on cash** (CFO negative; CFO/EBITDA -5.0% < 30%). The bull side (CFO/EBITDA >70% AND days <=90) failed on CFO. Q3 has no cash flow statement under Reg 33, so the next cash gate is the FY27 annual results (Reg 33 limit 30-May-2027). New gate: FY27 consolidated CFO/operating EBITDA and receivable days.
- **Proposed Decision Status (operator sets it):** unchanged **WATCHLIST / AVOID**. Conditional: if ruling 50 adopts the 90/100-day bands, the bear separating metric is met on the CFO leg; the operator may then harden to AVOID (drop WATCHLIST). Re-entry consideration would need FY27 CFO/EBITDA above 70% with consolidated receivable days at or below 90, plus net debt/EBITDA trending toward 0.65x.

### 8B. Add-back / trim trigger refinement
- Original re-open trigger [memory]: "ROCE reverting toward the pre-depression band and cash conversion turning, plus any semiconductor qualification milestone."
- Revised re-open trigger (proposed): the original, plus (i) FY27 consolidated CFO/operating EBITDA at or above 70% with receivable days at or below 90 on a stated basis (ruling 50); (ii) net debt/TTM EBITDA back under 1.0x; (iii) standalone operating EBITDA margin back above 18%. Reason: this quarter shows profit growing faster in non-manufacturing subsidiaries than in the parent, and cash turning negative on debt.
- Original trim ladder: "Any further downgrade to BBB or lower = auto-trim (moot given no position)". Revised: none (not held).

### 8C. Single cleanest metric for Q3 FY27
**Consolidated operating EBITDA margin in Q3 FY27** (PBT before exceptional + D&A + finance cost - other income, over revenue). Reason: Q3 carries no cash flow statement, and management dated the margin recovery to "within the third quarter" (PPT L141). This one number tests the "temporary" claim, the pass-through hedge (PPT L208) and the FY27 20-22% guide.
- Bull threshold: **20.0% or higher** (re-enters the guide band; confirms the cost hit was temporary).
- Bear threshold: **below 18.0%** (the Notion RED line; "temporary" claim fails; the 20-22% FY27 guide becomes unreachable).
The decisive cash reading follows at FY27 results (by 30-May-2027): consolidated CFO/operating EBITDA, bull above 70%, bear below 30%.

---

## ROLE 5 SLOT (CONCALL ANALYSIS): NOT RUN

**No transcript exists.** The company cancelled the Q2 FY27 earnings call scheduled for Monday 19-Oct-2026 at 17:00 IST "due to unforeseen circumstances" (NTC L35-40). The notice was signed at 16:03:53 IST (NTC L58-59), 56 minutes before the start. It gives no new date and no substitute channel (NTC-A3-01, NTC-A3-04). Role 5 was not loaded. The notice is treated as a filed document:
- Promise-vs-delivery log: the 13-Oct-2026 intimation (NTC L34-36) is a disclosure commitment. Status: **MISSED (cancelled, no reschedule)**. Logged for the Role 5 tracker; credibility-ratio recompute deferred to the next Role 5 run.
- Silence audit: all 8 checklist items and all 8 Q2 questions got no management answer (NTC-A3-05). Cash conversion and receivable days: second consecutive quarter without cash Q&A (Q1 call silent [memory]). The Notion page's own rule says a second quarter without cash Q&A strengthens the structural-cash leaning. The H1 filing shows negative CFO on rising revenue. NTC-A3-05 set its upgrade condition as "H1 FY27 cash flow shows negative CFO ... on rising revenue". **That condition is met: the silence is reclassified CONFIRMATORY-NEGATIVE.** This adds weight to the structural lean in Step 5. It does not fire trigger (a) by itself.
- Presentation as the only management commentary this quarter: the deck's CMD message (PPT L111-L221) opens "Good evening, ladies and gentlemen" (L111) and reads as a prepared call script [INFERENCE]. It carries the dated claims logged in the commitment register below.

### Presentation findings feeding Role 4 (summary)
- **Same-day restatement (PPT-A3-P-01, P-02).** Two H1 ratios changed between the 18:05 and 20:54 decks: RoE 2.6% to 6.3%; Debt/EBITDA 4.30 to 1.16 (PPT L76-81). The letter calls them "typographical errors" (PPT L41). Both changes make the ratios look better. The earlier values tie to wrong cells (Q2 PAT / closing net worth = 2.64%; H1 debt / H1 FY26 EBITDA = 4.30). The corrected 6.3% still fails the PAT / closing net worth basis that reproduces FY23-FY25. On that basis FY26 RoE is 5.4% (deck prints 7.2%) and H1 FY27 is 4.6% (9.2% annualised). The cover letter says there are "no changes in other financial numbers" (PPT L45), and the same deck leaves two wrong period labels uncorrected (PPT-A3-P-15). Classification: disclosure-control weakness, not a change in filed financial data. The results filing is unaffected.
- **Debt/EBITDA basis change (PPT-A3-P-03).** FY23-FY25 use EBITDA including other income; FY26 and H1 use EBITDA excluding it. The direction is conservative.
- **CMD cost claim checked (PPT-A3-P-13).** "decrease in employee cost by 2% accompanied by decrease in other expenses by 2%" (PPT L134). Against the filing, employee cost fell 1.63 pp of revenue QoQ (10.02% to 8.39%) and other expenses fell 1.58 pp (25.58% to 24.00%). In rupees both rose: employee cost +8.9% and other expenses +22.0% QoQ (RES L152, L155). The claim holds only as a share of revenue, rounded up.
- **R&D intensity (PPT-A3-P-10).** R&D capital and revenue spend H1 FY27 Rs 4.59 Cr = 1.19% of H1 revenue (PPT L1108 R724); FY26 Rs 7.83 Cr (R723). The "FY27 R&D <2% for a second year" watch item is on course to fire at FY27 close.
- **Shareholding (PPT-A3-P-18).** Promoter 72.02%, MF 2.87%, FPI 4.38%, public 19.58%, others 1.15% (image successor R734-R738). Verify FPI against the NSE Sept-2026 shareholding pattern.

---

## STEP 8.5: QUESTIONS FOR MANAGEMENT

Ordered by importance. Every A3 FORWARD-SIGNAL and AMBIGUOUS finding maps to at least one question (coverage check below the table). Categories A-G per protocol.

| # | Cat | Question | Why it matters | Bull answer | Bear answer | From finding |
|---|---|---|---|---|---|---|
| 1 | D | H1 FY27 consolidated CFO was Rs -3.68 Cr against operating EBITDA of Rs 72.99 Cr, and working capital absorbed Rs 72.73 Cr of Rs 73.47 Cr pre-WC profit. What FY27 CFO/EBITDA do you commit to, in per cent? | Decides trigger (a), the Pillar 2 band and the separating metric | A number at or above 50% with a dated WC release plan | No number, or "growth needs working capital" | PPT-A3-P-19, NTC-A3-05 |
| 2 | D | Receivables rose Rs 59.35 Cr in H1 to Rs 178.38 Cr. What is Customer 1's receivable at 30-Sep, and what amount is overdue beyond terms? | Tests concentration (36% of revenue and receivables in FY26 [memory]) and receivable quality | Customer 1 share falling; overdue under 5% | Customer 1 share rising, or overdue not disclosed | PPT-A3-P-19, PPT-A3-P-20 |
| 3 | C | Q2 operating EBITDA margin was 18.72%. If H2 revenue equals twice Q2, H2 needs 20.9-24.7% to reach the 20-22% FY27 band. Does the 20-22% FY27 band stand: yes or no? | Tests "temporary" and the margin guide | Yes, with Q3 at or above 20% | No, or the band is quietly dropped | PPT-A3-P-07, PPT-A3-P-13, PPT-A3-P-06 |
| 4 | C | Solvent prices rose 60-100% in Q2. What per cent of that increase did you recover through customer prices in Q2, and what is the contract repricing lag in days? | Tests pass-through ("progressively where appropriate", PPT L208) | Majority recovered; lag under 60 days | Minority recovered; lag a quarter or more | PPT-A3-P-11, PPT-A3-P-06 |
| 5 | E | The US and EU subsidiaries have no materials, payroll or debt but earned 28.3% of Q2 group PAT (Rs 6.06 Cr). What transfer-pricing method applies, and what were intercompany debtor days at 30-Sep? | Profit location; >90-day sub-trigger | Arm's-length method stated; days under 90 | Margin parked in trading arms; days over 90 or not given | RES-A3-06, RES-A3-03 |
| 6 | A | Standalone operating EBITDA margin averaged 19.60% in H2 FY26, then fell to 16.38% in Q1 and 15.05% in Q2, while the group held 18.72%. What drove the parent decline? | The manufacturing entity's margin is the durable one | Named one-off (solvents) with a recovery date | Structural: transfer pricing shifts margin offshore | RES-A3-04 |
| 7 | A | In H2 FY26 the subsidiary profit gap fell to Rs 0.48 Cr. Will a year-end true-up (transfer pricing or unrealised-profit elimination) reduce the H1 FY27 subsidiary profit of Rs 11.60 Cr? | Year-end reversal risk | No true-up mechanism | Yes, or no answer | RES-A3-03 |
| 8 | A | Standalone other income exceeds consolidated by Rs 2.20 Cr in H1 FY27 (nil in H1 FY26), and H1 cash flow deducts an unrealised FX gain of Rs 3.91 Cr. What is the intra-group income, and on which P&L line (other income or other expenses) does the FX gain sit? | Quality of parent profit; whether core PBT carries a non-cash gain | Contractual service fee; FX in other income | Dividend or FX on intercompany balances; FX inside other expenses | RES-A3-05 |
| 9 | A | What was the Rs 1.32 Cr exceptional charge in Q1 FY27? Cash or non-cash, tax treatment, will it recur? | Second filing with no note | Named one-off, non-recurring | No answer for a third quarter | RES-A3-01, PPT-A3-P-04 |
| 10 | F | Short-term borrowings rose Rs 50.17 Cr in H1 and long-term proceeds were nil. What term-loan amount is sanctioned for Dahej-III, what is the draw schedule, and what peak net debt/EBITDA do you expect? | Funding risk; 97.4% of debt is short-term | Sanctioned term loan with schedule; peak under 1.5x | No sanction; capex stays on short-term lines | RES-A3-02, PPT-A3-P-05 |
| 11 | B | CWIP rose Rs 19.48 Cr in H1, with no project split. How much is Dahej-III, has the equipment PO been placed, what is spend to date against the Rs 200 Cr budget, and what is the commissioning month? | GREEN test: PO by Q3 FY27 | PO placed; month stated | No milestone; schedule vague | PPT-A3-P-08 |
| 12 | D | Standalone deferred tax asset is Rs 0.77 Cr. From which quarter does current tax rise to the full P&L charge? | Cash tax step-up of about Rs 3.5 Cr a quarter | Date given; modelled in guidance | Not tracked | RES-A3-07 |
| 13 | B | Q2 annualised revenue is Rs 869 Cr against your Rs 800-850 Cr existing-footprint ceiling. How much of Q2 growth was price and how much volume, and how do you keep "similar momentum" before Dahej-III? | Capacity ceiling vs guidance | Debottlenecking with numbers; volume-led | Price-led; momentum cannot hold | PPT-A3-P-07, PPT-A3-P-14 |
| 14 | E | SDA was about 45% of Q2 revenue against about 34% in Q1. Is Customer 1 an SDA buyer, how many new SDA customers invoiced in H1, and what volume and tenor do your Euro 7 SDA contracts carry? | One-quarter step-up; concentration in one product and one customer | Multi-customer, multi-year contracts; new customers named | Single customer, spot or pre-build orders | PPT-A3-P-14 |
| 15 | B | ESS revenue was Rs 13.2 Cr in H1 against a Rs 40-50 Cr FY27 guide. Does the guide stand, and what is the date of first commercial hybrid-battery supply? | ESS guidance credibility | Date in Q3 FY27; guide holds | Guide cut or no date | PPT-A3-P-09 |
| 16 | B | R&D spend was 1.19% of H1 revenue while the CMD says the pipeline will "accelerate". What is the FY27 R&D budget in rupees? | Semiconductor and pipeline credibility | Budget at or above 2% of revenue | Budget under 2% for a second year | PPT-A3-P-10 |
| 17 | B | The Q1 call guided two further pharma molecules by Q3 end. The deck names one product. What is the status of molecules two and three? | Due 31-Dec-2026 | Both on schedule with dates | Slipped or not named | PPT-A3-P-20 |
| 18 | D | The Rs 3.82 Cr difference in dividend paid sits in financing (consolidated) and operating (standalone). Which classification is correct, and what is the balance? Which prior-period lines did Note 7 reclassify, and by how much? | CFO reading moves between Rs -3.68 Cr and Rs -7.50 Cr | Consolidated treatment confirmed; reclass amounts given | No answer | RES-A3-09, RES-A3-10 |
| 19 | G | Give the formula for RoE and Debt/EBITDA in each p14 column. Why do FY26 and H1 FY27 use a different basis from FY23-FY25, and which control failed before the 18:05 filing? | Disclosure control; the restated ratios were both flattering | Formula given; basis aligned in the Q3 deck | "Typographical" with no formula | PPT-A3-P-01, PPT-A3-P-02 |
| 20 | G | What were the "unforeseen circumstances"? Was the cancellation decided in the 11:30-15:45 board meeting or after it? When will the call be rescheduled, or will you publish written answers? | Transparency; the call was the only Q&A channel | Cause named; date given within 2 weeks | No cause; no date | NTC-A3-01, NTC-A3-02, NTC-A3-03, NTC-A3-04, RES-A3-08 |

Coverage check (FORWARD-SIGNAL and AMBIGUOUS findings, 29): RES-A3-01 (Q9), -02 (Q10), -03 (Q5, Q7), -04 (Q6), -05 (Q8), -06 (Q5), -07 (Q12), -08 (Q20), -09 (Q18), -10 (Q18); PPT-A3-P-01 (Q19), P-02 (Q19), P-04 (Q9), P-05 (Q10), P-06 (Q3, Q4), P-07 (Q3, Q13), P-08 (Q11), P-09 (Q15), P-10 (Q16), P-11 (Q4), P-13 (Q3), P-14 (Q13, Q14), P-19 (Q1, Q2), P-20 (Q2, Q17); NTC-A3-01 to -04 (Q20), NTC-A3-05 (Q1). All covered. NEUTRAL-FACT findings (RES-A3-11, -12, -13; PPT-A3-P-03, P-12, P-15, P-16, P-17, P-18) go to the monitorables or data-integrity list, not to questions.

**Top 3 by likelihood of thesis-changing information:**
- Bull probability: **Q3** (does the 20-22% FY27 margin band stand). A firm yes with a Q3 print at or above 20% would confirm the cost hit as temporary and lift the earnings base.
- Bear confirmation: **Q1** (FY27 CFO/EBITDA commitment). No number after two silent quarters, with H1 CFO negative, would confirm structural cash.
- Transparency: **Q20** (cause of the cancellation and a new date). Vagueness here, after a same-day deck restatement, is itself governance information.

**Channel recommendation: IR email now.** No call is scheduled (NTC L39-40), so send all 20 questions in writing to Investor Relations, Mr. Ajesh Pillai, ajesh@tatvachintan.com (PPT L1099 R711). Ask for written answers before Q3 results. If the company reschedules the call, push Q1, Q3 and Q20 live and the rest in writing. AGM questions are the fallback (next AGM by 30-Sep-2027).

Draft email header (operator to send; not sent): "Subject: Tatva Chintan Q2 FY27, questions in lieu of the cancelled 19-Oct-2026 earnings call. We request written answers to the 20 numbered questions below before the Q3 FY27 results." Then Questions 1-20 verbatim from the table.

---

## COMMITMENT REGISTER AND MONITORABLES / CATALYSTS

Seeded by the A3 commitment registers (RES F6: 3 administrative rows; PPT F6: C1-C12; NTC F6: 3 rows) and the board outcome (RES F13: results the only item). Implied dates use Reg 33 limits where no company date exists: quarterly results within 45 days of quarter end (Q3 FY27 by 14-Feb-2027), annual results within 60 days (FY27 by 30-May-2027).

| # | Item | Implied date | Source ref |
|---|---|---|---|
| M1 | Rescheduled earnings call or written Q&A | none given (open) | NTC L39-40 (R017); NTC-A3-01, NTC-A3-04 |
| M2 | Solvent and freight costs "normalise withing the third quarter" | 31-Dec-2026; tested at Q3 results by 14-Feb-2027 | PPT L140-141 (R035); C1 |
| M3 | Q3 operating EBITDA margin: bull 20.0% or higher, bear below 18.0% (Q2 18.72%) | Q3 FY27 results by 14-Feb-2027 | PPT L142 (R037); C3; Step 8C |
| M4 | Revenue "similar momentum": Q3 revenue vs Q2 base Rs 217.32 Cr; Rs 800-850 Cr footprint ceiling [memory] | Q3 FY27 results by 14-Feb-2027 | PPT L141 (R036); C2 |
| M5 | Hybrid-battery first commercial supply (Oct-Nov CY2026 [memory]; undated in deck) | by 30-Nov-2026; evidence at Q3 results | PPT L168 (R045); C5 |
| M6 | ESS FY27 Rs 40-50 Cr: H2 needs Rs 26.8-36.8 Cr after H1 Rs 13.2 Cr | FY27 results by 30-May-2027 | PPT L674 (R542); PPT-A3-P-09 |
| M7 | Two further pharma molecules (deck names one product) | 31-Dec-2026 [memory] | PPT L174 (R047); C7 |
| M8 | Dahej-III equipment PO (GREEN test); "in line with the planned schedule" | 31-Dec-2026 [memory] | PPT L194 (R054); C10 |
| M9 | Dahej-III term loan sanction and draw (LT proceeds nil H1; ST +Rs 50.17 Cr) | not given; test at FY27 balance sheet by 30-May-2027 | RES L315, L317, L240; RES-A3-02; PPT-A3-P-05 |
| M10 | Standalone DTA (Rs 0.77 Cr) exhausted; cash tax steps up about Rs 3.5 Cr a quarter | Q3 FY27 (to 31-Dec-2026); visible in FY27 cash flow by 30-May-2027 | RES L500, L464; RES-A3-07 |
| M11 | FY27 consolidated CFO/operating EBITDA (bull above 70%, bear below 30%; H1 -5.0%) and receivable days (H1 84.9 d / TTM 100.2 d) | FY27 results by 30-May-2027 | RES L289, L215; trigger (a) |
| M12 | H2 FY27 subsidiary profit share (H1 31.0% of group PAT; H2 FY26 gap Rs 0.48 Cr) | FY27 results by 30-May-2027 | RES L164, L466; RES-A3-03 |
| M13 | Standalone operating EBITDA margin (H2 FY26 19.60%, Q1 16.38%, Q2 15.05%) | Q3 FY27 results by 14-Feb-2027 | RES L447-L459; RES-A3-04 |
| M14 | Nature of the Rs 1.32 Cr exceptional charge | FY27 annual report; AGM by 30-Sep-2027 | RES L158, L460; RES-A3-01 |
| M15 | Note 7 reclass amounts; FY26 CFO basis (filed Rs 31.49 Cr vs ~Rs 35 Cr [memory]); P&L line of the Rs 3.91 Cr unrealised FX gain | check against FY26 AR now; FY27 AR by 30-Sep-2027 | RES L371, L289, L268; RES-A3-10 |
| M16 | FY27 R&D below 2% of revenue for a second year (H1 1.19%) | FY27 annual report by 30-Sep-2027 | PPT L1108 (R724); PPT-A3-P-10 |
| M17 | Deck disclosure controls: "taken necessary steps to prevent their recurrence" | Q3 FY27 deck, by 14-Feb-2027 | PPT L48-49; C12; PPT-A3-P-01, P-15, P-17 |
| M18 | MD re-appointment term begins after 43.5% institutional vote against [memory] | 01-Feb-2027 | Notion 28-Sep-2026 key note |
| M19 | Shareholding: FPI 4.38% vs text-layer attribution of 19.58% | Dec-2026 quarter SHP, by 21-Jan-2027 (Reg 31) | PPT L1067-1072, L1110; PPT-A3-P-18 |
| M20 | Operator ruling 50 (receivable-days line) and ruling 51 (FV Rs 237 or Rs 287) | pending, no date | Notion brief s.4 [memory] |
| M21 | ROCE clears 8% by FY28 (tripwire b) | FY28 results by 30-May-2028 | Notion s.4 [memory] |
| M22 | Dahej-III commissioning Q3-Q4 FY28 | Oct-2027 to Mar-2028 [memory] | PPT L194-197; C10 |
| M23 | Semiconductor conversion (supply agreement, capex line or booked revenue) | not before Q4 CY2028 [memory] | PPT L185-191; C9 |
| M24 | Results and notice posted on company website (administrative) | 19-Oct-2026 (initiated) | RES L47, L368, L641; NTC L44-45 |
| M25 | Q3 FY27 SDA revenue vs Q2 (about Rs 97 Cr; share 45%) | Q3 FY27 results by 14-Feb-2027 | PPT L614, L623, L1106 |

---

## STEP 9: NOTION UPDATE PAYLOAD (NOT WRITTEN; operator-approval gate; Decision Status never written)

- Decision Status: no change written. Proposed: unchanged WATCHLIST / AVOID; conditional harden to AVOID if ruling 50 adopts the 90/100-day bands (Step 8).
- Promoter Verdict: proposed note "Q2 FY27: earnings call cancelled 56 min before start, no cause named, no new date; same-day deck restatement of two ratios (both flattering); exceptional item and cash questions unanswered for a second quarter."
- Key Notes (prepend): "20-Oct-2026: Q2 FY27 review. Revenue Rs 217.32 Cr (+75.9% YoY), op EBITDA 18.72%, PAT Rs 21.45 Cr (+116.3% YoY). H1 CFO Rs -3.68 Cr on revenue +59.9%; WC absorbed 99% of pre-WC profit; net debt/TTM EBITDA 1.22x; 97.4% of debt short-term. Subsidiaries 28.3% of Q2 PAT; parent op margin 15.05%. SDA step-up is one quarter old. Trigger (a): CFO legs met, 185-day leg not met (84.9-100.2 d); ruling 50 decides. Call cancelled, no new date. A4 verdict PROCEED WITH FLAGS. WATCHLIST/AVOID unchanged (operator-only)."
- Page content to append: Steps 0D, 1, 2, 3, 4, 5, 5.5, 6, 8, 8.5 in full from this review.
- FLAG for the page: reconcile the stale verdict-block entry zone (Rs 97-121) with the properties (Rs 118-147); add a Bear/Base/Bull P&L projection table so Step 6A can grade Q3.

---

## A4 VERDICT

**PROCEED WITH FLAGS.**

Reasons: (1) cash conversion is INDETERMINATE-WITH-DIRECTION (leaning structural), which caps the verdict at PROCEED WITH CAVEATS or below; (2) the flags go beyond evidence gaps: negative H1 CFO on +59.9% revenue, trigger (a) at the edge pending ruling 50, leverage at 1.22x vs a 0.65x band, profit moving to non-manufacturing subsidiaries while the factory margin falls, a cancelled call with no cause named, and a same-day restatement of two flattering ratios. The three bull claims (core profit real, operating leverage, SDA fired) each now carry a bear counter and a separating observation. No mechanical failure exists, so REWORK and INSUFFICIENT EVIDENCE do not apply. The filing is complete and foots (A2 section 0).

Flags (surfaced; decisions stay with the operator) are listed in the closing YAML.

---

## PLAIN-LANGUAGE BRIEF

Provenance tags: FILED (results filing or exchange notice), MGMT (company deck or call claims), AGENCY (rating agency), SECONDARY (third-party data quoted by the company), INFERENCE (A4 reading). [Q2] = from this quarter's documents. [Notion] = from prior Notion or AR work (memory). Metrics the filings did not disclose are named.

### 1. SUMMARY NARRATIVE

Tatva had its biggest quarter. Revenue was Rs 217.32 Cr, up 75.9% on last year [FILED, Q2]. Profit after tax was Rs 21.45 Cr, up 116.3% [FILED, Q2]. Core profit before other income grew 114.8% [FILED, Q2]. The filing does not say where a Rs 3.91 Cr half-year currency gain sits, so part of that growth could be non-cash [FILED, Q2; INFERENCE].

Cash did not follow. Over six months the business used Rs 3.68 Cr of operating cash while revenue rose 59.9% [FILED, Q2]. Working capital, mainly stock and customer dues, absorbed 99% of the operating profit before working capital [FILED, Q2]. Short-term bank debt paid for the gap. Net debt is now 1.22 times a year of operating profit [FILED, Q2; INFERENCE ratio]. The thesis checklist sets the comfort line at 0.65 times [Notion].

Margin slipped. The operating margin was 18.72%, below the 20-22% the company guided [FILED, Q2; Notion]. Management blames solvent prices (up 60-100%) and freight (up 100%) and says both should ease within Q3 [MGMT, Q2].

Profit is moving to the overseas trading arms. These units have no plant, staff or debt, but they earned 28.3% of group profit [FILED, Q2; INFERENCE]. The Indian factory company's margin fell in each of the last two quarters, to 15.05% [FILED, Q2].

Two disclosure events add weight. The company cancelled its results call 56 minutes before the start, with no cause named and no new date [FILED, Q2]. The same evening it re-filed its deck to change two ratios, and both changes made the numbers look better [FILED, Q2].

For the decision: the name is not held and stays WATCHLIST / AVOID. The cash test came out on the bear side. Whether that breaks the thesis depends on a pending operator ruling on which receivable-days line applies [Notion]. The price, Rs 1,841, is 12.5 times the top of the entry zone [Notion].

### 2. SECTOR INTELLIGENCE

- Demand: Euro 7 emission rules are pulling SDA demand for zeolite catalysts, the company says [MGMT, Q2]. Q2 numbers agree: SDA was about 45% of Q2 revenue [MGMT image, Q2]. But the step-up rests on one quarter; SDA was about 34% of Q1 revenue [INFERENCE from FILED deck values].
- Supply shock: specialty solvent shortages raised some solvent prices 60-100%, and US and Europe freight rose over 100% [MGMT, Q2]. The company calls both temporary. The filings give no index to check this, and no tracker rows were supplied.
- Structural tailwind claim: China holds 46% of the global chemical industry and India 3% [SECONDARY via deck, CEFIC/IBEF CY25]. The deck argues China's falling competitiveness lets India gain share [MGMT, Q2]. This is a sector narrative, not company evidence.
- Credit: CRISIL upgraded the company to A-/Stable on 08-Sep-2026 [AGENCY, Notion]. The deck repeats the rating [MGMT, Q2].
- Not disclosed: peer demand tone (Clean Science, Neogen), customer-industry volumes, and any solvent or freight index.

### 3. BUSINESS-MODEL INTELLIGENCE

- How it makes money: batch chemistry in four lines. In H1 FY27, SDA earned Rs 154.6 Cr, PASC (pharma, agro and speciality) Rs 124.7 Cr, PTC (catalysts) Rs 88.1 Cr and ESS (battery and capacitor salts) Rs 13.2 Cr [MGMT, Q2]. About 75% of FY26 revenue came from exports [MGMT, Notion].
- Unit economics: gross margin was 51.11% in Q2 vs 54.93% in Q1 [FILED, Q2; INFERENCE ratio]. At group level, staff and other costs each fell about 1.6 points of revenue in the quarter [FILED, Q2; INFERENCE ratio]. At the factory company the cost ratios also fell, but materials rose 8.1 points of revenue on last year, so its margin fell [FILED, Q2; INFERENCE ratio].
- Capital intensity: plant and lease assets of Rs 588.80 Cr support revenue running at Rs 869 Cr a year on Q2 [FILED, Q2; INFERENCE]. That is near the 1.5x asset turn management targets [Notion].
- Model drift this quarter, three points. First, profit is shifting to the US and EU trading subsidiaries while the factory company's margin falls [FILED, Q2]. Second, the cash cycle is about 300 days on cost of goods, so growth eats cash [INFERENCE]. Third, the company funds both capex and working capital with short-term debt; 97.4% of debt is short-term [FILED, Q2].
- Not disclosed: segment profit, customer concentration this quarter, intercompany sales, receivable ageing, pharma revenue, the P&L line of currency gains.

### 4. COMPETITION INTELLIGENCE

- Where it wins: the company claims #2 globally in SDA for zeolites and the only commercial SDA maker in India [MGMT, Q2]. It also claims #1 in India for PTCs and for electrolyte salts for supercapacitors, and #3 globally in glymes [MGMT, Q2]. New entrants need 1-6 years for customer approval [MGMT, Q2]. None of these claims carries third-party data in the documents.
- Where it is weaker: one customer took 36% of FY26 revenue and receivables, and the top three held 79% of receivables [Notion, FY26 AR]. SDA is now about 45% of revenue, so one product and possibly one buyer carry the growth [INFERENCE]. R&D spend is 1.19% of revenue [MGMT, Q2], low for a company that sells a five-product semiconductor pipeline.
- Named rivals: Sarchem in SDA on Euro 7 models [Notion]; Clean Science and Neogen as peer demand readers [Notion]. No peer numbers are in this quarter's documents.
- Competitive risk to watch: an SDA price or share loss at the main customer, or a second SDA supplier qualifying on Euro 7 programmes. Either would hit the line that supplied about 78% of the quarter's revenue gain [INFERENCE].

### 5. FORWARD MAP (next ~10-11 months)

**Make-or-break next reading:** Q3 FY27 consolidated operating EBITDA margin, results due by 14-Feb-2027. Bull: 20.0% or higher. Bear: below 18.0%. Q2 was 18.72%.

| Date | Catalyst | Bull fork | Bear fork |
|---|---|---|---|
| open, no date | Rescheduled call or written Q&A (M1) | Cause named and answers given to the 20 questions | No reschedule; a third quarter without cash Q&A |
| by 30-Nov-2026 | Hybrid-battery first supply (M5) | Supply confirmed; ESS path toward Rs 40-50 Cr reopens | No date; ESS guide cut |
| by 31-Dec-2026 | Solvent and freight normalise (M2) | Costs ease; gross margin recovers from 51.11% | Costs stay high; pass-through stays partial |
| by 31-Dec-2026 | Two more pharma molecules (M7) | Both commercial | One or both slip |
| by 31-Dec-2026 | Dahej-III equipment PO (M8) | PO placed on schedule | No milestone, or an extension disclosed |
| by 31-Dec-2026 | Standalone tax shield runs out (M10) | Cash tax absorbed by higher CFO | Cash tax adds about Rs 3.5 Cr a quarter to the cash drain |
| by 21-Jan-2027 | Dec-quarter shareholding filing (M19) | FPI at 4.38% confirmed or rising | Institutional holding falls after the cancelled call |
| 01-Feb-2027 | MD's new term begins after a 43.5% institutional vote against (M18) | Governance steps answer the dissent | Dissent repeats on other resolutions |
| by 14-Feb-2027 | Q3 FY27 results (M3, M4, M13, M17) | Margin 20.0% or higher; revenue at or above Rs 217.32 Cr; parent margin recovers; deck clean | Margin below 18.0%; revenue stalls at the Rs 800-850 Cr ceiling; parent margin falls again |
| by 14-Feb-2027 | Q3 SDA revenue (M25) | SDA holds at or above about Rs 97 Cr with new customers named | SDA falls back toward Rs 55-60 Cr; Q2 was a one-quarter spike |
| by 30-May-2027 | FY27 results with full-year cash flow (M6, M9, M11, M12) | CFO/EBITDA above 70%; receivable days at or below 90; term loan in place; subsidiary share holds | CFO/EBITDA below 30%; days above 100; debt still short-term; year-end subsidiary true-up |
| by 30-Sep-2027 | FY27 annual report and AGM (M14, M15, M16) | Exceptional item explained; FX gain shown in other income; R&D at or above 2%; customer concentration falls | Exceptional still unexplained; FX gain inside operating costs; R&D below 2% a second year; concentration rises |
| pending | Operator rulings 50 and 51 (M20) | 185-day line kept; FV basis settled | 90/100-day bands adopted; trigger (a) read as met on the CFO leg |

---

```yaml
stage: A4-analyst
company: "TATVA"
quarter: "Q2 FY27"
model: "claude-opus-5-5"
status: complete
docs_merged: [results, presentation, notice]
ledger_reconciliation:
  notes: 13
  turns: 0
  slides: 42
  all_reviewed: true
  a3_findings_incorporated: [RES-A3-01, RES-A3-02, RES-A3-03, RES-A3-04, RES-A3-05, RES-A3-06, RES-A3-07, RES-A3-08, RES-A3-09, RES-A3-10, RES-A3-11, RES-A3-12, RES-A3-13, PPT-A3-P-01, PPT-A3-P-02, PPT-A3-P-03, PPT-A3-P-04, PPT-A3-P-05, PPT-A3-P-06, PPT-A3-P-07, PPT-A3-P-08, PPT-A3-P-09, PPT-A3-P-10, PPT-A3-P-11, PPT-A3-P-12, PPT-A3-P-13, PPT-A3-P-14, PPT-A3-P-15, PPT-A3-P-16, PPT-A3-P-17, PPT-A3-P-18, PPT-A3-P-19, PPT-A3-P-20, NTC-A3-01, NTC-A3-02, NTC-A3-03, NTC-A3-04, NTC-A3-05]
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE-WITH-DIRECTION"
decision_status_verified: "WATCHLIST / AVOID (not held)"
position_branch: "8A-W"
sc_gap_pat_pct:
  - "Q2 FY26: 10.9% of std PAT (cons 9.92 vs std 8.94 Rs Cr)"
  - "Q1 FY27: 53.0% (15.98 vs 10.45)"
  - "Q2 FY27: 39.4% (21.45 vs 15.39); +28.5pp YoY, -13.6pp QoQ"
  - "H1 FY26: 17.7% (16.57 vs 14.07)"
  - "H1 FY27: 44.9% (37.43 vs 25.83)"
  - "FY26: 7.6% (42.05 vs 39.08); H2 FY26 derived 1.9%"
questions_for_management:
  - {q: "Commit to FY27 consolidated CFO/EBITDA in per cent (H1 CFO Rs -3.68 Cr vs op EBITDA Rs 72.99 Cr; WC absorbed 99% of pre-WC profit)", from_finding_id: "PPT-A3-P-19, NTC-A3-05"}
  - {q: "Customer 1 receivable at 30-Sep and amount overdue beyond terms (receivables +Rs 59.35 Cr to Rs 178.38 Cr)", from_finding_id: "PPT-A3-P-19, PPT-A3-P-20"}
  - {q: "Does the 20-22% FY27 EBITDA band stand, yes or no (Q2 18.72%; H2 needs 20.9-24.7%)", from_finding_id: "PPT-A3-P-07, PPT-A3-P-13, PPT-A3-P-06"}
  - {q: "Per cent of the 60-100% solvent increase recovered in Q2 prices, and repricing lag in days", from_finding_id: "PPT-A3-P-11, PPT-A3-P-06"}
  - {q: "Transfer-pricing method for US/EU subsidiaries (no plant, staff or debt; 28.3% of Q2 PAT) and intercompany debtor days at 30-Sep", from_finding_id: "RES-A3-06, RES-A3-03"}
  - {q: "Driver of standalone op EBITDA margin decline (H2 FY26 19.60% -> Q1 16.38% -> Q2 15.05%) while group held 18.72%", from_finding_id: "RES-A3-04"}
  - {q: "Risk of year-end true-up reducing H1 subsidiary profit Rs 11.60 Cr (H2 FY26 gap Rs 0.48 Cr)", from_finding_id: "RES-A3-03"}
  - {q: "Nature of std-over-cons other income Rs 2.20 Cr H1, and P&L line (other income or other expenses) of the Rs 3.91 Cr unrealised FX gain", from_finding_id: "RES-A3-05"}
  - {q: "Nature, cash/non-cash, tax treatment and recurrence of the Rs 1.32 Cr Q1 exceptional charge", from_finding_id: "RES-A3-01, PPT-A3-P-04"}
  - {q: "Dahej-III term-loan sanction, draw schedule and peak net debt/EBITDA (ST debt +Rs 50.17 Cr, LT proceeds nil)", from_finding_id: "RES-A3-02, PPT-A3-P-05"}
  - {q: "Dahej-III share of the H1 CWIP rise of Rs 19.48 Cr (project split ND), equipment PO status, spend vs Rs 200 Cr, commissioning month", from_finding_id: "PPT-A3-P-08"}
  - {q: "Quarter from which current tax rises to the full P&L charge (std DTA Rs 0.77 Cr)", from_finding_id: "RES-A3-07"}
  - {q: "Price vs volume split of Q2 growth and how momentum holds at Rs 869 Cr annualised vs Rs 800-850 Cr ceiling", from_finding_id: "PPT-A3-P-07, PPT-A3-P-14"}
  - {q: "SDA ~45% of Q2 vs ~34% of Q1: is Customer 1 an SDA buyer, how many new SDA customers invoiced, volume and tenor of Euro 7 contracts", from_finding_id: "PPT-A3-P-14"}
  - {q: "Does ESS Rs 40-50 Cr FY27 guide stand (H1 Rs 13.2 Cr); hybrid-battery first supply date", from_finding_id: "PPT-A3-P-09"}
  - {q: "FY27 R&D budget in rupees (H1 1.19% of revenue vs 'accelerate' claim)", from_finding_id: "PPT-A3-P-10"}
  - {q: "Status of pharma molecules two and three due by Q3 end (deck names one product)", from_finding_id: "PPT-A3-P-20"}
  - {q: "Correct classification of the Rs 3.82 Cr dividend difference; Note 7 reclass lines and amounts", from_finding_id: "RES-A3-09, RES-A3-10"}
  - {q: "RoE and Debt/EBITDA formula per p14 column; why FY26/H1 basis differs; which control failed", from_finding_id: "PPT-A3-P-01, PPT-A3-P-02"}
  - {q: "Cause of call cancellation; decided in or after the 11:30-15:45 board; reschedule date or written Q&A", from_finding_id: "NTC-A3-01, NTC-A3-02, NTC-A3-03, NTC-A3-04, RES-A3-08"}
monitorables:
  - {item: "Rescheduled call or written Q&A", implied_date: "none given", source_ref: "NTC L39-40; NTC-A3-01"}
  - {item: "Solvent/freight normalisation within Q3", implied_date: "2026-12-31", source_ref: "PPT L140-141 (R035)"}
  - {item: "Q3 op EBITDA margin: bull >=20.0%, bear <18.0% (Q2 18.72%)", implied_date: "2027-02-14", source_ref: "PPT L142 (R037); Step 8C"}
  - {item: "Q3 revenue vs Q2 base Rs 217.32 Cr and Rs 800-850 Cr ceiling", implied_date: "2027-02-14", source_ref: "PPT L141 (R036); RES L145"}
  - {item: "Hybrid-battery first commercial supply", implied_date: "2026-11-30", source_ref: "PPT L168 (R045); memory Oct-Nov CY2026"}
  - {item: "ESS FY27 Rs 40-50 Cr (H1 Rs 13.2 Cr)", implied_date: "2027-05-30", source_ref: "PPT L674 (R542)"}
  - {item: "Two further pharma molecules", implied_date: "2026-12-31", source_ref: "PPT L174 (R047); memory"}
  - {item: "Dahej-III equipment PO", implied_date: "2026-12-31", source_ref: "PPT L194 (R054); memory"}
  - {item: "Dahej-III term-loan sanction and draw", implied_date: "2027-05-30", source_ref: "RES L315, L317; RES-A3-02"}
  - {item: "Std DTA exhaustion; cash tax step-up ~Rs 3.5 Cr/qtr", implied_date: "2026-12-31", source_ref: "RES L500, L464; RES-A3-07"}
  - {item: "FY27 CFO/op EBITDA (bull >70%, bear <30%) and receivable days", implied_date: "2027-05-30", source_ref: "RES L289, L215"}
  - {item: "H2 FY27 subsidiary profit share / year-end true-up", implied_date: "2027-05-30", source_ref: "RES L164, L466; RES-A3-03"}
  - {item: "Standalone op EBITDA margin trend (H2 FY26 19.60%, Q1 16.38%, Q2 15.05%)", implied_date: "2027-02-14", source_ref: "RES L447-L459; RES-A3-04"}
  - {item: "Nature of Rs 1.32 Cr exceptional", implied_date: "2027-09-30", source_ref: "RES L158, L460; RES-A3-01"}
  - {item: "Note 7 reclass amounts; FY26 CFO basis; P&L line of Rs 3.91 Cr unrealised FX gain", implied_date: "2027-09-30", source_ref: "RES L371, L268; RES-A3-10"}
  - {item: "FY27 R&D <2% second year (H1 1.19%)", implied_date: "2027-09-30", source_ref: "PPT L1108 (R724)"}
  - {item: "Deck disclosure controls in Q3 deck", implied_date: "2027-02-14", source_ref: "PPT L48-49; PPT-A3-P-01"}
  - {item: "MD new term starts after 43.5% institutional dissent", implied_date: "2027-02-01", source_ref: "Notion 28-Sep-2026 note (memory)"}
  - {item: "FPI holding check vs NSE SHP", implied_date: "2027-01-21", source_ref: "PPT L1110; PPT-A3-P-18"}
  - {item: "Operator rulings 50 and 51", implied_date: "pending", source_ref: "Notion brief s.4 (memory)"}
  - {item: "ROCE clears 8% by FY28", implied_date: "2028-05-30", source_ref: "Notion s.4 (memory)"}
  - {item: "Dahej-III commissioning Q3-Q4 FY28", implied_date: "2027-10-01 to 2028-03-31", source_ref: "PPT L194-197; memory"}
  - {item: "Semiconductor conversion condition", implied_date: "not before Q4 CY2028", source_ref: "PPT L185-191; memory"}
  - {item: "Website posting of results and notice (administrative)", implied_date: "2026-10-19", source_ref: "RES L47, L368, L641; NTC L44-45"}
  - {item: "M25 Q3 FY27 SDA revenue vs Q2 (about Rs 97 Cr; share 45%); bull holds with new customers named, bear falls toward Rs 55-60 Cr", implied_date: "2027-02-14", source_ref: "PPT L614, L623, L1106"}
flags:
  - "TRIGGER (a) AT EDGE: H1 CFO Rs -3.68 Cr on revenue +59.9%; receivable days 84.9 d (H1) / 100.2 d (TTM) vs 185 line; NOT FIRED as written; bear separating metric met on CFO leg; operator ruling 50 decides, not resolved by A4"
  - "CASH: WC absorbed 99% of pre-WC profit; FCF Rs -34.52 Cr funded by ST debt +Rs 50.13 Cr; INDETERMINATE-WITH-DIRECTION (structural lean); missing: receivable ageing, Customer 1 balance, intercompany days, Sep-25 balance sheet, Note 7 amounts"
  - "PILLAR 2: H1 CFO/PAT -0.10x vs 0.80x multiplier on file; points to 0.65x (deferred to /fttcp and Role 1, OR-30)"
  - "PILLAR 1: H1 annualised ROCE 11.6% (10.6% operating) vs 6.6% current leg on file; TTM 9.5% below the Q1 8D 12% reassess line (deferred)"
  - "LEVERAGE: net debt/TTM op EBITDA 1.22x vs 0.65x band; 97.4% of debt short-term; no term debt drawn for the capex"
  - "PROFIT LOCATION: subsidiaries with no plant, staff or debt earn 28.3% of Q2 group PAT; parent op margin H2 FY26 19.60% -> Q1 16.38% -> Q2 15.05%; parent materials +810 bps YoY vs staff/other -493 bps; std other income exceeds cons by Rs 2.20 Cr H1"
  - "CORE PROFIT QUALIFIER: P&L line of Rs 3.91 Cr H1 unrealised FX gain ND; if inside other expenses it is up to 8.3% of H1 core PBT and 16.5% of the H1 core-PBT increase; 95% core share is an upper bound"
  - "SDA: step-up sits in one quarter (Q1 ~34%, Q2 ~45% of revenue); Euro 7 link MGMT only; new-customer leg ND; trigger FIRED on revenue, durability unproven (M25)"
  - "MARGIN: op EBITDA 18.72% Q2, second quarter below the 20-22% guide; above the 18% red line"
  - "DISCLOSURE: call cancelled 16:03 IST, 15 min after results signed, no cause named, no new date; cash Q&A silent two quarters, now CONFIRMATORY-NEGATIVE"
  - "DISCLOSURE: same-day deck restatement RoE 2.6% -> 6.3% and Debt/EBITDA 4.30 -> 1.16, both flattering; corrected RoE fails the FY23-FY25 basis"
  - "DISCLOSURE: Rs 1.32 Cr exceptional item unexplained for a second filing"
  - "CF CLASSIFICATION: Rs 3.82 Cr dividend difference (financing cons vs operating std); cons CFO Rs -3.68 to -7.50 Cr by treatment; Note 7 reclass unquantified"
  - "TAX: std DTA Rs 0.77 Cr left; cash tax steps up from Q3 FY27"
  - "CAPACITY: Q2 annualised revenue Rs 869 Cr at or above the Rs 800-850 Cr existing-footprint ceiling (memory)"
  - "GUIDANCE: ESS behind (H1 Rs 13.2 Cr vs Rs 40-50 Cr FY27); R&D 1.19% of revenue"
  - "NOTION: no Bear/Base/Bull P&L table, so Step 6A not gradeable; verdict-block entry Rs 97-121 stale vs properties Rs 118-147; ruling 51 pending"
  - "TRACKER: rows not supplied; fewer than three signals; OR-17 gate will need them before /fttcp"
  - "DATA: RES-A3-13 std EPS cells re-verify; PPT PN-1 to PN-4 anchor issues; NTC anchor offsets R015/R023/R026; PPT-A3-P-01 call-timing inference void (call cancelled before deck filed); CWIP project split ND"
plain_language_brief_included: true
analyst_note: "Group profit grew (core PBT +114.8% YoY) but cash went the other way: H1 CFO -3.68 Cr on revenue +59.9%, funded by short-term debt. Cash is INDETERMINATE-WITH-DIRECTION, not structural, because receivable and inventory days are flat on the H1 basis; the structural lean rests on FY26 CFO/EBITDA of 33.8% and a ~300-day cycle. Trigger (a) is not fired on the 185-day text; the bear separating metric is met on the CFO leg, so ruling 50 decides. PROCEED WITH FLAGS, not CAVEATS, because the flags are substantive. Loop 1 grafted three bear counters beside the bull claims: the FX gain's P&L line is ND (core share is an upper bound); the parent's materials rose 810 bps against 493 bps of cost leverage, so the group offset depends on staffless subsidiaries; SDA's step-up is one quarter old (M25). CWIP is now an H1 change with no project split. Notion has no Bear/Base/Bull table, so 6A cannot grade. Q2 segment values are H1 FILED minus Q1 memory."
review_path: "runs/tatva-q2fy27/work/review_tatva_q2fy27.md (single merged file; supersedes parts/review_tatva_q2fy27.part2.md)"
```

---

## LOOP 1 CHANGE LOG (A5 audit runs/tatva-q2fy27/work/audit_tatva_q2fy27.md)

| A5 ID | Type | Change made | Where |
|---|---|---|---|
| F1 | FACTUAL | CWIP +Rs 19.48 Cr restated as the 31-Mar to 30-Sep change with project split ND; removed "Dahej-III build" and "since the 20-Jul groundbreaking"; capex verdict "project split ND"; Step 2 diagnostic 5 and Step 4 D&A bullet no longer attribute CWIP to Dahej-III | Step 5 table (CWIP, capex rows), Step 5 CWIP answer, Step 2 diag 5, Step 4, 6B #5, guidance #7, 6D Dahej row, Q11, YAML q11 |
| C1 | CONTRADICTION | Guidance tally restated: 1 delivered, 1 ahead, 2 behind, 1 far, 1 near, 3 consistent or on track, 1 window open, 1 not updated, 1 unverifiable, 5 not testable (17) | Step 6B guidance log score line |
| M1 | MISSING | FX-location bear counter grafted with bull reading, bear reading and separating observation; 95% core share labelled an upper bound; Step 2 core-PBT verdict qualified; brief narrative sentence added; Q8 asks the FX line; M15 extended | Step 2 diag 3 and 6, Step 4, brief part 1, Q8, M15, YAML flags |
| M2 | MISSING | Parent-level counter grafted: materials +810 bps vs staff -411 and other -82 bps, parent margin -317 bps; two readings and separating observation (M12, Q5, Q7); brief business-model line added | Step 2 diag 2, brief part 3, YAML flags |
| M3 | MISSING | SDA one-quarter counter grafted from filed shares (Q1 ~34%, Q2 ~45%); trigger status "FIRED on revenue (one quarter, MGMT attribution); durability unproven"; 6B #3 "GREEN on revenue; new-customer leg ND; one quarter"; monitorable M25 and forward-map row added; Q14 sharpened; sector line qualified | 6D, 6B #3, monitorables M25, forward map, Q14, brief part 2, YAML monitorables and flags |
| S1 | STYLE | "no reason" changed to "no cause named" | Brief part 1, Step 9 payload |
| S2 | STYLE | "Working capital, mainly stock and customer dues, absorbed 99%" | Brief part 1 |
| S3 | STYLE | Call-script reading tagged [INFERENCE] | Step 0E timeline reading, Role 5 slot |
| S4 | STYLE | A2 LABEL_ANOMALY (R1005, R1040) disposed: reviewed, no finding | Data-integrity list |
| S5 | STYLE | Self-description and YAML review_path now state one merged file | Header, YAML |
| S6 | STYLE | FY26 Rs 4.00 Cr non-current investment added as an ND line (investee, stake, earnings ND; 0.49% of equity) | Step 5 consolidated table |
| S7 | STYLE | A2-side note (presentation count test grep basis); no A4 change | n/a |

No Step 1 to Step 5 table number changed. Verdict unchanged: PROCEED WITH FLAGS.
