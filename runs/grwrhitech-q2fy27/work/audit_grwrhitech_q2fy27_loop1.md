# A5 ADVERSARY RE-AUDIT (CORRECTION LOOP 1): GRWRHITECH (Garware Hi-Tech Films Limited) | Q2 FY27

Audited artifact: runs/grwrhitech-q2fy27/work/review_grwrhitech_q2fy27.md (A4, revised, 697 lines, header l.9 "Correction loop 1").
Prior audit: runs/grwrhitech-q2fy27/work/audit_grwrhitech_q2fy27.md (findings C1, M1, M2, M3, F1, F2; STYLE S1-S9).
Inputs read: A1 fulltext (FT, 1,492 lines), A1 structured (ST, R001-R1782), A2 ledger (LG), A4 review (RV), prior A5 audit. No source PDF opened. Nothing under inputs/ opened. A3 reasoning not read.
Anchors: "FT l.N", "ST l.N", "LG l.N", "RV l.N" are line numbers in those files. [DERIVED] = my arithmetic on filed numbers, formula shown.
Scope: Notion values (RV l.26-56) and the orchestrator-supplied MPCB Reg 30 facts (RV l.82) are outside A5 inputs. I check their internal arithmetic and the filing's silence only. A fresh grep of FT for "MPCB|pollution|consent|bank guarantee|forfeit" returns one hit, the ESG slide (FT l.1370). The filing is silent on the MPCB action.

---

## PRIOR FINDINGS STATUS (loop 0 -> loop 1)

| ID | Type | Prior gap (short) | Where A4 fixed it (RV) | My re-check | Status |
|---|---|---|---|---|---|
| C1 | CONTRADICTION | 22.70 rise in other non-current assets labelled capital advances and also counted in operating Other assets | l.300-303, l.310, l.318-321, l.330 (note), l.335-337, l.405, l.433, l.473, l.486 (Q16), l.518, l.568, l.589 | A4 keeps the filed operating classification (reading B) as basis and states reading A with its numbers. Ties re-derived: C 13.10 + 22.70 = 35.80 (FT l.606, l.619-620, l.697); SA 4.77 + 22.70 = 27.47 (FT l.244, l.258, l.321). Reading A: capex 49.77 C / 49.76 SA; CFO/PAT 218.04 / 262.09 = 0.832x C, 117.40 / 266.45 = 0.441x SA. FCF unchanged. Separating observation named (FY27 AR note or Q16). The "advances explain the TPU gap" bull reading is now conditional on reading A (l.337, l.405, l.473). No cell still asserts the advances label as fact | RESOLVED |
| M1 | MISSING | Tariff-base effect not sized | l.194, l.222, l.237-248, l.254, l.384, l.523, l.559-560, l.691 | FY25 re-pairing confirmed independently (see Section 2). Q2 two-year +12.0% (5.8% a year), H1 +21.2% (10.1% a year), +34.6% for two years at 16% all tie. Margin climb +297 bps Q2 / +311 bps H1 ties on the chart (incl other income) basis | RESOLVED (basis wording: STYLE S10) |
| M2 | MISSING | PAT-level consolidation deduction absent; release reading unsupported | l.180-183, l.475, l.524, l.588, l.646, l.692, l.694 | Q2 50.88, Q1 3.71, H1 54.59; beyond dividend 22.84-22.97 Q2, 26.55-26.68 H1, all tie (Section 2). Release reading withdrawn with the correct reason. Q5 extended with the intra-subsidiary dividend question | RESOLVED as specified. The lean to reading (a) that came with the graft is not supported: new finding F3 |
| M3 | MISSING | 225.19 / 35.5% stated without upper-bound qualifier | l.177-178, l.182, l.383, l.471, l.585 | Qualifier present in 1-G, 6B item 2, Q1 and the brief. Basis ("total revenues", FT l.443) stated at l.182 | RESOLVED |
| F1 | FACTUAL | "ESG slide claims ZLD" | l.82, l.478, l.511, l.678 | Text now matches FT l.1369-1372: "Zero Liquid Discharge initiatives" and "100% water recycling through advanced treatment processes". Grep of RV for "ZLD" returns zero hits | RESOLVED |
| F2 | FACTUAL | OI remainder 12.97, dividend not bucketed | l.227 | 39.25 - 23.22 - 3.05 = 12.98; less dividend 0.13 (FT l.681) = 12.85 ND | RESOLVED (two further small known items: STYLE S11) |

