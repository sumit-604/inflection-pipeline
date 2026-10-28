# A5 ADVERSARY / COMPLETENESS AUDIT: UNIMECH Q2 FY27

Agent: A5 adversary | model claude-opus-5-5 | run date 28-Oct-2026
Under audit: runs/unimech-q2fy27/work/review_unimech_q2fy27.md ("review l.N")
Inputs read: seven A1 fulltexts and structured files (extracted/), four A2 ledgers, the A4 review. Nothing under inputs/ was opened. No A3 file was read; A3 finding IDs appear only as A4 cites them.
Anchors: res / deck / pr / call / MA / dev / lta l.N = A1 fulltext line. R### = A1 structured row ID.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

PLAIN-LANGUAGE BRIEF at review l.997-1082:
(1) Summary narrative, review l.1001-1019, 18 lines: PRESENT.
(2) Sector intelligence, review l.1021-1034: PRESENT.
(3) Business-model intelligence, review l.1036-1052: PRESENT.
(4) Competition intelligence, review l.1054-1064: PRESENT.
(5) Forward map, review l.1066-1082: one make-or-break reading plus 12 dated catalysts, each with a bull and a bear fork: PRESENT.

Gate: PASS. All five parts carry real content.

---

## 1. COVERAGE AUDIT

Method: an independent line-by-line pass over each A1 fulltext, diffed against the A2 ledger. Structured ID counts were re-grepped: results 953, presentation 670, press release 123, concall 257, monitoring 261, deviation 68, LTA 31. Every count equals the A1 header, the A2 ledger and the A4 preamble.

| Document | Category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | Numbered notes (SA 8 + CO 9) | 17 | 17 (res l.335-342, l.702-718) | none | PASS |
| Results | Board agenda items | 3 | 3 (res l.37, l.44, l.57) | none | PASS |
| Results | Auditor paragraphs (SA 4 + CO 7) | 11 | 11 (res l.106-129, l.365-469) | none | PASS |
| Results | Statement line items (8 statements) | 250 | 250 (SA BS 40, SA P&L 25, SA CF 38+16, CO BS 40, CO P&L 33, CO CF 39+19) | none | PASS |
| Results | ZERO_STANDING dash/Nil rows | 49 | 49 | none | PASS |
| Results | Consolidation entities | 6 | 6 (res l.407-432; l.703-711) | none | PASS |
| Results | Structured IDs | 953 | 953 | none | PASS |
| Presentation | Slides | 26 | 26 | R222 (deck l.369) | FAIL (see C1) |
| Presentation | Table line items (p8 / p24 / p25) | 81 | 81 (20 + 23 + 38, deck l.230-249, l.671-693, l.731-769) | none | PASS |
| Presentation | MISSING_FROM_STRUCTURED | 2 (M1, M2) | 2; spot checks of p12-p15, p18, p20 found every number rowed (R215-R255) | none | PASS |
| Press release | Pages | 3 | 3 | none | PASS |
| Press release | Table cells (4 rows x 8 columns) | 32 | 32 (pr l.106-109) | none | PASS |
| Press release | Structured IDs | 123 | 123 (+ M01-M05 trivial) | none | PASS |
| Concall | Speaker turns | 65 | 65; turn ranges are contiguous from call l.22 to l.847 | R244 / R065 (call l.352-356) | FAIL (see M2) |
| Concall | Analyst questions | 24 | **25** | n/a | **FAIL (see M1)** |
| Concall | Structured IDs | 257 | 257 | none | PASS |
| Monitoring / deviation / LTA (no A2 ledger) | Rows read by A4 | n/a | MA total row, object rows, ICDR text and dev rows re-checked; LTA effective date R019 cited by ID only | lta R019-R020 not stated | FAIL (see M5) |

**Missing from the ledger (A2).** A2's question ledger (ledger_concall section 3) records T57 only as "Operator / Gaurav ... next question". The turn carries an analyst question at call l.792-794: "of the 250 [FAIs] you've proved so far how many part numbers are now in serial production and what is the current quarterly revenue run rate from those serial PCA parts?" The management answer is at T58 (call l.794-800). Fresh count: 25. Ledger count: 24. A4 already reviews this question as Q22a (review l.703) and makes it Exchange 3 (review l.732-738). A4's own 0C still says "24 question turns" (review l.523), so A4 contradicts its own 25-row table.

**Orphan rows.** A4 marks every row as reviewed in a single blanket statement (review l.21: "No ledger row is unreviewed"). For the descriptive slides (p2-p4, p9-p11, p17-p18, p21-p23, p26) and the boilerplate rows, I accept that blanket statement as "reviewed, no finding". Two rows fail it, because each row's content contradicts or qualifies an A4 conclusion and A4 never cites it:
- Presentation R222 (deck l.369): "Joint Investment in JV: ~USD 30 Mn". This contradicts A4's Saudi funding-gap flag (C1).
- Concall R244 and R065 (call l.352-356): the 65% utilisation includes capacity dedicated to new-product, prototype and qualification work. A4 reads 65% with no qualifier (M2).

