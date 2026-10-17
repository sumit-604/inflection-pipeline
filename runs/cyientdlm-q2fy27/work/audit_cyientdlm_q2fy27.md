# A5 ADVERSARY / COMPLETENESS AUDIT: Cyient DLM Ltd (CYIENTDLM) | Q2 FY27

Agent: A5 adversary | Model: claude-opus-5-5 | Run date: 2026-10-17
Review under audit: work/review_cyientdlm_q2fy27.md (A4). Cited as "rev L###".
Inputs read: A1 fulltexts (res, pres, pr), A1 structured (3), A2 ledgers (3), A4 review. No source PDF, nothing under inputs/, no A3 file opened.
Anchors: "res L###" = results fulltext line; "pres L###" = presentation fulltext line; "pr L###" = press release fulltext line. All recomputation runs on the Rs Mn source values (res L534-L565 image transcription for page 2; res L135-L262 for the balance sheet and cash flow). Rs Cr = Rs Mn x 0.1.

---

## AUDIT 0: DELIVERABLE-COMPLETENESS (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT (rev L590-L603, 13 lines, inside the 10-20 line band) | sector PRESENT (rev L605-L611) | business model PRESENT (rev L613-L621) | competition PRESENT (rev L623-L628) | forward map PRESENT (rev L630-L643; 9 dated rows, each with a bull fork and a bear fork, plus a named make-or-break reading at L631). Gate: PASS.

---

## AUDIT 1: COVERAGE

Fresh pass method: grep of A1 fulltexts for page markers, note headers, numbered items, footnote markers, signature blocks and consolidation lists; grep of A1 structured files for row IDs by tag; hand tally of numbers per slide and per press release line. Then a diff against each A2 count test.

| Doc | Category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | Row IDs total | 993 | 993 (grep `^R\d{3} \|`) | none | PASS |
| Results | NUMBER rows | 891 | 891 | none | PASS |
| Results | ENTITY / FORWARD / DATE / QUALIFIER | 35 / 5 / 20 / 42 | 35 / 5 / 20 / 42 | none | PASS |
| Results | Notes | 8 | 8: Notes 1, 2, 3(i), 3(ii), 4, 5 (res L268-L294), cash-flow note (i) (res L256-L262), EPS footnote (res L118, L564) | none | PASS. Composition differs: A2 counts Note 1 twice (R655, R656) and files the EPS footnote (R644) as unnumbered. A4 tables every item of both sets (rev L68-L79). |
| Results | Agenda items | 3 | 3 (res L36, L39, L42) | none | PASS |
| Results | Auditor paragraphs | 9 | 9: standalone L321, L328, L336, L346; consolidated L396, L404, L412 (+L422 Reg 33(8) sub-para), L425, L450 | none | PASS |
| Results | Consolidated entities | 3 | 3 (res L429, L433, L434) | none | PASS |
| Results | Signature blocks | 5 | 5 (res L54-L57, L299-L300, L360-L363, L464-L467, L514-L518) | none | PASS |
| Results | ZERO_STANDING cells | 18 | 18 (res L555 x5, L556 x4, L557 x6, L565 x3) | none | PASS |
| Results | Annexure-B items | 4 (L4) | 4 (res L483-L508) | none | PASS. Sl.4 "Not applicable" (res L508) is absent from A1 structured; A2 records it as M1, so the ledger is complete. |
| Presentation | Slides | 18 | 18 (`[page N]` markers) | none | PASS |
| Presentation | NUMBER rows | 280 | 280 (grep); hand tally p1 4, p6 25, p7 8, p8 4, p10 19, p11 33, p12 37, p13 18, p14 57, p15 21, p16 54 | none | PASS |
| Presentation | P&L line items | 34 | 34 (pres L375-L392, L430-L451) | none | PASS |
| Presentation | ENTITY / FORWARD / DATE / QUALIFIER | 20 / 21 / 21 / 30 | 20 / 21 / 21 / 30 | none | PASS |
| Press release | Pages | 3 | 3 | none | PASS |
| Press release | NUMBER rows | 24 | 24 (19 business numbers pr L60-L95; 5 admin pr L24, L39, L53 x2, L117) | none | PASS |
| Press release | ENTITY / FORWARD / DATE / QUALIFIER | 16 / 7 / 8 / 5 | 16 / 7 / 8 / 5 | none | PASS |
| Press release | Notes / footnotes | 0 | 0 (no "note", "footnote" or "*" in pr fulltext) | none | PASS |
| All | Turns / questions | 0 | 0 (no transcript in run) | none | PASS |

A4 citation check: rev L13-L21 declares every ledger row reviewed and tables all 8 results notes (rev L68-L79). Data slides are cited by line: p6 (pres L127-L128, L140), p7 (L150-L165), p8 (L179-L194), p10 (L229-L237), p11 (L247-L273), p12 (L284-L325), p13 (L353-L361), p14 (L374-L392), p15 (L414), p16 (L448). Non-data slides (p1-p5, p9, p17, p18) and the press release cover letter are covered by the preamble. Press release pages 2-3 are cited (pr L69, L81, L94-L95, L97, L103-L107). Orphan rows: none. Rows missing from the ledger: none.

Coverage result: PASS. One reviewed row carries an untested claim: R018 (pr L94, intake +15.4% YoY). See Audit 3, counter P2.

---

## AUDIT 2: ARITHMETIC

Every derived metric in A4's tables was recomputed from the Rs Mn source lines. Values below are Rs Cr unless marked Mn.

