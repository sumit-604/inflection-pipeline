# A5 AUDIT: Fairchem Organics Limited (FAIRCHEMOR), Q2 FY27, full-quarter merged review

Agent: A5 adversary | model claude-opus-5-5 | run date 2026-10-24 | loop_iteration 0
Review under audit: runs/fairchemor-q2fy27/work/review_fairchemor_q2fy27.md (1,213 lines; results + concall + presentation).
Inputs read: the three A1 fulltexts, the three A1 structured files, the three A2 ledgers and the A4 review. Not read: the source PDFs, anything under inputs/, any A3 output, any prior audit.
Anchors: "rev L###" = review line. "res / deck / call L###" = fulltext line. "res / deck / call R###" = structured row. [DERIVED] = my arithmetic on anchored values.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT | sector PRESENT | business model PRESENT | competition PRESENT | forward map PRESENT. Gate: PASS.

| Part | Location | Content check | Status |
|---|---|---|---|
| 1 Summary narrative | rev L1046-1060 | 14 lines (inside 10-20). Document Review Protocol not governing. Figures tie to Step 1-5 | PRESENT |
| 2 Sector intelligence | rev L1062-1068 | Feedstock economics, duty cut, alternate uses, import parity, end markets | PRESENT |
| 3 Business-model intelligence | rev L1070-1076 | Spread model, operating leverage, supplier terms, funding, model drift | PRESENT |
| 4 Competition intelligence | rev L1078-1095 | Claimed advantages, weaknesses, peers PENDING, competitive risk | PRESENT |
| 5 Forward map | rev L1097-1106 | 9 catalysts, each with a bull fork and a bear fork. 8 of 9 dated (M1 undated, S2) | PRESENT |

---

## 1. COVERAGE AUDIT

Method. I ran a fresh enumeration over each A1 fulltext (the spine), then checked it against the structured files and the A2 ledgers. ID totals by grep: results 484 rows, presentation 512 rows, concall 182 rows plus 101 turns (283). Per-type counts match each structured header. Then I mapped every R-ID the review cites (grep of rev, 1,213 lines) against each ledger.

### 1A. Fresh enumeration vs A2 ledger

| Document | Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | Notes | 9 | 9 (Notes 1-7 res L469-538; CF Note 1 L464; Note 6 cont. L532) | none | PASS |
| Results | Footnotes | 8 | 8 | none | PASS |
| Results | Line items | 353 | 353 (P&L 25 lines x 6 periods + R141 = 151; BS 38 lines x 2 = 76; CF 72; segment 54) | **res R294** (L447) | **FAIL, A3 (M1)** |
| Results | Zero-standing | 19 | 19 | none | PASS |
| Results | Agenda items | 2 | 2 (res L52, L67) | none | PASS |
| Results | Auditor paras | 3 | 4 (res L159, L163, L171, L180) | none (para 1 is identification only; periods at R424 R425) | STYLE S6 |
| Results | Entities | 36 | 36 | none | PASS |
| Results | Signatures | 3 | 3 (res L114, L196, L552) | none | PASS |
| Results | Remaining numbers (A2 sec 10) | 13 | 13 | **res R374**, with qualifier R481 (L593) | **FAIL, A3 (M2)** |
| Presentation | Slides | 24 | 24 (deck [page 1]-[page 24]) | none | PASS |
| Presentation | NUMBER / ENTITY / FORWARD / DATE / QUALIFIER | 321 / 60 / 20 / 24 / 87 | 321 / 60 / 20 (13 + 7 addendum) / 24 / 87 (39 + 48 addendum) | none material | PASS |
| Presentation | Zero-standing | 14 | 14 | none | PASS |
| Concall | Participants | 15 | 15 | none | PASS |
| Concall | Turns | 101 | 101. Two possible unsplit speaker changes: T024 at call L144 ("Okay, okay" after the 21 s gap R167); T026 at call L148-149 | none | PASS (S6) |
| Concall | Questions | 45 | 46: adds the question at call L291 ("what sustainable margin ... will throw some light?"), answered at L292. A1/A2 class L290-291 as moderator turn T075 | none (A4 row 31 covers it) | **CONTRADICTION C2** |
| Concall | Numbers | 45 | 45 (every number on call L21-L328 is captured) | none | PASS |
| Concall | Forward | 30 | 30 (land timing "current period", L205, sits as DATE R138) | none | PASS |
| Concall | Dates | 18 | 18 | none | PASS |
| Concall | Entities | 48 | 49: adds "crude oil prices" (call L157, analyst). A1 took "biodiesel" from the same line (R069) | none | STYLE S6 |
| Concall | Qualifiers | 41 | 41. I re-timed every timestamp. 18 gaps of 20 s or more, sum 20+25+21+21+36+32+29+29+38+26+51+22+22+23+23+28+24+24 = 494 s | none | PASS |

