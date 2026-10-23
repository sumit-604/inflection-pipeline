# A5 ADVERSARY / COMPLETENESS AUDIT: GHV Infra Projects Limited (GHVINFRA), Q2 FY27 (RE-AUDIT, iteration 2)

Agent: A5 adversary | model: claude-opus-5-5 | run date: 2026-10-23 | iteration: 2 (after correction loop 1; one-iteration cap, final audit)
Instruction file: prompts/quarterly-a5-adversary.md
Inputs read (only these):
- A4 review (loop 1): runs/ghvinfra-q2fy27/work/review_ghvinfra_q2fy27.md (865 lines)
- A1 fulltext (the spine): runs/ghvinfra-q2fy27/extracted/ghvinfra-results-q2fy27-fulltext.md (843 lines, unchanged since the base run)
- A1 structured: runs/ghvinfra-q2fy27/extracted/ghvinfra-results-q2fy27-structured.md (R001-R821, unchanged)
- A2 ledger: runs/ghvinfra-q2fy27/work/ledger_results_ghvinfra_q2fy27.md (253 rows, unchanged)
- A5 base-run audit (gap list): runs/ghvinfra-q2fy27/work/audit_ghvinfra_q2fy27_base.md
Not opened: the source PDF and everything under inputs/. A3 reasoning was not read. Every figure below was re-derived from the fulltext.
Anchors: "l###" = fulltext line. "review l###" = A4 review line (loop 1 file). Units: Rs Lakhs (L) as filed; Rs Cr = L x 0.01.

---

## BASE-RUN GAP CLOSURE (iteration 1 findings vs loop 1 review)

| Base ID | Type | Base gap | Status | Evidence in loop 1 review |
|---|---|---|---|---|
| F1 | FACTUAL | Q6 gave the subsidiaries 19.78% of H1 C PAT | CLOSED | review l609, l806: 19.51% (482.78 / 2,474.39 L); 19.78% labelled subsidiaries plus JV at review l111. Recomputed 19.511% and 19.784% (l573, l578, l642) |
| F2 | FACTUAL | Brief said FY26 subsidiary revenue had "no direct cost" | CLOSED | review l235, l623, l741, l820: 0.69 Cr construction cost net of WIP. Recomputed 1,101.69 - 1,031.74 - 0.47 = 69.48 L, 6.99% of 994.23 L (l333, l335, l625, l627) |
| M1 | MISSING | Orphans L030, L134, L080, L158; "parent exposure ND" | CLOSED, with two new defects at the fix site (F-A, M-A below) | review l84, l254, l282, l389, l395, l411-412, l427, l491, l535, l552, l586, l607, l632-635, l684, l716, l762-763 |
| M2 | MISSING | Orphan L082, 59.18 Cr deposits from "Others" | CLOSED, with two new defects at the fix site (F-B, F-C below) | review l394, l403, l409, l432, l636, l695 |
| M3 | MISSING | Orphans L055, L056, L074, L075, 171.87 Cr non-trade liabilities | CLOSED | review l390-393, l398, l410, l432, l637, l695, l742 |
| M4 | MISSING | Summary dropped "up to"; Erisha link tiered FILED | CLOSED | review l715: "Up to Rs 40.52 Cr ... the Erisha link is INFERENCE" |
| M5 | MISSING | Promoter conversion economics absent | CLOSED, with one new gap at the fix site (M-B below) | review l66-72, l82, l106, l388, l537, l615, l655, l672, l694, l721, l764 |
| S1 | STYLE | Anchor l70 for "Formerly Sindu Valley" | CLOSED | review l128 cites l101, l257, l320 |
| S2 | STYLE | Forward map out of date order | CLOSED | review l758-768: dated rows run Now, 22-Jan, 14-Feb, 30-May, 14-Aug, 22-Aug |
| S3 | STYLE | "completed" for the Erisha contract end | CLOSED | review l654: "ended early" |
| S4 | STYLE | Stray l640 heading | CLOSED | review l495 (FN20, watchlist item 7) |
| S5 | STYLE | Rounding-level differences | no action (logged) | unchanged |
| S6 | STYLE | In-cell cash qualifier | CLOSED | review l247, l749 |
| S7 | STYLE | C CF finance cost add-back 2,527.52 vs 2,529.38 L | CLOSED | review l495 (FN21) |

A5 self-correction. In the base run, my Claim 3 said the warrant allotment date "is NOT FOUND in this filing". On this run my fresh pass found that ledger row R302 (l448, H1 FY26 column) narrows it. A4 carried my base-run wording, so this gap belongs to A5 as much as to A4. It is raised below as M-B.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

DELIVERABLE-COMPLETENESS: PASS. All five labelled brief parts are present and carry real content.

