# A5 ADVERSARY / COMPLETENESS AUDIT: ROUTE MOBILE LIMITED (ROUTE), Q2 FY27

Agent: A5 adversary | Model: claude-opus-5-5 | Run date: 2026-10-29
Review under audit: runs/route-q2fy27/work/review_route_q2fy27.md (A4, 819 lines)
Inputs read: A1 fulltexts (results 1,279 lines; presentation 909 lines; press release 131 lines), A1 structured files (R001-R1129; R001-R368; R001-R074), A2 ledgers (3), A4 review. No source PDF and nothing under runs/route-q2fy27/inputs/ was opened. A3 reasoning was not read.
Line anchors: "L###" = results fulltext line unless prefixed "deck L###" (presentation fulltext) or "pr L###" (press-release fulltext). "rv L###" = A4 review line.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Heading in review | Content | Status |
|---|---|---|---|
| 1 Summary narrative | rv L688 "1. SUMMARY NARRATIVE" | 12 lines (rv L689-700), numbers tagged by tier | PRESENT |
| 2 Sector intelligence | rv L702 | 6 lines (rv L703-708) | PRESENT |
| 3 Business-model intelligence | rv L710 | 5 lines (rv L711-715) | PRESENT |
| 4 Competition intelligence | rv L717 | 6 lines (rv L718-723) | PRESENT |
| 5 Forward map | rv L725 | make-or-break reading plus 8 catalysts, each with a Bull and a Bear fork (rv L726-734) | PRESENT |

Gate: PASS. All five parts are present and carry real content. Undated items (transcript, MOA vote, Mumbai office) are marked "date unknown / not found", not left blank.

---

## 1. COVERAGE AUDIT

Method: fresh grep and line sweep over the three A1 FULLTEXTS, then a diff against the A2 ledger counts and the structured-file ID sets.

### 1A. Category counts

| Doc | Category | A2 count | Fresh count (fulltext) | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | structured IDs referenced | 1,129 | 1,129 (grep `^R\d+ \|`; every ID R001-R1129 falls in a ledger range; checked range by range) | none | PASS |
| Results | notes | 23 | 23: consol 1)-9) L815-860, 3a L834, 7a L853, 7b L856; standalone 1)-8) L1166-1213, 3a L1195; CF "Note:" L755/L810 and L1153/L1154 | none | PASS |
| Results | statement line items | 244 | 244: p7 38, p8 21, p9 40, p10 43, p14 22, p15 38, p16 42 (row blocks R049-R269 = 221 = 38 lines x 6 cols less 7 blank cells; R270-R395 = 126 = 21 x 6; R396-R475 = 80 = 40 x 2) | none | PASS |
| Results | table rows (IPO x2, FX, sub dividend) | 12 | 12 (L828-833, L1184-1193, L845-848/L1277, L1209) | none | PASS |
| Results | zero_standing cells | 42 | 42 (p7 9, p8 3, p9 2, p10 11, p15 1, p16 6, tables 10) | none | PASS |
| Results | agenda items | 5 | 5 (L37, L50, L78, L84, L97) | none | PASS |
| Results | auditor paragraphs | 13 numbered + 1 continuation | 13 numbered (consol 1-8 L153-250; standalone 1-5 L889-926) + L211 continuation | none | PASS |
| Results | Annexure 1 entities | 33 | 33 names (L281-314; Ghana sits on unnumbered L300, so the blank Sr.33 at L315 is a numbering offset, not a missing name) | none | PASS |
| Results | annexures | 2 | 2 (Annexure 1 L145/L278; Annexure 2 L1226) | none | PASS |
| Results | **signature blocks** | **6** | **12** digitally signed blocks: CS L123-126; MSKA L259-263 and L935-938; MD on every statement page L508-513 (p7), L625-629 (p8), L696-698 (p9), L756-761 (p10), L870-873 (p11), L1017-1022 (p14), L1085-1090 (p15), L1155-1161 (p16), L1218-1221 (p17) | none | **FAIL (MISSING, loop A2)** |
| Deck | structured IDs referenced | 368 | 368 (slide inventory ranges sum to 368) | none | PASS |
| Deck | slides | 23 | 23 ([page 1]-[page 23]) | none | PASS |
| Deck | slide numbers | 252 | 252 (per-slide recount: s1 3, s4 14, s5 17, s9 6, s10 5, s12 20, s13 20, s14 4, s16 18 with repeated L307 values deduped, s17 30 incl. 11 axis ticks, s18 20, s19 60, s20 13, s21 10, s22 12) | none | PASS |
| Deck | zero_standing | 18 | 18 (slide 19 dash cells: ESOP 3, FX 4, capital advance 3, Masivian 2, exceptional 3, tax 3; deck L761-810) | none | PASS |
| Deck | signature timestamp | captured | R010 = deck L46-47 00:02:49 | none | PASS |
| Release | structured IDs referenced | 74 | 74 (T1 page lists cover R001-R074) | none | PASS |
| Release | pages | 3 | 3 | none | PASS |
| Release | numbers / qualifiers / fwd | 41 / 4 / 5 | consistent on page sweep (p1 8, p2 26, p3 7) | none | PASS |
| Release | signature timestamp | captured | R036 = pr L48-49 00:03:52 | none | PASS |

