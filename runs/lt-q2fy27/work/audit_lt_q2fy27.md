# A5 ADVERSARY / COMPLETENESS AUDIT: Larsen & Toubro Limited (LT), Q2 FY27

Stage: A5-adversary | Model: claude-opus-5-5 | Run date: 2026-10-28 | Re-audit loop 1: 2026-10-29
Under audit: runs/lt-q2fy27/work/review_lt_q2fy27.md (loop 0: 1,257 lines; loop 1: 1,287 lines)
Inputs read: A1 fulltexts and structured files (results, presentation, concall, order PR), the three A2 ledgers, the A4 review. Not opened: the source PDFs and anything under runs/lt-q2fy27/inputs/. No input gap forced a source read.

Anchor convention: RF = results fulltext line; PF = presentation fulltext line; CC = concall fulltext line; OP = order press release fulltext line; "review Lnnn" = line in the A4 review. Units Rs crore unless stated. Sections 0-3 and the loop-0 verdict below refer to loop-0 review line numbers. The RE-AUDIT LOOP 1 section at the end refers to loop-1 line numbers and carries the current verdict and YAML block.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

DELIVERABLE-COMPLETENESS: narrative PRESENT | sector PRESENT | business_model PRESENT | competition PRESENT | forward_map PRESENT. Gate PASSES.

| Part | Heading (review line) | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | "## 1. SUMMARY NARRATIVE" (L1088) | 15 bullet lines (L1089-L1103), within the 10-20 line band; numbers tagged FILED / MGMT / ASR-MGMT / COMPUTED | present |
| 2. Sector intelligence | "## 2. SECTOR INTELLIGENCE" (L1105) | 8 bullets: Gulf hydrocarbons, PDO framework, West Asia freight, China solar modules, Indian private capex, RBI repo, offshore wind, one INFERENCE | present |
| 3. Business-model intelligence | "## 3. BUSINESS-MODEL INTELLIGENCE" (L1115) | 8 bullets: threshold recognition, advance loop, listed subsidiaries, PP&M RoFE, capital drift to owned assets | present |
| 4. Competition intelligence | "## 4. COMPETITION INTELLIGENCE" (L1125) | 9 bullets: win factors, three PDO rivals, water and solar weakness, TPS pricing, peer gap stated | present (one attribution defect, F3) |
| 5. Forward map | "## 5. FORWARD MAP" (L1136) | 11 catalysts, 10 dated plus Hormuz "not dated", each with a bull and a bear fork | present (one fork rests on an unsupported basis, F7) |

---

## 1. COVERAGE AUDIT

Method: my own grep and line sweep over each A1 FULLTEXT, then a diff against the A2 counts. ID accountability: each A2 ledger reports ids_in_structured equal to ids_referenced (results 2,511, presentation 1,498, concall 492). A4 declares every ID range reviewed (review L19-L24: "Unreviewed ledger rows: none"). I tested that declaration by spot checks of material rows (see the note under the table).

| Doc | Category | A2 count | My fresh count | Evidence of my count | Orphan rows | Status |
|---|---|---|---|---|---|---|
| Results | notes | 41 | 41 | 29 roman notes (RF L515, L516, L521, L595, L620, L703, L774, L775, L849, L852, L860, L876, L884, L885, L958, L959, L964, L967, L973, L1047, L1097, L1166, L1167, L1234, L1236, L1244, L1256, L1259, L1260) + 4 lettered (RF L642, L643, L645, L647) + 4 CF notes (RF L770, L772, L1162, L1164) + item 15 (RF L1065) + 2 not-material footnotes (RF L698, L1094) + 1 formulae Note (RF L1066) | none | PASS |
| Results | line items | 400 | 400 | C_PL 41 (RF L468-L513), C_BS 54 (RF L530-L594), C_SA 4 (RF L603-L615), C_RAT 14 (RF L627-L640), C_CF 57 (RF L708-L768), C_SEG 50 (RF L795-L847), S_PL 32 (RF L916-L956), S_BS 48 (RF L981-L1042), S_RAT 14 (RF L1051-L1064), S_CF 48 (RF L1103-L1160), S_SEG 38 (RF L1190-L1232) | none | PASS |
| Results | Annexure 1 items | 58 | 58 | 8 group rows (RF L377-L384) + 24 Q2 segment cells-rows (RF L387-L395) + 24 H1 (RF L401-L409) + 2 notes (RF L414-L419) | none | PASS |
| Results | zero-standing cells | 42 | 42 | dash/NIL cells: RF L487 x5, CF L720, L745, L746, L747, L749, L750, L757 x7, L802 x1, L820 x5, L936 x3, L1130, L1132, L1138, L1149 x4, L1210-L1211 x3, L394 x2, Annexure III x2 = 32; "0.00" cells RF L632 x5, L1056 x5 = 10 | none | PASS |
| Results | agenda items | 5 | 5 | RF L44 (approval), L50 (Annexure I), L54 (Annexure II), L59 (Annexure III), L61-L64 (Reg 54 not applicable) | none | PASS |
| Results | auditor paragraphs | 16 | 16 | consolidated paras 1-9 (paras 6-9 read at RF L1332-L1402), standalone paras 1-7 | none | PASS |
| Results | entities | 177 | 177 | consolidated Annexure A: 94 subsidiaries (RF L1430-L1581) + 6 associates (L1583-L1588) + 9 JVs (L1590-L1609) + 34 joint operations (L1611-L1646) + parent (L1428) = 144; standalone 33 accepted on the 10 + 22 joint-operation cross-foot | none | PASS |
| Results | forward rows | 16 | 16 | press release RF L166, L168, L172, L305, L325, L337, L343, L347, L352; notes RF L516, L852, L959, L964, L967, L1236, L1939 | none | PASS |
| Results | signature blocks | 6 | 6 | RF L90, L781, L891, L1176, L1270, L1952 | none | PASS |
| Presentation | slides | 36 | 36 | 36 "[page N]" markers in the fulltext (grep count) | none | PASS |
| Presentation | slide numbers / qualifiers / forward / dates / entities | 1,352 / 77 / 16 / 18 / 35 | spot-checked, not re-enumerated cell by cell | appendix rows PF L954-L976 tie to every A4 cite I tested; qualifier rows present for PF L110, L142, L201-L202, L220-L222 (R1439), L389, L475, L546, L579, L606, L766, L811, L922, L946 | none | PASS (spot) |
| Concall | questions | 21 | 21 | question starts at CC L345, L377, L398, L420, L432, L451, L473, L482, L500, L529, L540, L574, L605, L624, L636, L657, L686, L713, L747, L774, L816; follow-ups (CC L367, L405, L439, L525, L566, L596) sit inside their parent rows | none | PASS |
| Concall | turns (approximate) | 45 | 45 | moderator intro + prepared remarks + 21 x (question + answer) + close | none | PASS |
| Concall | management numbers / forward / qualifiers / dates / entities | 206 / 74 / 90 / 29 / 72 | spot-checked | R101 (CC L136), R103 (L138), R165 (L206), R412 (L623), R446 (L701), R484 (L823) present | none | PASS (spot) |
| Order PR | structured rows (A1 only, no A2 by design) | n.a. | 69 rows read by A4 | A4 claims checked against OP L75-L126 | n.a. | PASS on coverage; one unsupported basis claim (F7) |