| Brief part | Heading (review line) | Status | Content check |
|---|---|---|---|
| 1. Summary narrative | "### 1. SUMMARY NARRATIVE" (review l703) | present | 20 lines (review l705-724), at the top of the 10-20 band. "Up to" and the INFERENCE tag restored (l715). The parent exposure line (l716) and the conversion price line (l721) are new |
| 2. Sector intelligence | "### 2. SECTOR INTELLIGENCE" (review l726) | present | 5 bullets. The West Asia quote ties to l483-484. Gaps stated as NOT FOUND |
| 3. Business-model intelligence | "### 3. BUSINESS-MODEL INTELLIGENCE" (review l734) | present | 9 bullets. The F2 fix is at l741. The non-trade liability line is at l742 |
| 4. Competition intelligence | "### 4. COMPETITION INTELLIGENCE" (review l746) | present | 5 bullets. The cash qualifier sits in the "Where GHV wins" bullet (l749) |
| 5. Forward map | "### 5. FORWARD MAP" (review l754) | present | A make-or-break line plus 9 catalysts. Each row has a bull fork and a bear fork. 6 rows carry dates. The warrant row says "NOT FOUND", but the extract supports an inferred latest date (M-B) |

Gate result: no part missing or empty. The gate does not fail.

---

## 1. COVERAGE AUDIT

### 1A. Fresh enumeration over the fulltext vs the A2 ledger

Method: a fresh grep pass over the fulltext (l1-l843), run without reference to the A2 counts, then a diff. The fulltext, structured file and ledger have not changed since the base run. I re-ran the pass anyway.

| Category | A2 count | A5 fresh count | Fresh-pass evidence | Orphan rows | Status |
|---|---|---|---|---|---|
| Notes, standalone | 8 | 8 | grep of numbered paragraphs: l463, l467, l470, l476, l481, l491, l493, l494 | none | MATCH |
| Notes, consolidated | 11 | 11 | l765, l768, l770, l772, l775, l778, l783, l787, l795, l796, l797 | none | MATCH |
| Footnotes (EPS asterisk) | 2 | 2 | l358, l662 | none | MATCH |
| Line items, all six statements | 196 | 196 | grep of value-terminated table lines = 196 (S P&L 26 confirmed by line sweep l328-l357) | none | MATCH |
| Zero-standing cells | 41 | 41 | 39 dash cells on 24 lines (S P&L l335, l345; S BS l376, l377, l383, l398; S CF l426, l431, l433, l442, l443, l445, l449, l451, l453; C P&L l627, l637, l644, l653, l656; C BS l680, l681, l687, l702) + 2 "Nil" at l572 | none | MATCH |
| Board agenda items | 4 | 4 | l42, l52, l60, l76 | none | MATCH |
| Annexures | 3 | 3 | l118, l174, l812 | none | MATCH |
| Auditor paragraphs | 11 | 11 | S l258, l266, l275, l296; C l514, l523, l531, l543, l561, l569, l591 | none | MATCH |
| Consolidation entities (excl. parent) | 4 | 4 | l545-l548; l770-l771 | none | MATCH |
| Turns / questions / slides | 0 | 0 | results filing | n/a | MATCH |
| Structured IDs | 821 | 821 | grep "^R### \|" = 821; ledger header orphan_ids [] | none | MATCH |
| Ledger rows | 253 | 253 | grep of row IDs (L001-L196, A01-G06) = 253 | none | MATCH |

Fresh-pass units absent from the structured file: none new. The l640 stray heading (base S4) is now logged in A4's drafting record (review l495).

missing_from_ledger = [].

### 1B. Ledger rows vs A4 review (orphan test)

The nine base-run orphans now carry explicit reads:

| Ledger row | Structured IDs (value checked) | Fulltext line | A4 citation (loop 1) | Status |
|---|---|---|---|---|
| L030 | R190 1,189.90; R191 985.12 | l374 | review l389, l411, l632 | CITED |
| L134 | R505 0.50; R506 0.50 | l678 | review l411 (unit slip, F-A), l607 | CITED |
| L080 | R291 (204.78); R292 dash | l442 | review l389, l411, l632 | CITED |
| L158 | R553 11,686.62; R554 12,075.60 | l708 | review l84, l412, l427, l604 | CITED |
| L082 | R295 5,918.44; R296 (960.00) | l444 | review l394, l403, l409, l636 | CITED |
| L055 | R240 9,758.29; R241 6,794.95 | l405 | review l390, l392, l410, l637 | CITED |
| L056 | R242 7,428.62; R243 5,003.12 | l406 | review l391, l392, l410, l637 | CITED |
| L074 | R279 3,227.61; R280 1,364.02 | l435 | review l393, l410 | CITED |
| L075 | R281 2,392.10; R282 11.96 | l436 | review l393, l410 | CITED |

No new orphan row arises from the loop 1 text. The new reads cite l410, l427, l443, l446, l692, l709-710, l714 and l746, and each of those rows is cited.

One cited row carries an unread cell. Ledger row l448 is cited for its H1 FY27 cell R301 (6,666.67 L). Its H1 FY26 cell R302 (3,850.00 L) is not interpreted anywhere in the review, and it carries the warrant timing (M-B). This is a MISSING interpretation, not an orphan.