Prior STYLE notes: S4 is resolved (RV l.588 now says "subsidiaries plus eliminations"). S1, S2, S3, S5, S6, S7, S8 and S9 still stand and stay logged (see STYLE NOTES).

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Heading (RV) | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | l.557 | 16 lines (l.558-573), inside 10-20. Results filing, so the 200-400 word rule does not govern | present |
| 2. Sector intelligence | l.575 | 6 bullets (l.576-581) | present |
| 3. Business-model intelligence | l.583 | 6 bullets (l.584-589) | present |
| 4. Competition intelligence | l.591 | 3 bullets (l.592-594) | present |
| 5. Forward map | l.596 | Make-or-break line (l.597) plus 8 catalysts (l.598-605), each with a bull fork and a bear fork. 7 are dated; the MPCB item (l.599) is still undated (STYLE S6) | present |

DELIVERABLE-COMPLETENESS: narrative present | sector present | business model present | competition present | forward map present. Gate PASS.

---

## 1. COVERAGE AUDIT

Fresh pass method: Grep over FT for numbered notes, asterisk footnotes (FT l.908-1470), forward-looking language ("on track", "expected to", "guidance", "target", "plans to", "FY27E", "Medium-term", "underway", "raises", "reaffirm", "commence", "estimated", "Commitments"), auditor paragraphs, entity lists and pages 20-43. I re-mapped every P&L, balance sheet and cash flow table by hand against its filed subtotals. ST header (ST l.4): NUMBER 1,292 + ENTITY 98 + FORWARD 37 + DATE 292 + QUALIFIER 63 = 1,782.

| Category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Notes | 7 | 7: SA Notes 1-3 (FT l.357-367), C Notes 1-4 (FT l.735-749) | none | PASS |
| Footnotes (unnumbered) | 14 (R1766-R1779) | Every asterisk line maps to a row: FT l.1114 (R1766), l.1121 (R1767), l.1128 (R1768), l.1137 (R1769), l.1148-1160 (R1770), l.1173 (R1771), l.1201 (R1772), l.1276-1277 (R1773), l.1280 (R1774), l.1282 (R1775), l.1286 (R1776), l.1443/l.1467 (R1777), l.1470 (R1778), l.1443 "Liquid Funds**" (R1779). FT l.908 "***" is a press-release separator | none | PASS |
| Disclaimers | 4 | 4 on p22 (FT l.928, l.947, l.952, l.953) = R1761-R1764 | none | PASS |
| Line items | 205 | 205: SA P&L 24 (FT l.170-224), SA BS 30, SA CF 38, C P&L 32, C BS 31 (adds DTA), C CF 41, media table 9 (FT l.772-788) | none | PASS |
| Zero-standing flags | 11 | 6 genuine. 5 flagged rows carry values: SA held for sale 0.59/0.58 (FT l.257 position), C held for sale (FT l.618 position), C OCI reclassifiable 0.14/0.09/1.71/0.23/3.82/5.15 (FT l.547), C CF net gain on financial assets (23.22)/(14.97) (FT l.687), C CF FX on cash 1.54/(0.57) (FT l.728). A4 carries the correction (RV l.17) | n/a | Unchanged from loop 0; STYLE S9 |
| Agenda items | 3 | 3: item 1 (FT l.40-43), press release (FT l.45-46), presentation (FT l.48-49); start time FT l.51 | none | PASS (ledger ID pointers: STYLE S5) |
| Auditor paragraphs | 13 | 13: SA 4 (FT l.100, l.106, l.114, l.125); C 7 numbered (FT l.390, l.398, l.407, l.424, l.429, l.441, l.454) plus 2 unnumbered (FT l.419, l.480) | none | PASS |
| Entities | 6 rows / 4 distinct | 6 / 4 (FT l.425-427; FT l.744-746) | none | PASS |
| Forward statements | 37 | 37 FORWARD rows (ST l.1405-1441) cover every grep hit. p24 restatements (FT l.970, l.973-974) duplicate R1399-R1401 | none | PASS (STYLE S8) |
| Slides | 24 | 24 (pages 20-43) | none | PASS |
| Slide numbers | 580 | 385 NUMBER + 195 DATE; p26 chart labels (FT l.1010-1032) all re-paired in Section 2 | none | PASS |
| MISSING_FROM_STRUCTURED | 4 | 4 (FT l.77, l.495, l.751, l.1478) | n/a | PASS |
| Turns / questions | 0 | 0 (results filing) | n/a | N/A |
| Structured IDs | 1,782 | 1,782 referenced; orphan_ids [] (LG l.18) | none | PASS |

