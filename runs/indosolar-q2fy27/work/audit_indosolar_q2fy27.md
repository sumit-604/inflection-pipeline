# A5 ADVERSARY / COMPLETENESS AUDIT: INDOSOLAR Q2 FY27

Company: Indosolar Limited (INDOSOLAR) | Quarter: q2fy27 (quarter ended 30-Sep-2026)
Agent: A5 adversary | Model: claude-opus-5-5 | Run date: 2026-10-23
Status: COMPLETE (all four audits run). Verdict: **INCOMPLETE**, loop back to A4.

Inputs read: A4 review (work/review_indosolar_q2fy27.md), A1 fulltexts (extracted/indosolar-results-q2fy27-fulltext.md, extracted/indosolar-presentation-q2fy27-fulltext.md), A1 structured files (both), A2 ledgers (both). I did not open the source PDF or anything under inputs/. I did not read A3 forensics. I re-derived everything from the A1 lakh values.

Anchor key: "L" = line in the results fulltext. "PR L" = line in the presentation (press release) fulltext. "A4 L" = line in the A4 review. "R###" = results structured row. "PR-R###" = press-release structured row.

---

## AUDIT 0: DELIVERABLE COMPLETENESS (hard gate)

The plain-language brief is at A4 L480-536.

| Part | Heading (A4 line) | Status | Check |
|---|---|---|---|
| 1. Summary narrative | "1. SUMMARY NARRATIVE" (A4 L482) | PRESENT | 13 lines (A4 L483-495), inside the 10-20 line band. Real content, tier-tagged. |
| 2. Sector intelligence | "2. SECTOR INTELLIGENCE" (A4 L497) | PRESENT | 5 bullets (A4 L498-502). Management claims anchored; background tagged SECONDARY, PENDING LIVE VERIFICATION. |
| 3. Business-model intelligence | "3. BUSINESS-MODEL INTELLIGENCE" (A4 L504) | PRESENT | 8 bullets (A4 L505-512), tolling vs owned economics with numbers. |
| 4. Competition intelligence | "4. COMPETITION INTELLIGENCE" (A4 L514) | PRESENT | 6 bullets (A4 L515-520). |
| 5. Forward map | "5. FORWARD MAP" (A4 L522) | PRESENT | 10 catalysts (A4 L527-536), each with a bull fork and a bear fork. Seven dated or "Immediate"; three dated NOT FOUND (M3, M4, M5) because no extract carries a date. No date is invented. |

Gate result: PASS. All five parts are present and carry real content.

---

## AUDIT 1: COVERAGE

### 1A. Fresh enumeration vs A2 ledger: results filing

My pass: Grep over the results fulltext. Pipe-delimited lines = 96, less 8 non-table lines (L65, L71, L75, L109, L113, L163, L167, L212) = 88 statement lines. Dash cells counted on L92, L96, L99, L100, L103, L120, L175, L176, L196, L197, L201, L202, L203. Numbered notes found by pattern `^[1-6] [A-Z]` on page 5 (L215, L217, L220, L222, L225, L227).

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Numbered notes | 6 (R371-R376) | 6 (L215-227) | none | PASS |
| Footnote-type rows | 4 (R360, R381-R383) | 4 (L104 EPS not annualised; L92 exceptional nil; L109 date repair; L283 UDIN) | none | PASS |
| Statement line items | 88 | 88 (P&L 25, balance sheet 32, cash flow 31) | none | PASS |
| Structured cells for those lines | 276 (R001-R276) | 276 (25x6 + 32x2 + 31x2) | none | PASS |
| ZERO_STANDING cells | 34 | 34 (6+6+3+6+5 on P&L; 1 on BS; 7 on CF) | none | PASS |
| Agenda items (board outcome) | 0 | 1 (L40-44: item 1, results approval) | none (rows R340, R359, R335 sit in ledger sec 4) | STYLE: category count differs, no row missing |
| Auditor paragraphs | 7 (labelled R377-R383) | 4 numbered paragraphs (L247, L252, L258, L267) plus signature/UDIN block; auditor rows R377-R380, R383 | none | STYLE: A2 label includes R381 and R382, which are not auditor rows |
| Entities | 27 (R308-R334) | 28 | none | STYLE: www.sgco.co.in (L287, auditor website) has no ENTITY row |
| Signatures | 2 | 3 (CS letter L51-56; director L229-233; audit partner L274-282) | none (partner rows R329, R300, R355 sit in ledger sec 5) | STYLE: category count differs, no row missing |
| Structured IDs referenced in ledger | 383 of 383 | 383 (header counts 307+27+4+20+25 re-added) | none | PASS |