Result: orphan_rows = [] and missing_from_ledger = []. My fresh pass found no unit the ledgers lack beyond the MFS rows A2 already logged (results MFS-1 to MFS-3; concall MFS-1 to MFS-5).

Note on substantive coverage. A4 cites no figure for FS NIM + fees (RF L416), the FS loan book (RF L291), DSCR / ISCR (RF L628-L629) or FS PCR / CRAR (PF L502-L503). These fall under A4's blanket "all reviewed" declaration and carry no finding, so they are not orphans. One cited row is cited incompletely: presentation R1439 (PF L220-L222) loses its second clause. That is finding F2, a content gap, not an orphan.

---

## 2. ARITHMETIC AUDIT

Every derived metric in A4's tables was recomputed from the raw extracted cells. No mismatch above rounding. Rounding-level drifts are logged as STYLE (S4).

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Operating EBITDA Q2 FY27 | 6,844.65 | 7,641.06 + 1,036.91 + 472.94 - 2,306.26 = 6,844.65 | RF L486, L484, L483, L469 | PASS |
| Operating EBITDA Q2 FY26 / Q1 FY27 | 6,806.41 / 6,116.48 | 6,806.41 / 6,116.48 | RF L469-L486 | PASS |
| Operating EBITDA FY26 / H1 FY26 / H1 FY27 | 29,151.14 / 13,124.07 / 12,961.13 | identical | RF L469-L486 | PASS |
| Operating EBITDA margin Q2 FY27 / Q2 FY26 / Q1 FY27 | 8.69% / 10.01% / 9.00% | 8.692% / 10.012% / 9.003%; filed row 8.69% / 10.01% / 9.00% | RF L636 | PASS |
| Margin change YoY | -132 bps | -132.0 bps | RF L636 | PASS |
| Reported EBITDA Q2 FY27 | 9,150.91 | 9,150.91; deck 9,151 | RF L486; PF L970 | PASS |
| Reported EBITDA margin | 11.62% vs 12.05% | 11.620% vs 12.048% | RF L468, L486 | PASS |
| Core PBT (PBT - OI) Q2 FY27 / Q2 FY26 | 5,334.80 / 4,951.83 (+7.73%) | 5,334.80 / 4,951.83 (+7.734%) | RF L469, L486 | PASS |
| OI / PBT Q2 FY27 / Q2 FY26 / H1 FY27 | 30.2% / 21.8% / 32.2% | 30.18% / 21.85% / 32.16% | RF L469, L486 | PASS |
| ETR Q2 FY27 / Q2 FY26 | 22.6% / 26.0% | 22.587% / 26.026% | RF L488, L492 | PASS |
| Current-tax ETR Q2 FY27 / H1 FY27 | 27.0% / 27.1% | 27.00% / 27.08% | RF L490 | PASS |
| PAT margin Q2 FY27 | 6.61% | 6.606% | RF L468, L496 | PASS |
| YoY: revenue / op EBITDA / D&A / FC / OI / PBT / owners PAT / EPS | +15.84% / +0.56% / -5.02% / -38.00% / +66.60% / +20.60% / +32.50% / +32.48% | +15.837% / +0.562% / -5.025% / -38.000% / +66.603% / +20.596% / +32.501% / +32.481% | RF L468-L512 | PASS |
| EBIT (operating) | 5,807.74 vs 5,714.64 (+1.63%) | identical, +1.629% | derived | PASS |
| PBT change | 1,304.95 | 7,641.06 - 6,336.11 = 1,304.95 | RF L486 | PASS |
| Bridge: EBITDA + D&A + FC + OI | 38.24 + 54.86 + 289.87 + 921.98 = 1,304.95 | identical | RF L469, L483, L484 | PASS |
| Revenue / margin contribution split | +1,077.99 / -1,039.75 | +1,077.92 / -1,039.67 (sum 38.25) | RF L468 | PASS (rounding, S4) |
| Tax change | -76.89 = -339.63 + 262.74 | -76.89 = -339.63 + 262.72 | RF L492 | PASS |
| JV / NCI / owners PAT change | +43.08 / +4.87 / +1,276.01 | identical | RF L494, L497, L496 | PASS |
| OI share of PBT gain | 70.7% | 70.65% | derived | PASS |
| Finance-cost share of core PBT gain | 75.7% | 289.87 / 382.97 = 75.69% | derived | PASS (attribution issue is F2, not arithmetic) |
| OI-reverted owners PAT | 4,375.74 (+11.45%) | 4,375.74 at ETR 26.03%; 4,376.0 (+11.46%) at unrounded ETR | RF L486-L497 | PASS (rounding) |
| Standalone op EBITDA Q2 FY27 / Q2 FY26 / Q1 FY27 | 2,391.35 / 2,319.76 / 1,914.60 | identical | RF L918, L932-L935 | PASS |
| Standalone op margin Q2 FY27 / Q2 FY26 / FY26 | 5.49% / 6.61% / 8.18% | 5.487% / 6.606% / 8.176%; filed row matches | RF L1060 | PASS |
| Standalone YoY: revenue / EBITDA / OI / core PBT / PBT pre-exc | +24.11% / +3.09% / +130.87% / +12.04% / +64.51% | identical | RF L916-L935 | PASS |
| Standalone ETR on pre-exc PBT Q2 FY27 / Q1 FY27 | 15.7% / 14.0% | 15.74% / 13.99% | RF L935, L942 | PASS |
| S-vs-C gap Q2 / Q1 / H1 / FY26 | 1,831.98 (+54.4%) / (332.41) (-7.5%) / 1,499.57 (+19.2%) / 9,796.86 (+155.8%) | identical | RF L496, L615 | PASS |
| S-vs-C swing Q1 to Q2 | 61.9 pp | 54.36 + 7.46 = 61.82 pp | RF L496, L615 | PASS (rounding, S4) |
| Subsidiary revenue / EBITDA | 35,166.36 (+7.0%) / 4,453.30 (-0.7%) | identical (+6.99% / -0.74%) | RF L468, L916 | PASS |
| Segment PBIT margins Q2 FY27 (I&U, E-Conv, E-Green, M&P, four core, TPS, FS, Realty) | 4.48, 6.70, 5.82, 13.15, 6.07, 16.35, 24.85, 24.59% | 4.478, 6.696, 5.818, 13.153, 6.072, 16.350, 24.849, 24.587% | RF L795-L813 | PASS |
| Segment PBIT YoY total / four core | +13.1% / +17.9% | +13.08% / +17.93% | RF L807-L815 | PASS |
| Segment-to-EBITDA residual Q2 FY27 / Q2 FY26 | 1,594.16 / 819.04 | 7,423.25 + 1,036.91 - 21.35 - 6,844.65 = 1,594.16; LY 819.04 | RF L815-L818 | PASS |
| Deck segment EBITDA gap | 1,650.35 / 875.59 | identical | PF L970 | PASS |
| Segment YoY (inflow, revenue) all rows | e.g. I&U -12.9% / +6.0%; E-Conv +104.5% / +28.5% | identical | RF L387-L395 | PASS |
| Book-to-bill Q2 / H1 / PPM Q2 / PPM H1 | 1.88x / 1.74x / 2.16x / 2.03x | 1.875 / 1.743 / 2.162 / 2.030 | RF L395, L409; PF L974 | PASS |
| Order book / TTM revenue | 2.84 years | 853,514 / 300,903.59 = 2.837 | RF L158, L468 | PASS |
| Inflow ex E-Conv | -10.6% | 69,252 / 77,435 = -10.57% | RF L388, L395 | PASS |
| Order book YoY by segment | +16.0 / +36.3 / +62.3 / -2.8 / +28.0% | identical | PF L974 | PASS |
| CFO / capex / FCF H1 FY27 | 5,750.53 / 2,563.06 / 3,187.47 | identical | RF L732, L734 | PASS |
| CF working-capital change | +9,058.76 vs +1,356.58 | identical | RF L725-L727 | PASS |
| Receivable / inventory / payable days; CCC | 70.0 / 14.0 / 86.5; -2.5 (Mar 77.2 / 12.2 / 88.7; 0.7) | 70.01 / 14.01 / 86.52; -2.50 (77.20 / 12.17 / 88.68; 0.69) | RF L549, L552, L585-L586 | PASS |
| Derived NWC Sep-26 / Mar-26 | (2,139.09) / 5,978.22 | identical | RF L549-L588 | PASS |
| Gross borrowings / cash + CI + OBB / net debt | 136,227.05 / 97,434.76 / 38,792.29 | identical | RF L551-L554, L572, L581-L582 | PASS |
| Net cash ex FS | 55,100 / 70,900 | 804 - 134 - 119 = 551; 974 - 135 - 130 = 709 bn | PF L646-L650, L967 | PASS ("L&T Finance 134/135" is LTF cash, PF L648) |
| CFO ex FS / owners PAT H1 FY26 / H1 FY27 | 1.40 / 1.93 | 1.401 / 1.929 | PF L969; RF L496 | PASS |
| Standalone CFO/PAT; CFO/(PAT - dividends); FCF | 0.97; 1.75; 6,303.64 | 0.973; 1.751; 6,303.64 | RF L943, L1124, L1126, L1143 | PASS |
| Standalone receivable days | 93.3 vs 107.7 | 93.26 vs 107.66 | RF L1001 | PASS |
| Auditor scope Q2 PAT outside principal review | 3,403.82 (57.2%); management-furnished 252.71 (4.2%) | 37.22 + 3,089.63 + 24.26 + 238.81 + 14.77 - 0.87 = 3,403.82; 238.81 + 14.77 - 0.87 = 252.71 | RF L1334, L1348, L1352, L1366, L1370, L1392 | PASS |
| Guidance: H2 inflow implied | -0.8% to +3.0% (group); -3.5% to +0.4% (PPM) | 223,471-232,183 vs 225,353; 172,959-179,962 vs 179,212 | PF L975; RF L409 | PASS |
| Guidance: H2 revenue needed | +8.8% to +12.5% | +8.79% to +12.50% | RF L468 | PASS |
| Guidance: H2 PPM margin needed | 8.47% vs H2 FY26 8.26% | 10,615 / 125,286 = 8.473%; 9,349 / 113,201 = 8.259% | PF L971, L976 | PASS |
| FY27E revenue / H2 | 317,320.54 / 170,628.86 (+10.6%) | identical | RF L468 | PASS |
| FY27E owners PAT A / B | 20,008.79 / 21,209.91 | identical | RF L469, L483-L497 | PASS |
| FY28E owners PAT A / B | 21,747.89 / 24,257.38 | A identical; B 24,251.2 with unrounded FY26 margin 10.197% | RF L636 | PASS (rounding, S4) |
| EPS and PE (FY27E A, B; FY28E A, B; TTM) | 145.42 (26.1x), 154.15 (24.7x), 158.06 (24.0x), 176.30 (21.6x), 129.85 (29.3x) | identical | RF L509, L512 | PASS |
| Sensitivities | Rs 0.77 EPS per 10 bps; Rs 4.52 EPS per Rs 1,000 cr OI | 0.771; 4.518 | derived | PASS |
| One-time upper bound | 611.76 (3.1%); Q2 669.99 (12.9%) | identical | RF L491, L720 | PASS |
| A4 resolutions P-19 / P-22 / C-19 | 76.1% and 93.9%; 6,605.17 vs 6,607.92 and 2,433.99 vs 2,433.62; I&U Q1 5.10% | identical | PF L959-L960; RF L734-L735, L760-L763; PF L970-L971 | PASS |
| Concall structure | 67.2 min; Q&A 37.5 min (55.8%); hedge count 18; specificity 27/72 | 4,031 s = 67.18 min; 55.8%; 18; 0.375 | CC L21, L36, L340, L841 | PASS |