Why the three extra fresh-pass units do not loop to A2. The enumeration guarantee exists to stop content going unreviewed. The content of each unit is already in the A4 review. The crude-oil link is at rev L688 and L1066. The L291 question is 4A row 31 (rev L622). Auditor para 1 carries only the entity and the periods, captured at res R424 R425. This follows the run's own precedent (prior A5 S14-S16, carried at rev M31 L994). The operator can overrule this classification.

### 1B. Ledger rows vs A4 review (cited, or marked "reviewed, no finding")

| Ledger | Rows | Cited by ID or explicit range | Covered only by line, turn or section anchor | Material orphans | Status |
|---|---|---|---|---|---|
| Concall | 182 + T001-T101 | 121 rows (incl. "reviewed, no finding" ranges at rev L38; FORWARD range R094-R123 at rev L740); all 101 turns | 61 rows: R024 R027 R029 R036 R037 R038 R040 R043; entities R058-R060 R062 R063 R065-R072 R075-R085 R089 R090 R093; dates R130 R131 R133 R137 R138 R139 R141; qualifiers R155 R158 R159 R160 R162 R163 R165 R168 R171-R174 R176-R182. Each one's line or turn is cited with its content (e.g. R024 at rev L593; R029 at L662; gaps via the 494 s aggregate, L422) | none | PASS (S1) |
| Results | 484 | about 220 | about 260 (BS totals, CF other lines, segment restatements, entities, dates, qualifiers), covered by Step 1 and 5 tables, A3 F-check ties and line anchors | **R294; R374/R481** | **FAIL, A3** |
| Presentation | 512 | about 150 (incl. slide ranges at rev L36) | about 360, covered by A3P section 5 tie-out and the history tables | none (context rows R296 R297 used in M4; R319-R321 at S7) | PASS (S1) |

Orphan detail.
- **res R294** (L447): H1 FY26 "Repayment of Current Borrowings (net)" (862.76) L. The H1 FY26 financing total ties: 862.76 + 976.57 + 161.48 = 2,000.81 (res R302 L454). The ID and the value appear nowhere in the review (grep "862", "8.63": no hit). It is material because the review lists "borrowings at 30-Sep-2025" as missing evidence (rev L1028) and asks for it (rev L568 Q9, L933 Q19). The extract derives it. See M1.
- **res R374 / R481** (L593): Annexure B item 4, "6.07% shareholding, considering entities holding shares in which he is interested" (the land counterparty). "6.07" appears nowhere in the review. It is material to the related-party economics. See M2.

---

## 2. ARITHMETIC AUDIT