Ledger-to-review check: A4's reconciliation preamble (RV l.15-18) is unchanged and its counts equal the ledger. Notes are cited by ID (RV l.67-80). Flagged rows are cited (R1737-R1740, R1767-R1769, R1778). Orphan rows: none. Rows my pass found that the ledger lacks: none. No A2 or A3 loop.

---

## 2. ARITHMETIC AUDIT

Independent tie-outs (re-run on this loop):
- P&L: SA Q2 FY27 296.62 - 0.82 + 42.87 + 42.11 + 1.57 + 12.72 + 109.15 = 504.22 (FT l.177-191). C Q2 FY27 = 542.00 and C Q1 FY27 = 476.34 (FT l.516-530). OCI ties in all six columns, SA and C (e.g. C Q2 -2.06 + 0.63 + 0.14 = -1.29, FT l.545-554).
- Balance sheet: SA non-current 1,757.90, current 1,469.87, total 3,227.77; liabilities 79.77 / 306.43; equity 2,841.57 (FT l.236-288). C 1,760.62 / 1,558.93 / 3,319.55; 69.37 / 343.33; equity 2,906.85 (FT l.597-651). Prior-date columns tie too.
- Cash flow: SA operating profit 325.16, cash generated 154.58, CFO 94.70, B (70.08), C (33.78), net (9.16), closing 35.98; prior 207.96 / 178.14 / 143.65 / (96.31) / (53.23) / (5.89) (FT l.298-355). C 358.61 / 261.38 / 195.34 / (95.26) / (36.53) / 63.55; 126.53 + 63.55 + 1.54 = 191.62; prior 237.83 / 201.82 / 163.03 / (124.13) / (55.23) / (16.33) / 93.60 (FT l.665-733).

