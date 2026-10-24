# A3 FORENSIC NOTES: Fairchem Organics (FAIRCHEMOR) Q2 FY27, doctype RESULTS (filing 22-Oct-2026)

Agent: A3 forensic notes | model claude-opus-5-5 | run date 2026-10-23
Inputs read: A1 structured (R001-R484), A1 fulltext (lines 1-680), A2 ledger. Source PDF and inputs/ not opened.
Prior-quarter extract: NONE (first quarterly run for this ticker). Prior-quarter auditor paragraph NOT AVAILABLE, so no verbatim EoM diff and no entity-list diff were possible.
Monitoring checklist: NONE. No Notion COMPANIES MASTER page, no companies/FAIRCHEMOR.md, no spear on record. This is a PRE-THESIS READ: findings are not tested against any thesis.
Units: Rs Lakhs as printed (x0.01 = Rs Cr). Derived numbers are marked [DERIVED]; inferences are marked [INFERENCE].

## 0. LEDGER RECONCILIATION

- Structured rows: 484. Ledger rows accounted for: 484 (A2 coverage index, orphan_ids empty). Rows read by A3: 484. Reconciled: 100%.
- Every value row was read in the structured file and located in the fulltext. Statement arithmetic re-run by A3 (all tie):
  - P&L: Q2 FY27 expenses 12,553.80 + 287.81 + 614.41 + 118.05 + 741.74 + 285.35 + 740.91 = 15,342.07; PBT 16,707.08 - 15,342.07 = 1,365.01. Q2 FY26, H1 FY26 and FY26 expense columns also tie (11,071.94; 24,030.05; 45,275.11). FY26 PBT 820.27 - 88.27 = 732.00.
  - Balance sheet: non-current assets 21,846.56 / 21,908.70; current assets ex held-for-sale 17,600.86 / 16,793.56; current liabilities ex held-for-sale 8,862.94 / 10,326.16; totals 39,843.09 / 39,097.93. All tie.
  - Cash flow: 2,405.23 - 439.67 - 1,966.34 = (0.78); opening 1.35, closing 0.57. Operating adjustments tie to 3,660.10 / 971.97.
  - Segment PBT ties to P&L PBT for every column; segment assets and liabilities equal balance-sheet totals at 30-Sep-2026 and 31-Mar-2026.
