# A5 ADVERSARY / COMPLETENESS AUDIT: Poonawalla Fincorp Limited (POONAWALLA), Q2 FY27

Stage: A5-adversary | Model: claude-opus-5-5 | Audit date: 2026-10-17
Review under audit: runs/poonawalla-q2fy27/work/review_poonawalla_q2fy27.md (978 lines)
Inputs read: A1 fulltexts (results 1,765 lines; concall 1,093; presentation, 42 pages; press release 136), A1 structured files (row IDs by grep, key rows by grep), A2 ledgers (4), A4 review. Not opened: source PDFs, anything under inputs/, A3 forensics, orchestrator notes.
Anchor convention: "Rev L###" = A4 review line. "Res / Call / Deck / PR L###" = A1 fulltext line. "R###" = A1 structured row. [DERIVED] = my arithmetic on anchored numbers.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT (Rev L833-843, 10 lines, inside the 10-20 band) | sector PRESENT (Rev L845-851) | business model PRESENT (Rev L853-861) | competition PRESENT (Rev L863-868) | forward map PRESENT (Rev L870-883: a make-or-break reading with bull and bear forks, then 8 dated or undated catalysts, each with a bull and a bear fork).

Gate result: PASS. No part is empty or a placeholder.

---

## 1. COVERAGE AUDIT

Method. I re-ran the enumeration on the A1 fulltexts with my own grep passes and line reads, then diffed against the A2 ledgers. Row-ID totals come from a grep of `R### |` rows in each structured file.

| Document | Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | Structured rows | 1,327 | 1,327 (grep) | none | PASS |
| Results | Numbered notes | 27 (cons 10, stand 13, Annex II 4) | 27: cons 1]-10] (Res L473-516), stand 1]-13] (Res L832-966), Annex II 1-4 (Res L1751-1754) | none | PASS |
| Results | Unnumbered footnotes | 10 | 10: Res L226, 469, 828, 912, 963, 964, 1033, 1038, 1144, 1568 (L1474 "*" is a stamp artefact, L1115 and L1160 are table/signature bullets) | none | PASS |
| Results | Statement line items | 245 | 245: cons P&L 34, BS 35, CF 42; stand P&L 31, BS 35, CF 42 (= 219); Reg 52(4) 26 | none | PASS |
| Results | Zero-standing rows | 33 | 33: L239-240 (4), 296 (1), 311 (2), 424 (1), 582-583 (4), 648 (1), 663 (1), 782 (1), 876 (1), 890 (2), 958-960 (11), 993 (2), 996 (2) | none | PASS |
| Results | Agenda items | 11 | 11: approval lead-in, enclosures 1-6, investor presentation, board approvals 1-2, meeting times (Res L36-95) | none | PASS |
| Results | Annexure A items | 5 | 5 (Res L125-176) | none | PASS |
| Results | Auditor paragraphs | 25 | 25: cons LRR 1-7 (Res L197-257), stand LRR 1-6 (L549-608), certificate 1-12 (L1376-1515) | none | PASS |
| Results | Consolidation entities | 2 | 2: JASPL (Res L224), PFL Employee Welfare Trust (Res L580) | none | PASS |
| Results | Signature blocks | 6 | 6 by A2's definition (cover, two results, three auditor documents). Five further CFO/MD sign-offs on pp19-30 are carried as T7 rows (FN19_1051, ANX21_1158, ANX22_1213/1216, ANX29_1577/1584, ANX30_1762) | none | PASS (definitional) |
| Results | MISSING_FROM_STRUCTURED | 6 (M001-M006) | agree; the four conclusion and independence units are unanchored text | n/a | PASS |
| Concall | Structured rows | 287 | 287 (grep) | none | PASS |
| Concall | Speaker turns | 45 | 45: named-speaker grep, Call L88 to L1086 | none | PASS |
| Concall | Analyst questions | 10 | 10 (Suraj Das 3 incl. follow-up, Pranay Mehta 2, Abhijit Tibrewal 3, Avinash Singh 2) | none | PASS |
| Concall | Analyst turns | 13 | 13: Call L628, 709, 727, 736, 804, 815, 866, 924, 984, 994, 1018, 1057, 1073 | none | PASS |
| Concall | Participants | 11 | 11 (6 management incl. CS, moderator, 4 analysts; Call L71-80, L625-990) | none | PASS |
| Concall | NUMBER rows | 176 | 176 (grep) | none | PASS |
| Concall | Hedge hits | 80 | 80 (tally of ledger s6; "approximately" re-grepped = 10, see F1) | none | PASS |
| Presentation | Structured rows | 676 | 676 (grep) | none | PASS |
| Presentation | Slides | 42 | 42 `[page N]` markers | none | PASS |
| Presentation | NUMBER rows | 551 | 551 (grep) | none | PASS |
| Presentation | P&L + BS line items | 78 | 78: slide 26 has 14 lines x 3 periods (Deck L799-814), slide 27 has 12 x 3 (Deck L822-844) | none | PASS |
| Presentation | Footnotes / fine print | 20 | not fully recounted; sample (Deck L134, 206-207, 348, 394, 569, 651-652, 688, 750, 846, 1299) consistent | none | PASS (sampled) |
| Press release | Structured rows | 96 | 96 (grep) | none | PASS |
| Press release | Pages | 3 | 3 | none | PASS |
| Press release | NUMBER rows | 51 | 51 (grep) | none | PASS |
| Press release | Notes / footnotes | 0 | 0 | none | PASS |

