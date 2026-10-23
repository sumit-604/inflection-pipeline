# A5 ADVERSARY / COMPLETENESS AUDIT: Fairchem Organics Limited (FAIRCHEMOR), Q2 FY27

Agent: A5 adversary | model claude-opus-5-5 | run date 2026-10-23
Inputs read: A4 review (work/review_fairchemor_q2fy27.md); A1 fulltexts and structured files (results, presentation); A2 ledgers (results, presentation). The source PDFs and inputs/ were not opened.
Anchors: "res L###" = results fulltext line. "deck L###" = presentation fulltext line. "rev L###" = A4 review line. "R###" = A1 structured row of the named document. [DERIVED] = A5 arithmetic on anchored numbers. [INFERENCE] = reasoning, not filed fact.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT | sector PRESENT | business_model PRESENT | competition PRESENT | forward_map PRESENT. **Gate PASS.**

| Part | Heading in review | Content check | Status |
|---|---|---|---|
| 1 Summary narrative | "### 1. Summary narrative" (rev L447) | rev L448-L455: about 270 words and 22 sentences. It covers revenue, margin, PAT, the price-led driver, the trough base, the cash quality and the land RPT. Provenance tiers are marked. | present |
| 2 Sector | "### 2. Sector intelligence" (rev L457) | rev L458-L461: feedstock economics (1.25% / 0.25% by-product), duty cut, import parity, end markets | present |
| 3 Business model | "### 3. Business-model intelligence" (rev L463) | rev L464-L467: the spread, opex leverage, one plant, cash and debt pattern, model drift | present |
| 4 Competition | "### 4. Competition intelligence" (rev L469) | rev L470-L473: claimed strengths, weaknesses, peer set (PENDING LIVE VERIFICATION), competitive risk | present |
| 5 Forward map | "### 5. Forward map" (rev L475) | rev L476-L483: a make-or-break reading plus 7 dated catalysts. Each one has a bull fork and a bear fork. | present |

STYLE note only: the narrative is 8 source lines, under the "10-20 lines" format. It renders longer and the content is complete (S7).

---

## 1. COVERAGE AUDIT

Method: an independent grep and sweep over each A1 FULLTEXT. The fulltext is the spine. I diffed it against the A2 ledgers, then checked each ledger row against the A4 review.

### 1A. Results filing (res fulltext, 680 lines, 11 pages)

| Category | A2 count | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Notes | 9 | 9: Notes 1-7 (res L469, L474, L479, L513, L515, L521, L538), CF Note 1 (res L464), and the Note 6 continuation (res L528-L536) as its own row | none | PASS |
| Footnotes (unnumbered) | 8 | 8 | none | PASS |
| Line items | 353 | 353. P&L 151 = 26 labels x 6 columns, less 5 blank Other Equity columns. BS 76. CF 72. Segment 54. All subtotals re-added: BS CA 17,600.86 / 16,793.56; CL 8,862.94 / 10,326.16; total assets 39,843.09 / 39,097.93. CF OP-before-WC 3,660.10 and cash generated 2,983.97 tie. | none | PASS |
| ZERO_STANDING | 19 | 19: P&L 5 (res L245, L247), BS 3 (res L293, L348, L370), CF 5 (res L412, L440, L441, L448, L451), segment 6 (res L498-L502) | none | PASS |
| Agenda items | 2 | 2 (res L52, L67) | none | PASS |
| Auditor paragraphs | 3 | 4 numbered (res L159, L163, L171, L180) | none | PASS (difference explained). Para 1 is the scope paragraph. Its period content sits in R424 and R425, which are ledger sec 7 supporting rows. No EoM, Other Matter or Going Concern text exists. |
| Entities | 36 | 36 | none | PASS |
| Signatures | 3 | 3 (res L107, L191, L545) | none | PASS |
| Forward / Dates / Qualifiers | 4 / 32 / 37 | 4 / 32 / 37 | none | PASS |
| Row IDs | 484 | 484 | orphan_ids [] | PASS |

### 1B. Investor presentation (deck fulltext, 676 lines, 24 pages)

| Category | A2 count | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Slides | 24 | 24 ([page N] markers) | none | PASS |
| Slide numbers (NUMBER) | 321 | 321. By page: p1 2, p4 3, p5 2, p7 2, p8 4, p10 3, p11 1, p13 3, p15 16, p16 38, p17 37, p18 60, p19 87, p20 18, p21 3, p22 28, p23 14. | none | PASS (the numeric spine is complete) |
| Financial line items p16-p20 | 240 | 240 (38 + 37 + 60 + 87 + 18) | none | PASS |
| Entities | 60 | 60 | none | PASS |
| Forward | 13 | 13 + **2 policy units not captured** (deck L305; deck L313-L323) | none | **FAIL (A2)** |
| Qualifiers (claim scope) | 39 | 39 + **at least 9 claim units not captured** (deck L206-L213, L213-L220, L229-L235, L251-L258, L284, L293, L295) | none | **FAIL (A2)** |
| Dates | 24 | 24 | none | PASS |
| ZERO_STANDING | 14 | 14 (A1 11 + A2 3) | none | PASS |
| Row IDs | 457 | 457 | orphan_ids [] | PASS |

### 1C. Fresh-pass units missing from the structured file and the ledger (MISSING, route A2)

The A1 schema captures management claims and policy statements as QUALIFIER or FORWARD rows. Examples: R423 "Near-zero rejections", R424 "Leading manufacturer in India", R425 "internal accruals", R386 "Make-in-India" strategy. The units below are the same kind of unit, and none has a row. A grep of the deck structured file for "lowest cost", "short payment", "entire quantity", "barriers to entry", "overleverage", "adequately capitalized", "volatility" and "demand-supply" returns no match. The A2 presentation ledger states "MISSING_FROM_STRUCTURED: none" (ledger L19).

