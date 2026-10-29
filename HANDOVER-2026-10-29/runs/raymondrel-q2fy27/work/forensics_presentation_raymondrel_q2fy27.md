# FORENSICS (presentation) RAYMONDREL q2fy27 — A3 Forensic Notes
Company: Raymond Realty Limited (RAYMONDREL) | Doctype: presentation (Q2 & H1 FY27 investor deck, dated 27-Oct-2026) | Model: claude-opus-5-5

Anchor convention: `l###` = A1 fulltext line (primary anchor). `s##` = the deck's own footer slide number, which is fulltext page − 1. "page N" = fulltext `[page N]` marker.

## 0. INPUTS AND RECONCILIATION
- Read: A1 structured (R001-R1082, all 1,082 rows), A1 fulltext (lines 1-761, all 46 pages), A2 ledger (1,082 IDs, 0 orphans), Notion monitoring copy (work/monitoring_checklist_raymondrel.md). Prior-quarter extract: none supplied. Source PDF and inputs/ were not opened.
- Ledger reconciliation: 1,082 of 1,082 ledger IDs read in the structured file and checked against the fulltext block at the cited line. Reconciled 100%.
- Render dependence. Pages 5, 11, 20, 22-24 and 26-44 have an interleaved text layer. A1 assigned values from renders that A3 cannot see. The fulltext header says `rendered_pages: [none]` (l12), but the structured header (structured l8) says pages 4-44 were render-checked. This is an A1 header inconsistency for the orchestrator. Internal arithmetic supports A1's mapping:
  - P&L: EBITDA − D&A − interest = PBT, and PBT − tax = PAT, in all four periods.
  - Balance sheet: assets = liabilities + equity at both dates.
  - Cash flow: 358 − 205 + 155 = 308.
  - Page 26 totals: project booking value + EWS 84 = 13,205 ≈ 13,200; collections + EWS 87 = 8,834; revenue = 10,078 exact.
  - Quarterly bookings summed by project: Q2 ≈ 900 vs 902; Q1 ≈ 697 vs 700; Q2FY26 ≈ 450 vs 455.
- A2 flags confirmed:
  - PAGE_ANCHOR_DEFECT on R840/R1068: line 567 sits under `[page 33]` (l556). The content is correct (Address S2, 580 units launched). Only the page label is wrong.
  - FOOTNOTE_UNRESOLVED R1067-R1075 is confirmed and used in A3-30.
  - R875 (page 13) is image-only and was not assessable.
- Derived numbers below are arithmetic on deck figures and are marked [DERIVED]. Interpretations are marked [INFERENCE]. A missing number is marked NOT FOUND.

