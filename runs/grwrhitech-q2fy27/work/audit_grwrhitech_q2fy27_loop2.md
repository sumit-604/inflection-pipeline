# A5 ADVERSARY RE-AUDIT (CORRECTION LOOP 2): GRWRHITECH (Garware Hi-Tech Films Limited) | Q2 FY27

Audited artifact: runs/grwrhitech-q2fy27/work/review_grwrhitech_q2fy27.md (A4, revised, 699 lines, header l.10 "Correction loop 2").
Prior audits: runs/grwrhitech-q2fy27/work/audit_grwrhitech_q2fy27.md (loop 0: C1, M1, M2, M3, F1, F2; STYLE S1-S9) and runs/grwrhitech-q2fy27/work/audit_grwrhitech_q2fy27_loop1.md (loop 1: F3; STYLE S10-S15).
Inputs read: A1 fulltext (FT, l.1-1492, read in full), A1 structured (ST, R001-R1782), A2 ledger (LG), A4 review (RV), both prior A5 audits. No source PDF opened. Nothing under inputs/ opened. A3 reasoning not read.
Anchors: "FT l.N", "ST l.N", "LG l.N", "RV l.N" are line numbers in those files. [DERIVED] = my arithmetic on filed numbers, formula shown.
Scope: Notion values (RV l.27-57) and the orchestrator-supplied MPCB Reg 30 facts (RV l.83) are outside A5 inputs. I check their internal arithmetic and the filing's silence only. A fresh grep of FT for "MPCB|pollution|consent|bank guarantee|forfeit" returns one hit, the ESG slide (FT l.1370). The filing is silent on the MPCB action.
Method: I re-mapped every SA and C P&L, balance sheet and cash flow column by hand from FT (the text layer is column-displaced on pp5-7, 12-14). Every column ties to its filed subtotal. ST NUMBER labels on those pages are position-based and often sit on the wrong label (for example R756 "Finance cost" carries the lease repayment 3.11), so FT is the authority for values.

---

## PRIOR FINDINGS STATUS

| ID | Loop | Type | Gap (short) | Where it stands now (RV) | My re-check | Status |
|---|---|---|---|---|---|---|
| F3 | 1 | FACTUAL | Unsupported lean to reading (a), a higher transfer markup | l.184 (1-G), l.525 (Flag 14), l.589 (brief), l.694 (YAML flag), l.696 (analyst note) | All five places now say the filing does not separate the readings. l.184: "each needs one undisclosed figure", "it cannot rank them", "The test does not exclude either reading; no lean is drawn". l.589: "The cause is not disclosed ... The filing does not show which." l.694: "no lean". Grep of RV for "lean" finds only the header note (l.10) and the unrelated cash-classification lean (l.337). The derived test is in 1-G and ties (Section 2). The H1 upstream-dividend precedent is cited (28.04 / 28.26 vs 0.13 / 0.20; FT l.307-308, l.337-339, l.681). Q5 stays the separating observation (l.476, l.648). No existing number changed | RESOLVED |
| C1 | 0 | CONTRADICTION | 22.70 rise in other non-current assets labelled capital advances and also counted in operating Other assets | l.301-304, l.311, l.319-322, l.331, l.335-338, l.406, l.434, l.474, l.487, l.519, l.569, l.590, l.687 | Filed classification is still the basis; reading A still stated with its numbers (capex 49.77 / 49.76; CFO/PAT 0.83x / 0.44x); Q16 separates. Ties: C 13.10 + 22.70 = 35.80 (FT l.606, l.619-620, l.697); SA 4.77 + 22.70 = 27.47 (FT l.244, l.258, l.321) | HOLDS |
| M1 | 0 | MISSING | Tariff-base effect not sized | l.195, l.223, l.238-255, l.385, l.524, l.560-561, l.693 | Re-pairing of the p26 chart re-derived (Section 2); all two-year figures tie | HOLDS (S10 basis note still open) |
| M2 | 0 | MISSING | PAT-level consolidation deduction absent | l.181-184, l.476, l.525, l.589, l.648, l.694, l.696 | Q2 50.88, Q1 3.71, H1 54.59; beyond dividend 22.84-22.97 / 26.55-26.68 tie | HOLDS |
| M3 | 0 | MISSING | 225.19 / 35.5% without upper-bound qualifier | l.178-179, l.183, l.384, l.472, l.586 | Qualifier present in all four places; basis "total revenues" (FT l.443) stated at l.183 | HOLDS |
| F1 | 0 | FACTUAL | "ESG slide claims ZLD" | l.83, l.479, l.512, l.680 | Text matches FT l.1369-1372. Grep of RV for "ZLD": zero hits | HOLDS |
| F2 | 0 | FACTUAL | OI remainder 12.97, dividend not bucketed | l.228 | 39.25 - 23.22 - 3.05 = 12.98; less 0.13 dividend (FT l.681) = 12.85 ND | HOLDS (S11 still open) |