Coverage verdict: PASS on enumeration and on the orphan test. orphan_rows = [].

---

## 2. ARITHMETIC AUDIT (every figure changed at the loop 1 fix sites)

"PASS" = matches within rounding (0.01 Cr, 0.01 pp). Figures outside the fix sites passed in the base run, and their inputs have not changed.

| Metric | A4 value (review line) | Recomputed (from Lakhs) | Source line | Status |
|---|---|---|---|---|
| Conversion price per share | Rs 80.00 (l66) | 6,666.67 L / 83,33,335 = Rs 80.0000 | l448, l472 | PASS |
| Upfront vs this-quarter split | 16.67 + 50.00 = 66.67 (l66) | 1,666.67 + 5,000.01 = 6,666.68 L; "balance consideration" at l470 supports the earlier part-payment | l448-449, l470 | PASS |
| Price / FY26 S EPS | 13.65x (l67) | 80 / 5.86 = 13.652x | l356 | PASS |
| TTM S EPS; price / TTM EPS | Rs 6.96; 11.50x (l67) | 5,595.36 L / 8,04,08,335 = Rs 6.9587; 80 / 6.9587 = 11.496x | l347, l475 | PASS |
| Price / FY26 C EPS | 11.76x (l67) | 80 / 6.80 = 11.765x | l660 | PASS |
| S BVPS; price / book | Rs 25.26; 3.17x (l67) | 20,313.57 L / 8,04,08,335 = Rs 25.263; 3.167x | l393, l475 | PASS |
| Price as % of CMP | 33.47% (l68) | 80 / 239 = 33.473% | Notion CMP (review l37) | PASS |
| Converted tranche at CMP; gap | 199.17; 132.50 (l68) | 83,33,335 x 239 = 199.17 Cr; less 66.67 = 132.50 | l472 | PASS |
| Pending tranche cost; still due; at CMP; gap | 87.33; 65.50; 260.91; 173.58 (l69) | 1,09,16,665 x 80 = 87.33 Cr; x 75% = 65.50; x 239 = 260.91; 260.91 - 87.33 = 173.58 | l475 | PASS |
| Still-due share of current borrowings | 17.33% (l69) | 6,550.00 / 37,789.84 = 17.333% | l402 | PASS |
| Paid-up capital rise | 4.17 (416.67 L) (l82) | 4,020.42 - 3,603.75 = 416.67 L | l353 | PASS |
| Subsidiary third-party trade payables, Sep-26 / Mar-26 / rise | 11.42 / 1.49 / 9.93 (l84, l412, l427) | 11,686.62 - 10,544.75 = 1,141.87 L; 12,075.60 - 11,926.60 = 149.00 L; rise 992.87 L | l404, l708 | PASS |
| Group exposure net of trade payables | about 29.10 (l84) | 4,051.91 - 1,141.87 = 2,910.04 L | l381, l386, l685, l690 | PASS (see STYLE ST3 on the net basis) |
| C investments | "0.50 Cr" (l411) | 0.50 L = Rs 0.005 Cr | l678 | FAIL (FACTUAL F-A, unit) |
| Investments eliminated on consolidation | 11.89 (l411) | 1,189.90 - 0.50 = 1,189.40 L | l374, l678 | PASS (computed in Lakhs; the unit label only is wrong) |
| S-over-C current OFA | 13.50 (l411) | 45,214.27 - 43,864.36 = 1,349.91 L | l384, l688 | PASS |
| Funded parent exposure; low end of range | 25.39; 25.11 (l395, l411) | 2,539.31 L; less JV losses 21.88 + 6.74 L = 2,510.69 L | l641 | PASS |
| Funded exposure Mar-26; change | 27.53; (2.14) (l395) | 984.62 + 1,768.76 = 2,753.38 L; 2,539.31 - 2,753.38 = (214.07) L | l374, l384, l678, l688 | PASS (see STYLE ST2) |
| Fall in what subsidiaries owe the parent | 4.19 (l412) | 1,768.76 - 1,349.91 = 418.85 L | l384, l688 | PASS |
| Subsidiaries' booked external liabilities; contingent ceiling | 12.21; 37.61 (l411) | 76,587.87 - 75,366.48 = 1,221.39 L; 2,539.31 + 1,221.39 = 3,760.70 L | l410, l714 | PASS on arithmetic; scope qualifier missing (M-A) |
| Funded exposure ratios | 12.50% of S NW; 0.86x H1 S PAT; 68.6% of H1 S core PBT (l282, l411) | 2,539.31 / 20,313.57 = 12.501%; / 2,963.91 = 0.857x; / 3,701.34 = 68.60% | l393, l347, l341, l329 | PASS |
| Ceiling as % of S NW | 18.51% (l411) | 3,760.70 / 20,313.57 = 18.513% | l393 | PASS |
| Consolidation bridge closes "only with" the 13.50 Cr (l411) | stated | 95,680.05 + 4,075.53 - 1,189.40 - 1,349.91 + 10.32 = 97,226.59 L, exact to l692. The 10.32 L residual is the C-over-S DTA (244.63 - 234.31, l376, l680) | l388, l572, l692 | PASS (see STYLE ST1) |
| S investments rise | +2.05 (l389) | 1,189.90 - 985.12 = 204.78 L = CF l442 | l374, l442 | PASS |
| OFL; OCL | 67.95 to 97.58, +29.63; 50.03 to 74.29, +24.26 (l390-391) | +2,963.34 L; +2,425.50 L | l405, l406 | PASS |
| OFL + OCL vs trade payables | 117.98 vs 141.99; 171.87 vs 158.48; +53.89 vs +16.50 (l392) | 11,798.07 / 14,198.54; 17,186.91 / 15,848.41; +5,388.84 / +1,649.87 L | l403-406 | PASS |
| Non-trade liabilities in days of H1 revenue | 60.6 (l410) | 17,186.91 / 51,868.22 x 183 = 60.64 | l328, l405-406 | PASS |
| CF liability lines; CFO without them | 13.76 / 56.20, +42.44; (300.56) (l393) | 1,375.98 / 5,619.71 L; (24,436.77) - 5,619.71 = (30,056.48) L | l435-436, l439 | PASS |
| CF excess over BS change in OFL + OCL + provisions | 54.24; 1.96 (l410) | 2,963.34 + 2,425.50 + 4.24 + 30.59 = 5,423.67 L; 5,619.71 - 5,423.67 = 196.04 L | l397, l405-407, l435-436 | PASS |
| Deposits swing; multiple of PAT; investing CF without them | +68.78; 2.0x; (67.87) (l394, l409) | 5,918.44 + 960.00 = 6,878.44 L; 5,918.44 / 2,963.91 = 1.997x; (868.75) - 5,918.44 = (6,787.19) L | l444, l446, l347 | PASS |
| Yield cap on the deposits | "caps the yield ... at 0.99% for the half [derived]" (l409); "implied yield is at most 0.99% ... so the deposits were mostly non-interest-bearing [derived]" (l636) | 58.39 / 5,918.44 = 0.987% holds as a ratio. It is a cap only if the full 59.18 Cr stayed out for all 183 days. l444 is a net H1 flow, and the filing gives neither the maturity dates nor the Mar-26 gross balance. Example: maturity at mid-half puts the same interest at about 1.97% of the average balance | l427, l444 | FAIL (FACTUAL F-B, premise) |
| Reclassification remainder | "The remaining 90.54 Cr at most" (l403) | 14,972.48 - 5,918.44 = 9,054.04 L holds. But A4 says only "up to" 59.18 Cr of the fall is deposit maturity. So 90.54 is the remainder only if all of it sat in this line. If less sat here, the candidate is larger, up to 149.72 Cr. "At most" inverts the bound | l375, l444 | FAIL (FACTUAL F-C, bound direction) |
| Q6 subsidiaries alone; with JV | 19.51%; 19.78% (l111, l609) | 482.78 / 2,474.39 = 19.511%; 489.52 / 2,474.39 = 19.784% | l573, l578, l642 | PASS |
| FY26 subsidiary direct cost | 0.69 Cr, 7.0% (l235) | 69.48 L / 994.23 L = 6.99% | l333, l335, l625, l627 | PASS |

