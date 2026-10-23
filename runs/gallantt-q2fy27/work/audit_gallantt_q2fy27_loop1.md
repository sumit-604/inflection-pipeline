# A5 ADVERSARY AUDIT (LOOP 1 RE-AUDIT) - Gallantt Ispat Limited (GALLANTT) - Q2 FY27 merged review

Auditor: A5, claude-opus-5-5, fresh context. Run date 23-Oct-2026.
Under audit: work/review_gallantt_q2fy27.md (A4, Loop 1 revision, 1,316 lines).
Prior audit checked for closure: work/audit_gallantt_q2fy27.md (M1-M9, S1-S8).
Read: the four A1 fulltexts, the four A1 structured files, the four A2 ledgers, the A4 review, the prior A5 audit.
Not opened: source PDFs, audio, anything under inputs/, the A3 forensics.

Anchor key:
- rev Lnnn = A4 review line.
- R:Lnnnn = original results fulltext. RR:Lnnnn = revised results fulltext. P:pN lL = presentation fulltext page and line. P:Rnnnn = presentation structured row. C:lN = concall fulltext line (ASR text). cc-Rnnn = concall structured row.
- led-rr / led-pres / led-cc Lnnn = A2 ledger lines. st-rr / st-pres Lnnn = A1 structured file lines.
- Rs Cr unless stated. Filed lakhs x 0.01.

---

## PART A. PRIOR FINDINGS M1-M9: CLOSURE CHECK

| ID | Prior gap | Status | Evidence of closure |
|---|---|---|---|
| M1 | resultsrev ledger lacked R744; stale 743 / QUALIFIER 54 | CLOSED | led-rr L3 and L14 now 744 and QUALIFIER 55; R744 enumerated at led-rr L18, L420. st-rr L4-5 and L757 agree. My grep: 744 IDs, 55 QUALIFIER rows. |
| M2 | p17 existing-mines "Nil" missing from structured | CLOSED | R1490 (st-pres L1509) and R1491 asterisk (st-pres L1510); led-pres Addendum 2 L263-278, 1,491 of 1,491. My grep: 1,491 IDs. |
| M3 | FY26 PPE sale Rs 110.30 Cr absent from A4 | CLOSED | rev L346 (Step 5 row), L377 (paragraph), Q3 at L517, 5B at L818, flag 9 at L1016, monitorable 22 at L995, brief L1107 and L1134. Ratios re-foot (Section 2). |
| M4 | open R018 conflict (p6 "30% QoQ" vs p21 "(23)%") | CLOSED | rev L39, L558, L997, L1026 list A3P-01 as a deck error. 6,148.56 / 8,010.40 - 1 = -23.24% (P:R1097-R1098). |
| M5 | Gorakhpur absorption counter | CLOSED | rev L443 (6D), L499 (seed row 8), L547 (Q33), L1019 (flag 12), L991 (monitorable 18), L1109, L1147, L1164. |
| M6 | promoter rise stated as a purchase | CLOSED | No promoter "bought" or "buying" left (grep). rev L71, L374, L548 (Q34), L975, L1031, L1086, L1110 say "mechanism undisclosed". |
| M7 | mines multiple not stated | CLOSED | rev L445 (6D, five qualifiers), L530 (Q16), L913, L935, L1022 (flag 15), L1136. |
| M8 | deck net debt / EBITDA on half-year EBITDA | CLOSED | rev L370, L385, L998, L1027, L1056. |
| M9 | p17 solar 7 / 85 MW evidence on Sidhpur | CLOSED | rev L264, L697, L729, L845, Q37 at L551, monitorable 6 at L979. |
| S1-S6 | style | APPLIED | rev L595, L188 and L539, L763, L673 and L747, L622 and L663, L383 and L883. |
| S7-S8 | A1/A2 conventions | OPEN at A1/A2 (no review change needed) | S7 recurs (see S12 below). |

All nine prior MISSING items are CLOSED.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

PLAIN-LANGUAGE BRIEF at rev L1092-L1164. All five parts are present and non-empty.
- (1) Summary narrative: PRESENT. rev L1096-L1113, 17 lines (inside the 10-20 band). It covers revenue, own volume, trading, core PBT, PAT, cash, the net-cash claim, the PPE sale, capacity, absorption, the promoter stake, the late filing and the decision.
- (2) Sector intelligence: PRESENT. rev L1115-L1124. It gives demand, price, cost, a bull and a bear reading, and the separating observation.
- (3) Business-model intelligence: PRESENT. rev L1126-L1139. It gives the chain, the spread, three drifts, the mines payback, a bull and a bear reading, and the separating observation.
- (4) Competition intelligence: PRESENT. rev L1141-L1151. Peers are tagged INFERENCE. It names where Gallantt wins and where it is weak, with a bull and a bear reading and the separating observation.
- (5) Forward map: PRESENT. rev L1153-L1164. One make-or-break line and ten dated catalysts. Each catalyst has a bull fork and a bear fork.