Prior STYLE notes S1-S3 and S5-S15 still stand (wording unchanged at the cited places; S4 was resolved in loop 1). They stay logged below.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Heading (RV) | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | l.558 | 16 lines (l.559-574), inside 10-20. Results filing, so the 200-400 word Document Review rule does not govern | present |
| 2. Sector intelligence | l.576 | 6 bullets (l.577-582) | present |
| 3. Business-model intelligence | l.584 | 6 bullets (l.585-590) | present |
| 4. Competition intelligence | l.592 | 3 bullets (l.593-595) | present |
| 5. Forward map | l.597 | Make-or-break line (l.598) plus 8 catalysts (l.599-606), each with a bull fork and a bear fork. 7 are dated; the MPCB item (l.600) is still undated (STYLE S6) | present |

DELIVERABLE-COMPLETENESS: narrative present | sector present | business model present | competition present | forward map present. Gate PASS.

---

## 1. COVERAGE AUDIT

Fresh pass method: Grep over FT for numbered notes ("Notes :" FT l.357, l.735), forward-looking language ("on track", "expected to", "guidance", "target", "plans to", "FY27E", "Medium-term", "underway", "reaffirm", "commence", "estimated", "to be launched", "next leg", "will"), asterisk footnotes (FT l.908-1470), auditor paragraphs, entity lists and pages 20-43. Hand re-map of all six financial tables. Grep of ST: 1,782 row IDs (ST header l.4: NUMBER 1,292 + ENTITY 98 + FORWARD 37 + DATE 292 + QUALIFIER 63).

| Category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Notes | 7 | 7: SA Notes 1-3 (FT l.358-367), C Notes 1-4 (FT l.736-749) = R1729-R1731, R1749-R1752 | none | PASS |
| Footnotes (unnumbered) | 14 (R1766-R1779) | Every asterisk line maps to a row (FT l.1114, l.1121, l.1128, l.1137, l.1148-1160, l.1173, l.1201, l.1276-1277, l.1280, l.1282, l.1286, l.1443, l.1449, l.1467, l.1470). FT l.908 "***" is a separator | none | PASS |
| Disclaimers | 4 | 4 rows on p22 (R1761-R1764). The third safe-harbour paragraph (FT l.941-945, "review our most recent annual reports") has no row of its own; it sits inside the R1763 safe-harbour block (FT l.926-945) and carries no number, date or forward claim | none | PASS |
| Line items | 205 | 205: SA P&L 24, SA BS 30, SA CF 38, C P&L 32, C BS 31, C CF 41, media table 9. Counted from my own re-map; every item I mapped is in LG | none | PASS |
| Zero-standing flags | 11 | 6 genuine; 5 flagged rows carry values (SA/C held for sale 0.59/0.58; C OCI reclassifiable FT l.547; C CF net gain on financial assets FT l.687; C CF FX on cash FT l.728). A4 carries the correction (RV l.18) | n/a | Unchanged; STYLE S9 |
| Agenda items | 3 | 3: item 1 (FT l.40-43), press release (FT l.45-46), presentation (FT l.48-49); start time FT l.51 | none | PASS (STYLE S5) |
| Auditor paragraphs | 13 | 13: SA 4 (FT l.100, l.106, l.114, l.125); C 7 numbered (FT l.390, l.398, l.407, l.424, l.429, l.441, l.454) + 2 unnumbered (FT l.419, l.480) | none | PASS |
| Entities | 6 rows / 4 distinct | 6 / 4 (FT l.425-427; FT l.744-746) | none | PASS |
| Forward statements | 37 | 37 FORWARD rows (ST l.1405-1441) cover every grep hit. p24 restatements (FT l.970, l.973-974) duplicate R1399-R1401 | none | PASS (STYLE S8) |
| Slides | 24 | 24 (pages 20-43) | none | PASS |
| Slide numbers | 580 | 385 NUMBER (R908-R1292) + 195 DATE; spot checks of FT l.864, l.871, l.878, l.1059, l.1065, l.1160, l.1301 each return rows | none | PASS |
| MISSING_FROM_STRUCTURED | 4 | 4 (FT l.77, l.495, l.751, l.1478) | n/a | PASS |
| Turns / questions | 0 | 0 (results filing) | n/a | N/A |
| Structured IDs | 1,782 | 1,782 rows in ST; 1,782 referenced in LG; orphan_ids [] (LG l.18) | none | PASS |

Ledger-to-review check: A4's reconciliation preamble (RV l.16-19) is unchanged and its counts equal LG. Notes are cited by ID (RV l.68-81). Flagged rows are cited (R1737-R1740, R1767-R1769, R1778). Orphan rows: none. Rows my pass found that the ledger lacks: none. No A2 or A3 loop.