- A2 FOOTNOTE_UNRESOLVED R462/R464 (R192/R193, R226/R227) are RESOLVED by arithmetic: each unlabelled number is the current-asset (or current-liability) subtotal before the held-for-sale line (sums above). R467 "Changes" (line 406) carries no value; it is a layout fragment. Neither is a numbers issue. Both count under F14 as drafting defects.
- A1 anchor defect (pipeline note, not a company finding). Several ZERO_STANDING "-" rows are anchored to hyphens in addresses, dates or labels, not to the table dash. Examples: R009 line 215 (address "Sanand - Kadi Highway"), R010 line 223 and R011 line 224 (date hyphens), R160 line 272 (address), R236 line 389 (address), R309 line 483 ("IND AS 108 - "). The real dashes sit at line 245 ("-  -  -  -  88.27": Exceptional Item, four FY27/Q2FY26 columns), line 247 (H1 FY26 dash), line 293 (ROU), line 348 (lease liability), line 370 (current tax liability), lines 412/440/441/448/451 (cash flow) and lines 498/501/502 (segment). R059 "4.55" is anchored to line 238 (substring of "2,314.55"); the value sits at line 258. All values are correct; only the anchors are wrong. Recommend an A1 fix: never anchor a bare "-" or a substring match.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R160 R161 (ZERO_STANDING) vs R165 R206; R245 R258 vs R287 R295 | 293; 348; 440; 448 | L293 "194.35  -" (Right to Use Asset 30-Sep-2026 / 31-Mar-2026); L348 "(i) Lease Liabilities  158.17  -"; L440 "(11.17)  -"; L448 "(25.61)  -" | AMBIGUOUS | A new lease began in H1 FY27: ROU Rs 1.94 Cr, initial direct cost Rs 0.11 Cr, H1 lease repayment Rs 0.26 Cr. The filing names neither the asset nor the lessor. In the same meeting the Board approved buying land next to the plant from the CMD (A3-07). Ask what was leased, from whom (related party or not), and for how long. |
| A3-02 | F6 | R004 R412-R415 R372-R375 R480 | 67-70; 582-591 | L68 "approved the Related Party Transaction for the purchase of 2 separate pieces of land"; L582-584 "agreement is being entered"; L588-591 "Rs. 12.01 Crores (exclusive of stamp duty and Registration Fees and other related expenses which shall be in actuals)" | FORWARD-SIGNAL | Dateable commitment, status INITIATED (approved, agreement "being entered", not executed). No completion or registration date given. Stamp duty and registration come on top of Rs 12.01 Cr. Track execution, registration and the cash outflow in Q3 FY27 / Q4 FY27 filings. |
| A3-03 | F8 | R094-R111; R246 (CF) ; R172 R173 | 251; 252; 411-412; 298-299 | L251 "310.73  359.79  (10.05)  670.52  21.10  6.53" (Current Tax: Q2FY27, Q1FY27, Q2FY26, H1FY27, H1FY26, FY26); L411 "Provision for Non-current Tax Assets"; L412 "73.46  -" | AMBIGUOUS | ETR [DERIVED]: Q2 FY27 25.51%, Q1 FY27 26.57%, H1 FY27 26.04%, Q2 FY26 34.43%, H1 FY26 30.34%, FY26 24.31% (statutory 25.17%). Three earlier-period signals, none labelled "earlier years": (a) current tax is negative (10.05) in a profit quarter (Q2 FY26); (b) FY26 current tax is 6.53 on PBT 732.00 (0.9%), so H2 FY26 current tax was (14.57) [DERIVED]; (c) H1 FY27 carries a new Rs 73.46 L "Provision for Non-current Tax Assets" (added back in CF, nil in H1 FY26), and non-current tax assets fell 395.92 to 291.71. [INFERENCE] tax refund claims for earlier years are being written down. A1 assigned the CF adjustment labels by order only, so the 73.46 label carries that caveat. Deferred tax is a persistent CHARGE (no DTA shield); DTL 2,056.97 to 2,092.43 ties to P&L deferred 40.02 less OCI tax 4.55. Cash tax paid rose to 578.74 from 239.50. FY27 is the first clean ~25-26% ETR base. Ask what the provision covers, which assessment years, and whether more is at risk. |
| A3-04 | F9 | R118-R134; R207 R208; R273 | 257; 349; 428 | L257 "33.20  (51.28)  (13.75)  (18.08)  (22.35)  49.86" (remeasurement: Q2FY27, Q1FY27, Q2FY26, H1FY27, H1FY26, FY26); L349 "445.87  310.77" (Provisions, non-current) | AMBIGUOUS | The Q1 FY27 actuarial loss of Rs 51.28 L exceeds the full FY26 OCI (+49.86) in size and runs the opposite sign; Q2 FY27 then swings back +33.20. Non-current employee provisions rose 43% in H1 FY27 (310.77 to 445.87; CF L428 "135.10"), after the FY26 Labour Code exceptional charge of Rs 88.27 L (Note 5, L517). Amounts are small (H1 OCI is 0.7% of H1 PAT), but the pattern suggests an assumption change (discount rate or the Labour Code wage definition). Verify actuarial assumptions at the FY27 Annual Report. Ask whether part of the Labour Code cost now runs through employee expense each quarter despite the "nonrecurring" label (L518). |
| A3-05 | F12 | R351-R362; R213 R214; R293 | 510; 507; 360; 447 | L510 "11,660.41  12,484.50  9,434.16  11,660.41  9,434.16  12,793.90" (Segment Liabilities); L360 "(i) Borrowings  6,865.32  8,378.23" | AMBIGUOUS | Segment liabilities rose Rs 33.60 Cr in H2 FY26 (9,434.16 to 12,793.90) while segment assets rose only Rs 2.59 Cr [DERIVED]. That window holds the Rs 34 Cr buyback (settled 21-Jan-2026, L534-535). [INFERENCE] the buyback was largely debt-funded. Liabilities then fell Rs 11.33 Cr in H1 FY27. The balance sheet points to debt repayment (borrowings down 1,512.91; CF L447 "(1,512.93)"), funded by an inventory release of 2,230.80 that offset a receivables build of 3,200.20. Ask for borrowings at 30-Sep-2025, how the buyback was funded, and whether the Rs 12.01 Cr land purchase re-levers the balance sheet. |
| A3-06 | F12 | R166 R167 R163 R164 R283 | 292; 294-295; 437 | L292 "20,475.49  19,618.77" (PPE); L294 "829.48"; L295 "2.71  1,838.12" (CWIP 30-Sep-2026 / 31-Mar-2026) | FORWARD-SIGNAL | CWIP fell Rs 10.09 Cr in H1 FY27 while capex spend was only Rs 4.52 Cr (L437) and PPE rose Rs 8.57 Cr net of Rs 5.59 Cr depreciation [DERIVED]. [INFERENCE] a project of about Rs 10 Cr was capitalised (commissioned) in H1 FY27. No note names it. Ask what was commissioned, the capacity added, and the revenue or margin ramp expected from it. |
| A3-07 | F13 | R004 R386 R409-R411 R372-R375 R480-R483 | 69; 588-601; 611; 619-623 | L69 "from the Chairman & Managing Director of the"; L593 "6.07% shareholding, considering"; L611 "Yes, Promoters of the Company"; L621-623 "transaction and is being done at "arm's length" basis." | AMBIGUOUS | Rs 12.01 Cr for 6,182 sq m = about Rs 19,427 per sq m before stamp duty [DERIVED]. The filing discloses no valuer, valuation report or price basis; the arm's-length claim is self-asserted. Size [DERIVED]: 4.3% of net worth (28,182.68), 59.5% of H1 FY27 PAT (2,018.14), 49.9% of H1 FY27 CFO (2,405.23), 2.6% of FY26 revenue. [INFERENCE] at 2.6% of turnover it sits below the 10%-of-turnover material-RPT test, so no shareholder vote follows. Cash on hand is Rs 0.57 L (L315), so CFO or working-capital lines fund it. Lean bear: a promoter-to-company land sale with no disclosed valuation is a governance data point. Ask for the valuer's report, the per-sq-m benchmark, and the independent directors' vote. |
| A3-08 | F13 | R412 R413 R415 | 69; 599-601 | L69 "(adjoining to the plant of the Company)"; L601 "admeasuring in aggregate 6,182 Sq." | FORWARD-SIGNAL | Land next to the plant points to a site or capacity expansion. The filing states no capex plan, project or timeline (A1 FORWARD table holds only the RPT). Ask what will be built, the capex, the timeline and the funding. A4 can cover A3-02 and A3-08 in one question set. |
| A3-09 | F14 | R002 R003 R426 R446 R423 | 46-47; 196; 552; 114; 163-164 | L46-47 "commenced at 03.30 p.m. and concluded at 04.15 p.m."; L552 "Date: 2026.10.22 15:41:45 +05'30'" (CMD, results); L196 "Date: 2026.10.22 15:59:19 +05'30'" (auditor); L114 "Date: 2026.10.22 16:24:05 +05'30'" (CS) | AMBIGUOUS | The CMD signed the results 11 minutes after the meeting opened and 34 minutes before it closed. The auditor signed 16 minutes before close, and auditor para 2 says the Statement was "approved by its Board of Directors" (L163-164). A sequenced agenda (results first, RPT second) explains this benignly. The filing does not record when the results resolution passed or when the Audit Committee met. Lean bear: if the auditor signed before Board approval, that is a procedural lapse. Ask for the time of the results resolution and the Audit Committee meeting. |
| A3-10 | F14 | R194 R195 R228 R229 (R192/R193, R226/R227 context) | 324; 328; 372-373; 380 | L324 "395.67  395.67"; L328 "Asset Held for Sale"; L372 "101.00"; L373 "100.00"; L380 "Liabilities held for sale" | FORWARD-SIGNAL | A disposal group (assets Rs 3.96 Cr, liabilities Rs 1.00 Cr rising to Rs 1.01 Cr) has sat in held-for-sale since at least 31-Mar-2026. None of Notes 1-7 (L469-540) describes it. Ind AS 105 expects a sale within 12 months of classification. [INFERENCE] the round liability of Rs 100.00 L may be an advance from a buyer. A completed sale would bring a gain or loss against the 395.67 carrying value and a cash inflow. Ask what the asset is, who the buyer is (related party or not), when it was classified, and the expected closing date. |
| A3-11 | F14 | R213-R225; R206; R295 | 360; 362; 372; 348; 448 | L360 "(i) Borrowings"; L362 "(ii) Trade Payables"; L372 "(iv) Other Financial Liabilities" | AMBIGUOUS | Current financial liabilities skip item (iii). The new lease shows a non-current liability of 158.17 (L348) and H1 repayments of (25.61) (L448), but no current lease-liability line. Other Financial Liabilities hardly moved (206.57 to 206.60). [INFERENCE] the current lease portion is either inside another line or missing from the template. Low money value, but it is a presentation gap. Check the FY27 Annual Report lease note. |
| A3-12 | F14 | R463 R462 R464 R467; R376 vs auditor heading | 151; 157; 159; 340; 322; 371; 406 | L151 "Limited Review Report on unaudited financial results of Fairchem organics Limited"; L340 "Tota Equity"; L406 "Profit Before Tax  Changes" | NEUTRAL-FACT | Cumulative drafting defects: the auditor report writes the company name as "Fairchem organics" (L151, L157, L159) against "FAIRCHEM ORGANICS LIMITED" elsewhere; there is a "Tota Equity" typo; two subtotals carry no label (L322, L371; resolved by arithmetic); and the cash flow has a stray "Changes" label. Each is immaterial. Together with A3-10 and A3-11 they form a governance data point on filing care. Note text and auditor letter agree on scope (Note 1 L471 "performed limited review"; auditor L171 "We conducted our review"). |