### 1B. Fresh enumeration vs A2 ledger: press release (presentation doctype)

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Pages | 3 | 3 | none | PASS |
| Numbers | 41 | 41 (3 headline, 26 table cells PR L123-127, 10 bullet values PR L97-101, scrip code, 1.3 GW) | none | PASS |
| Entities | 19 (incl. 2 summaries) | 19 | none | PASS |
| Forward / management claims | 7 | 8 | none | STYLE: the first CEO sentence (PR L109-110, "industry is undergoing an important phase of transformation ... India's increasing focus on domestic manufacturing") has no row. A4 carries it at A4 L499, so no claim is lost from the review. |
| Dates | 10 | 10 | none | PASS |
| Qualifiers | 7 | 7 | none | PASS |
| ZERO_STANDING | 0 | 0 | none | PASS |
| Structured IDs referenced in ledger | 84 of 84 | 84 | none | PASS |

Tagging note on the two unenumerated units (www.sgco.co.in; PR L109-110). The extract holds both and the structured file does not. Neither changes a number, a fact or a conclusion: one is a contact website, and A4 already quotes the other. Under the finding-type rules they are STYLE. They are listed in `missing_from_ledger` for the record, with no loop.

### 1C. Ledger rows vs A4 review (orphan test)

A4 L26 states that it reviewed 383 of 383 results IDs and 84 of 84 press-release IDs, and that no row is unreviewed. I tested that claim against the rows A4 never names. Rows not named in A4 are: right-of-use R155-R156, intangible R157-R158, security deposit R159-R160, non-current other financial assets R161-R162, income tax assets R165-R166, non-current provision R193-R194, other non-current liabilities R195-R196, warranty provision R225-R226, and the subtotal and total rows. I re-derived each one and none carries a finding:
- Warranty provision is 0.464% of H1 FY27 goods sales against 0.458% of H1 FY26 goods sales (77.36 / 16,674.51 vs 158.54 / 34,591.14; L178, L78). The ratio is stable.
- Income tax assets rose 50.45 lakh (L127). Tax paid was 54.12 lakh (L192), so the payment sits as an asset. This fits a period with no current tax.
- Other non-current liabilities: see the tie-out in 1D.

Every material row I tested is cited by A4 at line level. Result: orphan rows = none.

### 1D. Independent tie-outs (observations, not findings)
- The three statements foot in both periods. Balance-sheet totals: 48,295.78 and 34,440.30 lakh (L138, L161). The cash flow closes to balance-sheet cash 8,115.51 (L206 = L133). Other-equity movement 4,160.11 = H1 TCI (L142, L101).
- Cash-flow "other liabilities" +8,699.16 (L190) = change in other current liabilities 8,199.23 (L159) + change in other non-current liabilities 286.31 (L149) + deferred-grant drawdown 213.62 (grant recognised 669.16, L176, less received 455.54, L197). It ties to the lakh. So the deferred grant sits inside other liabilities, which supports A4's non-cash-grant reading and narrows A4 Q9.

---

## AUDIT 2: ARITHMETIC