Ledger-to-review accounting. A4 cites by ledger ID: all 27 notes and 10 footnotes (Rev L74-106), the auditor paragraphs and M004-M006 (Rev L110), AG2/AG3/AGT (Rev L468, L801), both entities (Rev L311), the Reg 52(4) lines it uses (Rev L287, L311), all 10 concall questions (Rev L578-587), the participant rows (Rev L455-464), M01 and M03 (Rev L616-617), and slides 6-8, 12-14, 20-27 and 40. Every remaining row falls under A4's explicit blanket marker (Rev L17: "All reviewed ... every A2 ledger row ... No ledger row is unreviewed"). I accept that marker as the "reviewed" mark.

Orphan rows: none. Missing from ledger: none.

Coverage caveat carried to Audit 3. One row group that sits only under the blanket marker carries a material fact: R390-R395, the deck's split of the fee line into Cross Sell Income and Servicing Income (Deck L802-803). A4 never cites R390-R392. I raise this as finding M1 (an unincorporated bear counter), not as an orphan, because the blanket marker covers it.

---

## 2. ARITHMETIC AUDIT

All values Rs crore unless stated. Every figure recomputed from the A1 fulltext.

| Metric | A4 value (Rev line) | Recomputed | Source line | Status |
|---|---|---|---|---|
| Core NII Q2 FY27 / Q1 FY27 / Q2 FY26 | 1,380.09 / 1,196.75 / 764.42 (L125) | 2,415.54-1,035.45; 2,118.40-921.65; 1,402.23-637.81 | Res L292, L301 | MATCH |
| Core NII FY26 / H1 FY26 / H1 FY27 | 3,374.14 / 1,403.67 / 2,576.84 (L125) | same method | Res L292, L301 | MATCH |
| Other income (total income less interest) Q2/Q1/Q2FY26 | 209.30 / 218.52 / 140.54 (L126) | 2,624.84-2,415.54; 2,336.92-2,118.40; 1,542.77-1,402.23 | Res L299 | MATCH |
| Rental + FV + other income, 6 columns | 1.83 / 8.78 / 3.27 / 18.26 / 6.44 / 10.61 (L129) | e.g. Q2: 0.95+0.54+0.34 | Res L293, L295, L298 | MATCH |
| NII incl. fees, 6 columns | 1,589.39 / 1,415.27 / 904.96 / 4,028.98 / 1,672.88 / 3,004.66 (L130) | core NII + other income | Res; Deck L808 | MATCH |
| Opex, 6 columns | 712.39 / 630.68 / 518.40 / 2,095.45 / 961.80 / 1,343.07 (L131) | employee + D&A + other | Res L304-306 | MATCH |
| PPOP, 6 columns | 877.00 / 784.59 / 386.56 / 1,933.53 / 711.08 / 1,661.59 (L132) | NII incl. fees less opex | derived | MATCH |
| Provisions, 6 columns | 375.70 / 373.33 / 287.67 / 1,209.92 / 528.75 / 749.03 (L133) | impairment + derecognition loss | Res L302-303 | MATCH |
| PPOP less provisions = PBT (6 columns) | ties (L143) | ties in all six | Res L308 | MATCH |
| Cost-to-income Q2 FY27 / Q1 / Q2 FY26 | 44.82% / 44.56% / 57.28% (L153) | 712.39/1,589.39; 630.68/1,415.27; 518.40/904.96 | derived | MATCH |
| Core NII / avg loans Q1 / Q2 | 8.11% / 8.38% (L152) | 4,787.00/59,045.2; 5,520.36/65,850.9 | Res L365; Deck L826 | MATCH |
| Credit cost computed Q1 / Q2 | 2.34% / 2.13% (L156) | 1,493.32/63,701; 1,502.80/70,531 | Deck L557-558 | MATCH |
| RoA computed Q1 / Q2 | 1.97% / 2.15% (L165) | 1,230.84/62,446.9; 1,499.40/69,603.1 | Res L736; Deck L834 | MATCH |
| RoE computed Q1 / Q2 | 10.5% / 11.2% (L166) | 1,230.84/11,678.8; 1,499.40/13,381.7 | Res L761; Deck L840-842 | MATCH |
| YoY growth set (interest income, NII, NII incl. fees, fees, opex, PPOP, finance cost, D&A, provisions, PBT, PAT, EPS, AUM, GNPA Rs) | +72.3 / +80.5 / +75.6 / +102.5 / +37.4 / +126.9 / +62.3 / +53.5 / +30.6 / +406.9 / +405.2 / +348.4 / +55.1 / +18.8% (L177-196) | each recomputed | Res L292-344; Deck L557-561, L713 | MATCH |
| Core PBT Q2 FY27 / Q1 FY27 / Q2 FY26 | 500.96 / 353.63 / 63.60 (L189, L213) | 501.30-0.34; 411.26-6.70-50.93; 98.89-0.47-34.82 | Res L296, L298, L308 | MATCH |
| Core PBT growth QoQ / YoY | +41.7% / +687.7% (L220, L189) | 500.96/353.63; 500.96/63.60 | derived | MATCH |
| ETR Q2 FY27 / Q2 FY26; ETR effect | 25.22% / 24.97%; 1.29 (L202, L240) | 126.45/501.30; 24.69/98.89; 126.45-501.30 x 24.967% | Res L308, L313 | MATCH |
| YoY PAT bridge | PBT +402.41; tax -100.47 and -1.29; PAT +300.65 (L231-242) | 615.67+103.71-34.82-0.13-193.99-88.70+0.67 = 402.41 | Res L292-314 | MATCH |
| QoQ PAT bridge | PBT +90.04; tax -22.90; PAT +67.14 (L248-257) | 183.34+48.07-50.93-6.36-81.71+7.20-9.57 = 90.04 | Res L292-314 | MATCH |
| Recurring share of YoY PBT change | 437.36 = 108.7% (L260) | (402.41+34.95)/402.41 | derived | MATCH |
| PAT at current-tax rate | 361.49, -3.6% (L263) | 501.30-139.81; 361.49/374.85-1 = -3.56% | Res L310 | MATCH |
| DTA roll | 91.16 (L263) | 72.70+24.33-6.28+0.41 | Res L371, L312, L329, L319 | MATCH |
| Note 11(c) derecognition gap | 26.03 (L264) | 29.33-(92.49-89.19) | Res L302, L906-908 | MATCH |
| Written-off pool vs impairment | 24.2% (L264) | 83.92/346.37 | Res L913, L303 | MATCH |
| Q1 ARC and written-off pools (H1 less Q2) | 5,826 / 118.90 / 54.29; 12,863 / 67.11 (L279-280) | 11,138-5,312; 280.50-161.60; 146.78-92.49; 23,421-10,558; 151.03-83.92 | Res L903-913 | MATCH |
| Stage 2 provision and release | ~116 to ~97; ~20 release (L275) | 650 x 17.90% = 116.35; 661 x 14.61% = 96.57 | Deck L704, L710 | MATCH |
| ECL stock and implied write-offs | ~891 to ~946; 290-320 a quarter (L281) | 350.68+116.35+424 = 891.0; 434.76+96.57+415 = 946.3; 346.37-55.3 = 291; 375.70-55.3 = 320 | Deck L703-714 | MATCH |
| D/E Jun-26 / Mar-26 / Sep-26 | 3.82x / 4.67x / 4.30x (L27, L287) | 49,866/13,060; 48,098.30/10,297.56; 58,865.41/13,703.39 = 4.296 | Deck L836-842; Res L745-747, L761, L989 | MATCH |
| QIP headroom used | 56% (L839) | 0.48/0.85 = 56.5% | derived | MATCH |
| Incremental debt and bank share | 10,767.11; 71.5% (L292) | 2,582.30+7,699.92+484.89; 7,699.92/10,767.11 | Res L389-391 | MATCH |
| QIP gross | 2,500.00 (L61) | 67,430,883 x 370.75 = Rs 2,500.0 cr | Res L497-498 | MATCH |
| Paid-up residual | 0.97 cr, ~4.87 m shares (L66) | 14.53-13.486-0.071 = 0.973; 0.973/2 = 0.487 cr shares | Res L339, L493, L497 | MATCH |
| Implied weighted shares | 87.79 / 78.11, +12.4% (L68) | 374.85/4.27; 74.20/0.95 | Res L314, L343 | MATCH |
| NIM computed on simple avg AUM | 9.01% (L704) | 6,357.56/70,531 | Deck L557-558 | MATCH |
| CoB computed | 7.62% (L284) | 4,141.80/54,365.5 | Deck L836 | MATCH |
| Ratio identity | 2.92% pre-tax; 2.18% post-tax (L709, L857) | (9.26-4.15-2.19) x (1-0.2522) = 2.184 | Call L596, L599, L603 | MATCH (evidential weight: see M4) |
| NCD pari-passu cover; headroom | 100.7%; 131.53 = 0.73% (L93) | 17,980.96/17,849.43; 17,980.96-17,849.43 | Res L1708, L1722 | MATCH |
| Annexure II cross-foot break | 68.04 (L428) | 939.30-871.26. Column 4,891.92 foots with 939.30; total 60,829.87 foots with 871.26 | Res L1729-1741 | MATCH |
| S vs C balance-sheet gap | 50.68 (L311) | 50.70-0.02; 13,754.07-13,703.39 | Res L379, L734, L997 | MATCH |
| Interest share of income; fee share of NII incl. fees | 92.0%; 13.1% (L854, L848) | 2,415.54/2,624.84; 207.47/1,589.39 | Res L292, L294, L299 | MATCH |
| Institutional holding | 27.67% (L379) | 11.75+11.64+4.28 | Deck L1279-1293 | MATCH |
| QoQ AUM run-rate Q3 FY26 to Q2 FY27 | +15.3 / +9.7 / +11.1 / +10.4% (L211-214) | 55,017/47,701; 60,348/55,017; 67,054/60,348; 74,008/67,054 | Deck L558-561 | MATCH |
| H2 FY26 tie-out | PAT 405.01 vs 405; PBT 541.28 vs 541 (L216) | 541.81-136.80; 723.61-182.33 | Res L308, L314 | MATCH |
| ALM net outflow 6-12 m / 3-5 Y | 5,538 / 4,461 (L424) | 9,384-3,846; 4,894-433 | Deck L644 | MATCH |
| Off-book gap Jun / Sep | 4,018 / 3,492 (L419) | 67,054-(61,523+650+863); 74,008-(69,010+661+845) | Deck L557-558, L703-713 | MATCH |
| Non-PAT equity Q2; trust sale vs H1 PAT | ~268; 33.4% (L422) | 13,703.39-13,060-374.85 = 268.54; 227.66/682.56 | Res L761, L451, L314 | MATCH |
| Q&A share of transcript | 46.7% (L471) | 470/1,006 | Call L88-1093 | MATCH |
| Quantified share of opening claims; specificity | 77.1%; 0.35 (L519, L676) | 27/35; 6/17 (register from A3, not re-derived) | derived | MATCH |
| Hedge breakdown, "approximately" | 9 (L680) | 10: Call L160, 163, 164, 179, 180, 193, 226, 254, 797, 1045 (all management turns) | Call fulltext; A2 concall ledger s6 | MISMATCH (F1) |
| EPS basic vs diluted spread | "0.01 to 0.02 in every period" (L68) | 0.00 to 0.02: Q2 FY26 0.95 / 0.95 and H1 FY26 1.76 / 1.76 have zero spread | Res L343-344 | MISMATCH (F2) |