A4 does not cite deck pages p10-p16, p22 or p25 by line anywhere (grep of the review). R222 sits on p14.

---

## 2. ARITHMETIC AUDIT

Every derived metric was recomputed from lakh-precision filed lines and then converted to Rs Cr. "PASS" means the result agrees within rounding.

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Op EBITDA Q2 FY27 (PBT + D + Fin - OI) | 49.01 | 4,490.68 + 904.32 + 203.36 - 697.79 = 4,900.57 lakh = 49.01 | res l.574, l.581, l.582, l.585 | PASS |
| Op EBITDA Q2 FY26 / Q1 FY27 / H1 FY27 / H1 FY26 / FY26 | 18.54 / 39.25 / 88.26 / 38.34 / 75.12 | 18.54 / 39.25 / 88.26 / 38.34 / 75.12 | same lines | PASS |
| Op EBITDA margin (6 columns) | 39.84 / 29.92 / 36.47 / 38.27 / 30.68 / 31.23% | 39.84 / 29.92 / 36.47 / 38.27 / 30.68 / 31.23% | res l.573 | PASS |
| Reported EBITDA (6 columns) | 55.98 / 28.41 / 46.58 / 102.57 / 59.64 / 122.08 | same | res l.581-585 | PASS |
| Core PBT (PBT - OI), 6 columns | 37.93 / 10.81 / 29.36 / 67.29 / 23.57 / 33.47 | same | res l.574, l.585 | PASS |
| OI / PBT | 15.5 / 47.7 / 20.0 / 17.5 / 47.5 / 58.4% | same | res l.574, l.585 | PASS |
| ETR Q2 FY27 | 27.57% | 27.565% on lakh (1,237.85 / 4,490.68); 27.57% on rounded Cr | res l.591, l.585 | PASS (rounding, S1) |
| ETR other columns | 23.70 / 23.68 / 22.14 / 25.82 / 20.82% | same | res l.591 | PASS |
| Current-tax ETR | 28.32 / 23.39 / 31.85 / 29.91 / 20.85 / 21.37% | same | res l.588 | PASS |
| ETR shields H1 (deferred / prior period) | 260 / 149 bps | 212.27 / 8,159.53 = 2.60%; 121.70 / 8,159.53 = 1.49% | res l.589-590 | PASS |
| PAT margin on revenue | 25.83 / 25.28 / 25.89 / 25.86 / 27.84 / 26.31% | same | res l.594 | PASS |
| Gross margin 1 - (COMC + inv chg)/Rev | 72.62 / 73.55 / 67.93 / 70.43 / 73.29 / 75.55% | same | res l.577-578 | PASS |
| Materials + conversion % | 30.61 / 32.18 / 35.34 / 32.81 / 33.03 / 30.30% | same | res l.577-579 | PASS |
| Employee % | 15.66 / 21.07 / 15.10 / 15.40 / 20.59 / 22.21% | same | res l.580 | PASS |
| YoY: revenue / op EBITDA / D&A / finance / OI / core PBT / PBT / PAT / EPS | +98.4 / +164.3 / +42.6 / +46.2 / -29.3 / +250.8 / +117.2 / +102.8 / +102.6% | same | res l.573-613 | PASS |
| Margin bridge YoY | +992 bps = -541 employee, -294 other exp, -157 materials + conversion | +992.4 bps; other exp 13.89% vs 16.83% | res l.580, l.583 | PASS |
| EBIT (op EBITDA - D&A) | 12.20 to 39.96, +227.5% | 1,220.32 to 3,996.25 lakh, +227.5% | derived | PASS |
| H1 YoY: revenue / op EBITDA / margin / core PBT / PAT / EPS | +84.5% / +130.2% / +759 bps / +185.4% / +71.4% / +71.3% | same | res l.573-613 | PASS |
| QoQ trajectory | Q1 FY26 62.99; Q3 FY26 33.72 and (6.94); run-rates -1.6 / -45.6 / +142.6 / +31.6 / +14.3% | same; Q3 core PBT (6.93) on rounded Notion Q4 inputs | res l.573; review l.203-208 | PASS (rounding) |
| PAT bridge Q2 YoY | 18.26 + 12.21 - 2.70 - 0.64 - 2.89 - 5.74 - 1.74 - 0.65 = 16.11 vs 16.10 | same; 18.26 + 12.21 = op EBITDA change 30.47 | res l.573-594 | PASS |
| OI-nil PAT test | ~26.7 (Q2 FY27); ~8.1 (Q2 FY26) | 37.93 x 0.7243 - 0.75 = 26.72; 10.81 x 0.763 - 0.11 = 8.14 | derived | PASS |
| Clean Q2 PAT ex prior-period tax credit | 30.56 | 3,177.48 - 121.70 = 3,055.78 lakh | res l.589, l.594 | PASS |
| SA operating EBITDA (6 columns) | 6.48 / (4.00) / 1.08 / 2.48 / 3.98 / 0.15 | same | res l.222-233 | PASS |
| SA core PBT (6 columns) | 3.36 / (6.78) / (1.54) / (3.43) / (0.90) / (10.58) | same | res l.222, l.233 | PASS |
| SA-CO gap (CO - SA)/SA | 163.9 / 1,165.7 / 272.7 / 135.1 / 456.0 / 184.8% | same, except H1 FY27 is 455.9% on PAT l.594 and 456.0% on owners' PAT l.603 | res l.240, l.594, l.603 | PASS (basis, S2) |
| SA share of CO PAT | 37.9 / 7.9 / 26.8 / 42.5 / 18.0 / 35.1% | same | same | PASS |
| Q2 decomposition | 8.53 + 24.00 - 0.75 = 31.77 | 3,177.48 - 852.59 + 75.35 = 2,400.24 lakh | res l.240, l.593-594 | PASS |
| Non-parent revenue QoQ / parent QoQ | +2.9% / 3.7x | 10,604.47 / 10,302.98 = +2.93%; 1,695.36 / 459.06 = 3.69x | res l.221, l.573 | PASS |
| Intra-group interest at least | Rs 8.79 Cr = 65.3% of SA H1 PBT | SA interest income 1,247.45 - CO 368.69 = 878.76 lakh; / 1,345.26 = 65.3% | res l.268, l.632, l.233 | PASS (lower-bound logic holds) |
| CFO / PAT H1 FY27; H1 FY26; CGO / PBT | 0.896x; 0.396x; 0.961x | 5,345.90 / 5,963.85 = 0.896; 13.79 / 34.80 = 0.396; 7,842.99 / 8,159.53 = 0.961 | res l.652-654, l.594, l.585 | PASS |
| Capex; FCF | 22.87 / 36.52 (+59.7%); (9.08) / 16.94 | same | res l.654-657 | PASS |
| Receivable / inventory / payable days; CCC | 98.3, 91.0 (97.0 on H1); 38.1, 28.3; 28.7, 19.3; 107.8 to 100.0 | same | res l.525, l.528, l.554-555 | PASS |
| Receivables acquired with Hobel (inference) | ~37.5 | 57.80 BS rise - 20.28 CF = 37.52 | res l.528, l.642 | PASS |
| Net cash Mar-26 / Sep-26 / change | 479.71 / 65.45 / -414.26 | 591.80 - 112.09; 226.44 - 160.98 | res l.527-530, l.545, l.551 | PASS |
| Borrowings | 112.09 to 160.98 (+43.6%, +48.89); parent 12.02 | same | res l.193, l.199, l.545, l.551 | PASS |
| Goodwill / total equity | 40.3% | 32,199.15 / 79,816.18 = 40.34% | res l.515, l.541 | PASS |
| Opening-cash gap; implied net Hobel cash | 10.75; 414.05 | 4,790.22 - 3,715.40 = 1,074.82 lakh; 424.80 - 10.75 | res l.529, l.660, l.688 | PASS |
| PPE / CWIP / intangibles / gross-block movement | +9.06 / +3.84 / +47.35 / +15.2 | same | res l.512-516 | PASS |
| IPO object rows, beginning of Q2 | 247.80 vs printed 153.30 | 23.54 + 25.29 + 35.43 + 44.71 + 0 + 40.65 + 61.29 + 16.89 = 247.80; plus 2.20 = 250.00 | MA l.355-515 | PASS |
| ICDR 7(3) share | 41.0% | (41.23 + 61.29) / 250 = 41.0% | MA l.457, l.473 | PASS |
| ROCE deck basis / incl OI / ex-treasury | 14.86% / 17.8% / 19.5% | 142.52 / 959.14; 171.14 / 959.14; 142.52 / 732.70 | deck l.235-237, l.733-739; res l.541 | PASS |
| H2 revenue needed (green / trigger a) | 189.38 (94.69 per quarter) / 169.38 (84.69 per quarter) | same | res l.573 | PASS |
| Run-rates | 492.0; 461.24; PAT 119.28 / 127.1; EPS 23.44 = 90% of Rs 26.0 | same | res l.573, l.594, l.613 | PASS |
| CMP multiples | 7.7x / 9.6x / 6.9x | 1,638 / 213, 170, 237 | review l.54 | PASS |
| Order book | -5.1% QoQ; book-to-bill ~0.88; 589 / 855 = 69%; 855 / 105 = 8.1x | same | deck l.153-155, l.192 | PASS |
| Implied FX; valued LTA items; residual | Rs 25.72 / SAR; Rs 96.46 / USD; 487.1; 101.9 | 39.3572 Cr / SAR 15.3 Mn = 25.724; x 3.75 = 96.46; USD 50.5 Mn x 96.46 = 487.1 | res l.341; deck l.396, l.529 | PASS |
| Saudi SAR 60M equity; funding gap | 154.3; 46-96 | arithmetic correct, but the SAR 60M input has no anchor in any extract and is contradicted by deck l.369 | review l.989 | INPUT FAIL (C1) |
| Credibility ratio | 46.9% (3.75 / 8); 52.8%; 34.1% | same | review l.616-641 | PASS |
| Quantified claims / specificity / hedges | 27 / 38 = 71%; 0.49 and 0.47; 15 | same | review l.537-577, l.808, l.823 | PASS |
| Q&A share of call | ~57% | 33:10 / 58:37 = 56.6% | call l.386, l.835, l.847 | PASS |
| Deck PAT% basis | 24.4% on total income | 317.7 / 1,299.8 = 24.4% | deck l.249; pr l.106 | PASS |

