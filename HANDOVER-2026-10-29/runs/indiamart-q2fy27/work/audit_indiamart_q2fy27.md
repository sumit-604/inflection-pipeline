# A5 ADVERSARY AUDIT: IndiaMART InterMESH Limited (INDIAMART) | Q2 FY27 | claude-opus-5-5

Inputs read: A4 review (runs/indiamart-q2fy27/work/review_indiamart_q2fy27.md, 1,148 lines), A1 fulltexts and structured files for results, presentation, press release, concall and full statements, and the four A2 ledgers. No source PDF and nothing under inputs/ was opened. A3 reasoning was not read. Every figure below was re-derived from A1 rows.

Anchor key: REV Lnnn = A4 review line. RES / DECK / PR / CC / FS Rnnn = A1 structured row. FT Lnnn = A1 fulltext line of that document. Units: RES and FS in INR million, DECK and PR in Rs Cr.

---

## AUDIT 0: DELIVERABLE-COMPLETENESS (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT (REV L962-979, 17 lines, inside the 10-20 band) | sector PRESENT (REV L981-990) | business model PRESENT (REV L992-1009) | competition PRESENT (REV L1011-1021) | forward map PRESENT (REV L1023-1034; 10 catalysts, each with a Bull and a Bear fork; 7 dated or implied-dated, 3 honestly marked undated). **Gate: PASS.**

---

## AUDIT 1: COVERAGE

Fresh pass method: grep of the A1 fulltexts for note headings, question intros, hand-offs and page markers; grep of the A1 structured files for row IDs and flags; diff against each A2 count test.

| Category | A2 count | Fresh count (A5) | Orphan rows | Status |
| --- | --- | --- | --- | --- |
| Results row IDs | 849 | 849 (grep `^R` in results structured) | none | PASS |
| Results numbered notes | 11 | 11 (consol 1-5 FT L518-539; SA 1-6 FT L888-910) | none | PASS |
| Results unnumbered footnotes | 5 | 5 (segment a-c FT L507-513; CF footnote rows R820, R835) | none | PASS |
| Results ZERO_STANDING | 26 | 26 | none | PASS |
| Concall row IDs | 614 | 614 | none | PASS |
| Concall turns | 17 | 17 (hand-offs FT L32, L79, L103, L133, L141, L156, L254, L409, L455, L571, L597, L630, L696, L724, L814, L826 plus IR open) | none | PASS |
| Concall questions | 9 | 9 (intros FT L141, L254, L409, L455, L571, L597, L630, L696, L724) | none | PASS |
| Deck row IDs | 1,620 | 1,620 | none | PASS |
| Deck slides | 69 | 69 (`[page n]` markers) | none | PASS |
| **Deck ZERO_STANDING** | **0 ("none found", deck ledger L8, L243-244)** | **8 (DECK R480-R481 p38 FT L844; R617-R622 p39 FT L895)** | n/a | **FAIL: A2 (MISSING)** |
| PR row IDs | 140 | 140 | none | PASS |
| PR pages | 5 | 5 | none | PASS |
| PR ZERO_STANDING | 3 | 3 (R127-R129) | none | PASS |
| Full statements | no A2 ledger (orchestrator scope) | FS SA note 7 sub-notes (i), (ii), (v) are rowed by A1 (FS R1059-R1064, R1114-R1127, R2107-R2110, R2962, R2964, R2973; FT L3267-3275) but absent from A4 | n/a | **FAIL: A3 (MISSING)** |
| A4 unit coverage | 11 notes / 17 turns / 74 slides | REV L15 marks all reviewed; REV 0D (L58-73) cites all 16 note units; REV 4A (L699-709) cites Q1-Q9 with turn refs | none | PASS |

Notes on the two FAIL rows:
- Deck ZERO_STANDING. The 8 IDs sit in the deck ledger as plain NUMBER rows, so no ID is orphaned. The ledger count test asserts 0 and passes its own gate on a false count. A4 disclosed this (REV L17). Fix is ledger-only; nothing downstream changes.
- Full statements. FS SA note 7(i): 1,172 OCDs of Livekeeping at INR 51,167 = 59.97 mn (FT L3267). Note 7(ii): 7,600,000 OCDs of Tradezeal Online at INR 25 = 190.00 mn (FT L3268; RPT R2107/R2109). Note 7(v): 7,870,000 Tradezeal OCCRPS converted 1:1 to equity (FT L3274-3275). A4 never names Tradezeal or the Livekeeping OCDs (grep of REV: no match). Two consequences follow from the extract:
  1. SA H1 investing outflow RES R667 = 1,020 mn reconciles to Fleetx 649.88 + Tradezeal 190.00 + IndiaMart Finance 120.50 + Livekeeping 59.97 = 1,020.35 mn [derived]. The listed company did not pay the Agillos 172.47 mn; a subsidiary did. This answers part of REV Q14 (L513) from the filing.
  2. IndiaMART put Rs 6.0 Cr of fresh money into Livekeeping in H1. Livekeeping carries a 5.3 Cr impairment allowance and sits under thesis-broken #11 scrutiny (REV L404). A4's #11 row omits the new funding.

Observation, no finding: the FS structured file is a declared targeted extraction (FS structured L8-11). Notes 21-24 are out of its scope. Note 24 (other expenses) columns are scrambled in the fulltext: SA "Advertisement expenses 202.28" (FT L3799) and consolidated "Advertisement expenses 2.94" (FT L1783) cannot both be aligned. The advertising line is unresolvable without an A1 render check. A4's only use of note 24, the 16.0 Cr Q2 FY26 SA impairment, is corroborated by structured rows: SA other expenses Q1 FY26 63.1 Cr (RES R162 less R160) vs Q2 FY26 87.9 Cr (R160), and SA cash-flow impairment 160 mn H1 FY26 (R632).