---

## 2. ARITHMETIC AUDIT

Independent tie-outs (re-run this loop, from FT):
- P&L: every column of SA and C Total Expenses sums from its components. Examples: SA Q2 FY27 296.62 - 0.82 + 42.87 + 42.11 + 1.57 + 12.72 + 109.15 = 504.22 (FT l.177-191); SA H1 FY26 displaced column 448.04 - 10.27 + 64.84 + 78.43 + 2.56 + 20.81 + 185.98 = 790.39; C FY26 1,029.20 - 73.00 + 129.33 + 194.46 + 8.20 + 45.13 + 405.41 = 1,738.73 (FT l.516-530).
- Balance sheet: SA non-current 1,757.90 / 1,711.47, current 1,469.87 / 1,221.68, total 3,227.77 / 2,933.15; liabilities 79.77 / 306.43 (FT l.236-288). C 1,760.62 / 1,715.13, 1,558.93 / 1,296.06, 3,319.55 / 3,011.19; liabilities 69.37 / 343.33 (FT l.597-651). SA non-current investments 103.44 / 80.69 (FT l.241 position) less C 101.58 / 79.35 (FT l.602 position): the gap rose from 1.34 to 1.86, the same 0.52 as the SA H1 investment in subsidiary (FT l.335).
- Cash flow: SA operating profit 325.16, cash generated 154.58, CFO 94.70, B (70.08), C (33.78), net (9.16), closing 35.98 (FT l.298-355). C 358.61 / 261.38 / 195.34 / (95.26) / (36.53) / 63.55; 126.53 + 63.55 + 1.54 = 191.62 (FT l.665-733). C financing order re-mapped: finance cost (5.34) = P&L finance cost, lease repayment (3.11), dividend (27.88), margin money 2.99, unclaimed (3.19) (FT l.720-726).

| Metric | A4 value (RV line) | Recomputed | Source line (FT) | Status |
|---|---|---|---|---|
| F3 test: subsidiaries' own Q2 op EBITDA under (a) | at least 48.15, 16.8% of 286.63 (l.184) | 25.31 + 22.84 = 48.15; / 286.63 = 16.80% | l.443, derived 1-G | PASS |
| F3 test: Q1 under (a) | at least 9.55, 3.6% of 267.47 (l.184) | 5.84 + 3.71 = 9.55; / 267.47 = 3.57% | l.443-444 | PASS |
| F3 test: H1 under (a) | at least 57.70, 10.4% of 554.10 (l.184) | 31.15 + 26.55 = 57.70; / 554.10 = 10.41% | l.443 | PASS |
| F3 test: under (b) | 25.31 (8.8%) Q2; 31.15 (5.6%) H1 (l.184) | 25.31 / 286.63 = 8.83%; 31.15 / 554.10 = 5.62% | l.443 | PASS |
| F3 precedent | SA dividend 28.04 H1 FY27 / 28.26 H1 FY26 vs C 0.13 / 0.20 (l.184) | SA CF operating l.307-308 and investing l.337-339; C CF l.681, l.714 | l.307-308, l.337-339, l.681 | PASS |
| C Reported EBITDA Q2 FY27 | **188.99** (l.130, l.223) | 173.06 + 13.05 + 2.89 = **189.00**. Margin 27.173% (27.17% unchanged); two-year +26.0% and +297 bps unchanged | l.523, l.525, l.532 | FAIL at rounding scale (F5) |
| Finance cost basis (claim, not a metric) | "lease interest only" (l.286; also l.199, l.273) | C H1 5.34 on lease liabilities 15.66 -> 12.61 (avg 14.14) = 75.6% a year if all lease interest [5.34 x 2 / 14.14]; SA 3.08 on 12.15 -> 9.60 = 56.6%; subsidiaries 2.26 (5.34 - 3.08) on 3.51 -> 3.01 = 138.7% | l.184, l.271, l.277, l.523, l.634, l.640, l.720-721 | FAIL (F4) |
| C1 / M1 / M2 / M3 / F2 values | as in loop 1 (l.178-184, l.223, l.228, l.301-331) | Re-verified: 13.10 + 22.70 = 35.80; 4.77 + 22.70 = 27.47; 49.77 / 49.76; 218.04 / 262.09 = 0.832x; 117.40 / 266.45 = 0.441x; 695.53 / 621 = 1.1200, root 1.0583; 1,328.61 / 1,096 = 1.2122, root 1.1010; 1.16^2 = 1.3456; Q2 50.88, Q1 3.71, H1 54.59; 22.84-22.97, 26.55-26.68; 218.53 / 225.19 / 443.72; 12.98, 12.85 | l.170, l.202, l.244, l.258, l.307, l.321, l.443-444, l.457, l.509-541, l.606-620, l.681-697, l.1010-1024 | PASS |
| p26 chart re-pairing | Q4 FY24 447 ... Q2 FY27 696 (l.223, l.238-252) | Every revenue x margin matches its EBITDA label: 447 x 20.1% = 89.8 (90); 475 x 27.4% = 130.2 (130); 621 x 24.2% = 150.3 (150); 466 x 20.1% = 93.7 (94); 548 x 22.2% = 121.7 (121); 495 x 24.8% = 122.8 (123); 570 x 23.4% = 133.4 (133); 459 x 18.9% = 86.8 (87); 597 x 26.2% = 156.4 (157); 633 x 30.3% = 191.8 (192); 696 x 27.2% = 189.3 (189). FY25 sum 2,110 vs 2,109; FY26 2,121 vs 2,120.11 | l.1010, l.1021-1024, l.1116, l.1412 | PASS |
| All other derived metrics | Op EBITDA, margins, ETR, OI/PBT, PAT margin, gross margin, SA set, 1-G gaps, YoY/QoQ tables, PAT bridge and QoQ bridge, OI-revert and stripped EPS, days and CCC, CFO/PAT, FCF, net cash, 933 liquidity, ROCE set, EPS bases, PE, CMP gaps, guidance arithmetic, 8C thresholds, 6A pro-rata (l.128-136, l.164-183, l.195-230, l.246-259, l.270-287, l.300-333, l.370-378, l.427, l.439, l.450, l.462) | All re-derived. Examples: C Op EBITDA 173.06 + 13.05 + 2.89 - 19.53 = 169.47 (24.366%); SA 144.16 (22.735%); bridge 26.384 + 23.647 - 2.24 - 0.79 + 5.67 - 12.757 - 1.703 = 38.21; C CCC 9.830 + 63.322 - 25.440 = 47.71; SA CCC 39.338 + 56.774 - 27.659 = 68.45; ROCE 709.72 / 2,919.46 = 24.31%, adj 709.72 / 2,155.46 = 32.93%; TTM EPS 70.59 + 112.81 = 183.40; H2 need 1,171.39 (+10.99%); midpoint H2 294.28 / 1,171.39 = 25.12%; 8C 25.12% - 2.81% = 22.31%; Reported EBITDA Q2 FY26 133.30, Q1 FY27 191.72, H1 380.72 / 256.25, FY26 499.55 | l.170-224, l.509-585, l.597-651, l.665-733, l.1106-1137 | PASS |