Result: two mismatches, both minor counts or ranges. Neither changes a table conclusion. Both are FACTUAL by rule and ride the A4 loop.

---

## 3. ADVERSARIAL READ

Acquisition-economics probe: NOT TRIGGERED. No document describes an acquisition, purchase or stake buy. Loans acquired by assignment are NIL (Res L882-890). JASPL is a disposal (Res L509-513). The QIP is a capital raise (Res L497-500). A grep for acqui/stake/merger/amalgamation over all four fulltexts returns only marketing usage and management bios.

### Claim 1 (most positive). "Profits are real and rising. Q2 is the clean run-rate quarter. Core PBT rose 41.7% QoQ. The headline is real." (Rev L201, L261, L835, L842, flag 14 at L792, analyst note)

Strongest bear counter, from the same extract:
- (a) The fee line drove 53% of the QoQ PBT rise: +48.07 of +90.04 (Rev L249, L255) [DERIVED]. The deck splits that line in two (Deck L802-803; R390-R395). Cross Sell Income went 68 to 91 to 118 (+30% QoQ, +74% YoY). Servicing Income went 37 to 70 to 91 (+30% QoQ). Cross-sell income is the line most likely to carry third-party insurance commission. The deck does not split it further. Management conceded "the possibility of that fee compression" under the proposed insurance commission rule (Call L1060-1061). At 118 cr, cross-sell income equals 23.5% of Q2 PBT (118/501.30) and 7.4% of NII incl. fees [DERIVED]. Servicing income rose while the derived off-book pool shrank (Rev L419). A4 never cites the 118 cr line. Its brief and Q8 use the whole 207.47 cr fee line as the base and say the insurance share "is not disclosed" (Rev L848, L415).
- (b) The +41.7% also rests on rupee credit cost held flat (+0.6%) while simple-average AUM rose 10.7% (70,531/63,701). At Q1's computed ratio of 2.34%, Q2 credit cost would be about 413.4 cr (373.33 x 70,531/63,701). Core PBT would then be about 463.3 cr, +31.0% QoQ, and headline PBT about 463.6 cr, +12.7% QoQ [DERIVED from Res L302-303, L308; Deck L557-558]. A4 states the denominator effect (flag 2) but never ties it to the bull headline.