## 1. FINDINGS TABLE
id | check | ledger row ref | line/slide | short verbatim quote | classification | forward implication
--- | --- | --- | --- | --- | --- | ---
A3-01 | F1 | R224 | l318 (s18) | "no new project launches during the quarter" | FORWARD-SIGNAL | Q2 had zero launches. H2 pre-sales now depend on Mahim-2 (Q3 FY27) and Mahim-1 (Q4 FY27). Any launch slip goes straight to H2 bookings.
A3-02 | F1 | R662-R664, R667-R668, R672 | l607 (s35) | "No of Bookings 5 2 0" | FORWARD-SIGNAL | Invictus Tower B (luxury, Thane) bookings fell from 5 to 2 to 0 over three quarters. Q2 booking value was 0. About 20% of 102 launched units are sold. Thane luxury velocity has stalled.
A3-03 | F1 | R774, R778, R782 | l700, l703 (s41) | "No of Bookings 0 (1) 14" / "0 -6 123" | AMBIGUOUS | BKC had a net cancellation in Q1 FY27 (−1 unit, −Rs 6 Cr). The Q2 rebound to Rs 123 Cr includes 11 retail units sold from 13 launched (l708). Residential demand at BKC is unproven.
A3-04 | F1 | R050, R052, R098, R355, R524-R540, R570-R578, R645, R690, R708-R720, R727-R743, R773-R785, R796-R812, R819-R835 | s5, s8, s23, s29-s43 | e.g. "0%    0%" (l115); "0" in Q2FY26 columns | NEUTRAL-FACT | The other 41 zero rows are mechanical. They are pre-JDA years, unlaunched-cohort receivables or S&M, pre-launch Q2FY26 columns (launches Q3 FY26-Q1 FY27 per R1011-R1025), sold-out projects, or rounding to 0.00 mn sq ft. One exception: the BKC Q2FY26 zeros sit beside Rs 175 Cr of revenue (A3-25).
A3-05 | F6 | R966, R967, R273-R282, R305-R310 | l172-173 (s9), l347-359 (s21) | "EBITDA MARGIN ~ 17-19%" / "PAT MARGIN ~ 9-10%" | FORWARD-SIGNAL | H1 EBITDA margin is 14.3% (185/1,293) and H1 PAT margin is 5.1% (66/1,293) [DERIVED]. With equal halves, H2 needs about 19.7% EBITDA and 12.9% PAT margin just to reach the low end [DERIVED]. Guidance is at risk. Lean bear.
A3-06 | F6 | R964, R146, R244-R245 | l170 (s9) | "PRE-SALES GROWTH ~20%" | AMBIGUOUS | Read literally, ~20% on FY26 Rs 3,023 Cr gives about Rs 3,628 Cr. After H1 Rs 1,602 Cr, that implies H2 of about Rs 2,026 Cr. H2 FY26 was Rs 2,263 Cr, so the guide implies H2 down about 10% [DERIVED]. Either the guide was not raised, or management expects an H2 slowdown.
A3-07 | F6 | R969, R1029 | l461 (s26) | "Mahim-1 (Residential) JDA 100.0% Q4 FY27 FY30" | FORWARD-SIGNAL | Checklist #4 red reads "Delay to Q4 FY27+". Mahim-1 now sits at Q4 FY27. Mahim-2 holds at Q3 FY27 (l460). Without a prior deck, A3 cannot confirm a slip. A4 should ask what the Q1 deck dated.
A3-08 | F6 | R972, R1035, R922 | l464 (s26) | "Thane Owned Land Parcel Owned 100.0% Q2 FY28 FY36" | FORWARD-SIGNAL | The Notion tracker expects a Thane (Jekegram) RERA launch in FY27 against the Rs 247 Cr warrant objects. The deck shows Q2 FY28. Thane land monetisation looks deferred by at least two quarters. The deck gives no acreage or use class (NOT FOUND).
A3-09 | F6 | R974, R977, R982, R984-R987 | l504, l553-554, l621; l687-690, l703-704, l720-721, l734 | "OC received for all towers" vs "Shore Pilling WIP" | CONFIRMATORY-NEGATIVE | I-1 reads red. Only Thane delivers OCs (Habitat, Address S1, Park Avenue 1A). Every MMR JDA is at shore piling, excavation or 4th-8th slab. The checklist's "earliest tell" has not turned.
A3-10 | F6 | R967, R965 | l171-173 (s9) | "PAT MARGIN ~ 9-10%" | AMBIGUOUS | Notion I-6 says management refuses to guide PAT ("current state"). This deck guides PAT margin and ROCE. Either I-6 is turning or the Notion state is stale. OCF is still not guided. The ROCE definition is NOT FOUND.
A3-11 | F7 | R962, R1042, R060 | l124 (s5) | "the Margins in % terms may appear lower" | FORWARD-SIGNAL | This is a pre-emptive hedge on margin percentages. JDA share of GDV rose from 9% (FY24) to 52% (H1 FY27) (l107-119). EBITDA/revenue fell over the same years: FY23 25.6%, FY24 23.2%, FY25 18.9%, FY26 16.5%, H1 FY27 14.3% [DERIVED from R159-R170, R266, R276]. Percentage-margin stops will keep testing.
A3-12 | F7 | R1080, R140-R171 | l744 (s44) | "regrouped/ reclassified, wherever necessary" | AMBIGUOUS | Demerger comparability. The FY20-FY26 track record (s11) and the Q2FY26/H1FY26 comparatives cover periods before the listed entity existed. Their basis (carve-out, audited or not) is NOT FOUND in the deck.
A3-13 | F7 | R963, R1044, R1045, R107 | l164-166 (s8) | "Selling & Marketing expenses would be additional approx. 5-6% of the Revenue" | AMBIGUOUS | The Rs 14,375 Cr "net surplus" leaves out S&M, corporate overhead (Rs 250 Cr in H1, R361-R364), interest and tax. Sales values and costs are "management estimates". The headline overstates distributable cash.
A3-14 | F8 | R291-R304 | l355-358 (s21) | "Taxes ... 13 15" (render-mapped) | AMBIGUOUS | ETR runs below the 25.17% statutory rate in every period: Q2FY27 19.7% (13/66), H1FY27 18.5% (15/81), Q1FY27 implied 13% (2/15), Q2FY26 14.3% (10/70), H1FY26 16.3% (15/92) [DERIVED]. The deferred-tax split is NOT FOUND. ETR may step up. The PAT guide may assume a low ETR.
A3-15 | F11 | R129, R133, R138, R336, R367 | l180, l182 (s10); l391, l405-406 (s23) | "1014 1220" / "Closing Balance ... 308" | FORWARD-SIGNAL | Net debt = 1,220 − 308 = Rs 912 Cr at Q2 [DERIVED]. The same method on FY26 gives 1,014 − 358 = Rs 656 Cr, which matches the checklist baseline. Net debt rose Rs 256 Cr in H1. It is below the Rs 1,000 Cr Q2 red line by Rs 88 Cr. The risk-matrix first signal (net debt > Rs 900 Cr, D/E > 0.75x; D/E 1,220/1,622 = 0.75) is lit. If the pending ruling treats the Rs 210 Cr AIF money as debt and it is not already in the 1,220, adjusted net debt is Rs 1,122 Cr [conditional DERIVED].
A3-16 | F11 | R129, R133, R366, R363, R313 | l401, l404 (s23); l366 (s21) | "Bank Loan" 155 vs "Finance, Legal & IT Cost" (26) | AMBIGUOUS | Debt rose Rs 206 Cr in H1, but the bank-loan inflow was Rs 155 Cr, a Rs 51 Cr gap. Cash finance cost (bundled with legal and IT) was Rs 26 Cr against P&L bank interest of Rs 55 Cr. Interest may be accruing into debt [INFERENCE]. If so, the management NOCF of (205) understates the cash burn. A4 should reconcile to the statutory CFS.
A3-17 | F11 | R325, R326, R134, R308 | l377 (s22), l182 (s10) | "Equity" 1,622 vs 1,567 | AMBIGUOUS | Equity rose Rs 55 Cr against H1 PAT of Rs 66 Cr, an Rs 11 Cr shortfall. The tracker's Rs 102 Cr warrant money is not visible in H1 equity. Its timing is NOT FOUND. Whether NCI is included in "Equity" is not stated. Internal tie-out holds (s10 = s22, both dates).
A3-18 | F12 | R341-R360, R321-R330 | l392-397 (s23); l372-379 (s22) | "Outflow (618) (410) (185) (1,212)" / "Approval (228) (150) (178)" | FORWARD-SIGNAL | (F12 applied by analogy to the project-cohort cash flow. A deck has no segment note.) The yet-to-launch cohort spent Rs 185 Cr against Rs 1 Cr of inflow, mostly approvals (178). Newly launched projects ran project OCF of (135). Only mature projects generate cash (+364). Current assets rose Rs 821 Cr in H1. That growth was funded mostly by current liabilities (+742) and debt. I-2 and I-4 read adverse.
A3-19 | F14 | R172, R1047, R878-R885 | l218 (s13) | "Board Independence : 100%" | AMBIGUOUS | The same slide lists 8 directors. Three are not independent: the Chairman (promoter, Gautam Hari Singhania), the MD, and Gautam Trivedi, "Non - Executive Director". So 5 of 8 are independent (62.5%). The slide redefines the claim as "All the Board Committees are chaired by Independent Director". This is a governance-claim drafting point under the Promoter CONCERN.
A3-20 | F14 | R015, R132, R136 | l68, l74 (s3); l178, l185 (s10) | "GDV 52,000" (FY26 axis) vs "42000 52000" (FY26, H1 FY27) | AMBIGUOUS | Page 4 labels Rs 52,000 Cr as FY26. Page 11 shows FY26 at Rs 42,000 Cr and H1 FY27 at Rs 52,000 Cr. If page 11 is right, about Rs 10,000 Cr of GDV was added in H1, almost all JDA (JDA share 41% to 52%). That bears on I-5 and checklist #5. The deck does not itemise new JDAs.
A3-21 | F14 | R037-R042, R474-R479 | l92 (s4, render 9,500); l443 (s25) | "13,200^ 10,078 8,834^" | AMBIGUOUS | Revenue recognised is Rs 9,500 Cr on page 5 and Rs 10,078 Cr on page 26. The JDA split is 1,930 vs 2,549. Note 10,078 − 577 (BKC) = 9,501 [DERIVED]. Page 5 appears to exclude BKC's revenue [INFERENCE]; see A3-24. Balance revenue is 3,700 on page 5 vs 3,122 implied by page 26.
A3-22 | F14 | R1053, R1055, R1056, R1065, R423, R431, R1067-R1075 | l346, l371, l385, l630-637, l423-424 | "H1FY27*" (no footnote text) | AMBIGUOUS | There are 12 footnote markers with no footnote text: 3 asterisks plus 9 "Units Launched" marks. The Park Street slide (s37) has no Customer Collections row. On page 26, Park Street and District 9 share one merged collections cell of 78, which page 30 gives wholly to District 9. The total ties to 8,834 only if Park Street collections are zero. Park Street has Rs 246 Cr booked and Rs 81 Cr revenue recognised.
A3-23 | F14 | R1037, R1078 | l29 (cover letter); l742 (s44) | "(Standalone and Consolidated)" / "has not been subjected to review by Auditors or the Board" | NEUTRAL-FACT | The deck's P&L and balance sheet do not say whether they are standalone or consolidated. All operating metrics are management-compiled and unreviewed. A4 must reconcile s21-s23 to the filed results before relying on them. The cover letter carries "(formerly known as Raymond Lifestyle Limited)" (l43). A4 should confirm the name history against the MCA record.
A3-24 | F16 | R448, R453, R454, R455, R784, R792, R788 | l427 (s25); l702 (s41) | "577" PTD revenue vs "521" PTD bookings | AMBIGUOUS | At Invictus BKC, revenue recognised (Rs 577 Cr) exceeds total booking value (Rs 521 Cr). Collections are Rs 64 Cr and work is at shore piling. Two slides agree. Revenue includes a non-unit-sale component [INFERENCE]; candidates are JDA landowner-share (barter) revenue or sale of rights. This is non-cash or non-customer revenue in EBITDA. Lean bear.
A3-25 | F16 | R789, R781, R785, R1019 | l707 (s41); l428 (s25) | "175  32  54" (Revenue, Q2FY26/Q1FY27/Q2FY27) | AMBIGUOUS | BKC recognised Rs 175 Cr in Q2FY26. That quarter had zero bookings and zero collections, and launch was dated Q3 FY26. Revenue came before launch. This was about 25% of Q2FY26 revenue (697). It flatters the Q2 YoY base and hides the sale-based growth rate. If the row is an A1 mapping error, the verifier should confirm.
A3-26 | F16 | R458-R465, R830, R834, R838, R987 | l429 (s25); l733-734 (s43) | "242" revenue vs "229" bookings; "Shore Pilling WIP" | AMBIGUOUS | Sion shows the same pattern: revenue Rs 242 Cr exceeds bookings Rs 229 Cr, with Rs 36 Cr collected and work at shore piling. Launch was Q4 FY26. It is the same question as A3-24.
A3-27 | F16 | R079, R446, R447, R454, R455, R464, R465, R472, R473 | l143 (s7); l426-430 (s25) | "JDA: 857" (amount collected) | FORWARD-SIGNAL | JDA revenue recognised to date is Rs 2,549 Cr (Bandra 1,345, BKC 577, Sion 242, Wadala 385). JDA collections are Rs 857 Cr (GST-inclusive). Revenue leads cash by about Rs 1,692 Cr [DERIVED]. In Q2, JDA revenue was 328 (44% of Rs 749 Cr) against JDA collections of 165. EBITDA quality is weakening as the JDA mix rises. I-2 reads adverse.
A3-28 | F11 | R311-R318, R903, R1054 | l364-367 (s21) | "Interest to Government authorities : BMC/TMC / MHADA" | FORWARD-SIGNAL | Interest owed to government authorities was 17 vs 10 in Q2 (+70%) and 36 vs 16 in H1 (+125%). This implies a growing deferred approval-premium liability outside "Debt" of Rs 1,220 Cr. The amount is NOT FOUND. Net debt understates leverage. Total interest rose 69% in Q2, which turned EBITDA +14% into PAT −12%.
A3-29 | F16 | R1062, R1063, R480, R481, R1061 | l415-430 (s25); l453-459 (s26); l447 | "Sr. No." 1-6 then 8; pipeline "1 2 3 5 6" | AMBIGUOUS | Two tables drop a numbered row. Launched Sr. 7 is probably the Thane EWS project: the totals include its Rs 84 Cr bookings and Rs 87 Cr collections and tie only with it [INFERENCE]. Pipeline Sr. 4 is unidentified. A project may have been removed from the launch pipeline (Thane commercial? another JDA?). A4 should ask.
A3-30 | F16 | R521, R590, R613, R659, R724, R747, R770, R793, R816, R839-R847, R1067-R1075, R468-R470 | l511-520 (s29); l430 (s25) | "LAUNCHED UNITS SOLD" / "1 747 Units Launched" | AMBIGUOUS | "% sold" is measured on launched units, and the footnote that defines "launched" is missing on 9 slides. Page 26 mixes bases. Wadala is "61%" sold but has booked 0.32 of 1.41 mn sq ft (23%). Address-III is 38% vs 9% by area; District 9 is 23% vs 16%. Sell-through looks higher than the project-level position.
A3-31 | F16 | R1043, R1058, R077-R082 | l149 (s7); l444 (s25) | "Amount Collected also includes GST Amount" | AMBIGUOUS | Collections include GST, and the deck nets them against bookings to give "outstanding" (Rs 4,366 Cr, R080). Whether booking value includes GST is not stated. Collection ratios and the +57% collection growth may be flattered by GST. The ex-GST receivable figure is NOT FOUND.
A3-32 | F16 | R441, R467, R482, R488, R491 | l426, l430 (s25); l460-463 (s26) | "Wadala ... 62%"; "Mahim-2 ... 82.4%" | AMBIGUOUS | Pre-sales and GDV are reported at 100% of JDA projects. Economic interest is 62% at Wadala, 91% at Bandra, 55% at Parel and 70.2% at Kandivali. Wadala alone booked Rs 264 Cr in Q2. The partner share sits only in the s8 cash table (Rs 6,278 Cr). Headline pre-sales overstate RRL's economic share, and the gap grows as Parel and Kandivali launch.
A3-33 | F16 | R305-R310, R291-R296 | l311-322 (s18) vs l358-359 (s21) | "Strong Pre-Sales Trajectory" (highlights) | CONFIRMATORY-NEGATIVE | The highlights slide leads with pre-sales (+98%), collections (+67%), income (+7%) and EBITDA (+14%). It leaves out PAT −12% (Q2) and −14% (H1), and PBT −6% and −12%. The PAT decline is confirmed, driven by interest (A3-28) and tax.
A3-34 | F16 | R1051, R902, R1076, R848, R849 | l318-319 (s18) vs l708 (s41) | "driven entirely by sustained sales velocity within the existing 'Address by GS' portfolio" | AMBIGUOUS | This attributes Total Income growth to sales velocity. Under the deck's own data, revenue follows construction progress or OC, not sales [INFERENCE]. Address-brand projects gave Rs 398 Cr of Rs 749 Cr Q2 revenue (53%) [DERIVED]. BKC launched 13 retail units in Q2 (l708). "Entirely" is not supported.
A3-35 | F16 | R259-R262, R263-R282 | l347-352 (s21) | "Other income 8 9 ... 18 21" | AMBIGUOUS | Deck EBITDA = Total Income − Expenses (757 − 642 = 115), so it includes other income. Ex-other-income margins are Q1 FY27 11.4% (60/526) and Q2 FY27 14.3% (107/749) [DERIVED]. On a deck basis, Q1 is 13.1% and Q2 is 15.2%. Under a 15% stop, the operating basis gives two consecutive quarters below 15% and the deck basis does not. Under 14%, neither basis fires. Under 18%, both fire. This is direct input to the pending margin-stop ruling.

