# A5 ADVERSARY / COMPLETENESS RE-AUDIT (LOOP 1): Poonawalla Fincorp Limited (POONAWALLA), Q2 FY27

Stage: A5-adversary | Model: claude-opus-5-5 | Audit date: 2026-10-17
Review under audit: runs/poonawalla-q2fy27/work/review_poonawalla_q2fy27.md (1,002 lines; correction loop iteration 1, Rev L8)
Prior audit (run 1, kept intact): runs/poonawalla-q2fy27/work/audit_poonawalla_q2fy27.md
Inputs read: A1 fulltexts (results, concall, presentation, press release), A1 structured files (row grep and targeted rows), A2 ledgers (4), A4 review, run-1 audit. Not opened: source PDFs, anything under inputs/, A3 forensics, orchestrator notes.
Anchor convention: "Rev L###" = A4 review line. "Res / Call / Deck / PR L###" = A1 fulltext line. "R###" = A1 structured row. [DERIVED] = my arithmetic on anchored numbers. [INFERENCE] = reasoning, not a disclosed fact.

---

## R. RUN-1 FINDINGS: RESOLUTION CHECK

| Run-1 ID | Type | Where applied (Rev line) | Re-checked against | Status |
|---|---|---|---|---|
| F1 hedge "approximately" 9 to 10 | FACTUAL | L689 | Call grep: 10 hits at L160, 163, 164, 179, 180, 193, 226, 254, 797, 1045; A2 concall ledger s6 L374-383 | RESOLVED |
| F2 EPS spread 0.00 to 0.02 | FACTUAL | L71 | Res L343-344: spreads 0.01 / 0.01 / 0.00 / 0.02 / 0.00 / 0.02 | RESOLVED |
| F3 auditor-change wording | FACTUAL | L852 (brief) | Res L249-257: Kirtane & Pandit LLP "one of the previous joint auditors", reports dated 17 July 2026 and 05 May 2026; current signers MSKA & Associates LLP and B. K. Khare & Co. (Res L259-260) | RESOLVED |
| M1 deck fee split | MISSING | L19, L254-255, L264, L272, L423, L645, L803, L830, L860, L895 | Deck L802-803; R390-R395 (structured L398-403) | RESOLVED on numbers. New finding FL1-1 on the evidence tier of one sentence that came from my run-1 wording |
| M2 credit-cost sensitivity of +41.7% | MISSING | L224, L268, L710, L780, L801, L846 | Res L302-303, L308; Deck L557-558; PR L83 | RESOLVED |
| M3 GNPA ARC-transfer qualifier | MISSING | L100, L279, L287, L442 (Q27), L708, L780, L802, L849 | Res L903-914; Deck L703-718 | RESOLVED as instructed. A4 improved my counter with a like-for-like test (1.55% to 1.42%). New findings ML1-1 and ML1-2: the graft leaves out filed evidence on classification and does not reach NNPA or the Step 7 pillar row |
| M4 ratio-set identity | MISSING | L718, L801, L869 | Call L186, L596, L599, L603-604; PR L83 | RESOLVED |

Run-1 style notes S1-S3 were not applied (Rev L8). That is allowed. They stay logged below.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT (Rev L844-855, 11 bullet lines, inside 10-20) | sector PRESENT (Rev L857-863) | business model PRESENT (Rev L865-873) | competition PRESENT (Rev L875-880) | forward map PRESENT (Rev L882-895: make-or-break reading with bull and bear forks, then 8 catalyst lines, each with a bull and a bear fork; the undated line carries two catalysts, each forked).

Gate result: PASS. No part is empty or a placeholder.

---

## 1. COVERAGE AUDIT

Method. Fresh grep passes on the A1 fulltexts and structured files this run. I diffed them against the A2 ledgers (count-test headers unchanged since run 1: results L7-19, concall L4-19, presentation L1-13, press release L2-14). Items marked "carried" were not re-grepped this run. Their ledger counts are unchanged and run 1 verified them line by line.