Arithmetic verdict: every recomputation matches within rounding. Three items FAIL on the claim built on the figure: a unit label (F-A), an unsupported cap premise (F-B), and an inverted bound (F-C).

---

## 3. ADVERSARIAL READ

### 3A. Base-run positive claims: graft check

| # | Positive claim (base) | Base bear counter | Graft now in A4? | Status |
|---|---|---|---|---|
| 1 | Revenue growth strong (+63.30% Q2, +96.30% H1) | 371.90 Cr WC build, 71.7% of H1 revenue (l328, l429, l432) | YES, in-cell at review l247 and l749; Step 5 | closed |
| 2 | "The headline is real at the core level" (core PBT +37.88%) | Parent funded exposure up to 25.39 Cr, 68.6% of H1 S core PBT, unprovided (l374, l384, l486-487, l678, l688) | YES, review l254, l282, l411 | closed |
| 3 | Promoter capital in; conversion a bull funding event | Rs 80 a share = 11.50x TTM S EPS, 33.47% of CMP; pending 87.33 Cr vs 260.91 Cr at CMP (l448, l472-475) | YES, review l66-72, l615, l764, l694 | closed (see M-B on the allotment window) |

### 3B. New claims introduced in loop 1 (adversarial read)

N1. "Contingent ceiling 37.61 Cr only if guaranteed" (review l84, l395, l411, l535, l552, l586, l607, l673, l684, l763; YAML l804, l849).
The word "ceiling" tells the reader that the parent cannot lose more than 37.61 Cr. The figure is funded exposure (25.39 Cr) plus the subsidiaries' booked external liabilities (12.21 Cr, l714 less l410). The filing says the outcome depends on "the ongoing discussions and related legal proceedings". It also says "the financial implications, if any, cannot presently be determined" (l485-487). No balance sheet carries a claim or counterclaim by Rana Exim against GHV Infra FZ-LLC. A parent performance guarantee would pass that claim to the parent. That is the same "if guaranteed" case in which A4 applies the ceiling. A4's own Q3 (review l606) lists "Counterclaim against GHV" as the bear answer, but the ceiling text leaves it out.
Survives? YES. The extract cannot bound the unbooked claim side. Graft required (M-A): label 37.61 Cr as a ceiling on booked balances only. State that claim or counterclaim amounts and any performance guarantee are NOT FOUND (l485-487) and sit outside it.