All figures recomputed on the lakh basis from structured rows (res R012-R159 at L225-266; BS R163-R235 at L292-376; CF R237-R307 at L406-460), then converted (x0.01).

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Op EBITDA Q2 FY27 / Q1 FY27 / Q2 FY26 | 17.54 / 17.87 / 4.19 | 1,753.71 / 1,786.71 / 418.79 L | res R081-R083, R061 R062 R066, R049 R050 R053, R019 R016 R020 (L227-244) | PASS |
| Op EBITDA FY26 pre / post exc; H1 FY26; H1 FY27 | 21.62 / 20.73; 9.41; 35.40 | 2,161.69 / 2,073.42; 941.05; 3,540.42 | res R085 R092 R064 R052 R021; R087 R071 R054 R024; R084 R063 R051 R023 | PASS |
| Op EBITDA margin (Q2 FY26, Q1 FY27, Q2 FY27, FY26, H1 FY26, H1 FY27) | 3.76 / 10.14 / 10.51 / 4.70 / 3.88 / 10.32% | 3.755 / 10.143 / 10.506 / 4.703 / 3.879 / 10.320% | as above / revenue R012-R018 | PASS |
| Reported EBITDA (same six periods) | 4.56 / 18.21 / 17.68 / 22.04 / 9.92 / 35.90 | 456.22 / 1,821.46 / 1,768.41 / 2,203.98 / 991.84 / 3,589.87 L | PBT + D + FC | PASS |
| Core PBT (PBT - OI) | 0.80 / 13.29 / 13.50 / 6.01 (6.90) / 2.29 / 26.79 | 80.33 / 1,328.92 / 1,350.31 / 601.44 (689.71) / 228.53 / 2,679.23 L | res R088-R093, R019-R024 | PASS |
| OI / PBT | 31.8 / 2.5 / 1.1 / 17.8 / 18.2 / 1.8% | 31.78 / 2.55 / 1.08 / 17.84 / 18.18 / 1.81% | | PASS |
| ETR | 34.4 / 26.6 / 25.5 / 24.3 / 30.3 / 26.0% | 34.43 / 26.57 / 25.51 / 24.31 / 30.34 / 26.04% | res R106-R111 L253-254 | PASS |
| PAT margin | 0.69 / 5.69 / 6.09 / 1.21 / 0.80 / 5.88% | 0.692 / 5.685 / 6.091 / 1.205 / 0.802 / 5.883% | res R112-R117 L254-255 | PASS |
| Gross margin | 20.32 / 22.65 / 23.07 / 20.13 / 19.33 / 22.85% | 2,266.43 / 3,989.93 / 3,850.77 / 9,253.18 / 4,688.65 / 7,840.70 L over revenue | res R030-R042 L234-235 | PASS |
| Opex ratio | 16.57 / 12.51 / 12.56 / 15.43 / 15.45 / 12.53% | 1,847.64 / 2,203.22 / 2,097.06 / 7,091.49 / 3,747.60 / 4,300.28 L over revenue | res R043-R048, R055-R058 R060 R065, R067-R072 R079 | PASS |
| YoY: revenue; op EBITDA; margin (GM / opex split); EBIT; core PBT; PBT; PAT; EPS; D&A; FC; OI | +49.7%; +318.8%; +675 bps (275 / 400); +939%; +1,581%; +1,059%; +1,217%; +1,268%; +2.8%; +93.7%; -60.7% | 1.4968; 4.1876; 675.1 (274.6 / 400.4); 10.393; 16.809; 11.592; 13.167; 13.678; 1.0283; 1.9365; 0.3927 | as above | PASS |
| QoQ and derived quarters: revenue -5.2%; core PBT +1.6%; FC -35.8%; Q1 FY26 131.06 / 3.98% / 1.48; H2 FY26 217.06 / 5.62% / 4.61 (3.73); H2 current tax (0.15); FG/WIP build 13.33; Q1 share of H1 draw 84.7% | as stated | 0.9476; 1.0161; 0.6423; 13,106.31 / 3.985% / 148.20; 21,706.24 / 5.623% / 461.18 (372.91); -14.57; -1,333.19; 1,598.10 / 1,885.91 = 84.74% | res L227-L251 | PASS |
| Per kg sold (Q1 / Q2 / H1): revenue; GP; opex; op EBITDA; materials per kg processed (H1) | 130.48 / 135.71 / 132.97; 29.56 / 31.31 / 30.39; 16.32 / 17.05 / 16.67; 13.23 / 14.26 / 13.72; 99.92 | same to 2 dp on 13,500 / 12,300 / 25,800 t and 24,600 t | call R013 R019 R020 L63, L70; res lines above | PASS |
| Revenue bridge Q1 to Q2 | volume -15.66; price +6.44; total -9.22 | -1,565.7; +643.5; -922.2 L vs filed 922.19 | res R012 R013 L225-227 | PASS |
| PAT bridge | +11.26, +4.58, -2.49 = 13.35; -0.08, -0.57, -0.23 = 12.47; -4.29; +1.22; = +9.40 | 1,125.9; 458.4; 249.42; 1,334.92; 7.85; 57.09; 22.73; 1,247.25; 429.38; 121.67; 939.54 L | res R081-R117 | PASS |
| After-tax attribution | 88.6% / -1.6% / 12.9% | 832.78 / -14.90 / 121.67 of 939.54 L | | PASS |
| Cash: CFO/PAT; ex-release; FCF; ex-release FCF; borrowing counterfactual | 15.76x / 1.19x; 0.09x; 19.84 / 19.53; -2.78; ~7.2 | 15.756 / 1.192; 0.0864; 1,983.64 / 1,952.86; -277.94; 717.87 L (ties to repayment 1,512.93 = 2,230.80 - 717.87) | res R279 R282 R254 R283 R284 R293-R299 L431-453 | PASS |
| WC change; swing | +23.33 / -6.76; -30.09 | 2,333.35 / -676.13 L | res R276 R253 R280 R252 L416-432 | PASS |
| Days: receivable (two bases); inventory; payable; CCC | 54.1 / 53.4 (57.1 / 55.2); 91.7 / 48.4; 11.0 / 7.8; 134.8 / 94.0 | 54.10 / 53.44 (57.12 / 55.21); 91.72 / 48.36; 10.99 / 7.80; 134.8 / 94.0 | res R178-R181 L312-314, R215-R218 L362-364 | PASS |
| Net debt; ND/E; land share of H1 fall | 82.56 / 67.23; 0.31 / 0.24; 78% | 8,255.62 / 6,722.88 L; 0.3139 / 0.2385; 1,201 / 1,532.74 = 78.4% | res R182-R185 R213 R214 R204 R205 | PASS |
| Implied FC rate H1 FY27 / FY26 | 7.9% / 5.0% | 603.68 / 7,621.78 = 7.92%; 369.66 / 7,339 = 5.04% | res R051 R052 R213 R214; deck R237 L521 | PASS on the stated basis (see M1 for the like-for-like H1 FY26 comparator) |
| ROCE H1 FY27 (op EBIT / PBT+FC); FY26; FY25 | 16.9% / 17.2%; 3.4%; 9.2% | 5,962.14 / 35,206.17 = 16.93%; 6,061.04 / 35,206.17 = 17.22%; 1,189.93 / 34,682.26 = 3.43%; 336 / 3,650 = 9.21% | res R204 R213 R206; deck R141 R137 R221 R237 | PASS |
| Run-rate and price facts | PAT 40.67 / 40.36 / 23.78; EPS 32.04 / 18.81; PE 21.1x / 35.9x; buyback 18.5% above CMP | as stated | res R115 R117 R114 R113 R148-R153; deck R309 L636 | PASS |
| Buyback and land | 47.4x / 186.9x / 25.0x; MTM 5.31 Cr; Rs 19,427 per sq m; 59.5% of H1 PAT | 800 / 16.88, 4.28, 32.04; 4,25,000 x 125; 12.01 Cr / 6,182; 12.01 / 20.18 | res R365 R368 R373 R375; deck R169 | PASS |
| Concall structure | Q&A 1,868 s = 84.3%; prepared 322 s = 14.5%; gaps 494 s = 22% of 2,217 s | 1,868 / 2,217 = 84.26%; 322 / 2,217 = 14.52%; 494 / 2,217 = 22.28% | call L96, L352, L24 | PASS |
| Concall scoring | 10/17 = 58.8%; specificity 4/30 = 0.13 (6/31 = 0.19); grades A6 B17 C10 D1 E3 ND3; C-E 14/37 = 37.8%; 3E tally 0/3/3/14; aspiration gap 449-749 bps; 1.05^4 / 1.10^4 = 21.6% / 46.4%; PBT margin 8.18% | all reproduced from the rev tables | rev L469-487, L592-633, L558-581 | PASS |
| **Hedge count (Role 5 Step 6C)** | **"we expect" row 4 (L88, L130, L186, L318); total 11 (9 excl. T046)** | **"we expect" row 5; total 12 (10 excl. T046)** | **call L238 (T057, MGMT): "obviously we can expect price realisation"** | **FAIL (F1)** |

