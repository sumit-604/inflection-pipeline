# A5 ADVERSARY / COMPLETENESS AUDIT: NETWEB Q2 FY27
Netweb Technologies India Ltd (NETWEB). Quarter and half year ended 30-Sep-2026.
Agent A5 | model claude-opus-5-5 | run date 28-Oct-2026.
Review under audit: `runs/netweb-q2fy27/work/review_netweb_q2fy27.md` (941 lines; cited below as `A4 Lnnn`).

Input discipline: I read only the five A1 fulltexts, the five A1 structured files, the five A2 ledgers and the A4 review. I did not open the source PDFs, the run's `inputs/` folder, or any A3 notes. Line cites: `RES/PRS/STR/PR/CC Lnnn` = A1 fulltext line; `Rnnn` = A1 structured row. Unit conversions: RES, PRS, PR in INR Mn (x0.1 = Rs Cr); STR charts INR Bn (x100 = Rs Cr); CC in Rs Cr. `[calc]` = my arithmetic.

---
## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)
| Brief part | Heading in A4 | Content check | Status |
|---|---|---|---|
| (1) Summary narrative | A4 L775 "1. SUMMARY NARRATIVE" | 15 lines (A4 L776-L790), inside the 10-20 line band; provenance-tagged | PRESENT |
| (2) Sector intelligence | A4 L792 "2. SECTOR INTELLIGENCE" | 11 lines (A4 L793-L803); real content | PRESENT (content gap logged as M6, not a gate failure) |
| (3) Business-model intelligence | A4 L805 "3. BUSINESS-MODEL INTELLIGENCE" | 11 lines (A4 L806-L816) | PRESENT |
| (4) Competition intelligence | A4 L818 "4. COMPETITION INTELLIGENCE" | 10 lines (A4 L819-L828) | PRESENT |
| (5) Forward map | A4 L830 "5. FORWARD MAP" | 1 make-or-break reading plus 11 catalysts (A4 L831-L846); every item has a bull fork and a bear fork; 10 dated, 1 labelled undated (Taiwan WOS) | PRESENT |

Gate result: PASS. All five parts exist and carry real content.

---
## 1. COVERAGE AUDIT
### 1A. Fresh enumeration vs A2 ledgers
| Doc | Category | A2 count | My fresh count (grep or sweep of fulltext and structured file) | Orphan rows | Status |
|---|---|---|---|---|---|
| RES | Numbered notes | 5 | 5 (RES L304, L308, L309, L316, L318) | none | PASS |
| RES | Unnumbered footnote (*) | 1 | 1 (RES L191) | none | PASS |
| RES | Line items | 107 | 107 (P&L 26 at L160-L190; BS 37 at L199-L245; CF 44 at L252-L299) | none | PASS |
| RES | Zero-standing cells | 18 | 18 (exceptional 6, earlier-period tax 5, investments 2, five CF single cells) | none | PASS |
| RES | Agenda items | 2 | 2 (RES L49, L54) | none | PASS |
| RES | Annexure II rows | 8 | 8 (RES L346-L376) | none; MISSING-1 resolved as R429 (RES L356) | PASS |
| RES | Auditor paragraphs | 5 | 5 (paras 1-4 RES L96-L124; sign-off L126-L146) | none | PASS |
| RES | Structured IDs | 429 | 429 (grep `^R\d{3} \|`) | none | PASS |
| PRS | Slides | 22 | 22 (`[page 1]`-`[page 22]`) | none | PASS |
| PRS | NUMBER rows | 297 | 297 (grep) | none | PASS |
| PRS | Structured IDs | 423 | 423 (grep) | none | PASS |
| STR | Slides | 28 | 28 (`[page 1]`-`[page 28]`) | none | PASS |
| STR | NUMBER rows | 181 | 181 (grep) | none | PASS |
| STR | Structured IDs | 336 | 336 (grep) | none by count; see M6 for uncited content | PASS |
| PR | Pages | 3 | 3 | none | PASS |
| PR | Table line items | 7 | 7 (PR L92-L104) | none | PASS |
| PR | Structured IDs | 170 + ledger-only M001-M004 | 170 (grep); M001-M004 not in structured file (see S6) | none | PASS |
| CC | Turns (ledger convention: host, prepared remarks, analyst boundaries) | 20 | 20 (grep `\| TURN`; CC L31 to L779) | none | PASS |
| CC | Analyst questioner turns | 15 | 15 (CC L211-L740; 14 answered, R133 no reply) | none | PASS |
| CC | Forward rows | 44 | 44 (R160-R203) | none | PASS |
| CC | Structured IDs | 261 | 261 (grep) | none | PASS |

Fresh-pass units the ledgers lack: none material.
- PRS L240 and STR L217 say "under OEM partnership with Nvidia & AMD". Both entities are enumerated (PRS R302; STR R186-R187), and the PRS slide sits inside entity-summary row R312. I treat the OEM wording as a qualifier on enumerated entities. No loop. The wrong A4 anchor for this quote is S1.
- CC L44-L51 (IR advisor safe-harbour handover) has no TURN row of its own. Under the ledger's documented convention (CC ledger L3) it sits inside T1. A4 reviews it (A4 L406). No loop.

### 1B. Ledger-row citation test (every ledger row cited in A4 or marked reviewed)
Standard applied: A4's preamble (A4 L18-L22) states "No ledger row is unreviewed" and "A3 reconciled 100% on all five documents". I accept this as the explicit "reviewed" mark for uncited rows. I then tested the uncited rows for material content.
- Cited by ID or line in A4: all 5 notes (R420-R425), the footnote (R402-R404), both agenda items (R412, R368), all 8 Annexure II rows (R368-R376, R429), the auditor paragraphs (R416-R418), all 20 turns (T1-T4 and T20 in A4 Section B 0B, 0C and Step 1; T5-T19 in A4 4A), all 15 questioner turns, and rows on every PRS, STR and PR slide that carries data.
- Uncited rows with no material content: identifiers, PIN codes, circular numbers, disclaimer rows, board biographies (STR p19-p20), minor BS and CF lines (ROU, intangibles, tax paid, investing CF). The blanket mark covers them.
- Uncited rows WITH material content (the blanket mark fails for these):
  - RES R238 (RES L259): unrealised foreign-exchange gain Rs 5.64 Cr in H1 FY27 PBT. See M4.
  - STR R065-R095 and R236-R248 (STR L297-L356): filed sector sizing and policy data. See M6.