Arithmetic mismatches above rounding: none. One slip at rounding scale (F5, 188.99 vs 189.00). It is tagged FACTUAL because no rounding path of the filed inputs gives 188.99 (the exact sum is 189.00); loop 0 gave the 12.97 vs 12.98 slip (F2) the same tag. No ratio, threshold or conclusion moves. By contrast S1 (-572 vs -571 bps) is a true rounding artefact (22.73% - 28.45% on rounded inputs) and stays STYLE.

---

## 3. ADVERSARIAL READ

The three most positive claims in the revised review:

### Claim 1: "Q2 strong at the operating level: revenue +22.09%, operating EBITDA +41.89%, ex-OI margin +340 bps; the headline growth is real at the operating level." (RV l.195-205, l.225, l.562)
Strongest bear counter, from the same extract: management credits growth to "robust demand and improved realizations" (FT l.796-797). Growth is on reported INR (FT l.953-954) for a group that exported 75% of FY26 sales (FT l.1199). Part of the lift can be price and currency, not volume.
Test [DERIVED, C, Q2 FY27 vs Q2 FY26, share of revenue]: by-nature gross margin +211 bps (52.58% to 54.69%); employee cost -89 bps (8.23% to 7.35%, FT l.521); other expenses -63 bps (17.44% to 16.81%, FT l.526); power and fuel +23 bps (5.94% to 6.17%, FT l.520). 211 + 89 + 63 - 23 = 340. The gain is broad: gross margin plus operating leverage. The volume-price split is not in the extract.
Survives? NO. The review already states that constant-currency growth is ND (l.223) and sizes the tariff base (M1). The extract holds no volume figure to push further.