| Metric | A4 value (rev line) | Recomputed | Source line | Status |
|---|---|---|---|---|
| Cons total-expense footing, six columns | foot except Q2 FY26, gap 20.00 (L125) | Q2 FY26 lines sum 2,768.18 Mn vs printed 2,968.18, gap 200.00 Mn; other five foot exactly | res L541-L547 | PASS |
| Cons Op EBITDA Q2 FY26 / Q1 FY27 / Q2 FY27 / H1 FY26 / H1 FY27 / FY26 | 31.19 / 39.16 / 34.17 / 56.25 / 73.33 / 126.82 (L131) | 311.93 / 391.63 / 341.70 / 562.51 / 733.33 / 1,268.19 Mn | res L539, L544, L545, L548 | PASS |
| Cons Op EBITDA margin, six columns | 10.04 / 10.48 / 8.69 / 9.55 / 9.56 / 10.05% (L132) | 10.04 / 10.48 / 8.69 / 9.55 / 9.56 / 10.05% | res L538 | PASS |
| Cons reported EBITDA, six columns | 53.85 / 39.43 / 56.79 / 83.09 / 96.21 / 163.08 (L133) | 538.54 / 394.28 / 567.85 / 830.88 / 962.13 / 1,630.82 Mn | res L544-L548 | PASS |
| Cons core PBT (PBT - OI) | 13.82 / 21.95 / 16.70 / 19.74 / 38.64 / 56.90 (L134) | 138.16 / 219.45 / 166.98 / 197.41 / 386.43 / 568.98 Mn | res L539, L548 | PASS |
| Cons OI / PBT | 62.12 / 1.19 / 57.53 / 57.62 / 37.19 / 38.93% (L135) | same | res L539, L548 | PASS |
| Cons ETR | 11.88 / 26.68 / 13.48 / 14.96 / 18.24 / 21.34% (L136) | same | res L548, L551 | PASS |
| Cons PAT margin | 10.35 / 4.36 / 8.65 / 6.72 / 6.56 / 5.81% (L137) | same | res L538, L552 | PASS |
| Cons gross margin | 41.22 / 37.94 / 37.41 / 40.74 / 37.67 / 40.37% (L138) | same | res L538, L541, L542 | PASS |
| Cons PAT ex-earnout | 12.57 / 16.29 / 15.82 / 20.03 / 32.10 (L139) | 125.70 / 162.85 / 158.19 / 200.33 / 321.04 Mn | res L552, L213, L288 | PASS |
| Cons ETR ex-earnout | 25.63 / 26.68 / 25.09 / 25.81 / 25.90% (L140) | same | res L548, L551, L213 | PASS |
| Q1 FY26 derived: revenue, op EBITDA, margin, core PBT, GM | 278.43 / 25.06 / 9.00% / 5.93 / 40.21% (L142) | 2,784.27 / 250.58 Mn / 9.00% / 59.25 Mn / 40.21% | res L538-L548 | PASS |
| H2 FY26 derived: revenue, op EBITDA, margin, core PBT, GM | 672.42 / 70.57 / 10.49% / 37.16 / 40.05% (L142) | 6,724.24 / 705.68 Mn / 10.49% / 371.57 Mn / 40.05% | res L538-L548 | PASS |
| Standalone Op EBITDA, six columns | 27.35 / 33.42 / 33.02 / 52.45 / 66.44 / 108.17 (L170) | 273.49 / 334.20 / 330.19 / 524.46 / 664.39 / 1,081.71 Mn | res L539-L548 | PASS |
| Standalone Op EBITDA margin | 11.61 / 11.81 / 11.20 / 11.87 / 11.50 / 11.48% (L171) | same | res L538 | PASS |
| Standalone core PBT, ETR, PAT margin, GM | L173-L177 | all 24 cells match | res L538-L552 | PASS |
| Standalone HY Sep-25 other expenses repair | 718.47 Mn (L28, L156) | 4,157.85 - 3,439.38 = 718.47 Mn | res L541-L547 | PASS |
| Standalone HY Sep-26 basic EPS repair | 4.55 (L28, L161) | 360.78 / 79.37 = 4.546; Q1 + Q2 basic = 4.54 | res L552, L562-L563 | PASS (rounding) |
| Subsidiary revenue, op EBITDA, margins, GM | L183-L186 | all cells match (e.g. Q2 FY27 982.98 Mn, 11.51 Mn, 1.17%, 38.85%) | res L538-L548 | PASS |
| Subsidiary PBT and PAT, reported and ex-earnout | L187-L190 | all cells match (e.g. Q2 FY27 PBT ex-earnout -50.41 Mn, PAT ex-earnout -35.60 Mn) | res L548, L552, L213, L288 | PASS |
| SA vs cons gap %, reported and ex-earnout | L200-L205 | 137.5 / -2.5 / 75.5 / 59.7 / 39.4 / 30.1%; ex -7.1 / -2.5 / -18.4 / -19.2 / -11.0% | res L552 | PASS |
| Cons YoY, Step 2A (12 lines) | L217-L228 | revenue +26.54%, op EBITDA +9.54%, margin -135 bps, D&A +7.62%, FC -10.42%, EBIT +10.53%, OI -0.20%, core PBT +20.86%, PBT +7.77%, PAT +5.81%, PAT ex-earnout +25.85%, EPS +5.68% | res L538-L563 | PASS |
| Standalone YoY, Step 2B (11 lines) | L234-L244 | all match; margin -40.5 bps shown as -41 | res L538-L563 | PASS |
| Subsidiary revenue growth, margin change | +31.08%, -396 bps (L248-L249) | +31.08%, -395.5 bps | res L538-L548 | PASS (rounding) |
| Cost ratios Q2 YoY | GM -381, employee +23 (on 529.42), other exp -268 bps (L249) | -380.7, +22.7, -268.4 bps | res L538-L546; pres L377 | PASS |
| PBT gap bridge | core +2.88; OI (0.05) = earnout (1.38) + FX +3.86 + other (2.52); PBT +2.84; tax (0.97); PAT +1.87 (L251) | +28.82; -0.46 = -13.80 + 38.55 - 25.21; +28.36; -9.67; +18.69 Mn | res L539, L548, L551, L552, L286, L213, L288 | PASS |
| Tax charge growth | +22.4% (L251) | 52.99 / 43.32 = +22.32% | res L551 | STYLE (computed from rounded Cr; see S1) |
| Earnout share of PBT / PAT / H1 OI | 46.3% / 53.5% / 79.5% (L250, L253, L302) | 46.28% / 53.49% / 79.52% | res L288, L548, L552, L539 | PASS |
| Interest income H1 | 2.33 vs 10.08 (L253) | 23.27 vs 100.83 Mn | res L212 | PASS |
| QoQ revenue run-rate | +11.57 / -2.36 / +21.69 / +1.27 / +5.16% (L262-L266) | same (deck 3,033 and 3,691 for Q3, Q4 FY26) | res L538; pres L247-L250 | PASS |
| TTM revenue | 1,439.31 (L271) | 6,724.24 + 7,668.90 = 14,393.14 Mn | res L538 | PASS |
| Deck H2 FY26 cross-check | revenue 672.4; EBITDA 74.0 - 3.4 = 70.6 (L268) | 3,033 + 3,691 = 6,724; 309 + 431 - 34 = 706 vs filed 705.68 Mn | pres L247-L256; res L538-L548 | PASS on arithmetic; inference fails, see C1 |
| PAT bridge Step 4 (all 16 rows) | L284-L299 | revenue +82.80 Mn (25.76%); margin -53.03 (16.50%); GM -149.64; employee -8.92; other exp +105.52; D&A -8.05; FC +7.10; tax -3.37 / -6.30; total +18.69 Mn (+5.81%) | res L538-L552 | PASS |
| OI-reversion PAT | PBT 16.96, PAT 12.69, annualised 50.77 (L303) | 169.63 Mn; 126.93 Mn at 25.17%; 507.7 Mn | res L539, L548 | PASS |
| Subsidiary deferred tax credit | 1.45; 368 bps of PBT; DTA 6.35 vs 4.90 (L305) | 14.48 Mn; 3.68%; 63.50 vs 49.03 Mn | res L550, L143 | PASS |
| Below-EBITDA offset | D&A +51, FC +64, OI ex-earnout +13, tax +5, total +133 bps; normalized PAT margin 4.02% vs 4.05% (L307) | +50.9, +64.1, +13.1, +4.7 = +132.7 bps; 4.024% vs 4.047% | res L538-L552 | PASS |
| Cons CFO, CFO/PAT, CFO/op EBITDA | 139.67 / 14.75; 3.53x / 0.29x / 0.46x ex-earnout; 248.3% / 20.1% (L319-L321) | 1,396.74 / 147.51 Mn; 3.526x / 0.293x / 0.459x; 248.3% / 20.1% | res L229, L552 | PASS |
| Cons capex, FCF, FCF after leases | 32.54 / 14.34; 107.14 / 0.41; 98.90 / (7.88) (L322-L324) | 325.39 / 143.40; 1,071.35 / 4.11; 988.96 / -78.81 Mn | res L234, L246-L247 | PASS |
| Cons WC change | +100.60 / (50.64) (L325) | +1,006.01 / -506.41 Mn | res L220-L226 | PASS |
| Cons days (filing basis): receivable, inventory, payable, CCC, NWC incl. contract assets | 88.9/77.6; 187.3/177.8; 79.1/81.1; 197.1/174.3; 209.8/189.0 (L326-L330) | 88.92/77.58; 187.30/177.78; 79.08/81.11; 197.14/174.25; 209.82/189.00 | res L148-L152, L180-L181; res L538 | PASS |
| Deck days, Q4 FY26 and Q2 FY27 | 153/74/64/18/145 and 162/73/68/13/153 (L331) | positional read of pres L286-L320 gives the same values | pres L286-L320 | PASS |
| Cons borrowings, cash pool, net cash, net debt incl. leases | 106.13/131.96; 145.80/154.60; 39.68/22.64; 26.47/49.01 (L334-L337) | 1,061.25/1,319.60; 1,458.00/1,545.98; 396.75/226.38; 264.74/490.08 Mn | res L151-L154, L170-L171, L177-L178 | PASS |
| Standalone cash block (CFO, CFO/PAT, capex, FCF, WC, four day counts, net cash) | L344-L356 | all match (CFO 25.31 Mn; 0.070x; FCF -116.68 Mn; WC -564.21 Mn; CCC 187.0; net cash 1,188.17 Mn) | res L135-L262; res L538 | PASS |
| Subsidiary balance sheet | borrowings 103.17 (current 67.18); cash 6.99; net debt 96.18; payables 31.52 vs 14.62 (+115.6%); OCFL 4.76 vs 22.31; GW + intangibles 117.89 = 11.0% of equity (L359) | 1,031.69 (671.80); 69.90; 961.79; 315.17 vs 146.19 (+115.6%); 47.56 vs 223.12; 1,178.91 Mn = 11.04% | res L137-L138, L153, L165, L170, L177, L180-L183 | PASS |
| US term debt moved to current | about 27.8 (L366) | 418.36 - 140.12 = 278.24 Mn | res L170, L245 | PASS |
| EPS ex-earnout; TTM EPS reported / ex-earnout; TTM ex-earnout PAT | 1.99; 10.58 / 8.29; 65.78 (L410, L414) | 1.993; 10.58 / 8.287; 336.74 + 321.04 = 657.78 Mn | res L552, L562 | PASS on arithmetic; basis caveat fails, see C1 |
| ROCE, EBIT margin | 8.48% / 9.73%; 6.63% (L412, L464) | 1,017.34 / 12,001.60 = 8.48%; / 10,455.62 = 9.73%; 508.67 / 7,668.90 = 6.63% | res L135-L177, L538-L548 | PASS |
| Order book ratios | +8.27% QoQ, +22.8% YoY, walk 1.55x, intake QoQ +9.3%, 1.95 / 1.79 years (L423, L440, L466) | 2,148 / 25,989; 5,226 / 22,911; 6,078.90 / 3,930.90 = 1.546; 6,078.90 / 5,561.00 = +9.31%; 28,137 / 14,393.14; 28,137 / 15,723.6 | pres L289-L294, L229-L230, L414; res L538 | PASS |
| Trailing PE | 92.5x / 118.1x; 22% lower (L470, L482) | 979 / 10.58 = 92.5x; 979 / 8.29 = 118.1x; 21.7% | Notion CMP (memory) | PASS |
| Q1 FY27 YoY gross margin change | -227 bps (L422) | 37.944% vs 40.206% = -226.2 bps | res L538-L542 | STYLE (rounded inputs; see S2) |
| H1 revenue growth | 30.19% (L639) | 7,668.90 / 5,890.61 = +30.19% | res L538 | PASS |
| Share and grant arithmetic | +19,000 shares; 273,400 units = 0.34% (L58-L60) | 0.19 Mn / Rs 10; 0.2734 / 79.38 = 0.344% | res L163, L42-L43 | PASS |
| Note conversions (FX, OCI, cash note, SBP swing, standalone PBT ex-FX QoQ) | L70-L77 | all match (e.g. 24.27 vs 24.35; swing 3.96; SBP 6.16) | res L285-L286, L555, L259-L261, L214 | PASS |
| Question-table numbers (Q3, Q7, Q9-Q13, Q20-Q23) | L506-L526 | all match (11.51 / 57.43 Mn; 4.11 Mn and about -168 Mn; 14.48 Mn; 4.6%; +32.7%) | res L135-L288 | PASS |

Arithmetic result: no mismatch above rounding. Two rounding-level items are logged as STYLE (S1, S2).

---

## AUDIT 3: ADVERSARIAL READ

The three most positive claims in A4, plus the mandatory acquisition-economics probe.

### P1. "The India entity did well: revenue up 25.10%, profit up 43.18%" (rev L597; Step 2B "Strong", rev L241-L244)

Bear counter, from the same extract:
- The FX line swung from a 19.54 Mn loss to an 18.89 Mn gain (res L285). That 38.43 Mn swing is 48.7% of the 78.99 Mn standalone PBT gain (182.60 to 261.59 Mn, res L548).
- Ex-FX, standalone PBT grew 20.1% (202.14 to 242.70 Mn). That is below standalone revenue growth of 25.1%.
- Standalone gross margin fell 435 bps YoY (41.28% to 36.93%; res L538, L541, L542). This is a bigger fall than the consolidated 381 bps.
- H1 standalone op EBITDA carries a 30.53 Mn ECL write-back against a 10.08 Mn charge a year earlier (res L216). The quarter split is NOT FOUND.
- H1 standalone CFO was 25.31 Mn against 360.78 Mn PAT (0.07x; res L229, L552). New current borrowings of 287.91 Mn funded the inventory build (res L565, L221).

Survives: YES. A4 shows the FX swing (rev L240) and asks about the ECL (Q22), but it never states the ex-FX growth or the FX share. The brief line has no qualifier. Graft into Step 2B and brief L597: "ex-FX standalone PBT +20.1%; FX is 48.7% of the PBT gain." Type: MISSING.

### P2. "Order book momentum GREEN / ON TRACK: record 28,137 Mn, +22.8% YoY, book-to-bill 1.6x" (rev L423, L440, L600)