N2. "So they were mostly non-interest-bearing ... not treasury deposits" (review l409; Q33 at l636 tags it [derived]).
The 0.99% "cap" holds only if the full 59.18 Cr stayed out for the whole half. The filing gives only a net H1 flow (l444, "Deposits (Placed)/Matured with Others"). It gives no dates and no opening gross balance. Interest income of 58.39 L (l427) also covers the 22.40 Cr placed with banks in H1 (l443). The inference may be right, but the extract cannot derive it.
Survives? YES, as a FACTUAL correction (F-B). Keep the 0.99% ratio. State its premise, and tag the conclusion INFERENCE, not derived.

N3. "The remaining 90.54 Cr at most is the candidate reclassification" (review l403).
The bear direction matters here. A bigger reclassification means more of the 109-day rise in receivables plus current OFA days (review l377, RED) is a move between balance-sheet lines, not new money owed. "At most" understates that case. It tilts the structural vs growth test toward structural further than the extract supports. Rule J sets the same bar for bull and bear claims. The extract supports a range. The candidate is 90.54 Cr if all 59.18 Cr sat in the non-current line and up to 149.72 Cr if none did. Other operating settlements inside the l432 line could lower it.
Survives? YES, as a FACTUAL correction (F-C). The cash classification (INDETERMINATE-WITH-DIRECTION) does not move, because the line the deposits sat in is already a named missing item (Q33).

N4. Funded parent exposure "fell" from 27.53 to 25.39 Cr (review l395, change (2.14)).
Bear counter: the whole fall is the 4.19 Cr drop in what the subsidiaries owe the parent. A4 itself reads that drop as more likely a re-label than a cash repayment (review l412). The parent also put in 2.05 Cr of fresh cash (l442). Nothing in the extract shows a recovery.
Survives? A4 already says this in substance at review l412. No graft required. Optional in-cell note (STYLE ST2).

### 3C. Mandatory acquisition-economics probe (re-run)

Subsidiary infusion: 2.05 Cr (l442) went in against a 4.83 Cr H1 subsidiary loss (l573) on Nil revenue (l572). The multiple is negative. No earnings case exists. A4 now carries this as Q29 (review l632) and in Step 5 (l411). Closed.

Promoter stake purchase: Rs 80 / TTM S EPS Rs 6.96 = 11.50x, against a market P/E of 34.35x. This is now in 0C (review l67-68).

The same extract gives new evidence. Ledger row l448, H1 FY26 cell R302, shows "Proceeds from Issue of Equity Shares" of 3,850.00 L. That equals 25% of 38,50,000 warrants x Rs 400 to the paisa [derived: 16,66,667 + 21,83,333 = 38,50,000; x Rs 400 = 154.00 Cr; x 25% = 38.50 Cr]. The 25% split fits the converted tranche (16.67 Cr utilised, l449, = 25% of 66.67 Cr). Paid-up capital did not move between Sep-25 and Jun-26 (l353), so the 38.50 Cr was not a share issue in that window.

Reading: the warrants were most likely allotted, and the Rs 400 price fixed, in H1 FY26 (Apr-Sep 2025) [INFERENCE]. Under the ICDR 18-month warrant tenure, the 21,83,333 pending warrants must convert or lapse by 31-Mar-2027 at the latest. On lapse, about 21.83 Cr of upfront money is forfeited to the company [INFERENCE, regulatory frame; not in the filing].

Three effects follow:
- (a) A4's forward-map date "NOT FOUND" (review l764) and monitorable M4 (l655) can carry an inferred latest date.
- (b) A4's separating observation (l72) narrows to the H1 FY26 market price and floor price. Both are still NOT FOUND.
- (c) The lapse bear fork is not one-sided. Forfeiture keeps the upfront money without dilution.

Survives? YES (M-B). The graft leaves A4's two readings as they are. It dates the catalyst and makes the lapse fork symmetric.

---

## FINDINGS REGISTER (tagged)