---

## AUDIT 2: ARITHMETIC

All values recomputed from A1 rows. Tolerance = rounding of the displayed precision.

| Metric | A4 value (REV line) | Recomputed | Source | Status |
| --- | --- | --- | --- | --- |
| 1-C consolidated P&L, all 7 columns x 13 lines | REV L90-106 | every cell matches INR mn / 10 | RES R001-R121 FT L341-376 | PASS |
| 1-S standalone P&L, all cells | REV L115-129 | every cell matches | RES R122-R230 FT L778-811 | PASS |
| Consol op EBITDA Q2 FY26 / Q1 / Q2 FY27 / FY26 / H1 FY26 / H1 FY27 | 129.7 / 146.5 / 159.2 / 530.0 / 263.2 / 305.7 (L140) | 1,320+72+7-102=1,297; 2,463+64+5-1,067=1,465; 1,447+64+5+76=1,592; 5,300; 2,632; 3,057 | RES R049, R031, R025, R007; ties segment R297-R302 FT L485 | PASS |
| Consol op EBITDA margin | 33.2 / 35.4 / 37.1 / 33.8 / 34.5 / 36.3% (L141) | 33.17 / 35.35 / 37.14 / 33.78 / 34.49 / 36.26% | as above / RES R001-R006 | PASS |
| Consol core PBT ex-OI | 108.4 / 125.0 / 137.0 / 443.8 / 219.9 / 262.0 (L143) | 1,186-102; 2,317-1,067; 1,294+76; 6,479-2,041; 3,225-1,026; 3,611-991 | RES R061-R066, R007-R012 | PASS |
| Consol ETR | 30.3 / 25.7 / 29.8 / 26.7 / 26.8 / 27.2% (L146) | 359/1,186=30.27; 595/2,317=25.68; 386/1,294=29.83; 26.73; 26.76; 27.17 | RES R079-R084 | PASS |
| SA op EBITDA and margin | 115.0 / 149.3 / 156.4; 31.9 / 39.7 / 40.2% (L155-156) | 1,187+36+7-80=1,150; 2,343+26+5-881=1,493; 1,446+26+6+86=1,564; 31.92 / 39.72 / 40.21% | RES R170, R152, R146, R128 | PASS |
| SA ex-impairment Q2 FY26 base | 131.0 (36.4%) (L157) | 1,150+160=1,310; 1,310/3,603=36.36% | RES R632; FS FT L3813-3815 | PASS |
| S-vs-C PAT gap Q2 FY27 / Q1 / Q2 FY26 / LFL / H1s / FY26 | -14.6 / -2.2 / -1.0 / -16.9 / -6.9, -5.3 / -9.6% (L166-174) | -155/1,063; -39/1,761; -8/835; -16.8/99.5; -194/2,824, -133/2,495; -505/5,252 | RES R085-R090, R194-R199 | PASS |
| Consol YoY: revenue / op EBITDA / margin / core PBT / PBT / PAT / EPS | +9.6% / +22.7% / +397 bps / +26.4% / +9.1% / +9.8% / +9.6% (L188-199) | 4,286/3,910; 1,592/1,297; 37.14-33.17; 1,370/1,084; 1,294/1,186; 908/827; 15.09/13.77 | RES as above | PASS |
| SA YoY reported and like-for-like | +36.0 / +19.4%; +829 / +385 bps; PAT +27.3 / +6.8% (L209-217) | 1,564/1,150; 1,564/1,310; 8.29pp / 3.85pp; 1,063/835; 1,063/995 | RES R170-R199; R632 | PASS |
| Consol sequential margin | +175 bps (L225) | +179 bps (35.35% to 37.14%) | RES R002, R050, R001, R049 | PASS within displayed rounding (37.1 less 35.4 = 170 +/- 10); STYLE S1 |
| SA sequential margin | +50 bps (L225) | +49 bps | RES R123, R171, R122, R170 | PASS |
| Rolling 4Q other income | 200.6 Cr (L229) | 2,041-1,026+991=2,006 | RES R012, R011, R010 | PASS |
| Equity factor funds Mar-26 to Sep-26 | 331.7 to 468.1 Cr, 15.6% (L229) | 3,316.79 to 4,680.65 mn (9 funds); 4,680.65/30,087=15.56% | FS R665-R812 (factor rows); RES R405 | PASS |
| Arbitrage funds | 299.5 to 89.1 Cr (L229) | 2,995.48 to 891.05 mn (5 funds) | FS R621-R748 | PASS |
| H2 FY26 derived | 805.9 / 266.8 (33.1%) / 223.9 (L245) | 15,690-7,631; 5,300-2,632; 4,438-2,199 | RES | PASS |
| SA deferred-revenue recognition | 18.6% (Q1 18.7%) (L251, L508) | 389 x 89% / 1,858 = 18.63%; 376 x 91% / 1,832 = 18.68% | DECK R984, R989, R965, R983, R988, R964 | PASS |
| PAT bridge Q2 YoY, 8 lines | foots to +81.0 mn (L261-272) | 124.7+170.3+8+2-178-19-32.7+5.7 = 81.0; PAT 908-827 = 81 | RES R001-R087 | PASS |
| QoQ bridge | -814 = +127 - 1,143 - 7 + 209 (L274) | matches | RES R002, R008, R056, R080 | PASS |
| OI-reversion PAT | 1,041 mn (L278) | 908 + 178 x 0.7483 = 1,041.2 | RES R009, R007 | PASS |
| CFO / CFO-PAT / FCF H1 | 298.8 / 1.14x / 297.9 (L293-297) | 2,988; 2,988/2,630; 2,988-9 | RES R577, R088, R581 | PASS |
| Rolling CFO/PAT | 1.43x (L295) | (129+290+163+135)=717 / (238.5+263.0)=501.5 = 1.430 | DECK R1324-R1327; RES R090, R089, R088 | PASS |
| WC inflow / contract-liability build | 60.6 to 54.4; 72.8 to 63.7 (L298-299) | 3,416-2,810; 3,722-3,178; R570 728; R569 637 | RES R557-R574 | PASS |
| Receivable / payable days | 0.9 / 35.1 days (L300-302) | 42/8,430 x 183 = 0.91; 369/1,923 x 183 = 35.1 | RES R407, R441, R443, R040 | PASS |
| Net cash Sep-26 / Mar-26 | 3,048.3 / 3,097.5 (L306) | 30,087+381+216-90-111 = 30,483; 30,294+804+108-131-100 = 30,975 | RES R405-R440 | PASS |
| Deferred revenue and days | 2,028.9 Cr; about 440 days (L303) | 7,843+12,446 = 20,289; 2,028.9/1,686 x 365 = 439 | RES R431, R447 | PASS |
| SA CFO / CFO-PAT / investees / dividends | 276.8 / 0.98x / 102.0 / 360.7 (L313-317) | R657 2,768; 2,768/2,824; R667 1,020; R679 3,607 | RES | PASS |
| Associate concentration | 69.5% of 28.1 Cr (L176) | (102.48+93.03)/281.44 = 69.5% | FS R174/R175 (965.21-862.73); FS FT L1159 (238.48-145.45); FS R007 | PASS |
| Unaudited share of PAT | 16.9% (L75); 18.3% incl other-auditor subs (L516) | 153.60/908; (153.60+12.96)/908 | FS R006; RES R694 | PASS |
| Other-auditor subs | 4.7% of assets; Q1 loss 6.5 Cr (L517) | 2,160.49/46,088; 77.71-12.96 = 64.75 | RES R691, R421, R694, R695 | PASS |
| Strategic deployment | 82.2 Cr Q2; +75% YoY (L944) | 649.88+172.47 = 822.35; 822/471 = +74.5% | FS R2005, R2009; RES R597, R598 | PASS |
| Busy Q1 billing growth from deck | about 9% (L520) | Q1 FY26 = 170-38-33-45 = 54; 59/54 = +9.3% | DECK R1160-R1164 | PASS |
| Busy cost growth | 38% vs revenue 27% (L519) | printed | DECK R1204, R1170 | PASS |
| H1 consolidated collections | +8.5% (L507) | (463+443)/(430+406) = +8.4% | DECK R663, R664, R667, R668 | PASS (rounded quarterly inputs) |
| Credibility ratio | 41.7% (L681) | 2.5 / (15-9) | REV L656-672 | PASS |
| Quantified share; specificity | 18/22 = 82%; 10/22 = 0.45 (L619, L798) | recount of REV tables | REV L595-616, L798 | PASS |
| Q&A share of call | about 84% (L582) | 55.1 / 65.8 min | CC R001; FT L141, L814 | PASS |
| Price framing | 21.9% / 9.3% / 36.7% / 2.2% below or above anchors (L481) | 1,573 vs 2,015 / 1,439 / 1,151 / 1,539 | session facts, SECONDARY | PASS (internal) |
| Market cap | Rs 9,469 Cr (L481) | 1,573 x 6.0143 Cr filed shares = Rs 9,460.5 Cr | DECK R1292 | STYLE S6 (session fact, 0.09%) |
| **Prior-question tally (Step B3E)** | **4 answered (two by filing only), 12 partial, 3 evaded, 12 not addressed (L693)** | **4 answered (three by filing only: Q14, Q18, Q19; plus C-8), 10 partial, 3 evaded, 14 not addressed** | **REV own table L420-444** | **FAIL: A4 (CONTRADICTION)** |
| **Brief: deferred-revenue build** | **"deferred revenue of Rs 2,028.9 Cr ... The prepaid book grew only Rs 5 Cr" (L994-998)** | **Consolidated book 2,014 to 2,029 = +Rs 15 Cr (+1%, PR R117). Rs 5 Cr is the standalone book** | **DECK R526/R527 FT L850; DECK R965/R966 FT L1091** | **FAIL: A4 (FACTUAL)** |

