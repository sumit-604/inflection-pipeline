# A5 ADVERSARY / COMPLETENESS AUDIT: RAYMOND REALTY LIMITED (RAYMONDREL), Q2 FY27

Agent A5 | model claude-opus-5-5 | run date 28-Oct-2026 | fresh context.

Inputs read: the A4 review (`work/review_raymondrel_q2fy27.md`), the four A1 fulltexts and four A1 structured files (`extracted/`), and the three A2 ledgers (`work/ledger_*`). I opened no source PDF, nothing under `inputs/`, and no A3 file.

Anchor key: `RES L###` results fulltext; `PRE l###` presentation fulltext; `CC L###` concall fulltext; `CA L###` corporate-action fulltext; `R###` an A1 row in the named structured file; `REV L###` a line of the A4 review; `[DER]` = my arithmetic on anchored figures.

File status: the initial audit (loop 0) follows verbatim. The re-audit for correction loop 1 is appended at the end. **The final verdict is the last YAML block in this file.**

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Location | Content check | Status |
|---|---|---|---|
| (1) Summary narrative | REV L940-941 | About 218 words of prose with provenance tags. Inside the 200-400 word band. | PRESENT |
| (2) Sector intelligence | REV L943-944 | Demand by ticket size, rates, cost inflation, AIF funding route, no-peer caveat | PRESENT |
| (3) Business-model intelligence | REV L946-947 | Two engines, Thane plateau, JDA revenue vs cash, ICICI 60% share | PRESENT |
| (4) Competition intelligence | REV L949-950 | Brand and JDA speed, Sunteck comparison (prior Notion), partner terms watch | PRESENT |
| (5) Forward map | REV L952-962 | Make-or-break reading named; 9 dated catalysts, each with a bull fork and a bear fork | PRESENT |

**Gate result: PASS.** All five parts exist and carry real content.

---

## 1. COVERAGE AUDIT

Method: I re-counted each category from the A1 fulltext (the spine) and the A1 structured headers. I then diffed against the A2 ledgers and tested the A4 preamble (REV L16-27).

| Document | Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | Structured IDs | 874 | 874 (grep of `R### \|` rows; header 698+50+12+39+75) | none | PASS |
| Results | Notes | 13 | 13 (standalone 1-5 RES L309-327; consolidated 1-5 RES L601-620; CF method notes RES L305, L597; asterisk RES L303) | none | PASS |
| Results | Statement line items | 184 | 184 (standalone P&L 23, BS 36, CF 36; consolidated P&L 23, BS 35, CF 31) | none | PASS |
| Results | Zero-standing | 23 items / 48 cells | 23 items / 48 cells (P&L OCI rows 6 x 5 cells; RES L268 2 cells; 16 single cells) | none | PASS |
| Results | Board agenda items | 3 | 3 (RES L60-66) | none | PASS |
| Results | Auditor paragraph rows | 13 (11 paras + 2 letterheads) | 13 | none | PASS |
| Results | Consolidated subsidiaries | 7 | 7 (RES L444-450) | none | PASS |
| Results | Fulltext units absent from structured | M1-M4 (UDINs, firm reg nos, place lines) | same; no further gap found | n/a | PASS (non-numeric, logged by A2) |
| Presentation | Slides | 46 | 46 (`[page 1]`-`[page 46]`) | none | PASS |
| Presentation | Structured IDs | 1,082 | 1,082 (grep; header 860+98+29+49+46) | none | PASS |
| Presentation | Zero-standing tags | 47 | 47 (grep `[ZERO_STANDING]`) | none | PASS |
| Presentation | Fulltext units absent from structured | M1 (phone, PRE l53) | same | n/a | PASS |
| Concall | Structured IDs | 320 | 320 (grep) | none | PASS |
| Concall | Turns | 16 | 16 (operator CC L21; host L28; MD L35; operator Q&A L184; Q1-Q10 at L191, L226, L250, L268, L330, L371, L391, L456, L533, L551; operator close L611; final L617) | none | PASS |
| Concall | Analyst questions | 10 | 10 | none | PASS |
| Concall | Management numbers | 145 | 145 (spot-walked every digit-bearing line CC L43-L606; each maps to an A1 row) | none | PASS |
| Concall | Forward rows | 59 | 59 | none | PASS |
| Concall | Line and turn attribution | line 0, all T3(R307) | A1 anchors vary (see C2) | n/a | CONTRADICTION (C2) |
| Corp action | Structured IDs | no ledger by design | 63 (grep; header 23+15+4+6+15) | n/a | n/a |

Orphan test. The A4 preamble marks every ledger unit as reviewed (REV L16-20: "All 13 / 16 / 46 reviewed"; 874, 1,082 and 320 IDs; CA 63 rows). The 81 A3 findings map fully: 70 FORWARD-SIGNAL and AMBIGUOUS findings to Q1-Q25, and 11 confirmatory findings to the verdict (REV L524-528). I accept the blanket marking. One sampled "reviewed" set did hide an unsurfaced contradiction (deck p5 rows R037-R039 against p26 row R478; see C1). That is a forensic miss, not an orphan.

Result: **orphan_rows: none. missing_from_ledger: none.** Ledger defect C2 is logged below.

---

## 2. ARITHMETIC AUDIT

Statements in Rs Lakhs converted at ÷100 (RES L162, L461). Every metric below was recomputed from the raw extracted figures.

| # | Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|---|
| 1 | Consolidated Op EBITDA (PBT+D+Fin-OI), Q2 FY27 / Q2 FY26 | 106.27 / 92.42 | 66.32+5.39+43.53-8.97 = 106.27; 70.12+5.33+25.61-8.64 = 92.42 | RES L467, L475-479 | MATCH |
| 2 | Op EBITDA, Q1 FY27 / H1 FY27 / H1 FY26 / FY26 | 61.17 / 167.44 / 121.10 / 446.83 | same | RES L467-479 | MATCH |
| 3 | Op EBITDA margin, Q2 FY27 / Q2 FY26 / Q1 FY27 / H1 FY27 / FY26 | 14.20 / 13.26 / 11.61 / 13.13 / 14.94% | 14.197 / 13.257 / 11.614 / 13.131 / 14.940% | RES L466 | MATCH |
| 4 | Reported EBITDA / total income, Q2 FY27 / Q2 FY26 / Q1 FY27 / H1 FY27 / FY26 | 15.21 / 14.32 / 13.11 / 14.34 / 16.30% | 15.213 / 14.319 / 13.106 / 14.340 / 16.301% | RES L468 | MATCH |
| 5 | Consolidated ETR, Q2 FY27 / Q2 FY26 / Q1 FY27 / H1 FY27 / FY26 | 20.0 / 14.2 / 11.5 / 18.4 / 18.7% | 19.99 / 14.18 / 11.47 / 18.41 / 18.70% | RES L479, L483 | MATCH |
| 6 | Consolidated PAT margin and OI/PBT, all periods | as tabled REV L170-172 | all reproduce | RES L466-484 | MATCH |
| 7 | Standalone Op EBITDA, margins, ETR, OI/PBT, PAT margin | as tabled REV L179-185 | all reproduce (e.g. Q2 FY27 43.61, 15.58%; FY26 295.61, 18.30%) | RES L167-185 | MATCH |
| 8 | Standalone vs consolidated PAT gap, six periods | +27.7 / -49.1 / +3.0 / -2.1 / -10.1 / +15.9% | same | RES L185, L484 | MATCH |
| 9 | YoY: revenue / op EBITDA / finance / core PBT / PBT / PAT / EPS / EBIT | +7.4 / +15.0 / +70.0 / -6.7 / -5.4 / -11.8 / -11.8 / +15.8% | +7.37 / +14.99 / +69.97 / -6.72 / -5.42 / -11.83 / -11.84 / +15.83% | RES L466-496 | MATCH |
| 10 | Margin change YoY, operating / reported | +94 / +89 bps | +94.0 / +89.4 bps | derived | MATCH |
| 11 | Q2 PAT bridge | 6.81 + 7.04 - 0.06 - 17.92 + 0.33 - 3.32 = -7.12; tax volume +0.54, rate -3.86 | same | RES L466-484 | MATCH |
| 12 | H1 PAT bridge | 22.35 + 23.99 - 2.77 - 50.51 - 3.14 - 0.11 = -10.19 (-13.3%) | same | RES L466-484 | MATCH |
| 13 | Q1 FY26 derived (H1 - Q2): revenue / op margin / rep margin / core PBT | 379.35 / 7.56% / 10.51% / 8.94 | same | RES L466-479 | MATCH |
| 14 | H2 FY26 derived (FY - H1) | 1,914.29 / 17.02% / 18.19% / 255.59 | same | RES L466-479 | MATCH |
| 15 | H2 FY27 margin needed for 17% guide | 19.0% (331.3 on 1,746.2); 18.5% at TI x1.20 | 18.97%; 18.46% | RES L468, L479 | MATCH |
| 16 | CFO / capex / FCF / CFO-to-PAT, consolidated and standalone | -147.02 / 20.69 / -167.71 / -2.21x; standalone 142.38 / 2.10x | same | RES L574, L576, L277, L279 | MATCH |
| 17 | Working-capital change, consolidated / standalone | -291.20 / +85.22 (prior -407.01 / -24.81) | same | RES L569-571, L272-274 | MATCH |
| 18 | Receivable / inventory / payable days and CCC | 32.0 / 1,028 / 175 / 885 (prior 27.5 / 729 / 124 / 633); standalone 66.6 / 673 / 349 / 391 | same | RES L517, L520, L543-544, L471, L473 | MATCH |
| 19 | Gross debt / liquid funds / net debt, Sep-26 and Mar-26 | 1,219.73 / 303.58 / 916.15; 1,013.75 / 356.00 / 657.75 | same | RES L519-522, L535, L541 | MATCH |
| 20 | Gross and net D/E | 0.752 / 0.565 (prior 0.647 / 0.420) | 0.7519 / 0.5648 (0.6468 / 0.4196) | RES L531 | MATCH |
| 21 | Equity roll-forward | 1,555.63 vs 1,555.61 | same | RES L494, L530, L484, L585, L566 | MATCH |
| 22 | Interest paid share; borrowing gap | 94.5%; 5.40 | 85.75/90.70 = 94.54%; 205.98 - 200.58 = 5.40 | RES L475, L582-586 | MATCH |
| 23 | Subsidiary share of Q2 revenue and gross assets; subsidiary revenue QoQ | 63.0%; 72.7%; +63% | 471.34/748.52 = 62.97%; 5,752.08/7,911.48 = 72.71%; 471.34/288.70 = +63.3% | RES L394-412 | MATCH |
| 24 | Margin-stop matrix, basis C and D | 9.56 / 12.97%; 8.01 / 11.93% | same | PRE l365 (R315, R317) | MATCH |
| 25 | Net-debt readings R2 / R3 / R4 | 604 / 814 / 1,126 | same | derived | MATCH |
| 26 | TTM PAT / EPS / PE; book per share | 294.40 / 44.22 / 12.4x; 243.7 | same | RES L484, L531 | MATCH |
| 27 | FY27 run-rates: revenue / PAT / EPS | 3,543 / 264 / 39.7 | same | RES L466, L484 | MATCH |
| 28 | H1 ROCE (annualised EBIT / avg equity + gross debt) | 12.7% | 344.38 / 2,711.54 = 12.70% | RES L475, L479, L531, L535, L541 | MATCH |
| 29 | **FY26 ROCE "same basis"** (REV L378) | **18.4%** | **23.4%** on the same basis: EBIT 472.33 (RES L479 + L475) / avg of FY25 capital 1,459 (PRE R127) and Mar-26 capital 2,581.17. On closing capital only: 18.3%. Neither gives 18.4% | RES L475, L479, L531, L535, L541; PRE l180 R127 | **MISMATCH (F3)** |
| 30 | Guidance consistency | 594.6; TI 3,129-3,497; +3% to +15%; 16.3% | same | RES L468, L479 | MATCH |
| 31 | Guide-implied H2 FY27 pre-sales | ~2,026 vs 2,263 | 3,023 x 1.20 - 1,602 = 2,025.6; 3,023 - 760 = 2,263 | PRE R146, R244, R245 | MATCH |
| 32 | Collections / pre-sales, H1 FY27 vs H1 FY26 | 77.0% vs 103.0% | 76.97% vs 103.03% | PRE R244, R245, R250, R251 | MATCH |
| 33 | Ex-BKC Q2 revenue | 522 to 695, +33% | 697.15-175 = 522.15; 748.52-54 = 694.52; +33.0% | PRE R789, R791 | MATCH |
| 34 | FY27E revenue A / B; H2 needed for A | 3,589-3,600 / 3,260-3,543; 2,314 (+20.9%) | same | RES L466 | MATCH |
| 35 | **FY27E PAT Reading B** (REV L920) | **264-290** | Lower end 264 reproduces (seasonality). Upper end does not. The stated bridge (H2 at H2 FY26 PAT margin, less ~27 after-tax interest) on Reading B's own revenue range gives ~272-309: H2 revenue 1,984.81-2,267.81 x 11.7-11.9% less 27.1, plus H1 66.49. The figure 290 reproduces only with an unstated H2 revenue of 2,144 (H2 FY26 x 1.12). Also 11.7% is PAT / total income (227.91 / 1,941.77); A4 defines PAT margin on revenue (REV L172), which gives 11.9% | RES L466-468, L475, L484 | **MISMATCH (F2)** |
| 36 | Forward EPS and PE table, rows A and FY28 | as tabled REV L927-930 | all reproduce | derived | MATCH |
| 37 | FY28E revenue B | 3,651-3,968 | same | derived | MATCH |
| 38 | Credibility ratio and sensitivities | 50%; 62.5%; 55% | same | REV L650-654 | MATCH |
| 39 | Specificity (forward rows R206-R264) | 30 / 59 = 0.51 | 30 quantified by my row count | concall R206-R264 | MATCH |
| 40 | Opening claims quantified | 22 / 26 = 84.6% | same | CC L43-178 | MATCH |
| 41 | **Defensive-language total** (REV L781) | **15** | **16**: A4's own list has 16 instances (CC L346, L230, L547, L382, L124, L287, L290, L326, L292, L477, L608, L50, L376, L518, L409, L475). The hedge-heavy conclusion (>5) is unchanged | CC lines listed | **MISMATCH (F4)** |
| 42 | Cohort share of outflow (I-4) | 595 / 1,212 = 49% | 49.1% | PRE R342-R344 | MATCH |
| 43 | RRL share of ICICI project capital | 140 | 210 / 0.60 x 0.40 = 140 | CC L197-198 | MATCH |