F1 detail. A4's matching rule counts two negative forms as "we expect": "we don't expect" at call L186 (T043) and L318 (T085). By that rule, the management statement "we can expect" at L238 also counts. The "we expect" row becomes 5. The total becomes 12, or 10 excluding T046. The figure appears at rev L752, L755, L893, L1011, L1203 and L1210. The conclusion (over 5, hedge-heavy) does not change.

---

## 3. ADVERSARIAL READ

Selection. These are the three most positive claims in the review. Each counter is built from the same extracts.

**Claim 1. "The operating gain is real at the core-PBT level, and the call shows the spread per kg widened in Q2"** (rev L1020; L161; L210). Step 7 adds that the margin swing "does not disprove" the lowest-cost claim (rev L381).
- Strongest bear counter. The widened spread is set at import parity. The call text also says the parity setter has cheaper feedstock. At call L146-149 (T026), the question "is it that their raw material is cheaper than us" is followed by "okay because they are growing edible oil in the country itself whereas India is importing a large portion understood". This sits beside the 21 s gap R168 (call L147-148). The speaker is unclear: either a management answer or the analyst restating one. It is ASR-tier. Lower dumping has no stated cause (call L141). The freight cause is rejected: "Not from China to India" (L145). The export-incentive question goes unanswered (L142; gap R167).
- Survives? **Yes.** It is supported by the extract. A4 has the import-parity, cost-lag and Q3-squeeze points (rev L234, L249). A4 does not have L146-149. Row 10 summarises T026 only as "Chinese edible-oil duty; do alternate uses set raw-material price?" (rev L601). The text is also absent from Step 7 (rev L381) and from Competition "Where it is weaker" (rev L1088-1093). **Graft required (M3, MISSING, A4).** Carry the speaker caveat.

**Claim 2. "Stock timing (Reading 3) is the best-evidenced reading. Q2's 166.92 Cr is the clean run-rate. The demand concern softens"** (rev L218-219, L895, L1010).
- Strongest bear counter. Reading 3 explains the dip. It does not show that output grew. The duty-cut availability benefit is not visible in Q2 (call L104-106, R096). Neither is the "completed" throughput expansion (deck R382 R419 L95-98). Inventory is at the lowest of three dates (deck R197-R199 L521), so Q3 must run on fresh output alone.
- Survives? Yes. **Already incorporated** at rev L212 ("Commissioning run-rate test: not passed on volume"), L217 (Reading 2 open) and L219 ("no stock cushion"; "production volume is ND"). No graft needed. The same reading cuts the other way on management credibility. See C1.

**Claim 3. "The receivables build is growth-induced. Management's 'around 100 days' supports the derived 94 days over the deck's 128"** (rev L272, L282; also L564, L682, L795, L1003).
- Strongest bear counter. The derived 94.0-day CCC rests on inventory days of 48.4 (res R178 L312). That is a three-date low after a 22.31 Cr release that cannot repeat (res R254 L418; deck R197-R199 L521). The other two legs worsened. Receivable-minus-payable days went from 43.1 (54.1 - 11.0) to 45.6 (53.4 - 7.8), a 2.5-day lengthening [DERIVED, res R180 R181 L314, R215-R218 L362-364]. The deck's own CCC series lengthens every period: 76, 82, 99, 128 (deck R296-R299 L600-603, chart positions inferred). A4 cites only 99 and 128. Management's statement also points up: "between 90 to 100 days for domestic sales. For export sales it will elevate further" (call L213-214). The 94 days is a trough, not a run-rate. At the FY26 inventory level the cycle is 134.8 days, near the deck's 128.
- Survives? **Yes.** **Graft required (M4, MISSING, A4).** Add this qualifier wherever the review says the call "supports" the 94 days.