| # | Slide | Fulltext lines | Unit (verbatim, short) | Why it is material |
|---|---|---|---|---|
| U1 | p7 | deck L206-L213 | "One of the Lowest Cost Producer Globally"; "Strong moat of secure and low-cost raw material supply enabling Fairchem to be the lowest cost producer globally" | The deck's central moat claim. It is absent from the A4 Competition section (rev L470), which lists weaker claims. |
| U2 | p7 | deck L213-L220 | "Low cost of raw material as Fairchem purchases waste products from oil refineries"; "Efficient manufacturing process comparable to global peers"; "Large off-take capability enabling strong purchasing power with suppliers" | Cost-position claims. They are the bull basis for a converter rung. |
| U3 | p7 | deck L229-L235 | "Bulk procurement at prices superior to alternative disposal options for suppliers - refineries"; "Buys directly from refineries, on an 'as-is-where-is' basis at the factory gate on short payment cycles" | This is a structural explanation of the payable days of 7.8 to 11.0 that A4 calls "Very low supplier credit" (rev L223). |
| U4 | p8 | deck L251-L258 | "Capable of offering blends specific to customer requirements at short notice"; "Low switching cost of process lines"; "Built the capability to expand and contract production as required" | These are flexibility claims, relevant to the utilisation question (rev L365). |
| U5 | p10 | deck L284, L293 | "Enjoy Leadership Position in the industry due to barriers to entry"; "highly cost competitive vis a vis global peers" | Moat claims with no evidence, the same kind as R424. |
| U6 | p10 | deck L295 | "Position to market entire quantity of Prime Products it produces" | This gives a supply-constrained reading of the Q2 revenue fall of 5.2% QoQ, which A4 scores "leaning bear on revenue" (rev L172). It also ties to the duty cut, then raw-material availability, then utilisation (deck L410-L412). That is the second reading A4 does not state. |
| U7 | p10 | deck L305 | "Judicious strategy on capacity expansion by evaluating market demand-supply scenario and working very closely with its customer base" | A4 already relies on it, citing "deck L305" with no row ID (rev L366). This shows the structured file dropped a unit the review uses. |
| U8 | p11 | deck L313-L323 (Governance column) | "Always be adequately capitalized"; "Not overleverage the balance sheet"; "Secure sources of sustainable raw material supply"; "Invest in backward and forward integration"; "Transparent communications with all the stakeholders"; "Low volatility in the cash flow generation" | These are management policy commitments that can be tested against the deck's own numbers. CFO was (168) Mn in FY25 and 416 Mn in FY26 (deck R262 R263 L538). Net debt to equity went 0.02 to 0.20 to 0.32 (deck R292-R294). Cash on hand is Rs 0.57 L (res R182 L315). "Low volatility in cash flow" fails on the deck's own page 20. |

Gap for A2: register U1-U8 as MISSING_FROM_STRUCTURED. A1 adds the rows. A3 and A4 then review the new rows. U6 and U8 are the decision-relevant units.

### 1D. Ledger rows vs the A4 review (orphan test)

- A4 states contract item 1 explicitly (rev L16-L17): "results ledger 484 of 484 structured rows ... presentation ledger 457 of 457 ... No ledger row is unreviewed."
- A row-level spot check finds every note (Notes 1-7, CF Note 1, R478) cited in Step 0D. Every A2 flag class is answered: SIGNATURE_BEFORE_MEETING_END (rev L376, L431), RELATED_PARTY (rev L426), ZERO_STANDING (rev L10, L93), CHART_UNASSIGNED (rev L19), ORDER_INFERRED (rev L19), RESTATED (rev L119), LAYOUT_GARBLED R382/R419 (rev L408, L410).
- Slides S08, S09 and S17 carry no row-level cite. Neither do the data-free S02, S03, S12 and S14. The same holds for results FOOTNOTE_UNRESOLVED R462, R464 and R467 (unlabelled subtotals that tie by arithmetic; stray "Changes" label). The blanket attestation covers them. **Orphan rows: none.** A STYLE note asks for a row-level "reviewed, no finding" line (S5).

---

## 2. ARITHMETIC AUDIT

Every A4 derived figure was recomputed from the lakh values in the A1 structured file (res R-rows). Unit conversions were swept for all 26 P&L labels across 6 periods, and every cell is within 0.005 Cr. **Mismatches above rounding: 0.**