Both are content gaps in A4's synthesis. A4 can graft them from the extracts. They route to A4, not A3.

Coverage result: counts PASS on all five documents. orphan_rows = [] under the stated standard. missing_from_ledger = []. Two uncited material clusters are raised as MISSING findings (M4, M6).

---
## 2. ARITHMETIC AUDIT
All values recomputed from RES rows in INR Mn, then shown in Rs Cr. Tolerance: rounding at the last shown digit.

| Metric | A4 value (A4 line) | Recomputed | Source line | Status |
|---|---|---|---|---|
| Step 1 table, all 6 columns x 16 lines | A4 L99-L115 | every cell matches (e.g. Rev Q2 13,232.79 Mn = 1,323.28; PAT H1 2,219.79 = 221.98) | RES L160-L190 | PASS |
| Op EBITDA Q2 FY27 / Q1 / Q2 FY26 | 197.30 / 120.52 / 45.46 (L121) | 1,826.49+37.12+238.00-128.62 = 1,972.99; 1,205.15; 454.64 Mn | RES L161, L167, L168, L173 | PASS |
| Op EBITDA H1 FY27 / H1 FY26 / FY26 | 323.04 / 90.32 / 284.84 | 3,230.35; 903.18; 2,848.42 Mn | same | PASS |
| Op EBITDA margin (6 columns) | 14.97 / 14.70 / 14.91 / 14.93 / 15.07 / 13.04 (L122) | 14.97 / 14.70 / 14.91 / 14.93 / 15.07 / 13.04 | same + L160 | PASS |
| Reported EBITDA, core PBT, OI/PBT, ETR, PAT margin (6 columns each) | A4 L123-L127 | all match (e.g. ETR Q2 459.93/1,826.49 = 25.18%) | RES L161-L179 | PASS |
| Gross margin Q2 FY26 / Q2 FY27; opex/revenue | 27.46 / 20.05; 12.49 / 5.14 (L128-L129) | 27.455 / 20.051 (740 bps unrounded; 741 on rounded); 12.487 / 5.141 | RES L160, L164-L166, L169 | PASS (rounding) |
| H1 non-additivity | 5.22; additive H1 margin 14.83% (L130) | OI 213.34 vs 161.13 Mn; other exp 635.25 vs 583.04; gap 52.21 Mn on both; 3,178.14/21,429.65 = 14.83% | RES L161, L162, L169, L170 | PASS |
| **Regroup margin bound per quarter** | "up to ±0.39%" (L79); "uncertain by up to 39 bps" (L168); Q1 to Q2 "+21 bps" stated without caveat (L149) | Q2: 52.21/13,232.79 = 39 bps. **Q1: 52.21/8,196.86 = 64 bps.** If the item sits in Q1, Q1 restates to 15.34% and Q1 to Q2 is **-43 bps**; if in Q2, Q2 restates to 15.30% and Q1 to Q2 is +60 bps | RES L160, L161, L169 | **FAIL (F1)** |
| YoY: revenue, Op EBITDA, EBIT, core PBT, PBT, PAT, EPS | +335.7 / +334.0 / +360.6 / +313.1 / +334.6 / +334.8 / +324.1% (L135-L145) | identical | RES L160-L190 | PASS |
| Finance cost multiples | 25.6x; 95.20 annualised = 7.4x FY26 (L152) | 238.00/9.30 = 25.6x; 95.20/12.95 = 7.35x | RES L167 | PASS |
| PAT bridge components | +152.62 / -0.78 / -0.28 / -22.87 / +11.94 / -35.45 / +0.05 = +105.22 (L175-L183) | prior margin 14.969%; components identical; sum 105.23 vs 105.22 (rounding) | RES L160-L179 | PASS |
| **Recurring share of ΔPAT** | "About 89%" (L187) | (152.62-0.78-0.28-22.87) x (1-0.2521) = 96.25; 96.25/105.22 = **91.5%**. It is the complement of the 8.5% OI share; A4's 89% + 8.5% = 97.5% does not close | RES L160-L179 | **FAIL (F2)** |
| OI after tax; PAT if OI reverted | 8.93; 127.73 (L187-L188) | 11.94 x 0.748 = 8.93; 136.66-8.93 = 127.73 | RES L161, L179 | PASS |
| Deferred tax shield Q1 | ~315 bps (L190) | 35.94/1,141.38 = 3.15% | RES L177 | PASS |
| CFO, CFO/PAT, FCF | (639.15), -2.88x, (646.53); H1 FY26 101.19, 1.63x, 97.22 (L195-L199) | identical | RES L278, L280, L179 | PASS |
| WC change H1 FY27 / H1 FY26 | (910.11) / +29.58 (L200) | sum of RES L268-L275 = (9,101.14) / +295.79 Mn; ties to CGO 3,249.29-9,101.14 = (5,851.85) | RES L266-L276 | PASS |
| Receivable tie (my added check) | n/a | BS change +1,144.18 Mn + credit charges 53.31 Mn = 1,197.49 Mn = CF receivables line | RES L213, L261, L262, L268 | PASS |
| Period-end days and CCC | 112.0/67.0; 134.5/164.9; 127.2/104.1; CCC 119.4/127.7 (L202-L208) | identical | RES L160, L211, L213, L237-L238 | PASS |
| Company days reproduce | 62 / 117 / 85 (deck) | avg balances / H1 revenue x 183 = 62.1 / 116.8 / 84.5. The deck footnotes say quarter revenue (PRS L553-L559); H1 revenue is what reproduces. Supports A4 Q21 | PRS L500-L503, L552-L559 | PASS |
| BS changes | Inv +139.9%; TR +17.1%; TP +60.3%; OCL -37.6%; debt +18.3%; equity +1,380.84 (L211-L221) | identical | RES L211-L240 | PASS |
| Net debt, filed gross basis | (307.13) / (791.64) (L219) | 2,822.23-5,893.50 = (3,071.27); 3,328.02-11,244.39 = (7,916.37) Mn | RES L214, L215, L227, L228, L234, L235 | PASS |
| Cash location residual | 351.55 (L224) | 1,124.44-346.4-426.49 = 351.55 | RES L214-L215, L314-L315; PRS L822 | PASS |
| QIP bridge | utilised 774.42; unutilised 425.58; WC+GCP 403.26; parked 426.49; gap 0.91 (L226) | 7,744.24 / 4,255.76 Mn; 2,037.56+1,995.02 = 4,032.58 Mn; 3,500+587.88+177.00 = 4,264.88 Mn | PRS L514-L522; RES L314-L315 | PASS |
| Monitoring residual = dividend; issue expense gap | 93.57-76.49 = 17.08; 24.42 vs 7.68 (L352) | identical | RES L292, L293, L295; PRS L520 | PASS |
| Share count and dilution | 59.445 Mn; +4.40% (L60-L61) | 118.89/2; 2.505/56.94 = 4.40% | RES L186, L312 | PASS |
| Deck ROCE, ROE; ROE on closing equity | 38.6%, 31.4%; 21.1% (L264, L313) | 6,642.22/17,212.32 = 38.59%; 4,439.58/14,137.20 = 31.40%; 4,439.58/21,041.41 = 21.10% | RES L173, L167, L179, L223, L227-L235 | PASS |
| EPS vs Notion bands | 96.5% of Bear; 59.4% of Bull; Bull/2 = 32.5 (L262) | 38.60/40; 38.60/65 | RES L190 | PASS (framing challenged in Read 2) |
| H2 implied by Rs 4,000 Cr target | 1,857.03; 928.52/qtr; -29.8% vs Q2 (L148, L170) | 4,000-2,142.97; /2; 928.515/1,323.28-1 = -29.8% | CC L458; RES L160 | PASS |
| Thesis-broken #1 hurdle | 110.99; miss 750.14 (L287) | 0.5 x 221.98; 110.99+639.15 | RES L179, L278 | PASS |
| Credit charges | 5.33 vs 0.36, 14.9x (L351, L932) | 53.31 / 3.57 Mn | RES L261-L262 | PASS |
| AI mix | Q1 AI 62.3%; non-AI +77.9% QoQ; residual 57.2 (L361) | 5,105/8,196.86; 5,501.79/3,091.86; 5,501.79-2,482-2,448 | PRS L140-L141, L678; RES L160 | PASS |
| Software share | 2.65% H1; 5.6% FY26 (L275) | 568/21,430; 1,232/21,836 | PRS L641-L645, L803 | PASS |
| Book + L1 | 3,281.5 vs 3,354.9 (-73.4); L1 -195.5 (L315, L356) | identical (Q1 values are Notion memory) | PRS L425, L422 | PASS |
| Q&A grades | A 4, B 10, C 9, D 2, E 5; C+D+E 16/30 = 53% (L560) | recount of A4 4A table identical | A4 L528-L559 | PASS |
| Credibility ratio | 7.0/10 = 70.0%; 66.7% to 75.0% (L492, L498) | identical | A4 L476-L489 | PASS |
| Claims and specificity ratios | 17/29 = 58.6%; 17/44 = 0.39 (L444, L643) | identical | CC R160-R203 | PASS (classification note S5) |
| Q&A duration share | 43.8 min, 76% (L402) | 57:28-13:40 = 43.8 min; /57.57 = 76% | CC L205, L780 | PASS |
| Employee cost YoY | +70.4% (L669) | 327.50/192.17 | RES L166 | PASS |
| Reg 33 dates | 14-Feb-2027; 30-May-2027; 14-Aug-2027 (L759-L769) | 45 / 60 / 45 days from period end | n/a | PASS |
| Promoter no-sale test | "drop from 66.98% is QIP dilution [calc]" (L291) | 66.98 x 56.94/59.445 = 64.16 closes, but 66.98% appears in no extract; see M5 | PRS L764 only | Arithmetic PASS; evidence gap M5 |