## 2. CHECKLIST SCORECARD

| check | status | one-line basis |
|---|---|---|
| F1 Zero-value standing lines | FINDING | 19 ZERO_STANDING rows dispositioned (table 2a). Exceptional Item nil in all FY27 periods is a template carry from FY26 (Labour Code Rs 88.27 L, Note 5); the five H1 FY26 CF dashes are classes that are new in FY27. Lease lines nil at FY26 end and populated at 30-Sep-2026 = A3-01. |
| F2 S-vs-C decomposition | N.A. | Standalone-only filing. Note 4 L513: "The Company does not have any subsidiary/associate/joint venture company as on September 30, 2026." No consolidated statement exists to compare. |
| F3 Shell-entity detection | N.A. | No subsidiaries (Note 4 L513); no consolidated cost lines to compare; no Going Concern EoM. |
| F4 Unaudited contribution ratio | PASS | Auditor reviewed the whole Statement (L159-161). No Other Matters paragraph and no component auditors or JVs. Unaudited contribution = Rs 0 = 0% of PAT. |
| F5 Going concern / EoM scope | PASS | Review report paras 1-4 (L159-185) carry no EoM, Other Matters or Going Concern language; conclusion unmodified (L180). Prior-quarter auditor paragraph NOT AVAILABLE (first run), so no verbatim quarter-on-quarter diff was performed. Next run must diff against L159-185. |
| F6 Forward-commitment phrases | FINDING | Lexicon hits: "approved" L68 (land RPT, initiated = A3-02), "commenced" L529 and "completed" L534 (buyback, closed Jan 2026). No "expected", "will be", "subject to approval", "in the process of", "proposes", "intends" hits. |
| F7 Hedge phrases | PASS | No lexicon hit in Notes 1-7 or Annexure B. The only near-match is the SRE 2410 boilerplate L176-177 "does not enable us to obtain assurance", which is standard review language, not a note hedge. |
| F8 Tax forensics | FINDING | ETR 24.3%-34.4% across periods; negative current tax in Q2 FY26; FY26 current tax 0.9% of PBT; new Rs 73.46 L provision against non-current tax assets in H1 FY27 = A3-03. |
| F9 OCI forensics | FINDING | Q1 FY27 remeasurement loss (51.28) exceeds the full FY26 OCI (+49.86) in size; NC provisions +43% in H1 = A3-04. |
| F10 Share count and dilution | PASS | Paid-up 1,302.09 (Q2/H1 FY26) to 1,259.59 (FY26 onward): a drop of 42.50 = 4,25,000 shares x Rs 10, traced to the Note 6 buyback (L521-536; extinguished 27-Jan-2026). Basic = diluted EPS in every period (L264-266): no dilutive instruments. EPS re-derived: 1,016.76 / 125.959 L shares = 8.07. |
| F11 Reserves and net worth tie-out | PASS | 1,259.59 + 26,923.09 = 28,182.68; 1,259.59 + 25,044.44 = 26,304.03 (L336-338). Other Equity movement 1,878.65 = H1 TCI 2,004.61 less dividend 125.96 (paid 125.31 L450 + 0.65 to the restricted account L451). Exact tie. No third-party net worth number in the filing. |
| F12 Segment forensics | FINDING | Single segment; segment assets and liabilities equal balance-sheet totals. Liability path around the buyback = A3-05; CWIP capitalisation = A3-06. No zero-revenue asset build. |
| F13 Board outcome beyond results | FINDING | Item 2 land RPT with the CMD and relatives = A3-07 (pricing, governance) and A3-08 (expansion signal). No AR, AGM, record date, director appointment, auditor change or capital-raising item. No Role 6 event to schedule. |
| F14 Note drafting inconsistencies | FINDING | Signatures before meeting close (A3-09), held-for-sale with no note (A3-10), missing current lease line (A3-11), cosmetic defects (A3-12). Note text and auditor letter agree on limited review. |
| F15 Entity list diffs | PASS | Consolidation list is empty (Note 4 L513). Prior-quarter list NOT AVAILABLE (first run), so the diff is untested. Next run must diff against Note 4. |
| F16 Presentation dropped/reframed | N.A. | Results filing; no deck. |
| F17 Concall silence audit | N.A. | Results filing; no transcript; no monitoring checklist exists (pre-thesis). |

