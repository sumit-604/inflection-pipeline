# A5 ADVERSARY AUDIT: FEDFINA Q2 FY27, ROLE 5 CONCALL MERGE

Date: 2026-10-19 | model: claude-opus-5-5
Artefact under audit: work/review_fedfina_q2fy27.md (1,473 lines; line numbers below are "review Lnnn").
Prior record: work/audit_fedfina_q2fy27.md, Re-audit loop 2 (verdict INCOMPLETE on F5 only; S7-S10, S12-S14 logged).
Scope: the new ROLE 5 section (review L605-L1127), the concall ledger coverage, the re-graded and added Step 8.5 rows, flags, monitorables, Key Notes and the plain-language brief. Role 4 body: regression spot-check.

Read in full: concall fulltext (952 lines), concall structured file (R001-R267 and the 74-line turn index), concall ledger, the review.
Read in part: presentation structured rows R034, R226, R327, R450-R503, R555-R593, R606-R610, R620-R622, R670-R681, R705-R746, R760-R796, R1018-R1024, R1039-R1041; presentation fulltext L14-L37; my loop-2 record.
Not re-opened: the results, presentation and press-release ledgers. The review's counts for them (L17-L20) match the loop-2 record, and my loop-2 coverage PASS carries.
Not opened: inputs/, any source PDF or audio, A3 forensics, the orchestrator extraction check, the Notion copy. No git.

Edit footprint: the review grew from 816 to 1,473 lines. The Role 5 section, Section C, the 16 new Step 8.5 rows and the merge change log are new. The Role 4 body carries in-place "Role 5 note" insertions (review L148, L184, L196, L212, L318, L365, L367, L372, L377, L422, L466, L502).

Finding IDs continue the Role 4 series: F6+, M7+, C4+, S15+.

Record structure: the loop-0 concall audit follows unchanged, except that its YAML block is marked superseded and fenced as text. The "Re-audit loop 1" section follows; its YAML block is also marked superseded and fenced as text. The "Re-audit loop 2" section at the end carries the current verdict and the current YAML block. Line numbers inside the loop-0 record refer to the 1,473-line review. Line numbers in the Re-audit loop 1 section refer to the 1,496-line review after A4's Role 5 loop 1. Line numbers in the Re-audit loop 2 section refer to the review after A4's Role 5 loop 2 (last text line L1505).

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

- narrative: PRESENT. Review L1216-L1231, 15 lines (band 10-20).
- sector: PRESENT. L1233-L1244.
- business_model: PRESENT. L1246-L1258.
- competition: PRESENT. L1260-L1267.
- forward_map: PRESENT. L1269-L1281. One make-or-break metric plus 11 dated catalysts, each with a Bull fork and a Bear fork.

Gate: PASS.

---

## 1. COVERAGE AUDIT (concall)

Method:
- A fresh grep over the concall fulltext for every spoken digit (pattern `^\[..:..:..\] .*\d`, about 160 hit lines).
- A grep for every "?" (27 hit lines) and for the hedge lexicon.
- A line-by-line read of L24-L952 for speaker changes.
- A diff of the result against the 267 structured rows and the A2 ledger.

| Category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|
| participants | 17 | 17 | none | PASS |
| turns (A1 index lines) | 74 | 74 index lines, contiguous L24-L952. At least 80 speaker turns: T47, T50, T51 and T54 each hold three. | none | PASS on index lines; see mixed turns |
| mixed turns flagged | 5 (T22, T26, T33, T62, T71) | 9: add T47, T50, T51, T54 | n/a | FAIL (M9) |
| question turns | 23 | 26: add L687-L690 (Devansh follow-up in T47), L723-L726 (Yash second question in T50), L743-L746 (Yash upgrade pushback in T51) | n/a | FAIL (M9) |
| mgmt numbers, on A1 rows | 140 | 141: R121-R123 are management (L714-L718); R130-R131 are analyst (L744-L745) | n/a | FAIL (F6) |
| mgmt numbers, on the fulltext | 140 | 145 distinct instances: add L57, L113, L482, L483. Eight more repeat or time-reference instances are uncaptured. | n/a | FAIL (M7) |
| analyst or moderator numbers | 9 | 8 | n/a | FAIL (F6) |
| forward phrases | 49 | 58: add L56, L57, L100, L562, L567, L615, L810, L868-L869, L893-L894 | n/a | FAIL (M8) |
| qualifiers | 21 | 22 or more: add L715-L716. L106, L418-L419 and L639 are further candidates. | n/a | FAIL (M8) |
| entities | 35 | 35 | n/a | PASS |
| dates | 13 | 14: add L270 ("April", IGL launch) | n/a | FAIL (M8, minor) |
| zero standing | 1 (R100) | 1 | n/a | PASS |
| SPEAKER_INFERRED turns | 52 | 52 (22 explicit index lines, counted) | n/a | PASS |
| ledger rows cited or reviewed in A4 | 267 | 267. Review L21-L22 declares every row read; line-level cites run through the Role 5 section. | none | PASS |

Orphan rows: none. Rows the ledger lacks: yes (M7, M8, M9). Coverage: FAIL, loop to A2.

### F6 (FACTUAL, A2): number rows on the wrong side
- A1's turn index puts L704-L726 in one analyst turn (T50). Inside it, L714-L722 is a management answer: "Typically, a branch if it reaches about 6 to 7 crores of AUM, it turns profitable for us" (L714); "Last year we put about 150 branches" (L718). The ledger lists R121, R122 and R123 as ANALYST_OR_MOD_NUMBER (ledger L307-L309).
- T51 (L727-L759) holds Yash's pushback at L743-L746. R130 ("36%", L745) and R131 ("60-70%", L744) are his. The ledger counts both as management (ledger L276-L277). A1's own row context says "AUM growth stated by analyst" (R130) and "analyst: share of business" (R131); R266 says the 36% is analyst-stated and unconfirmed.
- Result: management numbers on A1 rows are 141, not 140. Analyst numbers are 8, not 9. The review repeats 140 at L21.
- Review impact: none on content. The review already reads L714-L722 as management (Q10 L542, 5A L875).

### M7 (MISSING, A2): management numbers absent from the structured file
| Fulltext line | Speaker turn | Verbatim | Note |
|---|---|---|---|
| L57 | T04 CEO | "to hold credit costs below 1%" | Review Step 1 row 3 cites it; no NUMBER row |
| L113 | T05 CFO (explicit) | "we had crossed the interim ROE milestone of 15 percent" | Distinct number; uncited anywhere in the review |
| L482 | T25 | "the exposure of a customer is capped at 75%" | Exposure-based LTV cap |
| L483 | T25 | "if it is 80% he offsores maximum LTV" | Exposure-based LTV cap. With L480 ("Ninety ninety-five percent" take the maximum), most new loans sit at their slab cap. |

Uncaptured repeats or time references with digits: L720 and L722 ("6, 7 crores", "12 to 13 months"), L754 and L890 ("20-25%", "20 to 25 percent"), L640 ("8-9 quarters"), L684 ("7-8 quarters"). A1 captures repeats elsewhere (17% ROE four times, R034, R041, R049, R051; 831 twice), so its own rule covers these.
Ledger section 9 says "MISSING_FROM_STRUCTURED: None found." That is the gap.

### M8 (MISSING, A2): forward, date and qualifier units absent from the structured file
A1's own standard captures R187 "We remain optimistic on continuing on this trajectory" (L123) and R208 "we will continue our trajectory of reducing OpEx" (L553). By that standard these are FORWARD rows too:
- L56 "to grow our core income even as we consciously reduce our reliance on direct assignment". The review's DA-RELIANCE-CONTRADICTION (flag 9), 7A L987 and monitorable 19 (concall C19) rest on this line. A3 registered it from the fulltext, but the structured file and the ledger do not carry it.
- L57 "to hold credit costs below 1%".
- L100 "we believe it positions us well for the quarters ahead".
- L562 "Going forward, we will continue on that trajectory."
- L567 "We will try and leverage through the OpEx ratio and the credit cost to reach that free [three] ROA."
- L615 "we will definitely live up to your expectations in Q3."
- L810 "we will be steady at that kind of an approval rate."
- L868-L869 "you will still continue to see at entity level, the trajectory on the ROA in a similar range as we are targeting."
- L893-L894 "our cost to income also will start going down on the gold side".

DATE: L270 "we had got it ready in April itself" (IGL launch; the review cites L268-L271).
QUALIFIER: L715-L716 "when the price is going on an upward trajectory or the price that is, even the price that is there today". It conditions the branch-breakeven claim on the gold price (see adversarial read 2).

### M9 (MISSING, A2): mixed turns and question turns
- T47 (L681-L695): L687-L690 is Devansh's follow-up, "And the lever that you would, you would assume that would offset it would be a family object [opex] for our credit card [or credit cost]." L691-L695 is the CFO's answer, "All of it ... a combination of all."
- T50 (L704-L726): Yash Q1 (L709-L713), management answer (L714-L722), Yash Q2 (L723-L726).
- T51 (L727-L759): management (L727-L742), Yash pushback "do you think your AVM guidance and your ROE guidance can be upgraded" (L743-L746), management (L747-L759).
- T54 (L766-L771): management clarification "You are asking on the gold side?" (L770).
- Line-level only: T56 ends with the first answer line (L799); T63 ends with "No, two things." (L844).
- Fresh question-turn count: 26, not 23. The review folds the three extra questions into Q14 and Q15 (L812-L813) and cites the pushback at L830, so no content is lost. Every count is inherited: L21, L632, L795, L1106.

### Downstream alignment A4 must make once A2 adds the units
- Counts at review L21, L632, L795 and L1106.
- Step 1 inventory (L640-L704): three T05 claims are absent. They are L106-L107 (headwinds and "lack of momentum and gold prices"), L110-L112 (a "consistent non-cyclical" ROA/ROE model) and L113 (15% interim ROE milestone, quantified). With them, quantified share is 39 of 58 (67%), not 38 of 55 (69%) (M15, A4).
- 6B specificity (L933-L935): with the nine forward phrases, the ratio is 17 or 18 of 58 (0.29-0.31; L57 is quantified, and L567 is quantified only by its reference to the 3% target). That puts it on the 0.3 hedge-heavy line, not "just above". The archetype stays ND because the bottom row is unchanged.

---

## 2. ARITHMETIC AUDIT (Role 5 section and touched Role 4 rows)