Gate result: PASS.

---

## 1. COVERAGE AUDIT

Method. (a) ID counts by grep on every structured file and ledger. (b) A fresh unit pass over each FULLTEXT: notes, statement lines and cells, slides and per-slide numbers, turns, questions, analysts and spoken numbers. (c) A diff against the A2 counts. (d) A test that every ledger row is cited in A4 or marked reviewed.

| Category | A2 count | Fresh count (A5) | Orphan / missing rows | Status |
|---|---|---|---|---|
| results: structured IDs vs ledger IDs | 449 / 449 | 449 (grep "^R### \|") | none | PASS |
| results: note rows (distinct notes) | 15 (7) | 15 (7): CF notes R:L398-400, R:L793-794, R:L1156; notes 1-5 R:L426-460 and the p11 copy from R:L817 | none | PASS |
| results: statement lines / cells | 96 / 296 | 96 / 296: P&L R:L1057-1082 = 26 x 6; BS R:L1084-1118 = 35 x 2; CF R:L1120-1147 + L1149-1155 = 35 x 2 | none | PASS |
| results: A2-noted rows absent from A4 | n.a. | R349/R350 (R:L1142) now cited at rev L346, L377, L517 | none | PASS (M3 closed) |
| resultsrev: structured IDs vs ledger IDs | 744 / 744 | 744; QUALIFIER 55 (grep) | none | PASS (M1 closed) |
| resultsrev: new standalone lines / cells | 94 / 284 | 94 / 284: P&L RR:L191-214 = 24 x 6; BS RR:L316-350 = 35 x 2; CF RR:L444-471 + L521-527 = 35 x 2 | none | PASS |
| resultsrev: note rows | 15 | 15: standalone CF notes RR:L500-502 and L528, notes 1-5 RR:L531-561 (no note beyond the consolidated set); 8 carried | none | PASS |
| resultsrev: A2-noted rows absent from A4 | n.a. | R307/R308 (RR:L466) cited at rev L346, L377; R744 cited at rev L28, L86 | none | PASS |
| presentation: slides / slides with no rows | 38 / 9 | 38 page markers; no-row pages 4, 5, 7, 14, 20, 25, 28, 33, 36 (all dividers or the contents list) | none | PASS |
| presentation: per-slide numbers, fresh on p6, p17, p37 | 30 / 18 / 16 | p6 30 (P:p6 l119-141); p17 18 including "Nil" (P:p17 l356-372); p37 16 (scrip code printed once for two columns) | none | PASS (M2 closed) |
| presentation: CELL / MAPS-TO / CORRECTION / loop-1 rows | 366 / 358 / 5 / 2 | 366 / 358 / 5 / 2 (R1490, R1491) | none | PASS |
| presentation: structured IDs vs ledger IDs | 1,491 / 1,491 | 1,491 (grep) | none | PASS |
| presentation: A2-flagged rows absent from A4 | n.a. | R018 listed as deck error A3P-01 (rev L39, L997); R030/R729 in Q28; R750/R1491 at rev L226 | none | PASS (M4 closed) |
| concall: turns / questions / analysts | 60 / 17 / 7 | 60 on A2's turn map (led-cc L263); 17 questions Q1a C:l215-217 to Q7 C:l419-422; 7 analysts | none | PASS |
| concall: management numbers, 21-figure spot check | 115 | All 21 present: cc-R018, R020-R023 (C:l128, l136-137), R090-R093 (C:l269-272), R098, R100 (C:l291, l297), R104 (C:l302), R111-R113 (C:l339-342), R118-R121 (C:l357-358), R026-R027 (C:l143) | none | PASS |
| concall: structured IDs vs ledger IDs | 263 / 263 | 263 (grep) | none | PASS |
| Row-to-A4 test | all rows reviewed (rev L22, L33) | Accepted. The blanket "reviewed" mark also covers rows where a cross-document forensic was missed: concall cc-R026/R027 against P:R863-R865 and P:R923-R925; deck P:R015, R086, R373, R479, R1101 and P:R1106-R1107 | no orphan row | PASS on coverage; the forensic misses are findings C1 and M12 |

Coverage result: no orphan rows; nothing missing from any ledger.

---

## 2. ARITHMETIC AUDIT

I recomputed every derived metric in A4's tables from raw filed lakhs (R:L1057-1155; RR:L191-214, L316-350, L444-471, L521-527) and from rendered deck cells.