**Mandatory acquisition-economics probe.** The documents describe two purchases: the land RPT (res L67-70, Annexure B L582-621) and the share buyback (res Note 6 L521-536).
- Land RPT. Consideration Rs 12.01 Cr, plus stamp duty and registration at actuals (NOT FOUND) (res R373 R480 L588). **Price / target PAT = not applicable.** Land has no earnings stream. It adds no new earnings, because the company already uses it "in our operations as well as our worker colony" (call L205). No expansion plan exists (call L330, uncontested). So I test the price against carrying cost. Cash on hand is Rs 0.57 L (res R182 L315), so the purchase is borrowing-funded. At the H1 FY27 implied cost of 7.9% (rev L171), it costs about 0.95 Cr a year pre-tax [DERIVED: 12.01 x 7.92%]. After tax at 25.17% it costs about 0.71 Cr: about 1.8% of H1-annualised PAT of 40.36 Cr, or about Rs 0.56 per share on 125.96 L shares [DERIVED]. The deal is value-neutral only if the company already paid the promoter rent of about 0.95 Cr a year or more. Prior-use terms: NOT FOUND (A4 Q3). Counterparty interest: the CMD's interest is 6.07% "considering entities holding shares in which he is interested" (res R374 R481 L593). He receives 100% of the price and bears about 6% of the company's cost. About 94% of any overpayment falls on other holders. Quality markers: the land adjoins the single plant (res L69), which is the bull reading (it secures operating land). Against that, no valuer is named, no benchmark is given, and arm's length is self-asserted (res R483 L621). **Bear reading survives.** A4 has the price per sq m, the 59.5%-of-H1-PAT and 78%-of-net-debt-fall framings and the in-use fact (rev L80, L918, L1001). A4 lacks the 6.07% asymmetry and the carrying-cost break-even. **Graft required (M2, MISSING; orphan rows, so A3 then A4).**
- Buyback (own-share purchase). Rs 800 per share = 47.4x FY25 EPS of Rs 16.88 (deck R169 L500), 186.9x FY26 EPS of Rs 4.28 (res R150 L264), and 25.0x H1-annualised EPS of Rs 32.04 [DERIVED]. A4 states all three, plus the MTM loss of about 5.31 Cr (rev L1004). The funding question the review leaves open is answerable from the extract (M1). No further graft beyond M1.

---

## 4. INDEPENDENT READ: CONTRADICTIONS

**C1. Production "online" is scored CONTRADICTED by sold volume, against A4's own Reading 3.**
- The claim: "every quarter you are planning to increase the production by 5% ... So are we online to achieve that?" Answer: "Yes, yes, we are online" (call L162-164).
- A4 scores it contradicted, or failed, by sold volume of -8.9% QoQ at rev L537, L603, L650, L771, L790, L802, L870, L894, L1011 and L1203. The provisional EVASIVE lean rests on it (rev L771).
- A4's own Step 3 says the Q2 sold-volume fall is stock timing. Q1 sold a 15.98 Cr FG/WIP draw and Q2 a 2.88 Cr draw (rev L218; res R037 R038 L235). Step 3 also names "Q2 intake at or above Q1" as the observation that confirms Reading 3 (rev L220). That is the same observation that would support "online".
- The Step 4 cost-lag qualifier says the drawn stock was built cheap in H2 FY26 (rev L234). So the tonnage behind the 13.10 Cr smaller Q2 drawdown cannot be bounded from the extract. Netted for stock, Q2 output may be at, above or below Q1 output.
- Sold volume therefore cannot test a production claim this quarter. The correct status is UNVERIFIABLE on production (ND), not supported. The export half of the same claim is undercut by management's own words in the same answer: "Things are not moving as expected" (call L164-165). That basis stands.
- The EVASIVE lean can still rest on the refusals (rev L771 rows 5, 17, 30, 40) and the product slip. The "one checkable claim fails" sentence must go.
- Route: A4. The same bar applies to bear and bull claims (CLAUDE.md Rule J).

**C2. T075 classification and the question count.**
- A2 labels T075 (call L290-291) a moderator turn (ledger table 2). Its 45-turn question table omits T075 (ledger table 3), yet it lists R088 "Mr. Leiser" as an analyst at L291.
- A4 treats T075 as an analyst question (4A row 31, rev L622). It still says "45 question turns (A2 table 3), of which 39 are substantive" (rev L455) against a 40-row inventory (rev L633).
- Fix in A4: state 45 A2 question turns plus the L291 question inside moderator turn T075 = 40 substantive. The A2 relabel is a pipeline note (S6). It is not a separate loop.