Bear counter, from the same extract:
- The press release states intake grew 11% QoQ and 15.4% YoY (pr L94). The book walk (closing book - opening book + revenue) gives these intakes: Q2 FY26 = 22,911 - 21,318 + 3,106.34 = 4,699 Mn; Q1 FY27 = 25,989 - 24,166 + 3,738.00 = 5,561 Mn; Q2 FY27 = 28,137 - 25,989 + 3,930.90 = 6,079 Mn (pres L289-L294; res L538).
- Walk-implied YoY intake growth is +29.4%, against the stated +15.4%. A gap of 14 percentage points.
- For the stated YoY rate to hold, the Q2 FY26 book must have lost 568 Mn (at the walk intake) to 751 Mn (at the stated 1.6x) to cancellations, FX revaluation or re-scoping. None of this is disclosed.
- A4 ties only the QoQ leg (+9.3% vs 11%) and the 1.55x vs 1.6x leg (rev L440, FN-05, Q15). The YoY leg, R018, is reviewed but never tested.
- The record book arrives with the lowest operating margin of six quarters (8.69%), customer advances down from 33 to 13 days (pres L305-L315), and an executable share that is NOT FOUND.

Survives: YES. The book is real, but the stated intake figures and the book cannot both be clean. Graft into 6B test 3, 6D, the ORDER BOOK flag and Q15: the YoY tie-out, with Q2 FY26 cancellations and FX named. The GREEN status can stand, with a second tie-out caveat. Type: MISSING.

### P3. "Normalized PAT +25.85%, Positive; normalized PAT margin held because most of the 133 bps offset is recurring while debt stays flat" (rev L227, L307, L595, L733)

Bear counter, from the same extract:
- The consolidated FX swing is 38.55 Mn pre-tax (19.01 vs (19.54), res L286). That is about 28.85 Mn after tax at 25.17%, or about 89% of the 32.49 Mn normalized PAT gain (125.70 to 158.19 Mn).
- Ex-earnout and ex-FX, consolidated PBT grew 1.9% (188.56 to 192.17 Mn; res L548, L213, L288, L286) on revenue +26.5%. Falling interest income (other OI fell 25.21 Mn) offsets the FX gain. A4's core PBT (+20.86%) removes both, so the core figure stands. The "+25.85%" headline that A4 marks Positive, and repeats in the brief, is FX-driven.
- The 64 bps finance-cost leg is half the 133 bps offset. Finance cost fell 10.42% YoY (res L544). Gross borrowings rose 24.3% in H1 (1,061.25 to 1,319.60 Mn; res L170, L177) and lease liabilities rose 8.3% (661.49 to 716.46 Mn; res L171, L178).
- The deck's cause, "lower working capital borrowings" (pres L381), conflicts with the balance sheet. A4's condition "while debt stays flat" was already false at 30-Sep-2026. A4's own L252 and L304 warn that finance cost may rise from Q3.

Survives: YES. Graft into Step 4 L307: the finance-cost leg is at risk on the H1 debt build, so "most of the offset is recurring" becomes "about half rests on finance cost that the H1 debt build puts at risk". Graft into Step 2A L227 and brief L595: "about 89% of the normalized PAT gain is the FX swing; ex-earnout ex-FX PBT +1.9%." Type: MISSING.

### P4. MANDATORY ACQUISITION-ECONOMICS PROBE: "Altek integration completed and renamed; stronger global footprint" (pres L191-L194; pr L103-L105; rev L444 lists it as confirming evidence)

- Consideration: NOT FOUND in the three extracts. The probe uses the acquired carrying value as the price proxy.
- Acquired goodwill + intangibles in the subsidiaries: 730.94 + 447.97 = 1,178.91 Mn (res L137-L138, consolidated minus standalone).
- Subsidiaries TTM (H2 FY26 + H1 FY27), consolidated minus standalone, net of eliminations: revenue 3,609.57 Mn; op EBITDA 148.43 + 68.94 = 217.37 Mn (6.0%); PAT ex-earnout 21.57 - 39.74 = -18.17 Mn (res L538-L552, L213, L288).
- Multiples: about 1,178.91 Mn carrying value / 217.37 Mn TTM op EBITDA = about 5.4x EBITDA. Against TTM PAT ex-earnout of -18.17 Mn there is no positive earnings multiple.
- Quality markers: Q2 op EBITDA margin 1.17%. Subsidiary net debt 961.79 Mn = 4.4x TTM op EBITDA, of which 671.80 Mn is current (res L153, L170, L177). Ex-earnout PAT is negative in every period shown.
- Seller performance: cumulative earnout fair-value write-backs 195.75 Mn (H1 FY26) + 181.95 Mn (Q2 FY27) = 377.70 Mn (res L213, L288). That is 32.0% of the carrying value. Targets were missed twice.
- Why it looks cheap at 5.4x EBITDA: the earnings year is not representative. TTM EBITDA includes H2 FY26 (148.43 Mn). That half fell to 68.94 Mn in H1 FY27 and to 11.51 Mn in Q2 FY27 alone. On Q2 annualised (46.04 Mn), the carrying value is about 25.6x EBITDA.

Reading: this is a leveraged, low-margin, loss-making (ex-earnout) asset, not a cheap high-quality one. The bear reading survives. A4 carries the substance (flags US ARM; Q2, Q9, Q11; tripwires a and b). It does not state the multiple, the cumulative write-back or the leverage ratio. Graft one line into Step 5B / the US ARM flag. Type: MISSING.

---

## FINDINGS (tagged)

### CONTRADICTION (loop A4)

C1. Q3 FY26 deck one-off: direction inverted (rev L263, L268, L414, L454, L532 vs pres L265-L273 and res L552).
- A4 infers that the 34 Mn Q3 FY26 one-off on the deck EBITDA chart (pres L253, L256) is a gain "most likely in other income". It labels 9.1% as "normalized" and says the deck's 10.2% "includes it".
- The deck's six-quarter PAT chart gives Q3 FY26 138 and Q4 FY26 224 (pres L269, L271, positional read). H2 FY26 = 362 Mn. The filed H2 FY26 PAT is 732.82 - 396.08 = 336.74 Mn (res L552). The gap is 25.26 Mn. The 34 Mn one-off after tax at 25.17% is 25.44 Mn.
- The other four deck quarters tie to the filing within 0.5 Mn (Q1 FY26 75 vs 74.63; Q2 FY26 321 vs 321.45; Q1 FY27 163 vs 162.85; Q2 FY27 340 vs 340.14).
- So the deck's H2 FY26 profit is above the filing by the after-tax one-off. That fits a charge in the filed operating costs that the deck adds back. It does not fit a gain in filed other income: if the one-off sat in other income, the deck PAT would equal the filed PAT.
- Two readings: (a) a charge the deck normalizes out (fits the PAT tie-out); (b) a gain outside op EBITDA (fits the stacking analogy with the earnout segments). The separating observation is the Q3 FY26 filed quarterly P&L, or the answer to Q29.
- Under (a), 9.07% is the filed Q3 FY26 margin and 10.2% is the deck-normalized margin. The deck FY26 EBITDA of 1,303 in pipeline note 6 (rev L29) includes the add-back. A normalized TTM ex-earnout PAT is about 68.3 Cr (EPS about 8.61). Under (b) it is about 63.2 Cr.
- A4's 65.78 Cr with a downside-only caveat (rev L414, L454) misstates the direction of the uncertainty. This is a pillar-relevant A21 base input.
- Fix: present both readings with the PAT tie-out, relabel the Q3 FY26 cell, state the TTM base as a two-sided range, and reword Q29 to ask direction and line.

C2. FLAG A21-2 (rev L455) says "six quarters rising revenue". A4's own Step 3 (rev L263) and the deck (pres L249: 3,106 to 3,033) show Q3 FY26 fell 2.36% QoQ. Fix: "five of six quarters rose; Q3 FY26 dipped 2.36%". The seasonality sentence must rest on that.

### MISSING (loop A4)

M1. Surviving counter P1. Standalone ex-FX PBT +20.1%; FX is 48.7% of the standalone PBT gain; standalone GM -435 bps. Graft into Step 2B verdicts and brief L597.
M2. Surviving counter P2. Stated intake +15.4% YoY (pr L94, R018) vs walk-implied +29.4% (pres L289-L294; res L538). Graft into 6B test 3, 6D, the ORDER BOOK flag and Q15.
M3. Surviving counter P3. About 89% of the normalized PAT gain is the FX swing; ex-earnout ex-FX PBT +1.9%. The 64 bps finance-cost leg rests on debt that rose 24.3% in H1. Graft into rev L227, L307, L595.
M4. Surviving counter P4 (acquisition probe). Carrying value 1,178.91 Mn = 5.4x subsidiary TTM op EBITDA (about 25.6x on Q2 annualised). TTM PAT ex-earnout is negative. Write-backs total 377.70 Mn = 32.0%. Net debt is 4.4x. Graft one line into Step 5B / the US ARM flag.

### FACTUAL
None. Every A4 table metric recomputes within rounding.

### STYLE (logged, no loop)
S1. Rev L251: tax growth "22.4%" recomputes to 22.32% on Rs Mn (52.99 / 43.32, res L551). The figure came from rounded Cr inputs, against the review's own Rs Mn convention (rev L7).
S2. Rev L422: Q1 FY27 YoY gross margin "-227 bps" recomputes to -226 bps on Rs Mn (37.944% vs 40.206%).
S3. Rev L271: "four rising quarters since Q3 FY26". Three consecutive QoQ rises follow Q3 FY26. Reword as "three consecutive rises after the Q3 FY26 dip".
S4. Brief rev L598: "Its EBITDA was Rs 1.15 Cr ... It lost money (FILED)" drops the qualifier carried at rev L179, L192 and Q3: consolidated minus standalone, net of intercompany eliminations, entity split NOT FOUND. Add the qualifier and tag the figure as derived.
S5. Brief rev L595: "up 25.85% (FILED)". The Q2 FY26 earnout placement comes from the deck (pres L385), so tag it FILED + MGMT.
S6. Upstream defects that A4 already corrected or that do not touch the deliverable (no loop):
- A1 results R451 tags the 19.33 Mn loan repayment to HY Sep-26. The investing footing (res L232-L239) places it in HY Sep-25. A4 pipeline note 2 corrects this.
- The A2 press ledger note on R036 reverses the rename direction. pr L103-L104 governs, and A4 pipeline note 1 corrects it.
- A1 press release page tags on R016-R019, R031-R034, R037 and R047 say page 3. pr L92-L97 sit on page 2 (page 3 starts at pr L99).
- A1 results structured lacks Annexure-B Sl.4 "Not applicable" (res L508). A2 records it as M1.