### 1B. The signature-block gap (MISSING, loop A2)
- A2 counts 6 blocks. It lists MD blocks for p7 (R969), p11 (R594/R979) and p17 (R909/R985) but not the identical MD blocks on p8, p9, p10, p14, p15 and p16. Six blocks are missing from the ledger.
- The structured file holds one signature timestamp only (R1025, CS 23:49:25). Eleven timestamps have no row: MSKA 23:15:18 (L263) and 23:18:16 (L938); MD 22:46:43 (L513), 22:47:07 (L629), p9 illegible (L698), "22:4s:o4" (L761), 22:48:33 (L873), 22:45:01 (L1022), "22:4s:1s" (L1090), 22:45:30 (L1161), 22:44:22 (L1221).
- A2's sig 5 note quotes "ts 23:18:16" against R595-R596, R982, R1052. None of those rows carries the timestamp. A2 still wrote MISSING_FROM_STRUCTURED: None.
- Why it matters: these timestamps are the evidence for the Reg 30 timing test that A4 closed as "Sequence clean" (see finding F-4).

### 1C. Ledger rows vs A4 review
A4's preamble (rv L17) marks all 1,571 ledger rows and all 23 notes and 26 slides as reviewed, and lists all 66 A3 findings as incorporated (rv L19-22, L750). I accept this blanket statement as the explicit "reviewed, no finding" marking. A4 cites rows on deck slides 4, 5, 7-10, 12-14 and 16-22 and on release pR004, pR036, pR040, pR046-047. Slides 1-3, 6, 11, 15 and 23 carry boilerplate or no data. Orphan rows: none.

---

## 2. ARITHMETIC AUDIT

