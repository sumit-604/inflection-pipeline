# A5 ADVERSARY RE-AUDIT (MERGED REVIEW, LOOP 1): GRWRHITECH | q2fy27

Agent: A5 adversary / completeness auditor | Model: claude-opus-5-5 | Date: 2026-10-23
Review under audit: runs/grwrhitech-q2fy27/work/review_grwrhitech_q2fy27.md (1,291 lines; A4 merged_loop_iteration 1)
Prior merged audit: runs/grwrhitech-q2fy27/work/audit_grwrhitech_q2fy27_merged.md (non-STYLE findings F1, F2, M1, M2, M3, M4, C1; STYLE S1-S9)
Inputs read: the A4 review (in full); A1 fulltexts (results l.1-1149 in full plus targeted greps of l.1150-1492; concall L0001-L0842 in full); A1 structured extractions (concall R001-R419 in full; results by count and targeted grep); A2 ledgers (results, concall, in full); the prior merged A5 audit (for the finding list only). No source PDF, no audio, nothing under inputs/ opened. No A3 file opened.
Anchors: "rev l.N" = line N of the review as it stands now. "l.N" = line N of grwrhitech-results-q2fy27-fulltext.md. "L0nnn" = the 4-digit source prefix in grwrhitech-concall-q2fy27-fulltext.md. "R###" = A1 structured row. [DERIVED] = my arithmetic on the cited lines.

---

## PRIOR FINDINGS: RESOLUTION CHECK

| Prior finding | Type | Where A4 fixed it | Check | Status |
|---|---|---|---|---|
| F1 Step 8C Q3 thresholds misread, H2 averages applied to Q3 | FACTUAL | rev l.478-486 rebuilt Q3-to-Q3: comparator Q3 FY26 87 / 459 = 18.95% incl OI (l.1010, l.1021, l.1024); bull 22.7% = 18.95% + 376 bps H1 refund-stripped YoY gain; bear 18.95% = no YoY gain on the same basis. Old 22.3% / 19.5% lines gone (grep: no hit outside the legitimate H2 FY26 19.49% cell, rev l.258, l.263). Aligned at 5.5C (l.369), 8A-W (l.469), 8B(ii) (l.475), Step 9 payload (l.532), Role 5 8E (l.996), Section C (l.1041), Flag 20 (l.1067), M6 (l.1079), brief (l.1121, l.1150, l.1156), YAML (l.1248, l.1285, l.1287) | Bull: 369.72 / 1,328.61 = 27.828% less 256.25 / 1,064.68 = 24.068% = 3.760 pts; 18.95 + 3.76 = 22.71%. Alt 178.00 / 695.53 = 25.592% less 23.399% = 2.19 pts, 21.1%. Bear sentence now true: both sides incl OI, refund-free | RESOLVED. One new error sits in the added guide-check bullet (rev l.486): see NF1 |
| F2 Brief "parity or better on many products" | FACTUAL | Brief l.1136, l.1146; Step 7 l.454; 8D l.985; 5A l.818; 7B l.927; Section C l.1037 | Matches L0496-L0515: 30-40% before, 80-85% now (L0498, L0501), 85-90% "in some cases" (L0505), 10-20% higher on "certain products" (L0506-L0508), excludes China and Korea (L0502), "85-120%" summary (L0515, L0534) | RESOLVED |
| M1 Q3 FY26 ex-OI bound for tripwire 3 | MISSING | Step 3 table l.256, diagnostics l.267; 6C row 3 l.415; Role 5 8C row 3 l.975; Flag 20 l.1067 | 87 - 0.18 x 459 = 4.38; Q1 FY26 OI 27.24 - 13.86 = 13.38; H2 FY26 OI 64.84 - 27.24 = 37.60; Q4 would need 37.60 - 4.38 = 33.22; even split (87 - 18.80) / 459 = 14.86%; Q4 floor (157 - 37.60) / 597 = 20.0% (l.510-511, l.1010, l.1022-1024) | RESOLVED |
| M2 Refund-stripped two-year margin climb | MISSING | Step 2 answer 1 l.231; Flag 13 l.1060; YAML l.1278 | (380.72 - 11) / 1,328.61 = 27.83% vs 280 / 1,096 = 25.55%: +228 bps; 369.72 / 280 = +32.0%; 178.00 / 695.53 = 25.59% vs 24.2%: +139 bps; 178 / 150 = +18.7% | RESOLVED |
| M3 Inventory composition partly derivable | MISSING | Step 5 C row l.315, SA row l.334, note l.343, growth answer l.349, 7A row l.906 | C 460.99 - 389.25 = 71.74 (l.609, CF l.692); less FG/WIP/SIT 26.45 (l.518) = 45.29, 63.1%; SA 378.98 - 288.99 = 89.99 (l.247, CF l.316) less 44.37 (l.179) = 45.62; outside parent 26.45 - 44.37 = -17.92 vs 100.26 -> 82.01 = -18.25 (FX gap 0.33) | RESOLVED (its export-stock counterpart is NM1) |
| M4 Top three on the filed 34% | MISSING | Q1 row l.495; Exchange 2 l.785; Flag 8 l.1055; YAML l.1273 | 34 + 2 x 11.33 = 56.7; 34 + 2 x 17 = 68; call basis 30 + 2 x 10 to 30 + 2 x 15 = 50-60 (L0262-L0264) | RESOLVED |
| C1 "Waluj plant" in 5.5C | CONTRADICTION | 5.5C l.370 (site ND); Q8 bear l.502 | Grep of the results fulltext: Waluj appears only in the registered-office lines l.60, l.79, l.153, l.497. No plant site is named anywhere in the extract | RESOLVED |
| S1-S9 | STYLE | Logged by A4, not applied (rev l.13) | Allowed: STYLE never loops. All nine still stand at their lines (rev l.627, l.628 / l.638 / l.1093, l.561, l.90 / l.1108, l.191, l.295, l.572 / l.1027, l.560, l.19) | LOGGED, carried |