I recomputed every derived figure from the A1 lakh values (x0.01 = Rs Cr). The table groups rows where every period matches.

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Step 1 conversions, 22 P&L rows x 6 periods | as tabled (A4 L83-104) | all match to 0.01 Cr | L78-106 | PASS |
| Revenue Q2 FY27 | 155.59 | 15,277.09 + 281.54 = 15,558.63 lakh | L78-79 | PASS |
| Total expenses foot Q2 FY27 | 15,045.66 lakh | 15,045.66 | L83-90 | PASS |
| 6M Sep-26 = Q1 + Q2, every P&L line | holds | holds | L78-97 | PASS |
| EPS on PAT vs TCI basis | 1.2063 / 10.0082 vs filed 1.20 / 10.00 | PAT 1.2063 / 10.0082; TCI 1.1974 / 9.9994 | L97, L101, L105 | PASS |
| Operating EBITDA (Q2FY26, Q1FY27, Q2FY27, FY26, H1FY26, H1FY27) | 70.73 / 48.46 / 14.82 / 270.75 / 134.29 / 63.28 | same | L80, L87, L88, L91 | PASS |
| Operating EBITDA margin | 34.92 / 70.89 / 9.52 / 39.82 / 33.81 / 28.26 % | same | as above, L78-79 | PASS |
| Reported EBITDA and margin | 70.74 / 56.85 / 16.40 / 272.26 / 135.62 / 73.25; 34.92 / 83.16 / 10.54 / 40.05 / 34.14 / 32.71 % | same | L87, L88, L91 | PASS |
| Core PBT and core PBT / revenue | 61.13 / 39.08 / 5.13 / 232.77 / 114.96 / 44.21; 30.18 / 57.17 / 3.30 / 34.24 / 28.94 / 19.74 % | same | L80, L91 | PASS |
| Other Income / PBT | 0.02 / 17.67 / 23.55 / 0.65 / 1.15 / 18.40 % | same | L80, L91 | PASS |
| Effective tax rate | 24.21 / 22.86 / 25.21 / -5.26 / -40.27 / 23.15 % | same | L91, L95 | PASS |
| PAT margin on revenue | 22.88 / 53.57 / 3.23 / 36.27 / 41.07 / 18.59 % | same | L97 | PASS |
| Release PAT margin on total income | 3.19 / 22.88 / 17.80 / 40.93 % | same | PR L127; L81, L97 | PASS |
| Gross margin | 41.81 / 89.66 / 18.89 / 47.08 / 40.44 / 40.49 % | same | L78-79, L83-84 | PASS |
| Services share of revenue | 15.49 / 79.56 / 1.81 / 29.59 / 12.92 / 25.54 % | same | L79 | PASS |
| Materials / Sale of Goods | 68.85 / 50.58 / 82.61 / 75.16 / 68.39 / 79.93 % | same | L78, L83-84 | PASS |
| Step 2 YoY: revenue, Op EBITDA, D&A, finance, EBIT, core PBT, PBT, PAT, EPS | -23.19 / -79.05 / +4.47 / -84.72 / -91.56 / -91.61 / -89.02 / -89.17 / -89.23 % | same (EBIT 61.51 / 5.19) | L78-97 | PASS |
| Op EBITDA margin change YoY | -25.40 pp | -25.395005 pp, rounds to -25.40 | L78-91 | PASS |
| Reported EBITDA margin change YoY | -2,438 bps | -2,438 bps | L87-91 | PASS |
| H1 YoY set | -43.62 / -52.88 / -61.54 / -53.41 / -74.48 / -74.50 / +3.33 / +648.48 % | same | L78-105 | PASS |
| MW sold and produced YoY | -60.64 / -39.34 % | same | PR L100-101 | PASS |
| Core PBT change YoY (A4 L153) | -55.99 Cr | -5,599.60 lakh = -55.996, rounds to -56.00 (A4 itself uses -56.00 at A4 L207) | L80, L91 | ROUNDING (STYLE) |
| Tax fall, rate effect, PAT change | 13.11 / -0.07 / -41.32 | same | L95, L97 | PASS |
| D&A / revenue | 6.19 / 4.55 % | same | L88, L78-79 | PASS |
| Grant + interest + asset profit vs H1 OI | 9.93 of 9.97; residual 0.03 | 993.39 of 996.75 lakh; residual 3.36 lakh | L175-176, L179, L80 | PASS |
| Step 3 Q1 FY26 derived (revenue, margin, core PBT, tax credit, PAT, PBT) | 194.68 / 32.65% / 53.84 / 61.64 / 116.79 / 55.16 | same | L78-97 | PASS |
| Step 3 H2 FY26 derived (revenue, margin, core PBT, tax, services %, quarterly averages) | 282.62 / 48.28% / 117.81 / 34.52 / 53.02% / 141.31 / 58.90 | same | L78-95 | PASS |
| Q2 FY26 revenue QoQ; Q1 FY27 vs H2 average | +4.04% / -51.62% | same | L78-79 | PASS |
| Q2 FY27 revenue QoQ (A4 L173) | +127.60% | 15,558.63 / 6,836.14 = 2.275939, i.e. +127.59% | L78-79 | ROUNDING (STYLE) |
| Q2 FY27 Op EBITDA, core PBT, PAT QoQ | -69.42 / -86.87 / -86.30 % | same | L80-97 | PASS |
| Q1 FY27 materials / revenue | 10.34% | 706.84 / 6,836.14 = 10.34% | L83-84 | PASS |
| H1 FY27 average revenue per quarter (A4 L178) | 111.98 | 11,197.385 lakh = 111.97 | L78-79 | ROUNDING (STYLE) |
| Q2 Op EBITDA shortfall vs H1 average (A4 L178) | 53.16% | 1 - 1,481.78 / 3,164.04 = 53.17% | L80-91 | ROUNDING (STYLE) |
| Goods share Q2 FY26 / Q2 FY27; goods spread change | 84.51 / 98.19 %; -1,376 bps | same | L78-79, L83-84 | PASS |
| **Mix share of the YoY gross-margin fall (A4 L181, L466, L488, L595, L607)** | **nil: "Mix shift does not explain the YoY fall"; "not a mix artifact"** | **Mix 9.42 pp of the 22.92 pp fall (41%); goods spread 13.51 pp (59%). In Rs Cr: tolling gross profit -28.55, goods volume -5.73, goods spread -21.02 (total -55.30)** | **L78, L79, L83, L84** | **FAIL (FACTUAL)** |
| Step 4 PAT bridge, all 9 components and foot | -19.63 / -35.67 / -0.61 / -0.41 / +0.33 / +1.57 / +13.17 / -0.07 = -41.32; lakh foot -4,131.91 | same | L78-97 | PASS |
| Step 4 % of Q2 FY26 PAT column | -42.37 / -76.97 / -1.31 / -0.89 / +0.70 / +3.39 / +28.43 / -0.15 % | same | L97 | PASS |
| Step 4 shares of PAT change | 135.5% / -3.8% / -31.7% | same | L80-97 | PASS |
| PAT with OI at prior-year level | 3.84 | 514.08 x (1 - 0.252109) = 384.48 lakh | L80, L91, L95 | PASS |
| FY26 PAT at 25.17% statutory tax; shield; EPS | 175.32 / 71.28 / 42.14 | same | L91, L97, L102 | PASS |
| DTA drawdown = H1 tax | 12.54 | 1,231.45 + 22.81 = 1,254.26 lakh | L126, L95 | PASS |
| Step 5 CFO, CFO/PAT, CFO/Op EBITDA | 71.28 / 79.57 (+11.63%); 0.44x / 1.91x; 0.53x / 1.26x | same | L193, L97 | PASS |
| Step 5 capex, FCF | 11.23 / 4.87 (-56.62%); 60.04 / 74.70 (+24.40%) | same | L195, L193 | PASS |
| WC change and swing | -65.44 / +16.02; +81.46 | same | L180, L191 | PASS |
| Receivable / inventory / payable days; CCC | 112.54 / 13.28; 21.39 / 304.80; 20.30 / 42.60; 113.63 / 275.48 | same | L130-132, L155-156, L78-84 | PASS |
| Net cash excl. and incl. leases | 5.76 / 85.42; 2.69 / 82.23 | same | L133-134, L147, L153 | PASS |
| WC composition, 9 lines | net +16.02 | same | L182-190 | PASS |
| Net working capital | 197.17 / 188.07 | 19,716.66 / 18,807.23 lakh | L130-136, L153-159 | PASS |
| Receivable and payable BS-vs-CF gaps | 34.94 / 37.25 | 19,335.91 - 15,841.73; 4,826.42 - 1,101.24 | L132, L155-156, L186-187 | PASS |
| Inventory outside P&L line; inventory / Q2 revenue; inventory multiple | 80.25; 1.43x; 10.5x | same | L84, L130, L185 | PASS |
| Interest recognised vs received; grant recognised vs received; prior cash interest multiple | 2.51 / 0.08; 6.69 / 4.56; 18.5x | same | L176-179, L197-198, L87, L202 | PASS |
| Capex reconciliation [INFERENCE] | PPE adds about 3.7 + CWIP 1.21 = 4.87 | PPE depreciation about 18.79 Cr (18.93 less ROU 0.15); adds about 3.69; plus CWIP 1.21 = 4.90 vs 4.87 | L119-121, L174, L195 | PASS |
| Step 6.5/7 EBIT and equity; derived utilisation | 5.19 / 44.35 / 234.04; 328.61; 45.5% | same | L143; PR L100, L133 | PASS |
| 8C EBITDA per MW; revenue per MW | 28.40 / 15.12 lakh; 0.81 / 1.59 Cr; -47% | same | PR L101, PR L123-124 | PASS |
| Q9 grant / H1 PBT | 12.35% | same | L176, L91 | PASS |
| LODR dates | 14-Feb-2027 / 30-May-2027 / 14-Aug-2027 | same | regulation | PASS |