### 2a. F1 ZERO_STANDING disposition (19 rows)

| rows | line item | why the line exists / what it anticipates | disposition |
|---|---|---|---|
| R009 R010 R011 R036 R078 | P&L Exceptional Item, nil in Q2FY27, Q1FY27, Q2FY26, H1FY27, H1FY26 (true dash at L245, L247) | Carried because the FY26 column holds the Rs 88.27 L Labour Code charge (L245 "88.27"; Note 5 L515-519). It anticipates nothing new. | No finding |
| R310 R311 R335 R342 R344 | Segment "Less: Exceptional Items (Note 5)", same periods | Mirror of the P&L line; FY26 (88.27) at L501 | No finding |
| R309 | Segment interest income, Q1 FY27 | Q1 nil, H1 0.22 = Q2 0.22 (L498); ties to CF interest income (0.22) L411 | No finding |
| R160 R161 | ROU asset, NC lease liability at 31-Mar-2026 | New lease in H1 FY27 | A3-01 |
| R162 | Current tax liability at 31-Mar-2026 | Interim provision 61.02 exceeds advance tax at 30-Sep-2026; normal interim pattern | No finding |
| R245 R258 | CF H1 FY26: ROU initial direct cost, lease repayment | Same new lease (11.17; 25.61) | A3-01 |
| R236 | CF H1 FY26: Provision for NC tax assets | New FY27 class (73.46) | A3-03 |
| R247 | CF H1 FY26: FD redemption | 0.27 in H1 FY27; immaterial | No finding |
| R267 | CF H1 FY26: dividend/restricted bank balance | 0.65 unpaid dividend moved to restricted account in H1 FY27; ties F11 | No finding |

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| Purchase 2 pieces of land (6,182 sq m, next to the plant) from CMD Nahoosh Jariwala and relatives for Rs 12.01 Cr, plus stamp duty and registration at actuals | NOT DISCLOSED (approved 22-Oct-2026; agreement "being entered") | Board outcome item 2 L67-70; Annexure B L582-623 | initiated |
| Buyback of 4,25,000 shares at Rs 800 (cap Rs 34 Cr), tender route | Completed: offer 8-14 Jan 2026; settled 21-Jan-2026; extinguished 27-Jan-2026 | Note 6 L521-536 | completed |
| Sale of held-for-sale disposal group (assets 395.67, liabilities 101.00) | Implied by Ind AS 105 classification (sale expected within 12 months); date NOT DISCLOSED; no note | Balance sheet L324, L328, L372-373, L380 | not stated (implied by classification) |