## 2. CHECKLIST SCORECARD
check | status | basis
--- | --- | ---
F1 | FINDING | 47 ZERO_STANDING rows classified. 41 are mechanical (A3-04). Velocity signals: R224 zero launches, Invictus Tower B at zero, BKC cancellation (A3-01 to A3-03).
F2 | N.A. | The deck has no standalone vs consolidated split. The cover letter (l29) names both, but the deck basis is unlabelled (logged at A3-23).
F3 | N.A. | No standalone/consolidated cost lines in a deck.
F4 | N.A. | No auditor report or Other Matters paragraph. The deck says it was not reviewed by auditors (l742; logged at A3-23).
F5 | N.A. | No EoM or Going Concern language in a deck. No prior extract.
F6 | FINDING | Hits: "will further improve" (l123), "shall improve" (l124), FY27 guidance (l169-173), launch dates (l460-464), "estimated to generate" (l164), OC/WIP status lines. See A3-05 to A3-10 and the register.
F7 | FINDING | Hits: "may appear lower" (l124), "would be additional approx. 5-6%" (l165), "management estimates" (l166), "subject to risks and uncertainties" (l754), "not been subjected to review" (l742), "regrouped/ reclassified" (l744). None for "exploring", "in discussions", "evaluating", "endeavour" or "no assurance".
F8 | FINDING | The deck carries a tax line. ETR is below 25.17% in all five periods (A3-14). Deferred tax is NOT FOUND.
F9 | N.A. | No OCI line in the deck.
F10 | N.A. | The deck carries no share count, EPS or warrant data. Warrant status is NOT FOUND in the deck; A4 does the cross-check.
F11 | FINDING | Net worth ties internally (s10 = s22). Findings: derived net debt 912 (A3-15), the debt vs bank-loan and interest gap (A3-16), the equity roll-forward and warrant gap (A3-17), the government-authority interest liability (A3-28).
F12 | FINDING | Applied by analogy to the project-cohort cash flow and balance-sheet growth (A3-18). No statutory segment note.
F13 | PASS | The cover letter records only the board meeting window (03:40-05:00 PM, l36). No AR, AGM, record date, fund-raise or director term dates in the deck.
F14 | FINDING | Board-independence claim (A3-19), GDV period label (A3-20), page 5 vs page 26 revenue (A3-21), 12 unresolved markers and Park Street collections (A3-22), basis unlabelled (A3-23).
F15 | N.A. | No consolidation entity list in a deck. No prior list.
F16 | FINDING | No prior deck, so A3 cannot diff dropped metrics across quarters. Within this deck: revenue-recognition definition (A3-24 to A3-27), dropped serial rows (A3-29), "% launched units sold" basis (A3-30), GST in collections (A3-31), gross-of-partner pre-sales (A3-32), PAT omitted from highlights (A3-33), attribution claim (A3-34), EBITDA includes other income (A3-35). The aggregate pre-sales area is not disclosed; value only (NOT FOUND).
F17 | N.A. | Concall-specific silence audit. The deck read-across against the Notion checklist is in Section 4 for A4.