| Document | Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | Structured rows | 1,327 | 1,327 (grep `^R### \|`) | none | PASS |
| Results | NUMBER rows | n/a in header | 975 (grep) | none | info |
| Results | Numbered notes | 27 | 27: cons 1]-10] Res L473-516 (10] OCR "I OJ" L516); stand 1]-13] Res L832-966 ("I]" L832, "I OJ" L862, "I !]" L868); Annex II 1-4 Res L1751-1754 | none | PASS |
| Results | Unnumbered footnotes | 10 | 10: Res L226, 469, 828, 912, 963, 964, 1033, 1038, 1144, 1568. Excluded: L1115, L1160 (table and date bullets), L1474, L1755 (stamp artefacts) | none | PASS |
| Results | Statement line items | 245 | carried (run 1: 219 + 26) | none | PASS (carried) |
| Results | Zero-standing / agenda / Annex A / auditor paras / entities / signatures | 33 / 11 / 5 / 25 / 2 / 6 | carried (run 1, line-level) | none | PASS (carried) |
| Results | MISSING_FROM_STRUCTURED | 6 | carried | n/a | PASS |
| Concall | Structured rows | 287 | 287 (grep) | none | PASS |
| Concall | NUMBER rows | 176 | 176 (grep) | none | PASS |
| Concall | Speaker turns | 45 | 45 (named-speaker grep). Generic label grep gives 48; the 3 extras are header lines L25, L34, L71 | none | PASS |
| Concall | Analyst turns | 13 | 13: Call L628, 709, 727, 736, 804, 815, 866, 924, 984, 994, 1018, 1057, 1073 | none | PASS |
| Concall | Questions / participants | 10 / 11 | carried | none | PASS (carried) |
| Concall | Hedge "approximately" | 10 (ledger s6) | 10 (grep) | none | PASS |
| Presentation | Structured rows | 676 | 676 (grep) | none | PASS |
| Presentation | NUMBER rows | 551 | 551 (grep) | none | PASS |
| Presentation | Slides | 42 | 42 `[page N]` markers | none | PASS |
| Presentation | P&L + BS line items | 78 | 78 (slide 26 Deck L799-814, 14 x 3; slide 27 Deck L822-844, 12 x 3) | none | PASS |
| Presentation | Fee split rows | in ledger | R390-R395 (Deck L802-803) now cited explicitly (Rev L19, L254-255) | none | PASS |
| Press release | Structured rows / NUMBER / pages / notes | 96 / 51 / 3 / 0 | 96 / 51 / 3 / 0 | none | PASS |

Total structured rows 2,386 (1,327 + 287 + 676 + 96). This matches A2 and Rev L18.

Ledger-to-review accounting. A4 keeps its blanket "every A2 ledger row ... reviewed" marker (Rev L18). It now cites R390-R395 explicitly (Rev L19). Loop 1 added no ledger rows. Q27 (Rev L442) cites NS11c lines Res L903-906. Orphan rows: none. Missing from ledger: none. The acquisition probe trigger was re-run: a grep for acqui|stake|merger|amalgamat|takeover over the four fulltexts returns only note 11(b) "acquired through assignment" (NIL, Res L882-890), marketing usage and bios. Probe NOT TRIGGERED.

Coverage-adjacent factual finding (FL1-2). Note ANXII-N3 is in the ledger and cited, but A4 misreads it. Rev L106 calls it a "Column-reporting note". The filed text says "Book value represents principal and interest accrued of all secured NCD's issued by the company" (Res L1753; R1326). Run 1 missed this.

---

## 2. ARITHMETIC AUDIT

Every [LOOP-1] figure recomputed from the A1 fulltexts. Rs crore unless stated.