arithmetic_mismatches: none above rounding.

---

## 3. ADVERSARIAL READ

The review leans bearish on profit quality. Its three most positive claims are on the order book and on cash. Each counter below comes from the same extracted text. All three survive and none is in the review today, so each must be grafted before save.

### Claim 1. Order book and visibility (review L441 "GREEN"; L1035 FY28E revenue +12% on "backlog building"; L167 RF "multi-year revenue visibility")
A4 reads 853,514 (+28%), 2.84 years of TTM revenue and book-to-bill 1.88x as GREEN, and grounds FY28E revenue growth of 12% on the backlog.
Strongest bear counter:
- 131,542 of the 186,467 YoY rise in the book (70.5%) sits in Energy-Conventional (+76,437) and Energy-Green (+55,105) (PF L974).
- International book +41.5% (3,268 to 4,623 bn) against domestic +15.0% (3,402 to 3,912 bn) (PF L954). The Middle East is 73% of the international book (CC L148).
- The Energy-Green book of Rs 1,436 bn is 49% solar (Rs 703 bn) (CC L257-L258). Management says renewables carry "a significant impact" from logistics (CC L668), expects "some deferment of revenue" and "could be some shortfall" (CC L417-L419).
- The hydrocarbon book (Rs 2.13 trn, CC L231) includes Oman yard output that "has to cross" Hormuz, with "some delay" possible (CC L697-L707).
Survives: YES. The book's growth sits in the segments and region where the call names the execution risk. A4 carries Middle East concentration for inflow (L440) but leaves the book GREEN and the FY28E basis unqualified.
Graft (A4): add the composition line to watch item 2 and to the E5 revenue basis. Type MISSING.