### The one arithmetic FAIL (FACTUAL, loop A4)

A4 L181 says the tolling-to-owned shift "does not explain the YoY margin collapse" and "The YoY fall is mainly spread compression on goods, not a mix artifact." Flag 2 (A4 L466) says "Mix shift does not explain the YoY fall". The brief (A4 L488), the YAML flag (A4 L595) and the analyst note (A4 L607) repeat this.

Recomputation on A4's own convention: all materials attach to goods (A4 L123). The tolling-heavy Q1 FY27 supports that convention, because materials were 10.34% of a revenue base that was 79.56% services (A4 L177; L78-79, L83-84). On that basis tolling revenue carries close to zero material cost.
- Q2 FY26 gross profit 8,468.43 lakh = services 3,136.48 + goods 5,331.95 (goods spread 31.15%).
- Q2 FY27 gross profit 2,938.26 lakh = services 281.54 + goods 2,656.72 (goods spread 17.39%).
- Q2 FY26 spreads at the Q2 FY27 mix give a 32.39% gross margin. Mix effect = 41.81% to 32.39% = -9.42 pp (41% of the fall). Goods-spread effect = 32.39% to 18.89% = -13.51 pp (59%).
- In rupees: tolling gross profit fell 28.55 Cr, goods volume took 5.73 Cr and goods spread took 21.02 Cr, for a total of 55.30 Cr. Inside A4's -35.67 Cr margin effect (A4 L194), mix is -14.65 Cr and spread -21.02 Cr.