All derived cells in Steps 0-8 and the brief were recomputed from the filed figures. The table shows every FAIL and a representative set of PASS rows by section.

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Consol Q2 FY27 Op EBITDA / margin | 115.02 / 9.75% | 100.93 + 23.84 + 2.46 - 12.21 = 115.02; 9.750% | L343, L340, L339, L334, L333 | PASS |
| Consol Q1 FY27 Op EBITDA / margin | 105.48 / 9.16% | 91.47 + 23.71 + 1.36 - 11.06 = 105.48; 9.160% | L343, L340, L339, L334 | PASS |
| Consol Q2 FY26 Op EBITDA / margin | 135.95 / 12.14% | 137.87 + 22.87 + 2.37 - 27.16 = 135.95; 12.145% | L401, L398, L397, L393 | PASS |
| Consol H1 FY27, H1 FY26, FY26 Op EBITDA | 220.50 / 247.61 / 537.25 | same | L432-440; L471-479 | PASS |
| Gross margin Q2 / Q1 / Q2 FY26 | 22.38 / 20.88 / 22.07% | 22.375 / 20.880 / 22.074% | L333, L337, L392, L395 | PASS |
| ETR Q2 / Q1 / H1 FY27 | 18.21 / 25.06 / 21.47% | 18.211 / 25.057 / 21.466% | L349, L343, L445, L440 | PASS |
| Normalised ETR Q2 FY26 | 27.21% | (20.83 + 16.69) / 137.87 = 27.214% | L406, L401; deck L752 | PASS |
| Adj EBITDA margin Q2 FY27 | 10.04% | 1,184.2 / 11,796.7 = 10.038% | deck L745; L333 | PASS |
| Adj EBITDA bridge Q2 / Q1 | 1,184.2 / 1,089.3 | 1,150.2 - 35.0 + 69.0; 1,054.8 - 28.1 + 49.0 + 13.6 | deck L739-745 | PASS |
| Adj ex-Masivian Q2 / Q1 / H1 | 9.45 / 9.34 / 9.40% | 111.52/1,179.67; 107.57/1,151.51; 219.09/2,331.18 | deck L744-745 | PASS |
| Condition-1 headroom | Rs 0.45 Cr | 118.42 - 117.967 = 0.453 | deck L745; L333 | PASS |
| Adj margin YoY change | -186 bps | -187 bps unrounded (11.904% to 10.038%) | deck L745 | PASS (rounding; STYLE S-5) |
| Standalone Q2 / Q1 Op EBITDA margin | 12.02 / 2.81% | 30.81/256.33; 5.57/197.93 | L962-972 | PASS |
| Standalone ETR Q2 / Q1 | 25.65 / 20.20% | 11.43/44.56; 4.09/20.25 | L972, L976 | PASS |
| S-vs-C PAT gap Q2 / Q1 / H1 / FY26 | 149.2 / 324.2 / 206.6 / 90.6% | 49.42/33.13; 52.39/16.16; 101.81/49.29; 122.16/134.78 | L350, L977, L446, L1008 | PASS |
| Ex-parent Op EBITDA margin Q2 / Q1 | 9.12 / 10.48% | 84.21/923.34; 99.91/953.58 | derived | PASS |
| Consolidation residual Q2 / Q1 | -15.80 / +28.18 | 82.55 - 33.13 - 65.43 + 0.21; 68.55 - 16.16 - 24.19 - 0.02 | L199-200, L230-231 | PASS |
| Component subs share of PAT Q2 / Q1 | 79.3 / 35.3% | 65.43/82.55; 24.19/68.55 | L199-200 | PASS |
| Overseas result QoQ | -24.8% | 64.40/85.67 - 1 = -24.83% | L528 | PASS |
| YoY: revenue, GP, Op EBITDA, core PBT, PBT pre-exc, normalised PAT | +5.38, +6.82, -15.40, -19.86, -26.79, -17.75% | same | L333, L337, L343, L401, deck L753 | PASS |
| ETR effect YoY | 9.08 | 100.93 x 27.214% = 27.47; less 18.38 = 9.09 | L349 | PASS |
| PAT bridge 4A sum / 4B sum | 101.38 / 14.00 | ties; 4B ETR effect 100.93 x 25.057% - 18.38 = 6.91 (49.4%) | L333-350, L392-407 | PASS |
| Implied ETR outside parent Q1 / Q2 | 26.44 / 12.33% | 18.83/71.22; 6.95/56.37 | L349, L976 | PASS |
| Q1 FY26 revenue / Op EBITDA margin (prior review) | 1,050.83 / 8.94% | 2,170.25 - 1,119.42 = 1,050.83; 93.94/1,050.83 = 8.94% after re-splitting the H1 FY26 net FX (Q1 loss 24.73, Q2 gain 17.72) | L470, L392; L1277 | PASS |
| **Q3 FY26 Op EBITDA (derived)** | **153.41; 13.86%** | **at most 146.40; at most 13.22%.** H2 FY26 by subtraction (537.25 - 247.61 = 289.64) carries +7.01: H1 FY26 other expenses hold the net FX loss 7.01, while FY26 nets its FX gain 14.76 into other income. As-reported Q3 + Q4 cannot exceed ex-FX H2 282.63; less Q4 136.23 = 146.40 | L477, L471, L1277 | **FAIL (CONTRADICTION)** |
| **Q3 FY26 core PBT ex-OI (derived)** | **129.33** | **at most 122.32** (ex-FX H2 233.74 less Q4 111.42) | L479, L471, L1277 | **FAIL (CONTRADICTION)** |
| **Q2 FY27 margin gap to Q3 FY26** | **about 410 bps** | **at most 347 bps** | rv L307 | **FAIL (CONTRADICTION)** |
| Rev and GP per billable transaction | 0.2478 / 0.0555; GP/txn +5.7% QoQ, +1.5% YoY | 11,797/47,600; 2,640/47,600; 1.0567; 1.0145 | deck L298, L301, L314 | PASS |
| New products share / ex-new-products QoQ | 10.88% / -0.54% | 128.4/1,179.67; 1,051.27/1,057.01 - 1 | deck L217; L333 | PASS |
| CFO / PAT H1 FY27 | 0.22x | 33.34/151.10 = 0.221x | L790, L446 | PASS |
| Deck Adjusted CFO | 150.17; 66%; 0.99x | 1,501.7 mn; 1,501.7/2,273.5; 150.17/151.10 | deck L830-833 | PASS |
| FCF / FCF after acquisition | 13.16 / (10.72) | 33.34 - 20.18; less 23.88 | L790-793 | PASS |
| WC change H1 FY27 / H1 FY26 | (157.34) / 13.17 | -45.69 - 161.33 + 49.68; -44.06 + 231.01 - 173.78 | L785-787 | PASS |
| DSO consol H1 x2 / Q2 x4; standalone Q2 x4 / H1 x2 | 74.13 / 73.25; 139.28 / 157.19 | same | L655, L1050, L333, L962 | PASS |
| DPO consol | 53.32 to 51.46 | 496.80/3,400.90 x 365; 515.12/3,653.58 x 365 | L681-682, L337 | PASS |
| Net cash ex-leases / after leases | 1,340.08 / 1,300.76 | 798.96 + 541.12; less 22.85 + 16.47 | L656-657, L672, L679 | PASS |
| **Step 5 cause of the 161.33 other-asset outflow** | **"116.83 vendor prepayment plus a standalone receivable build of 149.89"** | **116.83 + 149.89 = 266.72, above the 161.33 line. The standalone build sits in trade receivables, not in this line. Group trade receivables absorbed only 45.69; consolidated-minus-standalone receivables fell 112.36 (555.68 vs 668.04, derived). 44.50 of the 161.33 is unexplained** | L785-786, L655, L1050; deck L830 | **FAIL (FACTUAL)** |
| **Q2 FY27 finance cost composition** | **"2.46 is lease interest plus a new amortised-cost unwind (0.14 H1)"; QoQ +1.10 "Recurring (lease, deferred consideration unwind)"** | **H1 lease interest is 2.01 in total. CF itemises 0.14 + 0.00 + 2.01 + 0.69 = 2.84 of H1 finance cost 3.82; 0.98 is not itemised. The QoQ +1.10 driver is ND** | L339, L436, L773-776 | **FAIL (FACTUAL)** |
| ROCE on equity + leases, H1 annualised | 13.04% | (192.40 + 3.82) x 2 / (2,970.72 + 39.32) = 13.04% | L440, L436, L668, L672, L679 | PASS |
| **ROCE ex-cash, H1 annualised** | **23.50%** | **20.71%.** A4 keeps other income (mostly bank-deposit interest, 19.01 H1, L769) in the numerator while it removes the cash that earns it. On EBIT ex-OI: 172.95 x 2 = 345.90 / (3,010.04 - 1,340.08 = 1,669.96) = 20.71% | L559, L769, L656-657, L668, L672, L679 | **FAIL (FACTUAL; pillar-relevant)** |
| 6A revenue vs bear / PAT vs base / EPS vs base | +0.3% / -23.3% / -27.9% | 2,331.18/2,324; 151.10/197; 22.57/31.3 | L431, L446, L466 | PASS |
| Trailing PE at Rs 435 | 7.85 | TTM EPS 37.94 + 22.57 - 5.08 = 55.43; 435/55.43 = 7.85 (CMP itself is outside the extract) | L506, L466 | PASS |
| Monitorable dates | 26 Nov 2026; 14 Feb 2027; 30 May 2027; ~29 Jan 2028 | 27 Oct + 30 days; 31 Dec + 45; 31 Mar + 60; 29 Jul 2026 + 18 months | L64-67, L849-851 | PASS |
| Second interim dividend cash | ~25.20 | 6.30 Cr shares x Rs 4 | L61, L375 | PASS |