| Metric (rev line) | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Op EBITDA, six columns (L195) | 131.54 / 185.09 / 109.69 / 378.39 / 294.79 / 716.44 (S 716.45) | 13,154.15 / 18,509.28 / 10,969.41 / 37,838.91 / 29,478.68 / 71,644.38 lakhs (S 71,644.98) | R:L1058, L1064, L1065, L1070; RR:L192-204 | PASS |
| Op EBITDA margin (L196) | 12.99 / 16.16 / 9.57 / 17.68 / 12.86 / 16.21% | 12.989 / 16.156 / 9.573 / 17.677 / 12.864 / 16.213% | R:L1057 | PASS |
| Reported EBITDA (L197) | 144.76 / 203.40 / 127.85 / 398.43 / 331.25 / 776.04 | Q1 FY27 16,481.45 + 3,011.47 + 847.35 = 20,340.27; others identical | R:L1064-1070 | PASS |
| Core PBT, OI/PBT, ETR, PAT margins (L199-203) | as printed | 6,502.13 / 8,979.10 - 1 = -27.59%; ETR 2,266.30 / 8,317.37 = 27.25%; 1,577.50 / 10,300.75 = 15.31% | R:L1058, L1070, L1073, L1076 | PASS |
| Gross margin, traded share (L205-206) | 25.45 / 27.35 / 21.00%; 8.63% | 1 - 90,526.63 / 1,14,589.15 = 20.999%; 1 - 75,498.96 / 1,01,275.02 = 25.452%; 1 - 83,229.90 / 1,14,566.71 = 27.353%; 9,886.58 / 1,14,589.15 = 8.628% | R:L1060-1062 | PASS |
| Standalone P&L and S-vs-C gaps (L138-172) | as printed | Other expenses FY26 37,166.08 - 37,165.48 = +0.60; PBT -0.60; PAT gap 169.37 / 8,723.25 = 1.942% | RR:L200-208 vs R:L1066-1076 | PASS |
| S-vs-C balance sheet (L176-186) | +1.80, +0.24, +4.19, +0.03, -6.03, -0.22, -0.005, capex +5.35 | 180.46, 24.38, 419.37, 3.02, -603.32, -22.01, -0.50, 535.08 lakhs | RR:L316-337, L465 vs R:L1084-1105, L1141 | PASS |
| Deck volumes (L212-221) | TMT 176 / 192 / 164; billets 204 / 231 / 180; DRI 216 / 236 / 204; Gorakhpur TMT 111 / 125 / 106 | identical to rendered cells | P:R838-R841, R853-R856, R918-R921, R928-R931 | PASS |
| EBITDA per billet tonne (L222-223) | deck 6,618 / 8,010 / 6,149 / 8,785; filed 6,448 / 8,013 / 6,094 / 8,110 | 13,154.15 / 204 = 6,448; 18,509.28 / 231 = 8,013; 10,969.41 / 180 = 6,094; 71,644.38 / 883.4 = 8,110 | P:R1096-R1100, R853-R856, R966 | PASS |
| YoY table (L237-252) | +13.15%; -6.82%; -11.76%; +35.3%; -16.61%; -342 bps; EBIT -24.97%; PAT -31.95% / -30.63%; EPS -30.66% / -31.98% | +13.146%; -6.818%; -11.765%; +35.29%; -16.61%; -341.6 bps; 7,418.79 / 9,887.52 - 1 = -24.97%; -31.954% / -30.632%; -30.66% / -31.98% | R:L1057-1082; P:R898-R931 | PASS |
| PAT bridge and sum (L299-313) | +3,388.65 ... -169.37; sum -2,841.56 vs -2,841.55 | identical; tax split +303.75 and -992.55 | R:L1057-1076 | PASS |
| OI-revert PAT; coal effect (L315, L321) | 56.92; 51.6-57.3 = 68-76% of 75.40 | 7,823.78 x 0.72752 = 5,691.9 lakhs; 51.57-57.29 / 75.40 | R:L1058-1073; C:l268-269 | PASS |
| QoQ table and diagnostics (L275-287) | Q1 FY26 1,127.78 / 21.89%; H2 FY26 avg 1,139.20 / 14.84%; 11.25x; 115%; 40 days | 1,12,777.84; 21.888%; 1,13,919.67; 14.837%; 9,886.58 / 878.47 = 11.254x; 228 / 198 = 115.2%; 1-Oct to 10-Nov = 40 days | R:L1057-1070; P:R823; P:p13 l285 | PASS |
| CFO / PAT, three bases, S and C (L337-342) | 1.24x / 0.49x; 1.00x / 0.56x; 1.25x / 0.56x | C 9,082.36 / 18,417.78 = 0.493; (9,082.36 + 1,306.38) / 18,417.78 = 0.564; (9,082.36 + 2,922.18 - 1,711.35) / 18,417.78 = 0.559; FY26 1.244 / 0.999 / 1.251 | R:L1132, L1140, L1146, L1150; RR:L456, L464, L470, L522 | PASS |
| FCF, WC, days, CCC (L343-354) | as printed | FCF C -18,764.24 and 25,411.42 lakhs; S -18,230.19 and 25,500.65; WC 358.31 and -12,500.90; receivable days 14.668 to 14.795 | R:L1092-1141; RR:L464-465 | PASS |
| FY26 PPE sale ratios (L346, L377) | 110.30 / 110.31; loss 0.24; carrying value ~110.55; 6.2% of S PPE; 31.8% of capex; 18.3% of CFO; 94.3% of S loan book | 11,030.50 / 1,77,243.99 = 6.22%; 11,030.50 / 34,725.91 = 31.76%; 11,030.50 / 60,226.56 = 18.32%; 11,030.50 + 24.36 = 11,054.86; (11,030.50 + 17,002.18) / 29,742.32 = 94.25% | R:L1126, L1142, L1149; RR:L316, L450, L464-468 | PASS (standalone basis, stated) |
| Net debt, net cash, D/E, deck bases (L367-372) | 21.82 to 165.86; S 21.86 to 165.89; +99.92; 0.17x; 0.289; 0.64x vs 0.30x | 2,181.75 to 16,586.13; 9,992.33 lakhs; 59,197.39 / 3,48,654.13 = 0.170; 1,00,643.05 / 3,48,654.13 = 0.2887; 190.58 / 632.84 = 0.301 | R:L1093-1117; P:p6 l134-137 | PASS |
| Equity roll-forward gap (L373) | 14.06 | 18,436.30 - (3,24,526.04 - 3,07,495.39) = 1,405.65 lakhs | R:L1080, L1104 | PASS |
| Promoter scale (L374) | +0.95 / 0.86 pp; 20.75-22.92 lakh shares; Rs 112-158 Cr | 0.86% and 0.95% x 24,12,80,945; x 537.90 and x 690.65 | P:R582-R594 | PASS |
| TTM and market data (L456, L473) | Rev 4,569.95; Op EBITDA 632.84; PAT 405.72; EPS 16.82; Rs 12,978 Cr; 32.0x | 4,56,995.19; 63,284.15; 40,572.43 / 2,412.809 = 16.815; 537.90 x 24.128 = 12,978.5; 31.98x | FY26 + H1 FY27 - H1 FY26; P:p37 l760-762 | PASS |
| Capacity, absorption and mines (L443, L445) | +23.7%; +39%; 178-188 KT; 59 KT; 95% / 86%; 1.0-1.6x | 12,29,000 / 9,93,300 = 1.237; 2,35,700 / 6,00,000 = 39.3%; 0.85-0.90 x 8,35,700 / 4 = 177.6-188.0; 58.9; 142 / 150 = 94.7%; 514.3 / 600 = 85.7%; 249 / 245.8 = 1.01x and 249 / 153.16 = 1.63x | P:R153, R157, R142, R844, R960, R767, R1011 | PASS |
| Capex tracker (L382, L444) | 652.54 spent of 1,191; thermal 155.35 vs 151.00; Prayagraj 3.74 of 175.00 | 438.60 + 213.94; 107.99 + 47.36 vs 106.00 + 45.00; P:R770-R771 | P:R764-R793 | PASS |
| Role 5 counts (L602, L660, L757, L850, L860) | 57.6%; 30 / 43; A3 B7 C5 D1 ND1; 20 / 32; 10 | 1,514 / 2,629 s; 13 NO rows counted at rev L615-657; grades sum 17; 20 items listed; 8 + 2 | C:l208, l437, l21; rev tables | PASS |