Survives: YES. Both parts rest on filed or deck numbers. Graft required (findings M1 and M2).

### Claim 2. "Asset quality GREEN: GNPA 1.37% to 1.20%, absolute 863 to 845 cr; GNPA improvement CONFIRMED QoQ." (Rev L271-272, L699)

Strongest bear counter, from the same extract:
- In the same quarter the company transferred 5,312 stressed accounts to ARCs: principal 161.60 cr, NBV 92.49 cr (Res L903-906). It also sold 10,558 written-off accounts (Res L912-914). GNPA fell by only 18 cr (Deck L713), about one-ninth of the stressed principal that left the book. Over H1, GNPA rose 27 cr (818 to 845) while 280.50 cr of stressed principal was transferred (Res L904).
- Note 11(c) does not state the asset classification of the loans at transfer. If they were Stage 3, pre-transfer GNPA would be about 1,006.6 cr (845 + 161.60). That is about 1.42% of gross staged assets plus transfers (1,006.6/70,677.6), up from 1.37%, not down to 1.20% [DERIVED; Deck L703-713].
- A4 reports the ARC channel as "AMBER: rising" (Rev L279). It never links that channel to the GNPA fall it rates GREEN.

Survives: YES, as a conditional counter. The transfer data are filed. The classification at transfer is the open fact. Graft required, plus a question on classification at transfer (finding M3).

