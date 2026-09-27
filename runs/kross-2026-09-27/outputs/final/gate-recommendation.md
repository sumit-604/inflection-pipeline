PROCEED WITH CAVEATS

# KROSS: FTTCP gate recommendation (Phase 1, run 2026-09-27)

Scope: Phase 1 lite. This is the go or no go on sending Kross to FTTCP deliberation after Halt 1. It carries no valuation decision, no entry range, no margin of safety price, no destination multiple and no Hurdle verdict. Stage 11 has not run. The Mental Model is not signed. Freshness verdict: FRESHNESS PAIRS OK, so no freshness cap applies.

## How the verdict was reached

1. REWORK does not fire. Verifier A logged no CRITICAL. Every verifier acceptance rate sits at or above 73%. Overall confidence is 73.0, above the 60 floor. Verifier A's two source fidelity MAJORs were both cleared by an orchestrator reread of the AR FY26 balance sheet (AR PDF p.60, printed p.114) and logged in verifier-disagreement-log.md. Both were basis differences, not misreads.
2. INSUFFICIENT EVIDENCE does not fire on this reading. The annual reports, notes, four transcripts, three results, the rating rationale, the prospectus and two shareholding filings are all held. Gate 0 ran on screening data and results. The cash gap is partial and closable at Halt 1 (see FLAG-CASH). The other reading, and the observation that separates them, is set out in FLAG-CASH below.
3. FLAG-CASH is active. Its determination is INDETERMINATE, which caps the verdict at PROCEED WITH CAVEATS instead of PROCEED WITH FLAGS. FLAG-PROMOTER is not active: the promoter verdict is CAUTION, below the CONCERN trigger.
4. Confidence sits in the 60 to 74 band (73.0, set by redflag_coverage). That band moves a PROCEED verdict down one level, to PROCEED WITH CAVEATS. The cash cap already puts the verdict there. The two mechanisms land on the same level, and the band cannot push further: the levels below carry their own triggers (REWORK needs confidence under 60; INSUFFICIENT EVIDENCE needs a named gap that breaks the decision record).
5. Verifiers also logged MAJORs worth carrying (listed under Open items). That alone would give PROCEED WITH CAVEATS.

Final: PROCEED WITH CAVEATS. Rule applied: 3, with the INDETERMINATE cap; rule 4 concurs.

## Transition posture

NOT CLASSIFIED at Phase 1. The Mental Model is unsigned and the recognition gap is a Stage 11 read. The two variables the evidence can speak to now:
- Proof gate: NOT FIRED on current evidence. The margin claim (13% to 14 to 15% from in house tube and beams) is not in the numbers. Q1 FY27 EBITDA margin was 12.23% (Concall_Jul_2026; Q1 FY27 results). The extrusion line only went into production in July 2026 (Concall_Jul_2026 p.3, p.8). The seamless tube plant is due around Q4 FY27.
- Ugliness: undetermined, and it mirrors the cash determination. If the cash drain is capex and customer mix, it is an artifact of the climb. If it is slower payment that will not reverse, it is a structural feature.
With the proof gate not fired, the reachable cells are RESEARCH / WATCH (artifact, gap open), PRICED NARRATIVE (artifact, gap closed) and VALUE-TRAP RISK (structural). Halt 1 and Stage 11 pick among them.

## Confidence delta (phase 1)

| Component | Value | Basis |
|---|---|---|
| numerical_acceptance | 100.0 | B12a, 48 figures; raw 95.8 before two source reread clearances (verifier-disagreement-log.md) |
| redflag_coverage | 73.0 | B12b, 11 of 15 material caught including partial; 4 MAJOR missed |
| framework_adherence | 76.7 | B12c phase 1 half, 46 of 60 rules (Gate 0 42, Emerging Moat 18); valuation half pending phase 3 |
| peer_utilisation | 92.0 | B12d, 11 of 12 peer quarter cells handled correctly; all 3 peers used substantively |
| overall | 73.0 | min of four; set by redflag_coverage; band 60 to 74 |

Weakest component: red flag coverage at 73.0. The pipeline missed four MAJOR items in the company's own calls and one peer transcript, and all four cut against the thesis (plateau admission, fabricator receivables, cost creep, peer margin contradiction).

## Flag blocks