Arithmetic mismatches above rounding in A4's own tables: none.

---

## 3. ADVERSARIAL READ

The loop 1 grafts removed the promoter bull and hedged the capacity and mines bulls. These are the three most positive claims that remain in A4, each attacked from the same extracted text.

### Claim 1. The Q2 volume loss is a one-off from the two Gorakhpur shutdowns, and "the call explains the volume loss" (rev L258, L879, L960, L1102; flag 4 at L1011)
A4's Step 2 bull reads: "the volume loss is a one-off from the two Gorakhpur shutdowns". The 7A row calls the shutdown leg "plausible". Section C says "the call explains the volume loss but not the trading". The brief says "Management blames two shutdowns at Gorakhpur and dearer coal".

Strongest bear counter:
- Management places both shutdowns at Gorakhpur: "Margins were compressed this quarter by the two shutdowns at Gorakhpur" (C:l158). It names no Kutch shutdown in Q2. The Gujarat shutdown is a Q4 event (C:l397).
- Kutch still fell sharply on the deck's rendered cells. QoQ: power 43 to 32 (-25.6%, P:R803-R805), DRI 89 to 73 (-18.0%, P:R833-R835), billets 90 to 73 (-18.9%, P:R848-R850), TMT output 69 to 56 (-18.8%, P:R863-R865) and TMT sales 67 to 59 (-11.9%, P:R923-R925) [computed].
- Kutch TMT output fell faster than Gorakhpur's. Gorakhpur went from 127 to 105, -17.3% (P:R858-R859), and it was the plant that was shut [computed].
- Kutch carries about a third of the group's QoQ fall: 8 of 27 KT of TMT sales (30%), 17 of 52 KT of billets (33%) and 13 of 35 KT of TMT output (37%), on plant sums [computed].
- Kutch was also down YoY: TMT sales 65 to 59 (-9.2%, P:R926), billets 85 to 73 (-14.1%, P:R851), power 46 to 32 (-30.4%, P:R806) [computed]. Management's only Kutch reason is the lean monsoon, "where the demand usually stays low" (C:l363-364). A seasonal reason does not explain a YoY fall in the same season.