| Metric | A4 value | A5 recomputed (Rs Lakhs unless %) | Source line | Status |
|---|---|---|---|---|
| Op EBITDA Q2 FY27 / Q1 FY27 / Q2 FY26 | 17.54 / 17.87 / 4.19 Cr | 1,365.01+285.35+118.05-14.70 = 1,753.71 / 1,786.71 / 418.79 | res R081 R061 R049 R019 L237-L244 | PASS |
| Op EBITDA FY26 pre / post exc; H1 FY26; H1 FY27 | 21.62 / 20.73; 9.41; 35.40 | 2,161.69 / 2,073.42; 941.05; 3,540.42 | res R085 R092 R064 R052 R021; R087 R071 R054 R024; R084 R063 R051 R023 | PASS |
| Op EBITDA margin (7 cells) | 3.76 / 10.14 / 10.51 / 4.70 / 4.51 / 3.88 / 10.32% | 3.755 / 10.143 / 10.506 / 4.703 / 4.511 / 3.879 / 10.320% | revenue res R014 R012 R013 R015 R018 R017 | PASS |
| Reported EBITDA (6 cells) | 4.56 / 18.21 / 17.68 / 22.04 / 9.92 / 35.90 | 456.22 / 1,821.46 / 1,768.41 / 2,203.98 / 991.84 / 3,589.87 | res L237-L247 | PASS |
| Core PBT (ex-OI), 7 cells | 0.80 / 13.29 / 13.50 / 6.01 / 6.90 / 2.29 / 26.79 | 80.33 / 1,328.92 / 1,350.31 / 601.44 / 689.71 / 228.53 / 2,679.23 | res L244-L249, L227-L230 | PASS |
| OI / PBT | 31.8 / 2.5 / 1.1 / 17.8 / 18.2 / 1.8% | 31.78 / 2.55 / 1.08 / 17.84 / 18.18 / 1.81% | same | PASS |
| ETR | 34.4 / 26.6 / 25.5 / 24.3 / 30.3 / 26.0% | 34.43 / 26.57 / 25.51 / 24.31 / 30.34 / 26.04% | res R106 R110 R109 R108 R107 R111 L253-L254 | PASS |
| PAT margin | 0.69 / 5.69 / 6.09 / 1.21 / 0.80 / 5.88% | 0.692 / 5.685 / 6.091 / 1.205 / 0.802 / 5.883% | res R112-R117 L254-L255 | PASS |
| Gross margin | 20.32 / 22.65 / 23.07 / 20.13 / 19.33 / 22.85% | 20.323 / 22.651 / 23.069 / 20.131 / 19.328 / 22.855% | res R030-R042 L234-L235 | PASS |
| Opex ratio | 16.57 / 12.51 / 12.56 / 15.43 / 15.45 / 12.53% | 16.567 / 12.508 / 12.563 / 15.428 / 15.449 / 12.535% | res R043-R048, R055-R060, R065, R067-R072, R079 | PASS |
| YoY: revenue / op EBITDA / margin | +49.7% / +318.8% / +675 bps | +49.68% / +318.76% / +675.1 bps | res R013 R014 | PASS |
| Margin split GM / opex | ~275 / ~401 bps | 274.6 / 400.4 bps | derived | PASS (1 bp rounding; S2) |
| YoY: D&A / FC / OI | +2.8% / +93.7% / -60.7% | +2.83% / +93.65% / -60.73% | res R061 R066; R049 R053; R019 R020 | PASS |
| EBIT (op) Q2 FY26 / Q2 FY27; YoY | 1.41 / 14.68; +939% | 141.29 / 1,468.36; +939.2% | derived | PASS |
| YoY: core PBT / PBT / PAT / EPS | +1,581% / +1,059% / +1,217% / +1,268% | +1,580.9% / +1,059.1% / +1,216.7% / +1,267.8% | res R081 R083; R088 R090; R115 R112; R148 R151 | PASS |
| Opex growth 18.48 to 20.97 Cr | +13.5% | 1,847.64 to 2,097.06 = +13.50% | derived | PASS |
| ETR normalisation worth | +1.22 Cr | (0.344260 - 0.255126) x 1,365.01 = 121.67 | res R106 R090 R109 R088 | PASS |
| FC QoQ / interest cover | -35.8% / 12.4x | -35.77% / 1,468.36 / 118.05 = 12.44x | res R049 R050 | PASS |
| Share-count effect on EPS | ~3.4% | 1,302.09 / 1,259.59 = 1.0337 | res R144 R142 L262-L263 | PASS |
| Q1 FY26 derived: revenue / margin / core PBT | 131.06 / 3.98% / 1.48 | 13,106.31 / 3.985% / 148.20 | res R018-R014; R087-R083 | PASS |
| Q2 FY26 QoQ | -14.9% | -14.91% | derived | PASS |
| H2 FY26 block: revenue / margin / core PBT / current tax | 217.06 / 5.62% / 4.61 and 3.73 / (0.15) | 21,706.24 / 5.624% / 461.18 and 372.91 / -14.57 | res R015-R018; R099-R098 | PASS |
| Q1 FY27 vs H2 FY26 average quarter | +62% | 176.15 / 108.53 = +62.3% | derived | PASS |
| Q2 FY27 QoQ: revenue / core PBT / margin | -5.2% / +1.6% / +36 bps | -5.24% / +1.61% / +36.3 bps | res R013 R012 | PASS |
| H1 FY27 average revenue; Q2 vs average | 171.53; -2.7% | 17,153.48; -2.69% | res R017 | PASS |
| PAT bridge: rev contribution / GM change / opex / op EBITDA chg | +11.26 / +4.58 / -2.49 / +13.35 | 1,125.89 / 458.44 / -249.42 / 1,334.92 | derived | PASS |
| PAT bridge: D&A / FC / OI / PBT chg / tax at prior ETR / ETR chg / PAT chg | -0.08 / -0.57 / -0.23 / +12.47 / -4.29 / +1.22 / +9.40 | -7.85 / -57.09 / -22.73 / 1,247.25 / -429.38 / +121.67 / 939.54 | res R115 R112 | PASS (ties to the lakh) |
| After-tax attribution | 8.33 (88.6%) / -0.15 (-1.6%) / +1.22 (12.9%) | 832.78 (88.64%) / -14.91 (-1.59%) / 121.67 (12.95%) | derived | PASS (12.95 rounds either way) |
| OI reversion effect | +0.17 Cr | 22.73 x (1 - 0.2551) = 16.93 | derived | PASS |
| CFO YoY | -21.5% | 2,405.23 / 3,065.82 = -21.55% | res R282 R279 L431-L435 | PASS |
| CFO / PAT H1 FY26 / H1 FY27 / ex-inventory | 15.76x / 1.19x / 0.09x | 15.756 / 1.192 / (2,405.23 - 2,230.80) / 2,018.14 = 0.086 | res R279 R113 R282 R117 R254 | PASS |
| Capex YoY | -58.2% | 452.37 / 1,082.18 = -58.20% | res R283 R284 L437 | PASS |
| FCF H1 FY26 / H1 FY27 / change | 19.84 / 19.53 / -1.6% | 1,983.64 / 1,952.86 / -1.55% | derived | PASS |
| WC change H1 FY26 / H1 FY27 / swing | +23.33 / -6.76 / -30.09 | 2,333.35 / -676.13 / -3,009.48 | res R276 R253 R280 R252 | PASS |
| Receivable days 31-Mar-26 / 30-Sep-26 | 54.1 / 53.4 | 6,812.73 / 45,964.82 x 365 = 54.10; 10,017.55 / 34,306.95 x 183 = 53.44 | res R181 R180 L314 | PASS |
| Inventory days | 91.7 / 48.4 | 9,225.01 / 36,711.64 x 365 = 91.72; 6,994.21 / 26,466.25 x 183 = 48.36 | res R179 R178 L312 | PASS |
| Payable days | 11.0 / 7.8 | 1,105.88 / 36,711.64 x 365 = 11.00; 1,127.52 / 26,466.25 x 183 = 7.80 | res R215-R218 L362-L364 | PASS |
| CCC | 134.8 / 94.0 days | 134.82 / 94.00 | derived | PASS |
| PPE change / CWIP change | +8.57 / -10.09 | 856.72 / -1,008.64 | res R163 R164 R166 R167 | PASS |
| Net debt 31-Mar / 30-Sep / change | 82.56 / 67.23 / -15.33 | 8,378.23 - 1.35 - 121.26 = 8,255.62; 6,865.32 - 0.57 - 141.87 = 6,722.88; -1,532.74 | res R214 R183 R185; R213 R182 R184 | PASS |
| Net debt / equity | 0.31 / 0.24 | 0.3139 / 0.2385 | res R205 R204 | PASS |
| Equity roll (A3 F11) | ties | 26,304.03 + TCI 2,004.61 - dividend declared 125.96 (Rs 1 x 125.959 L shares; 125.31 paid + 0.65 to the restricted account) = 28,182.68 | res R205 R139 R296 R298 R204 | PASS (exact) |
| Receivables growth | +47% | 10,017.55 / 6,812.73 = +47.04% | res R180 R181 | PASS |
| A21 bases: PAT annualised Q2 / H1; TTM PAT; TTM EPS; divergence | 40.67 / 40.36; 23.78; 18.81; ~70% | 4,067.04 / 4,036.28; 2,018.14 + 359.47 = 2,377.61; 18.81; +70.3% | res R115 R117 R114 R113; R152 R150 R153 | PASS |
| PE H1-annualised / TTM; buyback premium to CMP | 21.1x / 35.9x; 18.5% | 675 / 32.04 = 21.07; 675 / 18.81 = 35.89; 800 / 675 = +18.52% | deck R309 L636; res R368 L524 | PASS |
| ROCE H1 FY27 annualised (pre-tax) | ~17.2% | (2,728.68 + 301.84) x 2 / (28,182.68 + 6,865.32 + 158.17) = 17.22% | res R091 R051 R204 R213 R206 | PASS (EBIT basis = PBT + FC, includes OI; S3) |
| ROCE FY26 pre-exc / FY25 | ~3.4% / ~9.2% | 1,189.93 / 34,682.26 = 3.43%; deck (299 + 37) / (3,020 + 630) = 9.21% | res R085 R052 R205 R214; deck R141 R137 R221 R237 | PASS |
| Land RPT ratios | 2.7x H1 capex; Rs 19,427 / sq m; 59.5% of H1 PAT | 1,201 / 452.37 = 2.65x; 12,01,00,000 / 6,182 = 19,427; 1,201 / 2,018.14 = 59.51% | res R373 L588, R375 L601, R283, R117 | PASS |
| Segment liabilities / assets change H2 FY26 | +33.60 / +2.59 | 3,359.74 / 259.42 | res R362 R359 R356 R353 L507-L510 | PASS |
| NC provisions change; FY26 current tax / PBT | +43%; 0.9% | +43.47%; 0.89% | res R207 R208; R099 R092 | PASS |
| Deck cross-checks | EBITDA 175 Mn = 17.54 Cr; total expenses 1,494 = 1,669 - 175 | ties | deck R043 R040 R037 L431-L433 | PASS |

---

## 3. ADVERSARIAL READ