| Metric (Rev line) | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Simple-average AUM Q1 / Q2; growth (L224) | 63,701 / 70,531; +10.7% | (60,348+67,054)/2; (67,054+74,008)/2; 70,531/63,701 = 1.1072 | Deck L557-558 | MATCH |
| Q2 credit cost at Q1 computed ratio (L224) | 413.36 | 373.33 x 70,531/63,701 = 413.36 | Res L302-303 | MATCH |
| Core PBT and growth at that cost (L224, L801) | 463.30, +31.0% | 500.96 - 37.66 = 463.30; /353.63 = 1.3101 | Res L296, L298, L308 | MATCH |
| Headline PBT at that cost (L224, L801) | 463.64, +12.7% | 501.30 - 37.66; /411.26 = 1.1274 | Res L308 | MATCH |
| Disclosed-ratio variant (L224) | 411.73; core +31.5%; headline +13.1% | 375.70 x 2.40/2.19 = 411.73; 464.93/353.63 = 1.3147; 465.27/411.26 = 1.1313 | PR L83 | MATCH |
| Share of +41.7% from flat rupees (L224) | 10.7 of 41.7 pts, about a quarter | 41.7 - 31.0 = 10.7; 25.7% | derived | MATCH |
| Fee line share of QoQ PBT rise (L268, L803) | 53.4% / 53% | 48.07/90.04 = 53.39% | Res L294-295, L293 | MATCH |
| Cross-sell growth QoQ / YoY (L272, L423, L860) | +29.7% / +73.5% | 118/91 = 1.2967; 118/68 = 1.7353 | Deck L802 | MATCH |
| Cross-sell / Q2 PBT; / NII incl. fees (L272, L803, L860) | 23.5%; 7.4% | 118/501.30 = 23.54%; 118/1,589.39 = 7.42% | Deck L802; Res L308 | MATCH |
| Cross-sell share of QoQ PBT rise (L272) | 30.0% | 27/90.04 = 29.99% | derived | MATCH |
| Servicing growth QoQ / YoY; / Q2 PBT; share of rise (L272) | +30.0% / +145.9%; 18.2%; 23.3% | 91/70; 91/37 = 2.4595; 91/501.30; 21/90.04 | Deck L803 | MATCH |
| Deck sub-lines vs filed line (L264, L272) | 209 / 161 / 105 vs 208.96 / 160.89 / 105.25 | 207.47+0.95+0.54; 158.81+1.64+0.44; 102.45+2.77+0.03 | Res L293-295 | MATCH |
| Pre-transfer GNPA Q2 and ratio (L279, L708, L802, L849) | 1,006.6; 70,677.6; 1.42% | 845+161.60; (69,010+661+845)+161.60; 1.4242% | Res L904; Deck L703-713 | MATCH |
| Like-for-like Q1 pre-transfer (L279, L442) | 981.9 / 63,154.9 = 1.55%; rupees +2.5% | 863+118.90; (61,523+650+863)+118.90; 1,006.6/981.9 = 1.0252 | Res L904 (H1 less Q2); Deck L703-713 | MATCH |
| ARC principal QoQ (L287) | +35.9% | 161.60/118.90 = 1.3591 | Res L904 | MATCH |
| Written-off pool consideration QoQ (L288) | +25.0% | 83.92/67.11 = 1.2505 | Res L912-913 | MATCH |
| Ratio identity denominators (L718) | 68,656 / 68,664 / 68,621 | 6,357.56/0.0926; 2,849.56/0.0415; 1,502.80/0.0219 | Call L186, L596; PR L83 | MATCH |
| RoA at 2.40% / 2.67% (L718, L801, L869) | 2.03% / 1.82% | 2.71 x 0.7478 = 2.0265; 2.44 x 0.7478 = 1.8246 | PR L83; Call L604; Res L308, L313 | MATCH |
| EPS spread (L71) | 0.00 to 0.02 | see R table | Res L343-344 | MATCH |
| Hedge "approximately" (L689) | 10 | 10 | Call grep | MATCH |

Untagged figures. Run 1 recomputed about 50 derived figures and all matched apart from F1 and F2. I re-checked eight untagged figures this run and all matched: core NII 1,380.09 (Res L292, L301); opex 712.39 (Res L304-306); PPOP 877.00; cost-to-income 44.82%; ETR 25.22% (Res L308, L313); PPOP / NII incl. fees 42.72% to 55.18%; QoQ opex +12.96% vs NII incl. fees +12.30%; D/E 4.296 (Res L989 inputs).