| Metric | A4 value (review line) | Recomputed | Source line | Status |
|---|---|---|---|---|
| Step 1 quantified share | 38 of 55, 69% (L701) | 17 NO rows (1, 2, 13, 15, 25, 27, 28, 29, 32, 35, 44, 45, 47, 48, 51, 54, 55); 38 / 55 = 69.1% | review L644-L698 | PASS |
| Step 1 forward quantified | 2 of 8, 25% (L701) | rows 3 and 53 YES of 3, 13, 28, 32, 51, 53, 54, 55 | review L646-L698 | PASS (row-type note S20) |
| FY27 AUM band, new guide | Rs 24,184-25,191 Cr (L712) | 20,153 x 1.20 = 24,183.6; x 1.25 = 25,191.3 | Deck R423 base via review L207 | PASS |
| FY27 AUM band, Q1 log | Rs 24,184-24,587 Cr (L712) | 20,153 x 1.22 = 24,586.7 | same | PASS |
| ROA bands | 2.7-2.8% new; 2.6-2.7% log (L719) | 2.4 + 0.30/0.40; 2.4 + 0.20/0.30 | Call L728-L729 | PASS |
| H2 growth needed, 20% / 25% | +9.8% / +14.3% (L728, L1030) | 24,184 / 22,035 = 1.0975; 25,191 / 22,035 = 1.1432 | Deck R428 | PASS |
| Gold H2 at tonnage pace | +7.4% to +9.4% (L728) | 13.86 / 12.9 = 1.0744; 14.112 / 12.9 = 1.0940 | Deck R491 | PASS |
| Gold AUM at Mar-27, flat price and LTV | Rs 12,799-13,037 Cr (L728) | 11,917 x 1.07442 = 12,804; 11,917 x 1.09395 = 13,036.6 | Deck R443, R491 | PASS (lower bound uses the rounded 7.4%; Rs 5 Cr) |
| Non-gold needed and its H2 growth | Rs 11,147-11,385 Cr; +10.2% to +12.5% (L728) | 24,184 - 13,037 = 11,147; 24,184 - 12,799 = 11,385; on 10,118 (22,035 - 11,917): 1.1017, 1.1252 | derived | PASS |
| Non-gold H1 growth | +3.2% (L728) | 9,801 (20,153 - 10,352) to 10,118 = 1.0323 | Deck R441, R443 | PASS |
| Branch plan vs log | 224, +24 (L721, L726) | 74 + 150 = 224 | Call L187-L189 | PASS |
| Credibility ratio | 0 / (6 - 6) = ND (L760) | six quantified FY27 targets, all UNCLEAR at H1 | review L740-L745 | PASS |
| 3E tally | 1 / 8 / 4 (L789) | answered: row 1; partial: 2, 3, 5, 6, 7, 10, AR-1, AR-3; not addressed: 4, 8, 9, AR-2 | review L775-L787 | PASS |
| 4A grade tally | A 2, B 15, C 6 (L823) | counted row by row | review L799-L821 | PASS (grade text conflict C5) |
| 6B specificity | 16 / 49 = 0.33 (L935) | 0.327 on the 49 A1 rows | Call R185-R233 | PASS on inputs; downstream note above |
| 6C hedge markers | 7 + 8 + 1 = 16 (L938-L940) | grep: lexicon 7; "we believe" 7 + "we still believe" 1 (L892); "we expect" 1 (L68) | fulltext grep | PASS |
| Q&A duration and share | 53.4 min, 78% (L631) | 01:08:19 - 00:14:54 = 53.42 min; / 68.53 = 77.9% | Call L6, L205, L949 | PASS (scope note S16) |
| 7A PAT QoQ | +14.31% (L962) | 130.75 / 114.38 = 1.1431 | Res R103-R104 | PASS |
| 7A ROA QoQ | +24 bps spoken, CONFIRMED (L963) | 2.843% - 2.605% = 23.8 bps (523.0 / 18,393.5; 457.5 / 17,561) | review L152-L158 | PASS |
| 7A disbursal YoY | gold +31.0%, MT LAP +16.4%, mortgage +12.5% (L965) | 5,822 / 4,445; 645 / 554; 855 / 760 (= 645 + 210 vs 554 + 206) | Deck R465, R469, R470, R474, R475, R479 | PASS |
| 7A credit cost QoQ | -20.5% (L970) | 27.08 / 34.06 - 1 = -20.49% | Res R043-R044 | PASS |
| 7A PCR segment check | 87.9 + 5.0; residual 14.0 Cr with 11.8 Cr ECL, 84% (L976) | 234.4 x 0.375; 47.6 x 0.105; 296 - 234.4 - 47.6; 104.7 - 92.9. Business loans alone are GS3 12.1 at 95.9% = 11.6 (Deck R744, R746), so the residual is mostly business loans. | Deck R724, R726, R734, R736, R781, R787 | PASS |
| 7A gold share of GS3 rise | about 88% (L978) | (47.6 - about 9.5) / 44 = 87%; the 0.1% Q1 base is rounded | Deck R738-R739, R780-R781 | PASS (wide band) |
| 7A off-book moves | gold +778, total +872; DA gap 177 (L985) | 2,496 - 1,718; 5,771 - 4,899; 876.89 - 700 | review L356-L358 | PASS |
| 7A PPOP | +9.35% QoQ, +47.6% YoY (L981) | 205.08 / 187.54; 205.08 / 138.99 | review L123 | PASS |
| 7A BVPS | Rs 84.37 (L994) | 3,164.96 / 37.514 | Res R420, R169 | PASS |
| 7A gold value per gram QoQ | about +4.7% (L995) | (11,917 / 12.9) / (11,191 / 12.7) = 1.0483; / (68.0 / 67.9) = 1.0468 | Deck R442-R443, R490-R491, R500-R501 | PASS |
| 7A tally | 23 / 3 / 2 / 3 / 7 = 38 (L1001) | counted row by row, L962-L999 | review | PASS on A4's verdicts; changes to 22 / 4 under F7 |
| **7A core yield ex-DA** | **CONFIRMED: "core yield constant at 16.40" (L982)** | **Slide 25 yield 16.4% (Q1) to 16.7% (Q2), XC order. The XC order is the only one that passes yield = CoB + spread (Q1 7.7 + 8.6 = 16.3; Q2 7.9 + 8.8 = 16.7). Add back net DA / ATA of -0.3% and 0.0% (Deck R1023-R1024): core is about 16.7% in both quarters. The constancy and the +29 bp optical rise tie. The 16.40 level ties only to the Q1 reported yield.** | **Call L138-L141; Deck R560-R561, R562-R581 (XC), R1023-R1024** | **FAIL (F7)** |
| ST LAP "best of 8-9 quarters" bar | above Rs 289 Cr (L579, L1137) | Slide 22 shows five quarters: 206, 208, 289, 144, 210 (Q2 FY26 to Q2 FY27). Q1 FY26 derives to 201 (904 - 703). FY25 quarters are not in the run (FY25 total Rs 1,004 Cr, average 251). | Deck R475-R479; review L40 | Bar not established (M11) |
| Sell-down "record" | record Rs 1,085 Cr (L598, L1225, L1185) | Highest of 11 quarters: 284, 577, 536, 486, 531, 1,044, 578, 313, 645, 530, 1,085 | Deck R670-R680 | PASS |
| Q3 tonnage test | 13.4 t (L1029, L1138) | 12.9 x (13.86 / 12.9)^0.5 = 13.37 | Deck R491 | PASS |
| Last year's H2 tonnage | +13.5% (L1029) | 12.6 / 11.1 = 1.1351 | Deck R487, R489 | PASS |
| Step 8.5 call tally | 3 / 8 / 20 = 31; 28 open (L522, L591) | row-by-row status column, L528-L563 | review | PASS |
| EBLR residual | about 43% (L869) | 100 - 33 - 24, reading the 24% as a share of total borrowings (Call L145-L146) | Call L630-L633 | PASS |

---

## 3. ADVERSARIAL READ (Role 5 focus)

### Claim 1. "The Q2 spread still widened 8.6% to 8.8% (XC). The risk is forward, not yet in the numbers." (review L856; also L1071, L1188, L1243, YAML L1423), together with the 7A CONFIRMED verdict on the CFO's yield claim (L982)
- Bear counter from the same extract: A4 confirms the CFO's statement that the 29 bp yield rise is "optical", caused by the Q1 DA unwinding (Call L138-L141; net DA / ATA -0.3% to 0.0%, Deck R1023-R1024). If the yield rise is optical, the reported spread rise is optical too.
- Ex-DA, yield was flat on the CFO's own account. CoB rose 20 bps on slide 25 (7.7% to 7.9%) and 13 bps on the P&L basis (7.74% to 7.87%); only the daily I-GAAP series was flat (Deck R609-R610). So the ex-DA spread narrowed about 13-20 bps in Q2 on two of three CoB measures.
- The whole NIM rise of 8.5% to 8.8% (Deck R1027-R1028) is DA; core NII / ATA held at 8.8% (Deck R1019-R1020).
- Survives: YES, in part. Core NII / ATA held, so "not yet in the numbers" is half-right. But the spread widening is not evidence against NIM pressure. On the yield-less-CoB measure the pressure is already in Q2.
- Graft (MISSING, A4; M12) at L856, L1071, L1188 / YAML L1423 and L1243: "The +20 bp reported spread rise is the DA-drag reversal: the CFO calls the yield rise optical (Call L138-L141), and net DA / ATA moved from -0.3% to 0.0% (Deck R1023-R1024). Ex-DA, yield was flat while CoB rose 13-20 bps on two of three measures, so the ex-DA spread narrowed about 13-20 bps. Core NII / ATA held at 8.8% (Deck R1019-R1020)."

### Claim 2. "Branch breakeven at Rs 6-7 Cr AUM in 12-13 months ... Supports the H2 branch economics" (review L875; also Q10 L542, brief L1251)
- Bear counter: the CEO himself ties the timeline to the gold price. "when the price is going on an upward trajectory or the price that is, even the price that is there today, we, in 12 to 13 months, the branch starts touching that number" (Call L715-L716).
- His evidence is the FY26 cohort, "Last year we put about 150 branches" (L718-L722). That cohort grew while the implied gold value per gram rose about 38% YoY (review Step 6D, L447).
- A gold branch's AUM is grams x price x LTV, so the record is price-assisted. The guidance itself assumes a flat price (Call L757-L758, L883). No evidence covers a flat-price cohort.
- Survives: YES, as a qualifier.
- Graft (MISSING, A4; M13) at L875, L542 and L1251: "The CEO ties the 12-13 months to a rising or current gold price (Call L715-L716). The FY26 cohort he cites grew while gold value per gram rose about 38% YoY (Step 6D). The timeline is untested at a flat price, which is the guidance's own assumption."