## 4. FLAGS FOR A4 (management questions)

FORWARD-SIGNAL: A3-02, A3-06, A3-08, A3-10.
AMBIGUOUS: A3-01, A3-03, A3-04, A3-05, A3-07, A3-09, A3-11.
NEUTRAL-FACT (no question needed): A3-12.
A2 flags weighed: SIGNATURE_BEFORE_MEETING_END -> A3-09; RELATED_PARTY -> A3-07, A3-08, A3-02; FOOTNOTE_UNRESOLVED -> resolved by arithmetic, residue in A3-12 and A3-10; lease lines at 30-Sep-2026 -> A3-01, A3-11.

## 5. LIMITATIONS

- First quarterly run: F5 and F15 had no prior quarter to diff. Both checks hold the current baseline for the next run.
- Pre-thesis read: no thesis or monitoring checklist exists, so no finding is weighed against a thesis claim.
- The page 5-7 layout text is column-scrambled. A1 assigned labels by default-order reading plus sum checks; A3 re-verified every statement total. The CF adjustment labels (incl. the 73.46 provision) are assigned by order only (A1 header).
- Not disclosed in this filing (NOT FOUND): dividend per share, borrowings at 30-Sep-2025, the held-for-sale asset, the leased asset, the capitalised project, the land valuation basis.

## 6. ADDENDUM: CORRECTION LOOP ITERATION 1 (2026-10-24)

Scope: the two rows A5 named as uncited. Sections 0-5 above stand unchanged. Rows read for this addendum: results structured R293, R294, R372-R375, R480-R482; results fulltext L336-383, L400-459, L575-629; A2 ledger lines 45, 58, 85; cross-reference (read-only) deck structured R237-R239 and its unit header (line 4 "Rs Mn (Millions)"); concall fulltext L198-213 and L322-337. Source PDF and inputs/ not opened.