## 3. COMMITMENT REGISTER (F6)
commitment | implied date | ref | status word
--- | --- | --- | ---
Mahim-2 (JDA 82.4%) launch, expected booking value Rs 2,300 Cr, completion FY31 | Q3 FY27 | s26 l460, R968 | initiated (deck: "Estimated Launch Date")
Mahim-1 (JDA 100%) launch, Rs 1,800 Cr, completion FY30 | Q4 FY27 | s26 l461, R969 | initiated
Kandivali (JDA 70.2%) launch, Rs 3,000 Cr, completion FY34 | Q2 FY28 | s26 l462, R970 | initiated
Parel (JDA 55%) launch, Rs 8,500 Cr, completion FY36 | Q2 FY28 | s26 l463, R971 | initiated
Thane Owned Land Parcel launch, 4.65 mn sq ft, Rs 8,500 Cr, completion FY36 | Q2 FY28 | s26 l464, R972 | initiated
FY27 guidance: pre-sales growth ~20%, ROCE ~20%, EBITDA margin 17-19%, PAT margin 9-10% | FY27 (Mar-2027) | s9 l169-173, R964-R967 | initiated
Portfolio to generate over Rs 14,375 Cr net surplus project cash flow (before S&M, overhead, interest, tax) | through FY36 (last pipeline completion) | s8 l164, R963 | initiated
"Realizations will further improve" on Mahim and Parel launches | Q3 FY27 to Q2 FY28 | s5 l123, R961 | initiated
"Absolute EBIDTA per sq. ft shall improve" while % margins "may appear lower" | undated | s5 l124, R962 | initiated
TenX Habitat: OC for all towers; 3,000+ homes delivered (RERA Q4 FY27) | done | s28 l504-506, R974, R1000 | completed
Address S1: Towers A and B OC received (RERA Q4 FY28) | done | s31 l553-554, R977 | completed
Park Avenue: Phase 1A OC received; Phase 1B finishing and MEP WIP (RERA Q4 FY29) | 1B by Q4 FY29 | s36 l621-622, R982 | completed (1A) / underway (1B)
TenX Era: Towers A-C finishing WIP (RERA Q4 FY29) | by Q4 FY29 | s30 l537-539, R976, R1004 | underway
Address S2: Tower C 37th slab, D 28th, E 5th (RERA Q4 FY29 under "II") | by Q4 FY29 | s32 l567-569, R978, R1006 | underway
Invictus Tower A: 28th floor slab WIP (RERA Q4 FY29) | by Q4 FY29 | s34 l601, R980 | underway
Address S3 Tower F and Invictus Tower B: foundation WIP (RERA Q2 FY32) | by Q2 FY32 | s33 l579; s35 l613; R979, R981, R1010 | underway
TenX District 9: Towers A and C excavation; B PCC (RERA Q1 FY33) | by Q1 FY33 | s29 l519-521, R975, R1012 | underway
Park Street: excavation WIP (RERA Q1 FY33) | by Q1 FY33 | s37 l632, R983, R1014 | underway
Address Bandra (JDA): Towers A-G launched; A 8th slab, B and C 4th, D Part B1 slab 3 (RERA Q1 FY31) | by Q1 FY31 | s40 l686-690, R984, R1018 | underway
Invictus BKC (JDA): shore piling (RERA Q2 FY32) | by Q2 FY32 | s41 l703-704, R985, R1020 | underway
Address Wadala (JDA): A and B excavation; C and D sub-structure (RERA Q4 FY31) | by Q4 FY31 | s42 l720-721, R986, R1026 | underway
Address Sion (JDA): shore piling (RERA Q2 FY31) | by Q2 FY31 | s43 l734, R987, R1024 | underway
Raymond Retail: no construction status on the slide (RERA Q1 FY33) | by Q1 FY33 | s38 l640-651, R1016 | NOT FOUND