### Claim 3. "Buy-side present; no yellow flag." and "No evidence of an orchestrated call." (review L828-L829)
- Bear counter: one buy-side questioner speaks as a holder. He calls the company "strong and influence players like us" (Call L517-L518). He says "I can already see Navratri and Diwali in our results. I hope it happens in our stock also" (L571-L572). Management replies "thank you for your support" (L573).
- Six of the nine questioners open with congratulations (L333, L469, L578, L674, L707, L831). The filing's main asset-quality flag drew no question (A4's own L831).
- Survives: YES, as a qualifier. It is not proof of pre-screening. It weakens the reading that buy-side presence means independent questioning.
- Graft (MISSING, A4; M14) at L828-L829: "One buy-side questioner spoke as a holder ('players like us', 'our stock', Call L517-L518, L571-L572), and management thanked him 'for your support' (Call L573). Six of nine questioners opened with congratulations. This does not show pre-screening. It weakens the buy-side-independence reading."

### Tested and failed (no graft)
- 7A "PCR fall from more gold in Stage 3: CONFIRMED (mechanism)" (L976). I tried to break it. Q2 business loans are GS3 Rs 12.1 Cr at 95.9% (Deck R744, R746). Mortgage, gold and business loans then explain Rs 104.5 Cr of the Rs 104.7 Cr Stage 3 ECL. The mix mechanism holds on the Q2 composition. Q1 mortgage PCR stays ND, as A4 says at L977.
- "Record" sell-down: holds (Deck R670-R680; 1,085 > 1,044).

### Mandatory acquisition-economics probe
Not triggered. The call describes no acquisition, purchase or stake buy. The filings show no loans acquired by assignment and no stressed loans acquired (Res R478-R479, review L87). The Rs 876.89 Cr assignment is a sale.

---

## 4. LINE-BY-LINE CHECK OF THE ROLE 5 SECTION: OTHER FINDINGS

I checked all 55 Step 1 cites, the Step 2L cites, all 23 Q&A rows, the three exchange quotes (verbatim against L382-L424, L723-L736, L648-L686), all 38 rows in 7A, the 47 Step 8.5 rows and the brief. Nearly all hold. The exceptions follow.

- F7 (FACTUAL, A4). 7A row L982 says CONFIRMED. The level does not tie (arithmetic table).
  - Fix: verdict "PARTIALLY CONFIRMED: the +29 bp optical rise and its DA cause tie under XC; the 16.40 level does not. Core ex-DA derives to about 16.7% in both quarters; 16.4% is the Q1 reported yield [ASR or definition]."
  - Align: the tally at L1001 becomes 22 CONFIRMED and 4 PARTIALLY CONFIRMED. Section C L1123 "confirms 23" becomes 22. At L46, FN-07 keeps a level leg, not only the CoB basis leg. Flag 15 (L1191, YAML L1426) gains a fourth drift: core yield 16.40 spoken vs about 16.7% ex-DA.
- F8 (FACTUAL, A4). Exchange 3, L855: "Not said: ... which 'other lever'". Management named the levers.
  - "We will try and leverage through the OpEx ratio and the credit cost to reach that free ROA" (Call L567; A4 cites L567-L569 itself at L718).
  - Asked whether the offset would be opex or credit cost, the CFO said "All of it ... a combination of all" (L689-L695).
  - The parenthetical cites L542 for the 150 branches; that figure is at L187-L189.
  - Fix: "Levers named only in general: opex and credit cost (Call L567, L689-L695), with no size. Both are partly used: at least 150 H2 branches add opex (Call L187-L189), and credit cost is already 0.6%."
- C4 (CONTRADICTION, A4). Q01 (L799) says "guidance held for Q3-Q4".
  - The gold-growth answer says "we will continue with our guidance in Q3 and Q4 as well" (Call L248-L249). The CFO adds "we would be able to perform to our guidance which we have been giving in the earlier quarters for this year on AUM" (L292-L293).
  - Against that, Step 1 says "gold AUM never reappears" (L703), Step 2L says "Withdrawn without acknowledgment" (L723), and 6A says "DROPPED" (L923).
  - Fix: add reading (c) to the L727 diagnostic: "the gold guide was reaffirmed without a number in the gold-growth answer (Call L248-L249, L292-L293)." Change L723 to "Not restated in number; reaffirmed only as 'our guidance' (Call L248-L249)". Qualify 6A L923, flag 6 L1182 / YAML L1417 and the brief L1237 the same way.
  - The DROPPED candidate stays a candidate. The separating observation (row 35, a written guidance table) is unchanged.
- C5 (CONTRADICTION, A4). L823 says "The refusals sit inside C-graded answers: gold yield (Q02), Stage 2 (Q04) and ST LAP numbers (Q10)". Q10 is graded B (L808).
  - Fix: regrade Q10 to C (the grade tally becomes A 2, B 14, C 7), or write "inside C-graded answers (Q02, Q04) and the B-graded Q10".
- C6 (CONTRADICTION, A4). The brief, L1231: "The operator must rule on one item". Section C, L1125: "Operator rulings open: Pillar 2L baseline; credit-cost tripwire basis."
  - Fix: the brief names both items.
- M10 (MISSING, A4). Branch split, Call L539-L541: "If you see we've done about 75 in the next quarter you will see us pushing for a hundred branch number in the Q4 again we'll push for more number".
  - A4 gives one parse: about 75 in Q3 and 100 in Q4.
  - A second parse fits the past tense and the filed Q2 count of 74 (Deck R033). In it, "we've done about 75" is Q2, Q3 is about 100, and Q4 is "more".
  - Fix at L541, L721, L807, monitorable 7 L1140 and YAML L1384: state both parses. The separating observation is Q3 FY27 branch additions, about 75 against about 100.
- M11 (MISSING, A4). The ST LAP bar.
  - "Best quarter compared to the last eight or nine quarters" (Call L589-L591) reaches back to Q2 or Q3 FY25.
  - The deck gives five quarters (Deck R475-R479), and Q1 FY26 derives to Rs 201 Cr. Rs 289 Cr is the highest known quarter, not a confirmed 8-9 quarter bar.
  - FY25 averaged Rs 251 Cr after an FY24 average of Rs 369 Cr, so an early-FY25 quarter could exceed Rs 289 Cr.
  - Fix at L579, L1098, L1126, L1137 / YAML L1381 and L1272: "above Rs 289 Cr, the highest of the six known quarters; FY25 quarterly values are not in the run, so the true bar may be higher (row 42 asks for the series)."
- M15 (MISSING, A4; follows M7). Step 1 omits three CFO claims: L106-L107, L110-L112 and L113 (see the downstream alignment in Section 1).

---

## 5. ROLE 4 REGRESSION SPOT-CHECK

| Item | Loop-2 state | Now | Status |
|---|---|---|---|
| F5 (loop-2 FACTUAL, analyst_note) | "rose only because" | L1447: "rose mainly because Stage 1 took 12.0 (55%) of the 21.8 Cr build"; flag 3 L1179 carries "(55%)" | RESOLVED |
| S14 (note label, gold wording) | open | "Loop 1 revision" and "fails its own price-flat condition" are gone from L1447 | RESOLVED |
| S13 (L476 wording) | open | L484 still names gold AT RISK twice | OPEN, logged |
| 1L-b pattern | 8 / 5 | L196 unchanged; adds the Role 5 re-grade 1 / 8 / 4, which ties to 3E | PASS |
| Step 2 wedge, Step 3 3.4%, stage-wise table | as fixed | L243, L263, L303-L311 unchanged | PASS |
| AT RISK 14.0 t clause | as fixed | L205, L455, L1182, L1237, YAML L1417 carry it | PASS |
| De-leverage, Rs 208.11 Cr gap, Annexure II anchor | as fixed | L208, L86, L90 unchanged | PASS |
| 6D count | 6 of 10 plus AT RISK | L484 unchanged | PASS |
| Inserted Role 5 notes | n/a | L318 (L160-L161, L420-L424), L365 (L92-L94, L148-L150), L367 (L136), L372 (L154-L159, L341-L342), L148: each cite matches the fulltext | PASS |
| 6B row 1 vs 8B row 1 | n/a | AMBER pre-call (L422) and GREEN post-call (L1045) with the reason stated | PASS (pre/post, not a contradiction) |

No Role 4 figure, verdict or Decision Status changed. No regression.

---

## VERDICT

VERDICT: **INCOMPLETE**.

- Deliverable gate: PASS. Arithmetic: one FAIL (F7); every other recomputation passes.
- Coverage: FAIL. Loop to **A2** first. The fresh grep finds units the structured file and the ledger lack (M7, M8, M9) and number rows on the wrong side (F6). A2 can add rows and fix attributions as it did in Role 4 loop 1.
- Then **A4**:
  - Align the counts (L21, L632, L795, L1106, Step 1, 6B).
  - Make the text fixes F7, F8, C4, C5, C6, M10, M11 and M15.
  - Graft the three surviving bear counters M12, M13, M14.
  - Each fix is a sentence or a cell, with replacement text given above.
- A3: no re-run is needed unless A4 finds a new forensic point in the added rows. L113, L482-L483 and L715-L716 are the candidates. A5 does not read A3, so A4 judges this.
- No finding changes the protocol verdict (PROCEED WITH FLAGS), a tripwire, the Pillar 2L condition or Decision Status.