Arithmetic result: the core tables (Steps 1-5, 6C matrix, Section C) recompute exactly. Three side figures fail: rows 29, 35, 41.

---

## 3. ADVERSARIAL READ (three most positive claims)

### Claim 1. "Operations improved: operating EBITDA +15.0% YoY, margin +94 bps" (REV L211-212, L227, L880, L941, analyst_note L1051)

**Strongest bear counter, from the same extract.** The +94 bps sits mostly in the classification of approval-linked interest. The press release names the Rs 17 Cr as "Interest to Government authorities: BMC/TMC / MHADA for Additional FSI and Approvals" (RES L717-719). Management describes approval costs that "get paid over a period of time", on which the authority charges interest (CC L104-109). That interest rose from Rs 10 Cr to Rs 17 Cr YoY (PRE l365, R316, R315). It sits in finance costs, below EBITDA. Treated as project cost:

| Basis | Q2 FY26 | Q2 FY27 | YoY |
|---|---|---|---|
| Op EBITDA, authority-adjusted | 92.42 - 10 = 82.42 (11.82%) | 106.27 - 17 = 89.27 (11.93%) | +8.3%; +10 bps [DER] |
| Reported (with OI), authority-adjusted | 101.06 - 10 = 91.06 (12.90% of TI) | 115.24 - 17 = 98.24 (12.97%) | +7.9%; +7 bps [DER] |
| H1 op EBITDA, authority-adjusted (16 to 36, R318, R317) | 105.10 (9.76%) | 131.44 (10.31%) | +25.1%; +55 bps vs +38.3%, +188 bps unadjusted [DER] |

Deck interest figures are rounded to whole crores, so growth is about 7.6-9.0%. The conclusion holds either way.

**Does it survive?** Yes. A4 built this exact basis (basis D, 11.93%; REV L418) for the margin stop. It never applied the basis to its headline YoY claim. **Graft into A4 (Step 2 table, Section C "Operations" row, brief summary, analyst_note):** "Authority-adjusted (interest to BMC/TMC/MHADA treated as approval cost, PRE l365): Q2 op EBITDA Rs 82.42 Cr to Rs 89.27 Cr, +8.3% YoY; margin 11.82% to 11.93%, +10 bps [DER]. Most of the reported +94 bps comes from where approval-linked interest is classified. Separating observation: the Q4 answer on principal owed to authorities and its balance-sheet line." Type: MISSING (M1).