"Mainly spread compression" holds in margin terms (59%). "Does not explain" and "not a mix artifact" do not hold, because the loss of tolling is the largest single rupee item. Required fix: restate as "goods-spread compression explains about three-fifths of the YoY gross-margin fall and the loss of tolling mix about two-fifths." The transfer-pricing question (A4 Q3) and the 8C metric still stand, because spread compression stays the larger share.

---

## AUDIT 3: ADVERSARIAL READ

These are the three most positive claims in the A4 review. Each has its strongest bear counter, built from the same extracts.

### Claim 1. "No debt, 85.42 Cr net cash" as a strength and as value the swap ratio must credit
Where: A4 L516 ("Where it wins: no debt, 85.42 Cr net cash"), L490, L253, the Q1 bear answer (A4 L403: "a ratio ... that ignores the 85.42 Cr net cash") and the M1 forks (A4 L527).
Bear counter: Cash and bank of 85.42 Cr (L133-134) sit against other current liabilities of 89.94 Cr (L159). That line rose 81.99 Cr in H1 from 7.95 Cr, and net cash rose 79.66 Cr in the same six months. The cash flow books +86.99 Cr from other liabilities (L190). A4 gives two readings of the line (A4 L245), and both make it an obligation: a customer advance must be repaid in goods, and a parent advance must be repaid in cash or cancels on amalgamation. Net of the line, the position is about -4.52 Cr (8,541.82 - 8,993.74 lakh). "No debt" holds only on the face of the balance sheet, and nothing shows the cash is free. If the line is a Waaree advance, a ratio that ignores the cash can be fair, which reverses the forks at A4 L403 and L527.
Survives: YES (L133, L134, L159, L190). Already in A4: only in part (A4 L245 readings; A4 L490 says the cash came from "a jump in unexplained liabilities"). Not at A4 L516, L403 or L527.
Type: MISSING. Graft into A4: qualify A4 L516, L490, L403 and L527 with "85.42 Cr net cash sits against 89.94 Cr unexplained other current liabilities (up 81.99 Cr in H1); net of them about -4.52 Cr; free cash unproven until the line's counterparty is known (Q6)".

### Claim 2. "The filing is complete, ties out, and carries an unmodified review conclusion"; auditor "CLEAN"
Where: A4 L462, L68.
Bear counter: The three statements foot (1D) and the release ties. But the cash-flow receivable and payable lines miss the balance-sheet movements by 34.94 Cr and 37.25 Cr (L132, L155-156, L186-187), and no note explains the gap. The review gives moderate assurance only (L261-265) and does not mention the Note 4 scheme.
Survives: YES. Already in A4: YES (A4 L68 moderate assurance and silence on Note 4; A4 L243 and flag 4 cover the gaps; Q7). Only the words "ties out" at A4 L462 overstate.
Type: STYLE. Reword A4 L462 to "the statements foot and tie to the release; two cash-flow lines do not reconcile to the balance sheet (flag 4)". No graft of new substance.

### Claim 3. H1 cash generation: CFO 79.57 Cr (+11.63%), CFO/PAT 1.91x "headline strong", FCF 74.70 Cr (+24.40%)
Where: A4 L222-226.
Bear counter: Gross inflows of 158.42 Cr (receivables) and 86.99 Cr (other liabilities) funded a 200.89 Cr inventory build and a 72.45 Cr other-current-asset build (L183, L185, L186, L190). Without the two inflows, CFO would be about -165.84 Cr. Even the 64.09 Cr pre-WC operating cash profit (L180) is mostly Q1 tolling profit: Q1 PBT 47.47 Cr is 87.6% of H1 PBT 54.18 Cr (L91).
Survives: YES. Already in A4: YES (A4 L223 "non-repeatable drivers", L250-251, flag 3, and the Pillar 2 row "Do not band on the 1.91x headline").
Type: none needed. No graft.

### MANDATORY ACQUISITION-ECONOMICS PROBE: the Note 4 amalgamation
Deal: Note 4 (L222-224) amalgamates Indosolar into its parent, Waaree Energies. Indosolar "shall stand dissolved". The release calls it "an important strategic milestone" with "meaningful operational synergies" (PR L117-119). For Indosolar holders this is a buyout of the minority, paid in parent shares.