The three most positive claims in the A4 review are below. Each has the strongest bear counter built from the same extracts.

### Claim 1: "Real operating gain, not treasury" (rev L136, L144, L439, L449)
A4: core PBT rose from 0.80 to 13.50 Cr. Margin rose 675 bps. "The gain is real at the operating level."

- **Counter 1a (import-parity spread).** Management credits realization to "higher raw material cost and higher import finished product cost" and to "lower imports" (deck R430 L401-L403, R431 L405-L406). The margin only returns to about the FY24 peak (deck R124 L477). *Survives. It is already in A4* (rev L149, L201, L427, Q6). No graft needed.
- **Counter 1b (inventory cost lag inside the H1 gross margin).** The FG/WIP inventory change charged to the P&L was +18.86 Cr in H1 FY27 (res R040 L235). Of that, Q1 FY27 was +15.98 Cr (R038). Total inventories fell from 92.25 to 69.94 Cr (res R179 R178 L312). That stock was built in H2 FY26: the FY26 change was (7.08) Cr and the H1 FY26 change was +6.26 Cr, so H2 FY26 built 13.33 Cr [DERIVED: (707.55) - 625.64 = (1,333.19) L]. Management says raw-material cost rose (deck L402-L403). Stock built in the low-margin H2 FY26 and sold into a rising-price half books a holding gain under weighted-average costing [INFERENCE]. Its size cannot be computed from the extracts. *Partial rebuttal from the same extracts:* Q2 FY27 drew down only 2.88 Cr (R037), yet its gross margin rose to 23.07% from 22.65% in Q1. So the Q2 print does not lean on the drawdown, but the H1 figure (22.85%) may. **Survives in narrowed form, so it must be grafted.** A4's thresholds use H1 gross margin as a base (rev L291, L353: bull at or above 22.7%, "H1 FY27 22.85%"). The Step 4 "Mixed" label on the margin-change row (rev L186) and Step 8C need one qualifier: H1 gross margin may carry a cost-lag component, mostly in Q1, so Q3 is the first quarter with no inventory cushion (inventory is at its lowest of three dates, deck R197-R199). Type MISSING, route A4.

### Claim 2: "Receivables build is growth-induced" (rev L221, L234)
A4: receivable days stayed flat near 54 on period revenue.

- **Counter.** The deck's own CCC rises from 99 to 128 days (deck R298 R299 L600), and the CFO rests on an inventory release. *Already in A4* (rev L224, L234, L428).
- **Second-basis test** (quarter-end balance against the latest-quarter revenue). At 30-Sep-2026: 10,017.55 / 16,692.38 x 92 = 55.2 days. At 31-Mar-2026, on the H2 FY26 half: 6,812.73 / 21,706.24 x 182 = 57.1 days [DERIVED; res R180 R181 R013 R015 R018]. Days are flat to lower on both bases. **The counter does not survive** beyond what A4 already carries. A4's claim holds. No graft.

### Claim 3: "FCF 19.53 Cr funded the 15.13 Cr debt repayment; net debt fell 15.33 Cr; ND/E 0.31 to 0.24" (rev L219, L227, L236)

- **Counter (the deleveraging was funded by inventory liquidation).** CFO excluding the inventory release is 2,405.23 - 2,230.80 = 174.43 L. Less capex of 452.37 L, that gives **H1 FCF of -2.78 Cr** [DERIVED; res R282 L435, R254 L418, R283 L437]. Without the 22.31 Cr release, H1 operations repaid no debt. Dividend (1.25 Cr, R296), lease (0.26 Cr, R295) and interest (3.02 Cr, R299) would then have added to borrowings. The land RPT of Rs 12.01 Cr plus stamp duty at actuals (res R414 L588) would undo **78%** of the H1 net-debt fall (1,201 / 1,532.74) [DERIVED]. ND/E of 0.24 is still 12x the FY24 level of 0.02 (deck R292, chart position inferred). The deck's own policy is "Not overleverage the balance sheet" (deck L315, unit U8). A4 has the pieces (rev L217, L233, L236) but frames the FCF row as "Funded 15.13 Cr debt repayment" with no qualifier. **Survives, so it must be grafted** into the Step 5 FCF row verdict and the net-debt answer. Type MISSING, route A4.

### Mandatory acquisition-economics probe

**(a) Land RPT (res L67-L70, L582-L623).** The company buys 2 parcels (6,182 sq m, adjoining the plant) from the CMD and relatives for Rs 12.01 Cr, excluding stamp duty and registration (res R373 R375 R480).
- Price / target PAT: **not computable.** Land has no earnings, and no valuation basis is filed. Per sq m the price is Rs 19,427 before stamp duty.
- Against the buyer: 59.5% of H1 FY27 PAT. 4.3% of total equity (1,201 / 28,182.68). 17.9% of 30-Sep net debt (1,201 / 6,722.88). 2.7x H1 capex. 1.4% of market cap (12.01 / 850.28 Cr, deck R312).
- Quality markers: counterparty holding 6.07% (res R374 L593); arm's length self-asserted (res R483 L621); no project named in either document; cash on hand Rs 0.57 L.
- The extracts cannot show the price is fair. The bear reading (price basis undisclosed, no stated use) is **already in A4**: Flag 1 (rev L426), Q3 and Q4 (rev L366-L367), M2-M4 (rev L403-L405), and the brief (rev L454, L478-L479). No further graft.

**(b) Share buyback (Note 6, res L521-L536; framed by the deck as a win under "Capital Efficiency", deck L302-L304, R016).** 4,25,000 shares at Rs 800 = Rs 34.00 Cr.
- Price / earnings: **47.4x FY25 EPS** (16.88, deck R169 L500; the last full year before the 20-Nov-2025 resolution). **186.9x FY26 EPS** (4.28, res R150). 25.0x even on today's H1-annualised EPS of 32.04.
- Against today's market: 18.5% above CMP of Rs 675 (deck R309). That is a mark-to-market loss of Rs 5.31 Cr (4,25,000 x 125) [DERIVED].
- Quality markers when executed: EBITDA margin falling 10.78% to 7.96% to 4.70% (deck R124-R126). Borrowings rising from 63.0 to 83.7 Cr (deck R237 R238). The FY25 dividend of 9.77 Cr was paid in the same year (res R297).
- **The bear reading survives.** The company levered up to buy back stock at about 47x prior-year EPS, at a price above today's market. A4 carries the debt funding (Flag 4, rev L429) and the 18.5% premium (rev L317). It does not state the earnings multiple or challenge the deck's "Capital Efficiency" framing. **Graft one line into Flag 4.** Type MISSING, route A4.

### Checks that produced no finding
- Single plant (rev L67, L466): the deck says "Business Continuity Plan for all plants" (deck L363-L364). Every other extract line shows one works address (res L20, L214) and one facility (deck L216, L221, L338). A4's reading is the conservative reading of the filed evidence. No finding.
- Signature timing (rev L376, L431): the timestamps are verified (res R446 L552 15:41:45; R426 L196 15:59:19; meeting 15:30-16:15, res L46-L47). A4 frames it as a question and does not assert a lapse. No finding.
- Deck omission of the land RPT (rev L426): verified. "land", "related party" and "RPT" do not appear in the deck fulltext.
- Tax-asset provision as a pre-tax charge (rev L55): it is consistent with its position among the PBT adjustments (res R246 L412), and its [INFERENCE] tag is correct.