---

## VERDICT

INCOMPLETE. Failing agent: A4. Finding types: CONTRADICTION (C1, C2) and MISSING (M1-M4).

Exact gap: A4 must (1) replace the Q3 FY26 one-off "most likely in other income" inference with both readings and the deck-vs-filing H2 FY26 PAT tie-out (362 vs 336.74 Mn), relabel the Q3 FY26 margin cell, and restate the A21-1 / Step 6A TTM ex-earnout base as a two-sided range (about 63.2-68.3 Cr); (2) correct A21-2 "six quarters rising revenue"; (3) graft the four surviving bear counters P1-P4 at the review lines named above.

No A2 re-enumeration and no A3 forensic re-run is needed. Coverage and arithmetic pass.

## STYLE NOTES
S1-S6 above, recorded for the record. No re-run.

---

```yaml
stage: A5-adversary
company: "CYIENTDLM"
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
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "India entity did well: standalone PAT +43.18% YoY, verdict Strong (rev L243, L597)", counter: "FX swing 38.43 Mn (18.89 vs (19.54)) is 48.7% of the 78.99 Mn standalone PBT gain; ex-FX standalone PBT +20.1% (202.14 to 242.70 Mn), below revenue +25.1%; standalone gross margin -435 bps; H1 standalone CFO 0.07x PAT", source_line: "res L285, L538, L541-L542, L548, L229", type: MISSING}
  - {claim: "Order book GREEN / ON TRACK: record 28,137 Mn, +22.8% YoY, book-to-bill 1.6x (rev L423, L440, L600)", counter: "Stated intake +15.4% YoY does not tie to the book walk: implied intake 4,699 Mn (Q2 FY26) to 6,079 Mn (Q2 FY27) = +29.4%; the stated rate needs 568-751 Mn of undisclosed Q2 FY26 book reductions; A4 tested only the QoQ and 1.55x legs", source_line: "pr L94; pres L289-L294; res L538", type: MISSING}
  - {claim: "Normalized PAT +25.85% Positive; most of the 133 bps below-EBITDA offset is recurring while debt stays flat (rev L227, L307, L595)", counter: "38.55 Mn FX swing (about 28.85 Mn after tax) is about 89% of the 32.49 Mn normalized PAT gain; ex-earnout ex-FX PBT +1.9% (188.56 to 192.17 Mn); the 64 bps finance-cost leg rests on finance cost -10.4% while gross borrowings rose 24.3% and leases 8.3% in H1", source_line: "res L286, L544, L548, L170-L171, L177-L178; pres L381", type: MISSING}
  - {claim: "Altek integration completed and renamed: stronger global footprint (pres L191-L194; rev L444)", counter: "Acquisition probe: consideration NOT FOUND; acquired goodwill + intangibles 1,178.91 Mn = about 5.4x subsidiary TTM op EBITDA 217.37 Mn (about 25.6x on Q2 annualised); TTM PAT ex-earnout (18.17) Mn, no positive earnings multiple; earnout write-backs 377.70 Mn = 32.0% of carrying value; subsidiary net debt 961.79 Mn = 4.4x EBITDA", source_line: "res L137-L138, L153, L170, L177, L213, L288, L538-L552", type: MISSING}
findings_by_type:
  factual: []
  missing:
    - "M1: standalone ex-FX PBT +20.1% and FX share 48.7% of the PBT gain absent from Step 2B and brief L597 (res L285, L548)"
    - "M2: stated intake +15.4% YoY vs walk-implied +29.4% untested; R018 reviewed but not tied (pr L94; pres L289-L294; res L538)"
    - "M3: FX is about 89% of the normalized PAT gain; ex-earnout ex-FX PBT +1.9%; debt rose 24.3% in H1 under the 64 bps finance-cost leg (res L286, L544, L170, L177)"
    - "M4: acquisition multiple not stated: 1,178.91 Mn carrying value = 5.4x subsidiary TTM op EBITDA; TTM PAT ex-earnout negative; write-backs 377.70 Mn = 32.0%; net debt 4.4x (res L137-L138, L213, L288)"
  contradiction:
    - "C1: A4 infers the Q3 FY26 34 Mn deck one-off is a gain in other income (rev L268) and labels 9.1% normalized (rev L263); deck H2 FY26 PAT 138 + 224 = 362 Mn exceeds filed 336.74 Mn by 25.26 Mn = 34 Mn after tax, which fits a charge the deck adds back; TTM ex-earnout base (rev L414, L454) is two-sided, about 63.2-68.3 Cr, not 65.78 with downside only (pres L265-L273; res L552)"
    - "C2: FLAG A21-2 says six quarters rising revenue (rev L455); A4 Step 3 and pres L249 show Q3 FY26 -2.36% QoQ (rev L263)"
  style:
    - "S1: tax growth 22.4% recomputes to 22.32% on Rs Mn (rev L251; res L551)"
    - "S2: Q1 FY27 YoY gross margin -227 bps recomputes to -226 bps (rev L422)"
    - "S3: four rising quarters since Q3 FY26 should read three consecutive rises after the Q3 FY26 dip (rev L271)"
    - "S4: brief L598 drops the net-of-eliminations, entity-split-NOT-FOUND qualifier on the US arm EBITDA and loss"
    - "S5: brief L595 tags 25.85% FILED; Q2 FY26 earnout placement is MGMT (pres L385)"
    - "S6: upstream defects already corrected or immaterial: A1 R451 period tag (HY Sep-25 by res L232-L239 footing); A2 press R036 rename reversed; A1 press page tags R016-R019, R031-R034, R037, R047 on page 2 not 3; A1 results lacks Annexure-B Sl.4 (A2 M1)"
loop_back_to: "A4"
gap: "A4 to (1) replace the Q3 FY26 one-off 'most likely in other income' inference with both readings and the deck-vs-filing H2 FY26 PAT tie-out (362 vs 336.74 Mn), relabel the Q3 FY26 margin cell (filed 9.07%, deck-normalized 10.2% under the charge reading) and restate the A21-1 / Step 6A TTM ex-earnout base as a two-sided range of about 63.2-68.3 Cr; (2) correct A21-2 'six quarters rising revenue' (Q3 FY26 -2.36%); (3) graft surviving counters: standalone ex-FX PBT +20.1% (FX 48.7% of gain) into Step 2B and brief L597; intake YoY tie-out (+15.4% stated vs +29.4% walk) into 6B test 3, 6D, ORDER BOOK flag and Q15; FX about 89% of normalized PAT gain, ex-earnout ex-FX PBT +1.9%, and the H1 debt rise under the 64 bps finance-cost leg into rev L227, L307, L595; acquisition multiple line (5.4x TTM op EBITDA, negative TTM PAT ex-earnout, 377.70 Mn write-backs = 32.0%, net debt 4.4x) into Step 5B and the US ARM flag"
style_notes:
  - "S1: rev L251 tax growth 22.4% vs 22.32% on Rs Mn"
  - "S2: rev L422 Q1 FY27 GM change -227 vs -226 bps"
  - "S3: rev L271 'four rising quarters' wording"
  - "S4: brief L598 needs the net-of-eliminations qualifier"
  - "S5: brief L595 provenance FILED + MGMT"
  - "S6: upstream A1/A2 defects already corrected by A4 (R451 period, R036 rename, press page tags, Annexure-B Sl.4)"
analyst_note: "The numbers are clean. Every A4 table metric recomputes from the Rs Mn source within rounding. The failures are reading failures. First, A4 reads the Q3 FY26 deck one-off as a gain in other income. The deck PAT chart puts H2 FY26 at 362 Mn against a filed 336.74 Mn. The 25.26 Mn gap equals 34 Mn after tax, so the item reads better as a charge the deck adds back. The TTM ex-earnout base is then a two-sided range of about 63.2-68.3 Cr, not 65.78 with downside only. Second, each of A4's three most positive reads lacks a qualifier the extract supports. Half the India PBT gain is FX. Stated YoY intake growth (15.4%) does not tie to the book walk (29.4%). About 89% of the normalized PAT gain is the FX swing, and the finance-cost leverage sits on debt that rose 24% in H1. Third, A4 never states the acquisition multiple. The acquired US asset shows no positive earnings multiple and about 5.4x a falling EBITDA. All fixes are grafts and relabels in A4. No re-enumeration or forensic re-run is needed."
```

---
---

# LOOP 1 RE-AUDIT (2026-10-17)

Agent: A5 adversary, fresh instance | Model: claude-opus-5-5 | Loop iteration: 1
Under audit: the revised work/review_cyientdlm_q2fy27.md (A4 loop_iteration 1) and work/blocks/a4.yaml. In this section "rev L###" means a line of the REVISED review. The run-1 record above keeps its own (old) line numbers.
Inputs read: the run-1 audit above, A1 fulltexts (res, pres), A1 presentation structured (R131-R148), A2 presentation ledger (R131-R148 status), the revised review and the A4 block. No source PDF, nothing under inputs/, no A3 file.
Scope (orchestrator): (1) deliverable gate; (2) closure of C1, C2, M1-M4, with every grafted figure recomputed from the fulltexts; (3) new FACTUAL / MISSING / CONTRADICTION in the revised passages; (4) a fresh adversarial pass on three bullish reads that run 1 did not test. No full arithmetic sweep beyond changed or newly tested figures.

## L1-0. DELIVERABLE-COMPLETENESS (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT (rev L612-L627, 15 lines, inside the 10-20 line band) | sector PRESENT (rev L629-L635) | business model PRESENT (rev L637-L645) | competition PRESENT (rev L647-L652) | forward map PRESENT (rev L654-L667; make-or-break reading at L655; 9 dated rows, each with a bull fork and a bear fork). Gate: PASS.

## L1-1. COVERAGE

Stands from run 1. The orchestrator states that no ledger or extraction changed. The revised preamble (rev L12-L22) keeps the run-1 counts and declares every row reviewed. Orphan rows: none. Rows missing from the ledger: none. Not re-run.

## L1-2. CLOSURE OF RUN-1 ITEMS (grafted figures recomputed)