### Claim 2. Cash strength (review L1096 "Cash looks strong"; L332 CFO ex FS +70.2%; L334 CFO ex FS / owners PAT 1.93 "High"; L352 net cash ex FS +15,800 "Up"; L941 "supports an order-book and cash-flow story")
Strongest bear counter (deck memorandum cash flow excluding FS, PF L969):
- Ex-FS cash from operations before working capital fell. H1: 179.9 - 87.2 = 92.7 bn vs 105.7 - 9.5 = 96.2 bn (-3.6%). Q2: 128.4 - 82.9 = 45.5 bn vs 47.6 + 1.6 = 49.2 bn (-7.5%).
- Ex-FS operating profit was 119.7 bn vs 120.7 bn in H1 (-0.8%).
- The ex-FS working-capital release (87.2 bn) plus net long-term investment and business disposals (33.8 bn, which include the Nabha exit; filed consideration 3,830.99 + 493.00, RF L745-L746) total 121.0 bn. That is about 77% of the 158 bn net-cash build A4 derives (PF L646-L650, L967).
Survives: YES. The whole rise in ex-FS CFO is working capital. Most of the net-cash build is advances plus one-off disposal proceeds. A4 flags "advance-assisted" and INDETERMINATE-WITH-DIRECTION, but it does not show that pre-working-capital cash fell or that disposals funded the cash pile.
Graft (A4): add both numbers to 5A or 5C and qualify brief L1096. Type MISSING. The INDETERMINATE-WITH-DIRECTION classification stands; the evidence for it gets stronger.

### Claim 3. Structural working-capital evidence (review L339 receivable days 77.2 to 70.0 "Better"; L379 "receivable days fell 7.2 days (filed)" as evidence for a structural shift)
Strongest bear counter:
- Trade receivables fell 2,742.30 (RF L552), but other current assets rose 9,551.28 (RF L558).
- The filed cash flow shows "(Increase)/decrease in trade and other receivables (7,761.39)" for H1 (RF L725). The receivable bucket consumed cash.
- Trade receivables plus other current assets: 151,764.44 to 158,573.42. On A4's revenue basis that is 193.8 days to 192.4 days, a 1.4-day fall, not 7.2.
Survives: YES. Most of the trade-receivable fall moved into other current assets. A4's derived NWC (L345) already nets OCA, so the NWC number is right. The 5C list still cites the 7.2-day fall as filed-tier structural evidence without the offset.
Graft (A4): add the offset to the 5C evidence list. Type MISSING.