| ID | Type | Agent | Gap (exact) | Exact fix | Anchors |
|---|---|---|---|---|---|
| F-A | FACTUAL | A4 | review l411 says "C keeps 0.50 Cr of investments (l678)". The filed value is 0.50 L = Rs 0.005 Cr. The derived 11.89 Cr is correct, because it was computed in Lakhs | Replace with "C keeps 0.50 L (Rs 0.005 Cr) of investments (l678)" | review l411; l678 |
| F-B | FACTUAL | A4 | review l409 says interest income "caps the yield ... at 0.99% for the half [derived]". Q33 (l636) concludes "so the deposits were mostly non-interest-bearing [derived]". The cap holds only if the full 59.18 Cr was out for all 183 days. l444 is a net H1 flow, and the filing gives neither the maturity dates nor the opening gross balance | l409: "H1 interest income of 0.58 Cr (l427) is 0.99% of the 59.18 Cr [derived]. That caps the half-year yield only if the full amount stayed out all half; maturity dates and the Mar-26 gross balance are NOT FOUND (l444 is a net flow). On that premise they were mostly non-interest-bearing ... [INFERENCE]." Q33 l636: replace "[derived]" on the conclusion with "[INFERENCE; maturity dates NOT FOUND]" | review l409, l636; l427, l443, l444 |
| F-C | FACTUAL | A4 | review l403 says "The remaining 90.54 Cr at most [derived] is the candidate reclassification". The deposits explain only "up to 59.18 Cr" of the fall. So 90.54 Cr is the remainder only if all of it sat in this line. Otherwise the candidate is larger, up to 149.72 Cr. The bound is inverted | Replace with "If all 59.18 Cr sat in this line, the remaining 90.54 Cr is the candidate reclassification; if less sat here, the candidate is larger, up to the full 149.72 Cr [derived; the deposits' line is NOT FOUND, Q33] [INFERENCE]" | review l403; l375, l444 |
| M-A | MISSING | A4 | The 37.61 Cr "contingent ceiling" covers booked balances only (25.39 funded + 12.21 booked subsidiary liabilities). Claim or counterclaim amounts in the "related legal proceedings" and any parent performance guarantee are NOT FOUND (l485-487). Under a guarantee, 37.61 Cr does not cap them. The ceiling text goes into the Notion Key Notes (l673) | At review l411 add: "The 37.61 Cr bounds booked balances only. Claim or counterclaim amounts in the legal proceedings (l485-487) and any parent performance guarantee are NOT FOUND and sit outside it." Elsewhere (l84, l395, l535, l552, l586, l607, l673, l684, l763; YAML l804, l849) replace "ceiling 37.61" with "booked-balance ceiling 37.61 (claims and performance guarantees NOT FOUND, outside it)" | review l84, l395, l411, l535, l552, l586, l606-607, l673, l684, l763; l485-487, l410, l714 |
| M-B | MISSING | A4 | Structured R302 (l448, H1 FY26) 3,850.00 L = 25% x 38,50,000 warrants x Rs 400, exact. The warrants were most likely allotted in H1 FY26 [INFERENCE]. Under ICDR 18-month tenure, the pending 21,83,333 convert or lapse by 31-Mar-2027 at the latest. On lapse, about 21.83 Cr of upfront money is forfeited to the company [INFERENCE]. A4 says "Warrant allotment date ... NOT FOUND" (l70) and "Neither is in this filing" (l72). It dates the forward-map and M4 rows "NOT FOUND" (l655, l764) | l70: "Not stated. H1 FY26 'Proceeds from Issue of Equity Shares' 3,850.00 L (l448) equals 25% of 38,50,000 warrants x Rs 400 [derived], so allotment was most likely in H1 FY26, Apr-Sep 2025 [INFERENCE]; exact date and floor price NOT FOUND." l72: "The filing narrows the allotment to H1 FY26 [INFERENCE]; the market and floor price then are not in it." l764 date: "by 31-Mar-2027 at the latest [INFERENCE: upfront in H1 FY26, l448; ICDR 18-month tenure]", and add to the bear fork "(on lapse about Rs 21.83 Cr upfront is forfeited to the company, no dilution [INFERENCE])". Same date at l655, l694 and YAML l838 | review l66, l70, l72, l655, l694, l764, l838; l448, l449, l353, l470-475 |
| ST1-ST5 | STYLE | none | See STYLE NOTES | as listed | as listed |

No CONTRADICTION finding. Review l432 and Q34 (l637) give customer advances two different roles. At l432 they are a drag on future CFO. At Q34 they are a bull answer. The two lines measure different things, cash timing and payer quality, so they do not conflict.

---

## VERDICT

VERDICT: INCOMPLETE.