**Arithmetic mismatches above rounding: none.** The one input failure is the unanchored SAR 60M figure. It is tagged CONTRADICTION in C1, not as arithmetic.

---

## 3. ADVERSARIAL READ

### Claim 1 (most positive): "Operations beat every thesis line ... The core earnings step-up is real" (review l.237, l.938, l.1186)
- **Bear counter from the extract.** The YoY base has no Hobel, which is consolidated only from 27-Apr-2026 (res l.711). Over Q2 the parent's revenue rose 3.7x QoQ while non-parent revenue rose 2.9% despite an extra Hobel month (res l.221, l.573). On the ASR figure "Hobel 30% of H1" (call l.315), revenue without Hobel fell about 12% QoQ. Management also signals compression beyond FY27: PCA margins equal to tooling or below, and a 1-2% R&D drag (call l.532, l.825-829).
- **Survives?** Yes, but A4 has already incorporated it: review l.175, l.191, l.165, flag 6 (l.981) and flag 9 (l.984). No graft required.

### Claim 2: "Earnings quality is better: OI share of PBT fell from 47.7% to 15.5% ... Treasury is now small" (review l.195, l.938)
- **Bear counter from the extract.** The filed consolidated cash flow names the H1 non-operating items:
  - Interest income is Rs 3.69 Cr (res l.632), down from Rs 15.64 Cr in H1 FY26. That is 25.8% of H1 OI of Rs 14.31 Cr (res l.574).
  - MTM gain on investments is Rs 1.96 Cr (l.634) and profit on sale of investments is Rs 2.47 Cr (l.638). Together these market gains are 31.0% of H1 OI.
  - There is a lease-modification gain of Rs 0.94 Cr (l.635), an unrealised FX gain of Rs 1.41 Cr (l.628) and a provision write-back of Rs 0.10 Cr (l.636). These are one-offs or non-operating items.

  The "steady run rate" of about Rs 7 Cr a quarter (call l.319-321) now rests on market gains and one-offs. Treasury yield no longer carries it. This answers A4's own puzzle (review l.195), where Rs 6.98 Cr a quarter looked "about 12.3% annualised, too high for treasury yield alone". A4 calls the composition ND (review l.195, l.384, QB11 l.462), and its note answer (3) says "the rest is recurring" (review l.80). The cash flow shows otherwise. Placement of the FX and lease gains inside OI is [INFERENCE]; their presence in PBT is filed.
