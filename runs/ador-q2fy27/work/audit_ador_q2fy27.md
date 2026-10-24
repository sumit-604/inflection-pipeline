# A5 ADVERSARY / COMPLETENESS AUDIT: Ador Welding Limited (ADOR), Q2 FY27

Agent: A5 adversary, model claude-opus-5-5. Audit date 24-Oct-2026.
Under audit: runs/ador-q2fy27/work/review_ador_q2fy27.md (A4, 1,088 lines).
Inputs read: the three A1 fulltexts, the three A1 structured files, the three A2 ledgers, the A4 review. No source PDF, nothing under inputs/, no A3 file was opened.
Anchors: `review l.n` = A4 review line. `res l.n`, `deck l.n`, `cc l.n` = A1 fulltext line. `R###` = A1 structured row. "A5 arith" = my recomputation, formula shown.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Location | Content check | Status |
| --- | --- | --- | --- |
| 1. Summary narrative | review l.933-950 | 16 numbered lines (10-20 required), provenance-labelled | present |
| 2. Sector intelligence | review l.952-959 | demand, input cycle, tailwinds, regulation, export exposure, gaps named | present |
| 3. Business-model intelligence | review l.961-969 | products, channels, unit economics, margin sources, model drift | present |
| 4. Competition intelligence | review l.971-977 | where it wins, where it is weak, named peers (SECONDARY labelled), unorganised | present |
| 5. Forward map | review l.979-991 | make-or-break line plus 9 catalysts, 7 dated, each with a bull and a bear fork | present |

Gate result: PASS. All five parts present and non-empty.

---

## 1. COVERAGE AUDIT

Fresh pass method. Results: I counted note headings, table lines with values, dash cells, agenda items, auditor paragraphs and entities directly in res l.17-678. Presentation: I counted `[page N]` markers, then numbers per slide (deck l.17-833, including the supplement), forward statements and dates. Concall: I walked every timed line (cc l.29-663) for speaker changes, analyst questions and numbers. I then diffed against the A2 ledgers and grepped the structured files for each gap.

### 1A. Counts

| Doc | Category | A2 count | A5 fresh count | Orphan / gap rows | Status |
| --- | --- | --- | --- | --- | --- |
| Results | notes (numbered + lettered) | 22 | 22 (S 1-9, C 1-10, 3a, 3b, 4a) | none | PASS |
| Results | line items | 242 | 242 legible + 1 unresolved (res l.317) | res l.317 "a a A (NA A SS" under the standalone note 3 table; no row; page 6 was not image-verified (res l.12); likely a Total row (831, which R134 already carries) | FAIL (unresolved, F16) |
| Results | zero-standing cells | 66 / 29 lines | 66 / 29 lines on the six statements | consol note 4 table adds 10 dash cells (res l.641-642); rows R863/R864 are in the ledger, flagged NO_Q2_H1_VALUES | PASS (note only) |
| Results | agenda items | 3 | 3 (a, b, c at res l.30, l.34, l.40) | none | PASS |
| Results | auditor paragraphs | 12 | 12 (10 numbered paras + 2 signature blocks) | none | PASS |
| Results | entities | 26 | 26 (grep ENTITY in structured = 26; fulltext sweep finds no unrowed entity) | none | PASS |
| Results | MISSING_FROM_STRUCTURED | 1 (M01) | 1 (res l.24 "Company Symbol: ADOR") | already in ledger, A1 loop open | carried, not re-raised |
| Deck | slides | 29 | 29 (`[page 1]` to `[page 29]`) | none | PASS |
| Deck | number rows | 315 | 316 | deck l.564 "Financial assets 0.0" (current-assets header). Its analogues l.556 and l.572 are rowed as R277 and R278; grep of structured "line 564" returns only R190-R192 (Trade Payables) | FAIL (F15) |
| Deck | zero-standing | 12 | 13 | same l.564 cell | FAIL (F15) |
| Deck | forward rows | 24 | 24 (slide 1: 1, slide 5: 9, slide 16: 3, slide 21: 10, slide 26: 1) | none | PASS |
| Deck | date rows | 34 | 34 (slide 9 timeline 16; slide 20: 4; slide 26: 4; others 10) | none | PASS |
| Deck | entity / qualifier rows | 79 / 18 | sampled slides 5, 8, 10, 16, 18, 22, 23, 26-29 tie; not every entity re-counted | none found | PASS (sampled) |
| Concall | participants | 12 | 12 | none | PASS |
| Concall | turns | 148 | 148 (line ranges contiguous cc l.29-663) | boundary ambiguity at cc l.36 and cc l.661 (structured l.160 notes it); count unchanged | PASS |
| Concall | management turns | 61 | 61 | none | PASS |
| Concall | questions | 46 | 47 | cc l.230 "[14:51] Do you see impact come in a quarter of movies?" (Q3, timing of WelDoS / automation impact). Answer R135 (cc l.231) is rowed; the question has no row (grep "line 230" returns nothing) | FAIL (F13) |
| Concall | number rows | 60 | 61 | cc l.585 analyst "a lot of people in last probably 12 to 18 months or probably 24 months" (hiring period, ties to employee cost +12.86% YoY). No row | FAIL (F14) |
| Concall | forward rows | 35 | 35 | none | PASS |

### 1B. Ledger rows vs A4 review (orphan test)

- A4's preamble (review l.28-32) marks all 900 / 470 / 291 IDs reviewed. I accept the blanket mark for rows that carry no finding.
- Cited directly in A4: all 22 notes (Step 0D table), all 46 question rows (Role 5 Step 4A), rows from 19 of 29 slides.
- Uncited slides 4, 7, 12, 13, 14, 15, 17, 19, 24, 25: no finding, except slide 14. Deck l.302 lists "Flares & Process Equipment" as a current M&R product. That supports the reconciling flare reading (F07).
- Rows marked "reviewed, no finding" that do carry a finding (substantive orphans):
  - res R412 "Flares & Process Equipment (erstwhile division)" (res l.326) and res R873 (res l.649).
  - cc R182 "analyst says Ador exited the same (engineering services) division" (cc l.350-353).
  - These three rows carry the second reading of the flare item. A4 omits it. Loop: A3 (re-grade C-A3-15), then A4 (F07).
- A2 flag housekeeping: the R744 A1_VALUE_CHECK flag is stale. Structured R744 reads 11,119 [OCR_CORRECTED] (structured l.752). A4 is correct (review l.24). STYLE S08.

Coverage status: FAIL. Four fresh-pass units are missing from the structured files and the ledgers (F13-F16, loop A2). Three rows carry an unmade finding (F07, loop A3 then A4).

---

## 2. ARITHMETIC AUDIT

Every derived metric in A4 Steps 1-7 and Role 5 was recomputed from the fulltext values (lakhs x 0.01 = Rs Cr).