Status-change tracking (initiated, then underway, then completed) needs the prior deck. None was supplied, so this register is the baseline.

## 4. MONITORING READ-ACROSS (deck evidence against the Notion checklist; input for A4, not an F17 audit)
item | deck evidence | reading
--- | --- | ---
#1 EBITDA margin (green ≥18%, red <15% for 2Q) | Q2 115/757 = 15.2%; Q1 70/536 = 13.1% [DERIVED]; deck "15%" (l321) | Not red on deck basis. Red on ex-other-income basis (A3-35). Below the 18% green line.
Stop: 2 consecutive Q EBITDA <14% | Q1 13.1%, Q2 15.2% | Not fired (deck basis). Ex-OI Q2 is 14.3%, also not fired.
#2 Q1 booking value (green ≥ Rs 500 Cr) | Q1 = 1,602 − 902 = 700 [DERIVED] | Green.
Stop: Q1 FY27 pre-sales YoY decline | Q1 FY27 700 vs Q1 FY26 305 (760 − 455) [DERIVED] | Not fired (+130%).
#3 / I-3 net debt (red > Rs 1,000 Cr by Q2; Rs 1,500 Cr exit) | Rs 912 Cr [DERIVED] (A3-15) | Below red. Risk-matrix first signal lit. AIF ruling pending.
#4 Mahim 1 and 2 launch (red: delay to Q4 FY27+) | Mahim-2 Q3 FY27; Mahim-1 Q4 FY27 (l460-461) | Partial red (A3-07).
#5 New JDA signings (green ≥ Rs 5,000 Cr by Q3) | Not itemised. GDV 42,000 → 52,000 (s10) [INFERENCE ~Rs 10,000 Cr] | NOT FOUND as a stated figure (A3-20).
#6 Related-party loans to subsidiaries | Not in the deck. s13 claims E&Y RPT review (l233-235). | NOT FOUND.
#7 Promoter governance event | Deck silent. Singhania is Chairman (l218). | No deck signal.
#8 Cost of debt (green 9.5-9.75%) | "9.6 %" (l186); CARE A+; Stable (l189) | Green.
#9 Thane commercial optionality | No commercial mention. Thane parcel use class not stated, Q2 FY28. | Silence continues (count needs prior quarters).
#10 / I-7 CFO | Management NOCF H1 (205) (R365). Statutory CFS not in the deck. | Negative. Possible understatement (A3-16).
Risk #5 Thane pre-sales (< Rs 1,000 Cr sustained) | Thane = total − JDA (Bandra, BKC, Wadala, Sion): Q1 ~252, Q2 ~384, H1 ~636 [DERIVED from render-mapped project rows] | About Rs 1,270 Cr run-rate. Above the line.
I-1 delivery/OC pace | Only Thane OCs (A3-09) | Red.
I-2 collections vs WIP | JDA revenue leads cash by Rs 1,692 Cr; current assets +821 in H1 (A3-18, A3-27) | Red.
I-4 launch-to-delivery mix | Newly launched + yet-to-launch = 595 of 1,212 project outflow (49%) | Early-stage weighted.
I-5 signing pace | ~Rs 10,000 Cr GDV added in H1 if s10 is right (A3-20) | Leaning red. Needs confirmation.
I-6 PAT/OCF guidance | PAT margin and ROCE guided; OCF not (A3-10) | Possible partial turn. Needs the prior deck.
Tracker: H1 CFO vs model FY27 −Rs 600 Cr | Management NOCF H1 (205) | Ahead of model on this format. Statutory CFS governs.
Tracker: warrant money Rs 102 Cr | Not in the deck; equity +55 vs PAT 66 (A3-17) | NOT FOUND.