| Metric | A4 value (RV line) | Recomputed | Source line (FT) | Status |
|---|---|---|---|---|
| C1: C Other assets split | 35.80 = 13.10 + 22.70 (l.303, l.330) | 91.67 - 78.57 = 13.10; 50.67 - 27.97 = 22.70; sum 35.80 | l.606, l.619-620, l.697 | PASS |
| C1: SA Other assets split | 27.47 = 4.77 + 22.70 (l.321, l.330) | 49.40 - 44.63 = 4.77; sum 27.47 | l.244, l.258, l.321 | PASS |
| C1: reading A capex | 49.77 C / 49.76 SA (l.301, l.319, l.330) | 27.07 + 22.70; 27.06 + 22.70 | l.711; l.331-332 | PASS |
| C1: reading A CFO and CFO/PAT | 218.04 / 117.40; 0.83x / 0.44x (l.300, l.318, l.330) | 195.34 + 22.70; 94.70 + 22.70; 218.04 / 262.09 = 0.832; 117.40 / 266.45 = 0.441 | l.709, l.541; l.329-333, l.202 | PASS |
| M1: FY25 chart re-pairing | Q1 475, Q2 621, Q3 466, Q4 548 (l.222, l.241-244) | Revenue x margin vs EBITDA label: 475 x 27.4% = 130.2 (130); 621 x 24.2% = 150.3 (150); 466 x 20.1% = 93.7 (94); 548 x 22.2% = 121.7 (121); also Q4 FY24 447 x 20.1% = 89.8 (90), Q3 FY26 459 x 18.9% = 86.8 (87), Q4 FY26 597 x 26.2% = 156.4 (157). FY25 sum 2,110 vs filed 2,109; FY26 sum 2,121 vs 2,120.11 | l.1010, l.1015-1017, l.1021-1024, l.1116, l.1412 | PASS |
| M1: Q2 FY26 vs Q2 FY25 | -8.3% (l.222, l.246) | 569.69 / 621 - 1 = -8.26% | l.509, l.1010 | PASS |
| M1: two-year Q2 / H1 | +12.0%, 5.8% a year; +21.2%, 10.1% a year (l.222) | 695.53 / 621 = 1.1200, root 1.0583; 1,328.61 / 1,096 = 1.2122, root 1.1010 | l.509, l.1010 | PASS |
| M1: base two-year | +34.6% (l.222) | 1.16 x 1.16 = 1.3456 | derived | PASS |
| M1: two-year margin | Q2 150 (24.2%) -> 188.99 (27.17%), +26.0%, +297 bps; H1 280 (25.55%) -> 380.72 (28.66%), +36.0%, +311 bps (l.222) | 1.2599, +297 bps; 280 / 1,096 = 25.547%, 380.72 / 280 = 1.3597, +310.9 bps | l.523-532, l.1021-1022 | PASS (basis: STYLE S10) |
| M1: Q3 seasonal fall (brief) | -25% FY25, -19% FY26 (l.577) | 466 / 621 - 1 = -24.96%; 459 / 569.69 - 1 = -19.43% | l.509, l.1010 | PASS |
| M2: PAT-level deduction | Q2 50.88, Q1 3.71, H1 54.59 (l.180) | 139.87 + 40.55 - 0.10 - 129.44 = 50.88; 126.58 + 10.06 - 0.28 - 132.65 = 3.71; 266.45 + 50.61 - 0.38 - 262.09 = 54.59 | l.202, l.443-444, l.457, l.541 | PASS |
| M2: beyond dividend | Q2 22.84-22.97; H1 26.55-26.68 (l.181) | 50.88 - 28.04 / - 27.91; 54.59 - 28.04 / - 27.91; 27.91 = 28.04 - 0.13 | l.307, l.681 | PASS |
| M2: Q1 third-subsidiary loss; OI gap | 0.28; -27.11 Q2, +3.72 Q1 (l.182) | 0.38 - 0.10; 19.53 - 46.64; 19.72 - 16.00 | l.457, l.171, l.510 | PASS |
| M3: intra-group revenue | 218.53 (37.4%); 225.19 (35.5%); 443.72 (36.4%) (l.177-178) | 584.14 + 267.47 - 633.08; 634.09 + 286.63 - 695.53; 1,218.23 + 554.10 - 1,328.61; 37.41% / 35.51% / 36.42% | l.170, l.443, l.509 | PASS |
| F2: OI remainder | 12.98, dividend 0.13, ND 12.85 (l.227) | 39.25 - 23.22 - 3.05 = 12.98; - 0.13 = 12.85 | l.510, l.675, l.681, l.687 | PASS (STYLE S11) |
| Unchanged loop-0 metrics | Op EBITDA, margins, ETR, YoY/QoQ, PAT bridge, OI-revert EPS, days, net cash, ROCE, EPS bases, guidance arithmetic, 8C thresholds (l.127-283, l.294-338, l.369-377, l.426, l.438, l.449, l.458, l.461-462) | Re-verified. Examples: SA YoY EBIT 131.44 vs 90.33 = +45.51%; C CCC 9.83 + 63.32 - 25.44 = 47.71; ROCE 709.72 / 2,919.46 = 24.31%; TTM EPS 70.59 + 112.81 = 183.40; H2 need 1,171.39; 8C 25.12% - 2.81% = 22.31% | l.170-220, l.509-577, l.597-651, l.665-733, l.1108-1118 | PASS |

Arithmetic mismatches above rounding: none.

---

## 3. ADVERSARIAL READ

The loop-0 counters (tariff base, the 22.70, the PAT bridge) are now grafted. The three most positive claims in the revised review:

### Claim 1: "Q2 strong: revenue +22.09%, operating EBITDA +41.89%, ex-OI margin +340 bps; the two-year margin climb of about 300 bps holds." (RV l.194-196, l.222, l.523, l.560)
Strongest bear counter, from the same extract: the two-year climb is measured on the chart's EBITDA, which includes other income (FT l.1021-1022; RV l.222 says "incl OI"). FY25 quarterly other income is not in the extract, so the two-year ex-OI climb is ND. Other income rose from 2.43% of Q2 FY26 revenue (13.86 / 569.69) to 2.81% (19.53 / 695.53), and 59% of H1 other income is mutual-fund gains (FT l.687).
Test [DERIVED]: ex-OI Q2 FY27 margin 24.37% already exceeds the incl-OI Q2 FY25 margin of 24.2%. Other income cannot be negative, so the two-year ex-OI climb is at least +17 bps. On H1, 25.70% vs 25.55% gives at least +15 bps. The +340 bps YoY figure is ex-OI and clean.
Survives? NO. The direction holds on any other-income level. Step 2 states the basis. The brief (l.560) and Flag 13 (l.523, l.691) drop the "incl other income" basis: STYLE S10.