Arithmetic result: 2 FAIL (F1, F2) out of about 120 recomputed values. Everything else ties.

---
## 3. ADVERSARIAL READ
### Read 1. Claim: "Earnings are real ... margin held because opex leverage (735 bps) offset a 741 bps gross-margin fall" (A4 L938; also L149, L742, brief L778 "The operating margin held at 14.91%").
Strongest bear counter, from the same extract: the margin "held" only on a definition that excludes the finance cost of the stock that produced the sales. A4 itself tags that cost "RED: WC funding cost" (A4 L139).
- (Op EBITDA - finance cost)/revenue: Q2 FY26 445.34/3,037.24 = 14.66%; Q2 FY27 1,734.99/13,232.79 = 13.11%. Change **-155 bps** [calc; RES L160, L161, L167, L168, L173].
- Core PBT margin (PBT - OI)/revenue: 13.53% to 12.83%, **-70 bps** [calc].
- Finance cost/revenue: 0.31% to 1.80%, +149 bps [calc; RES L167, L160].
- Management also hedged the H1 margin: "not to be quoted for the entire year" (CC L729).
Survives? YES, as a qualifier. Core PBT still grew 313.1% in absolute terms, so "earnings are real" stands. The flat-margin reading does not. A4 never states a margin after funding cost. Graft into Step 2 diagnostic 2, Section C and the brief: "On an all-in basis the margin fell. Core PBT margin fell 70 bps YoY (13.53% to 12.83%). Op EBITDA less finance cost fell 155 bps (14.66% to 13.11%). The working-capital funding cost now takes 1.80% of revenue." Type MISSING.