Result: no arithmetic mismatch.

---

## 3. ADVERSARIAL READ (fresh, on the post-loop review)

Acquisition-economics probe: NOT TRIGGERED (see Audit 1).

### Claim 1. "Profits are real and rising ... Core profit growth is real at either ratio." (Rev L224, L782, L854)
Bear counters tested against the extract:
- Flat rupee credit cost and fee concentration. Both are now grafted (M1, M2) at L224, L268, L854. They need no further graft.
- Stage 2 provision release of about 20 cr (Deck L704, L710). This is one of the mechanisms behind the flat rupee credit cost, so the M2 sensitivity already covers it. Stacking it would credit one effect twice. Rejected.
- Possible netting of the 83.92 cr written-off pool consideration inside impairment (Res L912-913). This cuts toward the bull on growth. Ex-netting, core PBT would be 500.96 - 83.92 = 417.04 vs Q1 353.63 - 67.11 = 286.52, +45.6% [DERIVED]. The bear point is about the level, and flag 5 and Q3 already carry it.
Survives as a new graft: NO. The claim now carries its qualifiers.

### Claim 2. "GNPA 1.37% to 1.20% ... GREEN on the reported ratio; AMBER-CONDITIONAL on ARC classification" and "NNPA GREEN on ratio; absolute 439 to 430" (Rev L279-280, L303, L384, L708, L849)
Strongest bear counter, from the same note the graft cites:
- Note 11(c) gives net book value at transfer next to principal. In Q2: NBV 92.49 against principal 161.60 (Res L904-906). That implies ECL cover at transfer of 1 - 92.49/161.60 = 42.8% [DERIVED]. For Q1 (H1 less Q2): 1 - 54.29/118.90 = 54.3%. For H1: 1 - 146.78/280.50 = 47.7% [DERIVED].
- Compare the deck's staged cover: Stage 3 PCR 49.11% (Jun) and 49.14% (Sep); Stage 2 PCR 17.90% and 14.61%; Stage 1 PCR 0.57% and 0.63% (Deck L709-718). The transfer pools carry Stage 3-level cover, about three times the Stage 2 cover.
- The Q2 pool's weighted residual tenor is 77 months (Res L905). That points to long-tenor lines such as LAP (3-15Y, 9.75-12% ROI, Deck L363), where Stage 2 cover would be low. A 43% haircut on such a pool is a Stage 3-type haircut [INFERENCE].
- Reading: the classification is still not disclosed. The Stage 3 reading is better evidenced [INFERENCE]. The Q27 bull answer "Mostly Stage 2 or SMA at transfer" (Rev L442) runs against the filed cover. On the better-evidenced reading, the reported rupee GNPA fall (863 to 845, -2.1%) is a transfer effect, and pre-transfer GNPA rose 2.5% (981.9 to 1,006.6). The like-for-like ratio still falls, 1.55% to 1.42%, so the bull holds on the ratio.
- NNPA carries the same mechanism and no qualifier. If the loans were Stage 3, pre-transfer NNPA was 430 + 92.49 = 522.49 in Q2 vs 439 + 54.29 = 493.29 in Q1. That is +5.9% in rupees against the reported -2.1%. The like-for-like ratio falls 0.79% to 0.74% [DERIVED]. Denominator: gross staged assets less Stage 3 provision. That basis reproduces the reported 0.70% (439/62,612) and 0.61% (430/70,101), and the NBV transferred is added back.
- The Step 7 pillar row for /fttcp (Rev L384) gives "GNPA 1.20%, NNPA 0.61%" with no qualifier. The Step 5L flag list (Rev L303) qualifies GNPA but not NNPA.
Survives: YES. Graft required (ML1-1, ML1-2).