Strongest rebuttal from the extract: the Gujarat captive-power debottleneck was "completed in the last month" (C:l425), so some Kutch downtime may be project work [INFERENCE: no Kutch downtime is stated]. Even on that reading, the call names "two shutdowns at Gorakhpur" only, so the call does not explain the Kutch loss.

Survives? YES. A4 never splits Q2 volume by plant beyond the Gorakhpur rows in Step 1(e). It never states that the plant without a shutdown fell 12-19%.
Graft into A4: the Step 2 bear reading and separating observation (add Q3 FY27 Kutch TMT sales against 67 KT, P:R924); the Step 3 distortions line (L284); the 7A "all one-time" row (L879); the Section C reconciliation line (L960); flag 4 or 5; brief part 1 line L1102; and Q9 (ask for the Kutch cause and its cost). Finding M10.
Linked contradiction: the call's Kutch rolling-mill claim is finding C1 below.

### Claim 2. The dated capacity step is the main new positive; integration protects the spread; the first full quarter "lifts volume at a steady margin" (rev L961, L1149, L1164)
The loop 1 absorption graft covers whether Gorakhpur can sell the extra tonnes (rev L443). It does not cover what the extra tonnes cost to make.

Strongest remaining bear counter:
- Gorakhpur adds capacity "at every stage of the chain at Gorakhpur except" sponge iron (C:l133-135; A1 records the exclusion as cc-R156).
- Gorakhpur already uses most of its own DRI. In FY26 it made 577.6 KT and sold 110.4 KT against 514.3 KT of billets, which is 0.91 t of own DRI per billet tonne (P:R951, R987, R960). In Q1 FY27 it made 148 KT, sold 10 KT and made 142 KT of billets, which is 0.97 t per tonne (P:R829, R889, R844) [computed].
- At management's 85-90% ramp, 178-188 KT of billets a quarter would need about 162-183 KT of DRI a quarter on the same charge ratio. Gorakhpur makes about 144-148 KT (FY26 average, Q1 FY27 peak) [computed; INFERENCE: constant charge mix; Gorakhpur DRI capacity NOT FOUND].
- The 14-39 KT a quarter gap must come from merchant DRI that Gorakhpur now sells, or from bought metallics. Merchant DRI was one of the Q2 revenue props: 32 KT at Gorakhpur (P:R888). Management says metallics prices "rose sharply in the second half of the quarter" (C:l129-130).
- So the incremental tonnes are less integrated than the base. The deck's "integrated cost position" (P:p10 l226) does not carry over to them in full.

Strongest rebuttal from the extract: the Gorakhpur DRI kilns may have spare capacity. FY26 Gorakhpur DRI output rose 40.6% after the 0.165 MTPA kiln (P:R953; P:p8 l160-162), but no Gorakhpur DRI capacity is stated. Billets can also take more scrap or pig iron, and both are bought.

Survives? YES, at INFERENCE tier on deck cells and a direct management statement. A4 cites C:l133-135 only for "lands at Gorakhpur" (rev L443). It never states the sponge-iron exclusion.
Graft into A4: the 6D Gorakhpur killing evidence, the competition bear reading (L1150), the Q1 FY28 bear fork (L1164), and Q33 (ask for Gorakhpur DRI capacity and the metallics plan). Finding M11.

### Claim 3. Prices rose late in Q2, so the better spread lands in Q3 (rev L1121, L258)
Strongest bear counter: the 21% is a one-month YoY figure (C:l128, l291), not a Q3-versus-Q2 spread. Coal took about 4.5-5% of sales (C:l268-269), iron ore rose too (C:l270), metallics rose sharply (C:l129-130), and "some bit of it is obviously being passed on to the energy prices" (C:l257-258). The analyst's import question (C:l285-286) was answered with demand data only (C:l287-291). The deck's safeguard slide gives a 200-day duty from Apr-2025 (P:p34 l713-715), and it notes record China exports of 119 MT (P:p34 l711-712).
Survives? YES, but A4 already carries the substance: the sector bear "coal stays dear and new capacity ... holds bar prices down" (L1122), the input leg "not one-time on its own words" (L317), the realisation contradiction (L257, L878) and the safeguard PENDING LIVE VERIFICATION (L1124). No graft is required. The unanswered import question is a grading note (S11).