---

## 5. FINDINGS BY TYPE

| ID | Type | Finding | Lines | Route |
|---|---|---|---|---|
| F1 | FACTUAL | Hedge count 11 should be 12 (10 excl. T046). "we expect" row omits the management "we can expect" (L238) while it counts the negative forms (L186, L318) | call L238; rev L752-755, L893, L1011, L1203, L1210 | A4 |
| M1 | MISSING | Orphan res R294. 30-Sep-2025 borrowings = about 54.4 Cr [DERIVED: deck R237 L521 63.0 Cr less res R294 L447 8.63 Cr; deck rounding +/-0.05 Cr]. H2 FY26 net borrowing = about +29.4 Cr, about 86% of the 34.00 Cr buyback. Deck p20 corroborates: H2 FY26 CFF = -27.9 - (-20.01) = -7.9 Cr, against +29.4 borrowing - 34.0 buyback - 2.1 interest = -6.7 Cr. Like-for-like H1 FY26 implied rate = about 5.5% (161.48 L x 2 / average 58.7 Cr), not the FY26 5.0% comparator. The finance-cost anomaly (A3P-20) is real but about 2.4 pp, not 2.9 pp | res R294 L447, R302 L454; deck R237 L521, R262-R269 L538-540; rev L171, L568, L933, L937, L1004, L1028, L1075 | A3, then A4 |
| M2 | MISSING | Orphan res R374/R481 (CMD 6.07% interest), plus the probe's carrying-cost break-even (about 0.95 Cr a year at 7.9%; prior rent NOT FOUND) | res R374 R481 L593; rev L80, L666, L917-918, L1001 | A3, then A4 |
| M3 | MISSING | Surviving counter to claim 1: call L146-149 (China's feedstock cheaper because it grows its own edible oil; speaker unclear, ASR) absent from 4A row 10, Step 7 and Competition | call L146-149; rev L601, L381, L861, L1088-1093 | A4 |
| M4 | MISSING | Surviving counter to claim 3: the 94-day CCC is an inventory trough. Ex-inventory the cycle is +2.5 days. Deck series 76-82-99-128 rises every period | res R178-R181 R215-R218; deck R296-R299 L600-603; call L213-215; rev L272, L282, L564, L682, L795, L1003 | A4 |
| C1 | CONTRADICTION | "Online" scored CONTRADICTED by sold volume while A4's own Reading 3 and cost-lag qualifier remove sold volume as a test of production | call L162-165; rev L218-220, L234; L537, L603, L650, L771, L790, L802, L870, L894, L1011, L1203 | A4 |
| C2 | CONTRADICTION | T075: A2 says moderator, A4 says question; A4 says 39 substantive against 40 rows | call L290-292; ledger tables 2-3; rev L455, L622, L633 | A4 (A2 relabel as pipeline note) |

---

## VERDICT

**INCOMPLETE.**
- Failing agents: **A3** for two orphan results rows (res R294; res R374/R481), MISSING. Then **A4** for F1 (FACTUAL), M1-M4 grafts (MISSING) and C1-C2 (CONTRADICTION).
- loop_back_to: **A3**. A3 scope: those two rows only. A4 then applies the fix list in the YAML gap field.
- No arithmetic error in any derived financial metric. The plain-language brief gate passes.
- By my read, none of the findings moves the PROCEED WITH FLAGS verdict. Each one changes a stated fact, count or conclusion, so none is STYLE.

---

## STYLE NOTES (logged, no loop)

- **S1. Coverage citation format.** 61 concall rows (listed in 1B), about 260 results rows and about 360 deck rows are covered only by line, turn or section anchors. None has an ID or an explicit "reviewed, no finding" line. Content is covered except for M1 and M2. Fix: add ID-range "reviewed, no finding" lines per ledger section.
- **S2. Forward map.** Item "Company-filed call transcript (M1)" carries no date in the brief (rev L1099). All other items are dated.
- **S3. "Trough" label.** Q2 FY26 is called "(trough)" in the revenue run-rate column (rev L187) and "the trough" (rev L174). It is the margin trough. The H2 FY26 average quarter revenue of 108.53 Cr (rev L190) was lower than Q2 FY26's 111.52 Cr. Numbers unchanged.
- **S4. Gap location.** "Most of the 494 s of gaps fall inside the Q&A" (rev L454). All 18 do: the first gap starts at 00:05:44 (call L100), after the Q&A opens at 00:05:23 (L96).
- **S5. Brief provenance.** "So feedstock supply follows India's edible-oil refining volume. It cannot grow faster than refining" (rev L1064) carries no INFERENCE tag. "Sold 12,300 tonnes in September" (rev L1052) should read "in the September quarter".
- **S6. Pipeline notes for the next A1/A2 pass.**
  - (a) Concall entity "crude oil prices" (call L157, analyst) is not captured. The review tags the crude-oil link INFERENCE (rev L688, L1066), though an analyst stated it on the call.
  - (b) Results auditor paragraph 1 (res L159) is not enumerated (3 vs 4).
  - (c) Possible unsplit speaker changes inside T024 (call L144) and T026 (call L148-149).
  - (d) Relabel T075 (C2).
- **S7. Dividend chart uncited.** Deck R319-R321 (L622-626: 75%, 75%, 10%; chart positions inferred) is uncited. The cut from Rs 7.5 to Rs 1.0 per share (FY25 dividend 976.57 L paid in H1 FY26, res R297 L450; FY26 dividend 125.31 L paid in H1 FY27, res R296 L450) sits beside the Rs 34 Cr buyback in the Flag 4 capital-allocation chain. Context only. Both cash figures are already in the review (rev L267, L287).

---

```yaml
stage: A5-adversary
company: "FAIRCHEMOR"
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
  orphan_rows:
    - "res R294 (L447): H1 FY26 net repayment of current borrowings (862.76) L; uncited; with deck R237 it derives the 30-Sep-2025 borrowings that the review lists as missing (rev L1028, Q9, Q19)"
    - "res R374 with qualifier R481 (L593): land counterparty CMD interest 6.07%; '6.07' appears nowhere in the review"
  missing_from_ledger:
    - "Logged, no A2 loop (content already in review; S6 / C2): concall entity 'crude oil prices' (call L157); results auditor para 1 (res L159); question at call L291 inside MOD turn T075"
arithmetic_mismatches:
  - {metric: "Role 5 Step 6C hedge count", a4_value: "'we expect' row 4 (L88, L130, L186, L318); total 11 (9 excl. T046)", recomputed: "'we expect' row 5 (adds MGMT 'we can expect', call L238, T057); total 12 (10 excl. T046)", source_line: "call L238; rev L752-755, L893, L1011, L1203, L1210"}
surviving_bear_counters:
  - {claim: "Operating gain real; spread per kg widened in Q2; margin swing does not disprove the lowest-cost claim (rev L1020, L210, L381)", counter: "Call T026 L146-149 (speaker unclear, beside 21 s gap R168, ASR): Chinese producers' raw material is cheaper because China grows its own edible oil while India imports. The import-parity ceiling is set by a rival with cheaper feedstock; lower dumping has no stated cause (L141); freight cause rejected (L145). Absent from 4A row 10 (rev L601), Step 7 (rev L381) and Competition (rev L1088-1093)", source_line: "call L146-149, L141, L144-145", type: MISSING}
  - {claim: "Management's ~100 days supports the derived 94-day CCC over the deck's 128 (rev L272, L282, L795)", counter: "94.0 days rests on inventory days at a three-date low (48.4) after the non-repeatable 22.31 Cr release; receivable-minus-payable days lengthened 43.1 to 45.6 (+2.5); deck CCC series 76, 82, 99, 128 lengthens every period; exports 'will elevate further' (call L214). The 94 is a trough, not a run-rate", source_line: "res R178-R181 L312-314, R215-R218 L362-364; deck R296-R299 L600-603; call L213-215", type: MISSING}
  - {claim: "Land RPT (acquisition probe): Rs 12.01 Cr for land adjoining the plant, already in company use (rev L80, L1001)", counter: "Price / target PAT not applicable (land; no new earnings; already used, call L205; no expansion plan, L330). Carrying cost at the H1 implied 7.9% = ~0.95 Cr/yr pre-tax, ~0.71 Cr after tax = ~1.8% of H1-annualised PAT 40.36 Cr; value-neutral only if prior rent >= ~0.95 Cr/yr (terms NOT FOUND). CMD interest 6.07%: he gets 100% of the price and bears ~6% of the cost; ~94% of any overpayment falls on other holders. No valuer; arm's length self-asserted", source_line: "res R373 L588, R374 R481 L593, R182 L315, R483 L621; call L205, L330", type: MISSING}
findings_by_type:
  factual:
    - "F1 (A4): hedge count 11 -> 12 (10 excl. T046); 'we expect' row omits MGMT 'we can expect' (call L238) while counting 'we don't expect' (L186, L318); conclusion unchanged"
  missing:
    - "M1 (A3 then A4): orphan res R294 L447. 30-Sep-2025 borrowings ~54.4 Cr [deck R237 63.0 less 8.63]; H2 FY26 net borrowing ~+29.4 Cr = ~86% of the 34.00 Cr buyback; like-for-like H1 FY26 implied rate ~5.5% vs A4's FY26 5.0% comparator (rev L171, L937). Amend Flag 4, brief L1075, Q9/Q19, missing-evidence list L1028"
    - "M2 (A3 then A4): orphan res R374/R481 L593 (CMD 6.07% interest) plus the probe's carrying-cost break-even; graft into Step 0D Board item 2 (rev L80), Exchange 3 (L666), Q3/Q4 (L917-918), Flag 1 (L1001)"
    - "M3 (A4): call L146-149 China cheaper-feedstock counter, speaker caveat; graft into 4A row 10 (rev L601), Step 7 strategic premium (L381), 8D (L861), Competition (L1088-1093)"
    - "M4 (A4): CCC qualifier: derived 94 days is an inventory trough; ex-inventory legs +2.5 days; deck series 76-82-99-128 rising; amend rev L272, L282, L564, L682, L795, L1003"
  contradiction:
    - "C1 (A4): 'online' (call L162-164) scored CONTRADICTED/failed by sold volume at rev L537, L603, L650, L771, L790, L802, L870, L894, L1011, L1203, while A4's Reading 3 (L218-220) attributes the sold-volume fall to stock timing and the cost-lag qualifier (L234) leaves the drawdown tonnage unbounded. Restate as UNVERIFIABLE on production; keep the export half (L164-165); re-base the EVASIVE lean on refusals and the product slip"
    - "C2 (A4): T075 (call L290-291) is MOD in A2 and absent from the 45-question table; A4 treats it as question row 31 (rev L622) but says 39 substantive (L455) against 40 rows (L633). State 45 + T075 = 40 substantive; A2 relabel is a pipeline note"
  style:
    - "S1: ID-level coverage format; 61 concall, ~260 results, ~360 deck rows covered only by line, turn or section anchors"
    - "S2: brief forward-map item M1 (transcript) undated (rev L1099)"
    - "S3: Q2 FY26 '(trough)' (rev L187) and 'the trough' (L174) is the margin trough only; H2 FY26 average quarter revenue 108.53 Cr was lower"
    - "S4: 'most of the 494 s of gaps' (rev L454) should be 'all'"
    - "S5: brief L1064 inference untagged; L1052 'in September' should be 'in the September quarter'"
    - "S6: pipeline notes for next A1/A2: 'crude oil' entity (call L157); auditor para 1 (res L159); possible unsplit speaker changes in T024 (L144) and T026 (L148-149); T075 relabel"
    - "S7: deck dividend chart R319-R321 (75%, 75%, 10%) uncited; cut from Rs 7.5 to Rs 1.0 per share sits beside the buyback in Flag 4"
loop_back_to: "A3"
gap: "A3: review two orphan results rows only: res R294 (L447, H1 FY26 net borrowing repayment 862.76 L) and res R374 with qualifier R481 (L593, CMD interest 6.07%). A4 then: (1) M1 derive 30-Sep-2025 borrowings ~54.4 Cr (deck R237 63.0 Cr less res R294 8.63 Cr) and the H2 FY26 rise ~29.4 Cr vs the 34.00 Cr buyback; amend Flag 4, brief L1075, Q9/Q19, missing-evidence list L1028, and the A3P-20 comparator (H1 FY26 ~5.5%, not FY26 5.0%); (2) M2 graft the land-RPT probe: 6.07% counterparty interest, ~0.95 Cr/yr carrying cost at 7.9%, rent break-even, terms NOT FOUND; (3) M3 graft call L146-149 into 4A row 10, Step 7, 8D and Competition, with the speaker caveat; (4) M4 qualify the 94-day CCC as an inventory trough (ex-inventory +2.5 days; deck 76-82-99-128); (5) C1 restate 'online' as UNVERIFIABLE on production at rev L537, L603, L650, L771, L790, L802, L870, L894, L1011, L1203 and re-base the EVASIVE lean; (6) F1 hedge count 12 (10 excl. T046) at rev L752-755, L893, L1011, L1203, L1210; (7) C2 question count 45 + T075 = 40 substantive (rev L455)."
style_notes:
  - "S1 coverage citation format: add ID-range 'reviewed, no finding' lines per ledger section"
  - "S2 date the transcript item in the brief forward map"
  - "S3 Q2 FY26 is the margin trough, not the revenue trough"
  - "S4 all 18 gaps fall inside the Q&A"
  - "S5 tag brief L1064 as INFERENCE; 'September quarter' at L1052"
  - "S6 next-run A1/A2 notes: crude oil entity L157, auditor para 1 L159, T024/T026 splits, T075 relabel"
  - "S7 dividend cut 75% to 10% (deck R319-R321) as Flag 4 context"
analyst_note: "Every derived metric in Steps 1 to 5 recomputes to rounding, including the PAT bridge, the per-kg table and the revenue bridge. The only number fix is the hedge count. The audit fails on completeness. Two results rows were never used. R294 answers the review's own open question on 30-Sep-2025 borrowings; with it, H2 FY26 net borrowing matches about 86% of the buyback. R374 gives the land seller's 6.07% stake, the core of the related-party economics. The adversarial read adds one bear point A4 missed: Chinese feedstock may be cheaper (call L146-149, speaker unclear). It adds one qualifier: the 94-day cycle is an inventory trough. The same bar runs the other way. A4's own stock-timing reading means sold volume cannot test the 'online' production claim, so 'contradicted' overstates it. By my read none of this moves PROCEED WITH FLAGS. Each item changes a stated fact or conclusion, so none is STYLE. The A3 loop covers two rows only; the A4 fix list is in the gap field."
```