| Item | Where A4 grafted it (rev) | Recomputed from the A1 fulltexts | Source lines | Status |
|---|---|---|---|---|
| C1 | L30, L271, L276-L281, L432, L436, L476, L492, L554, L753 | Deck H2 FY26 PAT 138 + 224 = 362 Mn; filed 732.82 - 396.08 = 336.74 Mn; gap 25.26 Mn; 34 x 0.7483 = 25.44 Mn. Other quarters: 75 vs 74.63, 321 vs 321.45, 163 vs 162.85, 340 vs 340.14. Filed H2 FY26 op EBITDA 1,268.19 - 562.51 = 705.68 Mn; less deck Q4 431 = 274.68 Mn / 3,033 = 9.06% (base bar 275 gives 9.07%); 309 / 3,033 = 10.19%. Deck FY26 EBITDA 251 + 312 + 309 + 431 = 1,303. TTM ex-earnout 336.74 + 321.04 = 657.78 Mn; plus or minus 25.44 = 683.22 / 632.34 Mn; / 79.383 Mn shares = 8.61 / 7.97; 979 / 8.607 = 113.7x; 979 / 7.966 = 122.9x. Both readings, the PAT tie-out, Q29 as the separating observation and the two-sided range are all present. The deck PAT chart shows no one-off segment for Q3 FY26 (pres L265-L273), which also fits reading (a). | pres L247-L273; res L538-L552, L163 | CLOSED |
| C2 | L477 | "Six quarters rising" is gone. The new text reads "revenue rose in five of six quarters". Rev L269 gives Q1 FY26 QoQ as ND. Measured QoQ moves: +11.57, -2.36, +21.69, +1.27, +5.16% = four rises in five. | pres L247-L250; res L538 | CLOSED; the new wording is a new defect, see LC1 |
| M1 | L241, L247-L252, L621, L747 | FX swing 18.89 + 19.54 = 38.43 Mn; PBT gain 261.59 - 182.60 = 78.99 Mn; share 48.65%; ex-FX PBT 202.14 to 242.70 Mn = +20.07%; revenue 2,947.92 / 2,356.44 = +25.10%; GM 41.28% to 36.93% = -435 bps; CFO 25.31 / PAT 360.78 = 0.070x; ECL (30.53) vs 10.08 Mn | res L216, L229, L285, L538-L552 | CLOSED |
| M2 | L445, L462, L540, L624, L711, L752 | Walk: Q2 FY26 22,911 - 21,318 + 3,106.34 = 4,699.34 Mn; Q1 FY27 25,989 - 24,166 + 3,738.00 = 5,561.00 Mn; Q2 FY27 28,137 - 25,989 + 3,930.90 = 6,078.90 Mn. YoY +29.36%; QoQ +9.31%. 6,078.90 / 1.154 - 4,699.34 = 568.4 Mn; 1.6 x 3,930.90 / 1.154 - 4,699.34 = 750.8 Mn | pres L179, L289-L294; pr L94; res L538 | CLOSED |
| M3 | L228-L232, L320, L617-L618, L745, L751 | FX 19.01 + 19.54 = 38.55 Mn; x 0.7483 = 28.85 Mn; normalized PAT 125.70 to 158.19 Mn (+32.49, +25.85%); share 88.8%. PBT ex-earnout ex-FX 188.56 to 192.17 Mn (+1.91%). Other OI 50.40 to 25.19 Mn (-25.21). Finance cost 68.11 to 61.01 Mn (-10.42%). Borrowings 1,061.25 to 1,319.60 Mn (+24.34%). Leases 661.49 to 716.46 Mn (+8.31%). 64 / 133 = 48%. | res L170-L171, L177-L178, L213, L286, L288, L539, L544, L548, L552 | CLOSED; one grafted sentence overreaches, see LF1 |
| M4 | L374-L381, L466, L746 | Goodwill 761.24 - 30.30 = 730.94; intangibles 466.54 - 18.57 = 447.97; total 1,178.91 Mn. Subsidiary op EBITDA: H2 FY26 (1,268.19 - 1,081.71) - (562.51 - 524.46) = 148.43; H1 FY27 733.33 - 664.39 = 68.94; TTM 217.37 Mn = 5.42x; Q2 11.51 x 4 = 46.04 Mn = 25.61x. Subsidiary PAT ex-earnout: H2 FY26 336.74 - 315.17 = 21.57; H1 FY27 321.04 - 360.78 = -39.74; TTM -18.17 Mn. Write-backs 377.70 / 1,178.91 = 32.04%. Net debt (1,319.60 - 287.91) - (827.07 - 757.17) = 961.79 Mn = 4.42x; current 959.71 - 287.91 = 671.80 Mn. | res L137-L138, L153-L154, L170, L177, L213, L288, L538-L552, L565 | CLOSED |
| S1-S5 | L259, L444, L284, L622, L617 | Tax 52.99 / 43.32 = +22.32% (now 22.3%); Q1 FY27 GM change 37.944% vs 40.206% = -226 bps (now -226); "three consecutive QoQ rises after the Q3 FY26 dip"; net-of-eliminations qualifier added; "FILED + MGMT" tag added | res L538-L551 | CLOSED |

Residue check: a grep of the revised review finds no "most likely in other income", no downside-only caveat on the TTM base, no "six quarters rising", no "four rising", no "22.4%" and no "-227". The flags in work/blocks/a4.yaml match the block embedded in the review.

## L1-3. NEW DEFECTS IN THE REVISED PASSAGES

LC1. CONTRADICTION (loop A4). Rev L477 (FLAG A21-2) says "revenue rose in five of six quarters".
- Rev L269 gives Q1 FY26 QoQ as ND (Q4 FY25 not in run).
- The extract supports four rises in five measured QoQ moves.
- This wording came from my own run-1 fix text for C2. The error is mine, and A4 adopted it.
- Fix: "revenue rose in four of the five measured QoQ moves; Q3 FY26 dipped 2.36%; Q1 FY26 QoQ is ND." The seasonality sentence after it stands.

LF1. FACTUAL (loop A4). Rev L320 says: "The deck credits 'lower working capital borrowings' (pres L381); the 30-Sep-2026 balance sheet does not support that." Rev L388 makes the same comparison. Q10 (rev L535) says "The deck claim and the balance sheet disagree".
- The deck claim is YoY: Q2 FY27 finance cost 61 vs 68 Mn (pres L381-L385).
- A4 tests it against a 31-Mar-2026 to 30-Sep-2026 balance move (res L170, L177). The 30-Sep-2025 borrowing balance is NOT FOUND.
- The extract leans toward the deck. In H1 FY26 the company repaid 992.96 Mn of current and 746.72 Mn of non-current borrowings against 823.58 Mn of proceeds (res L243-L245).
- H1 interest paid fell 33.0%, from 143.09 to 95.86 Mn (res L248).
- The whole YoY finance-cost fall sits in the standalone entity: 49.34 to 39.85 Mn. Subsidiary finance cost rose from 18.77 to 21.16 Mn (res L544).
- So the claimed disagreement sets a YoY statement against a half-year balance move. The extract does not support it.
- My run-1 counter P3 made the same overstatement ("conflicts with the balance sheet"), and A4 grafted it.
- Fix at L320, L388 and Q10: "The deck's YoY cause cannot be tested: the 30-Sep-2025 balance is NOT FOUND. H1 FY26 repayments and a 33% fall in interest paid fit it. The H1 FY27 build (gross borrowings +24.3%) points to higher finance cost from Q3 [INFERENCE]."
- The substance of M3 stands: the 64 bps finance-cost leg is at risk on the H1 build.

STYLE (logged, no loop):
- LS1. Rev L232: "Other other-income fell 25.21 Mn, mostly interest (res L212)". Res L212 gives H1 interest only (23.27 vs 100.83 Mn); the Q2 split is NOT FOUND. Tag the read [INFERENCE from H1].
- LS2. Rev L381: "EBITDA fell each half since". Only one half follows H2 FY26. Write "fell to 68.94 Mn in H1 FY27 and to 11.51 Mn in Q2 FY27".

## L1-4. FRESH ADVERSARIAL READ (three bullish reads run 1 did not test)

### N1. "The cause is materials, not overheads"; the other-expense leverage (-268 bps, +10.55 Cr) is "Recurring"; core PBT +20.86% "Positive", "headline growth is not inflated YoY" (rev L225, L257-L258, L301, L315, L444, L615)

Bear counter, from the same extract:
- QoQ, the margin fall is mostly overheads. Op EBITDA margin fell 178 bps (10.48% to 8.69%).
- Of that, gross margin gave 53 bps (37.94% to 37.41%), employee cost 3 bps (17.24% to 17.27%) and other expenses 122 bps (10.23% to 11.45%).
- Other expenses rose 17.7% (382.41 to 450.02 Mn) on revenue +5.2% (res L538-L546). So 125 of the 178 bps (70%) is opex.
- The YoY other-expense leg is measured against the highest filed ratio. Other-expense ratio: Q1 FY26 10.45%, Q2 FY26 14.13%, H2 FY26 12.29%, Q1 FY27 10.23%, Q2 FY27 11.45%.
- About 72 Mn of the 105.52 Mn "recurring" leg is the gap between the Q2 FY26 ratio and the H2 FY26 average. Against H2 FY26, Q2 FY27 leverage is about 84 bps (33 Mn).
- Combined employee plus other-expense ratio: Q1 FY26 31.21%, Q2 FY26 31.18%, H2 FY26 29.55%, Q1 FY27 27.47%, Q2 FY27 28.72%. Half of the YoY -245 bps (rev FN01) reversed in one quarter (+125 bps QoQ).
- The 28.82 Mn core PBT gain rests wholly on opex leverage. The bridge gives other expenses +105.52 Mn and employee -8.92 Mn against gross margin -149.64 Mn (recomputed). Core PBT fell 23.9% QoQ (219.45 to 166.98 Mn; res L539, L548).
- The deck's p11 comment is undated: "EBITDA margin reflects continued investment into sales, strategy and strengthening capabilities" (pres L255-L257). It fits the QoQ move. A4 tests it only against the YoY ratio (rev L444).
- Two readings:
  - (a) Q2 carries seasonally high other expenses. Q2 sits above Q1 in both years: consolidated +368 and +122 bps; standalone 13.34% to 18.81% and 13.34% to 15.47%. Then the YoY leverage is like-for-like and recurring.
  - (b) Q2 FY26 was a spike and the leverage peaked in Q1 FY27. Q2 FY27 then gave part of it back on the "investment" the deck names.
  - Separating observation: the Q3 FY27 combined opex ratio against the H2 FY26 average (29.55% consolidated, 27.11% standalone).