### MANDATORY ACQUISITION-ECONOMICS PROBE (re-run)
- Iron ore blocks: Rs 249.00 Cr raw-material plan (P:R767) against about Rs 153-246 Cr a year of claimed EBITDA (Rs 2,000/t, P:p13 l290, on 765.8 KT sales or 12.29 lakh MT capacity, P:R1011, R157). That is about 249 / 245.8 = 1.0x to 249 / 153.2 = 1.6x one year's claimed EBITDA [computed]. A4 now states this multiple with its five bear qualifiers (rev L445, L530, L1022, L1136). The bear reading survives and is grafted. No new graft.
- Coal block: consideration NOT FOUND, reserves NOT FOUND, undeveloped (C:l376-379). No multiple can be stated. A4's Q15 asks for reserves, grade, capex and the decision date.
- Suryalaxmi Technologies: cost of investment Rs 0.01 Cr (RR:L320 vs R:L1088). Nil revenue. No meaningful multiple.
- Promoter stake, if it was a purchase: about Rs 112-158 Cr at 32.0x TTM EPS, a full multiple. A4 carries the scale and the mechanism caveat (rev L374, L548).

---

## FINDINGS (every finding tagged)

| ID | Type | Loop to | Severity | Exact gap | Evidence lines |
|---|---|---|---|---|---|
| C1 | CONTRADICTION | A3, then A4 | MEDIUM | The call says Kutch rolling-mill utilisation rose from 66% to 68% (C:l142-143; cc-R026, cc-R027). The deck's rendered cells show Kutch TMT output fell from 69 to 56 KT (-18.8% QoQ) and Kutch TMT sales from 67 to 59 KT (-11.9%). On a fixed capacity, 66% x 56 / 69 = 53.6% [computed], not 68%. A4 carries the call figure as "+2 pp delivered" (Q32, rev L546), "MAINTAINED" (L844) and "66% to 68%" (L443, L633, L696), against its own evidence order, DECK > ASR (rev L8). Management's own "not much result" (C:l363-364) agrees with the deck. Needed: record the conflict; 3A Kutch row to DISPUTED, leaning NOT DELIVERED; rewrite Q32; count it in the call-vs-deck conflicts (four to five) in 3D and flag 19; correct the 6A direction. | C:l142-143, l363-364; P:R863-R865, R923-R925; rev L8, L443, L546, L633, L696, L844 |
| M10 | MISSING | A4 | MEDIUM | Surviving bear counter to "the volume loss is a one-off from the two Gorakhpur shutdowns" and "the call explains the volume loss" (Claim 1). Kutch had no named Q2 shutdown (C:l158), yet it fell 12-26% QoQ across power, DRI, billets, TMT output and TMT sales. It carries 30-37% of the group's QoQ volume fall, and it was down YoY in the same season. | P:R803-R806, R833-R835, R848-R851, R858-R859, R863-R865, R923-R926; C:l158, l363-364, l397; rev L258, L284, L879, L960, L1011, L1102 |
| M11 | MISSING | A4 | LOW | Surviving bear counter to the capacity positive's margin leg (Claim 2). Gorakhpur adds no sponge iron (C:l133-135; cc-R156). At the 85-90% ramp, own DRI falls about 14-39 KT a quarter short at the FY26 to Q1 FY27 charge ratio of 0.91-0.97 [computed; INFERENCE; DRI capacity NOT FOUND]. The gap is filled by diverted merchant DRI or bought metallics, whose prices "rose sharply" (C:l129-130). | C:l129-130, l133-135; P:R828-R829, R843-R844, R888-R889, R951, R960, R987; rev L443, L1149-L1150, L1164 |
| M12 | MISSING | A3, then A4 | LOW | Two deck arithmetic errors are absent from A4's deck-error list (six errors at rev L958, L997, L1026). (a) EBITDA "45.7% QoQ" on p6, p11, p21 and p23 (P:R015, R086, R373, R479, R1101) ties only to Q1 FY27 EBITDA including other income: 110.52 / 203.40 - 1 = -45.66% (R:L1064-1070). The deck's own Q1 chart value is 185 (P:R1092), which gives 110.52 / 185.09 - 1 = -40.3%, or 111 / 185 - 1 = -40.0%. The same p21 slide computes margin QoQ (655) bps on the 185 basis (16.19 - 9.64). (b) The p23 margin bars FY25 17.0% and FY26 18.0% (P:R1106-R1107) do not tie to the slide's own bars: 710 / 4,293 = 16.5% and 776 / 4,419 = 17.6% (P:R1087-R1088, R1094-R1095). Needed: add both to the deck-error list (six to eight), to Q10 (the QoQ delta uses an including-other-income Q1 base), to flag 19 and to monitorable 24. | P:p6 l123; P:p11 l233; P:p21 l451; P:p23 l499-513; P:R015, R086, R373, R479, R1087-R1088, R1092, R1094-R1095, R1101, R1106-R1107; R:L1064-1070; rev L524, L958, L997, L1026 |

Factual findings: none. Arithmetic in A4's own tables is clean.

---

## VERDICT

VERDICT: INCOMPLETE.