### Mandatory acquisition-economics probe
- Acquisition described: International Green Scapes Limited, "Acquired on April 13, 2026" (RF L1578, L1664). H1 cash flow: "Consideration paid on acquisition of Subsidiaries (including contingent consideration) (805.30)" (RF L748). This line may also hold earn-outs on earlier deals, so the IGSL price is ND.
- Multiple: ~Rs 805.30 cr consideration (upper bound, all subsidiaries) / target PAT ND = multiple NOT COMPUTABLE. ROCE, debt, cash and customer tenure of the target: ND.
- Stake buy: "Payment made for acquisition of additional stake in a subsidiary from non-controlling interest (698.99)" (RF L757). Subsidiary, stake % and earnings: ND. Multiple NOT COMPUTABLE.
- Asset purchase: about USD 750 m for 10,000+ GPUs (CC L506-L508). Contracted revenue and take-or-pay share: ND (CC L83-L85 says only "a significant portion").
- No document in the corpus frames any of these as cheap or accretive. The bear reading is that Rs 1,504.29 cr of H1 acquisition spend has no disclosed price-to-earnings basis. A4 already carries it as Step 8.5 Q20 and Q18 (review L531, L529) and as AMBER silence (L784). No graft needed.

---

## FINDINGS REGISTER (each tagged; loop agent named)

| ID | Type | Where in review | Finding | Evidence | Loop |
|---|---|---|---|---|---|
| F1 | CONTRADICTION | L444 (watch item 5) | "core share of segment results slipped 2 pp" sits next to "four core 48.2%". The four-core share ROSE from 46.26% (3,036.48 / 6,564.61) to 48.24% (3,580.92 / 7,423.25). The 2 pp loss is Realty + DP, which fell from 5.07% to 1.09% of segment results. A4's own Step 1C table (L215, L220: four core +17.9% vs total +13.1%) implies the rise. | RF L807-L815 | A4 |
| F2 | MISSING | L239, L301, L937, L1094 | The finance-cost fall is attributed wholly to the LTMRHL perimeter ("Lower interest cost from the Hyderabad Metro exit gave 22%"; "Perimeter (LTMRHL)... permanent after close"). The deck names two causes: "non-consolidation of Hyderabad Metro and decrease in Standalone debt" (PF L220-L222; presentation R1439). A4 quotes only the first (L848). Filed standalone finance cost fell 70.93 (476.23 to 405.30, RF L932), 24.5% of the 289.87 consolidated fall, and LTMRHL cannot sit in the standalone. At most 218.94 (16.8% of the PBT gain) is non-standalone, not 22%. Standalone gross borrowings rose 3,010.48 in H1 (RF L1018, L1026-L1027), so the standalone saving can reverse. | PF L220-L222; RF L483, L932 | A4 |
| F3 | CONTRADICTION | L1128 (competition brief) | "Management says it will not bid without a 'differentiated margin'. [ASR-MGMT]". A1 structured R412 records CC L623 as "Analyst: will not bid if do not get differentiated margin". The second-person wording ("You will not bid...") and the analyst's next line "Sir, and the second question..." (CC L624) support A1. No management reply follows. A4 applied this attribution test to CC L367-L369 and L596-L599 (L860) but not here. | CC L623-L624; A1 R412 | A4 |
| F4 | MISSING | L441, L1035 | Surviving bear counter 1 (book composition) not in review. | PF L954, L974; CC L148, L257-L258, L417-L419, L668, L697-L707 | A4 |
| F5 | MISSING | L332-L352, L379, L1096 | Surviving bear counter 2 (pre-WC ex-FS cash down; disposals and advances built the net cash) not in review. | PF L969, L646-L650, L967; RF L745-L746 | A4 |
| F6 | MISSING | L339, L379 | Surviving bear counter 3 (receivable-days fall offset by OCA build; CF receivables outflow) not in review. | RF L552, L558, L725 | A4 |
| F7 | FACTUAL | L984 (Section D), L1139 (forward map) | "At the band, it adds Rs 5,000-10,000 crore gross, before the partner share." The release gives the "Major" band (Rs 5,000 to 10,000 cr) but does not say whether it is gross package value or L&T's share (OP L75, L124-L126). The basis is ND. The forward-map bear fork "the partner share leaves little for L&T" rests on the unsupported basis. | OP L104-L110, L124-L126 | A4 |

None of F1-F7 changes A4's protocol verdict (PROCEED WITH FLAGS) or the cash classification (INDETERMINATE-WITH-DIRECTION). Each changes a stated fact, attribution or qualifier. Under the tagging rule, none is STYLE.

---

## VERDICT (LOOP 0)

VERDICT: INCOMPLETE. Failing agent: A4. Gap: F1 (CONTRADICTION, watch item 5 rationale), F2 (MISSING, dropped "decrease in Standalone debt" qualifier and the 70.93 standalone finance-cost fall), F3 (CONTRADICTION, CC L623 attribution vs A1 R412), F4-F6 (MISSING, three surviving bear counters to graft), F7 (FACTUAL, Dhaka band basis stated without support). No A2 re-enumeration and no A3 re-run is needed: coverage and arithmetic pass.