- **Survives?** YES. **Graft into A4 (M3).**

### Claim 3: "Operating promises (Q2 stronger, LTAs signed, FACC execution) are delivered"; Honeywell engine LTA scored DELIVERED, 1.0 point (review l.621, l.644)
- **Bear counter from the extract.**
  - The filed LTA is a framework: Honeywell "may issue purchase orders". No value, volume or minimum purchase is stated (lta l.45-46, R015, R026, R027). A4 already notes this (review l.749, l.371).
  - Not incorporated: the LTA is "effective from April 1, 2026 and remains in effect until November 1, 2036" (lta l.44, R019-R020). The Reg 30 intimation is dated 26-Oct-2026 (lta l.18), 208 days after that effective date.
  - On file, the 04-Aug Q1 call called this agreement "advanced stage" (review l.621, Notion l.880). So one of two things is true. The agreement was made retroactive to April. Or the August description understated an agreement already in force. The execution date, which sets Reg 30 timeliness, is not disclosed.
- **Survives?** YES. The DELIVERED score can stand, but it needs the filed-date qualifier. The fact also adds evidence to A4's trigger (d) candidate leg "Honeywell LTA signing date undisclosed" (review l.356). **Graft into A4 (M5).**

### MANDATORY ACQUISITION-ECONOMICS PROBE
The documents describe four deals: Hobel (deck l.309, "Rs 450 crore all-cash acquisition"), the Dheya stake buy (res l.339), the Kanoo-Unimech Saudi ODI (res l.341; deck l.365-396) and the intra-group Hobel share transfer (res l.47).