- Failing agents, in pipeline order: A3 (C1 forensic, M12 forensic), then A4 (grafts for C1, M10, M11, M12).
- loop_back_to = A3, the earliest failing agent.
- Types: one CONTRADICTION (C1) and three MISSING (M10, M11, M12). No FACTUAL finding. No arithmetic mismatch.
- Effect on the review's conclusions: none of the four changes the protocol verdict (PROCEED WITH FLAGS) or the cash class (INDETERMINATE-WITH-DIRECTION). C1 and M10 change two stated readings. One is the Kutch "+2 pp delivered". The other is "the call explains the volume loss". Both point the same way as the existing flags.
- Loop budget: A4 records loop 1 as the final permitted iteration (rev L6). Whether to run the narrow loop or carry C1 and M10-M12 to the save gate as open items is the orchestrator's and operator's call, not A5's.
- Narrow re-run scope, if run:
  - A3: concall forensic on A3C-13 against P:R863-R865 and R923-R925; presentation forensic on P:R015, R086, R373, R479, R1101 and R1106-R1107.
  - A4: graft C1 and M10-M12 at the review lines named in the table. No other section needs to change.
  - A5: re-audit of the grafted lines only.

---

## STYLE NOTES (logged; no loop)

- S9. rev L647, claim 33, carries "Rs 135 Cr (12.91%) Q2 FY26" without A2's ASR_SUSPECT flag (led-cc L167, cc-R046). 135 / 1,012.75 = 13.33%. The deck's p21 YoY (368) bps implies 13.32%, and 12.91% is the H1 FY27 margin spoken at C:l192. Mark the cell ASR_SUSPECT.
- S10. Sidhpur status: the deck's Kutch solar tracker line shows Rs 39.58 Cr spent of a Rs 50.00 Cr plan, with Rs 10.42 Cr still to spend (P:R785-R787). This supports "the capital investment is almost done and it is in commissioning phase" (C:l302) and the "leaning NOT DELIVERED" reading (rev L697). C:l302 also says "22 megawatt in Gujarat" against 18 MW (A2 flag ASR_SUSPECT on cc-R104). The evidence is optional, because the reading is already correct.
- S11. rev L745: Q3a is graded B. The import-effect half of the question (C:l285-286) got demand data only (C:l287-291). Consider C, or note the deflection.
- S12. Recurrence of prior S7 at A1. Concall structured context notes cite source-line numbers (file line minus 17): cc-R046 "line 175" is C:l192; cc-R084 "line 281" is C:l298; cc-R102 "line 186" is C:l203; cc-R104 "line 135" is C:l152; cc-R031 "line 373" is C:l390. A4 cites the right file lines. Fix the A1 convention at the next extraction.

---