- Failing agent: A4. Gaps:
  1. F-A: fix the "0.50 Cr" unit label at review l411. [FACTUAL]
  2. F-B: state the premise of the 0.99% yield cap. Re-tier the "non-interest-bearing" conclusion as INFERENCE (l409, l636). [FACTUAL]
  3. F-C: fix the inverted "at most 90.54 Cr" reclassification bound (l403). [FACTUAL]
  4. M-A: limit the 37.61 Cr ceiling to booked balances. Name unbooked claims and guarantees as NOT FOUND (l84, l395, l411, l535, l552, l586, l607, l673, l684, l763). [MISSING]
  5. M-B: from R302 (l448), date the pending warrant conversion "by 31-Mar-2027 at the latest [INFERENCE]". Narrow the allotment window to H1 FY26. Add the forfeiture leg to the lapse fork (l70, l72, l655, l694, l764). [MISSING]
- Iteration cap. This is iteration 2, the final audit. Under the one-iteration cap, these five items go to the orchestrator and operator as open items. Each has exact replacement text in the register above. None needs re-derivation.
- Not affected: the deliverable gate passes. The enumeration matches A2 in every category. Every base-run FACTUAL and MISSING item is closed. Every changed figure recomputes within rounding. No finding moves the protocol verdict (PROCEED WITH FLAGS), the cash classification (INDETERMINATE-WITH-DIRECTION), or the AVOID framing.

---

## STYLE NOTES (logged; no loop)

- ST1. Review l411 says the consolidation bridge closes "only with" the 13.50 Cr. It closes exactly with one more item: 10.32 L of C-over-S deferred tax asset (244.63 - 234.31, l376, l680). Bridge: 95,680.05 + 4,075.53 - 1,189.40 - 1,349.91 + 10.32 = 97,226.59 L (l692). Name the item so a reader can repeat the check.
- ST2. The 5-S row (review l395) shows funded exposure "(2.14)". Add in-cell: "not a recovery; the 4.19 Cr intra-group fall is read as a re-label (FN28), with 2.05 Cr of fresh cash in (l442)".
- ST3. "About 29.10 Cr net" (review l84, l412) is net of trade payables only. Net of all 12.21 Cr of booked subsidiary liabilities (the 37.61 Cr basis), it is about 28.31 Cr. Say "net of trade payables" or align the basis.
- ST4. The 25.39 Cr is labelled "Erisha exposure" (review l282, l411). It covers both subsidiaries, FZ-LLC and GHV Infra Inc. (Ohio). "Up to" keeps it a valid ceiling for the Erisha share. A clearer label is "exposure to the two subsidiaries (FZ-LLC holds Erisha)".
- ST5. In the forward map, the "undated" row and the two "NOT FOUND" rows sit between the 14-Feb-2027 and 30-May-2027 rows. Move them to the end. The dated rows are in order. If M-B is applied, the warrant row takes the date 31-Mar-2027, which falls between those two rows.

---