**(a) Hobel. The bear reading survives and must be grafted (M4).**
- **Consideration.** The deck states Rs 450 Cr (l.309, R215). H1 cash out is Rs 424.80 Cr for the partnership interest (res l.660) plus Rs 0.20 Cr for shares from "erstwhile shareholders" (res l.659). That leaves Rs 25.00 Cr of the headline outside H1 cash. Current other financial liabilities rose Rs 27.99 Cr (res l.556), of which only Rs 3.21 Cr went through CFO (res l.650). The remaining Rs 24.78 Cr non-cash increase is consistent with deferred consideration of about Rs 25 Cr [INFERENCE].
- **Multiple.** Target PAT is **NOT FOUND** in any of the seven A1 extracts, so price / PAT cannot be stated from filed evidence. The EV / EBITDA bound uses non-filed inputs:
  - On the H1 run-rate: Hobel = 30% of H1 revenue = Rs 69.19 Cr over 157 days (call l.315, MGMT, ASR), about Rs 160.9 Cr annualised. At the >50% EBITDA margin on file (review l.364, prior Notion), Rs 450 Cr / Rs 80.4 Cr = **about 5.6x EBITDA**.
  - On FY26 revenue of about Rs 129 Cr (prior Notion via review l.364): Rs 450 Cr / Rs 64.5 Cr = **at most about 7.0x EBITDA**.
- **Quality markers.** About 90% exports, 13+ year relationships with global OEMs, a 2 lakh sq ft SEZ plant, established 2007 (deck l.335-346). ROCE, debt and cash are NOT FOUND (cash about Rs 10.75 Cr only by inference from the opening-cash gap, res l.688 vs l.529).
- **Why is it cheap?** The extract and A4's file support two readings:
  - (i) Concentration. Two OEM groups take about 93% of Hobel sales (review l.364, prior).
  - (ii) A possible peak earnings year. Current Hobel demand is "driven by the strong demand of genset engines in data center industry", and customers ask for extra capacity (call l.211-214). That is a capex-cycle driver, which A4 scores only as a positive (trigger 4, review l.367). Hobel's share of the book is 7% of the PCA mix (deck l.195). That is about Rs 54.5 Cr (7% x 91% x Rs 855 Cr, deck l.153, l.194), or 1.2-1.7 quarters of Hobel revenue on A4's two readings [INFERENCE]. The orders are short-cycle.

  Representativeness cannot be tested. Management refuses the Hobel margin as policy (call l.527-529). Goodwill plus new intangibles (Rs 321.99 Cr + Rs 47.35 Cr = Rs 369.34 Cr, res l.515-516) are 82% of the Rs 450 Cr price and 40.3% of equity. Nothing in the extract shows that the multiple is fair.
- **What A4 must add.** A4 has the concentration and goodwill facts (review l.364, l.979). It does not state the multiple, the peak-year test, the order cover or the Rs 25 Cr reconciliation. **Graft into 6D trigger 1 and flag 4.**

**(b) Dheya. A4 already covers the bear reading; no graft.**
- The company paid Rs 299.82 lakh for 850 shares in a secondary purchase, about Rs 35.27 lakh a share (res l.339). Its stake fell to 27.24% because Dheya raised outside capital.
- Target earnings are a loss. The group's share of the loss is Rs 0.75 Cr in Q2 (res l.444, l.593), which implies a Dheya Q2 loss of about Rs 2.77 Cr at 27.24% [arithmetic; the stake moved within the quarter]. Price / PAT is not meaningful.
- Management cites an Avana round at about Rs 200 Cr (call l.240). At that value the 27.24% stake would be about Rs 54.5 Cr against an equity-method carrying value of Rs 13.25 Cr (res l.517). Unimech still declined the primary at that price. The price per share relative to the Avana round is NOT FOUND.
- A4 already carries the secondary-only purchase, the dilution, the 7x YoY loss share, revenue not before FY28/FY29 and the unnamed seller (review l.370, QB22-QB23).

**(c) Saudi ODI. The bear reading survives but runs opposite to A4's flag (C1).**
- Rs 39.36 Cr bought 51% of a pre-revenue JV (res l.341; deck l.396). Production readiness is Mar/Apr-2027 (call l.229) and there are zero proven O&G FAIs (deck l.163). No earnings multiple applies.
- The filed deck states "Joint Investment in JV: ~USD 30 Mn" (deck l.369, R222). At A4's filed Rs 96.46 / USD that is Rs 289.4 Cr, above the Rs 200-250 Cr capex (call l.574-575). So A4's "funding gap of about Rs 46-96 Cr" (review l.989) is not supported.
- The real bear is Unimech's own remaining 51% commitment. It is Rs 108.2 Cr on the USD 30 Mn all-equity reading (Rs 147.6 Cr less Rs 39.36 Cr paid). It is Rs 39.4 Cr on the SAR 60M equity reading A4 uses. Against it stands Sep-26 net cash of Rs 65.45 Cr, or about Rs 26.1 Cr after the 01-Oct ODI [arithmetic, before Q3 CFO]. The deck does not split equity from debt.