```
⚠️ CASH CONVERSION FLAG: CFO/PAT 0.18x (FY25) and 0.50x (FY26), both under 0.7x; FCF minus Rs 72.43 Cr FY26; WC days up from 89.01 (FY22) to 131.73 (FY26); receivables aged over six months up from 8.9% to 11.0% of gross. Direction: deteriorating.
Determination: INDETERMINATE.
Evidence:
- Capex: FY26 capex Rs 100.18 Cr against CFO Rs 27.75 Cr; capex 11.03x depreciation (AR FY26 cash flow, PDF p.61, printed p.116-117; B01 Block B; B03 FLAG-CASH). Axle beam extrusion Rs 25 Cr commissioned, in production Jul-2026; seamless tube Rs 167 Cr due around Q4 FY27, revenue from FY28 (AR PDF p.13, printed p.20-21; PDF p.30, printed p.58; Concall_Jul_2026 p.3, p.8; B05 guidance). This part of the FCF gap is capex timing.
- Receivables composition: over six months bucket 8.9% to 11.0% of gross; 6 month to 1 year bucket up 45.5% (Rs 137.63 Mn to Rs 200.28 Mn) against 8.5% revenue growth; ECL allowance flat at Rs 14.35 Mn for two years; receivables turnover 7.67x (FY24), 4.25x (FY25), 3.55x (FY26) (AR Note 11, PDF p.69, printed p.132-133; Note 52, PDF p.82-83, printed p.159-160; B02 rank 4). Customers above 5% of the book hold 54.19% of FY26 receivables (Note 39(a), PDF p.79, printed p.153; B03).
- Off balance sheet credit: bills discounted with recourse Rs 349.00 Mn, up 7.6%, 88% of contingent liabilities (Note 34, PDF p.76-77, printed p.146-147; B02 rank 2).
- Bank cross check: debtors reported to banks differ from books by Rs 150 to 406 Mn in 5 of 8 quarters, explained only as post period adjustments (Note 53, PDF p.83-84, printed p.161-162; B02 rank 5).
- Supplier side: payable turnover 12.85x (FY24) to 8.58x (FY26), days stretching from about 28 to about 43 (Notes 20, 40, 52; B02 rank 9).
- Company's own remark on net capital turnover (12.02x to 3.78x to 2.59x): "Increase in revenue along with increase in working capital following lower current liabilities." (Note 52, PDF p.82-83, printed p.159-160; B02 rank 11).
- Management on the call: fabricator receivables above 90 days and constrained OCF in H1 FY26 (Concall_Nov_2025 p.10-11, Lakshminarayanan and Kunal Rai; B12b missed item 2). No stage absorbed this.
- Rating agency quote: NOT CAPTURED. The India Ratings rationale of 01-Jun-2026 (IND A/Stable/IND A1) is held at inputs/rating/2026-06-02_credit_rating_reg30.pdf, pp 2-9 (B00), but no stage extracted its working capital paragraph. No verbatim quote is carried here, and none is paraphrased.
Two readings:
- GROWTH-INDUCED: the FCF gap is capex funded by the IPO, and the receivable build tracks a larger trailer fabricator book plus the IPO paydown of current liabilities (the company's own remark).
- STRUCTURAL: receivable days jumped in FY25 and stayed near 107 in FY26 while revenue grew only 8.5%; the aged buckets grow faster than sales, the allowance does not move, and part of collection is bank discounting with recourse.
Separating observation: H1 FY27 (half year to 30-Sep-2026) receivables growth against revenue growth, read with the aged bucket split by fabricator versus OEM customer.
Missing evidence (named, with source):
1. India Ratings 01-Jun-2026 rationale, working capital and liquidity paragraphs, verbatim with page (held: inputs/rating/2026-06-02_credit_rating_reg30.pdf pp 2-9). Standing extraction item for Halt 1.
2. Receivables ageing split by customer class (fabricator vs OEM vs export). Not disclosed in AR Note 11; a management question.
3. H1 FY27 statement of assets and liabilities and half year cash flow, filed with the Q2 FY27 results (BSE, due by mid Nov-2026).
Consequence: verdict caps at PROCEED WITH CAVEATS. INDETERMINATE does not resolve to PROCEED.
If items 1 and 2 cannot be obtained before FTTCP, the strict reading of the selection rules (INDETERMINATE cash with the missing evidence identified) moves this gate to INSUFFICIENT EVIDENCE.
```