Reading errors found while auditing (not arithmetic, logged here because they change a filed reading):

| Item | A4 statement | Extract | Status |
| --- | --- | --- | --- |
| Busy deferred revenue +40% YoY | "YES (YoY call-only)" (L604); "Deck prints level 155, no YoY ... UNVERIFIABLE" (L821) | Deck p9 prints "155 Cr ... 40% YoY" (DECK R057/R058, FT L213-215) | **FAIL: A4 (FACTUAL).** Status should be CONFIRMED |

---

## AUDIT 3: ADVERSARIAL READ

### Claim 1 (most positive): "Operations are stronger than the headline: core PBT ex-OI +26.4%, op EBITDA +22.7%, margin 37.1%" (REV L195 "Real operating growth"; L898)

Bear counter from the same extract. The gain is cost-led and partly mechanical. Employee cost is flat YoY (RES R019/R021) with headcount -6% (DECK R280). H1 share-based payment fell 5.7 Cr (RES R553/R554: 120 vs 177 mn). D&A fell 1.3 Cr in H1 (R034/R035). Management says the margin is elevated because "we are not investing heavily on the sales side" and that margins "are never comparable" because revenue lags cost by up to 18 months (CC FT L446-451). On filed H1 numbers, core PBT ex-OI grew +19.1% (2,620 vs 2,199). Holding SBP and D&A at H1 FY26 levels, it grows about +16.0% [derived: (2,620-57-13)/2,199].