## 5. PIPELINE NOTES (for the orchestrator)
- A1 header inconsistency: fulltext l12 `rendered_pages: [none]` vs structured l8 render checks on pages 4-44. Values on interleaved pages rest on renders A3 cannot see. Arithmetic ties support them (Section 0). Verifier sampling should include R789 (BKC Q2FY26 revenue 175) and R454/R464 (BKC and Sion PTD revenue).
- R840/R1068 page label 32 should read 33. Content is correct.
- No prior deck. F5, F15 and the cross-quarter half of F16 are not assessable this run. The next quarter's A3 should diff against this deck: guidance slide, pipeline serial numbers, launch dates, "% launched units sold" footnote.

```yaml
stage: A3-forensics
company: "RAYMONDREL"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/raymondrel-q2fy27/work/forensics_presentation_raymondrel_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: N.A.
  F11: FINDING
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "l318 s18 R224", classification: "FORWARD-SIGNAL", implication: "Zero Q2 launches; H2 pre-sales hinge on Mahim-2 Q3 and Mahim-1 Q4 FY27"}
  - {id: "A3-02", check: "F1", line: "l607 s35 R664/R672", classification: "FORWARD-SIGNAL", implication: "Invictus Tower B bookings 5->2->0, Q2 value 0; Thane luxury velocity stalled"}
  - {id: "A3-03", check: "F1", line: "l700/l703 s41 R774/R782", classification: "AMBIGUOUS", implication: "BKC net cancellation Q1 (-1 unit, -Rs 6 Cr); Q2 rebound includes 11 retail units"}
  - {id: "A3-04", check: "F1", line: "s5/s8/s23/s29-s43 (41 rows)", classification: "NEUTRAL-FACT", implication: "Remaining zero rows are pre-launch, unlaunched-cohort, sold-out or rounding"}
  - {id: "A3-05", check: "F6", line: "l172-173 s9; l347-359 s21", classification: "FORWARD-SIGNAL", implication: "H1 EBITDA 14.3%/PAT 5.1% vs guide 17-19%/9-10%; H2 needs ~19.7%/12.9% for low end"}
  - {id: "A3-06", check: "F6", line: "l170 s9 R964", classification: "AMBIGUOUS", implication: "~20% FY27 pre-sales guide implies H2 ~Rs 2,026 Cr vs H2 FY26 Rs 2,263 Cr (-10%)"}
  - {id: "A3-07", check: "F6", line: "l461 s26 R969", classification: "FORWARD-SIGNAL", implication: "Mahim-1 at Q4 FY27 touches checklist #4 red line; prior date needed"}
  - {id: "A3-08", check: "F6", line: "l464 s26 R972", classification: "FORWARD-SIGNAL", implication: "Thane parcel launch Q2 FY28, not FY27 as tracker expects; monetisation deferred"}
  - {id: "A3-09", check: "F6", line: "l504,l553-554,l621 vs l687-690,l704,l720-721,l734", classification: "CONFIRMATORY-NEGATIVE", implication: "I-1 red: only Thane delivering OCs; all MMR JDAs early-stage"}
  - {id: "A3-10", check: "F6", line: "l171-173 s9 R965/R967", classification: "AMBIGUOUS", implication: "PAT margin and ROCE now guided; Notion I-6 says refusal; OCF still unguided"}
  - {id: "A3-11", check: "F7", line: "l124 s5 R962", classification: "FORWARD-SIGNAL", implication: "Pre-emptive % margin hedge; EBITDA/revenue FY23 25.6% to H1 FY27 14.3% as JDA share 9% to 52%"}
  - {id: "A3-12", check: "F7", line: "l744 s44 R1080", classification: "AMBIGUOUS", implication: "Pre-demerger comparatives regrouped; basis of FY20-FY26 history NOT FOUND"}
  - {id: "A3-13", check: "F7", line: "l164-166 s8 R963/R1044", classification: "AMBIGUOUS", implication: "Rs 14,375 Cr surplus excludes S&M 5-6%, overhead, interest, tax"}
  - {id: "A3-14", check: "F8", line: "l355-358 s21 R301-R304", classification: "AMBIGUOUS", implication: "ETR 13-19.7% vs 25.17% statutory every period; step-up risk; deferred tax NOT FOUND"}
  - {id: "A3-15", check: "F11", line: "l180 s10; l405-406 s23 R133/R367", classification: "FORWARD-SIGNAL", implication: "Derived net debt Rs 912 Cr (+256 H1); first signal >900 lit; Rs 1,122 Cr if AIF 210 counted"}
  - {id: "A3-16", check: "F11", line: "l401,l404 s23; l366 s21", classification: "AMBIGUOUS", implication: "Debt +206 vs bank loan +155; cash finance 26 vs bank interest 55; interest may accrue into debt"}
  - {id: "A3-17", check: "F11", line: "l377 s22 R325/R326", classification: "AMBIGUOUS", implication: "Equity +55 vs PAT 66; warrant money not visible; NCI inclusion unstated"}
  - {id: "A3-18", check: "F12", line: "l392-397 s23; l372-379 s22", classification: "FORWARD-SIGNAL", implication: "Pre-launch cohort -185 (approvals 178); current assets +821 in H1; I-2/I-4 adverse"}
  - {id: "A3-19", check: "F14", line: "l218 s13 R172", classification: "AMBIGUOUS", implication: "'Board Independence 100%' vs 5 of 8 directors independent; governance claim drafting"}
  - {id: "A3-20", check: "F14", line: "l68 s3 vs l178 s10", classification: "AMBIGUOUS", implication: "GDV 52,000 labelled FY26 vs FY26 42,000; ~Rs 10,000 Cr H1 addition bears on I-5"}
  - {id: "A3-21", check: "F14", line: "l92 s4 vs l443 s25", classification: "AMBIGUOUS", implication: "Revenue recognised 9,500 vs 10,078; gap equals BKC 577"}
  - {id: "A3-22", check: "F14", line: "l346,l371,l385,l630-637,l423-424", classification: "AMBIGUOUS", implication: "12 unresolved markers; Park Street collections absent, totals tie only if zero"}
  - {id: "A3-23", check: "F14", line: "l29 cover; l742 s44", classification: "NEUTRAL-FACT", implication: "Deck P&L/BS basis unlabelled and unreviewed; reconcile to filed results"}
  - {id: "A3-24", check: "F16", line: "l427 s25; l702 s41 R454/R453", classification: "AMBIGUOUS", implication: "BKC revenue 577 > bookings 521, collections 64, shore piling; non-sale revenue in EBITDA"}
  - {id: "A3-25", check: "F16", line: "l707 s41 R789; l428 s25 R1019", classification: "AMBIGUOUS", implication: "BKC Rs 175 Cr revenue in Q2FY26 before Q3 FY26 launch with zero bookings; inflates YoY base"}
  - {id: "A3-26", check: "F16", line: "l429 s25; l733-734 s43", classification: "AMBIGUOUS", implication: "Sion revenue 242 > bookings 229, collections 36, shore piling"}
  - {id: "A3-27", check: "F16", line: "l143 s7; l426-430 s25", classification: "FORWARD-SIGNAL", implication: "JDA revenue 2,549 vs JDA collections 857; Q2 JDA revenue 328 vs collections 165; I-2 red"}
  - {id: "A3-28", check: "F11", line: "l364-367 s21 R315-R318", classification: "FORWARD-SIGNAL", implication: "Govt-authority interest +125% H1; deferred premium liability outside Rs 1,220 Cr debt"}
  - {id: "A3-29", check: "F16", line: "l415-430 s25; l453-459 s26", classification: "AMBIGUOUS", implication: "Launched Sr.7 (likely EWS) and pipeline Sr.4 dropped; pipeline project removed?"}
  - {id: "A3-30", check: "F16", line: "l511-520 s29; l430 s25", classification: "AMBIGUOUS", implication: "% sold on launched units, footnote missing; Wadala 61% vs 23% by area"}
  - {id: "A3-31", check: "F16", line: "l149 s7; l444 s25", classification: "AMBIGUOUS", implication: "GST-inclusive collections netted against bookings; collection growth may be flattered"}
  - {id: "A3-32", check: "F16", line: "l426,l430 s25; l460-463 s26", classification: "AMBIGUOUS", implication: "Pre-sales at 100% of JDAs (Wadala 62%, Parel 55%); overstates economic share"}
  - {id: "A3-33", check: "F16", line: "l311-322 s18 vs l358-359 s21", classification: "CONFIRMATORY-NEGATIVE", implication: "Highlights omit PAT -12% Q2 / -14% H1; interest drove the decline"}
  - {id: "A3-34", check: "F16", line: "l318-319 s18 vs l708 s41", classification: "AMBIGUOUS", implication: "'Entirely Address by GS' unsupported: Address projects 53% of Q2 revenue; BKC retail launched"}
  - {id: "A3-35", check: "F16", line: "l347-352 s21 R259-R262", classification: "AMBIGUOUS", implication: "EBITDA includes other income; ex-OI Q1 11.4%, Q2 14.3% fires a 15% stop; input to pending ruling"}
forward_signals: ["A3-01", "A3-02", "A3-05", "A3-07", "A3-08", "A3-11", "A3-15", "A3-18", "A3-27", "A3-28"]
ambiguous: ["A3-03", "A3-06", "A3-10", "A3-12", "A3-13", "A3-14", "A3-16", "A3-17", "A3-19", "A3-20", "A3-21", "A3-22", "A3-24", "A3-25", "A3-26", "A3-29", "A3-30", "A3-31", "A3-32", "A3-34", "A3-35"]
commitments:
  - {commitment: "Mahim-2 launch, Rs 2,300 Cr", implied_date: "Q3 FY27", ref: "s26 l460 R968", status_word: "initiated"}
  - {commitment: "Mahim-1 launch, Rs 1,800 Cr", implied_date: "Q4 FY27", ref: "s26 l461 R969", status_word: "initiated"}
  - {commitment: "Kandivali launch, Rs 3,000 Cr", implied_date: "Q2 FY28", ref: "s26 l462 R970", status_word: "initiated"}
  - {commitment: "Parel launch, Rs 8,500 Cr", implied_date: "Q2 FY28", ref: "s26 l463 R971", status_word: "initiated"}
  - {commitment: "Thane Owned Land Parcel launch, Rs 8,500 Cr", implied_date: "Q2 FY28", ref: "s26 l464 R972", status_word: "initiated"}
  - {commitment: "FY27 guide: pre-sales ~20%, ROCE ~20%, EBITDA 17-19%, PAT 9-10%", implied_date: "Mar-2027", ref: "s9 l169-173 R964-R967", status_word: "initiated"}
  - {commitment: "Rs 14,375 Cr net surplus project cash flow", implied_date: "through FY36", ref: "s8 l164 R963", status_word: "initiated"}
  - {commitment: "Realisations improve with Mahim/Parel; EBITDA per sq ft shall improve", implied_date: "Q3 FY27-Q2 FY28", ref: "s5 l123-124 R961/R962", status_word: "initiated"}
  - {commitment: "TenX Habitat OC all towers", implied_date: "done (RERA Q4 FY27)", ref: "s28 l504 R974", status_word: "completed"}
  - {commitment: "Address S1 Towers A, B OC", implied_date: "done (RERA Q4 FY28)", ref: "s31 l553-554 R977", status_word: "completed"}
  - {commitment: "Park Avenue 1A OC; 1B finishing", implied_date: "Q4 FY29", ref: "s36 l621-622 R982", status_word: "underway"}
  - {commitment: "TenX Era Towers A-C finishing", implied_date: "Q4 FY29", ref: "s30 l537-539 R976", status_word: "underway"}
  - {commitment: "Address S2 Towers C/D/E slab work", implied_date: "Q4 FY29", ref: "s32 l567-569 R978", status_word: "underway"}
  - {commitment: "Invictus Tower A 28th slab", implied_date: "Q4 FY29", ref: "s34 l601 R980", status_word: "underway"}
  - {commitment: "Address S3 Tower F, Invictus Tower B foundation", implied_date: "Q2 FY32", ref: "s33 l579; s35 l613", status_word: "underway"}
  - {commitment: "TenX District 9 excavation/PCC", implied_date: "Q1 FY33", ref: "s29 l519-521 R975", status_word: "underway"}
  - {commitment: "Park Street excavation", implied_date: "Q1 FY33", ref: "s37 l632 R983", status_word: "underway"}
  - {commitment: "Bandra JDA Towers A-D slab work", implied_date: "Q1 FY31", ref: "s40 l686-690 R984", status_word: "underway"}
  - {commitment: "BKC JDA shore piling", implied_date: "Q2 FY32", ref: "s41 l703-704 R985", status_word: "underway"}
  - {commitment: "Wadala JDA excavation/sub-structure", implied_date: "Q4 FY31", ref: "s42 l720-721 R986", status_word: "underway"}
  - {commitment: "Sion JDA shore piling", implied_date: "Q2 FY31", ref: "s43 l734 R987", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "Top item: JDA revenue runs ahead of cash, and at BKC and Sion ahead of bookings (577 vs 521; 242 vs 229). BKC booked Rs 175 Cr revenue in Q2FY26, a quarter before its Q3 FY26 launch, with zero bookings. Page 5 revenue recognised (9,500) equals page 26 (10,078) minus BKC 577 within Rs 1 Cr, which suggests BKC revenue is not unit-sale revenue [INFERENCE]; landowner-share barter revenue is a candidate. If so, EBITDA carries non-cash revenue and the JDA revenue-to-collection gap (2,549 vs 857) is structural. Second: deck EBITDA includes other income. Ex-other-income Q1 11.4%, Q2 14.3%, so a 15% operating stop fires while the deck-basis stop does not; feed this to the pending margin ruling. Third: derived net debt 912 (1,220 less closing balance 308; same method gives the 656 baseline). Debt rose 206 on a 155 bank inflow, and cash finance cost 26 sits against 55 bank interest; interest may roll into debt. Government-authority interest (+125% H1) points to an off-debt premium liability. Thane parcel launch is Q2 FY28, not FY27."
```