## STYLE NOTES (logged, no loop)
- S15: 0D L634 says the safe harbour is "one sentence". It is two sentences (Call L39-L42).
- S16: 0C L631 runs the Q&A to L949, so it includes the closing remarks (L928-L949). Q&A proper ends at L924: about 52.2 minutes, 76%.
- S17: 4B L827 "Topics graded C" lists four of the six C rows. Q08 and Q20 are missing.
- S18: Brief L1222, "He said an April change". The CFO dated the guidance to Q1 (Call L154). The April date is the CEO's (Call L341-L342).
- S19: Brief L1221, "provisions fell". The P&L charge fell (Rs 34.06 Cr to Rs 27.08 Cr). The ECL stock rose Rs 21.8 Cr. Write "the provision charge fell".
- S20: Step 1 L701 counts row 55 (typed Macro/Tailwind) as forward, but not rows 15 and 45, which have the same type.
- S21: 2L L730 puts Yash's refused upgrade in T50. The question is at L743-L746, inside index turn T51.
- S22: 5B L908 says management invoked peers twice. A third invocation is at Call L255-L258.
- S23: A1 structured line anchors are one line off for R026 (L83), R066 (L136), R073 (L144), R074 (L145), R122 (L716), R125 (L728) and R138 (L818). The values are right.
- Carried, open: S13 (L484), S7-S10, S12.

Loop-0 YAML block (SUPERSEDED; the current block is the Re-audit loop 2 block at the end of this file; kept as the record, fenced as text so that no parser reads it as the current block):

```text
stage: A5-adversary
company: "FEDFINA"
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
    - "NUMBER: Call L57 'below 1%' (T04), L113 '15 percent' interim ROE milestone (T05), L482 '75%' and L483 '80%' exposure LTV caps (T25); repeats L720, L722, L754, L890; time refs L640, L684"
    - "FORWARD: Call L56 (reduce reliance on DA), L57, L100, L562, L567 (opex and credit cost levers to ROA 3%), L615, L810, L868-L869, L893-L894"
    - "DATE: Call L270 'April' (IGL launch). QUALIFIER: Call L715-L716 (breakeven conditioned on gold price)"
    - "QUESTION TURNS: Call L687-L690 (in T47), L723-L726 (in T50), L743-L746 (in T51): 26 not 23. MIXED_TURN flags missing on T47, T50, T51, T54"
arithmetic_mismatches:
  - {metric: "7A core yield ex-DA level", a4_value: "CONFIRMED: 'core yield constant at 16.40' (review L982)", recomputed: "Slide 25 yield 16.4% Q1 to 16.7% Q2 (XC order, the only order passing yield = CoB + spread); add back net DA/ATA -0.3% and 0.0%: core about 16.7% both quarters. Constancy and the +29 bp optical rise tie; the 16.40 level ties only to Q1 reported yield. PARTIALLY CONFIRMED.", source_line: "Call L138-L141; Deck R560-R581 (XC), R1023-R1024"}
  - {metric: "Concall management-number count", a4_value: "140 (review L21, from ledger L295)", recomputed: "141 on A1 rows (R121-R123 are mgmt, Call L714-L718; R130-R131 are analyst, Call L744-L745, per A1 row context and R266); 145 with L57, L113, L482, L483", source_line: "Call L714-L718, L744-L745; ledger L276-L277, L307-L309"}
  - {metric: "Concall question turns", a4_value: "23 (review L21, L632, L795, L1106)", recomputed: "26", source_line: "Call L687-L690, L723-L726, L743-L746"}
surviving_bear_counters:
  - {claim: "Q2 spread still widened 8.6% to 8.8%; NIM risk is forward, not yet in the numbers (review L856, L1071, L1188, L1243)", counter: "A4 confirms the CFO's yield rise is optical (Q1 DA drag). Ex-DA, yield was flat while CoB rose 13-20 bps on two of three measures, so the ex-DA spread narrowed about 13-20 bps; the NIM rise 8.5% to 8.8% is all DA; core NII/ATA held at 8.8%", source_line: "Call L138-L141; Deck R1019-R1020, R1023-R1024, R1027-R1028, R609-R610; review L176", type: "MISSING"}
  - {claim: "Branch breakeven Rs 6-7 Cr in 12-13 months supports H2 branch economics (review L875, L542, L1251)", counter: "CEO ties the timeline to a rising or current gold price; the cited FY26 cohort grew while gold value per gram rose about 38% YoY; untested at the flat price the guidance assumes", source_line: "Call L715-L722, L757-L758; review L447", type: "MISSING"}
  - {claim: "Buy-side present, no yellow flag; no evidence of an orchestrated call (review L828-L829)", counter: "One buy-side questioner spoke as a holder ('players like us', 'our stock'); management thanked him 'for your support'; six of nine opened with congratulations. Not proof of pre-screening; weakens buy-side independence", source_line: "Call L517-L518, L571-L573", type: "MISSING"}
findings_by_type:
  factual:
    - "F6 (A2): R121-R123 (mgmt answer at Call L714-L722 inside analyst index turn T50) tagged ANALYST; R130-R131 (Yash at L744-L745 inside T51) counted as management against A1's own row context. Mgmt numbers 141 not 140; analyst 8 not 9"
    - "F7 (A4): 7A L982 core-yield row CONFIRMED; level does not tie (core ex-DA about 16.7% both quarters; 16.40 = Q1 reported). Make PARTIALLY CONFIRMED; tally 22/4 (L1001, L1123); FN-07 keeps a level leg (L46); flag 15 adds a fourth drift (L1191, YAML L1426)"
    - "F8 (A4): Exchange 3 L855 'Not said: which other lever'. Levers named: opex and credit cost (Call L567, L689-L695); L542 cite wrong for 150 branches (L187-L189)"
  missing:
    - "M7 (A2): management NUMBER instances absent from structured file and ledger: Call L57, L113, L482, L483 (plus repeats L720, L722, L754, L890; L640, L684). Ledger section 9 says none"
    - "M8 (A2): FORWARD phrases absent: Call L56, L57, L100, L562, L567, L615, L810, L868-L869, L893-L894; DATE L270; QUALIFIER L715-L716"
    - "M9 (A2): mixed turns T47, T50, T51, T54 unflagged; question turns 26 not 23 (L687-L690, L723-L726, L743-L746)"
    - "M10 (A4): branch split Call L539-L541 has a second parse (75 done in Q2, about 100 in Q3, more in Q4) fitting the past tense and the filed 74; state both at L541, L721, L807, L1140, YAML L1384"
    - "M11 (A4): ST LAP Rs 289 Cr is the highest of six known quarters (Deck R475-R479; Q1 FY26 derived 201); FY25 quarters not in run, so the 8-9 quarter bar may be higher. Qualify L579, L1098, L1126, L1137, L1272, YAML L1381"
    - "M12 (A4): graft surviving counter 1 (spread widening is the DA reversal) at L856, L1071, L1188/YAML L1423, L1243"
    - "M13 (A4): graft surviving counter 2 (breakeven price-assisted) at L875, L542, L1251"
    - "M14 (A4): graft surviving counter 3 (holder-analyst signal) at L828-L829"
    - "M15 (A4): Step 1 inventory omits CFO claims Call L106-L107, L110-L112, L113 (quantified); share becomes 39 of 58; align counts L21, L632, L795, L1106 and 6B (17-18 of 58, 0.29-0.31) after A2"
  contradiction:
    - "C4 (A4): Q01 L799 'guidance held for Q3-Q4' (Call L248-L249, L292-L293) vs L703 'gold AUM never reappears', L723 'Withdrawn without acknowledgment', L923 DROPPED. Add reading (c), unquantified reaffirmation; qualify L723, L727, L923, L1182, L1237, YAML L1417"
    - "C5 (A4): L823 lists Q10 among C-graded refusals; Q10 is graded B (L808)"
    - "C6 (A4): brief L1231 'operator must rule on one item' vs Section C L1125 two open rulings (Pillar 2L baseline; credit-cost tripwire basis)"
  style:
    - "S15: 0D L634 safe harbour is two sentences, not one (Call L39-L42)"
    - "S16: 0C L631 Q&A span includes closing remarks; Q&A proper ends L924 (about 52.2 min, 76%)"
    - "S17: 4B L827 'Topics graded C' omits Q08 and Q20"
    - "S18: brief L1222 attributes the April date to the CFO; it is the CEO's (Call L341-L342)"
    - "S19: brief L1221 'provisions fell': write 'the provision charge fell' (ECL stock rose Rs 21.8 Cr)"
    - "S20: Step 1 L701 counts row 55 (Macro/Tailwind) as forward but not rows 15 and 45"
    - "S21: 2L L730 places Yash's upgrade refusal at T50; it sits in index turn T51 (Call L743-L746)"
    - "S22: 5B L908 'peers invoked twice'; third at Call L255-L258"
    - "S23: A1 line anchors off by one for R026, R066, R073, R074, R122, R125, R138"
    - "S13 carried (L484); S7-S10, S12 carried"
loop_back_to: "A2"
gap: "A2 first: add the units the fresh grep finds (NUMBER Call L57, L113, L482, L483 plus repeats L720, L722, L754, L890, L640, L684; FORWARD L56, L57, L100, L562, L567, L615, L810, L868-L869, L893-L894; DATE L270; QUALIFIER L715-L716); flag T47, T50, T51, T54 MIXED_TURN and add question turns L687-L690, L723-L726, L743-L746 (26); re-attribute R121-R123 to management and R130-R131 to analyst (141). Then A4: align counts (L21, L632, L795, L1106, Step 1 incl. L106-L113 claims, 6B); F7 (L982 to PARTIALLY CONFIRMED; L1001, L1123, L46, flag 15); F8 (L855 levers); C4 (gold guide reading c, L703, L723, L727, L923, L1182, L1237); C5 (L808 vs L823); C6 (L1231 vs L1125); M10 (second branch parse); M11 (Rs 289 Cr bar qualifier); graft M12-M14. Replacement text is in the audit. No protocol verdict, tripwire or Decision Status change."
style_notes:
  - "S15-S23 new (see audit); S13, S7-S10, S12 carried, open; S14 and loop-2 F5 resolved"
analyst_note: "The Role 5 merge is careful and mostly right. I re-checked the 55 opening claims, 23 Q&A rows, 38 reconciliation rows and 47 question rows. Most cites and all main arithmetic hold. The fresh grep finds units A1 and A2 missed: the CFO's 15% interim ROE milestone (L113), the 75% and 80% LTV caps (L482-L483), and nine forward phrases. One of them is L56, 'reduce our reliance on direct assignment', which A4's DA-reliance contradiction rests on. A2 also left three mixed turns unflagged. So three management numbers sit as analyst numbers and two analyst numbers as management, and question turns are 26, not 23. In A4 the main issue is the yield and spread reading. A4 confirms the CFO's 'optical' yield rise, then cites the 20 bp spread widening as proof that NIM pressure is not yet in the numbers. Ex-DA the spread narrowed 13-20 bps on two of three CoB measures. Other A4 fixes are one-line qualifiers. Nothing changes the protocol verdict, a tripwire or Decision Status. A2 can add rows as in Role 4 loop 1; A4 then aligns without an A3 re-run unless the new rows raise a finding."
```