---

## 3. ADVERSARIAL READ

### Positive claim 1. Condition 1 NOT FIRED on the Adjusted basis: Adjusted EBITDA margin 10.04% (rv L471, L479, L535)
- Strongest bear counter from the extract: management's own Adjusted PAT carries no Masivian add-back and no capital-advance add-back. Adjusted PAT equals reported PAT in both quarters: Q2 825.5 = 825.5, Q1 685.5 = 685.5 (deck L750-753). The same costs that management calls one-time at EBITDA (deck L743-744) stay in its PAT. Management therefore does not treat them as non-recurring where it counts earnings. That supports the reported-basis reading of condition 1.
- A4 already shows the 0.45 Cr headroom and the 9.45% ex-Masivian reading. It does not show this PAT-level inconsistency.
- Verdict: SURVIVES. Graft into Step 6C (condition 1 rows) and flag F-1. Type MISSING, loop A4.

### Positive claim 2. Gross margin recovered +150 bps QoQ to 22.38%; "recovery in gross profit margin CONFIRMED"; "GM in 21.5-23% DELIVERED" (rv L487, L631, L633)
- Strongest bear counter from the extract: the recovery belongs to the Indian parent alone.
  - Standalone gross profit rose 33.24 (46.16 to 79.40; L962, L966). Consolidated gross profit rose only 23.51 (240.44 to 263.95; L333, L337).
  - Consolidated-minus-standalone gross profit fell 9.73 (194.28 to 184.55). Its gross margin fell 39 bps (20.37% to 19.99%, derived).
  - Inter-segment revenue rose 26.46 (147.98 to 174.44; L524). India segment revenue rose 65.99 (L522); overseas fell 11.39 (L523). India segment result rose 31.11 while overseas fell 21.27 (L527-528).
  - The parent's receivables rose 149.89 (+62%) and standalone CFO was -126.69 (L1050, L1127).