Survives? Yes, in substance. Already grafted: REV L226 ("real but cost-led"), L228 (D&A "must not be credited"), L281 (SBP down a third, margin line "least durable"), L453 and L522 (SBP tailwind reverses). **No graft required.** STYLE S8 asks A4 to print the ex-SBP, ex-D&A figure beside +26.4%.

### Claim 2: "Cash conversion classification: STRUCTURAL", rolling CFO/PAT 1.43x (REV L325, L898)

Bear counter. H1 CFO grew +8.6% (RES R577/R578) against core PBT +19.1%. The contract-liability build supplied 21% of H1 CFO (63.7 of 298.8 Cr) and fell 12.5% (RES R569/R570). The standalone book grew Rs 5 Cr QoQ (DECK R965/R966). With paying suppliers down four straight quarters (DECK R307-R310), the float build is the CFO line at risk.

Survives? Partly. The float slowdown is real, but the classification holds: rolling 1.43x, capex 0.9 Cr (R581), receivables 4.2 Cr against 2,028.9 Cr of prepayments. A4 already states the slowdown and its cause (REV L298-299, L321). **No graft required.**

### Claim 3: ARPU expansion "ON TRACK, now load-bearing alone" (REV L412); brief: "Growth now comes from price, not from more paying suppliers. [FILED]" and "Top accounts pay 12% more than a year ago. [FILED]" (REV L1000-1001)

Bear counter. The deck's ARPU is revenue per paying supplier: 72K (DECK R257) x 217K suppliers (R246) = Rs 1,562 Cr, about 4 x the Q2 SA revenue of 389 Cr (R984). Its +10% YoY (R258) is SA revenue +8% (R991) divided by a supplier base that fell 2% (R247). Top-10% ARPU (R268/R269) is a moving cohort: the top tenth of 217K accounts, not the same accounts as a year ago. Management says silver numbers "have not improved", gold/platinum numbers "are also stagnant" (CC FT L625-627), and that it does not want to "stress" price further (FT L614). When low-ARPU silver suppliers churn out, ARPU rises with no price change. The filing cannot split list price, tier mix and churn survivorship. A4's own Q7 (REV L506) asks management for that split.

Survives? **Yes.** The [FILED] tags on "growth comes from price" and "top accounts pay 12% more" claim more than the filing shows. Part of the ARPU gain may be the volume loss showing up as a per-supplier gain. **Graft into A4 (FACTUAL):** retag both brief lines [INFERENCE] or restate as "revenue per paying supplier rose 10% while the base shrank 2%". Add the survivorship reading to REV 6D trigger 1 (L412) and to Q7's fork (L506).

### Mandatory acquisition-economics probe

The extract describes two stake purchases in Q2 FY27.