### Claim 2: "FCF 168.27 strong; net cash 920.21 above the Notion FY27 base of 820; no borrowings; finance cost is lease interest only." (RV l.199, l.273, l.286, l.303, l.312, l.339, l.570)
Strongest bear counter, from the same extract: a debt-free group pays a finance cost that its leases cannot explain.
- H1 C finance cost is 5.34 (FT l.523; paid in financing, FT l.720). C lease liabilities were 15.66 at 31-Mar and 12.61 at 30-Sep (FT l.634, l.640: 9.09 + 6.57; 7.40 + 5.21). Principal repaid was 3.11 (FT l.721), which matches the 3.05 fall in the lease book.
- If the 5.34 were all lease interest, the rate would be 75.6% a year [DERIVED: 5.34 x 2 / 14.14]. Standalone: 3.08 on 12.15 falling to 9.60 is 56.6% (FT l.184, l.271, l.277).
- The subsidiaries carry 2.26 of H1 finance cost (5.34 - 3.08) on 3.51 falling to 3.01 of leases: 138.7% implied. It rose from 1.59 in H1 FY26 (+42%) and from 0.83 to 1.32 in Q2 (+59%) [DERIVED, FT l.184, l.523].
- No borrowings line sits on either balance sheet (FT l.271-288, l.634-651). So most finance cost is non-lease, and its source is ND. Readings: bank, LC or bill-discounting charges; interest on tax; interest on deposits held. If receivables are discounted or factored without recourse, receivables fall and CFO and cash rise with no borrowing on the balance sheet [INFERENCE].
Survives? YES. "Finance cost is lease interest only" is a claim the extract does not support, and the filed figures contradict it. FCF and net cash stand as filed; the qualifier is the open composition. Type FACTUAL (F4). Loop A4.

### Claim 3: "Cash conversion leans growth-induced: consolidated days are stable (receivable 9.83 vs 9.14; inventory 63.32 vs 67.01; CCC 47.71 vs 45.02)." (RV l.305-308, l.337)
Strongest bear counter, from the same extract: consolidated receivable days of 9.83 (71.56 on 2,657.22 annualised revenue; FT l.612 position, l.509) are low for a group that exports 75% (FT l.1199) through overseas subsidiaries in 90+ countries (FT l.906). The same subsidiaries pay non-lease finance cost with no borrowings (Claim 2). If part of the receivables is discounted, the low and stable days show a financing choice, not collection strength. The operating Other-assets drain also recurred in H1 FY26 (S14).
Survives? YES, in part. It does not reverse the direction: that would need the inference to be confirmed. But the review's missing-evidence list for the classification (l.337) does not name finance-cost composition or receivables discounting, and no question asks it. Type MISSING (M4). Loop A4.

### Mandatory acquisition-economics probe
The extract has no acquisition of a business, no third-party stake buy and no purchase consideration. Items tested:
- Investment in subsidiary 0.52 in H1 (SA CF, FT l.335; nil in H1 FY26; the SA less C non-current investment gap rose by the same 0.52, FT l.241, l.602 positions). Intra-group capital. If it went to the nil-revenue subsidiary (H1 loss 0.38, assets 0.18, FT l.454-458), price / target PAT is undefined (negative earnings). A4 asks (Q12, RV l.483).
- Lubrizol: an MoU with no consideration (FT l.830-833). No multiple to compute.
- TPU line: organic capex Rs 118 Cr (FT l.1057) for a claimed 150-200 bps consolidated margin uplift (FT l.1065). On Rs 2,500 Cr revenue (FT l.1108) that is Rs 37.5-50 Cr EBITDA a year, a 2.4-3.1 year pre-tax payback [DERIVED]. A4 keeps the uplift as a MGMT claim and a bull input (RV l.428, l.543).
No new counter.

---

## FINDINGS (tagged)

| ID | Type | Agent | Exact gap | Fix |
|---|---|---|---|---|
| F4 | FACTUAL | A4 | "Finance cost is lease interest only" (RV l.286), "(lease interest; no borrowings)" (l.199), "Recurring (lease interest)" (l.273). The extract does not break finance cost down, and the filed figures contradict the claim: H1 C finance cost 5.34 (FT l.523) on lease liabilities 15.66 -> 12.61 (FT l.634, l.640) implies 75.6% a year; SA 3.08 on 12.15 -> 9.60 implies 56.6% (FT l.184, l.271, l.277); subsidiaries 2.26 on 3.51 -> 3.01 implies 138.7%, up 42% YoY (H1 FY26 1.59) | Replace the l.286 sentence with: "Finance cost is not lease interest alone, and its composition is ND. No borrowings line sits on either balance sheet (l.271-288, l.634-651). If H1 consolidated finance cost of 5.34 (l.523) were all interest on leases of 15.66 falling to 12.61 (l.634-642), the rate would be 75.6% a year [DERIVED 5.34 x 2 / 14.14]; standalone 3.08 on 12.15 to 9.60 gives 56.6%. The subsidiaries carry 2.26 of it (5.34 - 3.08) on about 3.0-3.5 of leases, up from 1.59 in H1 FY26; Q2 1.32 vs 0.83. Readings: bank, LC or bill-discounting charges, interest on tax or on deposits. If receivables are discounted or factored, consolidated receivable days and CFO are flattered [INFERENCE]. Ask (Q17)." l.199 cell: "Small; composition ND (no borrowings; not lease interest alone, Step 4)". l.273 cell: "Recurring; composition ND (Step 4)". No number changes |
| F5 | FACTUAL | A4 | C Reported EBITDA Q2 FY27 shown as 188.99 (RV l.130, l.223). 173.06 + 13.05 + 2.89 = 189.00 (FT l.523, l.525, l.532). At rounding scale; margin 27.17%, +26.0% and +297 bps unchanged | Change 188.99 to 189.00 in both places |
| M4 | MISSING | A4 | The cash classification's missing-evidence list (RV l.337) omits finance-cost composition and receivables discounting. The "stable consolidated days" direction rests on receivable days of 9.83 for a 75% exporter (FT l.1199) while the subsidiaries pay non-lease finance cost with no borrowings (F4). No Step 8.5 question asks it | Add to the l.337 missing-evidence list: "finance-cost composition and any receivables discounting or factoring (Q17)". Add Q17 to Step 8.5 and the YAML questions list: "Finance cost was 5.34 in H1 with no borrowings and 12.61-15.66 of lease liabilities. What makes up finance cost? Does any group company discount or factor receivables: yes or no, and what amount was outstanding on 30-Sep-2026?" Category D / A4-4. Why it matters: decides whether the 9.83 receivable days and CFO 195.34 reflect collection or financing. Bull: bank, LC or tax-interest charges, no discounting. Bear: export receivables discounted at the subsidiaries; days and CFO flattered. Classification stays INDETERMINATE-WITH-DIRECTION; no verdict change |