---

## FINDINGS (tagged)

| ID | Type | Route | Gap | Anchor |
|---|---|---|---|---|
| M1 | MISSING | A2 | Deck claim and policy units U1-U8 on slides 7, 8, 10 and 11 are absent from the A1 structured file and the A2 ledger. The ledger reports MISSING_FROM_STRUCTURED: none. A4 already cites one of them by line with no row (deck L305). | deck L206-L235, L251-L258, L284, L293, L295, L305, L313-L323; ledger L19 |
| M2 | MISSING | A4 | Surviving counter to Claim 1: the H1 FY27 gross margin may include an inventory cost-lag gain (FG/WIP drawdown of 18.86 Cr, of which Q1 15.98 Cr, from stock built in H2 FY26 while raw-material cost rose). Q2 (2.88 Cr drawdown, higher GM) narrows it. Graft into the Step 4 margin-change row and Step 8C. | res R040 R038 R037 L235; R042 R041; deck R430 L401-L403 |
| M3 | MISSING | A4 | Surviving counter to Claim 3: H1 FCF excluding the inventory release is -2.78 Cr, so the deleveraging was inventory-funded. The land RPT would undo 78% of the H1 net-debt fall. Graft into the Step 5 FCF row and the net-debt answer. | res R282 R254 R283 L418-L437; R414 L588 |
| M4 | MISSING | A4 | Acquisition-economics probe (buyback): Rs 800 = 47.4x FY25 EPS and 186.9x FY26 EPS, 18.5% above CMP (MTM -Rs 5.31 Cr), debt rising. The deck frames it as "Capital Efficiency". Graft into Flag 4. | res R368 L524; deck R169 R170 L500, R309 L636, R237 R238 L521, L302-L304 |

FACTUAL: none. CONTRADICTION: none. Arithmetic mismatches above rounding: none.

---

## VERDICT

**INCOMPLETE.** Failing agent: **A2**, the first in the chain, followed by **A4** grafts. Finding type: MISSING (4). No FACTUAL or CONTRADICTION finding.
- A2 gap (M1): register the deck units U1-U8 (deck L206-L213, L213-L220, L229-L235, L251-L258, L284, L293, L295, L305, L313-L323) as MISSING_FROM_STRUCTURED, so that A1 adds the rows and A3/A4 review them. Decision-relevant: U8 (the governance policy fails against deck p20 CFO and p22 ND/E) and U6 (a supply-constrained second reading of the Q2 revenue dip).
- A4 grafts on the same pass (M2, M3, M4): the inventory cost-lag qualifier, the inventory-funded deleveraging qualifier, and the buyback earnings multiple.
- Everything else passes. That covers the plain-language brief gate, the results coverage, the numeric spine of both documents, every derived metric, the PAT bridge, the equity roll, and the receivables claim.

---

## STYLE NOTES (logged; no re-run)

- S1. Brief section 3 (rev L465) calls "staff, power, other" "fixed costs". Power and fuel is variable or semi-variable. Step 2 correctly says "opex". Change the label. No number changes.
- S2. The opex leverage is "about 401 bps" (rev L131, L143). On unrounded ratios it is 400 bps (16.567% - 12.563%), and 275 + 400 = 675. Cosmetic.
- S3. Step 7 EBIT of 30.31 Cr (rev L325) is PBT + FC and includes OI. Step 2 defines "EBIT (operating) = Op EBITDA - D" (rev L134). State the basis. On operating EBIT, the H1 ROCE is 16.9%, not 17.2%. The figure is a deferred, flag-only fact.
- S4. Anchor carry-overs from A1. Res R448 points to L17, but the text is at res L62-L63. Res R436 points to L466, but the text is at res L529. Cosmetic.
- S5. The ledger coverage attestation is blanket (rev L16-L17). Add one row-level line, "reviewed, no finding", for slides S08, S09 and S17 and for results R462, R464 and R467, so the next audit can verify it row by row.
- S6. Brief section 4, "100+ suppliers within about 500 km" (rev L470), merges two deck statements: 100+ suppliers (deck L227) and the vast majority procured or sold within 500 km (deck L228-L232).
- S7. The brief narrative is 8 source lines (about 270 words) against the "10-20 lines" format. It renders longer and the content is complete.

---