- [INFERENCE: a margin that moves to the parent while inter-segment revenue rises and the rest of the group loses margin can be a routing or transfer shift between group entities, which the deck's "enhanced routing strategy" (deck L311) would also describe. The filing does not separate this from genuine India mix gains.]
- A4 states the EBITDA-level version (rv L257: "QoQ EBITDA gain came wholly from the parent") and calls Trigger 1 WEAKENED. It does not show the gross-profit split or the inter-segment rise, and it records the GM recovery as CONFIRMED without that qualifier.
- Verdict: SURVIVES (partial). Graft the GP split and the inter-segment line into Step 6D Trigger 1 and the Section B "CONFIRMED" line. Type MISSING, loop A4.

### Positive claim 3. New products +36.7% YoY and +35.8% QoQ; watch item 5 GREEN; Trigger 3 ON TRACK; clients 2,400+ (rv L444, L489, L705)
- Strongest bear counter from the extract: about two months of Heltar sit inside the figure (L849). The deck says Heltar came with "Blue-chip enterprises already live on the platform at the time of acquisition" (deck L185). Part of the +33.9 QoQ and part of the +300 client count are therefore bought.
- Test: item 5 needs organic YoY of 15% or more. That fails only if Heltar contributed more than 128.4 - 1.15 x 93.9 = 20.41 Cr in Q2. At a total price of up to 33.66 Cr, a business billing 20 Cr in two months would be priced at under 0.3x annualised revenue. [INFERENCE: implausible for an AI software business; GREEN likely holds.]
- A4 already carries "organic rate unverified", "Heltar share not separated" and question 8.
- Verdict: DOES NOT SURVIVE beyond what A4 holds. The break-even figure is logged as STYLE S-6.

### Considered and not carried: net cash Rs 1,340.08 Cr GREEN (rv L380-385, L449)
- Counter: Rs 65 Cr IPO money is earmarked (L831-834). The unutilised QIP balance sits in fixed deposits and is ND (L835-837). A second interim dividend of about 25.20 and the Heltar deferred leg of 9.78 are due (L61, L851). The 116.83 vendor advance has already left cash (deck L830).
- After the known deductions net cash is still about 1,240, above the Rs 800 Cr line. A4 already shows the IPO earmark and the QIP ND. Verdict: DOES NOT SURVIVE.

### MANDATORY ACQUISITION-ECONOMICS PROBE: Heltar (note 6, deck slides 8-9)
- Price: up to Rs 33.66 Cr, made up of 23.88 paid at closing and 9.78 payable at 18 months (L851). The deck states "33.7 crore" and "9.8 crore Deferred, payable 18 months after closing" without the note's "up to" (deck L190, L197-199).
- Target earnings: NOT DISCLOSED. The results, deck and release give no Heltar revenue, PAT, ROCE, debt, cash or customer tenure. Multiple: Rs 33.66 Cr / target PAT NOT FOUND = NOT COMPUTABLE. A price per unit of revenue is not computable either.
- Quality markers the deck asserts without numbers: "marquee anchor customers", "Blue-chip enterprises already live" (deck L183-185); "funded from internal accruals" (deck L195); "Capture higher margins", "Subscription and AI fees" (deck L164-165).
- Balance-sheet trace: goodwill rose 28.17 (545.68 to 573.85; L643). This mixes Heltar with FX translation (FCTR +39.18 in H1; L452), so the purchase allocation cannot be read. The deferred leg is unwound at amortised cost (0.14 H1; L773). [INFERENCE: amortised-cost measurement points to a fixed deferral, which sits uneasily with the note's "up to".]
- Scale: 33.66 is about 2.5% of net cash and 22% of H1 PAT. The deal cannot move group value much either way.
- Bear reading: the deck frames the deal as a strategic win, but no filed number lets anyone test the price. The deck also drops the "up to" qualifier. No "cheap" claim is made, so there is no low multiple to stress.
- Verdict: SURVIVES as a disclosure-gap line. A4 has the consideration and question 8 (earn-out) but never states that the purchase economics cannot be tested. Graft into note C6 and watch item 14. Type MISSING, loop A4.

---

## 4. FINDINGS (every finding tagged)

### FACTUAL (loop A4)
- F-1. Step 5 cash cause (rv L391). The 161.33 other-asset outflow is attributed to the 116.83 vendor advance "plus a standalone receivable build of 149.89". The standalone build is a trade-receivables item. Group trade receivables absorbed only 45.69 (L785). The two items sum to 266.72, above the 161.33 line (L786). Fix: 116.83 of 161.33 is the vendor advance (deck L830); 44.50 is unexplained; the parent's receivable build bears on parent cash (standalone CFO -126.69, L1127) and on possible intra-group billing, not on consolidated CFO.
- F-2. Ex-cash ROCE 23.50% (rv L432, L476, L508) keeps treasury income in the numerator while it removes the cash. On EBIT ex-OI (segment result 172.95, L559) it is 20.71%. Pillar-relevant (ROCE base). Condition 4 is not affected.
- F-3. Finance cost (rv L342, L350). "2.46 is lease interest plus a new amortised-cost unwind" conflicts with the cash flow. H1 lease interest is 2.01 in total, other borrowing cost 0.69, unwind 0.14 (L773-776). These explain 2.84 of H1 finance cost 3.82 (L436). The QoQ +1.10 driver is ND, so do not call it "Recurring (lease, deferred consideration unwind)".
- F-4. Reg 30 timing, FN06 "RESOLVED ... Sequence clean" (rv L27). The extract shows the board concluded at 10:35 PM IST (L114). The MD signed the statements 22:44-22:48 (L1221, L513, L873). MSKA signed the review reports at 23:15:18 and 23:18:16 (L263, L938), after the board had "approved ... along with Limited Review Reports" (L39-42). The CS signed the outcome letter at 23:49:25 (L126), 74 minutes after closure. [INFERENCE: SEBI LODR Schedule III Part A para A.4 sets 30 minutes from closure for disclosure of financial results; the rule text is not in the extract; exchange dissemination time is ND.] "Clean" is not supported. Restate it as a timing flag and carry it to F-9 governance.
- F-5. Client cohort (rv L723 "the largest clients are thinning"; rv L446 item 7). The largest cohorts held or grew: above $15mn 5 to 5; above $10mn 8 to 9; above $1mn 73 to 80 (deck L595-602). The fall is in the $5-10mn band, 13 to 10 (derived). H1 is annualised against a full FY26. Rule J symmetry: state both sides in item 7 and in the brief.
- F-6. ESOP period label (rv L69). "Q1 FY26 1.14" is the H1 FY26 column (L781 "- 1.14"; deck L765 H1 FY26 11.5 mn).
- F-7. Question 11 premise (rv L594). "Why did Rs 62 Cr move from current to non-current" is not supported. Current loans to subsidiaries fell 62.00 (94.70 to 32.70, L1053). Non-current rose only 27.93 (186.60 to 214.53, L1041). H1 shows loans given 34.35 and repayments 72.65 (L1134-1135). Reword the question on these figures.

### CONTRADICTION (loop A4)
- C-1. Q3 FY26 trajectory (rv L301, L307). A4 states that reported EBITDA "does not add across periods" (rv L81, A3-03). It then derives Q3 FY26 by subtracting H1 FY26 and Q4 from FY26. H1 FY26 other expenses hold a net FX loss of 7.01, while FY26 nets its FX gain of 14.76 into other income (L1277). Q3 FY26 is therefore at most 146.40 Op EBITDA (13.22%) and at most 122.32 core PBT, not 153.41 (13.86%) and 129.33. "About 410 bps below Q3 FY26" becomes "at most 347 bps". Restate with the caveat, or mark Q3 FY26 ND.

### MISSING
- M-1 (loop A2). Signature blocks: the ledger counts 6, the fulltext carries 12. Six MD blocks (p8, p9, p10, p14, p15, p16) are absent from the ledger. Eleven signature timestamps (results L263, L938, L513, L629, L698, L761, L873, L1022, L1090, L1161, L1221) have no structured row. MISSING_FROM_STRUCTURED should list them.
- M-2 (loop A4). Surviving bear counter on condition 1: management's Adjusted PAT does not add back the Masivian or capital-advance items (deck L750-753). Add to Step 6C and F-1.
- M-3 (loop A4). Surviving bear counter on the GM recovery: parent-only GP gain (standalone +33.24 vs consolidated +23.51), consolidated-minus-standalone GP -9.73 and GM -39 bps, inter-segment revenue +26.46 (L524). Add to 6D Trigger 1 and qualify the Section B "CONFIRMED".
- M-4 (loop A4). Acquisition probe: state in C6 and item 14 that Heltar revenue, PAT and net assets are NOT DISCLOSED, that the price multiple is NOT COMPUTABLE, and that the deck drops the note's "up to" (deck L190 vs L851).

### STYLE (logged, no loop)
- S-1. rv L391 cites R834 for the 149.89 build. R834 is the standalone cash-flow line (151.63, L1122). The balance-sheet change is R752 less R753 (L1050).
- S-2. rv L705 "Its other sales were flat". Revenue outside new products rose 2.5% YoY and fell 0.5% QoQ. Name the period.
- S-3. rv L714 "the parent's unpaid bills". Readers may take this for payables. Say "money customers owe the parent".
- S-4. The input-discipline line (rv L9) does not list the market-data source behind CMP Rs 435 and the 52-week low Rs 407 (rv L514, L529-530). Add it.
- S-5. Adj margin YoY shows -186 bps on rounded inputs; unrounded it is -187 bps. Rounding only.
- S-6. Item 5 could state the break-even: GREEN fails only if Heltar contributed more than Rs 20.41 Cr in Q2.
- S-7. rv L395 "FX translation may explain the rest" of the receivable gap. The residual after write-off and ECL is 0.38, and positive FCTR (L452) would raise balances, not lower them. Drop the clause or say the residual is immaterial.
- S-8. Ledger reconciliation is a blanket statement (rv L17). It is accepted, but a per-document "reviewed, no finding" range list would make the next audit cheaper.

---

## VERDICT

INCOMPLETE.
- Failing agent (earliest in chain): A2. Gap: signature blocks 6 vs fresh 12; eleven signature timestamps absent from the structured file and the ledger (MISSING, M-1).
- Same cycle, A4: seven FACTUAL (F-1 to F-7), one CONTRADICTION (C-1), three MISSING bear-counter grafts (M-2, M-3, M-4).
- No finding changes the protocol verdict (PROCEED WITH FLAGS), the cash classification (INDETERMINATE-WITH-DIRECTION) or the F-1 basis framing. F-2 changes a pillar-relevant ROCE input. F-4 adds a governance flag.
- STYLE notes S-1 to S-8 are logged only.

## STYLE NOTES
S-1 to S-8 above. None of them re-runs an agent.

```yaml
stage: A5-adversary
company: "ROUTE"
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
    - "results signature block p8 MD L625-629 ts 22:47:07 (not in ledger; no structured timestamp row)"
    - "results signature block p9 MD L696-698 ts illegible in text layer (not in ledger)"
    - "results signature block p10 MD L756-761 ts 22:4s:o4 OCR (not in ledger; no row)"
    - "results signature block p14 MD L1017-1022 ts 22:45:01 (not in ledger; no row)"
    - "results signature block p15 MD L1085-1090 ts 22:4s:1s OCR (not in ledger; no row)"
    - "results signature block p16 MD L1155-1161 ts 22:45:30 (not in ledger; no row)"
    - "results timestamps with no structured row although the block is in the ledger: MSKA L263 23:15:18, MSKA L938 23:18:16, MD p7 L513 22:46:43, MD p11 L873 22:48:33, MD p17 L1221 22:44:22"
arithmetic_mismatches:
  - {metric: "ROCE ex-cash H1 FY27 annualised", a4_value: "23.50%", recomputed: "20.71% (EBIT ex-OI 172.95 x2 / (3,010.04 - 1,340.08))", source_line: "results L559, L769, L656-657, L668, L672, L679"}
  - {metric: "Q3 FY26 Op EBITDA derived", a4_value: "153.41; 13.86%", recomputed: "at most 146.40; at most 13.22% (H2 by subtraction carries +7.01 FX artifact)", source_line: "results L477, L471, L1277"}
  - {metric: "Q3 FY26 core PBT ex-OI derived", a4_value: "129.33", recomputed: "at most 122.32", source_line: "results L479, L471, L1277"}
  - {metric: "Q2 FY27 Op EBITDA margin gap to Q3 FY26", a4_value: "about 410 bps", recomputed: "at most 347 bps", source_line: "review L307; results L1277"}
  - {metric: "Q2 FY27 finance cost composition", a4_value: "2.46 = lease interest + 0.14 unwind; QoQ +1.10 recurring lease/unwind", recomputed: "H1 FC 3.82 itemised only 2.84 (lease 2.01, other 0.69, unwind 0.14); QoQ driver ND", source_line: "results L339, L436, L773-776"}
  - {metric: "H1 FY27 other-asset outflow attribution", a4_value: "161.33 = 116.83 vendor advance + 149.89 standalone receivable build", recomputed: "116.83 + 44.50 unexplained; standalone build is in trade receivables; group TR outflow 45.69", source_line: "results L785-786, L655, L1050; deck L830"}
surviving_bear_counters:
  - {claim: "Condition 1 NOT FIRED on Adjusted basis (Adj EBITDA 10.04%)", counter: "Management Adjusted PAT adds back neither Masivian fees nor the capital-advance allowance (Adj PAT = reported 825.5 Q2, 685.5 Q1), so the one-time label applies at EBITDA only", source_line: "deck L743-753", type: "MISSING"}
  - {claim: "GM recovered +150 bps QoQ to 22.38%; recovery CONFIRMED", counter: "Gain is parent-only: standalone GP +33.24 vs consolidated +23.51; consolidated-minus-standalone GP -9.73 and GM -39 bps; inter-segment revenue +26.46; overseas segment result -21.27", source_line: "results L333, L337, L962, L966, L522-528", type: "MISSING"}
  - {claim: "Heltar acquisition delivered; M&A pace GREEN (mandatory acquisition probe)", counter: "Price up to Rs 33.66 Cr / target PAT NOT DISCLOSED = multiple NOT COMPUTABLE; no target revenue, ROCE, debt, cash or tenure filed; deck drops the note's 'up to'", source_line: "results L849-851, L643; deck L183-199", type: "MISSING"}
findings_by_type:
  factual:
    - "F-1 (A4) Step 5 attributes the 161.33 other-asset outflow to the vendor advance plus the 149.89 standalone receivable build; the build is a trade-receivables item and group TR absorbed only 45.69 (results L785-786, L1050)"
    - "F-2 (A4) Ex-cash ROCE 23.50% keeps treasury income in the numerator; 20.71% on EBIT ex-OI (results L559, L769)"
    - "F-3 (A4) Finance cost 2.46 described as lease interest plus 0.14 unwind; H1 lease interest is 2.01 total and 0.98 of H1 FC 3.82 is unitemised; QoQ +1.10 driver ND (results L436, L773-776)"
    - "F-4 (A4) FN06 'Sequence clean' unsupported: outcome letter signed 23:49:25, 74 min after 22:35 board close; review reports signed 23:15/23:18 after board approval; 30-min Reg 30 window untested; dissemination time ND (results L114, L126, L263, L938)"
    - "F-5 (A4) 'Largest clients are thinning' unsupported: >$15mn 5 to 5, >$10mn 8 to 9, >$1mn 73 to 80; fall is the $5-10mn band 13 to 10 (deck L595-602)"
    - "F-6 (A4) ESOP 1.14 labelled Q1 FY26; it is the H1 FY26 column (results L781)"
    - "F-7 (A4) Q11 premise 'Rs 62 Cr moved from current to non-current' unsupported: current loans -62.00, non-current +27.93, loans given 34.35, repaid 72.65 (results L1041, L1053, L1134-1135)"
  missing:
    - "M-1 (A2) Signature blocks 6 vs fresh 12; 11 signature timestamps absent from structured file and ledger; MISSING_FROM_STRUCTURED wrongly none"
    - "M-2 (A4) Condition-1 bear counter: Adjusted PAT carries no Masivian or capital-advance add-back (deck L750-753)"
    - "M-3 (A4) GM recovery is parent-only at GP level; inter-segment revenue +26.46 (results L524, L962, L966)"
    - "M-4 (A4) Heltar purchase economics NOT COMPUTABLE (no target financials); deck drops 'up to' (deck L190 vs results L851)"
  contradiction:
    - "C-1 (A4) Q3 FY26 derived by subtraction across periods with different FX line placement, after A4 states EBITDA does not add across periods; Q3 at most 13.22% / 146.40 and core PBT at most 122.32, gap at most 347 bps (results L477, L1277; review L81, L301, L307)"
  style:
    - "S-1 R834 cited for the 149.89 build; R834 is the 151.63 CF line; use R752-R753"
    - "S-2 'other sales were flat' needs a period (YoY +2.5%, QoQ -0.5%)"
    - "S-3 'parent's unpaid bills' reads as payables; say money customers owe the parent"
    - "S-4 input-discipline line omits the market-data source for CMP Rs 435 and 52-week low Rs 407"
    - "S-5 Adj margin YoY -186 bps on rounded inputs; -187 bps unrounded"
    - "S-6 state the item 5 break-even: Heltar above Rs 20.41 Cr in Q2 breaks GREEN"
    - "S-7 receivable-gap residual is 0.38; FX translation with positive FCTR would raise balances; drop the clause"
    - "S-8 blanket ledger reconciliation accepted; a per-document range list would speed the next audit"
loop_back_to: "A2"
gap: "A2 MISSING: signature_blocks 6 vs fresh 12 and 11 signature timestamps (results L263, L938, L513, L629, L698, L761, L873, L1022, L1090, L1161, L1221) absent from structured file and ledger. Same cycle A4: FACTUAL F-1 Step 5 cash attribution, F-2 ex-cash ROCE 23.50% vs 20.71%, F-3 finance-cost attribution, F-4 Reg 30 'sequence clean' vs 74-min gap, F-5 client-cohort asymmetry, F-6 ESOP period label, F-7 Q11 loan premise; CONTRADICTION C-1 Q3 FY26 derived across FX bases (13.86% vs at most 13.22%); MISSING grafts M-2 Adj PAT inconsistency, M-3 parent-only GM recovery, M-4 Heltar multiple not computable."
style_notes:
  - "S-1 R834 cite for 149.89; use R752-R753"
  - "S-2 'other sales were flat' needs a period"
  - "S-3 'unpaid bills' ambiguous"
  - "S-4 add the market-data source to the input-discipline line"
  - "S-5 Adj margin YoY -186 vs -187 bps, rounding"
  - "S-6 state item 5 break-even Rs 20.41 Cr"
  - "S-7 drop the FX-translation clause on the 0.38 residual"
  - "S-8 per-document reviewed-range list would help"
analyst_note: "INCOMPLETE on one A2 coverage miss plus eleven A4 items. None changes PROCEED WITH FLAGS, the cash classification, or the F-1 basis framing. The A2 fix is mechanical. The ledger counts 6 signature blocks against 12 in the fulltext, and 11 timestamps have no structured row, yet A2 wrote none missing while quoting one of them. The orchestrator can batch it with the A4 fixes in one cycle; A3 needs no change beyond FN06. Substantive A4 items: (1) FN06 'sequence clean' ignores a 74-minute gap from board close to the outcome-letter signature. (2) Q3 FY26 is derived by subtracting periods that place FX in different lines, which A4 itself warns against, so the Q3 margin is at most 13.22%. (3) Ex-cash ROCE keeps treasury income in the numerator: 20.71%, not 23.50%. This is pillar-relevant. (4) Step 5 blames consolidated cash on a parent receivable build that sits in a different line. Strongest surviving bear: management's Adjusted PAT keeps the Masivian fees it adds back at EBITDA. The Heltar multiple is not computable because no target financials are filed. All other derived cells tie."
```