**(d) Intra-group Hobel share transfer.** The price is not disclosed (res l.47-55). There is no group P&L effect. A4 covers it (QB15, R-A3-09). No graft.

---

## 4. FINDINGS (tagged)

| ID | Type | Owner | Finding |
|---|---|---|---|
| M1 | MISSING | A2 (then A4 count) | Concall question ledger lacks the T57 analyst question (Gaurav, firm unidentified, call l.792-794: how many of the 250 qualified parts are in serial production and at what quarterly run-rate). Fresh count 25, ledger 24. A4 already reviews it as Q22a (review l.703). A4 0C says "24 question turns" (review l.523); correct it to 25 once A2 adds the row. |
| C1 | CONTRADICTION | A3 (review R222) then A4 | Saudi funding gap. Flag 14 (review l.989), QB20 (l.471) and 6D 5b (l.369) say the Rs 200-250 Cr capex exceeds "planned equity SAR 60M" and leaves a "funding gap of about Rs 46-96 Cr unstated". SAR 60M has no anchor in any extract. Filed deck l.369 (R222) says "~USD 30 Mn" joint investment = Rs 289.4 Cr at A4's Rs 96.46 / USD, which is above the capex. A4 never cites R222. Restate as Unimech's remaining 51% commitment of Rs 39.4-108.2 Cr against net cash of Rs 65.45 Cr (about Rs 26.1 Cr after the ODI). Note that the deck does not split equity from debt. |
| M2 | MISSING | A3 (review R244 / R065) then A4 | Utilisation qualifier dropped. Call l.351-356 says the ~65% "includes about 50% to 20% [garbled] of our available capacity ... dedicated to new produc[t introduction], provos, and customer qualification orders". A4 reads 65% with no qualifier: watchlist 4 (review l.342), concall watchlist (l.881), 2 (l.593). On a 15-20% reading [INFERENCE], serial-production utilisation is about 45-50%, under the "< 60% through FY27" red line. The AMBER status has not been tested on that basis. |
| M3 | MISSING | A4 | Other-income composition is called ND (review l.80, l.195, l.384, l.462). The filed H1 cash flow gives it: interest Rs 3.69 Cr (res l.632; H1 FY26 Rs 15.64 Cr), MTM Rs 1.96 Cr (l.634), investment-sale gain Rs 2.47 Cr (l.638), lease-modification gain Rs 0.94 Cr (l.635), unrealised FX gain Rs 1.41 Cr (l.628). Interest is only 25.8% of H1 OI. Graft: replace "ND" in Step 2 diagnostic 6 and 6.5A, list the lease-modification and FX gains as one-offs, and reword note answer (3). This is a surviving bear counter to Claim 2. |
| M4 | MISSING | A4 | The mandatory acquisition-economics probe was not run on Hobel. State that price / PAT is NOT FOUND. State EV / EBITDA of about 5.6-7.0x on MGMT / prior inputs. Graft the peak-year reading (data-centre genset demand, call l.211-214), about 93% concentration, an order cover of about Rs 54.5 Cr (deck l.153, l.194-195), goodwill plus intangibles at 82% of price (res l.515-516) and the Rs 450 Cr vs Rs 425.00 Cr cash reconciliation (deck l.309; res l.659-660) into 6D trigger 1 and flag 4. |
| M5 | MISSING | A4 | Honeywell LTA filed dates dropped: effective 1-Apr-2026 to 1-Nov-2036 (lta l.44, R019-R020), intimated 26-Oct-2026 (lta l.18). Add this qualifier to the 3A DELIVERED row (review l.621) and as evidence in the 6C(d) candidate list (review l.356). This is a surviving bear counter to Claim 3. |

FACTUAL findings: none. All numbers A4 states that are anchored to filed lines are correct.

---

## 5. VERDICT

**INCOMPLETE.**
- Failing agents, in pipeline order:
  - **A2** (M1, MISSING): one analyst question is missing from the concall question ledger.
  - **A3** (C1 and M2 rows): R222 and R244 / R065 are effectively unreviewed under the orphan rule.
  - **A4** (C1 CONTRADICTION; M2-M5 MISSING): the grafts listed in section 4.
- loop_back_to: **A2**, the earliest agent whose output changes. The A2 fix is mechanical: one row, count 24 to 25. A3's work is limited to two rows. The substantive repairs are A4's five grafts and its 0C count line. All of them fit inside one remediation cycle.
- Arithmetic: no mismatch. Brief gate: PASS.

---

## 6. STYLE NOTES (logged; no loop)