```yaml
stage: A5-adversary
company: "FAIRCHEMOR"
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
    - "deck p7 L206-L213: 'One of the Lowest Cost Producer Globally' / 'strong moat of secure and low-cost raw material supply'"
    - "deck p7 L213-L220: low-cost raw material from refinery waste; process comparable to global peers; large off-take purchasing power"
    - "deck p7 L229-L235: bulk procurement at prices superior to suppliers' disposal options; buys at factory gate on short payment cycles"
    - "deck p8 L251-L258: blends at short notice; low switching cost of process lines; expand and contract production as required"
    - "deck p10 L284, L293: leadership position due to barriers to entry; highly cost competitive vs global peers"
    - "deck p10 L295: position to market entire quantity of Prime Products it produces"
    - "deck p10 L305: capacity expansion by evaluating market demand-supply scenario (A4 cites by line, no row ID)"
    - "deck p11 L313-L323: governance policy - adequately capitalized; not overleverage; secure raw material; backward/forward integration; transparent communications; low volatility in cash flow generation"
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "Real operating gain, not treasury (rev L136, L449)", counter: "H1 FY27 gross margin may include inventory cost-lag gain: FG/WIP drawdown 18.86 Cr (Q1 15.98 Cr) of stock built in H2 FY26 (13.33 Cr) while mgmt says RM cost rose; Q2 drawdown 2.88 Cr with higher GM narrows it to H1/Q1; Q3 is first quarter with no inventory cushion", source_line: "res R040 R038 R037 L235; R042 R041 L235; R179 R178 L312; deck R430 L401-L403", type: MISSING}
  - {claim: "FCF 19.53 Cr funded 15.13 Cr debt repayment; net debt -15.33 Cr (rev L219, L227, L236)", counter: "FCF ex-inventory release = 174.43 L - 452.37 L = -2.78 Cr; deleveraging was inventory-funded; land RPT 12.01 Cr would undo 78% of H1 net-debt fall", source_line: "res R282 L435; R254 L418; R283 L437; R414 L588", type: MISSING}
  - {claim: "Deck 'Capital Efficiency': buyback INR 340 Mn (deck L302-L304, R016); A4 Flag 4 partial", counter: "Buyback at Rs 800 = 47.4x FY25 EPS 16.88 and 186.9x FY26 EPS 4.28; 18.5% above CMP 675 (MTM -Rs 5.31 Cr); borrowings rose 63.0 to 83.7 Cr in the same year", source_line: "res R368 L524; deck R169 R170 L500; deck R309 L636; deck R237 R238 L521", type: MISSING}
findings_by_type:
  factual: []
  missing:
    - {id: M1, route: A2, gap: "Deck claim/policy units U1-U8 (slides 7, 8, 10, 11) absent from A1 structured file and A2 ledger; ledger says MISSING_FROM_STRUCTURED none", source_line: "deck L206-L235, L251-L258, L284, L293, L295, L305, L313-L323"}
    - {id: M2, route: A4, gap: "Inventory cost-lag qualifier missing from Step 4 margin-change row and Step 8C", source_line: "res R040 R038 R037 L235; deck R430 L401-L403"}
    - {id: M3, route: A4, gap: "Step 5 FCF row lacks ex-inventory-release FCF (-2.78 Cr) and land-RPT reversal of 78% of H1 net-debt fall", source_line: "res R282 R254 R283 L418-L437; R414 L588"}
    - {id: M4, route: A4, gap: "Acquisition-economics probe on buyback: earnings multiple (47.4x FY25, 186.9x FY26 EPS) and challenge to deck 'Capital Efficiency' framing not stated; graft into Flag 4", source_line: "res R368 L524; deck R169 R170 L500; deck L302-L304"}
  contradiction: []
  style:
    - "S1 Brief sec 3 labels power and other expenses 'fixed costs' (rev L465); use 'opex'"
    - "S2 Opex leverage 401 bps vs 400 bps unrounded (rev L131, L143)"
    - "S3 Step 7 EBIT basis (PBT+FC, incl. OI) differs from Step 2 operating EBIT; label it (16.9% on operating EBIT)"
    - "S4 A1 anchor carry-overs: res R448 at L17 (true L62-L63); R436 at L466 (true L529)"
    - "S5 Add row-level 'reviewed, no finding' for slides S08 S09 S17 and res R462 R464 R467"
    - "S6 Brief sec 4 merges '100+ suppliers' and '500 km' statements (deck L227, L228-L232)"
    - "S7 Narrative 8 source lines vs 10-20 line format; content complete"
loop_back_to: "A2"
gap: "MISSING (A2): register deck units U1-U8 (deck L206-L213, L213-L220, L229-L235, L251-L258, L284, L293, L295, L305, L313-L323) as MISSING_FROM_STRUCTURED so A1 adds rows and A3/A4 review them; then MISSING (A4) grafts: M2 inventory cost-lag qualifier (Step 4, Step 8C), M3 ex-release FCF -2.78 Cr and land RPT undoing 78% of H1 net-debt fall (Step 5), M4 buyback at 47.4x FY25 / 186.9x FY26 EPS, 18.5% above CMP (Flag 4)."
style_notes:
  - "S1 'fixed costs' label (rev L465)"
  - "S2 401 vs 400 bps (rev L131, L143)"
  - "S3 Step 7 EBIT basis label (rev L325)"
  - "S4 A1 anchor carry-overs R448, R436"
  - "S5 row-level reviewed-no-finding lines"
  - "S6 supplier/500 km merge (rev L470)"
  - "S7 narrative line count"
analyst_note: "Numbers are clean. Every A4 derived metric recomputes within rounding at lakh level, the PAT bridge ties to the lakh, and the equity roll ties exactly once the dividend is taken as declared (125.96 L; 0.65 L moved to the restricted account). The numeric spine of both extracts is complete. The gap is qualitative: A1 dropped management claim and policy bullets on deck slides 7, 8, 10 and 11, and the A2 sweep missed them; A4 even cites deck L305 by line with no row. Two of those units cut opposite ways. The slide 11 policy ('not overleverage', 'low volatility in cash flow') fails against the deck's own CFO swing and debt rise. Slide 10 'market entire quantity' offers a supply-constrained second reading of the Q2 revenue dip that A4 scored as leaning bear. Three bear counters survive and need one-line grafts: inventory cost lag in H1 gross margin, inventory-funded deleveraging, and the buyback earnings multiple. The receivables-growth claim holds on a second test basis. The loop is narrow: about eight units to enumerate, review, and three grafts."
```

---
---

## ITERATION 1 RE-AUDIT (loop iteration 1 of 1)

Run date 2026-10-23. Fresh re-read of the revised inputs:
- A4 review, loop iteration 1 (rev line numbers below refer to the revised file).
- Presentation structured file, now R001-R512.
- Presentation ledger, 512 of 512 rows plus the loop 1 addendum.
- Results structured file and ledger: unchanged (R001-R484, 484 of 484).

The iteration 0 section above is kept intact. Its rev line numbers refer to the pre-loop review.

### I1-0. Deliverable-completeness gate

All five parts are PRESENT with real content.
- The narrative is now 11 source lines (rev L469-L479), which clears S7.
- Sector: rev L482-L486.
- Business model: rev L489-L494.
- Competition: rev L497-L500.
- Forward map: rev L503-L510, a make-or-break reading plus 7 dated catalysts, each with a bull fork and a bear fork.

**Gate PASS.**

### I1-1. Coverage audit

| Category | A2 count (loop 1) | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Deck QUALIFIER | 87 | 87 = 39 + 48 appended (R458-R495, R497-R499, R506-R512) | none | PASS |
| Deck FORWARD | 20 | 20 = 13 + 7 appended (R496, R500-R505) | none | PASS |
| Deck NUMBER / ENTITY / DATE / slides | 321 / 60 / 24 / 24 | unchanged | none | PASS |
| Deck row IDs | 512 | 512 | orphan_ids [] | PASS |
| Results, all categories | 484 (unchanged) | 484 | orphan_ids [] | PASS |

**Iteration 0 units mapped to the new rows:**
- U1 maps to R462 and R466.
- U2 maps to R467, R468 and R469 (plus R470).
- U3 maps to R473 and R474.
- U4 maps to R477, R478 and R479.
- U5 maps to R483 and R488.
- U6 maps to R490.
- U7 maps to R496.
- U8 maps to R500-R505.

**M1 CLOSED.**

**Orphan test against A4:**
- A4 attests 512 of 512 (rev L19) and adds row-level "reviewed, no finding" lines (rev L22).
- New rows are cited in Steps 3, 5, 7 and 8.5, Section M, the flags and the brief. The cited rows are R460, R461, R462, R474, R478, R483, R486, R487, R489, R490, R492, R494, R495, R496 and R500-R505.
- The uncited addendum rows are RESTATED, DUPLICATE_WORDING or context rows. The attestation covers them, and the S08 row-level line covers R475-R480.
- **Orphan rows: none.**

**Residual fresh-pass unit:**
- Deck p4 L85-L93, "Long lasting Pan India Raw Material sourcing capabilities with diversified vegetable oil refineries", has no row.
- R471, R472 and R487 already carry the same theme, and the unit adds no new testable content. Logged as STYLE (S16). No loop.

### I1-2. Arithmetic audit (new or changed figures in the revised review)