### Claim 3. Earnings quality: "recurring pre-tax drivers sum to +437.36 ... 108.7% of the PBT change"; Q2 "the clean run-rate quarter"; the servicing-income sub-line tagged "Recurring" (Rev L255, L267-268)
Strongest bear counter:
- Servicing income rose 70 to 91 while its natural base, the derived off-book gap (AUM less gross staged assets), fell 4,018 to 3,492 (Deck L557-558, L703-713). The implied annualised servicing yield on that gap is 280 / avg(3,549; 4,018) = 7.4% in Q1 and 364 / avg(4,018; 3,492) = 9.7% in Q2. Q2 FY26 was about 5.0% (148 / 2,970, period-end, because Jun-25 is ND) [DERIVED]. A servicing fee near 10% a year on the pool it services is not plausible, so the line's nature is ND and its recurrence unproven [INFERENCE].
- Test: exclude all +54 of YoY servicing growth from the recurring drivers. Recurring drivers are then 383.36 = 95.3% of the +402.41 PBT change [DERIVED]. Core NII (+615.67) dominates. The conclusion holds.
- A4 already puts the anomaly in the same cell (L255) and in Q12 (L427).
Survives: PARTIALLY. It does not change a number, the conclusion or the verdict, so no graft is required. It is logged as style note SL1-3.

### Symmetry check (Rule J): a correction in the bull direction
My run-1 M1 called cross-sell income "the regulatory-exposed sub-line" as a fact. The extract does not define Cross Sell Income (Deck L802 is a bare label). Management uses "cross-sell" for selling other loans to existing customers: "cross-sell of other loans" (Call L244-245) and the "multi-product cross-sell engine" of lending products (Call L298-307). The insurance-commission exposure on the 118 cr line is therefore an inference, not a filed fact. A4 tags it [INFERENCE] once (L272) but states it as fact in the brief, flag 16, 5A and M20. This is finding FL1-1. Fixing it reduces the stated bear exposure, which is the correct direction.

---

## FINDINGS (every finding tagged)