Survives: YES. A4 states reading (a) as settled. Its Q3 FY27 make-or-break tests gross margin alone (rev L512-L516, L655). Graft the QoQ decomposition and the two readings into Step 4 (rev L301 label, L315), Step 2C Q2 and brief L615 ("YoY. QoQ, opex caused 125 of the 178 bps"). Scope the 6B test 2 p11 sentence (rev L444) to YoY. Add the combined opex ratio as a co-reading in 8C. Type: MISSING.

### N2. "Revenue Strong, +26.54%"; "Aerospace is the engine this quarter"; "Aerospace growth of 62% shows this lane works" (rev L218, L256, L632, L648)

Bear counter, from the same extract [INFERENCE from MGMT shares and growth rates]:
- The deck names Aerospace and Industrial as the two largest slices (pres L353-L356). The slices are unassigned in A1 (R131-R135) and in A2 (SLICE_UNASSIGNED), so both mappings are tested.
- Mapping A (Aerospace 47%, Industrial 31%): Aerospace Q2 FY26 base 1,847.52 / 1.62 = 1,140.4 Mn, increment 707.1 Mn. Industrial 1,218.58 / 1.29 = 944.6 Mn, increment 274.0 Mn. Together 981.0 Mn = 119% of the 824.56 Mn total increase.
- Mapping B (Aerospace 31%, Industrial 47%): increments 466.4 + 415.3 = 881.7 Mn = 107% of the total.
- Either way, the other 22% of revenue (Defence, Med Tech, Auto & Others) shrank in aggregate. It fell 15.3% (1,021.3 to 864.8 Mn) under A and 6.2% under B; 5-17% across share rounding.
- Defence grew 13% and Med Tech 14% (pres L358-L362). So Auto & Others fell faster than the aggregate. The deck gives neither its value nor its growth.
- Aerospace alone gave 57-86% of the increase. Top customers were 56% of revenue (rev L649, SECONDARY).

Survives: YES, at INFERENCE tier. The filed headline stands; its breadth is the missing qualifier. Graft one line into Step 2C Q1 and the brief (Sector L632 or Competition L648): "Aerospace and Industrial gave more than all of the YoY increase. The other 22% of revenue shrank 6-15%, so Auto & Others fell sharply; value NOT DISCLOSED [INFERENCE]." Add a question on Auto & Others revenue and its YoY change. Type: MISSING.

### N3. "Ex-earnout consolidated ETR 25.09% is normal"; a single quarter ex-earnout is a valid A21 base (rev L318, L476-L478)

Bear counter, from the same extract:
- The 25.09% rate is normal only because the US loss is tax-effected. Subsidiary deferred tax is (16.12) - (1.64) = a 14.48 Mn credit. Subsidiary current tax is -0.33 Mn (res L549-L550).
- Without the credit, Q2 ex-earnout tax is 67.47 Mn on 211.18 Mn, a 31.95% rate.
- The credit is 9.2% of Q2 normalized PAT (158.19 Mn). It grew from 3.93 Mn in Q2 FY26 (consolidated (2.57), standalone 1.36).
- The 10.55 Mn increase is 32.5% of the 32.49 Mn normalized PAT gain. Without the credit in both quarters, normalized PAT grew 18.0% (121.77 to 143.71 Mn), not 25.85%.
- With M3: ex-FX (after tax at 25.17%) and ex the credit, normalized PAT fell about 5.1% (136.39 to 129.48 Mn) [derived].
- The pattern reversed last year. Subsidiary deferred tax was a 17.33 Mn credit in H1 FY26 and a 24.35 Mn charge in H2 FY26 (res L550).
- A21 effect: the Q2-annualised ex-earnout base (63.28 Cr) carries 5.79 Cr of annualised credit (4 x 14.48 Mn). The H1-annualised base (64.21 Cr) carries 2.71 Cr.
- The TTM base (65.78 Cr) nets the H2 FY26 charge against the H1 FY27 credit (net 10.81 Mn charge), so it is the cleaner base. A21-2 offers "a single quarter ex-earnout" as an equal option.

Survives: YES. A4 names the reversal risk (rev L318, A21-3, Q21). It does not size the credit against the ETR, the normalized PAT growth or the A21 base. Graft into Step 4 (rev L318), A21-1 to A21-3 and the EARNINGS QUALITY flag: "Q2 ex-earnout ETR is 31.95% before the 14.48 Mn US deferred-tax credit. The credit is 9.2% of Q2 normalized PAT and about a third of its YoY gain. A single-quarter A21 base annualises 5.79 Cr of a credit that reversed in H2 FY26; prefer TTM." Type: MISSING.

Also tested, does NOT survive: filing-basis days "Improving" and CCC -22.9 days (rev L339-L342, L386). On quarter-annualised revenue, receivable days still improve (76.0 to 71.0 days). Inventory days worsen slightly (160.0 to 162.7). A4 already shows the deck basis (DIO 153 to 162) and lands on a STRUCTURAL direction. No graft.

### Arithmetic for newly tested figures

| Metric | Recomputed | Source lines | Status |
|---|---|---|---|
| Cons op EBITDA margin, Q1 to Q2 FY27 | 10.477% to 8.693% (-178 bps) | res L538-L548 | new figure |
| GM / employee / other-expense ratio change QoQ | -53.3 / +3.3 / +121.8 bps (sum -178.4) | res L538-L546 | new figure |
| Other-expense ratio Q1 FY26 / Q2 FY26 / H2 FY26 / Q1 FY27 / Q2 FY27 | 291.05 / 2,784.27 = 10.45%; 14.13%; 826.71 / 6,724.24 = 12.29%; 10.23%; 11.45% | res L538, L546 | new figure |
| Combined opex ratio, same periods (Q2 FY26 employee 529.42 corrected) | 31.21 / 31.18 / 29.55 / 27.47 / 28.72% | res L538, L543, L546 | new figure |
| Standalone other-expense ratio Q1 FY26 / Q2 FY26 / Q1 FY27 / Q2 FY27; combined H2 FY26 | 13.34 / 18.81 / 13.34 / 15.47%; (527.80 + 829.71) / 5,006.78 = 27.11% | res L538, L543, L546 | new figure |
| Base-spike part of the other-expense leg | (14.133 - 12.294)% x 3,930.90 = 72.3 Mn of 105.52 Mn | res L538, L546 | new figure |
| Core PBT QoQ | 219.45 to 166.98 Mn (-23.9%) | res L539, L548 | new figure |
| Segment increments, mapping A / B | 707.1 + 274.0 = 981.0 Mn (119%); 466.4 + 415.3 = 881.7 Mn (107%) of 824.56 Mn | pres L334-L362; res L538 | new figure |
| Subsidiary deferred tax Q2 FY27 / Q2 FY26 / H1 FY26 / H2 FY26 / H1 FY27 | (14.48) / (3.93) / (17.33) / +24.35 / (13.54) Mn | res L550 | new figure |
| Ex-earnout ETR before the subsidiary credit | 67.47 / 211.18 = 31.95% | res L548, L551, L288 | new figure |
| Normalized PAT ex the subsidiary credit | 121.77 to 143.71 Mn (+18.0%) | res L213, L288, L550, L552 | new figure |
| Normalized PAT ex FX and ex the credit | 136.39 to 129.48 Mn (-5.1%) | res L286, L548, L550-L551 | new figure |
| Interest paid H1 | 143.09 to 95.86 Mn (-33.0%) | res L248 | new figure (LF1) |
| Finance cost, standalone / subsidiaries, Q2 YoY | 49.34 to 39.85 Mn / 18.77 to 21.16 Mn | res L544 | new figure (LF1) |

No mismatch exists in A4's figures. Every grafted number recomputes within rounding. The figures above are new and support the counters.

## L1-5. VERDICT

INCOMPLETE. Failing agent: A4. Finding types: CONTRADICTION (LC1), FACTUAL (LF1), MISSING (N1, N2, N3).

All run-1 items (C1, C2, M1-M4, S1-S5) are closed. Coverage stands. No number in A4's tables is wrong. LC1 and LF1 trace to my own run-1 fix texts. All five fixes are text grafts in A4. No A2 or A3 re-run is needed.

Exact gap: A4 to:
1. LC1: change rev L477 to "revenue rose in four of the five measured QoQ moves; Q3 FY26 dipped 2.36%; Q1 FY26 QoQ is ND".
2. LF1: at rev L320, L388 and Q10, replace the deck-versus-balance-sheet conflict with the untestable-YoY wording in LF1.
3. N1: add the QoQ margin decomposition (-178 bps = GM -53, employee +3, other expenses +122) and the two readings of the YoY opex leverage (separating observation: Q3 FY27 combined opex ratio vs H2 FY26 29.55%) to Step 4 L301/L315, Step 2C Q2 and brief L615. Scope 6B test 2 L444 to YoY. Add the combined opex ratio to 8C.
4. N2: add the breadth line (Aerospace + Industrial increments 881.7-981.0 Mn exceed the 824.56 Mn increase; the other 22% shrank 6-15%; Auto & Others NOT DISCLOSED [INFERENCE]) to Step 2C Q1 and the brief, with one question.
5. N3: add the US deferred-tax line (ETR 31.95% before the 14.48 Mn credit; 9.2% of normalized PAT; normalized PAT +18.0% without it; H1 FY26 credit 17.33 Mn reversed as an H2 FY26 charge of 24.35 Mn; a Q2-annualised base carries 5.79 Cr; prefer TTM) to Step 4 L318, A21-1 to A21-3 and the EARNINGS QUALITY flag.

## L1-6. STYLE NOTES
LS1 and LS2 above, logged only. No re-run.