Ledger coverage: R294 sits in the A2 block "R236-R307 | Cash flow p7, 72 rows" (ledger line 45) with no flag. R374 and R481 sit in the RELATED_PARTY rows at ledger lines 58 and 85. Coverage stays at 100%. The gap was a citation gap in A3, not a ledger gap.

### 6a. Addendum findings

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-13 | F12 | R294 (with R293; R213 R214; deck R237 R238 R239) | results L447, L448, L360, L409, L450; deck structured R237 (deck line 521) | L447 "(1,512.93)        (862.76)" (Repayment of Current Borrowings (net), H1 FY27 / H1 FY26; label at L448); L360 "(i) Borrowings  6,865.32  8,378.23"; deck R237 "630" (Current borrowings, FY25, Rs Mn) | AMBIGUOUS | Deck R237 puts current borrowings at 31-Mar-2025 at Rs 630 Mn = about 6,300 L. The filing shows no non-current borrowings (non-current financial liabilities hold only the lease, L348). Borrowings at 30-Sep-2025 [DERIVED] = 6,300 - 862.76 = about 5,437 L (Rs 54.4 Cr). Borrowings at 31-Mar-2026 were 8,378.23 L (L360), so H2 FY26 borrowings rose about 2,941 L (Rs 29.4 Cr) [DERIVED]. The buyback in that window cost Rs 34 Cr (4,25,000 x Rs 800). The rise equals about 86% of the buyback cash [DERIVED]. This sharpens A3-05: [INFERENCE] the buyback was mostly funded by bank lines, not by cash from operations. H1 FY26 shows the reverse pattern: CFO 3,065.82 (L431) paid both the 976.57 dividend (L450) and the 862.76 repayment. Finance costs rose 87% H1 on H1 (L409 "301.84  161.48") [DERIVED], which fits a higher average debt after the buyback. At 30-Sep-2026, borrowings of 6,865.32 L remain about 1,428 L above the 30-Sep-2025 level [DERIVED]. Two caveats lean bear and keep this AMBIGUOUS. First, deck R237 is ORDER_INFERRED and the deck truncates (FY26 8,378.23 L prints as "837", R238), so the FY25 base carries about +/-10 L of error. Second, the CF line is a net figure; FX revaluation on any foreign-currency loan would break the balance-to-flow tie. The H2 FY26 rise could also be partly working capital (no 30-Sep-2025 balance sheet is in this filing). The two readings are "buyback debt-funded" and "H2 working-capital build". One observation separates them: the 30-Sep-2025 borrowing figure and the H2 FY26 receivables and inventory movement. If the Rs 12.01 Cr land (A3-07) is also paid from bank lines, borrowings return to about 8,066 L before stamp duty [DERIVED], close to the 31-Mar-2026 peak. For A4: convert the A3-05 question "borrowings at 30-Sep-2025" into a confirmation of about Rs 54 Cr. Then ask how much of the Rs 29 Cr H2 FY26 rise funded the buyback, and how the land will be paid for. |
| A3-14 | F13 | R374 with qualifier R481 (R372 R373 R375 R480 R482; ledger lines 58, 85) | results L593-597, L582-584, L588, L611; concall L205, L330-331 | L593-597 "6.07% shareholding, considering entities holding shares in which he is interested"; L582-584 "Shri Nahoosh Jariwala and his relatives"; concall L205 "it's already been getting used in our operations as well as our worker colony" | AMBIGUOUS | Item 4 of Annexure B gives the counterparty's shareholding as 6.07%. That figure is the CMD's look-through stake only. The counterparty is the CMD "and his relatives" (L582-584), and the relatives' holdings are not disclosed. The promoter-group total is NOT FOUND in this filing. So the disclosure under-states, or at least does not state, the whole selling group's stake. Economics at the disclosed 6.07% [DERIVED]: the CMD bears about Rs 0.73 Cr of the Rs 12.01 Cr outflow through his stake. Other holders bear about Rs 11.28 Cr (93.93%). For each Rs 1 of any overpayment, the CMD gains about Rs 0.94 net. At this stake the seller's incentive to price at arm's length is weak, and the filing gives no valuer or price basis (A3-07). The concall changes the use reading. Management says the land is "already been getting used in our operations as well as our worker colony" and that "we thought of getting it through in the current period" (concall L205). Attribution caveat: the transcript is garbled. At L330 a participant (not management) frames the question "Since we do not have any immediate expansion plans", and the L331 reply "then we need CAPEX" does not dispute it. [INFERENCE] the purchase regularises land the company already uses. It is not a new expansion site. This weakens the expansion reading in A3-08, which stands as written, with this addendum recorded against it. It raises one new question. On what terms (rent, licence, or free) did the company use promoter land before? Is that use linked to the new H1 FY27 lease (A3-01)? Lean bear: buying land already in use, at a self-asserted price, from a seller with a low look-through stake, while cash is Rs 0.57 L, is a value-transfer data point until a valuation is produced. For A4, ask: (1) the relatives' names and stakes, and the selling group's total stake; (2) the prior usage terms and the rent paid in FY26 and H1 FY27; (3) why buy now and not keep leasing; (4) the valuer's report. |