### Claim 2: "FCF 168.27 strong; net cash 920.21 above the Notion FY27 base of 820, before H2 capex." (RV l.302, l.311, l.338, l.373, l.569)
Strongest bear counter, from the same extract:
- Part of the 162.28 rise in net cash is valuation, not cash. Current investments rose 93.56 (711.75 - 618.19, FT l.611-612 position) against net mutual-fund purchases of 72.28 (FT l.716). That leaves 21.28 of non-cash gain [DERIVED].
- FCF benefits from back-loaded capex: H1 capex 27.07 vs 86.82 a year earlier (FT l.711), against TPU 118 (FT l.1057) and SCF 191/192 (FT l.826, l.1213) committed, and "~170 cr capex" on slide 29 (FT l.1128).
Survives? NO. Without the 21.28, net cash is 898.93, still above 820. The review already says "capex back-ended" (l.302) and "before H2 capex" (l.338). The valuation component is not stated: STYLE S12.

### Claim 3: "Cash conversion leans growth-induced: consolidated days are stable." (RV l.336)
Strongest bear counter, from the same extract: the operating "Other assets" drain is not a growth effect. It was 31.20 C / 30.33 SA in H1 FY26 (FT l.697, l.321 prior column). In that half, revenue was 2.9% below H1 FY25 (1,064.68 vs 1,096 chart). That component is 35.80 of the 95.87 H1 FY27 build (37%), and it recurs whether or not sales grow.
Survives? NO, as a new counter. The review already carries the component as gap (c) and keeps the classification at INDETERMINATE-WITH-DIRECTION. The counter does not flip the direction for inventory and receivables, where days are stable. Adding the H1 FY26 recurrence to gap (c) is STYLE S14.

### Mandatory acquisition-economics probe
The extract has no acquisition of a business, no third-party stake buy and no purchase consideration. Items tested:
- Investment in subsidiary 0.52 in H1 (SA CF, FT l.335 position; nil in H1 FY26). This is intra-group capital. If it went to the nil-revenue subsidiary (H1 loss 0.38, assets 0.18, FT l.455-458), price / target PAT is undefined (negative earnings). A4 asks about it (Q12, RV l.482).
- Lubrizol: an MoU with no consideration (FT l.830-833). There is no multiple to compute.
- TPU line: organic capex Rs 118 Cr (FT l.1057) for a claimed 150-200 bps consolidated margin uplift (FT l.1065). On Rs 2,500 Cr revenue (FT l.1108) that is Rs 37.5-50 Cr EBITDA a year, a 2.4-3.1 year pre-tax payback [DERIVED]. A4 keeps the uplift as a MGMT claim and a bull input (RV l.427, l.542).
No new counter.