- S1. ETR Q2 FY27 shows 27.57%. On lakh precision it is 27.565%, i.e. 27.56% (review l.129). The difference is rounding only.
- S2. The SA-CO gap uses owners' PAT (res l.603) for H1 FY27 (456.0%) and PAT l.594 elsewhere (455.9% on l.594) (review l.162). Use one basis.
- S3. Brief provenance labels. "Hobel ... explains a large part of this growth [FILED]" (review l.1005), "That goodwill holds the return on capital down at 14.9% [FILED]" (l.1049) and "Customer qualification gives it switching protection [FILED ...]" (l.1056) are inferences built on filed numbers. Relabel them [INFERENCE].
- S4. Brief: "An equity raise comes in early 2027" (review l.1050) drops "expect to consider ... subject to final requirement and market conditions" (call l.366-369). A4 keeps the qualifier at review l.819; carry it into the brief.
- S5. The preamble (review l.21) lists the deck's M1-M2 but not the press release's M01-M05 (ledger_pressrelease l.47-52, all trivial).
- S6. The header puts the call at 11:00 IST (review l.4, Notion). The ASR file says it was produced at 11:55 IST for a 58:37 recording (call l.20, l.847). The two are about 4 minutes apart. Immaterial.
- S7. Basis of working-capital days. A4's CCC (100.0 days, review l.256) may not be management's WC-days basis. Management guides 150-160 by Mar-27, down from "160+" at Q1 (review l.595). A move of 50-60 days in two quarters points to a different definition. Label the basis on watchlist 5 (review l.343) and on the "Tightened" trajectory.
- S8. "Dheya CDR before 26-Dec-2026" (review l.956) reads ASR "December 26th" (call l.263) as a day. It may mean Dec-2026.
- S9. Quantify cash caution (i) (review l.265). H1 CFO includes an Rs 8.93 Cr inventory release (res l.641) although BS inventory rose Rs 13.08 Cr (res l.525). That implies about Rs 22.0 Cr of acquired inventory being run down [INFERENCE]. CFO also includes an Rs 6.78 Cr build in provisions (res l.649). The direction is already in A4, and the "test NOT MET" conclusion is unchanged.

---