**Fleetx (associate, follow-on).**
- Consideration: 4,630 CCPS at INR 140,362 (INR 10 face plus INR 140,352 premium) = 649.88 mn = Rs 65.0 Cr. Stake rose from 22.25% to 25.80% fully diluted (FS FT L1174-1175).
- Implied value: IndiaMART's Fleetx shares total 24,713 (10,323 + 3,805 + 2,226 + 808 + 2,921 + 4,630). Units x price reproduce each FS amount exactly (FS FT L1158-1165). At 25.80% that implies 95,787 fully diluted shares, about **Rs 1,344 Cr** at the round price [derived].
- Earnings: the group's share of Fleetx loss was 93.03 mn in H1 (cumulative (238.48) vs (145.45), FS FT L1159). At a 22.25-25.80% stake that implies a Fleetx H1 net loss of about Rs 36-42 Cr, roughly Rs 72-84 Cr annualised [derived]. **Price / PAT: not meaningful (loss-making). Implied value / annualised loss is about -16x to -19x.**
- Quality markers: revenue, ROCE, debt, cash and customer tenure are not disclosed in any extract (A4 monitor #12, REV L385).
- Price history: the Q2 price equals the previous tranche (2,921 CCPS, 410.00 mn, already held at Mar-26). It is +50% on the INR 93,575 tranches and 2.1x the INR 67,430 tranche. If IndiaMART alone had subscribed, its stake would be 26.04%, against 25.80% stated, so outside money in the round was small [INFERENCE].
- Bear reading **survives**. This is a flat-price, mostly insider follow-on into a company losing about Rs 75-85 Cr a year, at a Rs 1,344 Cr implied value, with no revenue in the filing to test the price. Cumulative cost is Rs 226 Cr (DECK R152); equity-method carrying value is about Rs 195 Cr (2,189.00 less 238.48 mn) [derived]. **Graft into A4 (MISSING):** state the implied value, the loss-based multiple and the flat-round fact next to Q14 (REV L513) and Flag 9 (L944).

**Agillos E-Commerce / Aerchain (associate, secondary purchase).**
- Consideration: 172.47 mn = Rs 17.25 Cr paid "to various shareholders" for 3.7% (FS FT L1180-1181; DECK R147, R178). Transfer completed 5-Oct (FS) or 7-Oct (deck).
- Implied value: 172.47 / 0.037 = about **Rs 466 Cr** for 100% [derived].
- Earnings: Agillos revenue and PAT are NOT FOUND (FS cons note 7 Agillos block FT L1135-1139 is layout-scrambled; the deck gives cost and stake only). **Price / PAT: not computable.**
- Entry comparison: the deck carries Agillos at Rs 43 Cr cost for 26.9% (DECK R166/R167). If that cost includes this tranche, the earlier 23.2% cost about Rs 25.75 Cr (about Rs 111 Cr implied). If it excludes it, about Rs 185 Cr implied. **The secondary price is about 2.5x to 4.2x IndiaMART's own average entry value** [derived].
- Payer: not the listed company. SA investing outflow reconciles without it (Audit 1) [derived].
- Bear reading **survives**. IndiaMART bought out undisclosed sellers, through a subsidiary, at a multiple of its own entry price, and the extract offers no earnings basis. **Graft into A4 (MISSING):** state the implied value and the step-up range in Q14 and Flag 9. Keep the related-party question open.

---

## FINDINGS (tagged)

| # | Type | Agent | Finding | Lines |
| --- | --- | --- | --- | --- |
| M1 | MISSING | A2 | Deck ledger ZERO_STANDING count 0 / "none found" vs 8 A1 tags (R480-R481, R617-R622). IDs present only as NUMBER rows. Ledger-only fix | deck ledger L8, L243-244; DECK structured L491-492, L628-633 |
| M2 | MISSING | A3 | FS SA note 7(i), (ii), (v) unreviewed: Livekeeping OCD 59.97 mn, Tradezeal OCD 190.00 mn, OCCRPS conversion. Consequences: Livekeeping funding missing from #11 (REV L404); SA outflow 1,020.35 mn reconciliation shows a subsidiary paid Agillos (REV Q14 L513) | FS FT L3267-3275; FS R1059-R1064, R1121-R1127, R2107-R2110, R2962, R2964, R2973; RES R667 |
| F1 | FACTUAL | A4 | Busy deferred revenue +40% YoY is printed in the deck. A4 calls it call-only and UNVERIFIABLE | REV L604, L821; DECK R058 FT L215 |
| F2 | FACTUAL | A4 | Brief attributes the standalone Rs 5 Cr QoQ build to the consolidated Rs 2,028.9 Cr book. The consolidated build was Rs 15 Cr | REV L994-998; DECK R526/R527, R965/R966 |
| F3 | FACTUAL | A4 | Surviving bear counter, claim 3: ARPU "growth comes from price" and "top accounts pay 12% more" tagged [FILED] without filed support. Survivorship reading missing | REV L412, L506, L1000-1001; DECK R246, R247, R257, R258, R991; CC FT L614, L625-627 |
| C1 | CONTRADICTION | A4 | Step B3E question tally (4/12/3/12, "two by filing") contradicts A4's own table (4/10/3/14, three by filing) | REV L693 vs L420-444 |
| M3 | MISSING | A4 | Acquisition probe: Fleetx implied value about Rs 1,344 Cr on an annualised loss of about Rs 72-84 Cr, flat to prior tranche; Agillos implied about Rs 466 Cr, 2.5-4.2x own entry, earnings NOT FOUND. Neither stated in A4 | FS FT L1158-1165, L1174-1175, L1180-1181; DECK R147, R152, R166-R167 |

## VERDICT

**VERDICT: INCOMPLETE.** Loop back to **A2** as the earliest failing agent. Then A3 and A4 in sequence.
- A2 (MISSING M1): restate the deck ledger ZERO_STANDING section and count test (8 rows). No A3/A4 input changes from this alone.
- A3 (MISSING M2): add FS SA note 7(i)/(ii)/(v) forensics, the R667 reconciliation, and the Livekeeping link to #11.
- A4 (FACTUAL F1, F2, F3; CONTRADICTION C1; MISSING M3): correct the Busy reconciliation, the brief's deferred-revenue basis and the B3E tally. Graft the ARPU survivorship counter and the Fleetx/Agillos purchase economics.

What holds: every P&L, margin, YoY, bridge, cash and S-vs-C figure recomputes. The #6 FIRED AS WRITTEN flag, the Decision Status handling (HELD, unchanged) and the OR-30 deferrals are sound.

## STYLE NOTES (logged, no re-run)

- S1. REV L225: print the consolidated sequential margin as +179 bps (35.35% to 37.14%), consistent with the precise bps used at L190, L210.
- S2. REV L943 and YAML L1130: "associates 15.3 Cr, +20% QoQ" pairs the reported level with ex-MonotaRO growth. The reported line is +4.8% (RES R056 146 to R055 153). +20.2% holds on the seven continuing associates (127.84 to 153.60 mn, FS R006/R007 and the 17.69 mn stub R009). State the basis, as Q13 (L512) already does.
- S3. REV L321 and L507: "smallest of five quarters" / "smallest build in five quarters". DECK R962-R966 give four QoQ builds (+21, +178, +26, +5).
- S4. Concall anchors with fulltext numbers under the L label: "CC L173" (REV L344, L832; the Google AI Overview line is FT L173 = L155) and "CC L152-159" (REV L778, L829; the competitor question is FT L151-159 = L133-141).
- S5. REV L425 and L788: the "We don't know" quote (FT L686) answers a question on silver-churn improvement timing (FT L682-683). Mapping it to net-adds timing is defensible through CC R177 (FT L403), but say so.
- S6. REV L481: market cap Rs 9,469 Cr (session fact) vs CMP x filed shares Rs 9,460.5 Cr (DECK R1292). Ex-cash value would be about Rs 1,035.
- S7. REV L384: "run-rate above the 50-55 Cr band" names a band absent from the item's own thresholds (green <40, red >65). Anchor it or drop it.
- S8. REV L195 and L898: show H1 core PBT ex-OI growth of about +16.0% with SBP and D&A held at H1 FY26 levels, beside the +26.4% Q2 headline.

---

```yaml
stage: A5-adversary
company: "INDIAMART"
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
    - "DECK R480, R481, R617, R618, R619, R620, R621, R622: ZERO_STANDING category absent from deck ledger (count test says 0 / none found); IDs present only as NUMBER rows"
arithmetic_mismatches:
  - {metric: "Prior-question answer tally (Step B3E)", a4_value: "4 answered (two by filing only), 12 partial, 3 evaded, 12 not addressed", recomputed: "4 answered (three by filing only), 10 partial, 3 evaded, 14 not addressed", source_line: "review L693 vs review table L420-444"}
  - {metric: "Brief: QoQ build of the Rs 2,028.9 Cr consolidated deferred-revenue book", a4_value: "Rs 5 Cr", recomputed: "Rs 15 Cr (2,014 to 2,029); Rs 5 Cr is the standalone book", source_line: "review L994-998; DECK R526/R527 FT L850; DECK R965/R966 FT L1091"}
surviving_bear_counters:
  - {claim: "ARPU expansion ON TRACK; brief 'growth now comes from price' and 'top accounts pay 12% more' [FILED] (review L412, L1000-1001)", counter: "ARPU = revenue per paying supplier; +10% = SA revenue +8% over a base -2%; top-10% ARPU is a moving cohort; silver not improved, gold/platinum stagnant; price vs mix vs churn survivorship not separable from the filing", source_line: "DECK R246, R247, R257, R258, R991; CC FT L614, L625-627", type: FACTUAL}
  - {claim: "Fleetx follow-on Rs 65.0 Cr framed as strategic capital (review Flag 9 L944, Q14 L513)", counter: "Flat-price, mostly insider round at INR 140,362/share; implied value about Rs 1,344 Cr; Fleetx H1 loss about Rs 36-42 Cr (annualised Rs 72-84 Cr); price/PAT n.m.; revenue, ROCE, debt, cash not disclosed", source_line: "FS FT L1158-1165, L1174-1175, L1159; DECK R152", type: MISSING}
  - {claim: "Agillos 3.7% stake buy Rs 17.25 Cr (review Flag 9 L944, Q14 L513)", counter: "Secondary from undisclosed sellers via a subsidiary; implied value about Rs 466 Cr, 2.5-4.2x IndiaMART's own average entry; Agillos earnings NOT FOUND, so price/PAT not computable", source_line: "FS FT L1180-1181; DECK R147, R166, R167, R178; RES R667", type: MISSING}
findings_by_type:
  factual:
    - "A4: Busy deferred revenue +40% YoY is printed in deck p9 (DECK R058 FT L215); review L604 'call-only' and L821 'UNVERIFIABLE' are wrong; status CONFIRMED"
    - "A4: brief L994-998 states the standalone Rs 5 Cr QoQ build against the consolidated Rs 2,028.9 Cr book; consolidated build was Rs 15 Cr (DECK R526/R527)"
    - "A4: surviving bear counter on ARPU; [FILED] tags on price-led growth and 'top accounts pay 12% more' lack filed support (review L412, L506, L1000-1001)"
  missing:
    - "A2: deck ledger ZERO_STANDING count 0 vs 8 A1 tags (R480-R481, R617-R622); ledger-only fix"
    - "A3: FS SA note 7(i) Livekeeping OCD 59.97 mn, 7(ii) Tradezeal OCD 190.00 mn, 7(v) OCCRPS conversion unreviewed (FS FT L3267-3275); Livekeeping funding absent from #11 (review L404); RES R667 1,020 mn reconciles without Agillos, so a subsidiary paid Agillos (review Q14 L513)"
    - "A4: acquisition-economics probe not run; Fleetx implied about Rs 1,344 Cr on about Rs 72-84 Cr annualised loss, flat to prior tranche; Agillos implied about Rs 466 Cr, 2.5-4.2x own entry, earnings NOT FOUND"
  contradiction:
    - "A4: Step B3E tally (review L693) contradicts A4's own prior-question table (review L420-444): 10 partial and 14 not addressed, not 12 and 12; three answers by filing, not two"
  style:
    - "S1 review L225: print consolidated sequential margin +179 bps, not +175"
    - "S2 review L943 / YAML L1130: state basis for associates +20% QoQ (reported +4.8%; +20.2% ex-MonotaRO stub)"
    - "S3 review L321, L507: four QoQ deferred-revenue builds are visible, not five"
    - "S4 concall anchors 'CC L173' and 'CC L152-159' are fulltext numbers under the L label"
    - "S5 review L425, L788: 'We don't know' answers a silver-churn timing question; state the net-adds mapping"
    - "S6 review L481: market cap 9,469 vs CMP x filed shares 9,460.5 Cr"
    - "S7 review L384: '50-55 Cr band' not in the item's thresholds"
    - "S8 review L195, L898: add H1 core PBT growth ex-SBP and ex-D&A (about +16.0%) beside +26.4%"
loop_back_to: "A2"
gap: "A2: deck ledger ZERO_STANDING section and count (8 rows, R480-R481, R617-R622). A3: FS SA note 7(i)/(ii)/(v) forensics, RES R667 reconciliation, Livekeeping link to #11. A4: fix Busy deferred-revenue reconciliation (DECK R058), brief deferred-revenue basis (consol +15 Cr), Step B3E tally (10 partial / 14 not addressed / 3 by filing); graft ARPU survivorship counter and Fleetx/Agillos purchase economics."
style_notes:
  - "S1 +179 bps sequential margin (review L225)"
  - "S2 associates growth basis (review L943, YAML L1130)"
  - "S3 four visible deferred builds (review L321, L507)"
  - "S4 FT numbers under L label (review L344, L778, L829, L832)"
  - "S5 churn-timing quote mapped to net adds (review L425, L788)"
  - "S6 market cap basis (review L481)"
  - "S7 unanchored 50-55 Cr band (review L384)"
  - "S8 ex-SBP, ex-D&A core growth (review L195, L898)"
analyst_note: "Arithmetic is clean: every P&L, margin, YoY, bridge, cash and S-vs-C figure recomputes from RES rows, and the PAT bridge foots to 81 mn. The failures are reading and completeness. The loop starts at A2 only because the deck ledger miscounts eight ZERO_STANDING rows; that fix is ledger-only and changes no downstream input. The real work is A3 then A4. A3 missed FS standalone note 7(i)/(ii)/(v): Rs 6.0 Cr of new OCD money into Livekeeping, which is under #11 scrutiny, and Rs 19.0 Cr into Tradezeal. The SA investing outflow of Rs 102.0 Cr reconciles exactly to Fleetx, Tradezeal, IndiaMart Finance and Livekeeping, so a subsidiary paid the Agillos sellers. A4 must graft the purchase economics: Fleetx is a flat-price, mostly insider round at about Rs 1,344 Cr implied value on an annualised loss near Rs 72-84 Cr; Agillos is a secondary at about Rs 466 Cr implied, 2.5-4.2x IndiaMART's own entry, earnings NOT FOUND. The #6 fired-as-written flag and Decision Status handling are sound. FS note 24 is outside A1's declared targeted scope, and its advertising line cannot be resolved in the scrambled fulltext."
```

---

## LOOP 1 RE-AUDIT (correction loop 1, the one permitted iteration)

Inputs this loop: the A4 review rewritten in full (change log at REV L3-11; line numbers below are the loop-1 file), the updated deck ledger (count test L8, ZERO_STANDING section L243-245), and the unchanged A1 fulltexts and structured files. The A3 forensics file was not read. Each fix was re-derived from A1 rows, not taken from the change log.

### Re-test of the seven loop-0 non-STYLE findings

| # | Type | Agent | Loop-1 evidence | A5 re-derivation | Status |
| --- | --- | --- | --- | --- | --- |
| M1 | MISSING | A2 | Deck ledger L8: zero_standing 8, match yes. L243-245 list R480-R481 (p38, FT L844) and R617-R622 (p39, FT L895). IDs 1,620 of 1,620, orphan none (L14) | A1 grep still gives 8 tags (DECK structured L491-492, L628-633) | RESOLVED |
| M2 | MISSING | A3 | REV L81 new 0D row for SA note 7(i), (ii), (v); L328 5-S composition; L416 #11 row; L525 Q14 payer; L550-552 Q39-Q41; L963 Flag 9 | 65.0 + 19.0 + 12.05 + 6.0 = 102.05 Cr vs RES R667 102.0. Livekeeping 59.97 mn is H1 only, nil in Q2 (FS R2111/R2113), so "Q1" holds. Earlier tranche 1,759 x INR 51,167 = 90.00 mn (FS R1114/R1115), so "same price" holds. Tradezeal equity 128.06 mn (FS R1050). Livekeeping goodwill 420.38 mn unchanged (FS FT L1016-1020). Allowance 52.61 mn at both dates (FS R1132/R1134). Agillos absent from the SA related-party list (FS FT L4043-4046) | RESOLVED |
| F1 | FACTUAL | A4 | REV L623 claim 10 "YoY confirmed in deck"; L840 CONFIRMED | DECK R057/R058, FT L213-215 | RESOLVED |
| F2 | FACTUAL | A4 | REV L1017-1018: consolidated book about Rs 15 Cr (about 1%), standalone Rs 5 Cr, each tagged | DECK R526/R527 (2,014 to 2,029); R965/R966 (1,858 to 1,863) | RESOLVED |
| F3 | FACTUAL | A4 | REV L424 6D trigger 1 survivorship [INFERENCE]; L518 Q7 asks price / mix / survivorship and same-account growth; brief L1020-1023 retagged | DECK R246, R247, R257, R258, R991 | RESOLVED |
| C1 | CONTRADICTION | A4 | REV L712: 4 answered (3 by filing), 10 partial, 3 evaded, 14 not addressed, with question numbers | Recount of the unchanged table REV L432-456 gives the same split | RESOLVED |
| M3 | MISSING | A4 | REV L554-556 economics note; L963 Flag 9 | Figures match the loop-0 derivation: Rs 1,344 Cr; Rs 72-84 Cr; -16x to -19x; flat round; Rs 466 Cr; 2.5-4.2x | RESOLVED |

### Correction to A5's own loop-0 audit

My loop-0 probe said Agillos earnings were NOT FOUND. That was wrong. A1's render-mapped rows FS R304/R305 (p17, render-verified per the FS structured header L18) put the Agillos "Less: Share of loss of associate" at (84.35) mn at Sep-26 and (64.23) mn at Mar-26. That is an H1 share of loss of 20.12 mn, which REV L556 now cites. At the 23.2% pre-transfer stake, Agillos lost about Rs 8.7 Cr in H1, about Rs 17 Cr annualised [derived]. The Rs 466 Cr implied value is about -27x that loss, so price / PAT is not meaningful, not "not computable". This strengthens the bear reading. No number in the review is wrong. The review's "earnings NOT FOUND" label (L963) and "not computable" (L556) followed my loop-0 wording: STYLE S9.

### Drift check (whole-file rewrite)

| Section | Loop-1 lines | Comparison with loop-0 reading | Result |
| --- | --- | --- | --- |
| Verdict card (Section C narrative, position, protocol verdict) | REV L915-927 | Identical text: PROCEED WITH FLAGS; #6 BROKEN AS WRITTEN; 8A; HELD unchanged | No drift |
| Step 1 tables (1-C, 1-S, 1-D, 1-G) | REV L96-188 | Every cell identical | No drift |
| Thesis-broken table (6C) | REV L401-416 | Rows #6, #4, 8B, #2, #5, #3, #1, #9, #7, #8, #10 identical. Row #11 rewritten (a patched point) | Patched only. Row #11 now adds "AMBIGUOUS on wording ... leg 2 is met" if "any amount" covers the carried 5.3 Cr allowance, while change log L11 says every thesis-broken result is unchanged. Headline stays NOT FIRED and the action tier is scrutiny, not EXIT, so the verdict is unaffected: STYLE S10 |
| Questions for Management (8.5) | REV L510-552 | Q1-Q6, Q8-Q13, Q15-Q38 identical. Q7 and Q14 rewritten, Q39-Q41 added (all patched) | No drift outside patched points |
| Consequential edits | REV L563, L951 | Question count 38 to 41 | Follows the patch |

Drift-check line: **no change outside the patched points in the verdict card, Step 1 tables, thesis-broken table or question table. One change-log understatement on row #11 (STYLE S10).**

### New items this loop

No new FACTUAL, MISSING or CONTRADICTION item. New STYLE:
- S9. REV L556 and L963: Agillos "earnings NOT FOUND" and "price / PAT not computable". The H1 share of loss (20.12 mn, FS R304/R305) is filed and is cited at L556. Say "loss-making; price / PAT not meaningful; implied value about -27x the annualised loss [derived]". This corrects A5's own loop-0 wording.
- S10. REV L11 vs L416: the change log says every thesis-broken result is unchanged, but row #11 gained an AMBIGUOUS wording qualifier. Name it in the change log.

Loop-0 STYLE notes carried, not applied (none loop): S3 (REV L333, L519), S4 (L356), S6 (L493), S7 (L396), S2 (L962) still read as in loop 0. S1, S5 and S8 were not re-checked.

### Loop-1 verdict

**VERDICT: COMPLETE.** All seven loop-0 FACTUAL, MISSING and CONTRADICTION findings are resolved and re-derive from A1 rows. The drift check is clean. The remaining findings are STYLE only and do not loop. The review may proceed to the operator-approval gate for Notion save.

```yaml
stage: A5-adversary
company: "INDIAMART"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
loop: 1
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
    - "S9 review L556, L963: Agillos is loss-making (H1 share of loss 20.12 mn, FS R304/R305); say price/PAT not meaningful, about -27x annualised loss, not 'earnings NOT FOUND' / 'not computable' (corrects A5 loop-0 wording)"
    - "S10 review L11 vs L416: change log says all thesis-broken results unchanged; row #11 gained an AMBIGUOUS wording qualifier (headline NOT FIRED, scrutiny tier)"
    - "Carried from loop 0, not applied: S2 (L962), S3 (L333, L519), S4 (L356), S6 (L493), S7 (L396); S1, S5, S8 not re-checked"
loop_back_to: ""
gap: ""
style_notes:
  - "S9 Agillos loss basis label (review L556, L963)"
  - "S10 change log understates #11 change (review L11, L416)"
  - "Loop-0 S1-S8 carried, no re-run"
analyst_note: "All seven loop-0 items are resolved, and each fix re-derives from A1 rows. The deck ledger now counts 8 ZERO_STANDING rows. The standalone outflow of 1,020 mn reconciles to Fleetx, Tradezeal, IndiaMart Finance and Livekeeping, with Livekeeping's 59.97 mn in Q1 (FS R2111/R2113). Busy +40% is CONFIRMED from DECK R058. The brief separates the Rs 15 Cr consolidated build from the Rs 5 Cr standalone build. The B3E tally matches the table. The ARPU survivorship reading and the Fleetx and Agillos purchase economics are grafted. The drift check is clean: verdict card, Step 1 tables, thesis-broken table and question table match loop 0 outside the patched points. The only gap is that change log L11 understates the row #11 qualifier. One correction to my own loop-0 audit: Agillos earnings are not absent. FS R304/R305 give an H1 share of loss of 20.12 mn, so Agillos loses about Rs 17 Cr a year at 100% [derived], and its Rs 466 Cr implied value is about -27x that loss. The review already cites 20.12 mn; only its labels are loose (S9). Remaining items are STYLE and do not loop."
```