---

## AUDIT 0. DELIVERABLE-COMPLETENESS (hard gate)

| Brief part | Location | Status |
|---|---|---|
| (1) Summary narrative | rev l.1104-1121 (17 lines, inside the 10-20 band) | PRESENT |
| (2) Sector intelligence | rev l.1123-1130 (7 bullets) | PRESENT |
| (3) Business-model intelligence | rev l.1132-1141 (9 bullets) | PRESENT |
| (4) Competition intelligence | rev l.1143-1147 (4 bullets; pricing now as said) | PRESENT |
| (5) Forward map | rev l.1149-1160 (make-or-break line plus 10 dated catalysts, each with a Bull and a Bear fork) | PRESENT |

Gate: PASS.

---

## AUDIT 1. COVERAGE (fresh enumeration vs A2 ledgers)

Method. Results: I re-counted each category from the results fulltext and grepped the structured file by row type. Notes at l.357-367 and l.735-749. Auditor paragraphs at l.100-135 and l.390-480. Entities at l.424-427 and l.744-746. Agenda at l.40-49. Statement labels at l.170-224, l.236-288, l.298-355, l.509-585, l.597-651, l.665-733 and l.770-788. Every asterisk line in the deck (grep "\*": l.1114, l.1128, l.1137, l.1148-1173, l.1201, l.1276-1280, l.1443, l.1467, l.1470) maps to R1766-R1779. Concall: I read L0001-L0842 in full and swept every number-bearing line against the R001-R419 line anchors, allowing the 1-3 line drift A2 documents (ledger_concall l.21). I also grep-counted rows by type.

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Results: numbered notes | 7 | 7 (SA 1-3 l.358-367; C 1-4 l.736-749) | none | PASS |
| Results: unnumbered footnotes | 14 | 14 (p29 4, p31 2, p32 1, p35 4, p42 3; R1766-R1779) | none | PASS |
| Results: line items | 205 | 205 (SA P&L 24, SA BS 30, SA CF 38, C P&L 32, C BS 31, C CF 41, release table 9) | none | PASS |
| Results: zero-standing | 11 | 11 (SA HFS; C P&L OCI-reclass, its tax, 3 NCI lines; C HFS; C CF sale of investment, doubtful advances, net gain, FX effect) | none | PASS |
| Results: agenda items | 3 | 3 (item 1 l.40; release l.45; presentation l.48) | none | PASS |
| Results: auditor paragraphs | 13 | 13 (SA 4; C 1-7, SEBI-circular l.419, "not modified" l.480) | none | PASS |
| Results: entities | 4 distinct / 6 rows | 4 / 6 | none | PASS |
| Results: forward statements | 37 | 37 (grep FORWARD = 37; R1391-R1427 contiguous) | none | PASS |
| Results: slides | 24 | 24 (pp20-43) | none (category-level "all reviewed", rev l.19; S9 carried) | PASS |
| Results: structured IDs | 1,782 | 1,782 (grep of row lines) | none | PASS |
| Results: MISSING_FROM_STRUCTURED | 4 | 4 (CIN l.77, l.495, l.1478; signature l.751) | none | PASS |
| Concall: participants | 11 | 11 (host L0019-L0021, Deepak Joshi L0026, 9 analysts L0103-L0804) | none | PASS |
| Concall: turns | 97 | 97 | none | PASS |
| Concall: analyst-side turns | 39 | 39 (all mapped to the 36 Step 4A exchanges; T67, T73, T81 merged into neighbours) | none | PASS |
| Concall: NUMBER / FORWARD / QUALIFIER / ENTITY / DATE rows | 222 / 67 / 47 / 53 / 30 | 222 / 67 / 47 / 53 / 30 (grep by type; sum 419) | none | PASS |
| Concall: fresh numeric sweep | 1 unit (MFS01, L0520) | 1. Digit lines with no same-line row (for example L0022, L0228, L0316, L0560-L0563, L0607, L0633-L0635, L0660, L0774, L0801, L0826-L0827) each restate a value with a row inside the documented drift | none | PASS |