```
⚠️ GATE 0 FLAG: GOOD, 81/160 (core 68/100, moat 13/60; blocks A 13, B 1, C 20, D 18, E 16; moats confirmed 3, MODERATE). Deal breaker #2 fired (Block B under 8 caps classification at GOOD). (B01)
Depressors:
- Block B 1/20: cumulative CFO/PAT 0.614x over 7 years; FCF positive in 3 of 7 years; cumulative FCF minus Rs 83.14 Cr; WC days up 42.72 (B01 Block B). CURRENT, not historical: FY24 to FY26 are the worst years.
- A4 scores 5 but masks a ROCE fall: computed 42.17% (FY24) to 15.55% (FY26); the AR's own Note 52 gives 28.15% to 16.74% to 15.03% (B01 FLAG-ROCE-BASE-EFFECT; B03). HISTORICAL in cause (rebase after the IPO: net worth Rs 146.81 Cr to Rs 489.77 Cr) but real in effect: EBIT grew about 9% over the same two years. The FY24 level gap (42.17% vs 28.15%) is a capital employed basis difference to reconcile before Section 1B Pillar 1.
- M11: revenue CAGR 45.12% (FY20 to FY23) slowed to 11.28% (FY23 to FY26) (B01 FLAG-GROWTH-DECELERATION). CURRENT.
- M2 and M9: FY26 EBITDA margin 13.08% vs 3 peer median 14.79%; gross margin proxy 45.86% vs 51.51% (B01 FLAG-MARGIN-BELOW-PEER). CURRENT.
Verifier C readings (not absorbed by stage 1):
- G-2 MAJOR: E2 used the post offer baseline (+0.87pp, score 3). The 3 year window from 99.99% before the offer to 68.57% gives score 0; Block E 13, core 65 (Prospectus lines 2020 to 2025; B12c). The drop is an IPO listing artefact (historical).
- G-1 MAJOR: M11 band ladder not evaluated; full period reading scores 3 (moats 4, class STRONG), latest window reading scores 0 (B12c).
- Recomputed: core 65, moat 14 or 17, grand 79 or 82, class MODERATE or STRONG. Classification GOOD holds under every reading, because deal breaker #2 caps it.
Gate 0 does not cap the verdict. It is surfaced for Role 2 position sizing.
```

```
PROMOTER FLAG: not active. B08 verdict CAUTION (scorecard clean 6, caution 3, red 1; deal breakers none). The flag block fires only on CONCERN or AVOID.
Carried as caveat (one connected governance story across the notes, AR and promoter stages):
- Bull Auto Parts, the proprietorship of CFO Kunal Rai: sales Rs 83.65 Mn FY22, Rs 80.93 Mn FY23, Rs 155.98 Mn FY24, Rs 93.54 Mn FY26 (1.39% of revenue), receivable Rs 49.38 Mn at FY26 end; no arm's length pricing comparison disclosed. FY25 amount NOT FOUND in this run (Prospectus PDF p.51; AR Note 51, PDF p.82, printed p.158; B08; B02 rank 3).
- 31-Aug-2026 preferential: 15 lakh shares at Rs 212 (Rs 31.8 Cr) to four individuals outside the promoter group, three sharing one surname group (relationship UNVERIFIED); 15 lakh warrants at Rs 212 (Rs 31.8 Cr) to promoters Sumeet Rai and Kunal Rai, 25% upfront, 18 months to exercise or lapse. Stated use: tractor shaft capacity Rs 15 Cr, cold drawn tube Rs 15 Cr, robotic automation Rs 13 Cr, office Rs 5 Cr, working capital Rs 10.6 Cr, general corporate up to Rs 5 Cr. NSE forced a corrigendum on 23-Sep-2026. Postal ballot result due by 03-Oct-2026: NOT FOUND (after run date) (Board outcome and Annexures A/B, 31-Aug-2026; postal ballot notice 31-Aug-2026; corrigendum 23-Sep-2026; B08).
- Head (Accounts and Finance) Dhirendra Jena and independent director Mukesh Kumar Agarwal both resigned on 24-Jul-2026, the Board's Report signing date; reason not disclosed (BSE filings 2026-07-24; B03 FLAG-GOVERNANCE; B08).
- Disclosure competence: AR Note 52 prints ROE 171.18% / 161.98% / 221.26% on paid up capital; true FY26 ROE about 11.95%; MD&A prints a third figure, 11.27%. Eight internal document defects in all, including a CARO cross reference to the wrong note (Note 52, PDF p.82-83; MD&A PDF p.24, printed p.43; CARO PDF p.58, printed p.110; B02 rank 1; B03 FLAG-DISCLOSURE-QUALITY).
Transition evidence: promoter holding rose every quarter from 67.70% (Sep-2024) to 68.57% (Jun-2026), no pledge; Anita Rai bought 89,027 and 30,000 shares in the open market on 27 and 31 March 2026; promoters give personal guarantees on company borrowings; new independent director Sharat Chandra Kumar appointed 24-Jul-2026 (NSE shareholding master JSON; SAST 29(2) filings 27 and 31-Mar-2026; Prospectus PDF p.63; directorate filing 24-Jul-2026; B08).
```