| Metric | A4 value | A5 recomputed | Source line | Status |
| --- | --- | --- | --- | --- |
| Step 1-C/1-S raw cells (all 6 columns, both P&Ls) | as tabled | every cell ties to the fulltext; tie-out 313.17 holds | res l.125-157, l.440-481 | PASS |
| Op EBITDA Q2 FY27 / Q1 FY27 / Q2 FY26 (C) | 37.72 / 35.71 / 34.75 | 36.38+4.98+1.17-4.81; 36.93+4.99+0.81-7.02; 33.67+4.77+0.63-4.32 | res l.441, 449, 450, 457 | PASS |
| Op EBITDA H1 FY27 / H1 FY26 / FY26 (C) | 73.43 / 30.35 / 118.51 | same formula | same | PASS |
| Op EBITDA ex one-offs H1 FY26 / FY26 (C) | 58.27 / 131.96 | 30.35+27.92; 118.51+24.82-14.12+2.75 | res l.451, 452, 456 | PASS |
| Op EBITDA margin Q2 FY27 vs Q2 FY26 (C) | 10.94% vs 12.36%, -142 bps | 10.942% vs 12.363%, -142 bps | res l.440 | PASS |
| Gross margin Q2 FY26 / Q1 FY27 / Q2 FY27 / H1 FY26 / H1 FY27 / FY26 (C) | 38.56 / 36.50 / 34.17 / 38.73 / 35.27 / 37.83% | COGS 172.69 / 196.51 / 226.96 / 326.52 / 423.47 / 708.72 over revenue | res l.444-446 | PASS |
| Core PBT, OI/PBT, ETR, PAT margin (C, 6 columns) | as tabled | all tie (e.g. ETR FY26 33.02/115.00 = 28.71%) | res l.441, 457, 461, 462 | PASS |
| Standalone Op EBITDA, margins, GM, core PBT, OI/PBT, ETR, PAT margin | as tabled | all tie (e.g. FY26 ex one-offs 113.15+24.82-14.12+8.31 = 132.16) | res l.125-147 | PASS |
| S vs C PAT gap, 6 periods; H1 swing | +0.97% ... -0.99%; 5.90 pp | 0.26/26.68 = 0.97% ... ; -4.96% to +0.94% | res l.147, l.462 | PASS |
| Implied consolidation adjustment H1 FY27 | +1.15 | 54.54 - 54.03 + 0.64 = 1.15 | res l.147, 409, 462 | PASS |
| YoY tables, consolidated and standalone (22 rows) | as tabled | all tie (e.g. EBIT 32.74/29.98 = +9.21%; S PAT 26.68/25.62 = +4.14%) | res l.125-157, 440-481 | PASS |
| Opex ratio Q2 FY26 / Q2 FY27 | 26.20% / 23.22% | 73.65/281.09; 80.06/344.74 | res l.448, 453 | PASS |
| Q1 FY26 derived: revenue, GM, margin, core PBT | 251.84; 38.92%; 9.34% ex, -1.75%; 17.92 ex, (10.00) | H1 FY26 minus Q2 FY26 | res l.440-457 | PASS |
| H2 FY26 block: revenue, GM, margins, net one-offs | 607.08; 37.04%; 12.14% / 14.52%; +14.47 | FY26 minus H1 FY26; 14.12 + 3.10 - 2.75 | res l.440-456 | PASS |
| QoQ run-rates | +11.61%, +7.99%, +1.95%, +11.40% | 281.09/251.84; 303.54/281.09; 309.46/303.54; 344.74/309.46 | res l.440 | PASS |
| PAT bridge 4A, Rs Cr components | 24.54, (15.16), (6.41), 2.97, (0.21), (0.54), 0.49, (0.08), (0.70), 1.93 | all tie; revenue effect 24.546 at unrounded GM is rounding | res l.440-462 | PASS |
| PAT bridge 4A, operating cost change % | +8.72% | +8.70% (80.06 / 73.65 - 1 = 0.08703) | res l.448, l.453 (R510, R512, R542, R544) | FAIL (F08) |
| PAT bridge 4B standalone; 4C H1 | as stated | all tie (PBT +1.57; H1 PBT +44.68; tax 11.20) | res l.125-147, l.440-462 | PASS |
| H1 FY26 PAT ex onerous; underlying H1 growth | 41.95; about +30% | 21.06 + 27.92 x 0.7483 = 41.95; 54.54/41.95 = +30.0% | res l.451, l.462 | PASS (rate is SECONDARY, S03) |
| CFO, CFO/PAT, FCF (C and S) | (8.45), -0.15x, (24.60); (7.50), -0.14x, (23.65) | tie | res l.276, 278, 599, 601 | PASS |
| WC change and components (C and S) | (73.03), +18.76; (71.93), +17.31 | tie | res l.269-273, l.592-596 | PASS |
| TTM revenue / COGS (C; S) | 1,261.28 / 805.67; 1,257.74 / 804.70 | tie | res l.125-131, l.440-446 | PASS |
| Receivable / inventory / payable days, CCC (C) | 74.27 to 59.26; 78.21 to 80.24; 99.77 to 65.90; 52.71 to 73.60 | tie | res l.519, 522, 549-550; deck R085-R086 | PASS |
| Same, standalone | payable days Sep-26 65.66; CCC 73.99 | 65.67 (144.77/804.70 x 365 = 65.666); 73.98 | res l.199, 202, 229-230 | PASS (rounding) |
| Net cash, narrow (C; S) | 122.59 to 91.82; 122.47 to 91.77 | tie | res l.201-204, 218, 226, 521-524, 538, 546 | PASS |
| ESOP potential shares | 0.68 lakh, 0.39% | 2,668/15.27 - 2,668/15.33 = 0.684 | res l.147, l.156-157 | PASS |
| Special dividend cash | 13.05 | 7.50 x 1.74 Cr shares | res l.41, l.153 | PASS |
| Indicative ROCE | 21.25% / 26.56% | 126.92 / 597.33; 126.92 / 477.80 | res l.450, 534, 546 | PASS |
| TTM PAT; Q2 annualised | 115.46; 107.76 | 60.92 + 54.54; 26.94 x 4 | res l.462 | PASS |
| 3DFT share of H1 PAT; employee cost YoY | 1.17%; +12.86% | 0.64/54.54; 32.73/29.00 | res l.409, l.448 | PASS |
| Middle East share of revenue | 12-17% | 15-20% x 80-85% | cc l.127, l.645 | PASS |
| Specificity; defensive count; grade count | 0.31 / 0.26; 12; 46 | 11/35, 9/35; 12 listed; A5, B24, C13, D1, E3 | ledger sections 3, 5 | PASS (grade count becomes 47 after F13) |
| Deck cross-checks (EBITDA, GM, FY26) | tie | 38 Cr, 10.9%, -140 bps; 132.0, 11.6%; 34.2%, -440 bps | deck l.127-136, l.794-795 | PASS |
| EPS dilution identity, Step 0C | "identical in Q2 FY26 and H1 FY26 (R194/R201, R196/R203)" | Q2 FY26 14.72 = 14.72; H1 FY26 standalone 12.74 vs 12.73 | res l.156-157 (R196, R203) | FAIL (F09, CONTRADICTION with A4's own Step 1-S, review l.134-135) |

Arithmetic status: one mismatch above rounding (F08). One cell-level contradiction (F09). Everything else ties.

---

## 3. ADVERSARIAL READ

### Claim 1: "Revenue growth of 22.6% is real" (review l.226 "the headline is real"; l.894 "a growth engine that is real on revenue"; l.1085 analyst_note)

Strongest bear counter, from the same extract:
- FY26 consolidated revenue grew 1.54%: Rs 1,122.7 Cr to Rs 1,140.0 Cr (deck l.788, R084, R083). The 22.6% follows a flat year.
- TTM revenue Rs 1,261.28 Cr is +12.3% over FY25 across 18 months, about 8.1% a year [A5 arith: (1,261.28/1,122.7)^(2/3) - 1].
- The MD splits the growth himself: "There's a certain amount of it that's obviously inflationary. But we are seeing growth to be in the plus 10% double digit region" (cc l.113-114, R091-R092, ASR). On his split, price may be up to about half of the 22.6% [INFERENCE].
- The volume figure is unresolved ASR: "It's in the approximate high ... team level" (cc l.173-175, R117).

What holds for the bull: Q2 FY26 (281.09) sat at the FY25 average quarter (280.68, A5 arith), so the Q2 base was normal. The rupee growth is real.

Survives: YES, as a composition and context counter. A4 carries the inflation split only in Step 2 (review l.224). It is absent from the brief, Section C and the analyst_note. The FY26 +1.5% fact is absent everywhere. Type MISSING (F01). Graft into brief line 1 and Section C:
> "FY26 revenue grew 1.5% (deck R083-R084). The MD puts underlying growth at 'plus 10%', so part of the 22.6% is price (cc R091-R092, ASR)."

### Claim 2: "Customers paid faster: receivable days fell from 74 to 59"; GREEN; "customers are not the problem" (review l.318, l.321, l.356, l.946, l.1085)

Strongest bear counter:
- March 2026 was the outlier, not the norm. Mar-25 receivables were Rs 192.7 Cr on FY25 revenue Rs 1,122.7 Cr = 62.65 days [A5 arith: 192.7/1,122.7 x 365] (deck l.566 R258; deck l.788 R084).
- In FY26, receivables rose Rs 39.3 Cr (+20.4%) while revenue rose 1.5%. Mar-26 receivable days reached 74.27.
- Sep-26 receivable days (59.26) are 3.4 days better than Mar-25, not 15 days. Most of the 15-day "improvement" reverses an FY26 year-end build.
- A same-season test is impossible: no Sep-2025 balance sheet was passed.

What holds for the bull: Sep-26 is the lowest reading in the window, and H1 FY27 shows a real Rs 27.59 Cr collection inflow (res l.593).

Survives: YES, partly. A4 never uses the 31-Mar-2025 balance sheet (grep of the review for "FY25" returns only the CFO/PAT line). Type MISSING (F02). Graft at Step 5-C receivable row and brief line 12:
> "Mar-25 receivable days were 62.65 (deck R258, R084). Most of the 15-day fall reverses an FY26 year-end build."

### Claim 3: "Without that charge, half-year profit grew about 30%" (review l.231, l.941); H1 EBITDA ex one-offs +26.02%

Strongest bear counter:
- The H1 growth sits almost entirely in Q1.
- EBITDA ex one-offs: Q1 FY26 23.52 (A4's own derived figure, review l.241) to Q1 FY27 35.71 = +51.8%. Q2: +8.55%.
- PAT ex onerous: Q1 FY26 16.94 [A5 arith on A4's 25.17% convention: (21.06 - 25.01) + 27.92 x 0.7483] to Q1 FY27 27.60 = +62.9%. Q2 PAT: +7.72%.
- Revenue grew alike in both quarters (Q1 +22.9%, Q2 +22.6%). The gap is margin: Q1 FY26 ex-onerous margin was 9.34%, the lowest in the window.
- The exit run-rate is single-digit profit growth.

Survives: YES. A4 states both numbers but never links them. A brief reader sees "+30%" with no warning that Q2 grew 7.7%. Type MISSING (F03). Graft into brief line 7:
> "Nearly all of that came in Q1 against a weak Q1 FY26. Q2 profit grew 7.7%."

### Mandatory acquisition-economics probe

1. Automation acquisition intent. Sources: deck l.115-116 (R403) "We continue to evaluate acquisition opportunities"; cc l.233-240 (R136-R138) "very early that nothing is going to happen"; cc l.527-531 (R223-R225) "it's going on".
   - Consideration: ND. Target: ND. Target PAT, ROCE, debt: ND. Price / target PAT = ND; no multiple can be stated.
   - No "cheap, accretive" claim is made, so there is no multiple to stress-test.
   - Bear reading: the "no major debt or equity dilution" answer (cc l.327-329, R166-R168) was given for capex, not M&A. The only small-technology subsidiary in the extract, 3DFT, needed Rs 0.68 Cr of new ICD (R357) and impairments of Rs 5.56 Cr in FY26 (R398) and Rs 0.64 Cr in H1 FY27 (R303).
   - A4 Q23 and Q25 carry these facts separately. Linking them is STYLE S05, with no loop.
2. Ador Fontech M&R merger, 2024 (deck l.696-698, R441).
   - Consideration, target PAT and multiple: ND.
   - Bear reading: the analyst says merged M&R revenue sat near Rs 220-230 Cr "even prior to the [merger] ... and they still around there" (cc l.572-573, R243-R244, ASR). The MD did not dispute the figure. He said fabrication products moved into the welding business (cc l.575-577, R245) and guided 8-12% growth (R246-R247).
   - A4 (review l.762) carries the Rs 220-230 Cr and the 8-12%, but not "flat since before the merger".
   - Survives at analyst / ASR tier. Type MISSING (F12). Graft one line at Role 5 Step 5A.

### Additional adversarial findings (both directions; Rule J symmetric bar)

- F04 (FACTUAL). The margin-target framing is wrong, and its "plausible" claim rests on one quarter.
  - A4 says the targets "only restore FY26 levels (gross margin 37.83%, EBITDA 11.58%). Any thesis that needs margin expansion beyond FY26 has no management support yet" (review l.731; repeated l.862, l.1085).
  - The 12-13% EBITDA target (cc l.97-98, R083-R084; cc l.423, R199-R200) is 42-142 bps above FY26 (11.58%; deck R104 11.6%) and 290-390 bps above FY25 (9.1%, deck R105). It is an expansion, MGMT-tier and undated.
  - Bear counter to A4's "plausible on Q2 cost leverage" (review l.606): with gross margin at 36-38%, which is at or below FY26's 37.83%, the target needs opex at 24-25% of revenue.
  - Opex ratios [A5 arith]: FY25 26.32% (deck R084, R096, R099); FY26 26.26%; H1 FY26 27.80%; Q2 FY26 26.20%; Q1 FY27 24.96%; Q2 FY27 23.22%; H1 FY27 24.04%.
  - At the FY26 opex ratio, 12-13% EBITDA needs gross margin of 38.26-39.26%, which is above the top of management's band.
  - Fix: state the target as expansion beyond FY26 that depends on holding two quarters of operating leverage. Origin C-A3-01.
- F05 (FACTUAL). "Gross margin has slipped in each of the last five reported periods" (review l.939; also l.252, l.891, l.1074, l.1085) is wrong.
  - The series has five data points and four declines: 38.92 (Q1 FY26, derived), 38.56, 37.04 (H2 FY26, a derived two-quarter block), 36.50, 34.17.
  - Q4 FY25 is ND, so the first point cannot be called a slip.
  - FY25 gross margin was 35.4% (deck l.791, R093). The run starts from an FY26 high. H1 FY27 (35.27%) is back at FY25's level, and Q2 FY27 is 123 bps below FY25.
  - Two readings: (a) a structural slide that predates the July shock (A4); (b) reversion from an FY26 peak plus the July shock. Separating observation: Q3 FY27 gross margin against 35.4% and 36%.
- F06 (MISSING). Payables and cash need a third reading.
  - Mar-25 payable days were 62.70 [A5 arith: 124.6/725.3 x 365] (deck l.564 R192; deck l.789 R087). Mar-26 was 99.77; Sep-26 is 65.90.
  - In FY26, payables rose Rs 69.1 Cr (124.6 to 193.7) while COGS fell 2.3%, and the FY26 working-capital line was a Rs 22.1 Cr inflow (deck l.586, R289).
  - Mar-25 CCC was 63.71 days [62.65 + 63.76 - 62.70], so Sep-26 is +9.9 days vs Mar-25, not +20.9.
  - Third reading beside A4's two (review l.356, l.1085): H1 FY27 partly unwinds an FY26 year-end payables stretch. It cuts both ways:
    - Bear: FY26 CFO/PAT of 1.41x (review l.355, l.436) was flattered. 18-month CFO/PAT is 0.79x [(115.9 - 8.45) / (81.98 + 54.54)].
    - Bull: Sep-26 payable days sit near the FY25 level, so a supplier squeeze is not the only fit.
  - Brief line 9 ("The cause is suppliers paid faster", review l.943) needs the Mar-25 reference.
  - The FY27 audited separating observation still holds.
- F07 (MISSING). The flare "contradiction" omits the extract's reconciling evidence.
  - A4 grades the item CONTRADICTED / RED and uses it as verdict flag (2) and as "the governance item to press" (review l.596, l.765, l.779, l.828, l.872, l.893, l.902, l.949, l.1075, l.1085).
  - The analyst asked about segment EBITDA losses. The MD answered: "The flare segment is pretty much done for now ... a few product lines that are not massive ... no losses ... insignificant" (cc l.144-155, R105-R110).
  - The filing itself calls the division "erstwhile" (res l.326, l.649; R412, R873). The analyst refers to "the same division that you have exited", and the MD does not contest it (cc l.352-353, R182). The deck still lists Flares & Process Equipment as an M&R product (deck l.302) and says the project "is still being executed" (deck l.824, R418).
  - Reading A (A4): the MD called the project done, which contradicts the filing.
  - Reading B: the MD described a wound-down division with a few small product lines left, while the legacy turnkey project remains in execution. On this reading there is no contradiction on project status.
  - Separating observation: Q3 FY27 note 4/5 wording (a completion or LD statement) or the official transcript.
  - Fix: re-grade to AMBIGUOUS, show both readings, keep Q10-Q12. Origin C-A3-15 (A3). The protocol verdict PROCEED WITH FLAGS stands on flags (1), (3) and (4).

---

## FINDINGS REGISTER

| ID | Type | Finding (short) | Anchor | Loop to |
| --- | --- | --- | --- | --- |
| F01 | MISSING | Surviving counter, claim 1: FY26 revenue +1.5%; MD's inflation split absent from brief and verdict | deck l.788 (R083-R084); cc l.113-114 (R091-R092); review l.226, l.894, l.1085 | A4 |
| F02 | MISSING | Surviving counter, claim 2: Mar-25 receivable days 62.65; the 15-day gain is mostly reversal | deck l.566 (R258), l.788 (R084); review l.321, l.356, l.946 | A4 |
| F03 | MISSING | Surviving counter, claim 3: underlying H1 +30% sits in Q1 (+62.9%); Q2 PAT +7.7% | res l.440-462; review l.231, l.941 | A4 |
| F04 | FACTUAL | "Targets only restore FY26": 12-13% EBITDA exceeds FY26 11.58%; target needs opex 24-25% vs 26.3% FY25-FY26 | cc l.97-98, l.423; deck l.792-795 (R094-R105); review l.606, l.731, l.862, l.1085 | A4 (origin C-A3-01) |
| F05 | FACTUAL | "Five consecutive" gross-margin declines is four, from a Q1 FY26 high; FY25 35.4% omitted | deck l.791 (R093); review l.252, l.891, l.939, l.1074, l.1085 | A4 |
| F06 | MISSING | Payables: Mar-25 baseline 62.70 days; third reading (FY26 year-end stretch unwound); 18-month CFO/PAT 0.79x | deck l.563-566, l.586, l.589 (R192, R252, R289, R298); review l.323, l.355-356, l.943 | A4 |
| F07 | MISSING | Flare item: the "erstwhile" label, the analyst's "division you exited" and deck l.302 are omitted; contradiction is ambiguous | res l.326, l.649 (R412, R873); cc l.144-155, l.352-353 (R182); deck l.302, l.824 | A3 then A4 |
| F08 | FACTUAL | Arithmetic: op cost change +8.72% should be +8.70% | res l.448, l.453; review l.267 | A4 |
| F09 | CONTRADICTION | Step 0C says basic = diluted EPS in H1 FY26; R196 12.74 vs R203 12.73 (A4's own Step 1-S) | res l.156-157; review l.48 vs l.134-135 | A4 |
| F10 | CONTRADICTION | "5 forward opening claims": A4's table types 3 as Forward; ledger has 4 FORWARD rows in T4 (R047, R051, R056, R066) | review l.567, l.570, l.573, l.581 | A4 |
| F11 | FACTUAL | 3DFT described as "3D printing" under a FILED label; no extract states its business (grep "print" over extracted/ finds none) | review l.968 | A4 |
| F12 | MISSING | Acquisition probe: Fontech merger multiple ND; analyst says M&R flat at ~Rs 220-230 Cr since before the merger; absent | cc l.572-577 (R243-R247); deck l.696-698 (R441); review l.762 | A4 |
| F13 | MISSING | Concall question at cc l.230 has no structured row; Q&A inventory should be 47 | cc l.230-231 (R135) | A2 (flag to A1) |
| F14 | MISSING | Concall analyst number at cc l.585 ("12 to 18 months or probably 24 months") has no row | cc l.585 | A2 (flag to A1) |
| F15 | MISSING | Deck "Financial assets 0.0" at deck l.564 has no row (l.556 and l.572 analogues are R277, R278) | deck l.564 | A2 (flag to A1) |
| F16 | MISSING | Results l.317 garbled line under note 3 table unresolved; page 6 not image-verified | res l.12, l.317 | A2 (flag to A1) |

Counts: FACTUAL 4, MISSING 10, CONTRADICTION 2, STYLE 9.

---

## VERDICT

INCOMPLETE.
- Failing agents: A2 (F13-F16, missed fresh-pass units), A3 (F07, C-A3-15 re-grade; F04 origin C-A3-01), A4 (F01-F12).
- Loop back to A2, the earliest failing agent, so that its rows flow downstream. A3 and A4 then fix their own items in the same cycle.
- The trigger types are FACTUAL, MISSING and CONTRADICTION. STYLE items do not loop.
- Scope note for the orchestrator:
  - The A2 items are small: one question, one analyst number, one zero header and one garbled line.
  - The A4 work is grafting and correcting text. No re-derivation of the arithmetic is needed; it ties except F08.
  - A4's protocol verdict (PROCEED WITH FLAGS) and cash classification (INDETERMINATE-WITH-DIRECTION) are not challenged.

---

## STYLE NOTES (logged; no re-run)

- S01. Review l.809 says the MD "answered every operational and financial question directly". This reads against A4's own grades (3 E, 1 D, 13 C). Reword to "the MD personally took every question".
- S02. Review l.536 says the CFO "did not answer the borrowing, payables or tax questions". No tax question was asked on the call. Drop "tax".
- S03. Rule knowledge not in the documents is labelled INFERENCE or cited to R010, but it is SECONDARY. This covers the 25.17% statutory rate (review l.231, l.495) and the Reg 33 45-day and 60-day deadlines (review l.456, l.909-925). Label it SECONDARY.
- S04. Add the MD's own qualifier beside the 15-20% growth-strategy attribution (review l.967). R074 (cc l.86) says the growth plan "does not impact margins very heavily at all".
- S05. Acquisition probe: link the automation-acquisition intent (deck R403; cc R224-R225) to the 3DFT funding and impairment record (R357, R398, R303) in one line near Q23 and Q25.
- S06. Review l.296 says "Op EBITDA explains 2.97 of the 2.71 PBT change". Rephrase as "Op EBITDA +2.97, less D&A and finance -0.75, plus OI +0.49 = PBT +2.71".
- S07. Review l.536 says "Yellow flags: none", while review l.787 marks CFO participation "Yellow". Align the two.
- S08. The A2 ledger flag A1_VALUE_CHECK on R744 is stale. Structured R744 = 11,119 [OCR_CORRECTED]. Close the flag. A4 already uses the right value.
- S09. The A1 concall header counts 45 ASR_UNCLEAR rows; the A2 ledger lists 65. A2 also counts rows whose speaker name is ASR_UNCLEAR. The difference is definitional; no row is missing. Align the definition.

---

```yaml
stage: A5-adversary
company: "ADOR"
quarter: "Q2 FY27"
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
  orphan_rows: ["res R412 and R873 ('erstwhile' Flares division) and cc R182 (analyst: Ador exited the division): uncited, covered only by the A4 blanket preamble, but they carry the reconciling flare reading (F07); loop A3 (C-A3-15) then A4"]
  missing_from_ledger: ["cc l.230 analyst QUESTION 'Do you see impact come in a quarter...' (answer R135 rowed, question not) (F13)", "cc l.585 analyst NUMBER '12 to 18 months or probably 24 months' hiring period (F14)", "deck l.564 NUMBER 'Financial assets 0.0' current-assets header; analogues l.556/l.572 are R277/R278 (F15)", "res l.317 garbled line under standalone note 3 table, unresolved, likely Total 831; page 6 not image-verified (F16)"]
arithmetic_mismatches:
  - {metric: "Step 4A operating cost change %", a4_value: "+8.72%", recomputed: "+8.70% (80.06 / 73.65 - 1 = 0.08703)", source_line: "res l.448, l.453 (R510, R512, R542, R544); review l.267"}
surviving_bear_counters:
  - {claim: "Revenue growth of 22.6% is real (review l.226, l.894, l.1085)", counter: "FY26 revenue grew 1.5% (1,122.7 to 1,140.0); TTM is +12.3% over FY25 in 18 months; MD says part is inflation, underlying 'plus 10%'", source_line: "deck l.788 (R083, R084); cc l.113-114 (R091, R092)", type: MISSING}
  - {claim: "Receivable days 74 to 59, customers paid faster, GREEN (review l.321, l.356, l.946)", counter: "Mar-25 receivable days were 62.65 (192.7 / 1,122.7 x 365); Sep-26 is 3.4 days better than Mar-25; the 15-day gain mostly reverses an FY26 year-end build", source_line: "deck l.566 (R258), deck l.788 (R084)", type: MISSING}
  - {claim: "Underlying H1 PAT growth about +30% (review l.231, l.941)", counter: "Growth sits in Q1: ex-onerous PAT 16.94 to 27.60 (+62.9%), EBITDA 23.52 to 35.71 (+51.8%); Q2 PAT +7.72%, EBITDA +8.55%", source_line: "res l.440-462 (R474-R478, R591-R595, R532)", type: MISSING}
  - {claim: "12-13% EBITDA with 36-38% GM is plausible on Q2 cost leverage (review l.606)", counter: "Needs opex 24-25% of revenue; opex was 26.32% FY25 and 26.26% FY26; at FY26 opex the target needs GM 38.26-39.26%, above the band", source_line: "deck l.788-795 (R084, R096, R099, R104, R105); res l.448, l.453", type: FACTUAL}
  - {claim: "Fontech M&R merger and the M&R line (review l.762); acquisition multiple ND", counter: "Analyst says merged M&R revenue sat near Rs 220-230 Cr before and after the 2024 merger; MD did not dispute it", source_line: "cc l.572-577 (R243-R247); deck l.696-698 (R441)", type: MISSING}
findings_by_type:
  factual:
    - "F04: 'targets only restore FY26' is wrong; 12-13% EBITDA is 42-142 bps above FY26 11.58% and needs opex 24-25% vs 26.3% in FY25-FY26 (review l.606, l.731, l.862, l.1085; origin C-A3-01) -> A4"
    - "F05: 'gross margin slipped in each of five periods' is four declines from a Q1 FY26 high; FY25 GM 35.4% (deck R093) omitted (review l.252, l.891, l.939, l.1074, l.1085) -> A4"
    - "F08: Step 4A operating cost change +8.72% should be +8.70% (review l.267) -> A4"
    - "F11: 3DFT '3D printing' carried under a FILED label; no extract states its business (review l.968) -> A4"
  missing:
    - "F01: surviving counter to 'revenue growth is real': FY26 +1.5% and MD inflation split not in brief/Section C/analyst_note -> A4"
    - "F02: surviving counter to receivables GREEN: Mar-25 receivable days 62.65 -> A4"
    - "F03: surviving counter to underlying H1 +30%: concentrated in Q1; Q2 PAT +7.7% -> A4"
    - "F06: payables third reading: Mar-25 payable days 62.70, FY26 payables +69.1 Cr, 18-month CFO/PAT 0.79x; brief line 9 and Pillar 2 history need it -> A4"
    - "F07: flare 'contradiction' omits res R412/R873 'erstwhile', cc R182 'division you exited', deck l.302; re-grade AMBIGUOUS with two readings -> A3 (C-A3-15) then A4"
    - "F12: acquisition probe: Fontech merger multiple ND; analyst 'flat at Rs 220-230 Cr since before the merger' absent (review l.762) -> A4"
    - "F13: cc l.230 analyst question has no structured row; Q&A inventory should be 47 -> A2"
    - "F14: cc l.585 analyst number '12 to 18 months or probably 24 months' has no row -> A2"
    - "F15: deck l.564 'Financial assets 0.0' has no row -> A2"
    - "F16: res l.317 garbled line unresolved (page 6 not image-verified) -> A2"
  contradiction:
    - "F09: Step 0C says basic = diluted EPS in H1 FY26; R196 12.74 vs R203 12.73 in A4's own Step 1-S (review l.48 vs l.134-135) -> A4"
    - "F10: '5 forward opening claims' vs 3 typed Forward in A4's table and 4 FORWARD rows in T4 (review l.581) -> A4"
  style:
    - "S01: 'answered every question directly' (review l.809) reads against A4's E/D grades; reword"
    - "S02: no tax question was asked; drop 'tax' (review l.536)"
    - "S03: 25.17% statutory rate and Reg 33 deadlines are SECONDARY, not INFERENCE/R010 (review l.231, l.456, l.495)"
    - "S04: add cc R074 'does not impact margins very heavily' beside the 15-20% attribution (review l.967)"
    - "S05: link automation-acquisition intent to the 3DFT funding/impairment record near Q23/Q25"
    - "S06: rephrase 'Op EBITDA explains 2.97 of the 2.71 PBT change' (review l.296)"
    - "S07: align 'Yellow flags: none' (l.536) with CFO 'Yellow' (l.787)"
    - "S08: close stale A2 flag A1_VALUE_CHECK on R744 (structured reads 11,119)"
    - "S09: A1 header ASR_UNCLEAR 45 vs A2 list 65 is definitional; align"
loop_back_to: "A2"
gap: "A2: add MISSING_FROM_STRUCTURED rows for cc l.230 (question), cc l.585 (analyst number), deck l.564 (0.0 header), res l.317 (unresolved line) and loop A1 for them (F13-F16). A3: re-grade C-A3-15 to AMBIGUOUS using res R412/R873 and cc R182 (F07); re-check C-A3-01, since the 12-13% EBITDA target exceeds FY26 11.58% (F04). A4: graft the surviving counters F01, F02, F03, F06, F12 and the F07 two-reading text; correct F04, F05, F08, F11; resolve F09, F10; add the cc l.230 question to the Q&A inventory (47 rows)."
style_notes: ["S01 reword 'answered every question directly' (l.809)", "S02 drop 'tax' (l.536)", "S03 label 25.17% and Reg 33 deadlines SECONDARY", "S04 add cc R074 qualifier (l.967)", "S05 link M&A intent to 3DFT record", "S06 rephrase l.296 bridge sentence", "S07 align CFO yellow flag l.536 vs l.787", "S08 close stale R744 flag", "S09 align ASR_UNCLEAR count definition"]
analyst_note: "Arithmetic is clean: every Step 1-5 metric ties to the fulltext except one percentage (F08). The failures are context and framing. A4 never used the deck's FY25 column or the 31-Mar-2025 balance sheet, and that baseline changes three readings. Revenue: FY26 grew 1.5%, so 22.6% follows a flat year. Gross margin: FY25 was 35.4%; the 'five-period slide' is four declines from a Q1 FY26 peak. Working capital: March 2026 was the outlier on receivables (74 vs 63 days) and payables (100 vs 63 days), so H1 FY27 partly unwinds an FY26 year-end stretch; FY26 CFO/PAT 1.41x was flattered, and 18-month CFO/PAT is 0.79x. That is a third payables reading beside A4's two. The 12-13% EBITDA target exceeds FY26's 11.58%; it needs opex at 24-25% of revenue against 26.3% in FY25 and FY26. The flare 'contradiction' ignores the filing's own 'erstwhile' label and the analyst's 'division you exited'; it is ambiguous. The A2 items are small. The A4 fixes are grafts, not re-derivations. A4's protocol verdict is not challenged."
```

---

# LOOP 1 RE-AUDIT (24-Oct-2026)

Under audit: the revised review (runs/ador-q2fy27/work/review_ador_q2fy27.md, 1,128 lines, revision log at review l.947-962).
Inputs re-read:
- The three revised structured files: results R001-R916, deck R001-R471, concall R001-R293.
- The three revised ledgers.
- The three fulltexts. The results fulltext l.317 now carries an A1 page-6 image-verification note; no line numbers shifted.

No source PDF, nothing under inputs/, no A3 file was opened. Anchors follow the convention above; `review l.n` now refers to the revised review.

## L1-0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Location | Content check | Status |
| --- | --- | --- | --- |
| 1. Summary narrative | review l.970-988 | 17 numbered lines (10-20 required), provenance-labelled; carries the FY26 +1.54%, Q1-concentration, Mar-25 days and two-reading flare lines | present |
| 2. Sector intelligence | review l.990-997 | unchanged, filled | present |
| 3. Business-model intelligence | review l.999-1007 | adds Mar-25 cash cycle, R074 qualifier, Fontech flat-revenue line, 3DFT business ND | present |
| 4. Competition intelligence | review l.1009-1015 | unchanged, filled | present |
| 5. Forward map | review l.1017-1029 | make-or-break plus companion reading; 9 catalysts, 8 dated (Labour Codes undated); each has a bull and a bear fork | present |

Gate result: PASS.

## L1-1. COVERAGE AUDIT

### Counts against the revised ledgers

| Doc | Category | A2 count (rev) | A5 fresh count | Gap rows | Status |
| --- | --- | --- | --- | --- | --- |
| Results | notes | 22 | 22 | none | PASS |
| Results | line items | 243 (238 + 5 note-table lines) | 243 (standalone note 3: l.314, l.316, l.317; consol note 4: l.641, l.642) | none | PASS |
| Results | zero-standing cells | 81 / 32 lines (statements + standalone note 3 table) | 91 / 34 lines on the same scope | Consol note 4 table, res l.641 "- - - - - 275" and res l.642 "- - = - - 275": 10 printed dash cells, no rows. R863/R864 carry only the FY26 value | FAIL (L1-F02) |
| Results | agenda / auditor paras / entities | 3 / 12 / 26 | 3 / 12 / 26 | none | PASS |
| Results | MISSING_FROM_STRUCTURED | M01 open (ledger l.396) | M01 | A1 has not added the "Company Symbol: ADOR" row; A2 tracks it | carried, not re-raised |
| Deck | slides / numbers / zero-standing | 29 / 316 / 13 | 29 / 316 / 13 | none (R471 at deck l.564) | PASS |
| Deck | forward / dates / entity / qualifier | 24 / 34 / 79 / 18 | 24 / 34 / 79 (sampled) / 18 (sampled) | none | PASS |
| Concall | participants / turns / mgmt turns | 12 / 148 / 61 | 12 / 148 / 61 | none | PASS |
| Concall | questions | 47 | 47 (R292 at cc l.230) | none | PASS |
| Concall | number rows | 61 (mgmt 47 + analyst/header 14) | 61 (R293 at cc l.585) | none | PASS |
| Concall | forward / all rows | 35 / 293 | 35 / 293 | none | PASS |

### Loop-0 coverage findings: status

| Finding | Fix observed | Status |
| --- | --- | --- |
| F13 (cc l.230 question) | cc R292 (structured l.455); ledger T47; A4 Q&A row at review l.699, grade C; count 47 (review l.733) | CLOSED |
| F14 (cc l.585 analyst number) | cc R293 (structured l.456); ledger T125; A4 review l.517, l.623, l.726, l.779 | CLOSED |
| F15 (deck l.564 zero header) | deck R471 (structured l.489); ledger 316 / 13 | CLOSED |
| F16 (res l.317 unresolved) | A1 page-6 image note at res l.317 ("Total row = - - - - - 831"); res R911-R916; R916 = 831 = R398 + R399; ledger 243 line items | CLOSED |
| Substantive orphans R412, R873, R182 | now cited at review l.63, l.613, l.677, l.847 | CLOSED |

### Why L1-F02 is raised now

- In loop 0, I logged the consolidated note 4 dashes as "PASS (note only)". At that time A2's zero-standing count covered the six statements only, and the note-table line rows existed.
- Loop 1 rowed the standalone note 3 dash cells (R901-R915), and A2's count now includes them (81 cells / 32 lines).
- The same scope must include the consolidated note 4 table. Its 10 dashes are printed in the fulltext (res l.641-642), unlike the standalone table, where A1 first read "blank" (res l.170).
- So the gap is a scope inconsistency introduced by the loop-1 fix.
- Materiality: nil. The consolidated exceptional line is already dash-rowed on the P&L (R560-R564).

### Ledger rows vs revised review

The preamble (review l.31-35) marks 916 / 471 / 293 IDs reviewed. New rows are cited directly:
- res R901-R916 at review l.27, l.60, l.132.
- deck R471 at review l.27.
- cc R292 and cc R293 (see the table above).

No row carries an unmade finding. orphan_rows: none.

## L1-2. ARITHMETIC AUDIT (new and changed values)

| Metric | A4 value | A5 recomputed | Source line | Status |
| --- | --- | --- | --- | --- |
| Op cost change % (F08) | +8.70% | 80.06/73.65 - 1 = 8.703% | res l.448, l.453; review l.276 | PASS |
| Operating cost ratio row (6 columns) | 26.20 / 24.96 / 23.22 / 27.80 / 24.04 / 26.26% | 73.65/281.09; 77.24/309.46; 80.06/344.74; 148.14/532.93; 157.30/654.20; 299.33/1,140.01 | res l.448, l.453; review l.152 | PASS |
| FY25 reference: revenue growth, opex ratio | +1.54%; 26.32% | 1,140.0/1,122.7; 295.5/1,122.7 | deck l.788, l.792-793; review l.159 | PASS |
| Q1 split: EBITDA, PAT, revenue | +51.8%; 16.94 to 27.60 = +62.9%; Q1 +22.88% | 35.71/23.52; (21.06-25.01)+27.92x0.7483 = 16.94; 309.46/251.84 | res l.440-462; review l.238 | PASS |
| H1 EBITDA gain split; Q1 share | Q1 +12.19, Q2 +2.97; 80% | 35.71-23.52; 12.19/15.16 = 80.4% | review l.295, l.305 | PASS |
| Mar-25 receivable / inventory / payable days; CCC | 62.65 / 63.76 / 62.70; 63.71 | 192.7/1,122.7; 126.7/725.3; 124.6/725.3 (x365); 62.65+63.76-62.70 | deck l.563-566, l.788-789; review l.330-333 | PASS |
| Changes vs Mar-25 | -3.39; +16.48; +3.20; +9.89 days | 59.26-62.65; 80.24-63.76; 65.90-62.70; 73.60-63.71 | review l.330-333 | PASS |
| FY26 balance-sheet moves | receivables +39.3 (+20.4%); payables +69.1; COGS -2.3% | 232.0-192.7; 193.7-124.6; 708.7/725.3 | deck l.564-566, l.789; review l.341 | PASS |
| 18-month CFO/PAT | 0.79x | (115.9-8.45)/(81.98+54.54) = 0.787 | deck l.589; res l.599, l.462; review l.366 | PASS |
| Standalone payable days, CCC (rounding note) | 65.67, -33.96; 73.98, +20.84 | 144.77/804.70x365 = 65.67; 73.98-53.14 | review l.356-357 | PASS |
| Target gap and required gross margin | +42 to +142 bps vs FY26; +290 to +390 vs FY25; 38.26-39.26% at 26.26% opex | 12-11.58, 13-11.58; 12-9.1, 13-9.1; 12+26.26, 13+26.26 | review l.623 | PASS |
| H1 employee cost YoY | +9.37% | 63.71/58.25 | res l.448; review l.623 | PASS |
| Grade count | A5 B24 C14 D1 E3 = 47 | recount of review l.685-731 | review l.733 | PASS |
| EPS identity (F09) | Q2 FY26 and consol H1 FY26 identical; standalone H1 FY26 12.74/12.73 | res l.156-157, l.480-481 | review l.51 | PASS |
| Deck FY25 core items | GM 35.4%; EBITDA 9.1%; Q2 FY27 123 bps below FY25 | deck R093, R105; 35.40-34.17 | review l.248, l.261 | PASS |

Step 1 tables were re-scanned and are unchanged from loop 0, so every loop-0 PASS stands. Arithmetic status: PASS, with no mismatch.

## L1-3. ADVERSARIAL READ

### Loop-0 counters and analytic findings: status

| Finding | Where grafted / corrected | Status |
| --- | --- | --- |
| F01 revenue context | review l.159, l.201, l.230, l.910, l.913, l.973, l.1116, l.1126 | CLOSED |
| F02 receivables vs Mar-25 | review l.330, l.341, l.910, l.984 | CLOSED |
| F03 H1 growth sits in Q1 | review l.238, l.295, l.305, l.442, l.979 | CLOSED |
| F04 target is expansion; opex lever | review l.623 (two readings, separator H2 opex ≤24.5%), l.749, l.881, l.985, Q34 l.517 | CLOSED |
| F05 four declines; FY25 35.4% | review l.261 (two readings), l.748, l.910, l.977, l.1113 | CLOSED |
| F06 third payables reading | review l.366-371, l.452, l.757, l.981, Q1-Q2 l.484-485 | CLOSED |
| F07 flare AMBIGUOUS | review l.613, l.784, l.798, l.847, l.891, l.912, l.922, l.987, Q12 l.495 | CLOSED |
| F08-F11 | review l.276, l.51, l.598, l.76 / l.1006 | CLOSED |
| F12 Fontech merger | review l.781, l.1005, Q14 l.497, Q23 l.506 | CLOSED |
| S01-S09 | review l.828, l.553, l.24 / l.237, l.490 / l.1005, l.506, l.305, l.553; ledger l.234 (R744 closed); S09 noted at review l.27 | CLOSED |

### New positive claims introduced in loop 1, tested

1. "Costs already run at 24% of revenue, so gross margin is the lever" (review l.476, l.623, l.985).
   - Bear counter: the H1 FY27 ratio (24.04%) rests on revenue growing +22.76% against employee cost +9.37%. Incentives are "linked to profitability" (cc R253), so the accrual may lag.
   - A4 already carries this as reading (b), names the separator (H2 opex ratio ≤24.5%) and asks Q34.
   - No graft needed.
2. "Current filings favour (a)" on flares (review l.847, l.912).
   - Bear counter: the deck still lists Flares & Process Equipment as a product (deck l.302), and the Rs 14.99 Cr LD provision is unsettled.
   - A4 shows both readings and names the separating observation (note 4/5 wording at completion; the onerous / LD line).
   - No graft needed. One supporting point does not discriminate between the readings (L1-S05).
3. "Part of this unwinds a March 2026 stretch" (brief line 10, review l.981).
   - Bear counter: the same fact means FY26 conversion was flattered; 18-month CFO/PAT is 0.79x.
   - Step 5, Step 7, verdict flag (1) and the analyst_note carry it. The brief does not (L1-S06).
   - No loop.

Mandatory acquisition-economics probe: unchanged. Automation target and Fontech merger consideration, target PAT and multiple are all ND. The bear readings are now in A4 (review l.506, l.781). Nothing further survives.

### New finding

- L1-F01 (CONTRADICTION). The Step 8C bands contradict each other (review l.475).
  - The text reads: "A reading between 34.2% and 35.4% says the FY26 peak has fully reversed; a reading below 35.4% (FY25) says the slide goes beyond reversion."
  - Any reading from 34.2% to 35.4% is also below 35.4%, so the same Q3 number gets both meanings.
  - This sits inside the single make-or-break metric for Q3.
  - Fix: "34.2-35.4%: below FY25, the slide goes beyond reversion. 35.4-36.0%: back at FY25, the FY26 peak fully reversed, short of the 36% floor. At or above 36.0%: bull."
  - Monitorable 4 (review l.932) and forward map line l.1019 stay consistent with that fix.

## L1 FINDINGS REGISTER

| ID | Type | Finding (short) | Anchor | Loop to |
| --- | --- | --- | --- | --- |
| L1-F01 | CONTRADICTION | Step 8C bands overlap: 34.2-35.4% is called both "fully reversed" and "beyond reversion" | review l.475 | A4 |
| L1-F02 | MISSING | Consol note 4 table: 10 printed dash cells (res l.641-642; Q2 FY27, Q1 FY27, Q2 FY26, H1 FY27, H1 FY26 on both lines) have no rows, while the standalone note 3 dashes are now rowed; A2 zero-standing 81 / 32 vs fresh 91 / 34 on A2's own loop-1 scope | res l.641-642 (R863, R864); ledger l.7 | A2 (flag to A1) |

Counts: FACTUAL 0, MISSING 1, CONTRADICTION 1, STYLE 6.

## L1 VERDICT

INCOMPLETE.
- Loop back to A2 (L1-F02), the earliest failing agent. A4 fixes L1-F01 in the same cycle.
- A3: no re-run is needed. No forensic finding changes.
- A4: rewrite one sentence (review l.475). Update the preamble ID count once the A2/A1 rows land (916 to 926 if 10 rows are added).
- Neither item touches an analytic number, the cash classification or the protocol verdict (PROCEED WITH FLAGS).
- All 16 loop-0 findings and all 9 loop-0 style notes are closed.

## L1 STYLE NOTES (logged; no re-run)

- L1-S01. Review l.230 labels A4's own arithmetic "[A5 arith: 1,122.7 / 4 = 280.68]". Use "A4 arith", per the review's convention at review l.22.
- L1-S02. Review l.27, l.517, l.623, l.726 and l.779 call R293 "senior hiring". The analyst said "a lot of people" (cc l.585). Seniority rests on the MD's "we've got a good senior talent now" (cc l.593), so cite l.593. Most of a 12-24 month hiring wave is already in H1 FY27 cost, so reading (b) rests mainly on the incentive accrual (cc R253). Weight it that way.
- L1-S03. Stale "blank" wording remains in two places: the A1 note p3 at res l.170 ("quarter/half columns blank") and results ledger l.24 ("quarter and half columns blank"). The new image-verified note at res l.317 and ledger l.289-291 say "dash". Align them; both mean nil.
- L1-S04. The results fulltext header (res l.12) still lists image-verified pages 4, 5, 9, 10, 11. Add page 6, per the res l.317 note.
- L1-S05. Review l.847 and l.912 cite the nil H1 FY27 onerous charge as support for flare reading (a). Reading (b) also predicts a nil charge until completion, so the point does not discriminate. The "erstwhile" label and the uncontested "exited" remark carry reading (a) on their own.
- L1-S06. Brief line 9 or 10 (review l.980-981) could add the 18-month CFO/PAT of 0.79x, so the unwind reading carries its bear side in the brief as well.

---

```yaml
stage: A5-adversary
company: "ADOR"
quarter: "Q2 FY27"
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
  missing_from_ledger: ["res l.641-642 consolidated note 4 exceptional table: 10 printed dash cells (Q2 FY27, Q1 FY27, Q2 FY26, H1 FY27, H1 FY26 on the Labour Codes and Total lines) have no rows; R863/R864 carry only FY26 275; standalone note 3 dashes are now rowed (R901-R915), so A2 zero_standing 81 cells / 32 lines vs fresh 91 / 34 on A2's loop-1 scope (L1-F02)"]
arithmetic_mismatches: []
surviving_bear_counters: []
findings_by_type:
  factual: []
  missing:
    - "L1-F02: consolidated note 4 table dash cells (res l.641-642, 10 cells) unrowed while standalone note 3 dashes are rowed; zero_standing count 81/32 vs fresh 91/34 -> A2 (flag to A1)"
  contradiction:
    - "L1-F01: Step 8C bands overlap; 'between 34.2% and 35.4% says the FY26 peak has fully reversed' and 'below 35.4% says the slide goes beyond reversion' assign two meanings to the same reading (review l.475) -> A4"
  style:
    - "L1-S01: review l.230 labels A4's own arithmetic '[A5 arith]'; use 'A4 arith'"
    - "L1-S02: R293 'senior hiring' rests on cc l.593, not the analyst's 'a lot of people' (cc l.585); reading (b) rests mainly on the incentive accrual (R253)"
    - "L1-S03: stale 'blank' notes at res l.170 and ledger l.24 vs image-verified 'dash' at res l.317 and ledger l.289-291; align"
    - "L1-S04: results fulltext header l.12 should list page 6 as image-verified"
    - "L1-S05: nil H1 onerous charge does not discriminate the two flare readings (review l.847, l.912)"
    - "L1-S06: brief line 9/10 could add the 18-month CFO/PAT 0.79x"
loop_back_to: "A2"
gap: "A2 (flag to A1): add ZERO_STANDING rows for the 10 dash cells in the consolidated note 4 table (res l.641 Labour Codes and l.642 Total; Q2 FY27, Q1 FY27, Q2 FY26, H1 FY27, H1 FY26), recount zero_standing to 91 cells / 34 lines, and align the stale 'blank' notes (res l.170, ledger l.24). A3: no re-run needed. A4: rewrite the Step 8C band sentence at review l.475 so 34.2-35.4% (beyond reversion) and 35.4-36.0% (back at FY25, short of floor) do not overlap; update the preamble ID count after the A2/A1 rows land."
style_notes: ["L1-S01 relabel '[A5 arith]' at review l.230 as A4 arith", "L1-S02 cite cc l.593 for 'senior'; weight reading (b) on R253", "L1-S03 align stale 'blank' notes (res l.170, ledger l.24)", "L1-S04 add page 6 to fulltext header image-verified list", "L1-S05 drop nil H1 charge as support for flare reading (a)", "L1-S06 add 18-month CFO/PAT 0.79x to the brief"]
analyst_note: "Loop 1 closed all sixteen loop-0 findings and the nine loop-0 style notes. The grafts are accurate: every new number re-ties to the fulltexts (FY25 baseline, Mar-25 working-capital days, the Q1/Q2 split, opex ratios, 18-month CFO/PAT 0.79x, the target gap). Two items remain, both small. A4's Step 8C bands now give two meanings to any Q3 gross margin between 34.2% and 35.4%; one sentence fixes it. Loop 1 rowed the standalone note 3 dash cells, so A2's zero-standing count now covers note tables, but the consolidated note 4 table's 10 printed dashes (res l.641-642) still have no rows. In loop 0 I logged them as a note because the count then covered statements only; the loop-1 scope turns them into a count mismatch. Neither item touches A3, the cash classification, the protocol verdict or any analytic number."
```

---

# LOOP 2 RE-AUDIT (24-Oct-2026)

Under audit: the revised review (runs/ador-q2fy27/work/review_ador_q2fy27.md; revision log at review l.949-975, with loop 2 at review l.967-975).
Inputs re-read:
- The revised results structured file (R001-R926) and the revised results ledger.
- Deck and concall structured files and ledgers, unchanged since loop 1 (471 / 293 IDs).
- The fulltexts, unchanged.

No source PDF, nothing under inputs/, no A3 file was opened. `review l.n` now refers to the loop-2 review.

## L2-0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Location | Content check | Status |
| --- | --- | --- | --- |
| 1. Summary narrative | review l.983-1001 | 17 numbered lines; line 10 now carries the 18-month CFO/PAT 0.79x | present |
| 2. Sector intelligence | review l.1003-1010 | unchanged, filled | present |
| 3. Business-model intelligence | review l.1012-1020 | unchanged, filled | present |
| 4. Competition intelligence | review l.1022-1028 | unchanged, filled | present |
| 5. Forward map | review l.1030-1042 | make-or-break line now states all four Step 8C bands (review l.1032); each catalyst has a bull and a bear fork | present |

Gate result: PASS.

## L2-1. COVERAGE AUDIT

| Doc | Category | A2 count (rev 2) | A5 fresh count | Gap rows | Status |
| --- | --- | --- | --- | --- | --- |
| Results | line items | 243 | 243 | none | PASS |
| Results | zero-standing cells | 91 / 34 lines | 91 / 34 (statements 66 / 29 + standalone note 3 15 / 3 + consolidated note 4 10 / 2) | none | PASS |
| Results | IDs | 926 | 926 (R917-R921 at res l.641, R922-R926 at res l.642, five non-FY26 columns each, ZERO_STANDING) | none | PASS |
| Results | notes / agenda / auditor paras / entities | 22 / 3 / 12 / 26 | unchanged | none | PASS |
| Results | MISSING_FROM_STRUCTURED | M01 open (ledger l.396) | M01 | A1 has still not added the "Company Symbol: ADOR" row; A2 tracks it | carried, not re-raised |
| Deck / Concall | all categories | unchanged from loop 1 | unchanged | none | PASS |

- L1-F02: CLOSED. A4 cites R917-R926 at review l.27 and l.60. The preamble reads 926 / 471 / 293 (review l.33).
- No row carries an unmade finding. orphan_rows: none.

## L2-2. ARITHMETIC AUDIT

- Loop 2 adds no derived number. The new Step 8C thresholds (36.0% / 35.4% / 34.2%) match their stated reference points:
  - management floor 36% (cc R087);
  - FY25 35.4% (deck R093);
  - Q2 FY27 34.2% (deck R019).
- Values elsewhere are unchanged from loop 1, so every earlier PASS stands.

Arithmetic status: PASS.

## L2-3. ADVERSARIAL READ

| Item | Where fixed | Status |
| --- | --- | --- |
| L1-F01 Step 8C bands | review l.473-477: Bull ≥36.0%; Middle 35.4% to <36.0%; Weak 34.2% to <35.4%; Bear <34.2%. No overlap. Each band maps to a Step 3 reading. Monitorable 4 (review l.934), forward map (review l.1032, l.1036) and the YAML monitorable all match | CLOSED |
| L1-S01 | review l.230 now "A4 arith" | CLOSED |
| L1-S02 | review l.27, l.519 (Q34 narrowed to the incentive accrual), l.625, l.728, l.781; seniority cited to cc l.593; reading (b) weighted on cc R253 | CLOSED |
| L1-S03 | review l.27, l.60: note-table cells are described as dashes (nil). The A1 / A2 wording upstream still says "blank" (see L2 style notes) | CLOSED on the A4 side |
| L1-S05 | review l.848, l.914: the nil charge is no longer cited as support; review l.848 says it does not discriminate | CLOSED |
| L1-S06 | review l.994 (brief line 10), l.912 | CLOSED |
| L1-S04 | A1 header item; no A4 dependency | carried (A1 housekeeping) |

- New positive claims: none. Loop 2 changes only band wording, counts and labels (review l.924).
- Mandatory acquisition-economics probe: unchanged. Consideration, target PAT and multiple remain ND, and the bear readings are in A4.
- No counter survives.

## L2 FINDINGS REGISTER

No FACTUAL, MISSING or CONTRADICTION finding remains. Counts: FACTUAL 0, MISSING 0, CONTRADICTION 0, STYLE 2 (plus 3 carried A1 / A2 housekeeping items).

## L2 VERDICT

COMPLETE. The review may proceed to the Notion save. Under the 2026-10-03 ruling, that save happens only after the operator approves the printed payload in this run; Decision Status is never written.
- All loop-0 findings (F01-F16) and loop-1 findings (L1-F01, L1-F02) are closed.
- A4's protocol verdict (PROCEED WITH FLAGS) and cash classification (INDETERMINATE-WITH-DIRECTION) stand.

## L2 STYLE NOTES (logged; no re-run)

- L2-S01. The Bear band reads "below 34.2%: worse than Q2 FY27" (review l.477). Q2 FY27 unrounded is 34.17% (res l.440-446), which itself sits below 34.2%. So a Q3 reading equal to Q2 would be labelled "worse than Q2". Use 34.17% as the boundary, or say "at or below Q2's 34.2% rounded".
- L2-S02. Results ledger l.24 cites "R901-R926" for the standalone note 3 dashes. The standalone range is R901-R915; R917-R926 belong to the consolidated note 4 table (ledger l.292-293).
- Carried A1 / A2 housekeeping, with no A4 dependency:
  - L1-S03: the "blank" wording at res l.170.
  - L1-S04: the fulltext header page list at res l.12.
  - M01: the missing "Company Symbol: ADOR" row (res l.24).

---

```yaml
stage: A5-adversary
company: "ADOR"
quarter: "Q2 FY27"
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
    - "L2-S01: Step 8C Bear band 'below 34.2%: worse than Q2 FY27' (review l.477); Q2 unrounded is 34.17%, so a reading equal to Q2 lands in Bear; use 34.17% or 'at or below Q2's 34.2% rounded'"
    - "L2-S02: results ledger l.24 cites R901-R926 for standalone note 3 dashes; standalone range is R901-R915 (R917-R926 are consolidated note 4)"
    - "Carried A1/A2 housekeeping, no A4 dependency: L1-S03 'blank' wording at res l.170; L1-S04 fulltext header page list at res l.12; M01 Company Symbol row (res l.24)"
loop_back_to: ""
gap: ""
style_notes: ["L2-S01 Bear band boundary: use 34.17% or 'at or below Q2's rounded 34.2%' (review l.477)", "L2-S02 ledger l.24 range should read R901-R915", "Carried A1 housekeeping: res l.170 'blank' wording, res l.12 header page 6, M01 Company Symbol row"]
analyst_note: "Loop 2 closed both loop-1 findings. The Step 8C bands no longer overlap, and every consumer of them (monitorable 4, forward map, YAML monitorable) points to the same four bands. The consolidated note 4 dash cells are rowed (R917-R926), and the zero-standing count now ties at 91 cells over 34 lines. No new derived number was introduced, so the loop-0 and loop-1 arithmetic stands. Across the three loops the review gained the FY25 baseline, the March 2025 working-capital days, the Q1 concentration of H1 growth, the corrected margin-target framing and a two-reading flare item. A4's protocol verdict and cash classification are unchanged. The remaining notes are cosmetic or upstream housekeeping and do not loop."
```