### Symmetric check (Master Rule J): the bear lean in the 1-G read. New finding F3.
The revised review states a lean to the bear reading of the consolidation deduction: "The evidence leans to (a)" (RV l.183); "the evidence leans to the transfer-price reading" (Flag 14, l.524; YAML flag l.692); "A change in prices between group companies is the leading reading" (brief, l.588); and the A4 analyst note (l.694). Reading (a) is a higher intra-group markup that builds unrealised profit in subsidiary stock. Reading (b) is a dividend between subsidiaries that is eliminated on consolidation. A bear claim carries the same evidence bar as a bull claim. This one does not meet it:
1. The beyond-dividend deduction (Q2 22.84-22.97; H1 26.55-26.68) is a residual: SA PAT + subsidiaries' PAT - third-subsidiary loss - C PAT - intra-group dividend (FT l.202, l.443-444, l.457, l.541, l.307, l.681). Any mix of an unrealised-profit rise and an intra-subsidiary dividend fits every filed line exactly. The residual cannot rank the two readings.
2. Withdrawing the "release" form of (b) is correct, because a release would shrink the deduction. That removes one form of (b). It does not favour (a) over the dividend form of (b).
3. Each reading rests on one undisclosed figure: (a) the unrealised-profit amount, (b) the intra-subsidiary dividend.
4. The filing gives the dividend form a precedent. The group pays upstream dividends to the parent in H1 each year: SA dividend income 28.04 in H1 FY27 and 28.26 in H1 FY26, against consolidated 0.13 and 0.20 (FT l.307-308, l.337-339, l.681). A chain dividend from the step-down Global Hi-Tech Films Inc (FT l.744-746) to its direct parent in the same window fits that pattern.
5. Reading (a) has its own strain [DERIVED]. With no intra-subsidiary dividend, the subsidiaries' own Q2 operating EBITDA equals the C - SA operating EBITDA of 25.31 plus the pre-tax unrealised-profit rise (at least 22.84). That is at least 48.15, or 16.8% of their Q2 revenue of 286.63. In Q1 it was at least 9.55 (5.84 + 3.71), or 3.6% of 267.47. Reading (a) needs that jump in the same quarter its own premise raises the subsidiaries' purchase markup. Under (b), the Q2 figure is 25.31 (8.8%). On H1, (a) needs at least 57.70 (31.15 + 26.55, 10.4% of 554.10) against 31.15 (5.6%) under (b).
6. Reading (a) also implies a higher parent margin on intra-group sales. The parent ex-OI margin fell 571 bps QoQ, from 28.45% to 22.73% (FT l.170-193), more than the group's 280 bps. The Q1 parent stock build of 43.55 (FT l.179) confounds this point, so it is directional only.
Result: the extract does not separate (a) from (b). The lean is a claim the extract does not support. Type FACTUAL. Loop A4. The lean entered through the loop-0 A5 audit (its Claim 3 said "the evidence now leans to reading (a)"). This audit withdraws it. Transfer pricing stays a live question, and Q5 (RV l.475) remains the separating observation.

---

## FINDINGS (tagged)

| ID | Type | Agent | Exact gap | Fix |
|---|---|---|---|---|
| F3 | FACTUAL | A4 | The review says the evidence leans to reading (a), a higher transfer markup (RV l.183, l.524, l.588, l.692, l.694). The extract does not support a lean. The beyond-dividend deduction (Q2 22.84-22.97, H1 26.55-26.68) is a residual that any mix of unrealised profit and intra-subsidiary dividend satisfies (FT l.202, l.307, l.443-444, l.457, l.541, l.681). The group pays the parent an H1 dividend every year (28.04 / 28.26, FT l.307-308), which gives (b) a filed precedent. Reading (a) needs the subsidiaries' own Q2 operating EBITDA at 48.15 or more (16.8% or more of 286.63), up from 9.55 or more (3.6%) in Q1, while their purchase markup rises; under (b) it is 25.31 (8.8%) | Replace the lean in the five places with: "The filing does not separate the two readings; each needs one undisclosed figure." In 1-G add the test in point 5 (subsidiaries' own operating EBITDA under each reading). Brief l.588: "The cause is not disclosed: either a change in prices between group companies or a dividend between subsidiaries." Keep Q5 as the separating observation. No number in the review changes |

No other FACTUAL, MISSING or CONTRADICTION finding. No arithmetic mismatch. No orphan row. Nothing missing from the ledger.

---

## VERDICT
INCOMPLETE. Failing agent: A4. One finding, F3 (FACTUAL): the unsupported lean to the transfer-markup reading at RV l.183, l.524, l.588, l.692 and l.694. All six loop-0 findings (C1, M1, M2, M3, F1, F2) are resolved. The Plain-Language Brief gate passes. Coverage holds and every recomputed figure ties. The fix is wording in five places plus one derived test in 1-G; no number changes. After that fix the review can go to save.