## Load bearing facts from intake: what the filings said

| LBF | Intake claim | Status | Filed evidence |
|---|---|---|---|
| LBF1 guidance vs delivery | FY27 ~22% growth at 14 to 15% margin vs Q1 FY27 12.2% and ~13% history | CONFIRMED, one side modified | Guidance stated in the Q4 FY26 call (Concall_May_2026). Q1 FY27 margin 12.23% missed it (Concall_Jul_2026). Revenue side beat: +32% in Q1. FY26 margin 13.08 to 13.10% (screener; AR). |
| LBF2 cash conversion | CFO/PAT ~19% and ~51%; WC days 30 to 124; FCF negative three years | CONFIRMED, figures modified | CFO/PAT 0.180x FY25, 0.503x FY26 (AR cash flow PDF p.61). FCF minus Rs 13.45 Cr, 19.72 Cr, 72.43 Cr over FY24 to FY26, not minus 19, 20, 72. WC days on the filed basis 85.11 (FY24), 125.36, 131.73, not 30 to 124. Determination INDETERMINATE (see flag). |
| LBF3 IPO proceeds and capex | Rs 250 Cr fresh issue use; tube capex Rs 167 Cr vs ~Rs 100 Cr; borrowings Rs 34 to 54 Cr | CONFIRMED on use, MODIFIED on capex and debt | Net proceeds Rs 236.92 Cr fully used as stated: capex Rs 70 Cr, debt Rs 90 Cr, WC Rs 30 Cr, GCP Rs 46.92 Cr; zero deviation (Note 54, PDF p.84; monitoring agency). Filings give Rs 167 Cr for the tube plant (AR PDF p.30, printed p.58); the ~Rs 100 Cr figure appears in no filing read. Funding of the tube balance NOT FOUND. Borrowings Rs 32.66 Cr to Rs 52.37 Cr on the AR basis; the screener Rs 53.73 Cr adds lease liabilities (AR PDF p.60, printed p.114). |
| LBF4 concentration and equity raise | Top five 59.5%; preferential at Rs 212 | CONFIRMED and extended | Top five 59.47% of Q1 FY27 revenue (Q1 FY27 deck slide 20). Related party sale to the CFO's firm found (Note 51). Allottees, promoter warrants and itemised use found (see promoter caveat). Outcome pending 03-Oct-2026. |

## Contradicted claims (priority monitoring)

From the peer stage:
1. Kross's M&HCV recovery and "high single digit" FY27 OEM volume view. Automotive Axles: "the revised forecast... is it could be less than 5%-10% dip compared to last year... Best case, same as last year." (AUTOAXLES-Concall_Aug_2026 p.9-10).
2. Trailers as the growth segment behind Kross's 34% Q1 FY27 trailer growth. Ramkrishna Forgings' MD: "I don't think that is growing significantly... growth is coming from the tipper vehicle" (RKFORGE-Concall_Feb_2026 p.18-19).