Fix list for A4 (edits only, no re-derivation of the review):
1. L444: restate the watch item 5 rationale. The four-core share rose 2.0 pp. The fall is Realty and DP. Re-judge the AMBER on the remaining grounds (no core PAT disclosure, L890).
2. L239, L301, L937, L1094: split the 289.87 finance-cost fall into standalone 70.93 (RF L932) and the non-standalone remainder 218.94. Quote PF L220-L222 in full at L848. Change "gave 22%" to "up to about 17%, with about 5% from lower standalone finance cost".
3. L1128: relabel as an analyst statement with no management reply (CC L623-L624), or drop it.
4. L441 and L1035: add the book-composition counter.
5. L332-L352, L379 and L1096: add the pre-WC ex-FS cash decline and the share of the net-cash build from WC release plus disposals.
6. L379: add the OCA offset to the receivable-days evidence.
7. L984 and L1139: state the band basis as ND and rewrite the bear fork.

---

## STYLE NOTES (LOOP 0; logged, no loop)

- S1 (L1090): "Orders in all other segments fell 10.6%" reads as if each segment fell. M&P (+34.3%), TPS (+11.5%) and FS (+27.4%) rose (RF L390-L392). Say "together".
- S2 (L1097): "Customer advances on new large orders explain much of that" is tagged ASR-MGMT. Management named advances as one of two drivers (CC L184-L186) and stressed frequent billing milestones (CC L572-L573). "Much" is A4's reading; tag it INFERENCE.
- S3 (L87): the 57.2% auditor-scope share compares subsidiary PAT "before consolidation adjustments" (RF L1346, L1364) with consolidated PAT. Add the qualifier.
- S4 rounding drifts: S-vs-C swing 61.9 pp vs 61.82 pp (L396); "H1 ran 20 bps below the prior-year H1" vs 25 bps unrounded (6.99% vs 7.25%, PF L971) (L675); contribution split 1,077.99 / -1,039.75 vs 1,077.92 / -1,039.67 (L298-L299); FY28E Reading B uses the rounded 10.20% margin (36,250.70 vs 36,240.75 unrounded; owners PAT 24,257.38 vs 24,251.2) (L1036-L1044).
- S5 (L285): "Q2 FY27 is the highest filed quarter". Q3 and Q4 FY26 are ND individually, and the H2 FY26 average is 77,105.96, so one of them may exceed 78,749.94. Say "highest quarter in this corpus".
- S6 (L653, L831): quote CC L173-L176 in full, including "coupled with higher treasury income". The contradiction call stands on "primarily", but the reader should see both named drivers. Claim #24 (L624) already carries the full text.
- S7 (L19-L24): coverage rests on a blanket "all reviewed" declaration. List the reviewed-no-finding ID ranges per ledger section so the next A5 can diff mechanically.
- S8: the deck restates M&P and Energy-Conventional comparatives for the MRU move (PF L389). Name it beside the segment YoY table (L183-L194) and Q11 (L522).

Loop 0 block (superseded by the RE-AUDIT LOOP 1 block at the end of this file; kept for the record, not for parsing):

```text
stage: A5-adversary
company: "LT"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
verdict: INCOMPLETE
plain_language_brief: {narrative: present, sector: present, business_model: present, competition: present, forward_map: present}
coverage: {orphan_rows: [], missing_from_ledger: []}
arithmetic_mismatches: []
surviving_bear_counters: 3 (order-book composition; ex-FS pre-WC cash and disposal-funded net cash; receivable-days offset by OCA), all type MISSING
findings_by_type: factual [F7]; missing [F2, F4, F5, F6]; contradiction [F1, F3]; style [S1-S8]
loop_back_to: "A4"
gap: "A4 edits only: F1 watch item 5 rationale; F2 finance-cost split 70.93 / 218.94 and full PF L220-L222 quote; F3 CC L623 analyst attribution per A1 R412; F4-F6 graft three surviving bear counters; F7 Dhaka band basis ND. Coverage and arithmetic pass; no A2 or A3 re-run."
```

---

# RE-AUDIT LOOP 1 (2026-10-29)

Scope: one re-audit of the rewritten review (1,287 lines; A4 "CORRECTION LOOP 1" log at review L5-L14) against the same A1 fulltexts, A1 structured files and A2 ledgers. Not opened: the source PDFs and anything under runs/lt-q2fy27/inputs/. Line numbers in this section are loop-1 review lines.

## R0. DELIVERABLE-COMPLETENESS AUDIT (re-run)

DELIVERABLE-COMPLETENESS: narrative PRESENT | sector PRESENT | business_model PRESENT | competition PRESENT | forward_map PRESENT. Gate PASSES.

| Part | Heading (review line) | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | L1116 | 16 bullet lines (L1117-L1132), inside the 10-20 line band; F2, F5 and S1, S2 edits present | present |
| 2. Sector intelligence | L1134 | 8 bullets, unchanged | present |
| 3. Business-model intelligence | L1144 | 8 bullets, unchanged | present |
| 4. Competition intelligence | L1154 | 10 bullets; the CC L623 line now reads as an analyst statement (L1158) | present |
| 5. Forward map | L1166 | 11 catalysts, each with a bull and a bear fork; Dhaka fork (L1169) and NWC / operating-cash fork (L1171) rewritten | present |

## R1. CLOSURE OF LOOP-0 FINDINGS