```yaml
stage: A5-adversary
company: "UNIMECH"
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
  orphan_rows:
    - "presentation R222 (deck l.369, 'Joint Investment in JV: ~USD 30 Mn'): uncited; contradicts A4 flag 14 / QB20 / 6D 5b"
    - "concall R244 + R065 (call l.352-356): 65% utilisation includes NPI/proto/qualification capacity; qualifier absent from A4 6B item 4"
  missing_from_ledger:
    - "concall question at T57 (Gaurav, firm unidentified, call l.792-794): serial-production count and run-rate of the 250 qualified parts; ledger 24 vs fresh 25"
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "Earnings quality better: OI share of PBT 47.7% to 15.5%, treasury now small (review l.195, l.938)", counter: "H1 interest income only Rs 3.69 Cr (Rs 15.64 Cr H1 FY26); OI now rests on MTM Rs 1.96 Cr, investment-sale gains Rs 2.47 Cr, lease-modification gain Rs 0.94 Cr, unrealised FX Rs 1.41 Cr; composition is filed, not ND", source_line: "res l.628, l.632, l.634, l.635, l.638; call l.319-321", type: MISSING}
  - {claim: "Operating promises delivered; Honeywell engine LTA DELIVERED 1.0 (review l.621, l.644)", counter: "Filed LTA is a no-minimum framework effective 1-Apr-2026 to 1-Nov-2036, intimated 26-Oct-2026 (208 days later) and called 'advanced stage' on 04-Aug; execution date undisclosed", source_line: "lta l.18, l.44-46", type: MISSING}
  - {claim: "Hobel consolidation trigger ON TRACK; Rs 450 Cr capability-led all-cash acquisition (review l.364; deck l.309)", counter: "Price/PAT NOT FOUND; EV/EBITDA about 5.6-7.0x on MGMT/prior inputs for a >50% margin, ~90% export asset; cheapness consistent with ~93% two-group concentration and a data-centre genset demand peak; goodwill+intangibles Rs 369.34 Cr = 82% of price; Rs 25.00 Cr of headline not in H1 cash", source_line: "deck l.309, l.335-346, l.195; res l.515-516, l.556, l.650, l.659-660; call l.211-214, l.315, l.527-529", type: MISSING}
  - {claim: "Saudi JV funding gap Rs 46-96 Cr vs SAR 60M planned equity (review l.989)", counter: "Filed deck states ~USD 30 Mn joint investment = Rs 289.4 Cr at Rs 96.46/USD, above Rs 200-250 Cr capex; the bear is Unimech's remaining 51% commitment of Rs 39.4-108.2 Cr against Sep-26 net cash Rs 65.45 Cr (about Rs 26.1 Cr post-ODI)", source_line: "deck l.369, l.373, l.396; call l.574-575; res l.341", type: CONTRADICTION}
findings_by_type:
  factual: []
  missing:
    - "M1 [A2]: concall question ledger lacks T57 Gaurav question (call l.792-794); 24 vs 25; A4 0C (review l.523) must then read 25"
    - "M2 [A3 R244/R065 -> A4]: utilisation qualifier dropped (call l.351-356); watchlist 4 AMBER untested on serial-production basis (~45-50% if 15-20% is qualification capacity, INFERENCE)"
    - "M3 [A4]: OI composition called ND (review l.80, l.195, l.384, l.462) though H1 CF gives it (res l.628-638); lease-modification and FX gains are one-offs"
    - "M4 [A4]: acquisition-economics probe absent for Hobel; state price/PAT NOT FOUND, EV/EBITDA ~5.6-7.0x, peak-year and concentration reading, Rs 450 Cr vs Rs 425.00 Cr cash; graft into 6D trigger 1 and flag 4"
    - "M5 [A4]: Honeywell LTA effective 1-Apr-2026 to 1-Nov-2036 (lta l.44) not stated; add to 3A DELIVERED row and 6C(d) candidate leg"
  contradiction:
    - "C1 [A3 R222 -> A4]: flag 14 / QB20 / 6D 5b Saudi funding gap on unanchored SAR 60M vs filed deck l.369 ~USD 30 Mn joint investment (Rs 289.4 Cr); restate as remaining Unimech commitment Rs 39.4-108.2 Cr vs net cash Rs 65.45 Cr"
  style:
    - "S1 ETR Q2 27.57% vs 27.56% on lakh precision (rounding)"
    - "S2 SC-gap H1 FY27 uses owners' PAT (456.0%) vs PAT l.594 (455.9%)"
    - "S3 brief provenance: inferences labelled FILED (review l.1005, l.1049, l.1056)"
    - "S4 brief drops equity-raise hedge 'expect to consider ... subject to market conditions' (call l.366-369)"
    - "S5 preamble omits press-release M01-M05"
    - "S6 call start 11:00 IST vs ASR produced 11:55 IST for a 58:37 recording"
    - "S7 CCC basis may differ from management WC-days basis; label watchlist 5"
    - "S8 Dheya CDR 'December 26th' may mean Dec-2026"
    - "S9 quantify CFO caution: Rs 8.93 Cr inventory release (res l.641), Rs 6.78 Cr provisions build (res l.649)"
loop_back_to: "A2"
gap: "A2: add T57 Gaurav question (call l.792-794) to concall question ledger, count 24 -> 25. A3: review presentation R222 (deck l.369) and concall R244/R065 (call l.352-356). A4: C1 reconcile Saudi funding-gap flag 14 / QB20 / 6D 5b with deck l.369 ~USD 30 Mn and state Unimech's remaining 51% commitment Rs 39.4-108.2 Cr vs net cash Rs 65.45 Cr; M2 carry utilisation qualifier into 6B item 4 and concall watchlist; M3 replace OI 'composition ND' with H1 CF items (res l.628-638) and list lease-modification and FX gains as one-offs; M4 state Hobel price/PAT NOT FOUND and EV/EBITDA ~5.6-7.0x, graft peak-year/concentration bear reading, order cover and Rs 450 vs Rs 425.00 Cr reconciliation into 6D trigger 1 and flag 4; M5 state Honeywell LTA effective 1-Apr-2026 (lta l.44) in 3A and 6C(d); correct 0C '24 question turns' to 25."
style_notes:
  - "S1 ETR rounding 27.57 vs 27.56"
  - "S2 SC-gap PAT basis mixed in H1 FY27"
  - "S3 relabel three brief inferences from FILED to INFERENCE"
  - "S4 keep equity-raise hedge in brief"
  - "S5 acknowledge press-release M01-M05"
  - "S6 call start-time inconsistency (~4 min)"
  - "S7 label CCC vs management WC-days basis"
  - "S8 Dheya CDR date reading ambiguous"
  - "S9 quantify CFO inventory release and provisions build"
analyst_note: "Arithmetic is clean. I recomputed every derived-metric group from lakh lines and found no mismatch beyond rounding. The brief gate passes. The failures are coverage and adversarial. A2 missed one analyst question inside T57. A4 already reviews it as Q22a, so A2's fix is one row and A4's 0C count goes from 24 to 25. A4's Saudi funding-gap flag uses an unanchored SAR 60M equity figure. It never cites the filed deck's ~USD 30 Mn joint investment, which is Rs 289 Cr at A4's own filed FX, above the capex. The real bear runs the other way: Unimech's remaining 51% commitment is Rs 39-108 Cr against Rs 65 Cr net cash. The 65% utilisation includes qualification capacity. Other income now rests on market gains and one-offs, because H1 interest fell to Rs 3.69 Cr. Hobel price/PAT is NOT FOUND, and EV/EBITDA of about 5.6-7.0x for a >50% margin asset raises the peak-year question that A4 never asks. The Honeywell LTA runs from 1-Apr-2026, 208 days before the intimation. All of it fits one remediation cycle."
```