---

## RE-AUDIT LOOP 1

Date: 2026-10-19 | model: claude-opus-5-5
Artefacts re-read:
- The review after A4's Role 5 loop 1: 1,496 lines. Line numbers in this section are "review Lnnn" on that file. Read in full from L1 to L60 and from L494 to L1495.
- The concall ledger after A2 loop 1: 520 lines, read in full.
- The concall fulltext: 952 lines, read in full again.
- Concall structured rows R119-R132 and R247-R267, plus line-range greps for L105-L107, L416-L419 and L636-L639.
- Presentation structured rows R033, R034, R327, R486, R496, R868 and R869.
- work/blocks/a4.yaml: string spot-check for the loop-1 fix strings (13 hits on 7 strings). Not re-audited line by line.
Not opened: inputs/, any source PDF or audio, A3 forensics, the orchestrator extraction check. No git.
Scope: the 16 prior findings, the style fixes, and every passage that the A2 loop-1 ledger and the review's ROLE 5 LOOP 1 CHANGES list (review L1477-L1495) touched. The prior findings are F6, M7, M8 and M9 (A2), and F7, F8, C4, C5, C6 and M10-M15 (A4).

### R1-0. Deliverable-completeness (re-check)
- narrative: PRESENT. Review L1219-L1234, 15 lines (band 10-20). It now names both open operator rulings (L1234).
- sector: PRESENT. L1236-L1247.
- business_model: PRESENT. L1249-L1261.
- competition: PRESENT. L1263-L1270.
- forward_map: PRESENT. L1272-L1284. One make-or-break metric plus 11 dated catalysts, each with a Bull fork and a Bear fork.

Gate: PASS.

### R1-1. Coverage audit (re-run against the updated ledger)
Method:
- I re-read fulltext L24-L952 in full and re-ran the digit and "?" greps.
- I recounted ledger section 4a (141 rows) and section 4c (8 rows) row by row.
- I read every MFS row at its fulltext line.

| Category | A2 count (loop 1) | Fresh count | Orphan rows | Status |
|---|---|---|---|---|
| participants | 17 | 17 | none | PASS |
| turns (A1 index lines) | 74 | 74 | none | PASS |
| mixed turns flagged | 9 (T22, T26, T33, T47, T50, T51, T54, T62, T71; ledger L18) | 9 | n/a | PASS (M9 closed) |
| question turns | 26 (Q01-Q23 plus Q24 T47 L687-L690, Q25 T50 L723-L726, Q26 T51 L743-L746; ledger L148-L150) | 26 | n/a | PASS (M9 closed) |
| mgmt numbers, on A1 rows | 141 (ledger L300) | 141 on a row-by-row recount of 4a. R121-R123 are in 4a, and R130-R131 have moved to 4c. | n/a | PASS (F6 closed) |
| mgmt numbers, with MFS | 145 (MFS-C1 L57, C2 L113, C3 L482, C4 L483) | 145. Each line holds the number verbatim. | n/a | PASS (M7 closed) |
| repeats and time refs, listed, not counted | 6: MFS-C5 L720, C6 L722, C7 L754, C8 L890, C9 L640, C10 L684 | 6. C5 and C6 repeat R121-R122. C7 and C8 repeat R127 (L730, March "20 to 25 percent") and R128. | n/a | PASS |
| analyst or moderator numbers | 8 (ledger L318) | 8 | n/a | PASS (F6 closed) |
| forward phrases | 58 (49 A1 rows plus MFS-C11 to C19) | 58. Each MFS line holds the phrase: L56, L57, L100, L562, L567, L615, L810, L868-L869 and L893-L894. | n/a | PASS (M8 closed) |
| qualifiers | 22 (21 A1 rows plus MFS-C21 at L715-L716) | 22 counted (candidate ruling below) | n/a | PASS (M8 closed) |
| entities | 35 | 35 | n/a | PASS |
| dates | 14 (13 A1 rows plus MFS-C20 at L270) | 14 | n/a | PASS |
| zero standing | 1 (R100) | 1 | n/a | PASS |
| SPEAKER_INFERRED turns | 52 (22 explicit; ledger L19) | 52 | n/a | PASS |
| rows cited or reviewed in A4 | 267 A1 rows plus 21 MFS rows | 267 plus 21. The review cites MFS-C1 to C4, C11 to C19 and C21 by ID, and C20 by line (5A, Call L268-L271). C5 to C10 fall under the review L21 statement that every A1 and MFS row was read. | none | PASS |

Qualifier candidates. In the prior audit I left three open (L106, L418-L419, L639). I now rule on them against A1's own QUALIFIER rows R247-R267:
- L106, "In spite of the turbulent headwinds over this quarter and lack of momentum and gold prices". This is a framing claim about the quarter. It is not a condition or a definition attached to a metric or a guide; R261, by contrast, conditions the AUM guide. Not a unit. A4 cites it from the fulltext as a claim (Step 1 row 56, 7A L998), which the protocol allows.
- L418-L419, "these would be optically misindicators rather than indicators". The CFO restates R254's "optical indicators" qualifier (L162). It is a repeat: list it, do not count it (S25).
- L639, "So technically they are fixed but they are not". This describes R119's 58% repricing claim. Not a unit.
- Result: qualifiers stay at 22, and my prior "22 or more" closes at 22. No A1 row exists at any of the three lines (grep), so nothing is double-counted.

Coverage: PASS. Orphan rows: none. Rows the ledger lacks: none.

### R1-2. Prior findings: closure status

| ID | Type | Agent | Fix required | Where it stands now (review or ledger lines) | Status |
|---|---|---|---|---|---|
| F6 | FACTUAL | A2 | R121-R123 to management; R130-R131 to analyst | ledger L275-L277 and L315-L316; counts L300, L318; review L21 | CLOSED |
| M7 | MISSING | A2 | NUMBER units L57, L113, L482, L483; repeats and time refs | ledger section 9, MFS-C1 to C10; each read verbatim | CLOSED |
| M8 | MISSING | A2 | 9 FORWARD, 1 DATE, 1 QUALIFIER | ledger MFS-C11 to C21 | CLOSED (qualifier candidates ruled in R1-1) |
| M9 | MISSING | A2 | MIXED_TURN on T47, T50, T51, T54; 26 question turns | ledger L18, L93-L100, L148-L150 | CLOSED |
| F7 | FACTUAL | A4 | 7A core yield PARTIALLY CONFIRMED; tally 22/4; FN-07 level leg; flag 15 fourth drift | L985, L1004, L1126, L46, L1194, YAML L1429, Q38 L575, YAML L1370 | CLOSED |
| F8 | FACTUAL | A4 | levers opex and credit cost named; 150-branch cite at L187-L189 | L858, L717, L574, L815, L1070, L1191, YAML L1426 | CLOSED |
| C4 | CONTRADICTION | A4 | reading (c): gold guide reaffirmed without a number | L706, L726, L729-L730, L746, L768, L780, L926, L1031, L1072, L1125, L534, L572, L1146, L1185, L1240; YAML L1339, L1367, L1390, L1420, L1450 | CLOSED. DROPPED stays a candidate, and row 35 still separates the readings. |
| C5 | CONTRADICTION | A4 | Q10 is B-graded in the refusal line | L826; grades recounted A 2, B 15, C 6 | CLOSED |
| C6 | CONTRADICTION | A4 | brief names both rulings | L1234, L1171, YAML L1413, L1200 | CLOSED |
| M10 | MISSING | A4 | both branch parses | L541, L724, L810, L1143, YAML L1341, L1387 | CLOSED |
| M11 | MISSING | A4 | Rs 289 Cr bar qualifier | L579, L1101, L1140, L1275, YAML L1374, L1384. Every "289" in the review carries the qualifier (grep). | CLOSED |
| M12 | MISSING | A4 | spread counter graft | L859, L1074, L1191, YAML L1426, L1246, L1450 | CLOSED |
| M13 | MISSING | A4 | breakeven qualifier graft | L878, L542, YAML L1342, L816, L1254. The 38% anchor ties to Step 6D L447. | CLOSED |
| M14 | MISSING | A4 | holder-analyst qualifier graft | L831-L832 | CLOSED |
| M15 | MISSING | A4 | Step 1 rows 56-58; counts; 6B | L699-L701, L704, L935-L938, L953, L1115, L1197, YAML L1433 | CLOSED |
| S15-S22 | STYLE | A4 | as logged | L634; L631 and L1109; L830; L1225; L1224; L704; L733; L911 | APPLIED |
| S13, S23 | STYLE | A4, A1 | as logged | not applied; A4 gives the reason at L1493 | CARRIED |

Verbatim checks on the cites A2 and A4 inserted: L56, L57, L100, L106-L107, L110-L113, L187-L189, L248-L249, L270, L292-L293, L480-L483, L517-L518, L539-L541, L562, L567, L571-L573, L615, L687-L695, L714-L722, L743-L746, L754, L810, L868-L869, L890 and L893-L894. All hold. Deck R868 is Q1 FY27 ROE 15.4%, so Step 1 row 58 holds. The stale phrases ("not yet in the numbers", "must rule on one", "Withdrawn without", "confirms 23", "0.33", "38 of 55") are gone from the body. They survive only in the Role 5 merge change log, which is a record.

### R1-3. Arithmetic audit (touched passages)