| ID | Type | Finding | Evidence | Fix (graft text, A4) | Loop |
|---|---|---|---|---|---|
| ML1-1 | MISSING | The GNPA graft calls the ARC-transfer classification a plain "ND" conditional. It leaves out the filed cover evidence from the same note. Implied ECL cover at transfer is 42.8% in Q2 and 54.3% in Q1, at the 49% Stage 3 PCR level and about three times the 14.6-17.9% Stage 2 PCR. The Q2 residual tenor of 77 months points to long-tenor secured lines. The Stage 3 reading is better evidenced [INFERENCE]. On it, rupee GNPA rose 2.5% before transfers. The ratio still falls like-for-like. | Res L904-906, L905; Deck L363, L709-718; Rev L100, L279, L442, L708, L802, L849 | GNPA row L279: add "Classification ND; filed NBV implies 42.8% ECL cover at transfer (Q1 54.3%), at Stage 3 PCR 49.1% vs Stage 2 PCR 14.6%; the Stage 3 reading is better evidenced [INFERENCE]: rupee GNPA +2.5% pre-transfer, ratio like-for-like 1.55% to 1.42% [DERIVED]". Carry it to L100, L708, flag 15 (L802), the Q27 bull and bear cells (L442) and brief L849, adding the like-for-like comparator to the brief. Q27 stays. | A4 |
| ML1-2 | MISSING | The M3 qualifier stops at GNPA. The NNPA row (L280 "GREEN on ratio; absolute 439 to 430"), the Step 5L flag list (L303 "NNPA 0.61%") and the Step 7 Asset-Quality Multiplier pillar row (L384 "GNPA 1.20%, NNPA 0.61%") carry no ARC qualifier. If Stage 3: pre-transfer NNPA 493.29 to 522.49 (+5.9%) vs the reported -2.1%; like-for-like ratio 0.79% to 0.74%. | Res L904-906; Deck L713-716; Rev L280, L303, L384 | Add the conditional qualifier and the derived NNPA figures to L280, L303 and L384. The pillar row feeds /fttcp, so it needs the same qualifier as L303's GNPA entry. | A4 |
| FL1-1 | FACTUAL | "Cross-sell income is the line exposed to the rule" is stated as fact. The extract does not define Cross Sell Income, and management uses "cross-sell" for loan cross-sell. The exposure on the 118 cr line is an inference. A4 tags it [INFERENCE] only at L272. The error starts in my run-1 M1 wording. | Deck L802; Call L244-245, L298-307, L1060-1061; Rev L272 (last sentence), L645, L803, L830, L860, L895, L975, L996 | Tag [INFERENCE] at each site. Reword to "most likely exposed base: cross-sell income 118 cr; insurance share ND; a second reading is that the line also carries loan-related cross-sell fees". Keep Q8. | A4 |
| FL1-2 | FACTUAL | Step 0D row ANXII-N3 says "Column-reporting note". Filed note 3: "Book value represents principal and interest accrued of all secured NCD's issued by the company." This existed before the loop, and run 1 missed it. | Res L1753; R1326; Rev L106 | Row: subject "NCD book value basis"; says "Secured NCD book value = principal plus accrued interest"; impact "cover denominator includes accrued interest". | A4 |
| SL1-1 | STYLE | Brief L846 ("Without it ... grew 41.7%") and 7A L710 ("core PBT ex DA gain ... +41.7%") label the figure as ex DA gain only. It also strips other income (6.70 Q1, 0.34 Q2). Ex DA gain alone, PBT growth is 39.1% (501.30/360.33). The number is right for the defined core PBT. | Res L296, L298, L308; Rev L192, L846, L710 | Wording: "without it and 6.70 crore of other income". | none |
| SL1-2 | STYLE | "About half of the quarter's profit rise came from fee income" (L854) and "53%" (L803) are gross-contribution shares. In the same bridge, core NII added +183.34 (204% of the +90.04 net rise) and the lost DA gain took -50.93. The framing comes from my run-1 counter. | Rev L252-263 | Absolute framing: "fees added 48 crore and core NII 183 crore to a 90 crore pre-tax rise". | none |
| SL1-3 | STYLE | Servicing income is tagged "Recurring" while its base shrank. Its implied yield on the derived off-book pool went from about 5.0% to 7.4% to 9.7% annualised. Nature ND. Conclusion unaffected: recurring share stays 95.3% YoY even ex servicing growth. | Deck L557-558, L703-713, L803; Rev L255, L427 | Tag "Recurring? nature ND"; add the implied yield to Q12. | none |
| SL1-4 | STYLE | The brief grafts (L846, L849, L852, L854, L860, L869, L895) carry no [LOOP-1] tag, although Rev L8 says all grafted text is tagged. | Rev L8 | Add tags, or state that the brief is exempt. | none |
| S1 (run 1) | STYLE | Brief book mix (L867) omits Machinery & Medical Equipment 1% and Professional Loan 1%. The listed shares sum to 97%. | Deck L386, L391 | Add the two lines. | none |
| S2 (run 1) | STYLE | Forward map L893 calls 5,538 cr "6-12 month debt maturities ... net". It is the fall in the cumulative structural gap. | Deck L644 | Relabel as net structural outflow. | none |
| S3 (run 1) | STYLE | Collection efficiency is correctly ND. Optional: add a question asking for a collection-efficiency table. | Deck L731-745 | Optional question. | none |

No CONTRADICTION is raised separately. The GNPA-vs-NNPA qualifier gap (L279 vs L280; L303 vs L384) is an internal inconsistency, logged once as ML1-2 (MISSING), because the fix is to add the dropped qualifier.

---

## VERDICT