## STYLE NOTES (logged, no re-run)
Carried from loop 0:
- S1. SA ex-OI QoQ shown as -572 bps (RV l.513, l.680). Unrounded it is -571 bps (22.735% - 28.445%).
- S2. "matching the deck's 23% and 32%" (RV l.377). Recomputed 23.82% and 32.93%. Say "close to"; the deck basis is ND.
- S3. "Q2 FY27 (25.31) sits near Q2 FY26 (18.60)" (RV l.183). It is 36% higher.
- S5. A2 ledger agenda rows cite R1297 / R1347, which are the SEBI and exchange-code entity rows (ST l.1309, l.1359), not the enclosures (FT l.45-49).
- S6. Forward-map MPCB catalyst is undated (RV l.599). Give a date bound, for example "next Reg 30 update or the Q3 call by 14-Feb-2027".
- S7. A4 coverage relies on a category-level "reviewed" mark (RV l.15-18). List uncited rows by ID next time.
- S8. p24 restatements of R1399-R1401 (FT l.970, l.973-974) have no FORWARD rows. They are verbatim duplicates of p18.
- S9. A2 zero_standing count of 11 is stale; 6 are genuine. A4 carries the correction (RV l.17).
New this loop:
- S10. The two-year margin climb "about 300 bps" in the brief (RV l.560) and Flag 13 (l.523, l.691) omits the basis that Step 2 states (l.222): chart EBITDA including other income. Add "including other income; ex-OI at least +17 bps, exact figure ND".
- S11. The ND remainder of 12.85 (RV l.227) may also hold sundry balances written back 0.04 (FT l.683) and profit on sale of PPE 0.15 (FT l.678). The filing does not say which P&L line carries them. Say so in one clause.
- S12. Net cash +162.28 includes 21.28 of non-cash mutual-fund gain [711.75 - 618.19 - 72.28; FT l.611-612, l.716]. Without it, net cash is 898.93, still above 820. Add the composition to the Step 5 net-debt row (RV l.311).
- S13. Reading A CFO/PAT of 0.83x sits above the 0.65-0.80 band the review cites (RV l.300, l.335). Name the band it falls in, or say "above the band".
- S14. Gap (c) in the cash classification (RV l.336) can add that the operating Other-assets drain recurred in H1 FY26 (31.20 C / 30.33 SA, FT l.697, l.321) when revenue was 2.9% below H1 FY25. That component does not track growth.
- S15. The Step 7 ROCE row (RV l.432) can add trailing-four-quarter ROCE beside the H1-annualised figure: TTM EBIT 574.41 [(454.42 - 234.87) + 354.86] / closing CE 2,919.46 = 19.68%, or 20.55% on average CE 2,795.64. The review uses the trailing base for EPS on seasonality grounds (l.426). Seasonality alone is small (H1 FY26 was 51.7% of FY26 EBIT); most of the gap is the tariff-hit H2 FY26, so this is context for /fttcp, not a correction.

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
arithmetic_mismatches: []
surviving_bear_counters: []
findings_by_type:
  factual:
    - "F3 (A4): review says the evidence leans to reading (a), a higher transfer markup (RV l.183, l.524, l.588, l.692, l.694). Unsupported: the beyond-dividend deduction (Q2 22.84-22.97, H1 26.55-26.68) is a residual that any mix of unrealised profit and intra-subsidiary dividend satisfies (FT l.202, l.307, l.443-444, l.457, l.541, l.681); the group pays the parent an H1 dividend every year (28.04 / 28.26, FT l.307-308), a precedent for (b); (a) needs subsidiaries' own Q2 operating EBITDA >= 48.15 (>= 16.8% of 286.63) vs >= 9.55 (3.6%) in Q1 while their purchase markup rises; (b) gives 25.31 (8.8%)"
  missing: []
  contradiction: []
  style:
    - "S1: SA ex-OI QoQ -572 bps vs -571 unrounded (RV l.513, l.680)"
    - "S2: 'matching' deck ROCE 23%/32% vs recomputed 23.82%/32.93% (RV l.377)"
    - "S3: 25.31 'near' 18.60 is 36% higher (RV l.183)"
    - "S5: A2 agenda rows cite R1297/R1347, which are SEBI and exchange-code entity rows (ST l.1309, l.1359)"
    - "S6: forward-map MPCB catalyst undated (RV l.599)"
    - "S7: A4 coverage uses category-level reviewed mark; list uncited rows by ID next time (RV l.15-18)"
    - "S8: p24 forward restatements (FT l.970, l.973-974) lack FORWARD rows; verbatim duplicates of R1399-R1401"
    - "S9: A2 zero_standing 11 is stale (6 genuine); correction already in A4 (RV l.17)"
    - "S10: two-year margin climb 'about 300 bps' in brief and Flag 13 (RV l.523, l.560, l.691) omits the incl-other-income basis stated at l.222; ex-OI climb at least +17 bps, exact ND"
    - "S11: ND OI remainder 12.85 (RV l.227) may hold sundry balances written back 0.04 and PPE sale profit 0.15 (FT l.678, l.683); P&L line not stated"
    - "S12: net cash rise 162.28 includes 21.28 non-cash MF gain (711.75 - 618.19 - 72.28; FT l.611-612, l.716); still above 820 without it (RV l.311)"
    - "S13: reading A CFO/PAT 0.83x sits above the cited 0.65-0.80 band (RV l.300, l.335)"
    - "S14: Other-assets drain recurred in H1 FY26 (31.20 C / 30.33 SA, FT l.697, l.321) with revenue down 2.9% on H1 FY25; add to gap (c) (RV l.336)"
    - "S15: Step 7 ROCE row (RV l.432) can add TTM ROCE 19.68% closing CE / 20.55% average CE (TTM EBIT 574.41) beside H1-annualised 24.31%"