### Claim 3. "The management ratio set is internally consistent: 9.26 - 4.15 - 2.19 = 2.92% pre-tax, 2.18% post-tax = disclosed RoA." (Rev L709 CONFIRMED; bull-side flag 14 at L792; brief L857 "matches the stated RoA")

Strongest bear counter, from the same extract:
- The check is an arithmetic identity. All three disclosed ratios back-solve to one denominator of about 68,650 cr: 6,357.56/9.26% = 68,656; 2,849.56/4.15% = 68,664; 1,502.80/2.19% = 68,621 [DERIVED]. Ratios that share a denominator must sum to PBT over that denominator. The check validates the denominator, not any input. A4's own Step 7A gives NIM 9.01% on simple-average AUM and rates the 9.26% "UNVERIFIABLE" (Rev L704).
- The identity carries the unproven credit cost straight into RoA. At Q1's 2.40% ratio, the same identity gives RoA (9.26-4.15-2.40) x 0.7478 = 2.03%. At Q2 FY26's 2.67%, it gives 1.82% [DERIVED; PR L83; Call L604].

Survives: YES. The bull-side flag carries no independent evidence. Graft a one-line qualifier (finding M4).

### Counters tested that do NOT survive (recorded for symmetry)
- "NIM expansion is QIP-funded equity, not spread." Fails. Equity as a share of total assets fell YoY (Sep-25 9,822/46,909 = 20.9%; Sep-26 13,703/74,533 = 18.4%) and QoQ (Jun-26 13,060/64,673 = 20.2%) [DERIVED; Deck L834-842; Res L736, L761]. Margin rose while the equity share fell.
- "YoY operating leverage is a DA-gain artefact." Fails. Excluding the 34.82 cr DA gain, Q2 FY26 cost-to-income is 518.40/870.14 = 59.6%, so the YoY gain to 44.82% is larger, not smaller [DERIVED; Res L296].