| Metric | A4 value (review line) | Recomputed | Source line | Status |
|---|---|---|---|---|
| Step 1 quantified share | 39 of 58, 67% (L704) | 19 NO rows (1, 2, 13, 15, 25, 27, 28, 29, 32, 35, 44, 45, 47, 48, 51, 54, 55, 56, 57); 39 / 58 = 67.2% | review L644-L701 | PASS |
| Step 1 forward quantified | 2 of 7, 29% (L704) | forward rows 3, 13, 28, 32, 51, 53, 54; YES at 3 and 53; 2 / 7 = 28.6% | review L646-L697 | PASS (S20 closed) |
| 6B specificity | 17-18 / 58 = 0.29-0.31 (L936-L938) | 16 A1 rows listed, plus MFS-C12 = 17, plus MFS-C15 = 18; unquantified 33 + 7 (+ 1) = 40-41; 17 / 58 = 0.293; 18 / 58 = 0.310 | review L936-L937; ledger L473-L481 | PASS |
| 6C markers | 7 + 8 + 1 = 16 (L941-L943) | management "we believe" at L100, L244, L251, L261, L543, L634, L855 and L892 = 8. L545 ("which believes") and L833 (analyst) are correctly excluded. | fulltext | PASS |
| 0C Q&A span | 52.1 min, 76% (L631) | 01:07:02 - 00:14:54 = 52.13 min; / 68.53 = 76.1% | Call L6, L205, L924 | PASS (S16 closed) |
| 0C prepared remarks | about 13.5 min (L631) | 00:14:46 - 00:01:13 = 13.55 min | Call L37, L202 | PASS |
| 0C question mix | 9 + 14 + 3 = 26 (L632) | primary Q01, Q03, Q06, Q10, Q11, Q14, Q15, Q16, Q20 = 9; follow-ups 23 - 9 = 14; embedded 3 | ledger L125-L150 | PASS |
| 7A tally | 22 / 4 / 2 / 3 / 7 = 38 (L1004) | Counted row by row over L965-L1002. CONFIRMED 22. PARTIALLY CONFIRMED 4 (L982, L985, L986, L988). PARTIALLY CONTRADICTED 2 (L991, L998). CONTRADICTED 3 (L971, L977, L990). UNVERIFIABLE 7 (L974, L980, L987, L999-L1002). | review | PASS |
| 7A core yield ex-DA | about 16.7% in both quarters (L985) | 16.4 + 0.3 = 16.7; 16.7 + 0.0 = 16.7 | Deck R1023-R1024 via L985 | PASS |
| Ex-DA spread change | narrowed about 13-20 bps (L859, L1074, L1191, L1246) | Ex-DA yield is flat. CoB rose 20 bps on slide 25 (7.7% to 7.9%) and 13 bps on the P&L basis (7.74% to 7.87%); daily I-GAAP was flat. On the reported spread instead: +20 - 30 = -10 bps. The 10 bp gap is slide 25 rounding (Q1 7.7 + 8.6 = 16.3 vs 16.4). | review L44, L986 | PASS (within the rounding of a 0.1% series) |
| 4A grade tally | A 2, B 15, C 6 (L826) | counted over L802-L824 | review | PASS |
| 3E tally | 1 / 8 / 4 (L792) | unchanged | review | PASS |
| M13 per-gram anchor | about +38% YoY (L878, L1254) | 1.770 / (1.162 x 1.102) = 1.383 | review L447 | PASS |
| Q36 ROA band | 2.8% at the top of 2.7-2.8% (L573) | 2.4 + 0.30 / 0.40 | review L722 | PASS |
| Ledger 4a / 4c | 141 / 8 | recounted row by row | ledger L159-L299, L310-L317 | PASS |
| Ledger MFS counted | 15 (4 + 9 + 1 + 1); 21 rows | 15 counted, 6 listed not counted, 21 rows | ledger L459-L483 | PASS |

Arithmetic: PASS. No mismatch above rounding.

### R1-4. Adversarial read (re-run on the loop-1 text)
The three surviving counters from the prior audit are now in the review (M12, M13, M14). I tested each graft from the bull side (Rule J symmetry):
- M12. The bull reading uses the CFO's own basis. On the daily I-GAAP CoB (7.80% to 7.79%, Deck R609-R610) the ex-DA spread was flat. The graft says "on two of three measures", so it keeps the bull basis. Holds.
- M13. The bull reading is that the CEO extends the claim to "even the price that is there today" (Call L715-L716), which means a flat price from here. The graft says "a rising or current gold price" and calls the timeline "untested". That is accurate: the claim covers a flat price, and the evidence does not. Holds.
- M14. "This does not show pre-screening" keeps the bull side. Holds.

Definite claims that loop 1 inserted, tested from the bear side:
1. Q41 (review L578), from MFS-C3 and MFS-C4: "90-95% of customers take the maximum, set by exposure slab caps of 75% and 80% (Call L480-L483, MFS-C3, MFS-C4), so most new loans sit at their slab cap."
   - Counter from the same extract: the CEO, in the next answer, says the company plays the LTV "minus or two percent". He says the working mix is "seventy three percent, seventy two percent, seventy four percent" and "it's not everybody at that highest one". Where competition is low, "you play with a 71% also" (Call L497-L506).
   - Filed average gold origination LTV is 72.1% (Deck R327), below both caps. The review itself says the working mix "agrees with origination LTV 72.1%" (L970), and portfolio LTV sits 4.1 pp below origination (L450).
   - If 90% of new loans sat at a 75% cap, the other 10% would need an average LTV of about 46% to give a 72.1% average ((72.1 - 0.9 x 75) / 0.1). Loans at the 80% cap make the gap wider.
   - Survives: YES. It is an internal contradiction (C7). The sentence comes from my own prior audit, the M7 table note on L483 ("most new loans sit at their slab cap"). I withdraw that note.
   - LTV-CREEP itself stands: the working mix of 72-74% and the origination LTV of 72.1% both sit above the 68.0% book.
2. Step 1 L705 and Q36 L573: "'Interim' implies a higher ROE target". Counter: the number is inaudible (Call L736), and "interim" may label the milestone already passed. The review already says the target is inaudible and asks for it (row 36). No graft needed.
3. 2L reading (c) at L730, the gold guide reaffirmed. Counter: L248-L249 sits in a gold-growth answer, but L292-L293 says "on AUM", which may mean the entity guide. The review keeps DROPPED as a candidate and names the separating observation (row 35). Balanced. No graft.

Mandatory acquisition-economics probe: not triggered. The call and the filings show no acquisition, purchase or stake buy (unchanged).

### R1-5. New findings
- C7 (CONTRADICTION, A4). Review L578 (Q41, inserted in loop 1) concludes "so most new loans sit at their slab cap".
  - That conflicts with review L970 and L450, with filed Deck R327 (average gold origination LTV 72.1%, below both caps) and with the CEO at Call L497-L506.
  - Fix at L578. Replace "90-95% of customers take the maximum, set by exposure slab caps of 75% and 80% (Call L480-L483, MFS-C3, MFS-C4), so most new loans sit at their slab cap" with: "Jagdish: 90-95% of customers want the maximum their exposure slab allows, 75% or 80% (Call L480-L483, MFS-C3, MFS-C4). CEO: the company plays the LTV 'minus or two percent', and the working mix is 72-74%, 'not everybody at that highest one' (Call L497-L506). Filed average origination LTV is 72.1% (Deck R327), below both caps. The share of new loans at the cap is ND; this row asks for it."
  - Align in the same edit (dependency rule). Flag 5 (L1184) and its YAML line (L1419) become: "90-95% of customers want the slab maximum, 75% or 80% (Jagdish, Call L480-L483); the CEO puts the working mix at 72-74%, 'not everybody at that highest one' (Call L500-L502); filed origination LTV 72.1% (Deck R327)". Change the YAML Q41 parenthetical (L1373) the same way.
  - No number, flag, protocol verdict, tripwire or Decision Status changes. LTV-CREEP stands.

### VERDICT (re-audit loop 1)

VERDICT: **INCOMPLETE**.

- Deliverable gate: PASS. Coverage: PASS (F6, M7, M8, M9 closed; no orphan row; nothing missing from the ledger). Arithmetic: PASS.
- All 16 prior findings are closed. The three grafts hold when tested from the bull side.
- One new finding: C7 (CONTRADICTION, A4), from a loop-1 insertion at L578, with alignment at L1184, L1419 and L1373. It traces to my own prior M7 note.
- Loop to **A4** only. A2 and A3 have no work. The replacement text is in R1-5.
- No finding changes the protocol verdict (PROCEED WITH FLAGS), a tripwire, the Pillar 2L condition or Decision Status.

### STYLE NOTES (re-audit loop 1; logged, no loop)
- S24: Step 1 L705, "(Call L736; row 36)". In Step 1, bare row numbers mean Step 1 rows, and Step 1 row 36 is Core NII. Write "Step 8.5 row 36".
- S25 (A2 ledger):
  - List Call L418-L419 (the CFO restates R254 "optical indicators", L162) as a qualifier repeat, not counted, as section 9 does for number repeats.
  - Ledger L319, "(4a + 4b) = 141": the 4b rows already sit inside 4a and 4c. Write "4a = 141".
  - Ledger L7 compares 9 index labels with a sweep of 26 under "match: yes". State both counts on one basis.
- S26: Q37 L574 puts "other levers" in quotes for Call L661-L662. The transcript reads "some other operating labor" [ASR: lever]. Quote it verbatim with the gloss, as Exchange 3 does at L856.
- S27: Q14 L815 reads the ASR line "a family object for our credit card" (Call L689-L690) as opex or credit cost with no [ASR] tag. Add the tag. The lever naming also rests on Call L567, which is clear, so no conclusion changes.
- Carried, open: S13 (review L484), S23 (A1 line anchors), S7-S10, S12. S15-S22 are applied and closed.

Re-audit loop 1 YAML block (SUPERSEDED by the Re-audit loop 2 block at the end of this file; kept as the record, fenced as text so that no parser reads it as the current block):