Multiple: consideration (exchange ratio) NOT FOUND in this run's extracts / target PAT = **NOT COMPUTABLE**. I cannot state a price-to-earnings multiple, and I cannot show the price is fair.

Target earnings bases from the extract:
- FY26 PAT 246.60 Cr (L97), an average of 61.65 Cr per quarter. At the 25.17% statutory tax rate it is 175.32 Cr, or 43.83 Cr per quarter.
- H1 FY27 PAT 41.64 Cr. Q1 FY27 supplies 36.62 Cr of it.
- Q2 FY27 PAT 5.02 Cr.
- The FY26 quarterly average is 12.3x Q2 FY27 (8.7x at statutory tax).

Quality markers:
- Borrowings: none (L145-160).
- Cash: 85.42 Cr, against 89.94 Cr of other current liabilities (Claim 1).
- FY26 operating EBIT 234.04 Cr on 287.01 Cr of Mar-26 equity (L143). This is a spot figure from a tolling-heavy year (H2 FY26 services 53.02%). It is for this probe only and is not a pillar input (Amendment 17 caution).
- Customer tenure: NOT FOUND.

Representative year: neither. FY26 carries a 71.28 Cr tax shield and a tolling-heavy H2. Q2 FY27 is the first near-pure owned quarter, at a 9.52% EBITDA margin.

Bear reading: The board approved the scheme on 23-Sep-2026 (L222). That date falls inside the quarter whose results show the trough. Indosolar's administration sits inside the transferee's group:
- the CS and secretarial emails use waaree.com (L56 unverified, L71);
- investor relations uses waaree.com (PR L145);
- the release letterhead reads "a WAAREE group company" (PR L72).

A4's own transfer-pricing reading (A4 L520, Q3) is that the parent may also price Indosolar's goods. If it does, the same group sets both the depressed earnings and the ratio. A ratio weighted to recent earnings would then move value from minority holders to Waaree.

Survives: YES (L97, L222, L56, L71; PR L72, PR L117-119, PR L125, PR L145). Already in A4: in part (ratio NOT FOUND; valuers at Q1; public vote at Q2; transfer pricing at Q3; M5 bear fork). Not in A4: the 12.3x earnings-base spread, the timing inside the trough quarter, and a question on which earnings year and method the valuers weighted.
Type: MISSING. Graft into A4: add the spread and the timing to Flag 1 (A4 L465) and to the Step 6.5/7 valuation-unit row (A4 L367). Extend Q1 (A4 L403) to ask "which earnings year and which methods did the valuers weight, and what weight went to market price?". Missing evidence: the 23-Sep-2026 Reg 30 scheme filing (ratio and valuation report). It is not in this run's documents, and A4 M1 already routes it to the operator before /fttcp.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**. No loop to A2 or A3 is needed.

| # | Type | Exact gap | Agent |
|---|---|---|---|
| F1 | FACTUAL | A4 L181, L466, L488, L595 and L607 state that the mix shift does not explain the YoY fall. On A4's own convention, mix explains 9.42 of the 22.92 pp gross-margin fall (41%) and goods spread 13.51 pp (59%). In Rs Cr, tolling gross profit -28.55, goods volume -5.73, goods spread -21.02 (L78-79, L83-84). Restate as about three-fifths spread, two-fifths mix. | A4 |
| M1 | MISSING | Net-cash qualifier absent at A4 L516, L490, L403, L527: 85.42 Cr cash (L133-134) against 89.94 Cr unexplained other current liabilities (L159), up 81.99 Cr in H1; net about -4.52 Cr. | A4 |
| M2 | MISSING | Acquisition-economics probe absent: consideration NOT FOUND, so price/PAT is not computable. Earnings base spans 12.3x (FY26 quarterly average 61.65 Cr vs Q2 FY27 5.02 Cr; 8.7x at statutory tax). Scheme approved 23-Sep-2026 (L222) inside the trough quarter by a board inside the transferee's group. Graft into Flag 1, the valuation-unit row and Q1. | A4 |

No CONTRADICTION findings. A4's protocol verdict (PROCEED WITH FLAGS) and cash-conversion class (INDETERMINATE-WITH-DIRECTION) are not under challenge. The three fixes change wording, flags and question text, not the verdict.

---

## STYLE NOTES (logged; no re-run)

- S1. Rounding slips at the last digit, against A4's own unrounded-lakh rule (A4 L42):
  - A4 L153 core PBT change -55.99 should be -56.00.
  - A4 L173 revenue QoQ +127.60% should be +127.59%.
  - A4 L178 H1 average revenue 111.98 should be 111.97.
  - A4 L178 shortfall 53.16% should be 53.17%.