| Metric | A4 value | A5 recomputed (Rs Lakhs unless %) | Source line | Status |
|---|---|---|---|---|
| H1 FY27 finance cost YoY (rev L149) | +86.9% | 301.84 / 161.48 = +86.92% | res R051 R054 | PASS |
| Implied borrowing cost H1 FY27 / FY26 (rev L149) | ~7.9% / ~5.0% | 603.68 / avg(8,378.23, 6,865.32) = 7.92%; 369.66 / avg(6,300, 8,378.23) = 5.04% | res R051 R052 R213 R214; deck R237 | PASS |
| FY26 borrowings / EBITDA (rev L244) | ~3.9x | 8,378.23 / 2,161.69 = 3.88x | res R214; derived | PASS |
| Deck CFO / PAT FY25 / FY26 / H1 FY27 (rev L244) | -0.8x / 6.7x / 1.2x | -168 / 220 = -0.76; 416 / 62 = 6.71; 240 / 202 = 1.19 | deck R262-R264, R149-R151 | PASS. FY26 uses pre-exceptional PAT; on reported PAT (5.54 Cr) it is 7.5x (S10) |
| H2 FY26 FG/WIP build (rev L168, L195) | 13.33 Cr | (707.55) - 625.64 = (1,333.19) | res R042 R041 | PASS |
| Ex-release FCF (rev L228) | -2.78 Cr | 174.43 - 452.37 = -277.94 | res R282 R254 R283 | PASS |
| Counterfactual borrowing add (rev L228) | ~7.31 Cr | named items 2.78 + 1.25 + 0.26 + 3.02 = 7.31 exactly. The full counterfactual, including other investing flows (+12.70), the restricted account (-0.65) and the cash draw (+0.78), is 717.87 L = 7.18 Cr. | res R285-R289, R298, R303 | PASS on the stated formula (S8) |
| Land RPT vs H1 net-debt fall (rev L236, L246) | 78% | 1,201 / 1,532.74 = 78.4% | res R373; derived | PASS |
| ND/E vs FY24 (rev L236) | 12x | 0.24 / 0.02 | deck R292 R295 | PASS |
| Buyback multiples (rev L450) | 47.4x / 186.9x / 25.0x | 800 / 16.88 = 47.39; 800 / 4.28 = 186.92; 800 / 32.04 = 24.97 | res R368; deck R169; res R150 R152 | PASS |
| Buyback mark-to-market (rev L450) | ~5.31 Cr | 4,25,000 x 125 = 5,31,25,000 | res R365; deck R309 | PASS |
| Second-basis receivable days (rev L230) | 57.1 / 55.2 | 57.12 / 55.21 | res R181 R180 R015 R018 R013 | PASS |
| ROCE on operating EBIT (rev L292, L335) | 16.9% | 2,981.07 x 2 / 35,206.17 = 16.93% | res R084 R063 R051 R023; R204 R213 R206 | PASS |
| Opex leverage (rev L134, L146) | 400 bps | 400.4 bps | derived | PASS |

**Mismatches above rounding: 0.**

### I1-3. Adversarial read (re-identified after loop 1)

The deleveraging claim is no longer a positive claim, because A4 now calls it inventory-funded. The three most positive claims in the revised review are below.

**C1. "The operating gain is real at the core-PBT level"** (rev L460, L471)
- Counters 1a (import parity) and 1b (cost lag) are both grafted (rev L195, L365, L448, L473).
- The claim holds as qualified. No graft.

**C2. "The receivables build is growth-induced"** (rev L243)
- The second basis is now in A4 (rev L230). The claim holds. No graft.

**C3. "The supply-bound reading of the Q2 dip softens the demand concern"**
- The claim appears at rev L460. Its support is rev L179: "The inventory evidence fits Reading 2 better: there is no unsold stock build." Reading 2 says "Under this reading Q2 volume was capped by feedstock" (rev L178).
- The brief offers only weaker demand or a feedstock shortage (rev L475).

**Counter to C3 (from the same extracts). It survives.**
- **Production input rose in Q2.** Materials consumed rose 4.4% QoQ (12,553.80 vs 12,026.54 L, res R030 R031 L234). Power and fuel rose 6.2% QoQ (741.74 vs 698.15 L, res R055 R056 L238). Production input did not fall in value.
- **The dip matches the drawdown taper.** The FG/WIP drawdown fell from 1,598.10 to 287.81 L (res R038 R037 L235). That is 13.10 Cr less stock sold at cost. Materials plus inventory change fell 5.7% (13,624.64 to 12,841.61 L), in line with the revenue fall of 5.2% (-9.22 Cr) [DERIVED].
- **A third, filed reading.** The Q2 dip is the taper of Q1's stock liquidation, while fresh production rose. In both quarters the company sold all it produced plus some stock. That fits the deck's "market entire quantity" claim (R490) without a feedstock cap. Q1's 176.15 Cr carried the larger liquidation, so Q2's 166.92 Cr is the cleaner run-rate. A4 already uses it as the Q3 bar (rev L182).
- **"No unsold stock build" does not discriminate.** The deck says the company "Built the capability to expand and contract production as required" (deck R479 L257-L258). A demand-led output cut would also show no stock build. A4 does not cite R479.
- **Limits.** These are values, not tonnes. A Q2 raw-material price rise could hide flat or lower intake. A4's tonnage separator (rev L180) still settles the question.

**Graft required in A4:**
- Add a Reading 3 (stock timing, filed) to Step 3, with the lines above.
- Qualify or drop the "fits Reading 2 better" tilt.
- Add one sentence each to the brief (rev L475), the verdict basis (rev L460) and the Q2 flag line (rev L589).
- No A4 number, ledger row or protocol verdict changes.
- Type MISSING, route A4.

A5 note on its own iteration 0: U6 was raised as a possible supply-constrained reading. The filed QoQ lines test that reading, and this finding corrects the weight it now carries.

**Mandatory acquisition-economics probe**
- The buyback multiple is grafted (rev L450, L478, L584).
- The land position is unchanged; no multiple can be computed and the bear reading is carried.
- Closed.

### I1-4. Status of the iteration 0 findings

| ID | Status | Where A4 applied it |
|---|---|---|
| M1 | CLOSED | A1 R458-R512; A2 addendum; A4 rev L19, L22, Steps 3/5/7, Q17-Q20, M20-M25, Flags 1, 3, 8, 9 |
| M2 | CLOSED | rev L195, L210, L326, L365, L448, L473 |
| M3 | CLOSED | rev L228, L236, L242, L246, L449-L450, L476 |
| M4 | CLOSED | rev L450, L478, L584 |
| S1-S7 | applied | S1 rev L490; S2 rev L134, L146; S3 rev L292, L335; S4 rev L67; S5 rev L22; S6 rev L497; S7 rev L469-L479 |

### I1-5. Findings (iteration 1)

| ID | Type | Route | Gap | Anchor |
|---|---|---|---|---|
| N1 | MISSING | A4 | The surviving counter to C3 is absent from the review. Filed QoQ production input rose (materials +4.4%, power and fuel +6.2%), and the Q2 dip equals the taper of the FG/WIP drawdown (13.10 Cr less stock sold vs revenue -9.22 Cr). R479 means "no stock build" does not discriminate. Step 3 Reading 2's feedstock-cap premise, the "fits Reading 2 better" tilt, the brief (rev L475) and the verdict basis (rev L460) omit this. | res R030 R031 L234; R055 R056 L238; R038 R037 L235; R012 R013; deck R479 L257-L258; rev L178-L179, L460, L475, L589 |

FACTUAL: none. CONTRADICTION: none. Arithmetic mismatches above rounding: none.