| ID | Type | Patched at (loop-1 lines) | My check against the extract | Status |
|---|---|---|---|---|
| F1 | CONTRADICTION | L244 (shares line), L472 (watch item 5), L918 (8B item 5) | Four core 46.26% to 48.24%; TPS + FS 48.67% to 50.67%; Realty + DP 5.07% to 1.09% (RF L807-L815). The AMBER now rests on the missing core PAT disclosure (CC L296-L302). | CLOSED |
| F2 | MISSING | L50, L75, L100, L262, L278, L288, L324-L325, L334, L337, L339, L496, L554, L876, L965, L1045, L1107, L1123, L1220, L1269, L1285 | Split 218.94 / 70.93 ties: 762.81 - 476.23 = 286.58 and 472.94 - 405.30 = 67.64 (RF L483, L932). 218.94 / 1,304.95 = 16.78%; 70.93 / 1,304.95 = 5.44%; 218.94 / 382.97 = 57.17%; 70.93 / 382.97 = 18.52%. The bridge check at L334 sums to 1,304.95. Deck remark quoted in full at L262, L339 and L876 (PF L220-L222; R1439). | CLOSED. The L876 patch adds a new error (N1). |
| F3 | CONTRADICTION | L730, L888, L1158 | Matches A1 R412 and CC L623-L624. | CLOSED |
| F4 | MISSING | L224, L469, L507, L915, L966, L1063, L1275 | 131,542 / 186,467 = 70.5% (PF L974); +41.5% / +15.0% (PF L954); 703 / 1,436 = 49% (CC L257-L258). | CLOSED |
| F5 | MISSING | L356-L358, L380, L406, L765, L861, L966, L969, L989, L1125-L1126, L1171, L1273 | 9,620 to 9,270 (-3.6%); 4,920 to 4,550 (-7.5%); 12,070 to 11,970 (-0.8%); 8,720 + 3,380 = 12,100 = 76.6% of 15,800 (PF L969, L646-L650, L967). | CLOSED |
| F6 | MISSING | L365-L366, L407, L965, L1273 | 151,764.44 to 158,573.42; 193.8 to 192.4 days; CF (7,761.39) (RF L552, L558, L725). | CLOSED |
| F7 | FACTUAL | L572 (Q33), L984, L1011-L1012, L1114, L1169, L1238, L1243, L1281 | The band basis is stated as ND, which matches OP L124-L126. The bear fork no longer assumes a gross basis. | CLOSED |

Style notes S1-S8: all applied. S1 at L1118. S2 at L1127. S3 at L105. S4 at L334, L424, L703 and L1064. S5 at L308. S6 at L653, L681 and L859. S7 at L38-L41: the listed ranges resolve to the right rows (R236-R239 FS NIM + fees; R624-R635 DSCR / ISCR; R1940-R2119 Annexure A; presentation R1385 and R1487 disclaimer). S8 at L201 and L550, supported by PF L387 and L389.

## R2. DRIFT CHECK OUTSIDE THE PATCHED POINTS

- Headline tables: every cell is unchanged from loop 0, so the loop-0 Audit 2 recomputations stand. Covered: Step 1A (L118-L148), consolidated derived (L152-L161), Step 1B (L167-L185), standalone derived (L189-L195), the Step 1C segment table (L203-L214) and the PBIT table (L230-L242).
- Step 2A and 2B: numbers unchanged. Only the finance-cost verdict cells changed (L262, L278), plus the PAT verdict wording (L267).
- Step 4 bridge: the finance-cost row is split in two (L324-L325). The total (1,304.95) and the owners-PAT change (1,276.01) are unchanged.
- Step 5A: the existing rows are unchanged. The four added rows (L357, L358, L366, L380) recompute.
- Step 5D: the swing now reads 61.8 pp (S4). The other cells are unchanged.
- INDICATIVE FY27E / FY28E (Section E, L1016-L1108): every number is unchanged. Checked: 317,320.54; 170,628.86; 15,801.26 / 17,733.29; 945.88; 2,073.82; 4,350.06; 17,131.62 / 19,063.65; 10,683.84 / 11,884.96; 20,008.79 / 21,209.91; 355,399.00; 32,214.08 / 36,250.70; 34,874.80 / 38,911.42; 21,747.89 / 24,257.38; EPS 145.42 / 154.15 / 158.06 / 176.30; PE 26.1x / 24.7x / 24.0x / 21.6x. The one added E8 sensitivity (about 71 cr pre-tax a quarter) equals the Q2 YoY standalone saving of 70.93 (RF L932).
- Questions for Management (L538-L574): 35 rows, same order, same finding IDs. Only Q11, Q15 and Q33 changed, as F2, F7 and S8 required. The YAML questions are aligned (L1205-L1240).
- Forward map: 11 catalysts. Only the two patched forks changed.
- Monitorables (L981-L1006): 24 rows; items 2 and 7 extended.
- Verdict and classification: PROCEED WITH FLAGS (L973) and INDETERMINATE-WITH-DIRECTION (L407, L411) unchanged.
- Coverage: no ledger count changed. orphan_rows = [] and missing_from_ledger = [] stand.

## R3. NEW FINDINGS (loop 1)

| ID | Type | Where | Finding | Evidence | Loop |
|---|---|---|---|---|---|
| N1 | FACTUAL | L876 (Step 7A finance-cost row; introduced by the F2 patch) | The cell says the standalone saving "is rate or timing, not a lower balance at Sep-26", and that "decrease in Standalone debt" is "not visible in the Sep-26 balance". The filed standalone ratios show the opposite. Debt-equity is 0.26 at Sep-25, 0.23 at Jun-26 and 0.19 at Sep-26 (RF L1051, columns per L1049-L1050). Total debt to total assets is 0.10, 0.08 and 0.07 (RF L1058). Applied to total assets of 183,090.62 at Sep-25 (RF L1222), even the bottom of the 0.10 rounding band (0.095) gives Sep-25 borrowings of at least about 17,390. The equity route gives the same answer: 0.255 x net worth 66,577.13 (RF L1064) is at least about 16,980. Sep-26 borrowings are 14,783.81 (RF L1018, L1026-L1027). Standalone debt is therefore lower than a year ago (by roughly 2,600 or more) and lower than at Jun-26 (0.075 x 216,000.96 is about 16,200 or more). It is higher only against Mar-26 (11,773.33). Both deck causes are visible in the filing. | RF L1018, L1026-L1027, L1049-L1051, L1058, L1064, L1222; PF L220-L222 | A4 |
| N2 | STYLE | L969 (Section C) | "The cash story rests on advances and disposal proceeds rather than operating cash" overstates. Ex-FS operating cash before working capital was still 92.7 bn in H1 (PF L969). It is the rise in cash and most of the net-cash build that rest on advances and disposals. Suggested: "The rise in cash rests mostly on advances and disposal proceeds; operating cash before working capital fell 3.6%." | PF L969 | none |
| N3 | STYLE | L380 (Step 5A sources row) | "incl Nabha and SWC proceeds" names entities that the CF lines do not name (RF L745-L746). Tag it INFERENCE. My loop-0 Claim 2 text made the same untagged Nabha link. | RF L745-L746; PF L231-L233 | none |