---

## FINDINGS (every finding tagged)

| ID | Type | Finding | Evidence | Fix | Loop |
|---|---|---|---|---|---|
| F1 | FACTUAL | Section B Step 6C gives "approximately 9" in the hedge breakdown. The fulltext and the A2 ledger give 10. The 80 total is right. | Call L160, 163, 164, 179, 180, 193, 226, 254, 797, 1045; Rev L680 | Change 9 to 10. The hedge-heavy conclusion stands. | A4 |
| F2 | FACTUAL | Step 0C says EPS basic vs diluted spread is "0.01 to 0.02 in every period". Two periods show zero spread. | Res L343-344 (Q2 FY26 0.95/0.95; H1 FY26 1.76/1.76); Rev L68 | Change to "0.00 to 0.02". | A4 |
| F3 | FACTUAL | The brief says "The audit firms changed after July 2026". The extract supports only that Kirtane & Pandit LLP is "one of the previous joint auditors". It does not say whether the other joint auditor changed. Step 0D wording ("the joint-auditor pair changed") is supported; the brief's plural is not. | Res L249-257, L598-607, L1425-1427; Rev L840 | Reword: "Kirtane & Pandit LLP left the joint-auditor pair after its 17 July 2026 review. Whether the other firm also changed is not stated." | A4 |
| M1 | MISSING | The deck's fee split is absent from the review. Cross Sell Income is 118 / 91 / 68 cr and Servicing Income 91 / 70 / 37 cr (Q2 FY27 / Q1 FY27 / Q2 FY26). Cross-sell income is the regulatory-exposed sub-line and equals 23.5% of Q2 PBT. Together the two lines supplied +48 of the +90.04 cr QoQ PBT rise. | Deck L802-803 (R390-R395); Call L1060-1061; Rev L249, L415, L848 | Graft into: brief part 2 (fee-risk bullet), Step 4 QoQ bridge (split the +48.07 into cross-sell +27 and servicing +21), Q8 (ask the insurance share of the 118 cr cross-sell income), and the claim-1 qualifier. | A4 |
| M2 | MISSING | The core-PBT +41.7% headline is not tied to its dependence on flat rupee credit cost. At Q1's computed credit-cost ratio, core PBT growth is about +31.0% and headline PBT growth about +12.7%. | Res L302-303, L308; Deck L557-558; Rev L220, L835 | Add the sensitivity next to the +41.7% in Step 3 and brief bullet 2, and to flag 14. | A4 |
| M3 | MISSING | GNPA is rated GREEN and "CONFIRMED QoQ" with no ARC-transfer qualifier. 161.60 cr of stressed principal went to ARCs in Q2 while GNPA fell 18 cr. If those loans were Stage 3 at transfer, pre-transfer GNPA was about 1,006.6 cr (about 1.42%). | Res L903-906, L912-914; Deck L703-713; Rev L271, L699 | Add the conditional qualifier to the Step 5L GNPA row, the Step 7A GNPA row and brief bullet 4. Add a question: asset classification of Q1 and Q2 ARC-transferred loans at transfer, and GNPA before transfers. | A4 |
| M4 | MISSING | Flag 14 lists the ratio-set consistency as bull-side evidence. It is an arithmetic identity on one company-chosen denominator (about 68,650 cr). It confirms no input and carries the unproven credit cost into RoA (2.03% at 2.40%; 1.82% at 2.67%). | Call L596, L599, L603-604; PR L83; Rev L704, L709, L792, L857 | Requalify the Step 7A row and flag 14: "arithmetic identity; no independent evidence". Add the RoA sensitivity. | A4 |
| S1 | STYLE | Brief part 3 book mix omits Machinery & Medical Equipment 1% and Professional Loan 1%. The listed shares sum to 97%. | Deck L386, L391; Rev L855 | Add the two lines. | none |
| S2 | STYLE | Brief part 5 calls the 5,538 cr "6-12 month debt maturities ... net". It is the fall in the cumulative structural gap (9,384 to 3,846), net of asset inflows, not gross debt maturities. | Deck L644; Rev L881 | Relabel as "net structural outflow". | none |
| S3 | STYLE | Collection efficiency stays ND under the A3 chart caveat, correctly. A positional read of slide 24 suggests 99.6% to 99.5% across the last two portfolio quarters. The mapping is unresolved, so it is not a fact. | Deck L731-745; Rev L160, L277 | Optional: add a question asking the company to state collection efficiency as a table. | none |