- S2. A4 L462 "ties out": reword per Claim 2.
- S3. A4 L487 "tolling earned a 70.89% margin": 70.89% is the whole-company Q1 margin, and Q1 revenue was 79.56% services. Reword to "the tolling-heavy Q1 earned 70.89%".
- S4. A4 L490 "Most of that cash came from collecting last year's receivables and from a jump in unexplained liabilities": this is a gross-flow framing. Net, CFO is 64.09 Cr pre-WC cash profit (L180) plus a 16.02 Cr net WC release. Suggested wording: "The receivable release and the liability jump paid for the stock build; neither repeats."
- S5. A4 L26 "4 unnumbered footnote rows R360, R381-R383": these rows are numbered structured IDs inside R001-R383. Say "4 footnote-type rows".
- S6. A1 enumeration: www.sgco.co.in (L287) has no ENTITY row. The CEO sentence at PR L109-110 has no FORWARD row (A4 carries it at A4 L499). Non-material.
- S7. A2 count-test labels:
  - auditor_paras 7 includes R381 and R382, which are not auditor rows;
  - signatures 2 omits the audit-partner block (L274-282);
  - agenda_items 0, but the outcome letter lists one item (L40-44).
  No row is orphaned or missing.
- S8. A4 L500, L511 and L518 carry background claims (sector policy, insolvency history, peer names). These come from memory, not from any extract, and are tagged SECONDARY, PENDING LIVE VERIFICATION. Keep them out of any Notion payload until verified.
- S9. A4 L200 label "(6.71 Cr x -1.00 pp)": the ETR rose 1.00 pp. The -0.07 Cr effect is correct; the sign in the label is not.
- S10. Forward map rows M3, M4 and M5 are dated NOT FOUND. This is acceptable because no extract carries a date. Re-date them after the 23-Sep-2026 scheme filing is extracted.

---