```yaml
stage: A5-adversary
company: "CYIENTDLM"
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
  - {claim: "The cause is materials, not overheads; other-expense leverage -268 bps Recurring; core PBT +20.86% Positive (rev L225, L257-L258, L301, L315, L444, L615)", counter: "QoQ op EBITDA margin -178 bps = gross margin -53, employee +3, other expenses +122 bps (other expenses +17.7% on revenue +5.2%), so 70% of the QoQ fall is opex; the YoY other-expense leg is measured against the highest filed ratio (Q2 FY26 14.13% vs H2 FY26 12.29%), about 72 of the 105.52 Mn; the 28.82 Mn core PBT gain rests wholly on opex leverage and core PBT fell 23.9% QoQ; two readings (Q2-seasonal opex vs a Q2 FY26 spike with leverage partly reversing), separated by the Q3 FY27 combined opex ratio vs H2 FY26 29.55%", source_line: "res L538-L548; pres L255-L257", type: MISSING}
  - {claim: "Revenue Strong +26.54%; Aerospace is the engine; this lane works (rev L218, L256, L632, L648)", counter: "Aerospace and Industrial increments (881.7-981.0 Mn across the two slice mappings) exceed the 824.56 Mn YoY increase; the other 22% of revenue shrank 6-15% (5-17% across rounding) while Defence +13% and Med Tech +14%, so Auto & Others fell sharply, value not disclosed; Aerospace alone gave 57-86% of the increase [INFERENCE]", source_line: "pres L334-L362; res L538; A1 pres R131-R148 slices unassigned", type: MISSING}
  - {claim: "Ex-earnout ETR 25.09% is normal; a single quarter ex-earnout is a valid A21 base (rev L318, L476-L478)", counter: "Subsidiary deferred-tax credit 14.48 Mn; ex-earnout ETR 31.95% without it; credit is 9.2% of Q2 normalized PAT and 32.5% of its YoY gain (3.93 to 14.48 Mn); normalized PAT +18.0% without it and -5.1% ex FX and ex credit; the 17.33 Mn H1 FY26 subsidiary credit reversed as a 24.35 Mn H2 FY26 charge; a Q2-annualised A21 base carries 5.79 Cr of it, TTM nets it", source_line: "res L213, L286, L288, L549-L552", type: MISSING}
findings_by_type:
  factual:
    - "LF1: rev L320, L388 and Q10 (L535) set the deck's YoY 'lower working capital borrowings' cause against a Mar-to-Sep 2026 balance move; the 30-Sep-2025 balance is NOT FOUND; H1 FY26 repayments (992.96 + 746.72 Mn) and interest paid -33.0% (143.09 to 95.86 Mn) fit the deck; the whole YoY finance-cost fall is standalone (49.34 to 39.85 Mn) (res L243-L248, L544; pres L381-L385). Originates in A5 run-1 counter P3."
  missing:
    - "N1: QoQ margin decomposition (opex 125 of 178 bps) and the two readings of the YoY opex leverage absent; the Q3 make-or-break tests gross margin only (res L538-L548; rev L301, L444, L512-L516, L615)"
    - "N2: revenue breadth absent: Aerospace + Industrial exceed 100% of the YoY increase; the other 22% of revenue shrank 6-15% (pres L334-L362; res L538)"
    - "N3: the 14.48 Mn US deferred-tax credit is not sized against the 25.09% ETR, the +25.85% normalized PAT growth or the single-quarter A21 base (res L549-L552; rev L318, L476-L478)"
  contradiction:
    - "LC1: rev L477 'revenue rose in five of six quarters' vs rev L269 Q1 FY26 QoQ ND; four of five measured QoQ moves rose (pres L247-L250; res L538). Originates in A5 run-1 C2 fix text."
  style:
    - "LS1: rev L232 'mostly interest' rests on H1 interest (res L212); Q2 split NOT FOUND; tag [INFERENCE from H1]"
    - "LS2: rev L381 'EBITDA fell each half since'; only one half follows H2 FY26"
loop_back_to: "A4"
gap: "A4 to (1) LC1: rev L477 read 'revenue rose in four of the five measured QoQ moves; Q3 FY26 dipped 2.36%; Q1 FY26 QoQ is ND'; (2) LF1: at rev L320, L388 and Q10 replace the deck-vs-balance-sheet conflict with 'the deck YoY cause cannot be tested: the 30-Sep-2025 balance is NOT FOUND; H1 FY26 repayments (992.96, 746.72 Mn) and a 33% fall in interest paid (143.09 to 95.86 Mn) fit it; the H1 FY27 build (gross borrowings +24.3%) points to higher finance cost from Q3 [INFERENCE]'; (3) N1: add the QoQ margin decomposition (op EBITDA -178 bps = GM -53, employee +3, other expenses +122; other expenses +17.7% on revenue +5.2%) and the two readings of the YoY opex leverage (Q2-seasonal opex vs a Q2 FY26 spike partly reversing; separating observation Q3 FY27 combined opex ratio vs H2 FY26 29.55%) to Step 4 L301 and L315, Step 2C Q2 and brief L615; scope the 6B test 2 p11 sentence (L444) to YoY; add the combined opex ratio as a co-reading in 8C; (4) N2: add to Step 2C Q1 and the brief that Aerospace and Industrial increments (881.7-981.0 Mn) exceed the 824.56 Mn YoY increase and the other 22% of revenue shrank 6-15%, so Auto & Others fell sharply, value NOT DISCLOSED [INFERENCE], plus one question; (5) N3: add to Step 4 L318, A21-1 to A21-3 and the EARNINGS QUALITY flag that Q2 ex-earnout ETR is 31.95% before the 14.48 Mn US deferred-tax credit (9.2% of normalized PAT; normalized PAT +18.0% without it), that the 17.33 Mn H1 FY26 credit reversed as a 24.35 Mn H2 FY26 charge, and that a Q2-annualised A21 base carries 5.79 Cr of it, so TTM is the cleaner base"
style_notes:
  - "LS1: rev L232 tag the 'mostly interest' read as [INFERENCE from H1]; Q2 interest split NOT FOUND"
  - "LS2: rev L381 replace 'fell each half since' with 'fell to 68.94 Mn in H1 FY27 and to 11.51 Mn in Q2 FY27'"
analyst_note: "Loop 1 closed every run-1 item. C1, C2, M1-M4 and S1-S5 are in place, and each grafted figure recomputes from the fulltexts. Two of my run-1 fix texts were wrong, and A4 adopted both. 'Five of six quarters rose' should read four of five measured QoQ moves. The deck's YoY 'lower working capital borrowings' cause cannot be tested against a March-to-September balance move; H1 FY26 repayments and a 33% fall in interest paid fit it. The fresh pass found surviving counters on three bullish reads. QoQ, opex caused 125 of the 178 bps margin fall, so 'materials, not overheads' holds only YoY, and the Q3 test needs the opex ratio. Aerospace and Industrial gave more than all of the YoY revenue increase; the rest of the mix shrank. The 25.09% ex-earnout ETR rests on a 14.48 Mn US deferred-tax credit, and a similar credit reversed last H2; a single-quarter A21 base carries 5.79 Cr of it. All fixes are text grafts, and no table number changes. To bound the loop, scope the loop-2 re-audit to closure of these five items, with no new adversarial pass."
```

---
---

# LOOP 2 RE-AUDIT (2026-10-17, final; no further loop exists)

Agent: A5 adversary, fresh instance | Model: claude-opus-5-5 | Loop iteration: 2
Under audit: the loop-2 work/review_cyientdlm_q2fy27.md (A4 loop_iteration 2) and work/blocks/a4.yaml. In this section "rev L###" means a line of the LOOP-2 review. The earlier sections keep their own line numbers.
Inputs read: this audit file (run 1 and loop 1), work/blocks/a5.yaml (loop 1), A1 results fulltext (res L160-L294, L530-L565), A1 presentation fulltext (pres L240-L394), the loop-2 review and the A4 block. No source PDF, nothing under inputs/, no A3 file.
Scope (orchestrator): (1) deliverable gate on the revised review; (2) closure of LC1, LF1, N1, N2 and N3, with every grafted figure recomputed from the A1 fulltexts at the cited lines; (3) a check that the revised passages introduced no new FACTUAL, MISSING or CONTRADICTION finding. No new adversarial pass beyond the revised passages. No full arithmetic sweep.

## L2-0. DELIVERABLE-COMPLETENESS (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT (rev L620-L638; 18 lines at L621-L638, inside the 10-20 line band) | sector PRESENT (rev L640-L647) | business model PRESENT (rev L649-L657) | competition PRESENT (rev L659-L664) | forward map PRESENT (rev L666-L679; make-or-break reading at L667 with the opex co-reading; 9 dated rows at L671-L679, each with a bull fork and a bear fork). Gate: PASS.

## L2-1. COVERAGE

Stands from run 1. No ledger or extraction changed. The A4 preamble (rev L13-L23) and block (notes 8, turns 0, slides 21, all_reviewed true) keep the run-1 counts. Q30 (rev L562) comes from A5 counter N2, not from a ledger row. Orphan rows: none. Rows missing from the ledger: none. Not re-run.

## L2-2. CLOSURE OF LOOP-1 ITEMS (grafted figures recomputed)

