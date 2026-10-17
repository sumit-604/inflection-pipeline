# A5 AUDIT: Eimco Elecon (India) Limited (EIMCOELECO) | Q2 FY27 | Loop 1 re-audit

Run: /run-quarterly A5 adversary | Model: claude-opus-5-5 | Date: 2026-10-17
Review under audit: runs/eimcoeleco-q2fy27/work/review_eimcoeleco_q2fy27.md (Revision: Loop 1)
Prior audit: work/audit_eimcoeleco_q2fy27.run1.md (not read; its block, work/blocks/a5-audit.yaml, was read only after this audit's own derivation was complete, to check that Loop 1 items were applied)

Input discipline: I read only the three A1 fulltexts, the three A1 structured files, the three A2 ledgers and the A4 review. I did not open the source PDFs, anything under inputs/, or any A3 file. Every count and number below is re-derived from the fulltext. Anchor key: `res` / `pres` / `pr` = A1 fulltext line; `rev` = review line; `[d]` = my arithmetic on filed numbers (computed in Rs lakhs, then converted).

## LOOP 1 CHECK (prior A5 items)
| Prior item | Applied in review? | Where |
|---|---|---|
| A5-F01 (H2-heavy "both years") | Yes | rev L169, L317, L453 |
| A5-F02 (fixed-cost leverage attribution) | Yes | rev L133-134, L148, L182, L352, L458 |
| A5-M01 (base-effect qualifier) | Yes, but see A5-M03 below: the wording it adopted is incomplete | rev L139, L149, L434, L454-455 |
| A5-M02 (treasury liquidity) | Yes | rev L233-234, L239, L249, L320, L438 |
| S01, S04, S05 | Yes | rev L469, L210, L452 |
| S02, S03, S08 (rounding, deck gap, ED mitigant) | Not applied (STYLE, optional) | carried below as S12, S13, S16 |

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

PASS. All five parts of the PLAIN-LANGUAGE BRIEF are present and carry real content.
| Part | Status | Evidence |
|---|---|---|
| (1) Summary narrative | present | rev L451-466, 16 lines (inside the 10-20 line band) |
| (2) Sector intelligence | present | rev L469-474 (coal, metals, construction, payer mix) |
| (3) Business-model intelligence | present | rev L477-484 |
| (4) Competition intelligence | present | rev L487-491 |
| (5) Forward map | present | rev L494-501; 7 dated catalysts plus the make-or-break line, each with a bull and a bear fork |

---

## 1. COVERAGE AUDIT

Fresh pass method: page-marker grep on each fulltext; notes grep on res L187-194, L266, L328; line-by-line recount of every P&L, balance-sheet and cash-flow line (res L154-326); per-slide recount of numeric tokens on the table and chart slides; label-by-label recount of the results p7-8 and press-release p2-3 chart and remark numbers.

| Doc | Category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|---|
| results | notes | 7 | 7 (Notes 1-6 + unnumbered CF note, res L188-194, L266, L328) | none | PASS |
| results | line items | 99 | 99 (P&L 27, BS 36, CF 36 incl. M001 at res L322) | none | PASS |
| results | zero-standing | 11 | 11 (R125 Other Equity blank in five columns is a template blank, accounted as LI025) | none | PASS |
| results | agenda items | 2 | 2 (res L35, L41) | none | PASS |
| results | auditor paragraphs | 4 | 4 (res L94, L100, L108, L119) | none | PASS |
| results | annexures | 3 | 3 (A, B, C: res L79, L457, L481) | none | PASS |
| results | signatures | 4 | 4 (CS res L70-76; auditor res L125-136; ED res L337-339; CFO letter res L521-522) | none | PASS |
| results | entities | 29 | 29 | none | PASS |
| results | press-release numbers | 10 | 10 (res L395-414) | none | PASS |
| results | chart labels | 36 | 36 (24 on revenue/EBITDA, res L355-367; 12 on PAT/order book, res L376-384) | none | PASS |
| results | structured IDs | 470 + M001 | 470 + M001 | none | PASS |
| presentation | slides | 39 | 39 | none | PASS |
| presentation | slide numbers | 748 | 748 (recount: s15 34, s16 19, s17 10, s18 149, s19 146, s20 48, s28 8, s29 7, s30 8, s31 4, s36 81, s37 145, s38 48; others tie to ledger) | none | PASS |
| presentation | line items | 130 | 139 physical lines; 130 after the ledger's 9 same-label merges (PBT margin s18; investments, borrowings, lease, provisions on s19 and s37) | none | PASS (convention note S20) |
| presentation | zero-standing / entities / forward / dates / qualifiers | 93 / 73 / 18 / 72 / 35 | 93 / 73 / 18 / 72 / 35 | none | PASS |
| presentation | structured IDs | 946 | 946 | none | PASS |
| press release | pages | 4 | 4 | none | PASS |
| press release | numbers | 50 | 50 (36 chart, 10 remarks, 4 identifiers) | none | PASS |
| press release | entities / forward / dates / qualifiers | 14 / 7 / 14 / 7 | 14 / 7 / 14 / 7 | none | PASS |
| press release | structured IDs | 92 | 92 | none | PASS |

A4 citation check: rev L13 marks every ID range reviewed (results R001-R470 plus M001, presentation R001-R946, press release R001-R092). Every A2 flag is handled in the body: Z5/R150 (rev L18, L231), M001 (rev L21), H1 FY26 investing misalignment (rev L20, L222), text glitches R014/R153/R242/R267 (rev L19), OCI and earlier-period tax blanks (rev L59-60), new NC liability lines (M10, rev L424), TIMING_GAP (rev L66, Q9), FOOTNOTE_UNRESOLVED R462-R464 (rev L53, L122, Q6, Q10, Q20), LABEL_MISMATCH pr R092 (Q6), RESTATED deck pairs (rev L122). Orphan rows: none. Rows the fresh pass found that the ledger lacks: none.

---

## 2. ARITHMETIC AUDIT

All recomputation done in Rs lakhs from res L154-326, then x0.01. Tolerance: rounding of the last shown digit.

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Step 1 conversions, 21 lines x 6 periods | as tabled | all tie | res L154-186 | PASS |
| Q2 FY27 expense tie | 4,824.54 | 4,824.54 | res L158-167 | PASS |
| Q1 FY27 total income (glitch) | 85.28 | 7,752.31 + 775.94 = 8,528.25 | res L154-156 | PASS |
| Operating EBITDA Q2FY26/Q1FY27/Q2FY27/FY26/H1FY26/H1FY27 | 5.22/14.25/10.74/42.97/17.53/24.99 | 522.04/1,424.71/1,074.35/4,297.10/1,753.07/2,499.06 | res L155, L163, L164, L168 | PASS |
| Operating EBITDA margin | 15.71/18.38/18.92/18.62/17.39/18.61% | same | + res L154 | PASS |
| Reported EBITDA | 9.49/22.01/12.63/59.98/29.89/34.64 | same | res L163-168 | PASS |
| Core PBT (PBT - OI) | 2.62/11.86/8.55/33.35/12.94/20.41 | same | res L155, L168 | PASS |
| OI / PBT | 62.0/39.6/18.1/33.8/48.9/32.1% | same | res L155, L168 | PASS |
| ETR | 22.36/21.61/24.99/23.12/21.62/22.79% | same | res L168, L173 | PASS |
| PAT margin | 16.10/19.84/13.79/16.78/19.68/17.28% | same | res L154, L174 | PASS |
| Gross margin (filing basis) | 71.75/54.14/59.88/57.13/62.70/56.57% | same | res L154, L158-160 | PASS |
| Distributor / revenue; Other exp / revenue; Employee / revenue | as tabled | same | res L154, L162, L165, L166 | PASS |
| Distributor + other / revenue, H1 FY27 | 26.75% | 26.74% (3,592.21 / 13,432.03) | res L154, L165-166 | PASS (rounding, S12) |
| Release EBITDA cross-check | 18.92% and +105.8% vs 18.8% and 108.8% | 18.92%, +105.80% | res L403-404 | PASS |
| Deck margin gap | "0.1-0.3 pp" | 0.08-0.32 pp | pres L393, L704 | PASS (rounding, S13) |
| Deck "Other Expenses" = distributor + other | 16 = 15.83; 20 = 20.10 | ties (also 11 = 10.52; 36 = 35.92; 30 = 29.76) | pres L391 | PASS |
| Step 2 YoY set (rev +70.9, op EBITDA +105.8, margin +321 bps, D&A -15.1, FC -25.5, EBIT 2.78 to 8.67 +211.6, OI -55.7, core +226.4, PBT +51.5, PAT +46.4, EPS +46.3) | as tabled | all tie | res L154-185 | PASS |
| Q2 FY26 QoQ (Q1 FY26 = H1 - Q2) | 67.57; -50.8% | 6,756.99; -50.81% | res L154 | PASS |
| H1 YoY set (rev +33.2, op EBITDA +42.6, margin +122 bps, OI -22.0, core +57.7, PBT +18.8, PAT +17.0, EPS +17.0) | as stated | all tie; margin +121.5 bps | res L154-185 | PASS (rounding) |
| TTM core PBT | 40.82; +22.4% | 4,082.12; +22.40% | res L155, L168 | PASS |
| YoY margin decomposition | GM -1,187; employee +814; mfg +314; net -59; dist+other +380; ex-line margin 15.11% | -1,187.3; +813.8; +314.3; -59.2; +380.2; 15.11% | res L154, L158-166 | PASS |
| Other exp rupee growth; distributor rupee change | +92.3%; -19.6% | +92.26%; -19.64% | res L165-166 | PASS |
| Distributor-rate drop | 3.57 cr = 60% of 5.93 | 356.62 lakhs; 60.1% of 593.18 | res L154, L165 | PASS |
| Q1 FY26 core PBT; H2 FY26 quarterly average | 10.32; 10.21 | 1,032.14; 1,020.52 | res L155, L168 | PASS |
| ETR change and its cost | +263 bps; 0.28 | +263.6 bps; 27.52 lakhs | res L168, L173 | PASS (rounding, S12) |
| Q2 PAT bridge | 3.70 + 1.82 + 0.37 + 0.04 - 2.38 - 0.79 - 0.28 = 2.48; shares 149.2/73.4/14.8/1.7/-96.0/-32.0/-11.1% | 370.07 + 182.24 + 36.68 + 4.19 - 238.16 - 79.38 - 27.52 = 248.12; shares tie | res L154-174 | PASS |
| H1 PAT bridge | 5.83/1.63/0.13/-0.12/-2.71/-1.03/-0.35 = 3.38 | 582.83/163.16/12.88/-11.92/-271.39/-102.83/-35.03 = 337.70 on rounded components vs 337.71 filed | res L154-174 | PASS (0.01 lakh rounding) |
| OI reversion; core PAT | PBT 12.82, PAT 9.62; 6.41 vs 2.03 (+215%) | 1,282.40; 961.87; 641.43 vs 203.42 (+215.3%) | res L155, L168, L173 | PASS |
| Ex-deferred ETR; DTL change | 25.91%; -0.94 | 25.91%; 770.36 - 676.36 = 94.00 | res L170, L239 | PASS |
| FV gains share of OI; investment roll | 74.7%; 8.24 = 1.03 + 7.21 | 74.73%; 823.92 = 102.75 + 721.17 exactly | res L209, L216, L278, L305 | PASS |
| Step 3 set (Q1 FY26 margin 18.22%; H2 FY26 129.94 / 64.97 / 19.58%; Q1 FY27 +19.3% vs H2 average, +14.7% YoY; QoQ -26.7/-24.6/-27.9/-75.6/-46.8/-49.1; H2 56.3%; H1 average 67.16; threshold 173.1; 77%) | as stated | all tie | res L154-174 | PASS |
| CFO; CFO/PAT; CFO change | 1.84 / 6.04 / 22.11; 0.08x / 0.30x / 0.57x; -69.6% | 183.78 / 604.44 / 2,210.89; 0.079 / 0.305 / 0.571; -69.59% | res L174, L300 | PASS |
| FCF | (0.28) H1 FY27; (38.44) FY26 | (27.70); (3,844.02) lakhs | res L300, L303 | PASS |
| WC change | (15.76) / (6.08) / (11.31); -9.68 | (1,575.83) / (607.73) / (1,130.96); each equals CGO less OP before WC | res L285-296 | PASS |
| Receivable / inventory / payable days; CCC | 114.7 to 123.9; 400.4 to 361.2; 65.1 to 81.2; 450.0 to 403.9 | 114.66 to 123.89; 400.44 to 361.22; 65.05 to 81.18; 450.05 to 403.93 | res L154, L158-160, L214, L217, L252-257 | PASS (payables split ties to total CL at both dates) |
| PPE, CWIP, ONCA (Z5) | +47.44 (+74.0%); -1.12; 48.25 at Mar-26 | +4,744.12 (+74.00%); -111.66; NCA sums tie only with R150 in Mar-26 (31,717.32; 33,502.99) | res L204-212 | PASS |
| Net debt excluding investments | 3.55 to 5.75; +2.20 | 355.25 to 574.53; +219.28 | res L218-219, L235, L243-244 | PASS (rounding, S12) |
| Liquid net cash | 11.86 to (1.53); -13.39 | 1,186.31 to (152.54); -1,338.85 | res L216, L218-219, L243 | PASS |
| Net cash incl. all investments; ex-MTM | (200.98) to (207.03); +6.05; about -1.17 | 20,098.40 to 20,703.04; +604.64; -116.53 | res L209, L216, L218-219, L235, L243-244, L278 | PASS |
| Book non-current share; investments / total assets | 98.7%; 37.95% | 98.68%; 37.95% | res L209, L216, L224 | PASS |
| Stock-item moves (TR +25.8%, inventory +6.4%, CI -79.7%, OFL +110%, OCL -17.7%) | as stated | all tie | res L214-261 | PASS |
| Period-end current ratio; NFAT | 3.53; 2.22 | 3.525; 2.220 on TTM revenue / (PPE + CWIP + intangibles) | res L204-207, L223, L264 | PASS (basis unstated, S18) |
| FY23-FY26 OCF / PAT | 74 / 149 = 0.50x | 0.497x | pres L713, L762 | PASS |
| FY26 revenue fall "(247 to 231)" | -6.6% | -6.5% on deck figures; -6.6% on filed 230.75 vs deck 247 | pres L697; res L154 | PASS (basis, S12) |
| TTM set (revenue 264.26; op EBITDA 50.43 at 19.08%; OI 14.29; PAT 42.09; EPS 72.97) | as stated | 26,426.05; 5,043.09 at 19.08%; 1,429.08; 4,209.04; 72.97 | res L154-185 | PASS |
| Shares; net cash per share; BVPS | 57.684 lakh; 358.9; 846.7 | 576.84 / 10; 358.90; 846.70 | res L181, L231 | PASS |
| Order book / TTM revenue; Q3 margin at Q1 distributor rate; Q10 spares shares; Q11 fixed-cost recovery | 0.50x; 13.3%; 35% vs 48%; +1,128 bps | 0.503x; 13.26%; 35.1% vs 48.5%; +1,128.1 bps | res L154, L165, L364-366, L377 | PASS |
| Reserve-roll DPS | Rs 4.00 FY26; Rs 5.00 FY25 | 46,173.87 + 2,321.09 - 48,264.22 = 230.74 lakhs / 57.684 = Rs 4.00; 288.21 / 57.684 = Rs 5.00 | res L174, L230, L319 | PASS |
| Letter-to-board gap | 38 days | 5 Sep to 13 Oct = 38 days | res L32, L486 | PASS |
| Statement totals (BS both dates; CF all three columns incl. A+B+C and closing cash) | "all statements tie" | every total ties | res L204-326 | PASS |

Arithmetic mismatches above rounding: none.

---

## 3. ADVERSARIAL READ

### Claim 1 (data quality): "The filed numbers are clean: unmodified limited review, all statements tie, no exceptional items, standalone-only filer" (rev L434)
Strongest bear counter: every total ties, but two cells of the reviewed statements need correction before line-level use. The Other non-current assets value sits in the Sep-26 position yet ties only to Mar-26 (res L211-212). The H1 FY26 investing values do not match their labels: "Interest income" 10.15 equals the H1 FY26 dividend add-back (res L281, L306) and "Dividend income" shows (572.17) (res L307). The fulltext cannot show whether these are filing defects or text-layer artefacts.
Survives? Supported by the extract, but already in A4: rev L18-20 (data corrections), rev L222 (H1 FY26 capex ND). No graft needed. Wording fix only (S10).

### Claim 2 (earnings): "On less distorted bases core PBT grew 57.7% in H1 and 22.4% on TTM"; "TTM core PBT Rs 40.82 cr (+22.4% vs FY26)" (rev L139, L144, L149, L318, L434, L454, L586)
Strongest bear counter: the TTM base is not trough-free. TTM less FY26 equals H1 FY27 less H1 FY26, so the TTM gain (Rs 7.47 cr, 33.35 to 40.82) is the same Rs 7.47 cr as the H1 gain (12.94 to 20.41) [d, res L155, L168]. Rs 5.93 cr of it (79%) is the Q2 recovery off the Q2 FY26 trough. The only YoY comparison free of the trough, Q1 FY27 vs Q1 FY26, is +14.9% (10.32 to 11.86) [d]. On a two-year view the TTM levels have not recovered FY25:
- TTM EPS Rs 72.97 is 14.4% below FY25 EPS Rs 85.25 (pres L715) [d].
- TTM core PBT Rs 40.82 cr is below FY25's about Rs 48 cr (PBT 66 less OI 18, deck rounded, pres L705, L710).
- TTM operating EBITDA margin 19.08% is below the FY25 deck margin of 22.7% (pres L704).
- TTM revenue Rs 264.26 cr is only 7.0% above FY25's Rs 247 cr (pres L697) [d].
Survives? YES. The extract supports it and the review does not carry it. A4 cites FY25 only for the margin band (Q21) and the FY26 revenue fall (rev L247). GRAFT REQUIRED (A5-M03).

### Claim 3 (visibility): "The Rs 133 cr order book covers 77% of that threshold" (rev L172); order book +202% YoY (pres L354) as a candidate trigger (rev L310, L330, M6)
Strongest bear counter: the same figure is called an "open order pipeline" (res L413) and an "Order Book" (res L374). No sequential book is given, so H1 inflow and book-to-bill are unknown. Q2 revenue fell 26.7% QoQ in the quarter the ED credits to "robust execution of our order book" (res L396-397). Other current liabilities, the likely home of customer advances, fell 17.7% while the book tripled (res L261). Q2 built Rs 11.50 cr of finished goods and WIP (res L160). The book is for "complete mining solutions" (pres L355), which is equipment and presses gross margin.
Survives? Supported, but already in A4: Q6, Q7, Q12, Q13, Q19; rev L172 "before definition is confirmed"; rev L330 "Do not credit"; rev L483. No graft needed.

### Additional counter (cash): "Payable days lengthening (supports cash)" (rev L227) and Q18's bull fork "Capital creditors tied to the H1 asset" (rev L386)
Strongest bear counter: H1 FY27 CFO of Rs 1.84 cr includes a Rs 7.14 cr operating inflow from Other financial liabilities (res L294). The same line gave Rs 0.09 cr for all of FY26 and Rs 0.53 lakh in H1 FY26 (res L294). Without that one line, H1 CFO is Rs (5.30) cr [d: 183.78 - 713.83 lakhs]. Trade payables added another Rs 8.61 cr (res L292). The balance-sheet line it feeds doubled, from Rs 5.27 cr to Rs 11.10 cr (res L260). Q18 names capital creditors as the bull answer. If capital creditors sit inside this operating line, reported CFO is overstated by up to that amount and capex is understated. That answer is therefore a bear case for cash quality, not a bull case.
Survives? YES. The review gives the BS line (rev L237, Q18) but never ties it to the CFO figure, and the Q18 forks point the wrong way for cash. GRAFT REQUIRED (A5-M04).

### Mandatory acquisition-economics probe
Not triggered. None of the three documents describes an acquisition, a business purchase or a stake buy. The only purchase-like items are (a) the Rs 47.44 cr PPE capitalisation, an undisclosed asset with no target earnings (res L204, L211), and (b) net treasury purchases of Rs 1.03 cr (res L305). No consideration-to-PAT multiple can be formed. A4 already treats (a) as a disclosure gap (Q4, Q5).

---

## FINDINGS (tagged)

FACTUAL
- A5-F03: rev L474 says "the customer roster is mostly state-owned miners [MGMT, pres L513]". The slide lists 16 names (pres L515-532). Eight are state-owned: ECL, MCL, SECL, WCL, Singareni, MOIL, Hutti Gold, UCIL. Eight are private: Adept Mining, Inderdeep Infra, JMS Mining, Minop, Singh & Sons, SMS, Technoblast, Tata Steel. The deck itself cites "both public-sector and private-sector customers" (pres L356). rev L490 "dependence on state-owned buyers" has no filed support. The slow-payer inference that follows (rev L474) loses its stated base. Loop: A4.
  Fix text for rev L474: "Payer mix: the customer slide shows 16 names, 8 state-owned (four Coal India subsidiaries, Singareni, MOIL, Hutti Gold, UCIL) and 8 private (mining contractors and Tata Steel) [MGMT, pres L515-532]. The deck cites demand from both public and private customers [MGMT, pres L356]. A logo count gives no revenue or receivable share; Q2 asks for it. If state payers dominate receivables, slow payment would fit the cash picture [INFERENCE]." For rev L490, replace "dependence on state-owned buyers" with "an undisclosed customer mix".

MISSING
- A5-M03: the base-effect qualifier from Loop 1 is incomplete (Claim 2 above). Graft into Step 2 diagnostic 3 (rev L149), Step 6.5 TTM bullet (rev L318), the verdict (rev L434), the summary (rev L454) and the flag (rev L586). Suggested text: "TTM is not a trough-free base: the TTM core-PBT gain of Rs 7.47 cr equals the H1 gain, and Rs 5.93 cr of it is the Q2 recovery off the Q2 FY26 trough. The trough-free comparison, Q1 FY27 vs Q1 FY26, is +14.9%. TTM EPS of Rs 72.97 is 14.4% below FY25's Rs 85.25 [MGMT, pres L715], and TTM core PBT of Rs 40.82 cr is below FY25's about Rs 48 cr [MGMT, pres L705, L710]. Profit has not yet recovered the FY25 level." Loop: A4.
- A5-M04: the CFO dependency is absent (Additional counter above). Graft into Step 5 (after rev L224 or in the H1 cash-funding line, rev L239): "H1 CFO of Rs 1.84 cr includes a Rs 7.14 cr inflow from other financial liabilities (res L294), against Rs 0.09 cr in all of FY26. Without that line H1 CFO is Rs (5.30) cr [d]." Re-fork Q18: bull = operating accruals with a dated settlement, with CFO stated without them; bear = capital creditors carried inside operating cash flow, or dues that unwind in H2. Loop: A4.

CONTRADICTION
- A5-C01: rev L170 (Step 3) calls Q2 FY26 "the distorted base ... gross margin 71.75%, outlier vs every other period". rev L491 then reads the YoY gross-margin fall from that same base as possible tender pricing ("may reflect tender pricing, not only mix"). The sequential series the review omits points the other way [d, res L154, L158-160]: Q2 FY27 gross margin of 59.88% is above Q1 FY27 (54.14%), Q1 FY26 (58.25%), H2 FY26 (52.81%) and FY26 (57.13%). Under the A3-14 chart reading (spares = upper segment, res L364-367), the spares share is 48% (Q2 FY26), 35% (Q2 FY27), 21% (Q1 FY26) and 18% (Q1 FY27). Gross margin ranks in exactly that order. The extract shows a mix effect. It shows no price erosion. Fix: in rev L491, state the sequential series and the spares-share ranking before any pricing inference, and keep Q11 as the test. Loop: A4.

STYLE (logged, no loop): S10-S20 below.

---

## VERDICT

**INCOMPLETE.** Failing agent: A4. Gap: one FACTUAL (A5-F03, customer roster), two MISSING (A5-M03, TTM base and FY25 level; A5-M04, CFO dependency on the other-financial-liabilities inflow and the Q18 forks), one CONTRADICTION (A5-C01, outlier gross-margin base vs the tender-pricing inference). All four are grafts into the review text. None needs re-enumeration (A2) or new forensic work (A3). Coverage and arithmetic are clean. None of the four changes the protocol verdict PROCEED WITH FLAGS or the cash classification INDETERMINATE-WITH-DIRECTION; A5-M03 and A5-M04 sharpen existing flags.

---

## STYLE NOTES (logged, no re-run)
- S10: rev L434 "all statements tie" would read better as "all column totals tie". The R150 column position and the H1 FY26 investing labels need the corrections listed at rev L18-20.
- S11: rev L454 and L457 tag derived figures [FILED] (core PBT 2.62 to 8.55; operating margin 18.9% vs 15.7%; gross margin 71.8% vs 59.9%). Tag them [FILED, derived], as rev L452 and L455 already do.
- S12 (carries prior S02): rounding-basis artefacts with no conclusion change. H1 distributor plus other 26.75% vs 26.74%; H1 margin +122 vs +121.5 bps; Q2 ETR +263 vs +263.6 bps; net debt change +2.20 vs +2.19; FY26 revenue -6.6% labelled "(247 to 231)", which computes to -6.5% (the -6.6% uses filed 230.75 against deck 247).
- S13 (carries prior S03): rev L122 "0.1-0.3 pp below". The range is 0.08-0.32 pp.
- S14: rev L221 "-22.6 pp vs H1 FY26" applies pp to a ratio in x. Write "-0.23x".
- S15: forward map rev L500 "By 30 Apr 2027, statutory CFO window" drops the PENDING LIVE VERIFICATION tag that M3 (rev L417) carries. A shorter listing-regulation timeline for a CFO vacancy may apply. That is outside the extract and needs live verification before the date is relied on.
- S16 (carries prior S08): CFO flag balance (Rule J). ED Kamlesh Shah signs the statements (res L337-339) and is an ICAI fellow with about 27 years in financial operations and treasury management (pres L212-217). That is a continuity mitigant. It does not address the 38-day disclosure gap or the missing successor.
- S17: rev L233 "liquid net cash" excludes lease liabilities, while the two net-debt rows (rev L232, L234) include them. State the difference. With leases, the Sep-26 liquid position is Rs (2.93) cr [d].
- S18: rev L241 "NFAT 2.8 vs 2.22" does not state the 2.22 basis. It ties to TTM revenue / (PPE + CWIP + intangibles) = 264.26 / 119.03.
- S19 (carries prior S07): A4 coverage is a range-level "reviewed" statement (rev L13). Accepted. Row-level marking would make the next audit cheaper.
- S20 (carries prior S06, A2): the presentation ledger line_items count of 130 merges 9 same-label lines (139 physical). All IDs are referenced. A2 should state the convention.

```yaml
stage: A5-adversary
company: "EIMCOELECO"
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
  - claim: "On less distorted bases core PBT grew 57.7% in H1 and 22.4% on TTM; TTM core PBT Rs 40.82 cr, +22.4% vs FY26 (rev L139, L144, L149, L318, L434, L454, L586)"
    counter: "TTM is not trough-free. The TTM gain of Rs 7.47 cr equals the H1 gain (12.94 to 20.41), and Rs 5.93 cr of it (79%) is the Q2 recovery off the Q2 FY26 trough. The trough-free comparison, Q1 FY27 vs Q1 FY26, is +14.9% (10.32 to 11.86). TTM EPS Rs 72.97 is 14.4% below FY25 EPS Rs 85.25. TTM core PBT Rs 40.82 cr is below FY25 about Rs 48 cr (PBT 66 less OI 18, deck rounded). TTM operating EBITDA margin 19.08% is below FY25 22.7%. TTM revenue is only 7.0% above FY25 Rs 247 cr. Profit has not recovered the FY25 level."
    source_line: "res L154, L155, L168, L185 [d]; pres L697, L704, L705, L710, L715"
    type: MISSING
  - claim: "Payable days lengthening (supports cash); Q18 bull answer 'capital creditors tied to the H1 asset' (rev L227, L386)"
    counter: "H1 CFO Rs 1.84 cr includes a Rs 7.14 cr inflow from other financial liabilities (Rs 0.09 cr in all of FY26; Rs 0.53 lakh in H1 FY26). Without that line H1 CFO is Rs (5.30) cr. Trade payables added Rs 8.61 cr more. If capital creditors sit inside this operating line, reported CFO is overstated and capex understated, so the Q18 bull answer is a cash-quality bear."
    source_line: "res L260, L292, L294, L300 [d]"
    type: MISSING
findings_by_type:
  factual:
    - "A5-F03: rev L474 'the customer roster is mostly state-owned miners [MGMT, pres L513]' is unsupported. The slide lists 16 names: 8 state-owned (ECL, MCL, SECL, WCL, Singareni, MOIL, Hutti Gold, UCIL) and 8 private (Adept, Inderdeep, JMS, Minop, Singh & Sons, SMS, Technoblast, Tata Steel) (pres L515-532). The deck cites both public and private customers (pres L356). rev L490 'dependence on state-owned buyers' has no filed support. Loop A4."
  missing:
    - "A5-M03: the Loop 1 base-effect qualifier calls TTM a less distorted base, but the TTM core-PBT gain (Rs 7.47 cr) equals the H1 gain and 79% of it is the Q2 trough recovery. The trough-free Q1 YoY is +14.9%. TTM EPS Rs 72.97 is 14.4% below FY25 Rs 85.25 (pres L715); TTM core PBT is below FY25 about Rs 48 cr (pres L705, L710). Graft into rev L149, L318, L434, L454, L586. Loop A4."
    - "A5-M04: Step 5 never ties H1 CFO Rs 1.84 cr to the Rs 7.14 cr other-financial-liabilities inflow (res L294); without it H1 CFO is Rs (5.30) cr. Q18 (rev L386) labels capital creditors as the bull answer, which would mean CFO is overstated. Graft the dependency line into Step 5 and re-fork Q18. Loop A4."
  contradiction:
    - "A5-C01: rev L170 calls Q2 FY26 gross margin 71.75% an outlier base, yet rev L491 reads the YoY fall from it as possible tender pricing. Sequentially Q2 FY27 GM 59.88% is above Q1 FY27 54.14%, Q1 FY26 58.25%, H2 FY26 52.81% and FY26 57.13%. Under the A3-14 chart reading, GM ranks with the spares share (48%, 35%, 21%, 18%) in all four quarters with a split. The extract shows mix, not price. Loop A4."
  style:
    - "S10: rev L434 'all statements tie' should read 'all column totals tie' (R150 position and H1 FY26 investing labels need the rev L18-20 corrections)."
    - "S11: rev L454 and L457 tag derived figures [FILED]; use [FILED, derived]."
    - "S12: rounding-basis artefacts (26.75 vs 26.74%; +122 vs +121.5 bps; +263 vs +263.6 bps; +2.20 vs +2.19; FY26 revenue -6.6% labelled 247 to 231, which gives -6.5%)."
    - "S13: rev L122 deck margin gap is 0.08-0.32 pp, not 0.1-0.3 pp."
    - "S14: rev L221 '-22.6 pp' applies pp to a ratio in x; write -0.23x."
    - "S15: rev L500 30 Apr 2027 CFO date lacks the PENDING LIVE VERIFICATION tag carried in M3; a shorter listing-regulation timeline may apply (outside the extract)."
    - "S16: CFO flag balance: ED Kamlesh Shah signs the statements (res L337-339) and is an ICAI fellow with about 27 years in financial operations and treasury (pres L212-217)."
    - "S17: rev L233 liquid net cash excludes leases while the net-debt rows include them; with leases Sep-26 is Rs (2.93) cr."
    - "S18: rev L241 NFAT 2.22 basis unstated; it ties to TTM revenue / (PPE + CWIP + intangibles) = 264.26 / 119.03."
    - "S19: A4 coverage is a range-level reviewed statement (rev L13); accepted; row-level marking would make the next audit cheaper."
    - "S20: presentation ledger line_items 130 merges 9 same-label lines (139 physical); A2 to state the convention."
loop_back_to: "A4"
gap: "Four A4 grafts, no re-enumeration. (1) FACTUAL rev L474 and L490: restate the customer roster as 8 state-owned and 8 private of 16 names (pres L515-532, L356); make the slow-payer inference conditional. (2) MISSING rev L149, L318, L434, L454, L586: the TTM core-PBT gain of Rs 7.47 cr equals the H1 gain and 79% of it is the Q2 trough recovery; trough-free Q1 YoY +14.9%; TTM EPS Rs 72.97 is 14.4% below FY25 Rs 85.25 (pres L715); TTM core PBT below FY25 about Rs 48 cr (pres L705, L710). (3) MISSING Step 5 and Q18 (rev L224, L239, L386): H1 CFO Rs 1.84 cr includes a Rs 7.14 cr other-financial-liabilities inflow (res L294), so CFO without it is Rs (5.30) cr; re-fork Q18. (4) CONTRADICTION rev L170 vs L491: add the sequential gross-margin series (59.88% vs 54.14%, 58.25%, 52.81%, 57.13%) and the spares-share ranking before any tender-pricing inference."
style_notes:
  - "S10: qualify 'all statements tie' to 'all column totals tie'."
  - "S11: tag derived summary figures [FILED, derived]."
  - "S12: compute bps and pp deltas from lakhs, or state the rounded basis."
  - "S13: restate the deck margin gap as 0.08-0.32 pp."
  - "S14: express the CFO/PAT change as -0.23x."
  - "S15: add PENDING LIVE VERIFICATION to the 30 Apr 2027 forward-map date."
  - "S16: name the ED (ICAI fellow, about 27 years in finance) as the continuity mitigant in the CFO flag."
  - "S17: state that liquid net cash excludes leases (Rs (2.93) cr with leases)."
  - "S18: state the NFAT 2.22 basis."
  - "S19: row-level reviewed marking would make the next audit cheaper."
  - "S20: A2 to state the same-label merge convention (130 merged, 139 physical)."
analyst_note: "Loop 1 applied all four prior items; I confirmed each in the review. Coverage and arithmetic are clean again. Fresh counts tie on all three documents, and every derived metric recomputes within rounding from lakhs. This loop is about reading. First, the roster claim fails on the deck's own slide: 8 state-owned, 8 private. Second, the Loop 1 base-effect text, which the prior A5 worded, calls TTM a less distorted base. But the TTM gain is the H1 gain, and 79% of it is the Q2 trough recovery. The trough-free Q1 comparison is +14.9%, and TTM EPS is still 14.4% below FY25. This corrects the prior A5's own wording. Third, H1 CFO is positive only because other financial liabilities rose Rs 7.14 cr, and Q18's bull fork would make cash quality worse. Fourth, the competition brief reads a possible price cut from a gross-margin fall the review itself calls an outlier base; sequential margins track mix. None of this moves PROCEED WITH FLAGS. No acquisition is described, so the probe does not apply. One A4 pass closes all four."
```