loop_back_to: "A4"
gap: "F3 (FACTUAL): remove the unsupported lean to reading (a) at RV l.183, l.524, l.588, l.692, l.694. State that the filing does not separate (a) higher transfer markup from (b) intra-subsidiary dividend; each needs one undisclosed figure. In 1-G add the test: under (a) the subsidiaries' own Q2 operating EBITDA is at least 25.31 + 22.84 = 48.15 (16.8% of 286.63), up from at least 9.55 (3.6% of 267.47) in Q1, while their purchase markup rises; under (b) it is 25.31 (8.8%). Note the H1 upstream-dividend precedent (SA dividend income 28.04 H1 FY27, 28.26 H1 FY26 vs C 0.13 / 0.20; FT l.307-308, l.681). Keep Q5 as the separating observation. No number changes."
style_notes:
  - "S1: SA ex-OI QoQ -572 bps vs -571 unrounded (RV l.513, l.680)"
  - "S2: 'matching' deck ROCE 23%/32% vs recomputed 23.82%/32.93% (RV l.377)"
  - "S3: 25.31 'near' 18.60 is 36% higher (RV l.183)"
  - "S5: A2 agenda rows cite R1297/R1347, which are SEBI and exchange-code entity rows (ST l.1309, l.1359)"
  - "S6: forward-map MPCB catalyst undated (RV l.599)"
  - "S7: A4 coverage uses category-level reviewed mark; list uncited rows by ID next time (RV l.15-18)"
  - "S8: p24 forward restatements (FT l.970, l.973-974) lack FORWARD rows; verbatim duplicates of R1399-R1401"
  - "S9: A2 zero_standing 11 is stale (6 genuine); correction already in A4 (RV l.17)"
  - "S10: two-year margin climb 'about 300 bps' in brief and Flag 13 omits the incl-other-income basis; ex-OI at least +17 bps, exact ND"
  - "S11: ND OI remainder 12.85 may hold sundry balances written back 0.04 and PPE sale profit 0.15 (FT l.678, l.683)"
  - "S12: net cash rise includes 21.28 non-cash MF gain; still above 820 without it"
  - "S13: reading A CFO/PAT 0.83x sits above the cited 0.65-0.80 band"
  - "S14: Other-assets drain recurred in H1 FY26 (31.20 C / 30.33 SA) with revenue down 2.9%; add to gap (c)"
  - "S15: Step 7 ROCE row can add TTM ROCE 19.68% / 20.55% beside H1-annualised 24.31%"
analyst_note: "Re-audit after loop 1. All six prior non-STYLE findings are resolved: C1 (filed classification kept as basis, reading A stated with capex 49.77 and CFO/PAT 0.83x / 0.44x, Q16 separates), M1 (two-year figures in Step 2, Step 3, 6B, brief and Flag 13; chart re-pairing re-derived), M2 (PAT bridge added, release reading withdrawn, Q5 extended), M3 (upper bound stated in four places), F1 (slide quoted exactly), F2 (12.98, ND 12.85). Coverage holds and every recomputed figure ties. One new FACTUAL finding, F3. The review now says the evidence leans to the transfer-markup reading. That lean came from the loop-0 A5 audit, and this audit withdraws it. The beyond-dividend deduction is a residual that any mix of unrealised profit and intra-subsidiary dividend satisfies. The group's yearly H1 upstream dividend gives the dividend reading a filed precedent. The markup reading needs the subsidiaries' own Q2 operating EBITDA at 16.8% or more of their revenue in the quarter their purchase markup rose. The fix is wording in five places plus one derived test; no number changes. Fourteen STYLE notes are logged (S4 resolved)."
```