### Claim 2. "Demand leg confirmed: pre-sales +98% Q2 / +111% H1; collections +67%; BD target FIRED" (REV L355, L386, L389, L435, L879, L887)

**Strongest bear counter, from the same extract.**
1. Management did not raise the FY27 guide of at least 20% pre-sales growth after H1 grew 111% (RES L723; PRE l170). On FY26 pre-sales of Rs 3,023 Cr (R146), the guide implies H2 FY27 pre-sales of about Rs 2,026 Cr against Rs 2,263 Cr in H2 FY26, a fall of about 10.5% [DER]. A4 computes this itself (REV L628) but does not carry it into Section C ("Demand: Strong", REV L879), the protocol verdict ("demand leg confirmed", REV L887) or the brief.
2. At RRL's economic interest, Q2 pre-sales grew about 81%, not 98% [DER]. Q2 FY27 JDA bookings were Bandra 85, BKC 123, Wadala 264 and Sion 46 (R760, R783, R806, R829), a total of 518 (57.4% of 902, matching the press release's 57%). Q2 FY26 had only Bandra 194 (R758; BKC, Wadala and Sion zero: R781, R804, R827). With Bandra at 91% (R441) and Wadala at 62% (R467), Q2 FY27 is about Rs 794 Cr against about Rs 438 Cr.
3. The BD trigger "FIRED" (REV L435) and checklist #5 GREEN (REV L389) rest on gross GDV. The H1 addition of about Rs 8,500 Cr (CC L72-74) equals Parel's listed GDV of Rs 8,500 Cr, and Parel's economic interest is 55% (R491, R493) [INFERENCE that the addition is Parel]. At RRL's share that is about Rs 4,675 Cr [DER]. That is below the Rs 5,000 Cr green line and below the Rs 8,000 Cr trigger. The separating observation is A4's own Q14 (which JDAs make up the GDV rise).
4. Luxury velocity is weak. Invictus Tower B (Thane) bookings ran 5, 2, 0 (PRE l607). BKC upper floors wait on an aviation approval (CC L517-522). Management expects Thane to stabilise at Rs 1,500-1,600 Cr a year (CC L439). A4 records these elsewhere (Q9, Q10, Step 5A).