---

## VERDICT
INCOMPLETE. Failing agent: A4. Three findings: F4 (FACTUAL), the unsupported "finance cost is lease interest only" at RV l.199, l.273, l.286; F5 (FACTUAL, rounding scale), Reported EBITDA 188.99 for 189.00 at RV l.130, l.223; M4 (MISSING), finance-cost composition and receivables discounting absent from the cash-classification evidence list (RV l.337) and from the questions. The loop-1 finding F3 is resolved, and all six loop-0 fixes still hold. The Plain-Language Brief gate passes. Coverage holds with no orphan rows and nothing missing from the ledger. No A2 or A3 loop. The fix is wording at five places (RV l.130, l.199, l.223, l.273, l.286), one added evidence item and one added question. No existing number changes except 188.99 -> 189.00, and the protocol verdict does not change.

## STYLE NOTES (logged, no re-run)
Carried from loops 0 and 1 (still open at the cited lines):
- S1. SA ex-OI QoQ shown as -572 bps (RV l.514, l.682). Unrounded it is -571 bps (22.735% - 28.445%).
- S2. "matching the deck's 23% and 32%" (RV l.378). Recomputed 23.82% and 32.93%. Say "close to"; the deck basis is ND.
- S3. "Q2 FY27 (25.31) sits near Q2 FY26 (18.60)" (RV l.184). It is 36% higher.
- S5. A2 ledger agenda rows cite R1297 / R1347, which are entity rows (ST l.1309, l.1359), not the enclosures (FT l.45-49).
- S6. Forward-map MPCB catalyst is undated (RV l.600; M2 at l.535). Give a date bound, for example "next Reg 30 update or the Q3 call by 14-Feb-2027".
- S7. A4 coverage uses a category-level "reviewed" mark (RV l.16-19). List uncited rows by ID next time.
- S8. p24 restatements of R1399-R1401 (FT l.970, l.973-974) have no FORWARD rows; verbatim duplicates of p18.
- S9. A2 zero_standing count of 11 is stale; 6 are genuine. A4 carries the correction (RV l.18).
- S10. The two-year margin climb "about 300 bps" in the brief (RV l.561), Flag 13 (l.524) and the YAML flag (l.693) omits the basis Step 2 states (l.223): chart EBITDA including other income. Add "including other income; ex-OI at least +17 bps, exact figure ND".
- S11. The ND remainder of 12.85 (RV l.228) may also hold sundry balances written back 0.04 (FT l.683) and profit on sale of PPE 0.15 (FT l.678). Say so in one clause.
- S12. Net cash +162.28 includes 21.28 of non-cash mutual-fund gain [711.75 - 618.19 - 72.28; FT l.611-612 position, l.716]. Without it net cash is 898.93, still above 820. Add to the Step 5 net-debt row (RV l.312).
- S13. Reading A CFO/PAT of 0.83x sits above the 0.65-0.80 band the review cites (RV l.301, l.336). Say "above the band".
- S14. Gap (c) in the cash classification (RV l.337) can add that the operating Other-assets drain recurred in H1 FY26 (31.20 C / 30.33 SA, FT l.697, l.321) when revenue was 2.9% below H1 FY25.
- S15. The Step 7 ROCE row (RV l.433) can add trailing-four-quarter ROCE beside the H1-annualised figure: TTM EBIT 574.41 / closing CE 2,919.46 = 19.68%, or 20.55% on average CE 2,795.64. Context for /fttcp, not a correction.
New this loop:
- S16. The 1-G test (RV l.184) states a strain on reading (a) only ("Reading (a) needs that jump in the same quarter its own premise raises the subsidiaries' purchase markup"). Two balancing points. First, stock bought at the old transfer price can carry into Q2 cost of sales, so a subsidiary margin can rise in the quarter its purchase price rises. Second, reading (b) has its own implication: if the subsidiaries' "total revenues" (FT l.443) include other income, then under (b) their Q2 operating revenue is about 262.86 (286.63 - 22.84 - 0.93) against about 260.04 in Q1 (267.47 - 3.71 - 3.72), +1.1%, while the parent grew 8.55% and the group 9.86%; under (a) it is 285.70 vs 263.75, +8.3% [DERIVED; 0.93 = 19.53 - 46.64 + 28.04, 3.72 = 19.72 - 16.00; FT l.171, l.510]. The "no lean" conclusion does not change. Add one sentence for symmetry.
- S17. Competition (RV l.593): "It also claims the world's largest single-site sun-control film capacity". The deck says both "World's largest single-location SCF capacity" (FT l.1160-1161) and "One of World's largest Single-location SCF capacity" (FT l.1328-1330). Quote the weaker form or note that the deck states both.

