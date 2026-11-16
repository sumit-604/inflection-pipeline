# ACCORD — Accord Transformer & Switchgear Ltd
Run folders read: runs/accord-2026-10-06 (origin/run/accord-2026-10-06)
Company file: companies/ACCORD.md (origin/run/accord-2026-10-06)

## Our base case
"Base basis: ORDER-BOOK for FY27, then the Amendment 14 fade."
Source: origin/run/accord-2026-10-06:runs/accord-2026-10-06/forward_module.md §D1 L182-184
"FY27 = H1 Rs 52.68 Cr [H1upd p.2] + H2 Rs 53.80 Cr (filed orders with H2 windows, Section C1) = Rs 106.48 Cr [calc]."
Source: same file §D1 L185
"| Base margin FY27 | 13.17% [calc] | | |"
Source: same file §D2 L211
"| Revenue | 95.03 | 101.60 | 106.48 | 114.57 | 126.60 | 135.24 | D1 |" (cols Bear FY27, Bear FY28, Base FY27, Base FY28, Bull FY27, Bull FY28)
Source: same file §D4 L240
"| Operating EBITDA ex OI | 8.42 | 9.00 | 14.02 | 15.04 | 20.04 | 21.28 | D2 |"
Source: same file §D4 L242
"| Core PAT (x 0.7483) | 5.36 | 5.79 | 9.58 | 10.23 | 14.08 | 14.90 | [calc] |"
Source: same file §D4 L248
"INFERENCE, the most evidenced range: H1 FY27 operating EBITDA Rs 6.1-7.5 Cr, a margin of 11.5% to 14.2%, centre about 13.1%. Core PAT Rs 4.1-5.2 Cr."
Source: same file §B3 L126
Header: "Written 2026-10-06." ; "PROVISIONAL FORWARD MODULE, operator request 2026-10-06. Pre-signature: the Mental Model is UNSIGNED and Halt 1 is open."
Source: same file L1, L5

## Management guidance and promised catalysts
| G1 | FY27 revenue | Rs 120-180 Cr | FY27 | Nitin, Tr. p6, L262-264 | VIEW |
| G2 | Revenue growth, current year | 60-80% (stated "due to the deferment") | FY27 | Nitin, Tr. p6, L250-259 | VIEW |
| G4 | EBITDA margin | 13-15% ("trying to maintain") | 2-3 years (question frame) | Nitin, Tr. p11, L435-439, L479 | VIEW |
| G5 | PAT margin | 9-11%, ~10% average | 2-3 years | Nitin, Tr. p11, L479-480 | VIEW |
Source: origin/run/accord-2026-10-06:runs/accord-2026-10-06/outputs/reports/05-concall.md §1B L48-52 (call of 2026-06-01)
Promises (promise_delivery YAML):
"promise: \"Land identified for expansion ~2.50 lakh sq ft\", outcome: \"delivered\", explanation: \"Land bought 3-Jul-26, 20,300 sq m ..."
"promise: \"FY27 revenue Rs 120-180 Cr\", outcome: \"partial\", explanation: \"H1 52.68; H2 needs 67.3-127.3; in progress, not scoreable\""
"promise: \"Expansion ground work in 2-3 months, manufacturing in 6 months minimum\", outcome: \"partial\", explanation: \"land and funding approval only; build 9-10 months from 26-Sep-26 per B03; slipping\""
"promise: \"NHEV work for 10-15 stations by FY27-end\", outcome: \"partial\" ..."
"promise: \"MVVNL ~Rs 125 Cr and Torrent ~Rs 100 Cr bids to open Jun/Jul\", outcome: \"missed\", explanation: \"no outcome reported by 5-Oct-26 ...\""
Source: same file L257-264
"Timeline slippages: expansion start (2-3 months from June means Aug-Sep 2026; only land bought 3-Jul and a building-funding approval 26-Sep)."
Source: same file L74

## Reported results (Q4 FY26 / Q1 FY27 / Q2 or H1 FY27)
Q4 FY26 (H2 FY26) and FY26:
"| Revenue | 27.72 | 42.35 | 70.07 | [Deck p.23]; [AR p.78]; [calc] |" (cols H1 FY26, H2 FY26, FY26)
"| Operating EBITDA ex other income | 2.25 (8.1%) | 4.70 (11.1%) | 6.95 (9.9%) | ..."
Source: forward_module.md §B1 L85, L90
"FY26 revenue Rs 70.07 Cr; FY25 Rs 79.02 Cr; PAT Rs 4.50 Cr | AR p.78; AR p.55"
Source: outputs/final/business-narrative.md L41
"FY26 called "steady growth and improved profitability" ... Filed: revenue minus 11.3%, PAT minus 24.2%, EBITDA margin 11.68% to 10.39%, H2 revenue minus 26.4%, H2 PAT minus 40.3%"
Source: outputs/final/verifier-summary.md L39
Q1 FY27: no result (half-yearly reporter). "Order book: ... Rs 159 Cr at 22-Jul-2026 [Q1 update p2]"
Source: step1-business-brief.md L10
Q2 / H1 FY27:
"H1 FY27 revenue Rs 52.68 Cr, +90.07% YoY ... Profit not disclosed; H1 audited results not yet filed. [BSE H1 FY27 business update, 2026-10-05, p2]"
Source: step1-business-brief.md L9
"Its figures are "management estimates and are subject to final audit adjustments" [H1upd p.3]."
Source: forward_module.md L21
All source prefixes: origin/run/accord-2026-10-06:runs/accord-2026-10-06/

## Management's stated reasons
"Why did revenue fall despite tailwinds (Khetan, Fenil) | customer site delay, oil | Partly: no customer name, no billing date | Yes. The Rs 31 Cr order is 44% of FY26 revenue (calc)"
Source: outputs/reports/05-concall.md L151
"transformer oil procurement "cut" (Tr. p10, L400-402) | external-blame"
Source: outputs/reports/05-concall.md L98

## Risk flags raised before the result, and any overruling
Q2 FY27 margin is untested; no shortfall recorded. Flags in file:
"R6: "we will not lose anything into the price variation" (Tr. L449 to 450) ... oil up 100% ... Status: PARTIALLY CAUGHT"
Source: outputs/final/verifier-summary.md L41 (Verifier B)
"Falsifier: below 10% with revenue up (dossier B6; B05 kill signal)." ; "Below 9.9% | THESIS BREAK."
Source: forward_module.md §I1 L493-505
No overruling found.

## Verdicts and dates
"PROCEED WITH CAVEATS" — Source: outputs/final/gate-recommendation.md L1
"Rule 3 fires. FLAG-CASH is active and the determination is INDETERMINATE." — L15
"Posture: not set." — L27
Company file: "Mental Model signed: NOT SIGNED"; "Halt 1 decision (KILL/SHALLOW/PROCEED): PENDING"; "Spear: OVERRIDE 2026-10-06" — companies/ACCORD.md L12, L21-22
Archetype: NOT FOUND in files read.

## Lessons archive mentions
"## 2026-10-06 ACCORD (/step1 intake + phase 1 + operator forward module)" ... "Verifier B acceptance 62.5% on 8 material items; overall confidence 62.5, set by redflag coverage." "Operator commissioned valuation (forward_module.md) on an unsigned model in the same session; recorded as ruling 1 for the operator."
Source: origin/run/accord-2026-10-06:LESSONS_ARCHIVE.md (export LESSONS_ARCHIVE_offmain_lines.md L392-403)