Found by the verifiers, not absorbed by any stage:
3. The margin excuse. Automotive Axles lifted Q1 FY27 EBITDA margin from 12.4% to 13.6% under the same LPG and steel costs, with commodities back to back; Happy Forgings puts the domestic steel lag at one month. Kross fell from 14.9% to 12.23%. The peer stage graded the excuse VERIFIED on mechanism alone (AUTOAXLES-Concall_Aug_2026 p.4, p.13; HAPPYFORGE-Concall_May_2026 p.8; Concall_Jul_2026 p.4).
4. The share claim. Ramkrishna's Rs 120 Cr at 4 to 5% share implies a Rs 2,400 to 3,000 Cr market, which puts Kross's trailer revenue of about Rs 289 Cr at 10 to 12%, not 26 to 28% (RKFORGE-Concall_May_2026 p.9; Concall_May_2026 p.5). The market sizing stage adopted the lower market band and named the divergence; it did not resolve it.
5. The capacity constraint claim. Axle output about 3,500 a month against 5,000 capacity, forging at 60 to 70%, and a Q4 order book of 4,000 axles a month not met (Concall_Jul_2026 p.6, p.9; Concall_May_2026 p.7-8; Concall_Feb_2026 p.8-9). Automotive Axles runs at 90%, "at the peak of our capacity" (AUTOAXLES-Concall_May_2026 p.6-7).
6. The company against itself. The chairman said trailer axle growth "has plateaued out and we will now have to grow with what the segment grows by", against the later 26 to 28% to 35% share target (Concall_Nov_2025 p.13; Concall_Feb_2026 p.6, p.10).

## Open items carried from the verifiers

Verifier A and the disagreement log:
- Both source fidelity MAJORs cleared by source reread. Borrowings Rs 53.73 Cr (screener) equals Rs 52.37 Cr borrowings plus Rs 1.36 Cr lease liabilities. Cash Rs 23.74 Cr (screener) equals Rs 4.44 Cr cash plus Rs 19.30 Cr other bank balances (AR PDF p.60, printed p.114).
- Phase 3 must settle net debt: the notes describe the Rs 19.30 Cr other bank balances as locked or collateral deposits. A net debt figure that treats them as free cash understates net debt by that amount. Gate 0 test D1 used the screener figures.

Verifier B, four MAJOR misses (no stage absorbed them):
1. The chairman's trailer axle plateau admission (Concall_Nov_2025 p.13).
2. Fabricator receivables above 90 days and constrained OCF in H1 FY26; the concall stage wrongly states cash conversion never came up on a call (Concall_Nov_2025 p.10-11).
3. Other expenses at 26.5 to 28% of sales against 24.5% earlier; semi fixed costs grew 35% a year against 30% revenue growth over FY22 to FY25; management promised a return to 22 to 23% (Concall_Feb_2026 p.7, p.12-13).
4. The peer margin contradiction in item 3 above (AUTOAXLES-Concall_Aug_2026 p.4, p.13).
Verifier B, three MAJORs where the stage caught the item but gave it too little weight:
5. Evasion on performance against the industry spans Q2 FY26, Q3 FY26 and Q1 FY27, graded MEDIUM; the Q2 FY26 unmet "I'll let you know" on the tractor split and the Q3 FY26 tractor lag are untracked (Concall_Nov_2025 p.7-9; Concall_Feb_2026 p.14; Concall_Jul_2026 p.6). Verifier B reads the pattern as CRITICAL grade.
6. Capacity claim against utilisation (contradicted claim 5).
7. Share arithmetic from Ramkrishna (contradicted claim 4).
Verifier B on credibility: concurs lower, C minus. The extrusion slip was about six months, not two to three; the FY27 tipping jack guide of Rs 45 to 50 Cr (about 4,000 kits) is unreachable on 226 kits in Q1 and was never restated.

Verifier C, Gate 0 and Emerging Moat fragility:
- G-2 (MAJOR) E2 baseline and G-1 (MAJOR) M11 ladder: see the Gate 0 flag. Classification GOOD holds.
- E-1 (MAJOR): A1 rare manufacturing capability scored as documented, while the stage's own rule for the same evidence gives claim tier. The emerging moat score falls from 15 to 13.6; to 12.6 with E-2; to 11.6, which grades NONE, if B2 qualification lock in is also zeroed. The whole forward moat reading rests on one engine and one tier call.
- E-4: only 2 of the 4 listed 12 month catalysts fall inside 12 months.