```yaml
stage: A5-adversary
company: "GALLANTT"
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
  - claim: "Q2 volume loss is a one-off from the two Gorakhpur shutdowns; the call explains the volume loss (rev L258, L879, L960, L1102; flag 4)"
    counter: "Kutch had no named Q2 shutdown (C:l158 'two shutdowns at Gorakhpur'; Gujarat shutdown is Q4, C:l397) yet fell QoQ: power -25.6%, DRI -18.0%, billets -18.9%, TMT output -18.8%, TMT sales -11.9%; Kutch TMT output fell faster than shut Gorakhpur's (-17.3%). Kutch = ~30-37% of the group QoQ volume fall (8/27 KT TMT sales, 17/52 KT billets, 13/35 KT TMT output) [computed]. Also down YoY (TMT sales -9.2%, billets -14.1%); management's only Kutch reason is the lean monsoon (C:l363-364), which cannot explain a YoY fall."
    source_line: "P:R803-R806, R833-R835, R848-R851, R858-R859, R863-R865, R923-R926; C:l158, l363-364, l397"
    type: MISSING
  - claim: "Capacity step is the main new positive; integration protects the spread; first full quarter lifts volume at a steady margin (rev L961, L1149, L1164)"
    counter: "Gorakhpur adds capacity at every stage except sponge iron (C:l133-135; cc-R156). It already uses 0.91-0.97 t own DRI per billet tonne (FY26 577.6 made, 110.4 sold, 514.3 billets; Q1 FY27 148, 10, 142). At 178-188 KT billets a quarter it needs ~162-183 KT DRI vs ~144-148 KT made [computed; INFERENCE: constant charge mix; DRI capacity NOT FOUND]. Gap filled by diverting merchant DRI (32 KT at Gorakhpur in Q2, a revenue prop) or buying metallics whose prices 'rose sharply' (C:l129-130): incremental tonnes are less integrated than the base."
    source_line: "C:l129-130, l133-135; P:R828-R829, R843-R844, R888-R889, R951, R960, R987"
    type: MISSING
findings_by_type:
  factual: []
  missing:
    - "M10 (A4, MEDIUM): graft the Kutch volume counter to the 'one-off Gorakhpur shutdowns' reading into Step 2 bear and separating observation (Kutch TMT sales vs 67 KT, P:R924), Step 3 distortions L284, 7A L879, Section C L960, flag 4/5, brief L1102, Q9"
    - "M11 (A4, LOW): graft the Gorakhpur sponge-iron exclusion (C:l133-135) and DRI-gap counter into 6D Gorakhpur killing evidence, competition bear L1150, Q1 FY28 bear fork L1164, Q33"
    - "M12 (A3 then A4, LOW): deck errors missing from A4's six-error list: (a) EBITDA '45.7% QoQ' (P:R015, R086, R373, R479, R1101) ties only to Q1 EBITDA incl. other income 203.40 (-45.66%), not the deck's own 185 (P:R1092; -40.3%); (b) p23 margin bars FY25 17.0% / FY26 18.0% (P:R1106-R1107) vs own cells 710/4,293 = 16.5% and 776/4,419 = 17.6%; add to deck-error list, Q10, flag 19, monitorable 24"
  contradiction:
    - "C1 (A3 then A4, MEDIUM): call Kutch rolling-mill utilisation 66% to 68% (C:l142-143; cc-R026/R027) vs deck Kutch TMT output 69 to 56 KT, -18.8% QoQ (P:R863-R865) and TMT sales 67 to 59 KT (P:R923-R925); 66% x 56/69 = 53.6% [computed]; A4 carries '+2 pp delivered' (rev L546), 'MAINTAINED' (L844), '66% to 68%' (L443, L633, L696) against its DECK > ASR order (rev L8)"
  style:
    - "S9: rev L647 claim 33 carries Q2 FY26 '12.91%' without A2 ASR_SUSPECT (cc-R046); 135/1,012.75 = 13.33%; deck (368) bps implies 13.32%"
    - "S10: Kutch solar tracker Rs 39.58 Cr spent of Rs 50.00 Cr, Rs 10.42 Cr balance (P:R785-R787) supports Sidhpur 'in commissioning phase' (C:l302); C:l302 says 22 MW vs 18 MW (cc-R104 ASR_SUSPECT)"
    - "S11: rev L745 Q3a graded B; the import-effect half (C:l285-286) got demand data only (C:l287-291)"
    - "S12: A1 concall context notes cite source lines (file line minus 17), e.g. cc-R046 'line 175' = C:l192, cc-R084 'line 281' = C:l298; recurrence of prior S7"
loop_back_to: "A3"
gap: "A3: (C1) missed that the call's Kutch rolling-mill utilisation 66% to 68% (C:l142-143) conflicts with deck Kutch TMT output 69 to 56 KT, -18.8% QoQ (P:R863-R865) and sales 67 to 59 KT (P:R923-R925); A4 carries '+2 pp delivered' (rev L546, L696, L844). (M12) deck EBITDA '45.7% QoQ' (P:R015, R086, R373, R479, R1101) ties only to Q1 EBITDA incl. other income 203.40, not the deck's own 185 (-40.3%); p23 margins FY25 17.0% / FY26 18.0% (P:R1106-R1107) vs 16.5% / 17.6% from its own cells. A4: graft C1 and M12, plus (M10) the Kutch volume counter to the 'one-off Gorakhpur shutdowns' reading (P:R803-R865, R923-R926; C:l158, l363-364) and (M11) the Gorakhpur sponge-iron exclusion and DRI gap (C:l129-135; P:R828-R829, R888-R889, R951, R960, R987). Prior M1-M9 all CLOSED; arithmetic clean; verdict and cash class unaffected."
style_notes:
  - "S9: mark the Q2 FY26 12.91% cell ASR_SUSPECT (rev L647)"
  - "S10: optional Kutch solar tracker evidence for Sidhpur (P:R785-R787); note the 22 vs 18 MW ASR gap"
  - "S11: consider grade C for Q3a, or note the deflected import question"
  - "S12: fix the A1 concall context-note line convention (offset 17)"
analyst_note: "Re-audit after loop 1. All nine prior MISSING items (M1-M9) are CLOSED: the resultsrev ledger holds R744, the p17 'Nil' cell is R1490, and A4 carries the PPE sale, the R018 deck error and the absorption, promoter, mines, net-debt and Sidhpur grafts. The brief passes. Coverage re-counts clean at 449, 744, 1,491 and 263 IDs, and every derived metric in A4's tables re-foots. The new gaps come from the deck's plant split. Kutch had no named Q2 shutdown, yet its TMT output fell 19% QoQ and its TMT sales 12%. Kutch carries about a third of the group's QoQ volume fall. That contradicts the call's Kutch mill claim of 66% to 68%, which A4 carries as '+2 pp delivered'. It also weakens A4's line that the call explains the volume loss. Two smaller grafts follow. Gorakhpur adds no sponge iron, so the new tonnes are less integrated. The deck's '45.7% QoQ' EBITDA fall and its FY25-FY26 margin bars do not tie to its own cells. Verdict, cash class and arithmetic are unaffected. A4 called loop 1 final, so the orchestrator decides whether to loop or carry these as open items."
```