```text
stage: A5-adversary
company: "FEDFINA"
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
  - {claim: "Q41 (review L578, loop-1 insertion): 90-95% of customers take the maximum at the 75% or 80% exposure slab cap, so most new loans sit at their slab cap", counter: "The CEO, in the next answer, says the company plays the LTV 'minus or two percent', the working mix is 72-74%, 'it's not everybody at that highest one', and 71% where competition is low. Filed average gold origination LTV is 72.1%, below both caps; with 90% of loans at a 75% cap the other 10% would need about 46% LTV to give 72.1%. The review itself says the working mix agrees with 72.1% (L970). LTV-CREEP stands on 72-74% and 72.1% vs the 68.0% book", source_line: "Call L480-L483, L497-L506; Deck R327; review L450, L970", type: "CONTRADICTION"}
findings_by_type:
  factual: []
  missing: []
  contradiction:
    - "C7 (A4): review L578 (Q41, inserted in Role 5 loop 1 from MFS-C3/C4) concludes 'so most new loans sit at their slab cap'. That conflicts with review L970 and L450, filed Deck R327 (average gold origination LTV 72.1%, below both the 75% and 80% caps) and the CEO at Call L497-L506 ('not everybody at that highest one'). The sentence traces to A5's own prior M7 note on L483, which A5 withdraws. Fix L578; align flag 5 (L1184), its YAML line (L1419) and YAML Q41 (L1373)"
  style:
    - "S24: Step 1 L705 '(Call L736; row 36)': bare row numbers in Step 1 mean Step 1 rows, and Step 1 row 36 is Core NII; write 'Step 8.5 row 36'"
    - "S25 (A2): list Call L418-L419 (CFO restates R254 'optical indicators', L162) as a qualifier repeat, not counted, as section 9 does for number repeats; ledger L319 '(4a + 4b) = 141' should read '4a = 141' (4b rows already sit inside 4a and 4c); ledger L7 compares 9 index labels with a sweep of 26 under 'match: yes', so state both on one basis"
    - "S26: Q37 L574 quotes 'other levers' for Call L661-L662; the transcript reads 'some other operating labor' [ASR: lever]; quote verbatim with the gloss, as Exchange 3 does at L856"
    - "S27: Q14 L815 reads the ASR line 'a family object for our credit card' (Call L689-L690) as opex or credit cost without an [ASR] tag; add it (the lever naming also rests on the clear Call L567)"
    - "Carried, open: S13 (review L484), S23 (A1 line anchors), S7-S10, S12"
loop_back_to: "A4"
gap: "A4 only, C7. Review L578 (Q41): replace '90-95% of customers take the maximum, set by exposure slab caps of 75% and 80% (Call L480-L483, MFS-C3, MFS-C4), so most new loans sit at their slab cap' with 'Jagdish: 90-95% of customers want the maximum their exposure slab allows, 75% or 80% (Call L480-L483, MFS-C3, MFS-C4). CEO: the company plays the LTV minus or two percent, and the working mix is 72-74%, not everybody at that highest one (Call L497-L506). Filed average origination LTV is 72.1% (Deck R327), below both caps. The share of new loans at the cap is ND; this row asks for it.' Align flag 5 (L1184) and its YAML line (L1419): '90-95% of customers want the slab maximum, 75% or 80% (Jagdish, Call L480-L483); the CEO puts the working mix at 72-74%, not everybody at that highest one (Call L500-L502); filed origination LTV 72.1% (Deck R327)'. Align the YAML Q41 parenthetical (L1373) the same way. No A2 or A3 work. No number, flag, protocol verdict, tripwire or Decision Status change; LTV-CREEP stands."
style_notes:
  - "S24-S27 new (see audit, Re-audit loop 1); S15-S22 applied and closed; S13, S23, S7-S10, S12 carried, open"
  - "Prior qualifier candidates closed against A1's own QUALIFIER rows R247-R267: Call L106 is a framing claim, not a unit; L418-L419 repeats R254 (see S25); L639 describes R119. The qualifier count stays 22"
analyst_note: "Loop 1 closes all 16 prior findings. A2 added the 21 MFS rows I named, re-attributed R121-R123 and R130-R131, flagged four mixed turns and added three question turns. My recount ties: 141 management and 8 analyst numbers on A1 rows, 145 with MFS, 58 forward phrases, 26 questions. A4 made every text fix and graft. The Step 1 share, the 6B ratio, the 7A tally and the grade tally recompute. I closed my three open qualifier candidates against A1's own QUALIFIER rows, and the count stays 22. One new item fails, and it is mine. My prior M7 note said most new gold loans sit at their slab cap, and A4 copied it into Q41. The CEO says the working mix is 72-74% and 'not everybody at that highest one'. The filed average origination LTV is 72.1%, below both caps, and the review itself says the mix agrees with 72.1%. So Q41 contradicts L970. The fix is one sentence plus two flag lines. LTV-CREEP stands. Nothing changes the protocol verdict, a tripwire or Decision Status."
```

---

## RE-AUDIT LOOP 2

Date: 2026-10-19 | model: claude-opus-5-5
Artefacts re-read:
- The review after A4's Role 5 loop 2. Its last text line is L1505 (L1495 in loop 1). Line numbers in this section are "review Lnnn" on that file. Read in full: L1-L30, L560-L589, L695-L735, L805-L824, L1170-L1290 and L1330-L1505.
- work/blocks/a4.yaml: string check of the loop-2 lines (Q41 at L65, flag 5 at L111, role5_loop_2 at L142, analyst_note at L143). The text matches the review YAML.
- Concall fulltext L470-L514, L560-L569, L652-L696 and L730-L739.
- Concall structured turn index, lines 30-37 (T22 to T29). Concall ledger L68-L75 and L455-L520.
- Presentation structured row R327 and presentation fulltext L460-L474.
Not opened: inputs/, any source PDF or audio, A3 forensics, the orchestrator extraction check. No git.
Scope: C7 and its three alignment points; style items S24, S26 and S27; the ROLE 5 LOOP 2 CHANGES list (review L1498-L1505); a regression check that nothing else changed since loop 1.
Line map: the task names L1420 for the flag 5 YAML line. Flag 5 YAML sits at L1419, the line my loop-1 gap named. L1420 is the GOLD-TRIGGER-AT-RISK line. It still carries the loop-1 C4 text. I checked both lines.

### R2-0. Deliverable-completeness (re-check)
- narrative: PRESENT. Review L1219-L1234, 15 lines (band 10-20). It names both open operator rulings (L1234).
- sector: PRESENT. L1236-L1247.
- business_model: PRESENT. L1249-L1261.
- competition: PRESENT. L1263-L1270.
- forward_map: PRESENT. L1272-L1284. One make-or-break metric plus 11 dated catalysts, each with a Bull fork and a Bear fork.

Gate: PASS. Line positions and text are the loop-1 state.

### R2-1. Coverage audit (carried)
A2 did not run in loop 2. The concall ledger still ends at L520. Section 9 (MFS-C1 to C21, ledger L456-L483) and the A2 YAML counts (ledger L493-L517) read as in loop 1. The review preamble (L21) carries the same counts. The A1 files did not change in this loop.

| Category | A2 count | Fresh count (R1-1, checked against the unchanged ledger) | Orphan rows | Status |
|---|---|---|---|---|
| participants | 17 | 17 | none | PASS |
| turns (A1 index lines) | 74 | 74 | none | PASS |
| mixed turns flagged | 9 | 9 | n/a | PASS |
| question turns | 26 | 26 | n/a | PASS |
| mgmt numbers, A1 rows / with MFS | 141 / 145 | 141 / 145 | n/a | PASS |
| analyst or moderator numbers | 8 | 8 | n/a | PASS |
| forward phrases | 58 | 58 | n/a | PASS |
| qualifiers | 22 | 22 | n/a | PASS |
| entities | 35 | 35 | n/a | PASS |
| dates | 14 | 14 | n/a | PASS |
| zero standing | 1 (R100) | 1 | n/a | PASS |
| SPEAKER_INFERRED turns | 52 | 52 | n/a | PASS |
| rows cited or reviewed in A4 | 267 A1 rows plus 21 MFS rows | 267 plus 21. MFS-C3 and C4 stay cited at Q06 (L807) and Q41 (L578). | none | PASS |

Coverage: PASS. Orphan rows: none. Rows the ledger lacks: none.

### R2-2. C7: closure check

| Location | Required (R1-5 and loop-1 gap) | Now | Status |
|---|---|---|---|
| Q41 "Why it matters" cell, L578 | Replace the slab-cap sentence with the R1-5 text | Present, word for word against my loop-1 gap string | CLOSED |
| Flag 5 body, L1184 | Jagdish slab maximum; CEO 72-74%, not everybody at that highest one; Deck R327 72.1% | Present | CLOSED |
| Flag 5 YAML, L1419 | Same | Present; the same line is at a4.yaml L111 | CLOSED |
| YAML Q41, L1373 | Same, plus share at the cap ND | Present; the same line is at a4.yaml L65 | CLOSED |

Cite checks against the fulltext:
- Call L480: "Ninety ninety-five percent of the customers choices to get maximum loan for maximum value for his loan." Call L482-L483: "The moment the exposure of a customer is capped at 75%, he offsores maximum LTV. Similarly, if it is 80% he offsores maximum LTV." This supports "want the maximum their exposure slab allows, 75% or 80%".
- Call L497-L506: "minus or two percent and play with that LTV" (L498); "a mix of that seventy three percent, seventy two percent, seventy four percent" (L500-L501); "So it's not everybody at that highest one." (L502); "you play with a 71% also" (L506). Holds. The flag 5 cite, L500-L502, holds the mix and the "not everybody" sentence.
- Deck R327: "72.1% | Average Origination LTV, Gold Loans" (page 17). Presentation fulltext L468-L473 puts it on the slide that carries Q2 gold disbursal of Rs 5,822 Cr, so it is the Q2 FY27 figure. 72.1% is below both caps.
- Speakers: T25 (L477-L489) is Jagdish Rao. T27 (L495-L506) is Parvez Mulla, MD&CEO. A1 inferred both (SPEAKER_INFERRED; ledger L71 and L73; A1 index lines 33 and 35). The labels "Jagdish" and "CEO" follow A1 and A2. Flag 30 (L1209) carries the speaker-inference caveat.

Consistency:
- The stale clause "so most new loans sit at their slab cap" is gone from the body and the YAML (grep). It survives only in the loop-2 change log (L1500), which is a record.
- The corrected cells now agree with 7A L970 (the working mix agrees with origination LTV 72.1%), 6D L450 (LTV headroom 4.1 pp), 2L L731 (LTV "toward the 72.1% origination level") and the brief L1244 ("New loans run at 72-74%").

C7: CLOSED. LTV-CREEP stands at L1184 and L1419: the 72-74% mix and the 72.1% origination LTV sit above the 68.0% book.

### R2-3. Style items S24, S26, S27

| ID | Line | Now | Check | Status |
|---|---|---|---|---|
| S24 | L705 | "(Call L736; Step 8.5 row 36)" | Step 8.5 row 36 (L573) is the ROA 3% and ROE target question | APPLIED, closed |
| S26 | L574 | "some other operating labor" [ASR: lever] (Call L661-662) | Call L662: "by, you know, enhancing some other operating labor." Verbatim | APPLIED, closed |
| S27 | L815 | "a family object for our credit card" [ASR: read as opex or credit cost; the lever naming also rests on Call L567] | Call L689-L690 and L567 hold | APPLIED, closed |