Ledger-row accounting in A4: the preamble states all notes, turns and slides were reviewed, and "Unreviewed ledger rows: none" (rev l.19-24). A4 also takes up each named A2 flag (UNIDENTIFIED_ENTITY_ASSIGNMENT Q12; STEP_DOWN_ONLY_IN_NOTE3 1-G; FOOTNOTE_UNRESOLVED R1712, R1740; MGMT_ABSENCE; REPEAT_QUESTION and MARGIN_THEME; the studio-count conflict Q23; "beta margin" Q25; MFS01 rev l.23).
orphan_rows: none. missing_from_ledger: none. Coverage: PASS.

---

## AUDIT 2. ARITHMETIC (recomputed from raw extracted numbers)

I re-tied the load-bearing set and every figure added or changed in this loop. The one mismatch is the 8C guide check (row marked FAIL).

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| C Op EBITDA Q2 FY27 / Q1 FY27 / Q2 FY26 / H1 FY27 | 169.47 / 172.00 / 119.44 / 341.47 | 173.06 + 13.05 + 2.89 - 19.53; 176.46 + 12.81 + 2.45 - 19.72; 120.39 + 10.81 + 2.10 - 13.86; 349.52 + 25.86 + 5.34 - 39.25 | l.510-532 | PASS |
| Margins (ex-OI) | 24.37 / 27.17 / 20.97 / 25.70% | 24.366 / 27.169 / 20.966 / 25.701% | l.509 | PASS |
| Reported EBITDA Q2 / H1 FY27 / H1 FY26 / FY26 | 189.00 / 380.72 / 256.25 / 499.55 | PBT + D + Fin | l.523-532 | PASS |
| YoY revenue / PAT | +22.09% / +41.88% | 695.53 / 569.69; 129.44 / 91.23 | l.509, l.541 | PASS |
| PAT bridge sum | +38.21 | 26.38 + 23.65 - 2.24 - 0.79 + 5.67 - 12.76 - 1.70 | rev l.288 | PASS |
| Refund-stripped two-year gain (M2) H1 / Q2 | +228 bps / about +139 bps; +32.0% / +18.7% rupee | 27.828 - 25.547; 25.592 - 24.2; 369.72 / 280; 178.00 / 150 | l.523-532, l.1010, l.1022 | PASS |
| OI share Q2 / H1 FY27 | 2.81% / 2.95% | 19.53 / 695.53; 39.25 / 1,328.61 | l.509-511 | PASS |
| Q3 FY25 / Q3 FY26 incl OI (chart) | 20.17% / 18.95% | 94 / 466; 87 / 459 | l.1010, l.1021-1024 | PASS |
| H2 FY25 / H2 FY26 incl OI; Q3 gap to own half | 21.20% / 23.05% filed, 23.11% chart; 103 bps / 410-416 bps | 215 / 1,014; 243.30 / 1,055.43; 244 / 1,056 | l.1010, l.1021-1024; l.523-532 | PASS |
| M1 bound: Q3 FY26 OI threshold; Q4 need; even split; Q4 floor | 4.38; 33.22; 14.86%; 20.0% | 87 - 82.62; 37.60 - 4.38; 68.20 / 459; 119.40 / 597 | l.510-511, l.1010, l.1024 | PASS |
| 8C bull line / Q2 alternative | 22.7% / 21.1% | 18.95 + 3.760; 18.95 + 2.193 | l.509, l.523-532, l.1024 | PASS |
| 8C refund share of Q3 | 2.79 pts | 16 / 573 (573 = 459 x 1.2479) | L0390; rev l.268 | PASS |
| H2 guide margin, 16 outside / inside | 25.12% / 23.76% | 294.28 / 1,171.39; 278.28 / 1,171.39 | l.1118; rev l.268 | PASS |
| **8C guide check: guide-path Q3 margin before the refund (16 inside the guide), FY26 / FY25 seasonality** | **21.0-24.1% "before any refund strip"; implied 18.2-21.3% after the strip (21.0 - 2.79), hence "a bear-zone print fits the guide only if the 16 sits inside the guide and Q3 repeats the deep FY26 dip" (rev l.486)** | **19.6-22.7% (23.76 - 4.16; 23.76 - 1.03). The seasonal gap was measured on refund-free quarters, so it applies to the H2 margin before the refund (Step 3's own 23.76%). Subtracting the gap from 25.12% and then the full 2.79-point Q3 refund removes 1.42 pts too much: the H2 margin holds only 16 / 1,171.39 = 1.37 pts of refund. If the 16 sits outside the guide, the band is 21.0-24.1% before the refund. A bear print (18.95% or less) sits below both bands** | l.1010, l.1021-1024, l.1118-1121; L0390; rev l.268, l.486 | **FAIL (NF1)** |
| Inventory split (M3) | 45.29 (63%); 45.62; -17.92 vs -18.25 | as resolution table | l.179, l.247, l.518, l.609 | PASS |
| Top three (M4) | 50-60%; about 57-68% | as resolution table | L0262-L0264 | PASS |
| 6A margin after refund strip | 24.87% ex-OI | 330.47 / 1,328.61 | rev l.386 | PASS |
| TTM ROCE; after an 11 strip | 19.68% / 20.55% | 574.41 / 2,919.46; / 2,795.64; strip: 563.41 / 2,919.46 = 19.30% | l.523, l.532, l.629-642 | PASS (see NS4) |
| CFO/PAT C / SA | 0.75x / 0.36x | 195.34 / 262.09; 94.70 / 266.45 | l.709, l.330-333 | PASS |
| Net cash; ex MF gain | 920.21; 898.93 | 191.62 + 29.45 + 711.75 - 12.61; less 21.28 | l.611-616, l.634-642, l.716 | PASS |
| PE at CMP 7,037.90 | 31.2x / 38.4x | / 225.62; / 183.40 | rev l.457 | PASS |

arithmetic_mismatches: one (NF1).

---

## AUDIT 3. ADVERSARIAL READ (three most positive claims)

### AR1. "At or above Base on H1 pro-rata for revenue, margin, PAT, EPS, net cash and ROCE, also after an 11 refund strip"; revenue "Above Bull" (rev l.385-390, l.467)
Bear counter tested. H1 is the strong half (Q1 peak, Q3 low; L0043, L0655). On the heaviest seasonal shares in the extract the call still holds. FY25 H1 was 52.0% of revenue and 56.6% of EBITDA (1,096 / 2,109; 280 / 495). FY26 H1 was 50.2%, 51.3% and 51.5% for revenue, EBITDA and PAT (l.509-541, l.1010, l.1022, l.1116, l.1120). Implied FY27 revenue is 2,555-2,646, above Bull 2,502. Implied EBITDA incl OI is 673-742, or 653 after the 11 strip, a 25.6-28.0% margin against the 24% base. Implied PAT is about 509, or about 493 after the strip (base 397) [DERIVED]. The thinnest line is ROCE: on the seasonally neutral trailing four quarters it is 19.68% (closing CE), or 19.30% after the 11 strip, against 19% [DERIVED]. That is above base, by 30-68 bps.
Survives: NO. Presentation point logged as NS4.

### AR2. "The YoY expansion is real on either split" and "the direction holds" over two years (rev l.231-232)
Bear counter tested. The YoY base is tariff-hit: FY26 organic growth was 0.5% (l.1114, l.1137). The two-year frame already strips that and the refund (+139 to +228 bps). The remaining doubt is other income: the chart series includes it, and FY25 other income is ND. For the H1 two-year direction to reverse ex-OI, H1 FY25 other income would need to be below 0.67% of revenue (2.95 - 2.28), about 7.3 on 1,096. Q2 would need a Q2 FY25 share below 1.42%, about 8.8 on 621. Every filed quarter ran 13.38-19.72 (l.510-511) [DERIVED]. The Q2 stock drawdown of 20.40 (l.518) releases conversion cost into Q2, which if anything depresses the Q2 margin.
Survives: NO. The review already says the ex-OI gain "could be smaller still" and that its value is ND.

### AR3. Working capital "leans growth-induced"; the derived split "partly verifies management's deliberate raw-material build" (rev l.343, l.349, l.906)
Bear counter (same extract). The same management answer has a second leg: "inventory to our Europe USA customers ... Their inventory has increased ... roughly 20 days overall company export level inventories" (L0308-L0312). The split that supports the raw-material leg also tests this one:
- Group FG/WIP/stock-in-trade fell 20.40 in Q2 and rose only 26.45 over H1 (l.518). Stock outside the parent fell about 17.9 (26.45 - 44.37; l.179) [DERIVED].
- Twenty days of Q2 export sales is about 121 at sales value, or about 55 at the Q2 material-cost share of 45.3% [DERIVED 695.53 x 80% x 4 / 365 x 20; 315.14 / 695.53; L0115 ASR; l.516-518].
- So a build of that size was not added to group books in Q2 or H1 FY27.
- Reading (a): the build is FY26 own stock at the subsidiaries, now unwinding. In FY26, group FG/WIP/SIT rose 73.00, of which about 47.0 sat outside the parent [DERIVED 73.00 - 25.98; l.518, l.179].
- Reading (b): the rise is recent and sits with the Europe/US customers, which is how L0310 literally reads ("Their inventory"). Then Q2 revenue carries channel fill, and part of the growth the working-capital reading leans on may reverse in Q3 [INFERENCE].
- The separating observation is the date of the 20-day rise (Q19) and Q3 export revenue YoY.
The review sets up Q19 and lists the 100.26 to 82.01 fall (rev l.513). It does not apply the filed timing test, and it does not show that an own-book build in FY27 is excluded. Rule J symmetry: the split was used for management on the raw-material leg, so it must also be applied to the export-stock leg.
Survives: YES, as a qualifier. Graft into Q19 (rev l.513), 6B row 11 (rev l.408), 5A row (rev l.814) and Flag 18 (rev l.1065). Type: MISSING (finding NM1).

### Mandatory acquisition-economics probe
No acquisition, business purchase or third-party stake buy appears in either document. The only entity investment is 0.52 into a wholly owned subsidiary (SA CF l.335/l.339). That subsidiary has nil revenue and an H1 loss of 0.38 (l.457), so consideration / target PAT = 0.52 / (-0.38) is not meaningful. There is no seller and no earnings multiple. The Lubrizol "understanding ... we buy this much of resin" (L0820-L0821) is a supply commitment, which the review tests as a possible take-or-pay (Q20). Probe: NOT APPLICABLE, reason stated.

---

## FINDINGS (tagged)

### FACTUAL
NF1. Step 8C guide check (rev l.486) mixes refund bases. Agent: A4.
- The bullet applies the refund-free FY25-FY26 Q3 seasonal gap (1.03 / 4.16 pts) to the H2 margin of 25.12%, which includes the 16 refund if the refund sits inside the guide. It then labels 21.0-24.1% "before any refund strip" and reads the bear zone against it after a full 2.79-point strip (21.0 - 2.79 = 18.2).
- The H2 margin carries only 1.37 pts of the 16 (16 / 1,171.39), so that route strips 1.42 pts too much [DERIVED].
- Consistent route: start from the H2 margin before the refund, 23.76% (16 inside; rev l.268) or 25.12% (16 outside). Apply the gap. The guide-path Q3 before the refund is then 19.6-22.7% (16 inside) or 21.0-24.1% (16 outside) [DERIVED; l.1010, l.1021-1024, l.1118; L0390]. The band does not depend on the 573 illustration.
- So "a bear-zone print fits the guide only if the 16 sits inside the guide and Q3 repeats the deep FY26 dip" is wrong. A print at 18.95% or less sits below the guide path on both seasonalities. The guide midpoint would then need a Q4 near 28.4% before the refund (16 inside) or 31.0% (16 outside) [DERIVED on Q3 revenue 573, illustration: (278.28 - 108.58) / 598.39; (294.28 - 108.58) / 598.39]. Every Q4 on the chart is lower: 20.1%, 22.2%, 26.2% (l.1021).
- The bull line (22.7%) sits inside the 16-outside band and at the top edge of the 16-inside band, so the review's statement about the bull line holds.
- Fix: restate the guide check with both bands on the before-refund basis. Replace the bear-zone sentence with the corrected reading: a bear print sits below the guide path and puts the 27% midpoint at risk, unless Q3 dips deeper than in FY26. Add that consequence to the bear bullet (rev l.483) and update the YAML F1 fix text (rev l.1174). The brief and forward map need no number change. Optional: "the guide midpoint at risk" in the forward-map Q3 bear fork (rev l.1156).
- Provenance: the 21.0-24.1% derivation and the "15.4-18.5% if the 16 refund is inside the guide and is also stripped" line came from my prior merged audit's F1 (bullet 3). A4 carried it forward faithfully. The error is mine in origin; the fix sits in A4's text.

### MISSING
NM1. Surviving bear counter AR3 is not in the review. Agent: A4.
- The derived inventory split excludes an own-book export-stock build in FY27: group FG/WIP/SIT -20.40 in Q2 and +26.45 in H1, stock outside the parent about -17.9 (l.518, l.179). A 20-day rise is about 55-121 [DERIVED; L0115, L0308-L0312].
- Two readings. (a) FY26 own stock at the subsidiaries, now unwinding: about +47.0 outside the parent in FY26 (73.00 - 25.98). (b) Customer channel fill in H1, Q2 revenue pulled forward [INFERENCE].
- Fix: add the timing test and both readings to Q19 "Why it matters" (rev l.513), 6B row 11 (rev l.408), the 5A export-stock row (rev l.814) and Flag 18 (rev l.1065). Q19 already asks for the date that separates them.

### CONTRADICTION
None new.

### STYLE (logged; no loop)
- S1-S9 from the prior merged audit: still unapplied; carried as logged.
- NS1. 5A (rev l.818) and brief (rev l.1146): "consistent with the prior 10-15% discount record". A typical 80-85% of the leader is a 15-20% discount, slightly wider than 10-15%. The prior record compared PPF peers (3M, Eastman, XPEL). The call figure is for architectural film (L0478). Suggest "no narrower than the prior record, on a different product line". The "not parity" conclusion stands.
- NS2. 8C bull reading (rev l.482) is on the incl-OI basis, and 59% of H1 other income is market-linked MF gain (l.687). Say that a bull print needs the ex-OI companion to confirm it. The companion is already reported (rev l.485).
- NS3. Step 5 C inventory row says the split is "before FX translation and elimination effects" (rev l.315). The note says those effects "sit inside these differences" (rev l.343). Align to "including".
- NS4. 6A ROCE row (rev l.390) shows only the H1-annualised 24.31%, which the strong half flatters. Put the seasonally neutral TTM 19.68% (19.30% after the 11 strip) in the cell beside it. "Above Base" holds on both.

---

## VERDICT
INCOMPLETE. Loop back to A4.
- Gap 1 (NF1, FACTUAL): the 8C guide check (rev l.486) strips the whole Q3 refund from a seasonal band built on a refund-inclusive H2 margin. Before the refund, the guide-path Q3 is 19.6-22.7% (16 inside) or 21.0-24.1% (16 outside). A bear print at 18.95% or less sits below both bands, so it puts the guide midpoint at risk. It does not "fit the guide" under the guidance-basis reading. Fix the bullet, the bear meaning (rev l.483) and the YAML fix text.
- Gap 2 (NM1, MISSING): graft the export-stock timing test into Q19, 6B row 11, 5A and Flag 18. Group FG/WIP/SIT fell 20.40 in Q2 and rose only 26.45 in H1, against about 55-121 for 20 days of export sales. So the rise is either FY26 own stock (about +47.0 outside the parent) or customer channel fill.
All seven prior non-STYLE findings (F1, F2, M1, M2, M3, M4, C1) are RESOLVED. Coverage: PASS (no orphan rows, nothing missing from either ledger). Arithmetic: one mismatch (NF1); every other recomputed figure ties within rounding. No A2 or A3 loop is needed.

## STYLE NOTES
S1-S9 (carried) and NS1-NS4 above, recorded; no re-run on their account.

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
  - {metric: "8C guide check: guide-path Q3 FY27 margin incl OI before the refund, 16 inside the guide (FY26 / FY25 seasonality)", a4_value: "21.0-24.1% labelled 'before any refund strip'; implied 18.2-21.3% after a full 2.79-pt strip; 'a bear-zone print fits the guide only if the 16 sits inside the guide and Q3 repeats the deep FY26 dip' (rev l.486)", recomputed: "19.6-22.7% (H2 before refund 23.76% less 4.16 / 1.03 pt Q3 gap); 21.0-24.1% if the 16 is outside the guide; H2 holds only 1.37 pts of refund (16/1,171.39), so the A4 route over-strips 1.42 pts; a bear print <=18.95% sits below both bands", source_line: "l.1010, l.1021-1024, l.1118-1121; L0390; rev l.268, l.486"}
surviving_bear_counters:
  - {claim: "WC leans growth-induced; derived split partly verifies the deliberate raw-material build (rev l.343, l.349, l.906)", counter: "Same answer says export-level inventories at Europe/US rose ~20 days (L0308-L0312); group FG/WIP/SIT fell 20.40 in Q2 and rose only 26.45 in H1, stock outside parent ~-17.9 (l.518, l.179), vs ~55-121 for 20 days of Q2 export sales; so not an own-book FY27 build: either FY26 own stock at subsidiaries (~+47.0 outside parent, 73.00-25.98) now unwinding, or customer channel fill with Q2 pull-forward [INFERENCE]; separating fact = date of the rise (Q19), Q3 export revenue YoY", source_line: "L0308-L0312; L0115; l.179; l.516-518", type: MISSING}
findings_by_type:
  factual:
    - "NF1 (A4): 8C guide check (rev l.486) applies the refund-free Q3 seasonal gap to the refund-inclusive 25.12% H2 margin, then strips the full 2.79-pt Q3 refund; H2 holds only 1.37 pts, so it over-strips 1.42 pts. Before the refund the guide-path Q3 is 19.6-22.7% (16 inside, from rev l.268's 23.76%) or 21.0-24.1% (16 outside). A bear print <=18.95% sits below both, so the guide midpoint is at risk (Q4 near 28.4% or 31.0% needed on Q3 rev 573, above every chart Q4 20.1/22.2/26.2%, l.1021). The sentence 'a bear-zone print fits the guide only if the 16 sits inside the guide and Q3 repeats the deep FY26 dip' is wrong. Fix the bullet, the bear meaning (rev l.483), YAML fix text (rev l.1174). Origin: prior merged A5 audit F1 bullet 3"
  missing:
    - "NM1 (A4): graft AR3. Export-level stock up ~20 days (L0308-L0312) is not an own-book FY27 build: group FG/WIP/SIT -20.40 Q2, +26.45 H1, outside parent ~-17.9 (l.518, l.179) vs ~55-121 for 20 days of Q2 exports (L0115). Readings: FY26 own stock at subsidiaries (~+47.0 outside parent, 73.00-25.98) now unwinding, or customer channel fill [INFERENCE]. Add to Q19 (rev l.513), 6B row 11 (rev l.408), 5A row (rev l.814), Flag 18 (rev l.1065)"
  contradiction: []
  style:
    - "S1-S9 (prior merged audit): still unapplied; carried as logged"
    - "NS1: 'consistent with the prior 10-15% discount record' (rev l.818, l.1146): 80-85% is a 15-20% discount, on architectural film vs a PPF-peer record; say 'no narrower than, on a different product line'"
    - "NS2: 8C bull is incl OI and 59% of H1 OI is MF gain (l.687); state that a bull print needs the ex-OI companion (rev l.485) to confirm"
    - "NS3: Step 5 inventory row 'before FX translation and elimination effects' (rev l.315) vs note 'sit inside these differences' (rev l.343); align"
    - "NS4: 6A ROCE cell shows only H1-annualised 24.31%; add seasonally neutral TTM 19.68% (19.30% after the 11 strip) vs 19% base"
loop_back_to: "A4"
gap: "NF1 (FACTUAL): rebuild the 8C guide check (rev l.486) on the before-refund H2 margin: guide-path Q3 before refund 19.6-22.7% (16 inside, 23.76% H2) or 21.0-24.1% (16 outside); a bear print <=18.95% sits below both, so it puts the 27% midpoint at risk (Q4 ~28-31% needed) rather than 'fitting the guide'; align the bear meaning (rev l.483) and YAML fix text. NM1 (MISSING): add the export-stock timing test (group FG/WIP/SIT -20.40 Q2, +26.45 H1, outside parent ~-17.9 vs ~55-121 for 20 days of exports; FY26 ~+47.0 outside parent) with both readings to Q19, 6B row 11, 5A row, Flag 18"
style_notes:
  - "S1-S9 carried (prior merged audit), unapplied"
  - "NS1 pricing 'consistent with' -> 'no narrower than, different product line'"
  - "NS2 bull print needs the ex-OI companion (MF gains 59% of H1 OI)"
  - "NS3 align FX/elimination caveat wording in Step 5"
  - "NS4 show TTM ROCE 19.68% (19.30% after strip) in the 6A cell"
analyst_note: "All seven prior non-STYLE findings are fixed, and every dependent cell I traced is aligned. Both ledgers tie and the load-bearing arithmetic ties. Two new items loop to A4. First, the 8C guide check, added this loop, mixes refund bases. It applies the refund-free Q3 seasonal gap to the 25.12% H2 margin. It then strips the whole 2.79-point Q3 refund, but that H2 margin holds only 1.37 points of it. On the review's own 23.76% H2 margin before the refund, a guide-path Q3 before the refund is 19.6-22.7% if the 16 sits inside the guide. It is 21.0-24.1% if the 16 sits outside. A bear print at 18.95% or less therefore sits below the guide path either way, and the 27% midpoint would need a Q4 above any on the chart. The error started in my prior audit's F1 derivation, and A4 carried it forward. Second, the inventory split that supports the raw-material build also tests the export-stock claim. Group finished stock fell 20.40 in Q2. So the 20-day rise is FY26 own stock or customer channel fill."
```