---

## VERDICT

VERDICT: INCOMPLETE.
- Failing agent: A4.
- Gap (MISSING): graft the three surviving bear counters before save. M1 (deck fee split: cross-sell income 118 cr, servicing income 91 cr, Deck L802-803). M2 (core PBT +41.7% falls to about +31% at Q1's credit-cost ratio). M3 (conditional GNPA counter: 161.60 cr stressed principal to ARCs in Q2, Res L903-906, plus a classification question). M4 (ratio-set check is an identity; RoA 2.03% at 2.40% credit cost).
- Gap (FACTUAL, minor, same pass): F1 hedge count 9 to 10; F2 EPS spread range 0.00 to 0.02; F3 auditor-change wording in the brief.
- No CONTRADICTION findings. No A2 or A3 loop: coverage is complete and no orphan row exists.
- Gate 0 (deliverable completeness), Audit 1 (coverage) and Audit 2 (arithmetic, apart from F1 and F2) pass. The protocol verdict PROCEED WITH FLAGS is not challenged. The grafts change how the bull flags read, not the verdict.

## STYLE NOTES (logged, no re-run)
- S1: add Machinery & Medical Equipment 1% and Professional Loan 1% to the brief's book mix (Deck L386, L391).
- S2: relabel the 5,538 cr in the forward map as a net structural outflow (Deck L644).
- S3: optional question asking for collection efficiency as a table (Deck L731-745 mapping unresolved).

---

```yaml
stage: A5-adversary
company: "POONAWALLA"
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
  - {metric: "Concall hedge breakdown, count of 'approximately' (Section B Step 6C)", a4_value: "9", recomputed: "10", source_line: "Call L160, L163, L164, L179, L180, L193, L226, L254, L797, L1045; A2 concall ledger s6"}
  - {metric: "EPS basic vs diluted spread range (Step 0C)", a4_value: "0.01 to 0.02 in every period", recomputed: "0.00 to 0.02 (Q2 FY26 0.95/0.95; H1 FY26 1.76/1.76)", source_line: "Res L343-344"}
surviving_bear_counters:
  - {claim: "Profits real and rising; Q2 clean run-rate quarter; core PBT +41.7% QoQ (Rev L201, L261, L835, L842, flag 14)", counter: "53% of the QoQ PBT rise (+48.07 of +90.04) came from the fee line; deck splits it into Cross Sell Income 91->118 and Servicing Income 70->91. Cross-sell income (118 cr = 23.5% of Q2 PBT) is the line exposed to the proposed insurance commission rule; A4 never cites it. At Q1's computed credit-cost ratio (2.34%) Q2 credit cost would be ~413.4 cr and core PBT growth ~+31% (headline ~+12.7%).", source_line: "Deck L802-803 (R390-R395); Call L1060-1061; Res L302-303, L308; Deck L557-558", type: MISSING}
  - {claim: "Asset quality GREEN: GNPA 1.37%->1.20%, absolute 863->845 cr, CONFIRMED QoQ (Rev L271, L699)", counter: "Same quarter: 5,312 stressed accounts, principal 161.60 cr (NBV 92.49), transferred to ARCs, plus 10,558 written-off accounts sold. GNPA fell only 18 cr. Classification at transfer undisclosed; if Stage 3, pre-transfer GNPA ~1,006.6 cr (~1.42%), up from 1.37%. H1: GNPA +27 cr vs 280.50 cr transferred.", source_line: "Res L903-906, L912-914; Deck L703-713", type: MISSING}
  - {claim: "Management ratio set internally consistent: 9.26-4.15-2.19 = 2.92% pre-tax, 2.18% post-tax = disclosed RoA (Rev L709, L792, L857)", counter: "Arithmetic identity: all three ratios back-solve to one denominator (~68,650 cr), so they must sum to PBT over it; no input is validated (A4's own NIM check is 9.01%, UNVERIFIABLE). The identity carries the unproven credit cost into RoA: 2.03% at Q1's 2.40%, 1.82% at Q2 FY26's 2.67%.", source_line: "Call L596, L599, L603-604; PR L83; Rev L704", type: MISSING}
findings_by_type:
  factual:
    - "F1: Section B Step 6C hedge breakdown says 'approximately' 9; fulltext and A2 give 10 (Call L160-1045). Fix to 10."
    - "F2: Step 0C says EPS basic-diluted spread is 0.01 to 0.02 in every period; Q2 FY26 and H1 FY26 are 0.00 (Res L343-344). Fix to 0.00 to 0.02."
    - "F3: Brief says 'The audit firms changed'; extract supports only that Kirtane & Pandit LLP is a previous joint auditor, not whether the other firm changed (Res L249-257, L598-607, L1425-1427). Reword."
  missing:
    - "M1: Deck fee split absent: Cross Sell Income 118/91/68 and Servicing Income 91/70/37 cr (Deck L802-803, R390-R395). Graft into brief part 2, Step 4 QoQ bridge, Q8 and the claim-1 qualifier."
    - "M2: Core PBT +41.7% QoQ not tied to flat rupee credit cost; ~+31% at Q1's computed ratio (Res L302-303, L308; Deck L557-558). Graft into Step 3, brief bullet 2, flag 14."
    - "M3: GNPA GREEN without ARC qualifier; 161.60 cr stressed principal to ARCs in Q2 vs GNPA -18 cr; conditional pre-transfer GNPA ~1.42% (Res L903-906; Deck L703-713). Graft into Step 5L, Step 7A, brief; add classification-at-transfer question."
    - "M4: Ratio-set consistency (flag 14, Step 7A) is an arithmetic identity on one denominator (~68,650 cr); RoA 2.03% at 2.40% credit cost. Requalify and add sensitivity."
  contradiction: []
  style:
    - "S1: Brief book mix omits Machinery & Medical Equipment 1% and Professional Loan 1% (Deck L386, L391)."
    - "S2: Forward map calls 5,538 cr '6-12 month debt maturities'; it is the net structural outflow, cumulative gap 9,384 to 3,846 (Deck L644)."
    - "S3: Collection efficiency correctly ND under the chart caveat; optional question asking for a CE table (Deck L731-745)."
loop_back_to: "A4"
gap: "MISSING: graft three surviving bear counters before save. M1 deck fee split (cross-sell income 118 cr, servicing 91 cr, Deck L802-803) into brief part 2, Step 4 QoQ bridge and Q8. M2 core PBT +41.7% is ~+31% at Q1's credit-cost ratio. M3 conditional GNPA counter (161.60 cr stressed principal to ARCs in Q2, Res L903-906) plus a classification-at-transfer question. M4 ratio-set check is an identity; RoA 2.03% at 2.40% credit cost. FACTUAL (same pass): F1 hedge count 9->10; F2 EPS spread 0.00 to 0.02; F3 auditor-change wording in the brief."
style_notes:
  - "S1: add Machinery & Medical Equipment 1% and Professional Loan 1% to the brief book mix (Deck L386, L391)."
  - "S2: relabel the 5,538 cr as a net structural outflow (Deck L644)."
  - "S3: optional question asking for collection efficiency as a table (Deck L731-745)."
analyst_note: "Coverage and arithmetic are clean. Every count I re-derived from the fulltexts matches A2: 27 notes, 10 footnotes, 245 line items, 45 turns, 10 questions, 42 slides, 3 release pages, 2,386 rows. About 50 A4 derived figures recompute exactly, including both PAT bridges, the ECL-stock identity and the Annexure II break. The audit fails on the adversarial read. A4 never cites the deck's fee split (cross-sell 118 cr, servicing 91 cr), so its insurance-commission risk runs on the wrong base. Its clean-quarter headline also hides that 53% of the QoQ PBT rise came from those two lines. GNPA is rated GREEN with no note that 161.60 cr of stressed principal went to ARCs that quarter. The classification at transfer is undisclosed, so that counter is conditional. The ratio-set check A4 lists as bull evidence is an arithmetic identity. Three minor factual fixes ride the same pass. None of this changes PROCEED WITH FLAGS. It changes how the bull flags read. The acquisition probe was not triggered: no purchase or stake buy is described."
```