Verifier D:
- Automotive Axles' Q4 FY26 call carries a 90% utilisation, "peak of our capacity" statement directly on the capacity claim, left unused (AUTOAXLES-Concall_May_2026 p.6-7).

## Gaps to close before FTTCP

| Gap | Needed for | Where to get it |
|---|---|---|
| India Ratings working capital and liquidity paragraphs, verbatim | Cash determination | inputs/rating/2026-06-02_credit_rating_reg30.pdf pp 2-9 (held; extraction at Halt 1) |
| Receivables ageing by customer class | Cash determination | Management question; not in AR Note 11 |
| H1 FY27 balance sheet and cash flow | Cash determination, WC trend | Q2 FY27 results filing, BSE, due by mid Nov-2026 |
| Postal ballot result and allotment | Capital allocation, dilution | BSE announcements, due by 03-Oct-2026 |
| Identity of three of four allottees outside the promoter group | Promoter read | claude.ai live check; allottee annexures 31-Aug-2026 |
| Funding plan for the seamless tube balance | Capex and debt path | Management question; Q2 FY27 call |
| FY25 Bull Auto Parts amount | Related party trend | AR FY25 related party note (held: Annual_Report_2025.pdf) |
| Shareholding before Mar-2026 (DII 9.72% intake claim) | Institutional trend | NSE SHP filings Mar-2025 and earlier |
| Q2 FY26 results | Quarter series | BSE results filing, Oct or Nov 2025 |
| ROCE basis reconciliation (42.17% vs 28.15% FY24) | Section 1B Pillar 1 | Stage 11, from AR Note 52 and prospectus balance sheet |

## Monitorables

1. Q2 FY27 EBITDA margin in the results for the quarter to 30 September 2026 (BSE, due by mid November 2026). A print of 14% or more supports the one quarter steel lag excuse. A print under 13% breaks it. Read Automotive Axles' same quarter margin beside it. This tests the margin bridge and the first load bearing fact.
2. H1 FY27 receivables against revenue in the half year balance sheet filed with the Q2 results. If receivables grow faster than revenue, the cash drain reads structural. If they grow slower, it reads as growth. This settles the cash determination.
3. The aged receivables bucket (11.0% of gross in FY26), the ECL allowance (Rs 14.35 Mn) and bills discounted with recourse (Rs 349.00 Mn) in the FY27 annual report, Notes 11 and 34. A rising bucket with a flat allowance, or more discounting, points to hidden credit strain.
4. The preferential issue: postal ballot result by 3 October 2026, allotment, and whether Sumeet and Kunal Rai pay the other 75% on their warrants within 18 months (BSE announcements). Lapsed warrants would say the promoters did not want the stock at Rs 212. This tests promoter alignment and capital allocation.
5. The capex engine on schedule: robotic forging confirmed in September 2026, seamless tube around Q4 FY27, and axle output against capacity (about 3,500 a month against 5,000 today; extrusion line 7,500 a month) in the Q2 and Q3 FY27 calls and Reg 30 filings. Another slip tests the whole transition.
6. Trailer share: Ramkrishna Forgings' quarterly trailer axle revenue (Rs 120 Cr now, Rs 250 Cr target) and SIAM tractor trailer and tipper volumes against Kross's trailer segment growth (34% in Q1 FY27). If the segment grows with the market and not above it, the chairman's plateau statement stands and the share claim does not.
7. Cost creep and interest: other expenses as a share of sales (26.5 to 28% against the promised 22 to 23%) and finance cost on a full year of FY26 borrowings (Rs 8.07 Cr in FY26 on debt drawn through the year) in the quarterly results. Both sit inside the margin bridge.
8. Mix targets: exports (3.60% of FY26 revenue, 4.51% in Q1 FY27) toward 8%, and tractor parts (9.48%, 9.93% in Q1 FY27) toward 15%, in the quarterly investor deck; plus any Reg 30 order from Leax Falun AB or the European Tier 1 customer. A fourth cut to the export target ends the export leg.

## Falsification line

Q2 FY27 EBITDA margin below 13.0% in the results for the quarter ended 30 September 2026. All three peers put the steel settlement lag at about one quarter, so a second straight miss cannot be lag.

## Publish check

No publish candidate this analysis.