### Read 2. Claim: "H1 EPS ₹38.60 ... ABOVE BULL on half-year pro-rata (Bull/2 = 32.5)" (A4 L262; Section C L742).
Strongest bear counter: a half-year pro-rata is the wrong yardstick for a front-loaded year. Management's own Rs 4,000 Cr target (CC L458) puts H2 revenue at Rs 1,857.03 Cr, 13.3% below H1 [calc; RES L160]. From Q3 every quarter carries the full 59.445 Mn shares (RES L186).
- To reach Bull Rs 65, FY27 needs H2 EPS of at least Rs 26.40. That is H2 PAT of at least Rs 156.93 Cr, an **H2 PAT margin of at least 8.45%** [calc]. On full-year weighted shares of about 58.48 Mn the threshold is 8.51%.
- H1 PAT margin was 10.36% (RES L179, L160). The drivers A4 itself flags all push toward the threshold: OI from QIP deposits falls as proceeds deploy (A4 L153), finance cost runs at Rs 23.80 Cr a quarter (RES L167), and management hedged the margin (CC L729).
- At the H1 margin the guided path gives FY27 EPS of about Rs 71.0, 9.2% above Bull. The pro-rata framing implies 18.8% above (38.60 vs 32.50) [calc].
Survives? PARTIALLY. "Above Bull" holds on the guided path. The cushion is half what the pro-rata shows, and it depends on a 1.9 pp margin buffer. Graft into Step 6A "Lands In": "Above Bull on the guided path only if H2 PAT margin stays at or above about 8.5% (H1: 10.36%). Pro-rata overstates the cushion." Type MISSING.

### Read 3. Claim: cash failure is inventory, not receivables. "Receivables are improving (period-end 112 to 67 days)". This underpins INDETERMINATE-WITH-DIRECTION rather than a structural reading (A4 L230, L938). Also A4 L660: receivable days claim "CONFIRMED (direction)".
Strongest bear counter: the customer side of working capital also consumed cash, and credit quality moved the wrong way.
- Receivables absorbed Rs 119.75 Cr (RES L268). Other liabilities fell Rs 166.45 Cr (RES L272). Combined customer-side absorption is **Rs 286.20 Cr in H1** [calc]. If other current liabilities hold customer advances, which is A4's own Q8 premise (A4 L350), revenue billed against advances creates no receivable. That flatters receivable days. [INFERENCE: the filing does not state what other liabilities contain.]
- Provision for doubtful debts Rs 3.83 Cr plus bad debts written off Rs 1.51 Cr in H1 FY27, against Rs 0.36 Cr in H1 FY26, is **14.9x** (RES L261-L262). On the call management said "all our debtors that is being reported are all very healthy and top notch" (CC L590). A4's concall-vs-filing table (A4 L656-L672) has no row for this claim.
Survives? YES, as a qualifier and a missing cross-check. It does not force a STRUCTURAL label. Receivable days improved on both methods, and A4 already cites the 90-110 day CCC guide as the structural evidence. It does weaken "receivables improving" as support for the non-structural reading. Graft (a) into Step 5 "Structural or growth-induced?": "The customer leg also absorbed Rs 286.20 Cr (receivables plus the fall in other liabilities). Credit charges rose 14.9x." Graft (b) as a new A4 7A row: '"all our debtors ... very healthy and top notch" (CC L590) | credit charges Rs 5.33 Cr vs Rs 0.36 Cr, 14.9x (RES L261-L262) | PARTIALLY CONTRADICTED'. Type MISSING.

### Mandatory acquisition-economics probe
No document describes an acquisition, a purchase of a business, or a stake buy. The only new-entity item is the Taiwan wholly owned subsidiary. It is a greenfield cash subscription: "Subscription to the share capital will be in cash" and "Cost of subscription / price ... To be determined" (RES L367-L371). Its background reads "Company yet to be incorporated" (RES L359). It has no stated earnings, ROCE, debt, cash or customers, so no price-to-earnings multiple can be computed. Probe: NOT APPLICABLE this quarter. A4 already carries the capital-size question (A4 Q17) and the bear fork (A4 L845). Re-run the probe when the subscription amount is disclosed.

---
## FINDINGS (every finding tagged)
### FACTUAL (loop A4)
- **F1. Regroup margin bound misstated.** A4 L79 says "up to ±0.39%" and A4 L168 says "up to 39 bps". Recomputed: Q2 39 bps, **Q1 64 bps** (52.21/8,196.86 Mn; RES L160, L161, L169). Consequence: A4's sequential "+21 bps" (A4 L149) can be **-43 bps** (item in Q1) or +60 bps (item in Q2). Fix: state 64 bps (Q1) / 39 bps (Q2), and caveat the sign of the Q1 to Q2 margin move in Step 2 diagnostic 2 and Step 3.
- **F2. Recurring share of ΔPAT misstated.** A4 L187 says "About 89%". Recomputed 91.5% [(152.62-0.78-0.28-22.87) x 0.7479 / 105.22]. A4's 89% + 8.5% does not reach 100%. Fix: 91.5%.