VERDICT: INCOMPLETE.
- Failing agent: A4. All fixes are text grafts on numbers already in the extract. There is no re-derivation and no protocol step to re-run. No A2 or A3 loop: coverage is complete, with no orphan rows and nothing missing from the ledgers.
- Gap (MISSING): ML1-1. Graft the filed ARC-transfer cover evidence: NBV 92.49 vs principal 161.60 gives 42.8% cover at transfer (Q1 54.3%), against Stage 3 PCR 49.1% and Stage 2 PCR 14.6% (Res L904-906; Deck L709-718). Mark the Stage 3 reading as better evidenced [INFERENCE], and show rupee GNPA +2.5% pre-transfer against the like-for-like ratio 1.55% to 1.42%. ML1-2. Carry the ARC qualifier to NNPA (L280, L303) and to the Step 7 pillar row (L384): pre-transfer NNPA +5.9%, like-for-like ratio 0.79% to 0.74%.
- Gap (FACTUAL): FL1-1. Tag the "cross-sell income is the exposed line" claim [INFERENCE] at L645, L803, L830, L860, L895 and the YAML. FL1-2. Correct the ANXII-N3 description (Res L1753).
- Run-1 F1-F3 and M1-M4: all applied; all loop-1 arithmetic matches.
- The protocol verdict PROCEED WITH FLAGS is not challenged. The grafts change how the asset-quality flag reads, not the verdict.
- Loop cap: the review marks this pass "iteration 1 of 1" (Rev L8). Whether a second graft pass runs or these items go to the operator is the orchestrator's decision. A5 does not override the cap.

## STYLE NOTES (logged, no re-run)
- SL1-1: the 41.7% label in brief L846 and 7A L710 also strips other income; ex DA gain alone the growth is 39.1%.
- SL1-2: replace the "about half" or "53%" fee framing with absolute bridge figures (fees +48, core NII +183, net +90).
- SL1-3: servicing income "Recurring" tag; implied yield on the derived off-book pool 5.0% to 7.4% to 9.7%; nature ND; add the yield to Q12.
- SL1-4: the brief grafts lack [LOOP-1] tags.
- S1-S3 (run 1): carried, not applied by A4 (allowed).

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
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "GNPA 1.37%->1.20% GREEN on reported ratio, AMBER-CONDITIONAL on ARC classification; NNPA GREEN on ratio, 439->430 (Rev L279-280, L303, L384, L708, L849)", counter: "Note 11(c) NBV 92.49 vs principal 161.60 implies 42.8% ECL cover at transfer in Q2 (Q1 54.3%, H1 47.7%), at the Stage 3 PCR level (49.1%) and ~3x Stage 2 PCR (14.6-17.9%); Q2 residual tenor 77 months points to long-tenor secured lines. Stage 3 reading better evidenced [INFERENCE]: pre-transfer GNPA +2.5% in rupees (981.9->1,006.6) and NNPA +5.9% (493.29->522.49) vs reported -2.1% each; like-for-like ratios still fall (GNPA 1.55%->1.42%, NNPA 0.79%->0.74%). NNPA and the Step 7 pillar row carry no ARC qualifier.", source_line: "Res L904-906; Deck L363, L709-718", type: MISSING}
findings_by_type:
  factual:
    - "FL1-1: 'Cross-sell income is the line exposed to the rule' stated as fact (Rev L645, L803, L830, L860, L895, YAML L975/L996); extract does not define Cross Sell Income (Deck L802) and management uses 'cross-sell' for loan cross-sell (Call L244-245, L298-307). Tag [INFERENCE]; name the second reading; keep Q8. Origin: A5 run-1 M1 wording."
    - "FL1-2: Step 0D ANXII-N3 described as 'Column-reporting note' (Rev L106); filed note 3 says secured NCD book value = principal plus accrued interest (Res L1753; R1326). Correct the row. Pre-existing; missed in run 1."
  missing:
    - "ML1-1: GNPA ARC graft omits filed cover evidence: NBV/principal implies 42.8% ECL cover at transfer in Q2, 54.3% in Q1, vs Stage 3 PCR 49.1% and Stage 2 PCR 14.6% (Res L904-906; Deck L709-718); Stage 3 reading better evidenced [INFERENCE]; rupee GNPA +2.5% pre-transfer, ratio like-for-like 1.55%->1.42%. Graft into Rev L100, L279, L442 (Q27 bull/bear), L708, L802, L849."
    - "ML1-2: ARC qualifier missing on NNPA (Rev L280, L303) and on the Step 7 Asset-Quality Multiplier pillar row (Rev L384). If Stage 3: pre-transfer NNPA 493.29->522.49 (+5.9%) vs reported -2.1%; like-for-like 0.79%->0.74% [DERIVED]."
  contradiction: []
  style:
    - "SL1-1: Brief L846 and 7A L710 label +41.7% as ex DA gain; it also strips other income (6.70 Q1); ex DA gain alone growth is 39.1% (501.30/360.33). Wording only."
    - "SL1-2: 'About half of the profit rise came from fee income' (L854) / '53%' (L803) is a gross-contribution share; core NII added +183.34 to a +90.04 net rise. Use absolute bridge figures."
    - "SL1-3: Servicing income tagged Recurring (L255) while its derived off-book base fell; implied yield ~5.0%->7.4%->9.7% annualised; nature ND; add to Q12. Recurring share stays 95.3% YoY even ex servicing growth."
    - "SL1-4: Brief grafts (L846, L849, L852, L854, L860, L869, L895) carry no [LOOP-1] tag despite Rev L8."
    - "S1 (run 1, carried): brief book mix omits Machinery & Medical Equipment 1% and Professional Loan 1% (Deck L386, L391)."
    - "S2 (run 1, carried): forward map 5,538 cr is a net structural outflow, not gross debt maturities (Deck L644)."
    - "S3 (run 1, carried): optional collection-efficiency table question (Deck L731-745)."