```yaml
stage: A5-adversary
company: "GHVINFRA"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
iteration: 2
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
base_run_gaps_closed: [F1, F2, M1, M2, M3, M4, M5, S1, S2, S3, S4, S6, S7]
arithmetic_mismatches:
  - metric: "C investments (unit label)"
    a4_value: "0.50 Cr (review l411)"
    recomputed: "0.50 L = Rs 0.005 Cr; derived 11.89 Cr eliminated is correct (1,189.90 - 0.50 L)"
    source_line: "fulltext l374, l678"
  - metric: "Yield cap on 59.18 Cr deposits matured from Others"
    a4_value: "caps the yield at 0.99% for the half [derived] (review l409, l636)"
    recomputed: "58.39 / 5,918.44 = 0.987% as a ratio; a cap only if the full 59.18 Cr was out all 183 days; l444 is a net H1 flow, dates and opening gross balance not filed"
    source_line: "fulltext l427, l443, l444"
  - metric: "Non-current OFA fall: candidate reclassification"
    a4_value: "remaining 90.54 Cr at most (review l403)"
    recomputed: "90.54 Cr (14,972.48 - 5,918.44 L) only if all 59.18 Cr sat in this line; otherwise larger, up to 149.72 Cr; bound inverted"
    source_line: "fulltext l375, l444"
surviving_bear_counters:
  - claim: "Parent Erisha exposure has a contingent ceiling of 37.61 Cr if guaranteed"
    counter: "37.61 Cr = 25.39 funded + 12.21 booked subsidiary liabilities only; claim or counterclaim amounts in the related legal proceedings and any parent performance guarantee are NOT FOUND and are not capped by it (financial implications 'cannot presently be determined')"
    source_line: "fulltext l410, l485-487, l714; review l84, l395, l411, l606-607, l673, l684"
    type: MISSING
  - claim: "Warrant allotment date NOT FOUND; pending conversion undated; lapse leaves only a funding gap"
    counter: "H1 FY26 equity proceeds 3,850.00 L = 25% x 38,50,000 warrants x Rs 400 exactly, so allotment most likely H1 FY26 [INFERENCE]; ICDR 18-month tenure puts conversion or lapse by 31-Mar-2027 at the latest, with about 21.83 Cr upfront forfeited to the company on lapse [INFERENCE]"
    source_line: "fulltext l353, l448, l449, l470-475; review l70, l72, l655, l694, l764"
    type: MISSING
  - claim: "Deposits from Others were mostly non-interest-bearing [derived]"
    counter: "the 0.99% cap needs a full-half balance; maturity dates and opening gross balance are not filed; the conclusion is INFERENCE"
    source_line: "fulltext l427, l444; review l409, l636"
    type: FACTUAL
findings_by_type:
  factual:
    - "F-A (A4): review l411 'C keeps 0.50 Cr of investments'; filed 0.50 L = Rs 0.005 Cr (l678); 11.89 Cr derived figure unaffected"
    - "F-B (A4): review l409/l636 '0.99% yield cap [derived]' and 'mostly non-interest-bearing [derived]' rest on an unfiled full-half balance; l444 is a net flow; restate premise, tier conclusion INFERENCE"
    - "F-C (A4): review l403 'remaining 90.54 Cr at most' inverts the bound; 90.54 only if all 59.18 Cr sat in non-current OFA, else larger up to 149.72 Cr"
  missing:
    - "M-A (A4): 37.61 Cr 'contingent ceiling' lacks the scope qualifier: booked balances only; unbooked claims/counterclaims and any performance guarantee NOT FOUND (l485-487); sites l84, l395, l411, l535, l552, l586, l607, l673, l684, l763"
    - "M-B (A4): R302 (l448 H1 FY26 3,850.00 L) ties to 25% upfront on 38,50,000 warrants at Rs 400; allotment most likely H1 FY26; pending warrants convert or lapse by 31-Mar-2027 at the latest, forfeiture on lapse [INFERENCE]; sites l70, l72, l655, l694, l764"
  contradiction: []
  style:
    - "ST1: name the 10.32 L C-over-S DTA residual in the consolidation bridge (review l411; l376, l680, l692)"
    - "ST2: annotate the (2.14) funded-exposure change as not a recovery (review l395; l412, l442)"
    - "ST3: 'about 29.10 Cr net' is net of trade payables only; about 28.31 Cr net of all 12.21 Cr booked subsidiary liabilities"
    - "ST4: 25.39 Cr covers both subsidiaries (FZ-LLC and Ohio); label as exposure to the two subsidiaries"
    - "ST5: move undated and NOT FOUND forward-map rows to the end"
loop_back_to: "A4"
gap: "A4 (iteration cap reached; route as operator open items, exact replacement text in the audit register): F-A fix 'C keeps 0.50 Cr' to '0.50 L (Rs 0.005 Cr)' at review l411 [FACTUAL]; F-B restate the 0.99% yield cap as conditional on a full-half balance and tier 'mostly non-interest-bearing' as INFERENCE at l409 and Q33 l636 [FACTUAL]; F-C replace 'remaining 90.54 Cr at most' with '90.54 Cr if all 59.18 Cr sat in this line, larger up to 149.72 Cr otherwise' at l403 [FACTUAL]; M-A qualify the 37.61 Cr ceiling as booked balances only, unbooked claims and performance guarantees NOT FOUND (l485-487), at l84, l395, l411, l535, l552, l586, l607, l673, l684, l763 [MISSING]; M-B from R302 (l448 H1 FY26 3,850.00 L = 25% x 38,50,000 x Rs 400) narrow the allotment to H1 FY26 and date the pending conversion 'by 31-Mar-2027 at the latest [INFERENCE]' with forfeiture on lapse, at l70, l72, l655, l694, l764 [MISSING]."
style_notes:
  - "ST1: add the 10.32 L DTA residual to the consolidation bridge sentence"
  - "ST2: in-cell 'not a recovery' on the (2.14) change"
  - "ST3: state the net basis of 29.10 Cr (trade payables only) or align to 28.31 Cr"
  - "ST4: relabel 25.39 Cr as exposure to the two subsidiaries"
  - "ST5: undated forward-map rows to the end"
analyst_note: "Loop 1 closed every base-run gap. The nine orphan rows now have reads. Q6 and the subsidiary direct cost are fixed. The parent exposure, the conversion economics and the summary qualifier are now in the review. Every changed figure recomputes within rounding, and the consolidation bridge ties to the paisa. The five open items sit at the new fix sites. Three claims go further than their figures allow: a unit label, a yield cap that needs an unfiled full-half balance, and an inverted reclassification bound. A fourth item is a ceiling that leaves out the unbooked legal-claim side, which the filing says it cannot yet determine. That one matters because the text goes to Notion Key Notes. The fifth is my own base-run miss. H1 FY26 equity proceeds of 38.50 Cr equal 25% upfront on all 38.50 lakh warrants at Rs 400. That places the allotment in H1 FY26 and the pending conversion or lapse by Mar-2027 at the latest. All five are text edits with exact wording in the register. None moves PROCEED WITH FLAGS, INDETERMINATE-WITH-DIRECTION or AVOID. The cap is reached, so the operator decides whether to approve the edits before the Notion save."
```