### MISSING (loop A4)
- **M1. Read 1 counter survives.** Margin after funding cost fell 155 bps and core PBT margin fell 70 bps YoY. Graft text in Read 1.
- **M2. Read 2 counter survives partially.** EPS "above Bull" needs an H2 PAT margin of at least about 8.5% on the guided path. Graft text in Read 2.
- **M3. Read 3 counter survives.** Customer-side WC absorbed Rs 286.20 Cr. Credit charges rose 14.9x against management's "top notch" debtors claim (CC L590). Grafts (a) and (b) in Read 3.
- **M4. Unrealised FX gain uncited (RES R238, RES L259).** The CF adds back an unrealised FX **gain of Rs 5.64 Cr** in H1 FY27 PBT; H1 FY26 had a Rs 1.81 Cr loss. This filed row bears on A4's top-3 question Q5 (the Rs 5.22 Cr regroup). Q1+Q2 OI less H1 interest income (RES L258, Rs 13.69 Cr) leaves Rs 7.64 Cr of non-interest OI in the quarter columns and Rs 2.42 Cr in the H1 column. The Rs 5.22 Cr gap is the fall in that residual. [INFERENCE] This is consistent with an FX gain shown in quarter OI and netted against other expenses in H1. If so, the filed H1 Op EBITDA margin of 15.07% carries about 24 bps of FX gain (5.22/2,142.97). Fix: cite R238 in Q5, in the Step 1 additivity note and in Step 4 (Other Income "forex").
- **M5. Promoter no-sale test unanchored (A4 L291; 6B #7 L277).** "Drop from 66.98% is QIP dilution [calc]". The extracts give only the Sep-26 holding of 64.16% (PRS L764). 66.98% equals 64.16 x 59.445/56.94, the pre-QIP stake that holds only if no promoter sold. If A4 back-solved it, the test is circular. Thesis-broken #5 "NO on sales" and checklist #7 GREEN rest on it. Fix: anchor 66.98% to its Notion source (Jun-26 shareholding, memory tier), or state "Jun-26 promoter holding NOT FOUND in this run's documents; no-sale reading unverified".
- **M6. Filed sector data absent from SECTOR intelligence (STR R065-R095, R236-R248; STR L297-L356).** The brief says "The filings did not disclose a demand index, a price index or peer data" (A4 L803). It omits the deck's third-party (1Lattice) sizing and policy rows:
  - Indian HPC market Rs 7,140 Cr FY26 to Rs 11,190 Cr FY30P (11.9% CAGR).
  - Private cloud and HCI Rs 45,670 Cr to Rs 91,910 Cr (19.1%).
  - India AI market Rs 32,270 Cr to Rs 1,14,290 Cr (37.2%).
  - AI infrastructure Rs 11,540 Cr to Rs 28,290 Cr (25.1%).
  - AI data-centre capacity 0.24 GW to 4.00-5.50 GW.
  - IndiaAI Mission about Rs 10,300 Cr over FY25-29.
  - NSM 2.0 targets pre-exascale and exascale systems by CY28, "making domestic design and manufacturing key procurement criteria" (STR L347-L352).
  [INFERENCE for the graft] The deck's own projected CAGRs for HPC, private cloud/HCI and AI infrastructure (11.9%, 19.1%, 25.1%) sit below the 30-40% company growth band (CC L491-L509). The band therefore needs share gain. Caveat for A4: several p12 CAGR labels do not reproduce from the printed endpoints. AI data-centre capacity 0.24 to 4.00-5.50 GW over four years computes to 102-119%, against a label of 119.6%-137.8%. Use recomputed CAGRs on the market values and flag the label mapping as A2 did (LAYOUT_ORDER_MAPPING, AMBIGUOUS_MAPPING).

### CONTRADICTION
None raised as a separate finding. The management-vs-filing contradiction on debtor quality is carried inside M3, because A4's gap is the missing cross-check.

---
## VERDICT
**INCOMPLETE.** Loop back to **A4**.
Gap: two FACTUAL arithmetic errors (F1, F2) and six MISSING items (M1-M6): three surviving bear counters to graft, one uncited filed FX row, one unanchored promoter-stake input, and the filed sector data missing from SECTOR intelligence. Every fix draws on rows already in the A1 extracts and A2 ledgers. No A2 or A3 re-run is needed. The fixes narrow A4's positive claims. None of them changes the protocol verdict (PROCEED WITH FLAGS) or the thesis-broken #1 flag. Re-audit after the A4 revision should check only these eight items plus the five-part gate.

---
## STYLE NOTES (logged; no loop)
- **S1.** Wrong anchor: A4 L290 cites PRS R302-R303 for the quote "OEM partnership with Nvidia & AMD". R302 is a technology-partner list and R303 reads "NVIDIA OEM partnership". The quoted phrase is at PRS L240 (p8, inside R312) and STR L217 (p7, no row). Re-anchor.
- **S2.** Mixed periods at A4 L189: finance cost QoQ +106.5% is set against period-end debt +18.3%, which is the Mar to Sep (H1) change. Label it H1.
- **S3.** A4 L145 "Trails PAT by 10.7 pp (QIP dilution)". About 8.4 pp comes from the QIP. About 2.3 pp comes from the 0.285 Mn shares allotted between Sep-25 and Mar-26 (RES L186: 113.31 to 113.88). The numbers are right; the label is incomplete.
- **S4.** Brief A4 L785 says management "warned that the first-half margin will not hold for the full year". The transcript says the H1 margin is "not to be quoted for the entire year" (CC L729). Suggest: "said the H1 margin should not be assumed for the full year".
- **S5.** Specificity numerator (A4 L643) counts R170, R173, R179 and R196 as binary milestones. They are qualitative statements. Without them the ratio is 13/44 = 0.30. The archetype (ratio at or below 0.5) does not change.
- **S6.** Process hygiene: the press-release ledger file has no embedded A2 YAML block. The block itself exists at `work/blocks/a2-pressrelease.yaml`. Rows M001-M004 exist only in the ledger; no A1 addendum created them, unlike results R429. A4 reviewed them (A4 L21, L167, L290). No content was lost.
- **S7.** Call-date narrowing, optional: the CFO said "I trust you have had the opportunity to review our earnings presentation and press release" (CC L161-L162). The earnings deck was signed 16:46:54 IST on 24-Oct (PRS L48-L49). The call therefore took place after that time at the earliest. This narrows the 24-Oct vs 26-Oct conflict (A4 L10, L401) but does not resolve it.

---
```yaml
stage: A5-adversary
company: "NETWEB"
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
  - {metric: "Rs 5.22 Cr regroup: per-quarter Op EBITDA margin bound and Q1-to-Q2 sign", a4_value: "up to ±0.39% / 39 bps (A4 L79, L168); Q1 to Q2 +21 bps (A4 L149)", recomputed: "Q2 39 bps; Q1 64 bps (52.21/8,196.86 Mn); Q1 to Q2 ranges -43 bps (item in Q1) to +60 bps (item in Q2)", source_line: "RES L160, L161, L169"}
  - {metric: "Recurring share of Q2 YoY PAT change", a4_value: "about 89% (A4 L187)", recomputed: "91.5% = (152.62-0.78-0.28-22.87) x 0.7479 / 105.22; complement of the 8.5% OI share", source_line: "RES L160-L179"}
surviving_bear_counters:
  - {claim: "Earnings real; Op EBITDA margin held at 14.91% (A4 L938, L149, L778)", counter: "Margin after WC funding cost fell: (Op EBITDA - finance cost)/revenue 14.66% to 13.11% (-155 bps); core PBT margin 13.53% to 12.83% (-70 bps); finance cost/revenue 0.31% to 1.80%", source_line: "RES L160, L161, L167, L168, L173; CC L729", type: MISSING}
  - {claim: "H1 EPS Rs 38.60 above Notion FY27 Bull on half-year pro-rata (A4 L262)", counter: "Pro-rata misfits a front-loaded year; on the Rs 4,000 Cr guided path (H2 Rs 1,857.03 Cr) and 59.445 Mn shares, Bull Rs 65 needs H2 PAT margin of at least about 8.5% vs H1 10.36%; cushion about 9% above Bull, not about 19%", source_line: "RES L160, L179, L186, L190; CC L458", type: MISSING}
  - {claim: "Receivables improving, so cash failure is inventory-only; supports INDETERMINATE over structural (A4 L230, L660)", counter: "Customer-side WC absorbed Rs 286.20 Cr (receivables Rs 119.75 Cr + other liabilities -Rs 166.45 Cr); credit charges Rs 5.33 Cr vs Rs 0.36 Cr (14.9x) contradict management's 'all our debtors ... very healthy and top notch'", source_line: "RES L261, L262, L268, L272; CC L590", type: MISSING}
findings_by_type:
  factual:
    - "F1: Regroup margin bound misstated as up to 39 bps (A4 L79, L168); Q1 bound is 64 bps; the Q1-to-Q2 +21 bps (A4 L149) can be -43 bps. Source RES L160, L161, L169."
    - "F2: Recurring share of dPAT stated about 89% (A4 L187); recomputed 91.5%. Source RES L160-L179."
  missing:
    - "M1: Graft Read 1 counter (margin after funding cost -155 bps; core PBT margin -70 bps) into Step 2, Section C, brief."
    - "M2: Graft Read 2 counter (Bull needs H2 PAT margin >= ~8.5% on the Rs 4,000 Cr path) into Step 6A Lands In."
    - "M3: Graft Read 3 counter (customer-side WC Rs 286.20 Cr; credit charges 14.9x) into Step 5, and add a 7A row for CC L590 vs RES L261-L262."
    - "M4: Unrealised FX gain Rs 5.64 Cr in H1 PBT (RES R238, L259) uncited; bears on the Rs 5.22 Cr regroup (Q5) and on H1 margin quality (~24 bps if netted in other expenses) [INFERENCE]."
    - "M5: Promoter 66.98% pre-QIP stake (A4 L291) appears in no extract; equals 64.16 x 59.445/56.94, so the no-sale test is circular unless anchored to Notion Jun-26 data; #5 NO and #7 GREEN rest on it."
    - "M6: SECTOR brief omits filed sector data (STR R065-R095, R236-R248; L297-L356: market sizes, CAGRs, IndiaAI ~Rs 10,300 Cr, NSM 2.0 exascale by CY28) and says none was disclosed (A4 L803); graft with recomputed CAGRs."
  contradiction: []
  style:
    - "S1: A4 L290 anchors 'OEM partnership with Nvidia & AMD' to PRS R302-R303; phrase is at PRS L240 / STR L217."
    - "S2: A4 L189 sets QoQ finance cost against H1 debt change; label H1."
    - "S3: A4 L145 attributes the 10.7 pp EPS gap to QIP only; about 2.3 pp is the Sep-25 to Mar-26 allotment."
    - "S4: Brief A4 L785 'will not hold' overstates CC L729 'not to be quoted for the entire year'."
    - "S5: Specificity counts four qualitative rows as binary milestones; 13/44 = 0.30 without them; archetype unchanged."
    - "S6: PR ledger file lacks an embedded A2 YAML block (block exists in work/blocks/a2-pressrelease.yaml); M001-M004 are ledger-only rows; no content loss."
    - "S7: CC L161-L162 places the call after the 16:46:54 IST 24-Oct deck filing at the earliest; narrows the date conflict."
loop_back_to: "A4"
gap: "A4 to (1) restate the regroup bound as 64 bps Q1 / 39 bps Q2 and caveat the Q1-to-Q2 margin sign (A4 L79, L149, L168); (2) restate recurring dPAT share as 91.5% (A4 L187); (3) graft the three surviving bear counters (Reads 1-3, incl. a 7A row for CC L590 vs RES L261-L262); (4) cite the unrealised FX gain RES L259 in Q5, Step 1 and Step 4; (5) anchor or withdraw the 66.98% pre-QIP promoter stake behind #5 and #7; (6) add STR L297-L356 sector data to SECTOR intelligence and drop the 'no demand data' line. No A2/A3 re-run needed."
style_notes:
  - "S1 re-anchor OEM quote to PRS L240 / STR L217"
  - "S2 label debt change as H1 at A4 L189"
  - "S3 split EPS dilution gap: ~8.4 pp QIP, ~2.3 pp earlier allotment"
  - "S4 brief: 'should not be assumed for the full year' per CC L729"
  - "S5 specificity 13/44 = 0.30 if four qualitative rows excluded; archetype unchanged"
  - "S6 PR ledger file has no embedded YAML (block in work/blocks/a2-pressrelease.yaml); M001-M004 ledger-only"
  - "S7 call took place after 16:46:54 IST 24-Oct at the earliest (CC L161-L162, PRS L48-L49)"
analyst_note: "Orphan standard: A4's preamble (L18-22) marks every ledger row reviewed. A4 cites rows for every note, agenda item, Annexure II row, auditor paragraph, turn, question and data slide. I accepted that mark for uncited administrative rows and tested uncited rows for material content instead of failing about 1,620 IDs mechanically. Two uncited clusters carry material content: the unrealised FX gain (RES R238) and the strategy-deck sector data (STR R065-R095, R236-R248). Both are A4 grafts from the extracts, so no A2 or A3 re-run is needed. Of about 120 recomputed values, two fail. The bear counters do not overturn PROCEED WITH FLAGS or the thesis-broken #1 flag. They narrow three positive claims: margin after funding cost fell 155 bps, the EPS Bull cushion holds only if H2 PAT margin stays at or above about 8.5%, and the customer side of working capital also absorbed cash. No document describes an acquisition. The Taiwan WOS is a greenfield subscription with cost to be determined, so no earnings multiple exists to test."
```

---
# LOOP 1 RE-AUDIT (the one permitted re-audit)
Agent A5 | model claude-opus-5-5 | 28-Oct-2026.
Review under re-audit: the revised `work/review_netweb_q2fy27.md` (987 lines). It has a REVISION LOG at A4 L783-L798 and inline `[REV1-<id>]` tags. In this section, `A4 Lnnn` means a line in the REVISED file. My inputs did not change. I re-checked every tagged line against the A1 extracts and recomputed every new or changed number. The loop-0 sections above stand as the record of the first pass.

## R0. Deliverable-completeness gate (re-run)
| Brief part | Location (revised) | Check | Status |
|---|---|---|---|
| (1) Summary narrative | A4 L804-L820 | 16 lines (L805-L820), inside the 10-20 band; M1 lines (L807-L808) and S4 line (L815) present | PRESENT |
| (2) Sector intelligence | A4 L822-L845 | 23 lines; M6 graft at L824-L835; old "no demand index" line replaced at L845 | PRESENT |
| (3) Business-model intelligence | A4 L847-L859 | 12 lines; M1 line L853 added | PRESENT |
| (4) Competition intelligence | A4 L861-L871 | unchanged, 10 lines | PRESENT |
| (5) Forward map | A4 L873-L889 | unchanged; make-or-break reading plus 11 catalysts, each with a bull fork and a bear fork | PRESENT |

Gate: PASS.

## R1. Closure of loop-0 FACTUAL and MISSING items
| Item | Type | Revised lines | Re-check against the extract | Status |
|---|---|---|---|---|
| F1 | FACTUAL | L74, L79, L156, L170, L171, L175 | Bound 52.21/8,196.86 = 64 bps (Q1), 52.21/13,232.79 = 39 bps (Q2). Q1 to Q2 move -43 to +60 bps (RES L160, L161, L169). The "+" sign on the quarter that carries the item is right: netting lowers that quarter's OI and raises its Op EBITDA. | CLOSED |
| F2 | FACTUAL | L194 | (152.62-0.78-0.28-22.87) x 0.7479 / 105.22 = 91.5%; 11.94 x 0.7479 = 8.93 = 8.5%; the two shares now sum to 100% | CLOSED |
| M1 | MISSING | L140-L143, L156, L673, L753, L807-L808, L852-L853; flag L969 | 445.34/3,037.24 = 14.66%; 1,734.99/13,232.79 = 13.11% (-155 bps); core PBT 411.02/3,037.24 = 13.53% to 1,697.87/13,232.79 = 12.83% (-70 bps); finance cost/revenue 0.31% to 1.80% (RES L160-L173) | CLOSED |
| M2 | MISSING | L271, L274, L479, L753; flag L970 | 38.60/32.50-1 = 18.8%; 1,857.03/2,142.97-1 = -13.3%; 26.40 x 59.445 Mn = Rs 156.93 Cr; /1,857.03 = 8.45%; 8.51% on 58.48 Mn weighted shares; FY27 at the H1 margin about Rs 70.96 (+9.2% vs Bull); buffer 10.36-8.45 = 1.91 pp (RES L160, L179, L186, L190; CC L458) | CLOSED |
| M3 | MISSING | L208-L211, L239, L669, L671, L753-L755; flag L968 | -119.75-166.45 = -286.20 (RES L268, L272). New H1 FY26 comparator -55.84+218.87 = +163.04; change -449.24. Both correct. Credit charges 5.33 vs 0.36 (RES L261-L262); inventory build 1,125.85/286.20 = 3.9x. New 7A row for CC L590 present. A4 kept INDETERMINATE-WITH-DIRECTION and gave a reason. This matches my loop-0 view that the counter does not force STRUCTURAL. | CLOSED |
| M4 | MISSING | L117 (memo row), L133, L160, L171, L186, L316, L357, L674; flag L975 | Unrealised FX (56.38) Mn = Rs 5.64 Cr gain; 18.08 Mn = Rs 1.81 Cr loss (RES L259). 21.33-13.69 = 7.64; 16.11-13.69 = 2.42; gap 5.22; 5.22/2,142.97 = 24 bps. The body tags the FX link [INFERENCE] (L133, L171) and keeps Q5 open. | CLOSED (tagging note N1) |
| M5 | MISSING | L95, L287, L301, L727; flag L978 | 66.98% is now anchored to Notion memory (`work/notion_checklist_2026-10-26.md` line 66), labelled "memory, not filed". The #7 and #5 statuses now read "memory-anchored". 66.98 x 56.94/59.445 = 64.16. Share capital is the same at Mar-26 and Jun-26 (RES L186: 113.88), so a Mar-26 figure serves. A5 did not open the memory file because it sits outside the A5 input set. The gap was provenance, and the revision closes it. | CLOSED |
| M6 | MISSING | L824-L835, L845 | HPC 71.4 to 111.9 bn = 11.89%; private cloud/HCI 456.7 to 919.1 = 19.11%; AI market 322.7 to 1,142.9 = 37.18%; AI infrastructure 115.4 to 282.9 = 25.13%. The Rs Cr conversions (x100) are correct. IndiaAI ~103 bn = Rs 10,300 Cr (STR L347); NSM 2.0 CY28 (STR L348-L352). Three of the four rates sit below 30%. HPC share 530.8/7,140 = 7.43%: FY26 HPC is 5,308 Mn (PRS L651-L653), and the series mapping is confirmed by the 42.2% FY24-26 CAGR label (PRS L680). The "no demand index" line is gone. | CLOSED (tagging note N2) |

Style items from loop 0: S1 adopted (L300: PRS L240, STR L217). S2 adopted (L196). S3 adopted (L151: 8.4 + 2.3 = 10.7 pp). S4 adopted (L815, verbatim CC L729). S7 adopted (L10, L411). S5 not adopted; it stays logged as STYLE with no loop. S6 was a process note outside A4's remit.

## R2. Arithmetic re-audit of every changed line
| New or changed number (A4 line) | Recomputed | Source | Status |
|---|---|---|---|
| Q1 / Q2 margin +64 / +39 bps (L170-L171) | as F1 | RES L160, L161, L169 | PASS |
| 91.5% recurring; 8.93 OI after tax (L194) | as F2 | RES L160-L179 | PASS |
| 14.66% / 13.11% / -155 bps; 13.53% / 12.83% / -70 bps; 0.31% / 1.80% (L141-L143) | as M1 | RES L160-L173 | PASS |
| Customer leg +163.04 / (286.20) / -449.24 (L208) | -558.36+2,188.73 = +1,630.37 Mn; -1,197.49-1,664.46 = -2,861.95 Mn | RES L268, L272 | PASS |
| Credit charges 0.36 / 5.33 / 14.9x (L209) | 3.57 / 53.31 Mn | RES L261-L262 | PASS |
| 3.9x inventory vs customer leg (L239) | 1,125.85/286.20 = 3.93 | RES L271, L268, L272 | PASS |
| EPS note: 18.8%, -13.3%, 26.40, 156.93, 8.45%, 8.51%, about 71.0, 9.2%, 1.9 pp (L274) | as M2 | RES L160, L179, L186, L190; CC L458 | PASS |
| FX memo 1.81 loss / (5.64) gain; 7.64 / 2.42 / 5.22; 24 bps (L117, L133) | as M4 | RES L161, L258, L259 | PASS |
| EPS gap split 8.4 / 2.3 pp (L151) | QIP-only weighted shares 57.771 vs 56.655 Mn: EPS +326.4%, gap 8.4 pp; remainder about 2.1-2.3 pp | RES L186, L190, L312 | PASS |
| Market rates and Rs Cr values (L825-L831); HPC share 7.4% (L835) | as M6 | STR L297-L352; PRS L651-L653 | PASS |
| Call after 16:46:54 IST 24-Oct (L10, L411) | deck signature time | PRS L48-L49; CC L161-L162 | PASS |

Arithmetic result: no mismatch on any changed line.

## R3. Adversarial re-read of the changed lines
The revision adds bear-side qualifiers. Its new or restated positive claims are these three:
- "Classification kept: INDETERMINATE-WITH-DIRECTION" (L239). Bear counter: the guided 90-110 day CCC "even going forward" (CC L374, L381) plus the customer-leg drain argue STRUCTURAL. Does it survive? NO new graft. A4 now states both items and gives a reason tied to filed evidence: receivable days improved on both methods, and the 31-Mar-2027 inventory and FY27 CFO are not yet filed. The flag (L968) records the firmer adverse direction.
- "#7 GREEN / #5 NO on a memory-anchored basis" (L287, L301). Bear counter: the input is memory, not filed. A4 now discloses that in the cell, the status label and flag L978. No graft needed.
- "Netweb's HPC revenue was about 7.4% of that market" (L835). Neutral claim. The bear point is that it assumes the two HPC definitions match, which is a tagging issue (N2), not a surviving counter.
No new surviving counter. The acquisition probe is unchanged: NOT APPLICABLE, because the Taiwan WOS is still a greenfield subscription with cost to be determined (RES L367-L371).

## R4. New errors introduced by the revision
No FACTUAL, MISSING or CONTRADICTION finding. Three new STYLE notes, logged with no loop:
- **N1.** Summary fields firm an inference without its tag. Section C L753 says "likely FX-linked". Flag L975 says "likely the Rs 5.64 Cr unrealised FX gain". The A4 analyst_note says "likely reflects". The amounts differ (5.22 vs 5.64), and the filing does not say what the item is. The body tags the link correctly ([INFERENCE] at L133 and L171) and keeps Q5 open. Suggest: "consistent with FX netting (H1 unrealised FX gain Rs 5.64 Cr) [INFERENCE]". This changes no number, filed fact or verdict.
- **N2.** L835 tags the 7.4% HPC share [FILED, calc]. The arithmetic is filed. The claim that the 1Lattice "Indian HPC market" and Netweb's "HPC systems" line share one definition is an inference. Suggest the tag [FILED, calc, INFERENCE] and the anchor PRS L651-L653.
- **N3.** The REVISION LOG M4 line list (L790) cites line 118 for the memo row. The memo row is at L117; L118 carries the tag. Cosmetic.
Carried forward: S5 (specificity numerator), not adopted, still STYLE.

## R5. VERDICT (loop 1)
**COMPLETE.** All loop-0 FACTUAL and MISSING items (F1, F2, M1-M6) are closed against the extracts. Every changed number recomputes. The five-part brief passes. No new counter survives. Only STYLE notes remain (N1-N3, plus S5 carried forward). They are recorded and do not trigger a re-run. A4's protocol verdict (PROCEED WITH FLAGS), cash classification (INDETERMINATE-WITH-DIRECTION) and the thesis-broken #1 flag are unchanged. The review may proceed to the Notion save step.

```yaml
stage: A5-adversary
company: "NETWEB"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
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
findings_by_type:
  factual: []
  missing: []
  contradiction: []
  style:
    - "N1: Summary fields state the FX link as 'likely' without the [INFERENCE] tag (Section C A4 L753, flag L975, A4 analyst_note); amounts differ (5.22 vs 5.64). Body tags it correctly (L133, L171). Suggest 'consistent with FX netting [INFERENCE]'."
    - "N2: A4 L835 HPC share 7.4% tagged [FILED, calc]; definitional match of 1Lattice HPC market and Netweb HPC systems is an inference. Add INFERENCE tag and anchor PRS L651-L653."
    - "N3: REVISION LOG L790 cites line 118 for the M4 memo row; the row is at L117."
    - "S5 (carried from loop 0, not adopted): specificity 13/44 = 0.30 if four qualitative rows are excluded; archetype unchanged."
loop_back_to: ""
gap: ""
style_notes:
  - "N1 tag the 'likely FX' wording in Section C, flag L975 and analyst_note as [INFERENCE]; say 'consistent with'"
  - "N2 add INFERENCE tag and PRS L651-L653 anchor to the 7.4% HPC share at A4 L835"
  - "N3 revision log M4 line list: memo row is L117, not L118"
  - "S5 specificity numerator includes four qualitative rows; 13/44 = 0.30; archetype unchanged"
analyst_note: "Loop 1 re-audit. All eight loop-0 items (F1, F2, M1-M6) close against the extracts, and every changed number recomputes. A4 adopted five of the seven loop-0 style notes (S1-S4, S7). S5 stays logged; S6 was a process note outside A4. The revision adds only bear-side qualifiers. It keeps PROCEED WITH FLAGS and INDETERMINATE-WITH-DIRECTION and states the reasons. M5 closes on provenance: the 66.98% input now carries a Notion memory anchor. A5 did not open that file because it sits outside the A5 input set. Three new style notes: the summary fields call the Rs 5.22 Cr regroup 'likely' FX without an [INFERENCE] tag, though the body tags it; the 7.4% HPC share needs an inference tag for the definitional match; and one revision-log line number is off by one. None changes a number, a filed fact or the verdict. Verdict COMPLETE; the review may proceed to save."
```