### R2-4. The ROLE 5 LOOP 2 CHANGES list (review L1498-L1505)
- Item 1 (Q41): matches L578. It says "A5's text verbatim". That holds against my loop-1 gap string, which had lost the quote marks of my R1-5 text (see S29).
- Item 2 (flag 5 body and YAML): matches L1184 and L1419.
- Item 3 (YAML Q41): matches L1373.
- Item 4 (S24, S26, S27): matches L705, L574 and L815.
- Item 5 (alignment): header L3, verdict line L1177, role5_loop_2 at L1450 and the analyst_note at L1451. a4.yaml L142-L143 carry the same two lines.
- Item 6: S25 is not applied. That is correct: S25 is an A2 item and STYLE, so it loops nowhere. The carried list (S13, S23, S7-S10, S12) matches mine.

The list covers every edit I found.

### R2-5. Regression check: nothing else changed
I have no git and no pre-loop-2 copy of the review. A grep of work/ finds the loop-1 change list only in the review and in this audit. I used three tests.
- Line fingerprint. The loop-1 anchors I recorded on the 1,496-line review sit at the same lines now, from L21 to L1449. Examples: L450, L541, L573, L575, L704, L717, L724, L726, L730, L810, L816, L826, L938, L953, L970, L1004, L1115, L1171, L1185, L1191, L1194, L1197, L1200, L1234, L1240, L1246, L1254 and L1275; YAML L1339, L1341, L1342, L1367, L1370, L1374, L1384, L1387, L1390, L1413, L1420, L1426, L1429 and L1433. The loop-1 analyst_note (loop-1 L1450) now sits at L1451, under the new role5_loop_2 line. The loop-1 change list (loop-1 L1477-L1495) now sits at L1478-L1496. The last text line moves from L1495 to L1505: +1 for role5_loop_2 and +9 for the loop-2 change log (a blank, the heading, a blank and six items). So every other edit was in place, line for line.
- Fix strings. The loop-1 fixes are intact: "39 of 58" (L704); "0.29-0.31" (L938, L953, L1115, L1197, YAML L1433); "22 CONFIRMED, 4 PARTIALLY CONFIRMED" (L1004); "A 2 (Q11, Q17), B 15, C 6" and "the B-graded Q10" (L826); both rulings (L1234); the spread graft (L1191, L1246, YAML L1426); the breakeven qualifier (L816, L1254, YAML L1342); the holder-analyst qualifier (L831); the two branch parses (L724, L810, YAML L1387); the Rs 289 Cr qualifier (L579, L1275, YAML L1374, L1384); the gold-guide reading (c) (L726, L730, L1185, L1240, YAML L1420). The stale loop-0 phrases stay out of the body.
- Lines read in full. In L1-L30, L560-L589, L695-L735, L805-L824, L1170-L1290 and L1330-L1505, the only changes against my loop-1 record are at L3, L574, L578, L705, L815, L1177, L1184, L1373, L1419, L1450 and L1451. Each one is in the loop-2 change list.
- Limit: without a diff, an in-place edit outside the lines I read cannot be fully excluded. No test points to one. This is the evidence standard I used in loop 1.

### R2-6. Arithmetic audit (touched passages)

| Metric | A4 value (review line) | Recomputed | Source line | Status |
|---|---|---|---|---|
| Origination LTV vs the caps | 72.1%, below both caps (L578) | 72.1 < 75 < 80 | Deck R327; Call L482-L483 | PASS |
| Working mix | 72-74% (L578, L1184, L1373, L1419) | spoken 73, 72 and 74 | Call L501 | PASS |
| Share wanting the maximum | 90-95% (L578, L1184, L1373, L1419) | "Ninety ninety-five percent" | Call L480 | PASS |
| LTV headroom | 4.1 pp (L450, unchanged) | 72.1 - 68.0 = 4.1 | Deck R327, R501 | PASS |
| Slab-cap test (audit only, from loop 1) | n/a | with 90% of new loans at a 75% cap, the other 10% would need (72.1 - 0.9 x 75) / 0.1 = 46% | Deck R327 | supports the fix |
| A4 analyst_note figures | 12.0 (55%) of 21.8; 24.5% to 20.2%; Rs 1,085 Cr; 20-25% and +30-40 bps vs 20-22% and +20-30 (L1451) | 12.0 / 21.8 = 55.0%; the others as recomputed in loop 1 and loop 0 | review L1182; Deck R680; Call L727-L733 | PASS |

Arithmetic: PASS. No mismatch above rounding.

### R2-7. Adversarial read (loop-2 text)
Loop 2 added no positive claim. It moved one cell toward the filed number and made three style edits. I tested the change from both sides (Rule J symmetry).
1. Bull side: could most new loans still sit at the slab cap? Only if Deck R327 covered another period, or if "working mix" meant something other than new loans. R327 sits on the Q2 FY27 slide with gold disbursal of Rs 5,822 Cr (presentation fulltext L468-L473). The 72-74% is the CEO's own figure for the LTV he plays. The slab-cap test leaves the other 10% at about 46%. The corrected text keeps Jagdish's claim, attributes it, and marks the share at the cap ND, with row 41 asking for it. Holds. No graft.
2. Bear side: does the correction soften LTV-CREEP? No. Flag 5 keeps the 68.0% book against the 72-74% mix, the 72.1% origination LTV and IGL up to 85%. The brief (L1244) keeps "a thinner cushion". No graft.
3. Loop-1 claims (the M12, M13 and M14 grafts; Q36 "interim"; 2L reading (c)): the text is unchanged at L1191, L1246, L816, L1254, L831, L573, L705 and L730. The loop-1 tests stand.

Mandatory acquisition-economics probe: not triggered. The call and the filings show no acquisition, purchase or stake buy (unchanged).

### R2-8. New findings
No FACTUAL, MISSING or CONTRADICTION finding. Two STYLE notes follow.

### VERDICT (re-audit loop 2)

VERDICT: **COMPLETE**.

- Deliverable gate: PASS. Coverage: PASS (carried; the ledger and the A1 files did not change). Arithmetic: PASS.
- C7 is closed at all four points: L578, L1184, L1419 and L1373. All 16 loop-0 findings stay closed (R1-2).
- S24, S26 and S27 are applied and closed. Two new STYLE notes (S28, S29) are logged. They loop nowhere.
- loop_back_to is empty. The review may proceed to the Notion save, after the operator approves the printed payload in this run.
- No finding changes the protocol verdict (PROCEED WITH FLAGS), a tripwire, the Pillar 2L condition or Decision Status.

### STYLE NOTES (re-audit loop 2; logged, no loop)
- S28: 4A Q06 (L807) still reads "90-95% take the maximum; LTV set by exposure slab caps of 75% and 80%". Q41 and flag 5 now say "want the maximum". L807 is a fair summary of Call L480 ("choices to get maximum loan"). Q07 (L808) records the CEO's 72-74% on the next row. No fact changes. To keep one meaning in all three cells, write "90-95% want the maximum their exposure slab allows, 75% or 80%".
- S29 (my own replacement text):
  - Q41 (L578) and flag 5 (L1184, YAML L1419) state the 72-74% working mix twice: once in the clause A4 already had, once in my CEO sentence. Drop one.
  - My loop-1 gap string lost the R1-5 quote marks round the transcript phrases "minus or two percent" and "not everybody at that highest one" (L578, L1184, L1373, L1419). Restore them. Gloss the first as [ASR: plus or minus two percent], as Q07 (L808) reads it.
- Closed: S24, S26, S27 (applied in loop 2). S15-S22 (closed in loop 1).
- Carried, open: S13 (review L484), S23 (A1 line anchors), S25 (A2 ledger), S7-S10, S12.

```yaml
stage: A5-adversary
company: "FEDFINA"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
verdict: COMPLETE
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
  factual: []
  missing: []
  contradiction: []
  style:
    - "S28: 4A Q06 (review L807) still reads '90-95% take the maximum; LTV set by exposure slab caps of 75% and 80%' while Q41 (L578) and flag 5 (L1184, YAML L1419) now say 'want the maximum'. L807 fairly summarises Call L480, and Q07 (L808) records the CEO's 72-74% on the next row, so no fact changes. Write '90-95% want the maximum their exposure slab allows, 75% or 80%'"
    - "S29 (A5's own C7 replacement text): Q41 (L578) and flag 5 (L1184, YAML L1419) state the 72-74% working mix twice; drop one. The loop-1 gap string lost the quote marks round the transcript phrases 'minus or two percent' and 'not everybody at that highest one' (L578, L1184, L1373, L1419); restore them and gloss the first [ASR: plus or minus two percent], as Q07 (L808) reads it"
    - "Carried, open: S13 (review L484), S23 (A1 line anchors), S25 (A2 ledger), S7-S10, S12"
loop_back_to: ""
gap: ""
style_notes:
  - "S28, S29 new (Re-audit loop 2); S24, S26, S27 applied and closed (review L705, L574, L815); S15-S22 closed in loop 1; S13, S23, S25, S7-S10, S12 carried, open"
  - "Resolved and carried as resolved: C7 (loop-1 CONTRADICTION) closed at review L578, L1184, L1419 and L1373 (the task's L1420 is the unchanged GOLD-TRIGGER-AT-RISK YAML line); all 16 loop-0 findings (F6, M7, M8, M9, F7, F8, C4, C5, C6, M10-M15) stay closed"
analyst_note: "Loop 2 closes C7. A4 put my text into Q41 (L578) and aligned flag 5 (L1184), its YAML line (L1419) and the YAML Q41 question (L1373); a4.yaml carries the same lines. Each cite holds: Call L480-L483 (90-95% want the maximum; 75% and 80% caps), Call L497-L506 (CEO: 72-74% mix, 'not everybody at that highest one') and Deck R327 (72.1% average gold origination LTV, Q2 slide). The cells now agree with 7A L970, 6D L450 and the brief. S24, S26 and S27 are applied verbatim. With no git and no pre-loop-2 copy, I tested regression by line fingerprint and fix strings. Every loop-1 anchor still sits at its line up to L1449. The last text line moves from L1495 to L1505: +1 for role5_loop_2, +9 for the loop-2 change log. Every edit I found is in that log. An unlisted in-place edit outside the lines I read cannot be fully excluded; nothing points to one. Two STYLE notes: Q06 still says 'take the maximum', and my own replacement text repeats 72-74% and lost its quote marks. Verdict COMPLETE."
```