### 6b. Scorecard and register effect

- No checklist status changes. F12 and F13 were already FINDING. A3-13 adds to F12 and A3-14 adds to F13.
- Commitment register: no new commitment. The land row (Section 3) now carries a use note: per concall L205 the land is already in operational use.
- Section 5 NOT FOUND item "borrowings at 30-Sep-2025" is now DERIVED (about 5,437 L) from deck R237 and results R294, with the caveats in A3-13. It is not a filed figure.

### 6c. Updated flags for A4

FORWARD-SIGNAL: A3-02, A3-06, A3-08, A3-10.
AMBIGUOUS: A3-01, A3-03, A3-04, A3-05, A3-07, A3-09, A3-11, A3-13, A3-14.
NEUTRAL-FACT: A3-12.
Suggested merges: A3-05 + A3-13 (one debt-funding question set); A3-07 + A3-14 + A3-08 + A3-01 (one land and lease question set).

```yaml
stage: A3-forensics
company: "FAIRCHEMOR"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
loop_iteration: 1
forensics_path: "runs/fairchemor-q2fy27/work/forensics_fairchemor_q2fy27_results.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "293; 348; 440; 448", classification: "AMBIGUOUS", implication: "New lease in H1 FY27 (ROU 194.35 L, lease liability 158.17 L, repayment 25.61 L); asset and lessor undisclosed; ask if related party or tied to plant expansion"}
  - {id: "A3-02", check: "F6", line: "67-70; 582-591", classification: "FORWARD-SIGNAL", implication: "Land RPT Rs 12.01 Cr plus stamp duty at actuals approved, agreement being entered, no completion date; track execution and cash outflow Q3/Q4 FY27"}
  - {id: "A3-03", check: "F8", line: "251; 411-412; 298-299", classification: "AMBIGUOUS", implication: "Negative current tax Q2FY26 (10.05), FY26 current tax 0.9% of PBT, new 73.46 L provision against NC tax assets in H1FY27; earlier-year tax claims likely written down; FY27 ETR ~26% is the clean base"}
  - {id: "A3-04", check: "F9", line: "257; 349; 428", classification: "AMBIGUOUS", implication: "Q1FY27 actuarial loss (51.28) exceeds full FY26 OCI 49.86; NC provisions +43% in H1; verify discount rate and Labour Code wage basis at FY27 AR"}
  - {id: "A3-05", check: "F12", line: "510; 360; 447", classification: "AMBIGUOUS", implication: "Segment liabilities +33.60 Cr in H2FY26 (buyback window), then -11.33 Cr in H1FY27 via borrowings repayment; buyback likely debt-funded; land purchase may re-lever"}
  - {id: "A3-06", check: "F12", line: "292; 294-295; 437", classification: "FORWARD-SIGNAL", implication: "CWIP fell 10.09 Cr against 4.52 Cr capex; about Rs 10 Cr project capitalised in H1FY27, unnamed; ask capacity and revenue ramp"}
  - {id: "A3-07", check: "F13", line: "69; 588-601; 611; 619-623", classification: "AMBIGUOUS", implication: "Promoter-to-company land sale at ~Rs 19,427/sq m, no valuer or price basis disclosed, arm's length self-asserted; 59.5% of H1 PAT; cash 0.57 L so funded from CFO or WC lines"}
  - {id: "A3-08", check: "F13", line: "69; 599-601", classification: "FORWARD-SIGNAL", implication: "Land adjoining the plant foreshadows site or capacity expansion; no capex plan stated; ask project, capex, timeline, funding (addendum: concall L205 says land already in use, see A3-14)"}
  - {id: "A3-09", check: "F14", line: "46-47; 196; 552; 114", classification: "AMBIGUOUS", implication: "CMD signed 15:41:45 and auditor 15:59:19 inside a 15:30-16:15 meeting; benign if results passed first, lapse if auditor signed before Board approval; ask resolution and Audit Committee times"}
  - {id: "A3-10", check: "F14", line: "324; 328; 372-373; 380", classification: "FORWARD-SIGNAL", implication: "Held-for-sale assets 395.67 L and liabilities 101.00 L since at least 31-Mar-2026 with no note; pending disposal brings gain/loss and cash; ask asset, buyer, related-party status, date"}
  - {id: "A3-11", check: "F14", line: "360; 362; 372; 348; 448", classification: "AMBIGUOUS", implication: "Current financial liabilities skip item (iii); no current lease liability line despite 25.61 L H1 repayments; check AR lease note"}
  - {id: "A3-12", check: "F14", line: "151; 157; 159; 340; 322; 371; 406", classification: "NEUTRAL-FACT", implication: "Cumulative drafting defects (name case in auditor report, Tota Equity typo, unlabelled subtotals resolved by arithmetic, stray label); governance data point on filing care"}
  - {id: "A3-13", check: "F12", line: "results 447; 448; 360; 409; 450; deck R237 (deck line 521)", classification: "AMBIGUOUS", implication: "R294 H1 FY26 net repayment 862.76 L off deck FY25 current borrowings 630 Mn gives ~5,437 L at 30-Sep-2025 [DERIVED]; H2 FY26 rise ~2,941 L = ~86% of the Rs 34 Cr buyback; finance cost +87% H1 on H1; deck base ORDER_INFERRED and truncated, CF line net, H2 WC build not excluded; confirm 30-Sep-2025 borrowings and buyback funding; land on bank lines takes debt back to ~8,066 L"}
  - {id: "A3-14", check: "F13", line: "results 593-597; 582-584; 588; 611; concall 205; 330-331", classification: "AMBIGUOUS", implication: "R374/R481 6.07% is the CMD's look-through stake only; relatives' stakes and group total undisclosed; CMD gains ~Rs 0.94 net per Rs 1 overpaid; concall L205 says land already used for operations and worker colony, so the buy regularises existing use and weakens A3-08; ask relatives' stakes, prior usage terms and rent, why buy now, valuer report"}
forward_signals: ["A3-02", "A3-06", "A3-08", "A3-10"]
ambiguous: ["A3-01", "A3-03", "A3-04", "A3-05", "A3-07", "A3-09", "A3-11", "A3-13", "A3-14"]
commitments:
  - {commitment: "Purchase 2 pieces of land (6,182 sq m adjoining plant) from CMD and relatives, Rs 12.01 Cr plus stamp duty/registration at actuals (land already in operational use per concall L205)", implied_date: "NOT DISCLOSED", ref: "Board outcome item 2 L67-70; Annexure B L582-623", status_word: "initiated"}
  - {commitment: "Buyback 4,25,000 shares at Rs 800, cap Rs 34 Cr", implied_date: "Jan 2026 (settled 21-Jan-2026, extinguished 27-Jan-2026)", ref: "Note 6 L521-536", status_word: "completed"}
  - {commitment: "Sale of held-for-sale disposal group (assets 395.67 L, liabilities 101.00 L)", implied_date: "NOT DISCLOSED (Ind AS 105 implies within 12 months of classification)", ref: "Balance sheet L324, L328, L372-373, L380", status_word: "not stated"}
gate_a3: pass
blank_checks: []
analyst_note: "Pre-thesis read, first run: F5 and F15 have no prior quarter to diff; next run must diff auditor L159-185 and Note 4. One capital-allocation chain runs through this filing. H1 FY26: CFO paid a 976.57 L dividend and cut borrowings 862.76 L to about 5,437 L at 30-Sep-2025 (A3-13, derived from deck FY25 630 Mn). H2 FY26: borrowings rose about 2,941 L beside the Rs 34 Cr buyback, so roughly 86% of it looks debt-funded (A3-05, A3-13). H1 FY27: repaid 1,512.93 L, and now a Rs 12.01 Cr land purchase from the CMD with no disclosed valuation (A3-07). The CMD's disclosed look-through stake is 6.07%, so other holders bear about 94% of any overpayment; relatives' stakes are not disclosed (A3-14). Concall L205 says the land is already used for operations and a worker colony, which weakens the expansion reading in A3-08. Cash is Rs 0.57 L, so bank lines or operating cash fund the land. Tax (A3-03) matters because FY26 current tax was near zero. A1 anchors bare dashes to hyphens (values correct); fix in A1."
```