```yaml
stage: A5-adversary
company: "INDOSOLAR"
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
    - "results L287 www.sgco.co.in (auditor website): no ENTITY row in A1 structured; STYLE, non-material, no loop"
    - "presentation PR L109-110 CEO industry-transformation sentence: no FORWARD row in A1 structured; carried in A4 L499; STYLE, non-material, no loop"
arithmetic_mismatches:
  - {metric: "Mix share of Q2 YoY gross-margin fall (A4 L181, L466, L488, L595, L607)", a4_value: "nil: 'Mix shift does not explain the YoY fall'", recomputed: "mix -9.42 pp of -22.92 pp (41%), goods spread -13.51 pp (59%); Rs Cr: tolling GP -28.55, goods volume -5.73, goods spread -21.02, total -55.30", source_line: "results L78, L79, L83, L84"}
surviving_bear_counters:
  - {claim: "No debt, 85.42 Cr net cash; 'where it wins'; ratio must credit the net cash (A4 L516, L490, L403, L527)", counter: "Cash 85.42 Cr sits against 89.94 Cr unexplained other current liabilities, up 81.99 Cr in H1 while net cash rose 79.66 Cr; both A4 readings make the line an obligation; net about -4.52 Cr; if a parent advance it cancels on amalgamation and is not minority value", source_line: "results L133, L134, L159, L190", type: MISSING}
  - {claim: "Amalgamation framed as strategic milestone with synergies (PR L117-119); acquisition-economics probe", counter: "Consideration NOT FOUND so price/PAT not computable; earnings base spans 12.3x (FY26 quarterly avg PAT 61.65 Cr vs Q2 FY27 5.02 Cr; 8.7x at statutory tax); scheme approved 23-Sep-2026 inside the trough quarter by a board inside the transferee's group (waaree.com addresses, group letterhead); a ratio weighted to recent earnings moves value from minorities", source_line: "results L97, L222, L56, L71; PR L72, PR L125, PR L145", type: MISSING}
  - {claim: "Filing complete, ties out, unmodified review (A4 L462, L68)", counter: "Statements foot, but cash-flow receivables and payables miss balance-sheet movements by 34.94 and 37.25 Cr with no note; review is moderate assurance and silent on Note 4; facts already in A4 L68, L243, flag 4; wording fix only", source_line: "results L132, L155-156, L186-187, L261-265", type: STYLE}
findings_by_type:
  factual:
    - "F1: A4 L181/L466/L488/L595/L607 claim mix shift does not explain the YoY fall; recomputed mix explains 9.42 of 22.92 pp gross-margin fall (41%), goods spread 13.51 pp (59%); tolling GP loss 28.55 Cr exceeds goods-spread loss 21.02 Cr (L78-79, L83-84). Loop A4."
  missing:
    - "M1: net-cash qualifier absent at A4 L516, L490, L403, L527; 85.42 Cr cash (L133-134) vs 89.94 Cr unexplained other current liabilities (L159), up 81.99 Cr; net about -4.52 Cr. Loop A4."
    - "M2: acquisition-economics probe absent; consideration NOT FOUND (price/PAT not computable); 12.3x earnings-base spread and 23-Sep-2026 approval inside the trough quarter by transferee-group board not stated; extend Flag 1, valuation-unit row (A4 L367), Q1 (A4 L403). Loop A4."
  contradiction: []
  style:
    - "S1: rounding slips vs unrounded-lakh rule: A4 L153 -55.99 (-56.00); L173 +127.60% (+127.59%); L178 111.98 (111.97); L178 53.16% (53.17%)"
    - "S2: A4 L462 'ties out' overstates; two cash-flow lines do not reconcile to the balance sheet (flag 4)"
    - "S3: A4 L487 '70.89%' is the whole-company Q1 margin, not a tolling margin"
    - "S4: A4 L490 gross-flow framing of H1 cash; net CFO is 64.09 Cr pre-WC profit plus 16.02 Cr WC release"
    - "S5: A4 L26 calls R360, R381-R383 'unnumbered'; they are numbered structured IDs"
    - "S6: A1 enumeration gaps www.sgco.co.in (L287) and PR L109-110 CEO sentence; non-material"
    - "S7: A2 count-test labels: auditor_paras includes R381-R382; signatures omits audit partner block L274-282; agenda_items 0 vs one outcome item L40-44; no row missing"
    - "S8: A4 L500, L511, L518 memory-sourced background (SECONDARY, PENDING LIVE VERIFICATION); keep out of Notion payload"
    - "S9: A4 L200 rate-effect label sign; ETR rose 1.00 pp; -0.07 Cr effect correct"
    - "S10: forward map M3, M4, M5 dated NOT FOUND; re-date after scheme filing extraction"
loop_back_to: "A4"
gap: "A4: (F1 FACTUAL) correct 'mix shift does not explain the YoY fall' at L181, L466, L488, L595, L607 to about three-fifths goods spread (13.51 pp) and two-fifths mix (9.42 pp) of the 22.92 pp gross-margin fall; (M1 MISSING) qualify the 85.42 Cr net cash at L516, L490, L403, L527 against 89.94 Cr unexplained other current liabilities (L159), net about -4.52 Cr; (M2 MISSING) add the acquisition-economics probe to Flag 1, the valuation-unit row and Q1: consideration NOT FOUND, 12.3x earnings-base spread (FY26 quarterly avg 61.65 Cr vs Q2 FY27 5.02 Cr), scheme approved 23-Sep-2026 inside the trough quarter by a board inside the transferee's group."
style_notes:
  - "S1 rounding slips at A4 L153, L173, L178 (two)"
  - "S2 reword A4 L462 'ties out'"
  - "S3 reword A4 L487 tolling margin"
  - "S4 reword A4 L490 cash attribution"
  - "S5 reword A4 L26 'unnumbered'"
  - "S6 A1 unenumerated units L287, PR L109-110"
  - "S7 A2 count-test category labels"
  - "S8 memory-sourced background claims stay out of Notion until verified"
  - "S9 A4 L200 rate-effect label sign"
  - "S10 re-date forward-map NOT FOUND rows after scheme extraction"
analyst_note: "Arithmetic re-derives clean from the lakh values. Only four last-digit rounding slips exist (STYLE). Three findings send the review back to A4. (1) FACTUAL: A4 says the mix shift does not explain the YoY fall. On A4's own convention (all materials to goods, which the tolling-heavy Q1 at 10.34% materials supports), mix explains 9.42 of the 22.92 pp gross-margin fall and goods spread 13.51 pp. In rupees, lost tolling gross profit (28.55 Cr) exceeds the goods-spread loss (21.02 Cr). 'Mainly spread' holds; 'not a mix artifact' fails. (2) MISSING: the 85.42 Cr net cash sits against 89.94 Cr of unexplained other current liabilities. That line rose 81.99 Cr while net cash rose 79.66 Cr; net of it, about -4.52 Cr. (3) MISSING: the scheme multiple is not computable (consideration NOT FOUND). A4 omits that the earnings base swings 12.3x (FY26 quarterly average vs Q2 FY27) and that a board inside the transferee's group approved the scheme in the trough quarter. Independent tie: the cash-flow other-liabilities line equals the change in current plus non-current other liabilities plus the 2.14 Cr deferred-grant drawdown, to the lakh."
```