---

```yaml
stage: A5-adversary
company: "GRWRHITECH"
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
  - {metric: "C Reported EBITDA Q2 FY27 (rounding scale)", a4_value: "188.99 (RV l.130, l.223)", recomputed: "189.00 = 173.06 + 13.05 + 2.89; margin 27.17%, +26.0%, +297 bps unchanged", source_line: "FT l.523, l.525, l.532"}
surviving_bear_counters:
  - {claim: "FCF 168.27 strong; net cash 920.21; no borrowings; finance cost is lease interest only (RV l.199, l.273, l.286, l.303, l.312)", counter: "H1 C finance cost 5.34 on lease liabilities 15.66 -> 12.61 implies 75.6% a year if all lease interest; SA 3.08 implies 56.6%; subsidiaries 2.26 on 3.51 -> 3.01 implies 138.7%, up 42% YoY; no borrowings line; composition ND; receivables discounting is one reading [INFERENCE]", source_line: "FT l.184, l.271, l.277, l.523, l.634, l.640, l.720-721", type: FACTUAL}
  - {claim: "Cash conversion leans growth-induced; consolidated days stable (RV l.305-308, l.337)", counter: "Receivable days 9.83 for a 75% exporter coexist with non-lease finance cost and no borrowings; if receivables are discounted, stable days reflect financing, not collection; finance-cost composition and discounting status absent from the missing-evidence list and the questions", source_line: "FT l.509, l.523, l.612, l.634, l.640, l.1199", type: MISSING}
findings_by_type:
  factual:
    - "F4 (A4): 'Finance cost is lease interest only' (RV l.286; also l.199, l.273) unsupported and contradicted: H1 C finance cost 5.34 on leases 15.66 -> 12.61 implies 75.6% a year; SA 3.08 on 12.15 -> 9.60 implies 56.6%; subsidiaries 2.26 implies 138.7%, up 42% YoY (FT l.184, l.271, l.277, l.523, l.634, l.640)"
    - "F5 (A4): C Reported EBITDA Q2 FY27 188.99 should be 189.00 (173.06 + 13.05 + 2.89; FT l.523, l.525, l.532) at RV l.130, l.223; rounding scale, no ratio moves"
  missing:
    - "M4 (A4): cash-classification missing-evidence list (RV l.337) and Step 8.5 lack finance-cost composition and receivables discounting (Q17); receivable days 9.83 for a 75% exporter (FT l.1199) sit beside non-lease finance cost with no borrowings"
  contradiction: []
  style:
    - "S1: SA ex-OI QoQ -572 bps vs -571 unrounded (RV l.514, l.682)"
    - "S2: 'matching' deck ROCE 23%/32% vs recomputed 23.82%/32.93% (RV l.378)"
    - "S3: 25.31 'near' 18.60 is 36% higher (RV l.184)"
    - "S5: A2 agenda rows cite R1297/R1347, which are entity rows (ST l.1309, l.1359)"
    - "S6: forward-map MPCB catalyst undated (RV l.600, l.535)"
    - "S7: A4 coverage uses category-level reviewed mark; list uncited rows by ID next time (RV l.16-19)"
    - "S8: p24 forward restatements (FT l.970, l.973-974) lack FORWARD rows; duplicates of R1399-R1401"
    - "S9: A2 zero_standing 11 is stale (6 genuine); correction already in A4 (RV l.18)"
    - "S10: two-year margin climb 'about 300 bps' (RV l.524, l.561, l.693) omits the incl-other-income basis; ex-OI at least +17 bps, exact ND"
    - "S11: ND OI remainder 12.85 (RV l.228) may hold sundry write-back 0.04 and PPE sale profit 0.15 (FT l.678, l.683)"
    - "S12: net cash rise 162.28 includes 21.28 non-cash MF gain (FT l.611-612, l.716); still above 820 without it (RV l.312)"
    - "S13: reading A CFO/PAT 0.83x sits above the cited 0.65-0.80 band (RV l.301, l.336)"
    - "S14: Other-assets drain recurred in H1 FY26 (31.20 C / 30.33 SA, FT l.697, l.321); add to gap (c) (RV l.337)"
    - "S15: Step 7 ROCE row (RV l.433) can add TTM ROCE 19.68% closing CE / 20.55% average CE"
    - "S16: 1-G test (RV l.184) states a strain on (a) only; add that old-price stock can carry into Q2 cost of sales and that (b) implies subsidiaries' Q2 operating revenue about flat QoQ (262.86 vs 260.04, +1.1%) vs (a) 285.70 vs 263.75; no change to 'no lean'"
    - "S17: 'world's largest single-site SCF capacity' (RV l.593); deck says both 'World's largest' (FT l.1160-1161) and 'One of World's largest' (FT l.1328-1330)"
loop_back_to: "A4"
gap: "F4 (FACTUAL): remove 'finance cost is lease interest only' at RV l.286, l.199, l.273. State composition ND; no borrowings; H1 C finance cost 5.34 on leases 15.66 -> 12.61 implies 75.6% a year if all lease interest [5.34 x 2 / 14.14]; SA 3.08 on 12.15 -> 9.60 implies 56.6%; subsidiaries carry 2.26 (H1 FY26 1.59; Q2 1.32 vs 0.83); readings: bank/LC/bill-discounting charges, tax or deposit interest; receivables discounting would flatter days and CFO [INFERENCE]. F5 (FACTUAL): Reported EBITDA Q2 FY27 188.99 -> 189.00 at RV l.130, l.223. M4 (MISSING): add 'finance-cost composition and any receivables discounting or factoring (Q17)' to the RV l.337 missing-evidence list, and add Q17 (what makes up finance cost; does any group company discount or factor receivables, yes/no, amount at 30-Sep-2026) to Step 8.5 and the YAML questions. Classification and protocol verdict unchanged."
style_notes:
  - "S1: SA ex-OI QoQ -572 bps vs -571 unrounded (RV l.514, l.682)"
  - "S2: 'matching' deck ROCE 23%/32% vs recomputed 23.82%/32.93% (RV l.378)"
  - "S3: 25.31 'near' 18.60 is 36% higher (RV l.184)"
  - "S5: A2 agenda rows cite R1297/R1347, which are entity rows (ST l.1309, l.1359)"
  - "S6: forward-map MPCB catalyst undated (RV l.600, l.535)"
  - "S7: A4 coverage uses category-level reviewed mark; list uncited rows by ID next time"
  - "S8: p24 forward restatements lack FORWARD rows; duplicates of R1399-R1401"
  - "S9: A2 zero_standing 11 is stale (6 genuine); correction already in A4"
  - "S10: two-year margin climb 'about 300 bps' omits the incl-other-income basis; ex-OI at least +17 bps"
  - "S11: ND OI remainder 12.85 may hold sundry write-back 0.04 and PPE sale profit 0.15"
  - "S12: net cash rise includes 21.28 non-cash MF gain; still above 820 without it"
  - "S13: reading A CFO/PAT 0.83x sits above the cited 0.65-0.80 band"
  - "S14: Other-assets drain recurred in H1 FY26; add to gap (c)"
  - "S15: Step 7 ROCE row can add TTM ROCE 19.68% / 20.55%"
  - "S16: 1-G test strain stated on (a) only; add the (b) implication and the old-price-stock point"
  - "S17: deck states both 'World's largest' and 'One of World's largest' single-location SCF capacity"
analyst_note: "Loop-2 re-audit. F3 is resolved in all five places: the review draws no lean between the transfer-markup and intra-subsidiary-dividend readings, and the new 1-G test ties. All six loop-0 fixes still hold. Coverage holds, and every SA and C table was re-mapped from the fulltext and ties. One new substantive finding, F4: the review calls finance cost lease interest only. The group has no borrowings and leases of 12.61-15.66, yet paid 5.34 of finance cost in H1, a 75.6% implied rate; the subsidiaries alone pay 2.26, up 42% YoY. The source is not disclosed. One reading is receivables discounting, which would fit receivable days of 9.83 for a 75% exporter, so M4 asks for it in the cash-classification evidence list and as Q17. F5 (188.99 vs 189.00) is tagged FACTUAL because no rounding path gives 188.99, but it moves no ratio and rides the same loop. The fix is wording, one question and one evidence item; the protocol verdict and the classification do not change. Sixteen STYLE notes are logged."
```