Self-correction on F2. My loop-0 F2 text compared standalone borrowings only with Mar-26 ("+3,010.48 in H1, so that part may reverse"). It omitted the year-on-year ratio evidence above. A4's "reversible" hedges at L325, L337, L496, L1107, L1123, L1269 and L1285 rest on that wording. They are hedges, not false statements, so they do not loop on their own. The N1 fix should still align them.

Fix for N1 (A4, text only; no number in Section E changes):
1. L876 reconciliation cell. Suggested text: "Standalone finance cost -70.93 (RF L932). Standalone borrowings are lower than a year ago and than at Jun-26 (filed D/E 0.26 to 0.23 to 0.19; debt to total assets 0.10 to 0.08 to 0.07; RF L1051, L1058). They are 3,010.48 above Mar-26 (RF L1018, L1026-L1027). Both deck causes are visible. 'Non-consolidation' vs 'Held for Sale' wording still unclear (P-24)." Status: PARTIALLY CONFIRMED on accounting wording only.
2. L325, L337, L496, L1107, L1123, L1269, L1285: replace the bare "reversible" with "backed by lower debt year on year; narrows if borrowings keep rising from the Mar-26 level".

## R4. VERDICT (LOOP 1)

VERDICT: INCOMPLETE. Failing agent: A4. Gap: N1 (FACTUAL). The Step 7A finance-cost cell (L876) states that the deck's "decrease in Standalone debt" is not visible and that the saving is not a lower balance. The filed standalone ratios (RF L1051, L1058, L1222) show standalone debt lower year on year and quarter on quarter. All seven loop-0 findings (F1-F7) are closed, and all eight style notes are applied. Audit 0 passes. Coverage and arithmetic pass. Nothing drifted outside the patched points. N1 changes no number, no verdict and no classification. The fix is one cell plus aligned hedge wording. Loop 1 was the only permitted iteration, so the orchestrator decides how to carry N1.

## R5. STYLE NOTES (LOOP 1; logged, no loop)

- N2 (L969): reword the Section C cash line as above.
- N3 (L380): tag the Nabha and SWC naming as INFERENCE.

```yaml
stage: A5-adversary
company: "LT"
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
surviving_bear_counters: []   # loop-0 counters 1-3 grafted at review L469/L1063, L357-L358/L380/L1126, L366/L407; none open
findings_by_type:
  factual:
    - "N1 review L876 (Step 7A finance-cost row, added by the F2 patch): says the standalone saving is 'not a lower balance at Sep-26' and that 'decrease in Standalone debt' is 'not visible'; filed standalone D/E 0.26 (Sep-25) to 0.23 (Jun-26) to 0.19 (Sep-26) (RF L1051) and debt to total assets 0.10 to 0.08 to 0.07 (RF L1058) with Sep-25 total assets 183,090.62 (RF L1222) imply Sep-25 borrowings of at least about 17,390 vs 14,783.81 at Sep-26 (RF L1018, L1026-L1027); debt is lower YoY and QoQ and higher only vs Mar-26 (11,773.33)"
  missing: []
  contradiction: []
  style:
    - "N2 review L969 Section C 'cash story rests on advances and disposal proceeds rather than operating cash' overstates; ex-FS pre-WC CFO was 92.7 bn in H1 (PF L969); say the rise in cash rests mostly on advances and disposals"
    - "N3 review L380 'incl Nabha and SWC proceeds' names entities the CF lines do not name (RF L745-L746); tag INFERENCE"
loop_back_to: "A4"
gap: "N1 (FACTUAL): rewrite the Step 7A finance-cost cell at review L876; standalone borrowings are lower YoY and QoQ per filed ratios (RF L1051, L1058, L1222) and up 3,010.48 only vs Mar-26, so both deck causes are visible; align the bare 'reversible' hedges at L325, L337, L496, L1107, L1123, L1269, L1285. Text only; no Section E number, verdict or classification changes. F1-F7 closed; S1-S8 applied; Audit 0, coverage and arithmetic pass."
style_notes:
  - "N2 reword Section C cash line (L969)"
  - "N3 tag Nabha/SWC naming as INFERENCE (L380)"
analyst_note: "Loop 1 re-audit. All seven loop-0 findings are closed and all eight style notes are applied. The brief passes. Headline tables, every Section E number, the 35-row question table and the 11-fork forward map are unchanged outside the patched rows. One new FACTUAL error came in with the F2 patch. The Step 7A finance-cost cell says the standalone saving is not a lower balance and that the deck's 'decrease in Standalone debt' is not visible. The filed standalone ratios show the opposite: D/E fell from 0.26 to 0.19 and debt to total assets from 0.10 to 0.07 year on year. That puts Sep-25 borrowings at about 17,390 or more against 14,783.81 at Sep-26. Debt rose only against Mar-26. My loop-0 F2 text compared only with Mar-26, and the review's 'reversible' hedges rest on it, so the fix should add the year-on-year context. The fix is one cell plus wording. The verdict, the cash class and every Section E number stand. Loop 1 was the only permitted iteration, so the orchestrator decides how to carry N1."
```