**Does it survive?** Yes, points 1-3. Point 4 is already in A4. **Graft into A4 (Section C Demand row, protocol verdict line, 6B #5, 6D trigger 5, brief summary):** the guide-implied H2 decline; the economic-interest growth of about 81%; and the BD status written as "FIRED on gross GDV; not fired at economic interest if the H1 addition is Parel (about Rs 4,675 Cr at 55%)". Type: MISSING (M3).

### Claim 3. "ICICI AIF partnership: a funding positive that answers an earlier gap" (REV L825, L858, L870, L950) — includes the MANDATORY ACQUISITION-ECONOMICS PROBE

The filing describes a stake purchase. ICICI Prudential Real Estate Development Fund invests up to Rs 210 Cr in Ten X Realty West Limited (CA L42-50, L130).

**Purchase-economics probe.**
- Multiple: **Rs 210 Cr consideration / TXRWL PAT = NOT COMPUTABLE.** The filing discloses no TXRWL earnings, ROCE, debt, cash or customer data (CA R063 absence note). The funded project is pre-launch (Mahim launches Q3 and Q4 FY27, PRE l460-461), so trailing earnings are nil. No earnings multiple can be stated or stress-tested.
- What the extract does price: ICICI supplies 60% of project capital and takes 60% of residual profit after an execution fee of about 5% of project turnover paid to RRL (CC L194-201). Implied project peak equity is 210 / 0.60 = Rs 350 Cr, with RRL's share Rs 140 Cr [DER]. The coupon is "virtually zero" (CC L584-587). ICICI therefore earns the project's equity return, not a debt return. Management puts project IRR at 20-25% (CC L468-469), against a 9.6% cost of debt (RES L716). Management also says "equity anyway is available at a higher rate" (CC L469-470). The deal lowers reported net debt only if the instrument is classified as equity. It does not lower the cost of capital on that project. It also transfers 60% of the residual profit at par capital. The extract shows no premium paid for RRL's JDA rights, approvals or brand beyond the 5% fee.
- Parties: RRL is itself a named party to the Investment Agreement, as counterparty 3 (CA L44, L121-123). A4's term table (REV L67-85) lists only the issuer and the investor. Item (f) states "No restriction or liability imposed" on RRL (CA L144). The instrument terms (put, redemption, ratio) are NOT DISCLOSED (R063). The filing does not say why the parent signed.

**Does it survive?** Partly. A4 already grafts NCI, fee elimination, undisclosed terms and the "has raised" overstatement. Two items survive and are absent: (a) RRL is a signatory; (b) the capital is priced like equity (20-25% project IRR against 9.6% debt), so "funding positive" holds for leverage but not for cost of capital. **Graft into A4 (0C term table, Section C "Capital" row, 8E "undisclosed material positive" line):** "RRL is a party to the agreement (CA L121-123). Price / TXRWL PAT is not computable (earnings NOT DISCLOSED; pre-launch). ICICI's 60% residual-profit share at a near-zero coupon prices the money at the project equity return management cites (IRR 20-25%, CC L468-469), against 9.6% debt (RES L716). Positive for net debt; not cheaper capital." Type: MISSING (M4).

---

## FINDINGS (every finding typed)

### FACTUAL
- **F1 (A4).** A4 misreads a deck line. Step 5 (REV L316), Q5 (REV L495) and YAML q5 (REV L995) treat a Rs 26 Cr deck line as "finance cost 26". The deck line is "Finance, Legal & IT Cost (26)" (PRE l401; R363), a corporate-cost line, not interest. The deck cash format (R361-R367) has no interest line. Q5's premise therefore misstates the deck. Fix: relabel the line. Re-pose Q5 as: "Where does the Rs 85.75 Cr interest paid (RES L586) sit in the deck's cash format, and how does the Rs 155 Cr bank-loan line (R366) reconcile to Rs 200.58 Cr net borrowing (RES L582-584)?"
- **F2 (A4).** The upper bound of FY27E PAT Reading B ("264-290", REV L920) does not reproduce from the stated basis (arithmetic row 35). On Reading B's own revenue range, the stated bridge gives about Rs 272-309 Cr, so the top end sits above the Notion bear of Rs 300 Cr. The figure 290 needs an unstated H2 revenue of Rs 2,144 Cr. The margin base also mixes total income (11.7%) with A4's revenue-based PAT-margin definition (11.9%). Fix: state the H2 input, or widen B to about 264-309. Re-derive the FY27E B row of the PE table (REV L928): basic PE becomes about 11.8-13.8x.
- **F3 (A4).** The FY26 ROCE "same basis" figure of 18.4% (REV L378) does not reproduce (arithmetic row 29). On the H1 method it is 23.4%, using deck FY25 capital of 1,459 (PRE R127). On closing capital it is 18.3%. Fix the figure and cite the denominator.
- **F4 (A4).** The defensive-language total says 15, but A4's own list has 16 instances (REV L781; arithmetic row 41). The conclusion is unchanged. Fix the count.

### MISSING
- **M1 (A4).** Claim 1 counter. The headline op EBITDA +15.0% / +94 bps carries no authority-adjusted qualifier. On that basis the figures are +8.3% / +10 bps. Graft text is in Section 3, Claim 1.
- **M2 (A4).** The GST qualifier is missing from collections. The deck states "Amount Collected also includes GST Amount" (PRE l149) and "Collections Till date: Includes GST and Other Possession Charges" (PRE l444). A4 sets GST-inclusive collections (JDA Rs 857 Cr; Thane Rs 7,977 Cr) against GST-exclusive revenue (Rs 2,549 Cr) without the qualifier (REV L320, L431, L947, L1040). The revenue-to-cash gap is therefore wider than shown; the GST amount is NOT DISCLOSED. Graft the qualifier at each site.
- **M3 (A4).** Claim 2 counter. Section C, the verdict line, 6B #5, 6D trigger 5 and the brief omit three points: the guide-implied H2 pre-sales decline of about 10.5%; economic-interest Q2 growth of about 81%; and BD of about Rs 4,675 Cr at RRL's share if the addition is Parel. Graft text is in Section 3, Claim 2.
- **M4 (A4).** Claim 3 counter and acquisition probe. Two items are missing: RRL is a party to the agreement, and the capital is equity-priced (20-25% project IRR against 9.6% debt). The price / PAT multiple is not computable. Graft text is in Section 3, Claim 3.

### CONTRADICTION
- **C1 (A4).** The deck contradicts itself on JDA revenue, and A4 surfaced only one side. Deck p5 states revenue recognised to date of Rs 9,500 Cr in total: owned land Rs 7,570 Cr, JDAs Rs 1,930 Cr (R037-R039; A1's render check confirms the row mapping, structured header line 8). The project table and project slides give a total of Rs 10,078 Cr (R478), and the JDA projects sum to Rs 2,549 Cr: Bandra 1,345 (R769), BKC 577 (R792), Wadala 385 (R815), Sion 242 (R838). Owned land agrees within Rs 41 Cr (7,570 vs 7,529). The whole gap, Rs 619 Cr, sits in JDAs. p5 ties revenue to sold units: JDA sold 3,430 = recognised 1,930 + balance 1,500 (R036, R039, R042). A4 uses 2,549 throughout (REV L320, L947, L1040) and never cites the p5 figure. [INFERENCE] The Rs 619 Cr may be the revenue not tied to unit sales (landowner share) that A4 calls the biggest open risk (analyst_note, REV L1051), so it is the number Q1 needs. Graft: cite both figures in Step 5, Q1, the business-model brief and the flag. Ask management in Q1 to reconcile p5 Rs 1,930 Cr with p26 Rs 2,549 Cr.
- **C2 (A2, annotation repair only).** The concall ledger's line and turn columns contradict A1. Sections 4 and 7 list every management number (R001-R145) and every forward row (R206-R264) at "line 0" and turn "T3(R307)". Sections 5, 6 and 8 leave lines blank. The ledger header says "Line = fulltext line". A1 anchors differ, for example: R069 at line 208 (Q1 turn R309); R113 at line 409 (Q7 turn R315); R241 at line 377 (Q6 turn R314); R198 at line 584 (Q10 turn R318). IDs and counts are complete, and no A4 number depends on this column, because A4 cites CC lines directly. Fix: re-map mechanically from the A1 `line` field and the R305-R320 turn spans. This item needs no A3 or A4 re-run.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**.

Gap: (C1) surface the deck p5 vs p26 JDA revenue contradiction (Rs 1,930 Cr vs Rs 2,549 Cr; Rs 619 Cr) in Step 5, Q1, the brief and the flags. (M1) add the authority-adjusted YoY qualifier: op EBITDA +8.3%, margin +10 bps. (M2) add the GST-inclusive qualifier on collections. (M3) qualify the demand verdict: guide-implied H2 -10.5%, economic-interest growth about +81%, BD about Rs 4,675 Cr at economic interest if Parel. (M4) add RRL's party status and the equity-priced cost of the ICICI capital. (F1) relabel deck R363 and re-pose Q5. (F2) fix the FY27E PAT B range and its PE row. (F3) fix FY26 ROCE (23.4% same basis). (F4) fix the hedge count to 16. Separately, A2 should repair the concall ledger's line and turn columns (C2, annotation only; no chain re-run).

Finding types that drive the loop: FACTUAL x4, MISSING x4, CONTRADICTION x2.

---

## STYLE NOTES (logged; no re-run)

- **S1.** Q20 (REV L510) and watchlist #7 (REV L391) omit the deck's own gloss: "Board Independence : 100% i.e. All the Board Committees are chaired by Independent Director" (PRE l218-220; R1047). Quote the gloss so the question is fair. The status (GREEN, drafting point) is unchanged.
- **S2.** "Call 28-Oct-2026 11:30 IST (CA header; CC L19)" (REV L567). The 11:30 IST time appears in the concall fulltext header (line 14). CC L19 gives the transcript production time (10:59 IST). Correct the cite.
- **S3.** "Other current liabilities (customer-advance line)" and "customer advances funded 67%" (REV L314, L320). The statement line is "Other current liabilities" (RES L546), and its composition is not disclosed. Tag the label [INFERENCE].
- **S4.** The Step 3 "One-offs flagged" column lists Q1 FY27 authority interest of Rs 19 Cr (REV L247). It is recurring (Q2 17, H1 36; PRE l365). Move it to the run-rate note.
- **S5.** "Dilution at listed level: None: no RRL securities in the agreement (CA L170-180)" (REV L76). CA item (i) says no securities have been issued yet; it does not exclude RRL securities. Cite the issuer line instead (TXRWL as "Issuer", CA L101).
- **S6.** The results ledger count test says auditor_paras 11, while section 5 lists 13 rows (11 paragraphs + 2 letterheads). A4's "13 rows" matches the section. This is a count-test label only.

---

Initial audit block (loop 0). **Superseded** by the re-audit block at the end of this file.

```yaml
stage: A5-adversary
company: "RAYMONDREL"
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
  - {metric: "FY26 ROCE 'same basis' as H1 (EBIT / avg equity + gross debt)", a4_value: "18.4%", recomputed: "23.4% same basis (472.33 / avg of FY25 1,459 and Mar-26 2,581.17); 18.3% on closing capital", source_line: "RES L475, L479, L531, L535, L541; PRE l180 R127; REV L378"}
  - {metric: "FY27E PAT Reading B upper bound", a4_value: "290", recomputed: "~304-309 on Reading B top revenue 3,543 via the stated bridge; 290 needs unstated H2 revenue 2,144 (H2 FY26 x 1.12)", source_line: "RES L466-468, L475, L484; REV L920, L928"}
  - {metric: "Defensive-language total", a4_value: "15", recomputed: "16 (A4's own enumerated instances)", source_line: "CC L50, L124, L230, L287, L290, L292, L326, L346, L376, L382, L409, L475, L477, L518, L547, L608; REV L781"}
surviving_bear_counters:
  - {claim: "Operations improved: op EBITDA +15.0% YoY, margin +94 bps", counter: "Authority interest for FSI/approvals rose 10 to 17 and sits below EBITDA; authority-adjusted op EBITDA 82.42 to 89.27 (+8.3%), margin 11.82% to 11.93% (+10 bps)", source_line: "PRE l365 R315-R316; RES L717-719; CC L104-109; RES L466-479", type: "MISSING"}
  - {claim: "Demand leg confirmed: pre-sales +98%/+111%; BD Rs 8,000 Cr target FIRED", counter: "Unchanged >=20% guide implies H2 FY27 pre-sales ~2,026 vs 2,263 (-10.5%); at economic interest Q2 growth ~+81%; H1 BD 8,500 equals Parel GDV at 55% EI = ~4,675, below the 5,000 green line [INFERENCE]", source_line: "PRE R146, R244-R245, R441, R467, R491, R493, R758, R760, R783, R806, R829; CC L72-74; RES L723", type: "MISSING"}
  - {claim: "ICICI AIF partnership is a funding positive (acquisition-economics probe)", counter: "Price / TXRWL PAT not computable (earnings NOT DISCLOSED, pre-launch); 60% residual profit at near-zero coupon prices the money at project IRR 20-25% vs 9.6% debt; RRL is itself a party to the agreement", source_line: "CA L44, L121-123, L130, L144, R063; CC L194-201, L468-470, L584-587; RES L716", type: "MISSING"}
findings_by_type:
  factual:
    - "F1 (A4): deck R363 is 'Finance, Legal & IT Cost (26)' (PRE l401), not interest; Step 5 REV L316, Q5 REV L495 and YAML q5 misread it as finance cost; re-pose Q5"
    - "F2 (A4): FY27E PAT Reading B 264-290 upper bound not reproducible; stated bridge on Reading B revenue gives ~272-309; fix range and PE row"
    - "F3 (A4): FY26 ROCE 'same basis' 18.4% should be 23.4% (avg capital, FY25 1,459 PRE R127) or 18.3% (closing)"
    - "F4 (A4): defensive-language total 15 should be 16"
  missing:
    - "M1 (A4): authority-adjusted YoY qualifier absent from the op EBITDA +15% / +94 bps headline (+8.3% / +10 bps)"
    - "M2 (A4): collections to date include GST and possession charges (PRE l149, l444); JDA 857 vs revenue 2,549 compares unlike bases"
    - "M3 (A4): demand verdict lacks guide-implied H2 -10.5%, economic-interest growth ~+81%, and BD ~4,675 at EI if Parel"
    - "M4 (A4): ICICI term table and Capital row lack RRL party status (CA L121-123) and the equity-priced cost (IRR 20-25% vs 9.6% debt)"
  contradiction:
    - "C1 (A4): deck p5 JDA revenue recognised 1,930 (R039; total 9,500 R037) vs project slides 2,549 (R769, R792, R815, R838; total 10,078 R478); Rs 619 Cr gap unsurfaced; A4 uses 2,549 only"
    - "C2 (A2, annotation only): concall ledger puts all R001-R145 and R206-R264 at line 0 and turn T3(R307), contradicting A1 anchors; IDs and counts complete; no A3/A4 re-run needed"
  style:
    - "S1: Q20 omits the deck gloss 'i.e. All the Board Committees are chaired by Independent Director' (PRE l218-220)"
    - "S2: 11:30 IST call time cited to CA header and CC L19; it sits in the concall fulltext header"
    - "S3: 'customer-advance line' for Other current liabilities (RES L546) should carry [INFERENCE]"
    - "S4: Q1 FY27 authority interest listed as a one-off in Step 3; it recurs"
    - "S5: 'no RRL securities in the agreement' cites CA L170-180, which only says none issued yet"
    - "S6: results ledger count test says auditor_paras 11 vs 13 rows in section 5 (label only)"
loop_back_to: "A4"
gap: "C1 surface deck p5 JDA revenue 1,930 vs p26 2,549 (Rs 619 Cr) in Step 5, Q1, brief, flags; M1 authority-adjusted YoY (+8.3%, +10 bps); M2 GST-inclusive collections qualifier; M3 demand verdict qualifiers (H2 -10.5%, EI +81%, BD ~4,675 at EI); M4 ICICI: RRL a party, equity-priced capital, multiple not computable; F1 relabel R363 and re-pose Q5; F2 fix FY27E PAT B range and PE row; F3 FY26 ROCE 23.4%; F4 hedge count 16. Separately A2 repairs concall ledger line/turn columns (C2, annotation only)."
style_notes:
  - "S1 Q20 deck gloss"
  - "S2 call-time cite"
  - "S3 customer-advance label as inference"
  - "S4 authority interest not a one-off"
  - "S5 CA dilution cite"
  - "S6 results ledger auditor_paras label"
analyst_note: "All five brief parts are present, and every ledger ID ties: 874, 1,082 and 320, plus 63 corporate-action rows. A4's core tables recompute exactly. Three side figures fail: FY26 ROCE, the FY27E PAT B upper bound and a hedge count. The verdict turns on completeness. The largest gap: deck p5 states JDA revenue recognised of Rs 1,930 Cr, while the project slides sum to Rs 2,549 Cr. A4 used only 2,549. The Rs 619 Cr difference may be the non-sale revenue A4 names as its biggest open risk, so Q1 should cite it. Second, the 'operations improved' claim (+15%, +94 bps) shrinks to +8.3% and +10 bps if approval-linked authority interest counts as project cost. A4 used that basis for the stop test but not for the YoY claim. Third, the demand and BD readings rest on gross figures. At economic interest, Q2 pre-sales rose about 81%, and H1 BD may be about Rs 4,675 Cr if the addition is Parel. ICICI money is priced like project equity, and RRL signed the agreement. The concall ledger's line and turn columns are wrong, but no downstream number uses them."
```

---

## RE-AUDIT: CORRECTION LOOP 1 OF 1 (28-Oct-2026)

Inputs re-read:
- The rewritten A4 review, 1,087 lines, with its change log at REV L1065-1086.
- `work/blocks/a4-review.yaml`.
- The repaired concall ledger (`work/ledger_concall_raymondrel_q2fy27.md`).
- `work/blocks/a2-concall.yaml`.

The A1 fulltexts and structured files are unchanged, and I did not open `inputs/`. In this section, `REV L###` means a line of the **rewritten** review.

### R1. Closure of every looping item

| Item | Type | What I checked | Evidence in the rewritten review | Status |
|---|---|---|---|---|
| F1 | FACTUAL | Deck R363 is relabelled as a corporate-cost line, and Q5 is re-posed on interest paid and bank-loan reconciliation | REV L320; Q5 L499; YAML q5 L1001. A grep for "finance cost 26" and "finance 26" finds nothing in the review or the A4 block | CLOSED |
| F2 | FACTUAL | FY27E PAT Reading B is now 264-309 with the H2 inputs stated. My recompute: 1,984.81-2,267.81 x 11.906% - 27.09 + 66.49 = 275.7-309.4. PE row B: EPS 39.66-46.41 / 35.82-41.93, PE 11.81-13.82x / 13.07-15.30x | REV L924, L934; dependent lines L379-380, L384, L458, L470, L928, flag L1045. No "264-290" remains in the review or the A4 block | CLOSED |
| F3 | FACTUAL | FY26 ROCE on the same basis is 23.4% (472.33 / avg of 1,459 and 2,581.17), and 18.3% on closing capital | REV L382, L452 | CLOSED |
| F4 | FACTUAL | Hedge total now reads 16 against 16 listed instances | REV L785 | CLOSED |
| M1 | MISSING | Q2: 82.42 to 89.27, +8.3%, +10 bps. H1: 105.10 to 131.44, +25.1%, 9.763% to 10.307% = +54 bps. A4's +54 is exact; my loop-0 "+55" came from rounded margins | REV L215-216, L230, L807, L884, L553, L947, flag L1042, analyst_note L1059 | CLOSED |
| M2 | MISSING | The GST and possession-charge qualifier cites PRE l149 and l444, with the GST amount NOT DISCLOSED. The I-2 row correctly notes the press-release collections basis is not stated | REV L324, L400, L435, Q1 L495, Q24 L518, L953, flag L1047 | CLOSED |
| M3 | MISSING | Economic-interest Q2 bookings about 794 vs 438 (+81%); guide-implied H2 about 2,026 vs 2,263 (-10.5%); BD about 4,675 at economic interest if Parel, tagged [INFERENCE] with Q14 as the separating observation | REV L883, L891, L393, L439, L632, L648, L828, L836, Q14 L508, L947, flag L1048 | CLOSED |
| M4 | MISSING | New Parties row (CA L44, L95-123) and Price / economics row (multiple NOT COMPUTABLE; equity-priced at 20-25% IRR vs 9.6% debt) | REV L72, L78, L338, L862, L874, L888, Q2 L496, L956, flag L1050 | CLOSED |
| C1 | CONTRADICTION | p5 1,930 / 9,500 (R037-R039) against project rows 2,549 / 10,078 (R446, R454, R464, R472, R478). The gap is Rs 619 Cr, all in JDAs; owned land agrees within Rs 41 Cr. The Rs 619 Cr now leads Q1 and the top-3 list. Project-row IDs differ from my slide-level IDs (R769, R792, R815, R838); both carry the same values | REV L324, Q1 L495, L522, L761, L861, L884, L553, L953, flag L1047, analyst_note L1059, YAML q1 L997 | CLOSED |
| C2 | CONTRADICTION | Ledger sections 4-8 are rebuilt from A1 anchors, with no "line 0" and no blank anchors left. Turn spans tie to R305-R320 starts: R069 L208 in T5 R309; R113 L409 in T11 R315; R138 L518 in T12 R316; R145 L597 in T14 R318; R264 L615 in T15-16. DRIFT marks are verified against the fulltext: R009 L58, R037 L99, R054 L142, R092 L340, R130 L492, R142 L540. The A2 block counts 10 DRIFT rows and the ledger has 10. IDs are unchanged at 320/320 and gate_a2 passes | ledger L74-L400; `blocks/a2-concall.yaml` L25 | CLOSED |

The loop-0 style items S1-S5 are also closed:
- S1: REV L395, L514, YAML q20 L1016.
- S2: REV L571.
- S3: REV L304, L318, L324, L804.
- S4: REV L251.
- S5: REV L77.

S6 (the results ledger count-test label) stays open as a style note only.

### R2. Drift check outside the patched points

I re-read the rewritten review from L1 to L1061 against my loop-0 arithmetic table. Every unpatched figure equals its loop-0 value. That covers:
- Steps 1A-1D, 3 and 4.
- The Step 5 table and Pending ruling 2.
- The 6C matrix and Step 6.5.
- Role 5 Steps 0-4 and 6-7.
- Forward Reading A and the FY28 rows.
- Monitorables M1-M18.

The verdict lines are unchanged: PROCEED WITH FLAGS; INDETERMINATE-WITH-DIRECTION; credibility 50% and grade C; OVERPROMISER provisional; Decision Status untouched.

The 3A BD row is now scored DELIVERED "on the gross basis the commitment used", with the economic-interest qualifier attached (REV L648). That matches 6D (REV L439) and leaves the credibility ratio at 2.5 / 5.

The A4 block (`blocks/a4-review.yaml`) carries the patched values, and a grep finds no stale figure: no "264-290", "Total 15", "finance cost 26" or unqualified "2,549 vs 857".

### R3. Deliverable gate re-run

All five brief parts are present (REV L946-968). The summary is now about 290 words, inside the 200-400 band. The forward map is unchanged: 9 dated catalysts, each with a bull fork and a bear fork. **PASS.**

### R4. New style notes (logged; no re-run)

- **S7.** The concall ledger labels every opening row "T3-4 R307 MD remarks (R305-R306 opening)" (ledger L76-L138, L290-L308). All those lines (CC L43-L177) sit inside T3 (R307, CC L35-L183). T4 (R308) is the operator's Q&A opener and carries no numbers. This is a label only.
- **S8.** The Section C Demand row cites "R758-R829" as a range (REV L883). The rows that matter are R441, R467, R758, R760, R783, R806 and R829. This is a cite form only.

### R5. Re-audit verdict

**COMPLETE.** All four FACTUAL, four MISSING and two CONTRADICTION items from loop 0 are closed. No new factual, missing or contradiction finding arose in the re-read. The open items are three style notes (S6, S7, S8), and none of them loops. The review can proceed to Notion save through the operator-approval gate. Decision Status is not written.

---

Final audit block (re-audit, correction loop 1 of 1). **This block governs.**

```yaml
stage: A5-adversary
company: "RAYMONDREL"
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
    - "S6 (A2 results ledger, open from loop 0): count test says auditor_paras 11 vs 13 rows in section 5 (label only)"
    - "S7 (A2 concall ledger): opening rows labelled 'T3-4 R307'; lines CC L43-L177 sit wholly in T3 (R307); label only"
    - "S8 (A4 review REV L883): Section C Demand row cites 'R758-R829' as a range; operative rows are R441, R467, R758, R760, R783, R806, R829"
loop_back_to: ""
gap: ""
style_notes:
  - "S6 results ledger auditor_paras label"
  - "S7 concall ledger T3-4 label for opening rows"
  - "S8 Section C demand row range cite"
analyst_note: "Loop 1 closed all ten looping items. F1-F4: deck line R363 is relabelled and Q5 re-posed; FY27E PAT B now reads 264-309 with the H2 inputs stated and the PE row re-derived; FY26 ROCE reads 23.4% on the H1 basis; the hedge count reads 16. M1-M4: the authority-adjusted YoY (+8.3%, +10 bps), the GST qualifier on collections, the demand qualifiers (about +81% at economic interest, guide-implied H2 about -10.5%, BD about Rs 4,675 Cr if Parel) and the ICICI economics (RRL a party, equity-priced capital, multiple not computable) now sit in the steps, the combined verdict, the brief and the flags. C1: the deck p5 vs p26 JDA revenue gap of Rs 619 Cr is surfaced and leads Q1. C2: A2 rebuilt the concall ledger line and turn columns from A1 anchors; my spot checks tie. A full re-read found no drift: every unpatched number matches its loop-0 recompute, and the verdict lines are unchanged. The three surviving bear counters from loop 0 are now grafted. Three style notes remain; none loops."
```