| Item | Where A4 grafted it (rev) | Recomputed from the A1 fulltexts | Source lines | Status |
|---|---|---|---|---|
| LC1 | L483 (FLAG A21-2) | Text now: "revenue rose in four of the five measured QoQ moves; Q3 FY26 dipped 2.36%; Q1 FY26 QoQ is ND". QoQ: 3,106.34 / 2,784.27 = +11.57%; 3,033 / 3,106.34 = -2.36%; 3,691 / 3,033 = +21.69%; 3,738.00 / 3,691 = +1.27%; 3,930.90 / 3,738.00 = +5.16%. Four rises in five. Q1 FY26 = 5,890.61 - 3,106.34 = 2,784.27 Mn, which ties to deck 2784. Added clause "other expenses ran higher in Q2 than Q1 in both years": ratio 10.45% to 14.13% (FY26) and 10.23% to 11.45% (FY27). | pres L247-L250; res L538, L546 | CLOSED |
| LF1 | L326, L394, L542 (Q10), L718, L765 | Text now says the YoY cause "cannot be tested" (untestable). 30-Sep-2025 borrowings: NOT FOUND (the balance sheet prints 30-Sep-26 and 31-Mar-26 only). HY Sep-25 repayments 992.96 Mn (current) and 746.72 Mn (non-current) against 823.58 Mn of proceeds. Interest paid 143.09 to 95.86 Mn = -33.0%. Q2 finance cost: consolidated 68.11 to 61.01 Mn (-7.10); standalone 49.34 to 39.85 Mn (-9.49); subsidiaries 18.77 to 21.16 Mn (+2.39). Gross borrowings 778.25 + 283.00 = 1,061.25 Mn to 359.89 + 959.71 = 1,319.60 Mn (+24.34%). | res L163-L190, L243-L248, L544 | CLOSED |
| N1 | L258, L302, L317-L321, L450, L522, L536, L591, L624-L625, L667, L673, L742, L761 | Op EBITDA Q1 FY27 391.63 Mn (10.477%) to Q2 341.70 Mn (8.693%) = -178.4 bps. GM 37.944% to 37.411% (-53.3 bps); employee 17.237% to 17.270% (+3.3); other expenses 10.230% to 11.448% (+121.8); opex 125.1 of 178.4 bps. Other expenses 382.41 to 450.02 Mn (+17.7%) on revenue +5.16%. Core PBT 219.45 to 166.98 Mn (-23.9%). Other-expense ratio: Q1 FY26 291.05 / 2,784.27 = 10.45%; Q2 FY26 14.13%; H2 FY26 826.71 / 6,724.24 = 12.29%; Q1 FY27 10.23%; Q2 FY27 11.45%. Combined ratio (Q2 FY26 employee 529.42; Q1 FY26 1,107.24 - 529.42 = 577.82; H2 FY26 2,267.78 - 1,107.24 = 1,160.54): 31.21 / 31.18 / 29.55 / 27.47 / 28.72%. Q1-to-Q2 rises +368 and +122 bps. Base-spike part (14.133 - 12.294)% x 3,930.90 = 72.3 Mn = 7.23 Cr of the 105.5 Mn (10.55 Cr) leg. Combined QoQ +125 bps. | res L538-L548; pres L255-L257 | CLOSED |
| N2 | L257, L562 (Q30), L622, L644, L660, L738, L762 | YoY increase 3,930.90 - 3,106.34 = 824.56 Mn. Mapping A: Aerospace 1,847.52 / 1.62 = 1,140.44, +707.08; Industrial 1,218.58 / 1.29 = 944.64, +273.94; sum 981.02 Mn = 119.0%. Mapping B: 466.36 + 415.34 = 881.70 Mn = 106.9%. Other 22% = 864.80 Mn against a base of 1,021.26 (A, -15.3%) or 921.94 (B, -6.2%). Aerospace alone 56.6-85.8%. Across all six assignments of the 14 / 7 / 1% slices to Defence, Med Tech and Auto & Others, Auto & Others fell at least about 14.5%, so "fell sharply" holds at INFERENCE tier. | pres L334-L362; res L538 | CLOSED |
| N3 | L233, L324, L482-L484, L629, L758, L767 | Subsidiary deferred tax Q2 FY27 (16.12) - (1.64) = (14.48) Mn; current tax 69.11 - 69.44 = (0.33). Ex-earnout PBT 393.13 - 181.95 = 211.18; ETR 52.99 / 211.18 = 25.09%; before the credit 67.47 / 211.18 = 31.95%. Credit / normalized PAT 14.48 / 158.19 = 9.15%. Q2 FY26 subsidiary deferred tax (2.57) - 1.36 = (3.93). Ex the credit: 121.77 to 143.71 Mn (+18.0%). Ex FX after tax (x 0.7483) and ex the credit: 136.39 to 129.48 Mn (-5.07%). Subsidiary deferred tax H1 FY26 (17.33), H2 FY26 +24.35, H1 FY27 (13.54); TTM net +10.81 Mn charge. Annualised credit 4 x 14.48 = 57.92 Mn = 5.79 Cr; 2 x 13.54 = 27.08 Mn = 2.71 Cr. Bases 632.76 Mn = 63.28 Cr; 642.08 Mn = 64.21 Cr. H1 ex-earnout ETR 112.24 / 433.28 = 25.90%. Brief credit 14.48 Mn = Rs 1.45 Cr. | res L213, L286, L288, L548-L552 | CLOSED |
| LS1, LS2 | L233; L387 | "[INFERENCE from H1 ...]" tag present. Other other-income: 226.61 - 195.75 + 19.54 = 50.40 Mn to 226.15 - 181.95 - 19.01 = 25.19 Mn (-25.21). L387 now reads "fell from 148.43 Mn in H2 FY26 to 68.94 Mn in H1 FY27 and to 11.51 Mn in Q2 FY27". | res L212, L213, L286, L288, L539 | CLOSED |

Residue check: a grep of the loop-2 review for "does not support", "disagree", "conflicts with the balance", "five of six", "six quarters rising", "four rising", "fell each half" and "most likely in other income" finds nothing. The remaining "conflicts" (rev L536, Q4) and "contradicted" (rev L761, GROSS MARGIN flag) are both scoped to YoY. The block in work/blocks/a4.yaml matches the block embedded in the review (rev L683-L776).

## L2-3. REVISED PASSAGES: NEW-DEFECT CHECK

The loop-2 grafts introduced no new FACTUAL, MISSING or CONTRADICTION finding. Every grafted figure recomputes. No grafted sentence goes beyond its source. The revised passages agree with each other. Step 2C Q2, Step 4, 6B test 2, 8C, Q4, monitorable 3, the forward map and the GROSS MARGIN flag all carry the same QoQ decomposition and the same 29.55% separating observation.

One item came up inside a revised row. It most likely predates loop 2.

OI-1. CONTRADICTION (A4; open item, no loop exists). The Q10 bull answer (rev L542) reads "Internal cash; borrowings are US refinancing only".
- India accounts for all of the H1 borrowing rise. Consolidated gross borrowings rose 258.35 Mn (1,061.25 to 1,319.60 Mn; res L170, L177).
- Standalone took 287.91 Mn of new current borrowings (res L177, L565), from 287.08 Mn of proceeds (res L243).
- Subsidiary borrowings fell 29.56 Mn (1,061.25 to 1,031.69 Mn). They drew 95.31 Mn (382.39 - 287.08; res L243) and repaid 140.12 Mn (res L245).
- The review's own Q7 (rev L539), Step 5B (rev L374) and DEBT flag (rev L765) state the India borrowing. So the filing already rules out this bull answer.
- Effect: a Role 5 scorer could mark a management answer as bull when the filing contradicts it. No number, flag, test status or verdict changes.
- Origin: the loop-2 graft rewrote the Q10 question and "Why" cells. The bull cell most likely predates loop 2. Both earlier A5 passes read this row (the run-1 cite was rev L535). work/ holds no earlier copy of the review to date it.
- Fix (one cell): bull answer "Operating cash and the India short-term line fund the build, repaid from collections by Q4; US borrowings refinanced, not grown".

STYLE (logged, no loop):
- LS3. Rev L320 (reading b) cites pres L378-L379 for the deck's "investment" cause. That deck note explains the YoY employee-cost rise. QoQ the employee ratio moved +3 bps and other expenses +122 bps. So reading (b) rests on the p11 note (pres L255-L257). Drop the L378-L379 cite, or scope it to employee cost.

## L2-4. ARITHMETIC (loop-2 figures only)

No full sweep (scope). The L2-2 table recomputes every loop-2 grafted figure. Mismatches above rounding: none.

## L2-5. VERDICT

INCOMPLETE, on one open item. Failing agent: A4. Finding type: CONTRADICTION (OI-1).
- LC1, LF1, N1, N2, N3, LS1 and LS2 are CLOSED. Every grafted figure recomputes within rounding.
- The loop-2 grafts introduced no new finding.
- OI-1 sits in a revised row but most likely predates loop 2. The fix is one cell in a hypothetical answer.
- No further loop exists. OI-1 goes forward as an open item, flagged, not looped.
- Coverage and arithmetic stand. No A2 or A3 re-run is needed.

Exact gap: the rev L542 Q10 bull answer "Internal cash; borrowings are US refinancing only" contradicts the filed H1 borrowing composition (standalone +287.91 Mn new current borrowings; subsidiaries -29.56 Mn; res L170, L177, L243, L245, L565). It also contradicts the review's own Q7, Step 5B and DEBT flag.

## L2-6. STYLE NOTES
LS3 above, logged only. No re-run.

```yaml
stage: A5-adversary
company: "CYIENTDLM"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
loop_iteration: 2
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
closed_items: [LC1, LF1, N1, N2, N3, LS1, LS2]
findings_by_type:
  factual: []
  missing: []
  contradiction:
    - "OI-1: rev L542 Q10 bull answer 'Internal cash; borrowings are US refinancing only' contradicts the filed H1 borrowing composition: consolidated +258.35 Mn (1,061.25 to 1,319.60) = standalone +287.91 Mn new current borrowings (proceeds 287.08) and subsidiaries -29.56 Mn (drew 95.31, repaid 140.12) (res L170, L177, L243, L245, L565); the review's own Q7 (L539), Step 5B (L374) and DEBT flag (L765) state the India borrowing. Not introduced by the loop-2 grafts as far as the record shows; open item, no loop."
  style:
    - "LS3: rev L320 reading (b) cites pres L378-L379, which explains the YoY employee-cost rise; QoQ employee moved +3 bps and other expenses +122 bps; the reading rests on pres L255-L257"
loop_back_to: "A4"
no_further_loop: true
open_items:
  - "OI-1 (CONTRADICTION, owner A4): rev L542 Q10 bull answer; one-cell fix to 'Operating cash and the India short-term line fund the build, repaid from collections by Q4; US borrowings refinanced, not grown'. Flag at close; do not loop."
gap: "Final loop; no re-run. Open item OI-1: rev L542 Q10 bull answer 'Internal cash; borrowings are US refinancing only' contradicts the filed H1 borrowing composition (standalone +287.91 Mn new current borrowings; subsidiaries -29.56 Mn; res L170, L177, L243, L245, L565) and the review's own Q7, Step 5B and DEBT flag. One-cell fix; flag, do not loop."
style_notes:
  - "LS3: rev L320 drop the pres L378-L379 cite from reading (b) or scope it to employee cost; reading (b) rests on pres L255-L257"
analyst_note: "Loop 2 closed all five loop-1 items. LC1 now reads four rises in five measured QoQ moves. LF1 drops the deck-versus-balance-sheet conflict. The YoY finance-cost cause is untestable without the 30-Sep-2025 balance, and H1 FY26 repayments and a 33% fall in interest paid fit it. A4 grafted N1, N2 and N3 across Step 2C, Step 4, 6B, 6.5, 8C, Q30, the brief and the flags. Every figure recomputes from res L538-L552 and pres L334-L362. The grafts introduced no new defect. One contradiction sits inside the revised Q10 row. Its bull answer, 'borrowings are US refinancing only', cannot be true: the whole H1 borrowing rise is India's 287.91 Mn, and subsidiary borrowings fell 29.56 Mn. It most likely predates loop 2, and both earlier A5 passes missed it. It is a one-cell fix to a hypothetical answer and changes no number, flag or verdict. No loop remains, so it goes forward as a flagged open item. The tagging rule makes the verdict INCOMPLETE. The review is otherwise complete."
```