### I1-6. Verdict (iteration 1)

**INCOMPLETE.** Failing agent: **A4**. Finding type: MISSING (1), finding N1.
- The size of the change: one paragraph in Step 3 and one sentence each in the brief, the verdict basis and the flag line.
- No number, ledger row, cash classification or protocol verdict (PROCEED WITH FLAGS) moves.
- All four iteration 0 findings are closed. The deliverable gate, the coverage and the arithmetic pass.
- This was loop iteration 1 of 1. Under the loop cap, N1 goes to the orchestrator as an open item for the operator.

### I1-7. STYLE notes (iteration 1; logged, no re-run)

- S8. Step 5 FCF row (rev L228): "about 7.31 Cr" is the exact sum of the four named items. The full counterfactual, after 0.13 Cr of minor investing flows and the cash draw, is 7.18 Cr. Say "about 7.2 Cr" or name the omission.
- S9. Step 7 strategic premium (rev L338) says "lowest cost producer globally" is "contradicted" by the margin swing. The extracts support "unsupported", not "contradicted". A lowest-cost spread business still swings with price, and the FY26 trough stayed EBITDA-positive at 4.70%. The brief frames it correctly as INFERENCE (rev L498). Hold bull and bear claims to the same bar (Master v3.7 Rule J).
- S10. Rev L244: the FY26 CFO/PAT of 6.7x uses pre-exceptional PAT (deck R150, 6.2 Cr). On reported PAT of 5.54 Cr it is 7.5x. State the basis.
- S11. Step 3 Reading 1, "receivables rose 47% to hold volume" (rev L177), sits against Step 5's flat-to-lower receivable days (rev L230, L243). Say that only the deck CCC and the missing 30-Jun balance keep that leg open.
- S12. The brief says the buyback was bought "with borrowed money" (rev L478), while Flag 4 says "likely debt-funded" (rev L450). Align the hedge.
- S13. Rev L212 reads "A3-P20"; it should be A3P-20.
- S14. A1 rows R460 ("revenue") and R467 ("globally") carry text from the adjacent column, and R466 merges two phrases. A4 compensates by quoting the fulltext (rev L10). Recorded for A1.
- S15. The A2 deck ledger at L19 still reads "MISSING_FROM_STRUCTURED: none". The addendum (ledger L513-L572) supersedes it. Update the note.
- S16. The residual deck p4 L85-L93 "Pan India" sourcing claim has no row. Its theme is duplicated by R471, R472 and R487, though "Pan India" sits oddly beside the 500 km radius claim (R472). Immaterial. Recorded for next quarter's A1.

---

```yaml
stage: A5-adversary
company: "FAIRCHEMOR"
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
  - {claim: "Supply-bound reading of the Q2 -5.2% QoQ dip softens the demand concern; inventory evidence fits Reading 2 better (rev L178-L179, L460, L475)", counter: "Filed QoQ production input rose (materials consumed +4.4%, power and fuel +6.2%), so feedstock did not visibly cap Q2; the dip equals the taper of the FG/WIP drawdown (15.98 to 2.88 Cr; 13.10 Cr less stock sold vs revenue -9.22 Cr), so Q1 was flattered by stock liquidation and Q2 is the cleaner run-rate; 'no stock build' does not discriminate because deck R479 says production can expand and contract as required. Values not tonnes; tonnage separator still settles it", source_line: "res R030 R031 L234; R055 R056 L238; R038 R037 L235; R012 R013 L225-L227; deck R479 L257-L258", type: MISSING}
findings_by_type:
  factual: []
  missing:
    - {id: N1, route: A4, gap: "Add Reading 3 (stock timing, filed) to Step 3 and qualify the 'fits Reading 2 better' tilt; carry one sentence into the brief (rev L475), the verdict basis (rev L460) and the Q2 flag line (rev L589). No number or verdict change", source_line: "res R030 R031 R055 R056 R037 R038; deck R479 L257-L258"}
  contradiction: []
  style:
    - "S8 Step 5 counterfactual 'about 7.31 Cr' = exact sum of named items; full counterfactual 7.18 Cr (rev L228)"
    - "S9 'lowest cost producer' called 'contradicted' (rev L338); extract supports 'unsupported' (Rule J symmetric bar)"
    - "S10 FY26 CFO/PAT 6.7x on pre-exceptional PAT; 7.5x on reported (rev L244)"
    - "S11 Reading 1 receivables leg vs Step 5 flat-to-lower days (rev L177 vs L230, L243)"
    - "S12 Brief 'with borrowed money' vs Flag 4 'likely debt-funded' (rev L478 vs L450)"
    - "S13 'A3-P20' typo (rev L212)"
    - "S14 A1 column bleed in deck R460, R467; R466 merges two phrases (A4 compensates, rev L10)"
    - "S15 A2 deck ledger L19 stale 'MISSING_FROM_STRUCTURED: none'"
    - "S16 Residual deck p4 L85-L93 'Pan India' sourcing claim uncaptured; theme duplicated by R471 R472 R487"
loop_back_to: "A4"
gap: "MISSING (A4), N1: Step 3 lacks the filed stock-timing reading of the Q2 dip. Q2 materials consumed +4.4% and power and fuel +6.2% QoQ (res R030 R031 R055 R056); FG/WIP drawdown 15.98 to 2.88 Cr explains the revenue fall (res R038 R037); deck R479 makes 'no stock build' non-discriminating. Qualify the Reading 2 tilt and carry one sentence each into the brief (rev L475), verdict basis (rev L460) and Q2 flag line (rev L589). Loop cap reached: open item for the operator."
style_notes:
  - "S8 7.31 vs 7.18 Cr counterfactual wording (rev L228)"
  - "S9 'contradicted' to 'unsupported' (rev L338)"
  - "S10 CFO/PAT PAT basis (rev L244)"
  - "S11 Reading 1 receivables leg (rev L177)"
  - "S12 buyback funding hedge (rev L478)"
  - "S13 A3P-20 typo (rev L212)"
  - "S14 A1 column bleed R460 R467 R466"
  - "S15 A2 ledger L19 stale note"
  - "S16 residual p4 Pan India claim"
analyst_note: "Loop 1 closed every iteration 0 finding. A1 added 55 deck rows, A2 ledgered all 512 with no orphans, and A4 applied all four grafts and all seven style fixes. Every new figure recomputes. One new MISSING finding remains, and it comes from A4's own loop change. A4 turned the Q2 dip into demand-side vs supply-bound readings and tilted to supply-bound. That tilt now sits in the verdict basis. The filed P&L points elsewhere. Q2 materials consumed rose 4.4% and power and fuel rose 6.2% QoQ, so production input did not fall. The revenue dip equals the taper of Q1's stock liquidation, from a 15.98 Cr drawdown to 2.88 Cr. R479 'expand and contract production' means a lack of stock build proves nothing. This is values, not tonnes, so tonnage still decides. The fix is one Step 3 paragraph and three sentences, with no number or verdict change. My iteration 0 U6 note prompted the supply-bound reading, and this finding corrects its weight. The loop cap is reached, so N1 goes to the operator as an open item."
```