loop_back_to: "A4"
gap: "MISSING ML1-1: graft filed ARC-transfer cover evidence (NBV 92.49 vs principal 161.60 = 42.8% ECL cover at transfer, Q1 54.3%, vs Stage 3 PCR 49.1% and Stage 2 PCR 14.6%; Res L904-906, Deck L709-718), mark the Stage 3 reading better evidenced [INFERENCE], show rupee GNPA +2.5% pre-transfer vs like-for-like ratio 1.55%->1.42%, at Rev L100, L279, L442, L708, L802, L849. MISSING ML1-2: carry the ARC qualifier to NNPA (L280, L303) and the Step 7 pillar row (L384): pre-transfer NNPA +5.9%, ratio 0.79%->0.74%. FACTUAL FL1-1: tag the cross-sell-exposure claim [INFERENCE] at L645, L803, L830, L860, L895 and YAML. FACTUAL FL1-2: correct ANXII-N3 (Res L1753: NCD book value = principal plus accrued interest)."
style_notes:
  - "SL1-1: 41.7% label also strips other income; ex DA gain alone 39.1%."
  - "SL1-2: replace 'about half' fee framing with absolute bridge figures."
  - "SL1-3: servicing income Recurring tag; implied off-book yield 5.0%->7.4%->9.7%; add to Q12."
  - "SL1-4: brief grafts lack [LOOP-1] tags."
  - "S1-S3 (run 1): carried, not applied (allowed)."
analyst_note: "Run-1 F1-F3 and M1-M4 are applied, and every loop-1 figure recomputes exactly. Coverage is unchanged and clean: 2,386 rows, 27 notes, 45 turns, 42 slides, no orphans. The re-audit fails on the asset-quality graft. Note 11(c) gives Q2 ARC transfers an NBV of 92.49 against principal of 161.60. That is 42.8% ECL cover at transfer (Q1 54.3%), at the 49% Stage 3 PCR and three times the 14.6% Stage 2 PCR. The Stage 3 reading is better evidenced, though classification stays undisclosed. On it, rupee GNPA rose 2.5% before transfers, while the like-for-like ratio still fell. NNPA and the Step 7 pillar row carry no ARC qualifier. Two errors are partly mine: run 1 stated cross-sell income as the regulation-exposed line, and I missed the Annexure II note 3 misreading. Both fixes cut toward the bull or are neutral. All fixes are A4 text grafts; no A2 or A3 loop. PROCEED WITH FLAGS stands. The review marks this iteration 1 of 1, so the orchestrator decides between a second graft pass and operator escalation."
```
