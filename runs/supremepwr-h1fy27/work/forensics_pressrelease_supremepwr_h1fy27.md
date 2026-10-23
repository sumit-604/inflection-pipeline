# A3 FORENSIC NOTES: SUPREMEPWR H1 FY27, doctype PRESSRELEASE (presentation-class rules)

Document: Reg 30 press release dated 21.10.2026, 4 pages (A1 fulltext, 188 lines). Units Rs Cr (x1). "Derived" = A3 arithmetic on printed figures. [INFERENCE] = reasoned reading, not a filed fact.
Inputs read: A1 structured (R001-R166), A1 fulltext, A2 ledger. Prior-quarter extract: none, so a prior-period diff is NOT POSSIBLE. Notion checklist: none (PRE-THESIS READ); Spear load-bearing facts used as the checklist.
Cross-document ties: work/forensics_presentation_supremepwr_h1fy27.md (FP-xx) and work/forensics_supremepwr_h1fy27.md (FN-xx). The press release mostly restates the deck commentary (deck l.181-195). Findings already raised there are cited, not repeated.

## 1. LEDGER RECONCILIATION

Rows in ledger: 166. Rows read at their fulltext line: 166. Reconciled: 100%. Orphans: none.

Flag resolutions:
- R015 LAYOUT_OFFSET: RESOLVED BY TIE. "5.46" sits on l.68 below the EPS row (l.67). 5.46 / 3.76 = 1.4521, so +45.21%, which is the printed YoY (l.67). 5.46 is H1 FY27 EPS.
- R162 FOOTNOTE_UNRESOLVED (order pairing): RESOLVED BY SEQUENCE TIE. Left-column labels l.106-116 read Maharashtra, Hyderabad x4, Karnataka x3, New Delhi, Karnataka, Hyderabad. The 11 text blocks l.106-153 run in the same order (Maharashtra EPC; Hyderabad x4; Karnataka x3; New Delhi EPC; Karnataka EPC; Hyderabad). Labels and text pair one to one.
- R159 FOOTNOTE_UNRESOLVED (order book floor, no definition): UNRESOLVED in this document. See PR-04.
- R089-R099 UNNAMED_CUSTOMERS: confirmed. All 11 buyers are "company" or "EPC company". See PR-06 and FP-08.
- R125 UNQUANTIFIED_TARGET: confirmed at l.94. See PR-02.

Arithmetic ties (derived):
- Order sum: 13.50 + 13.50 + 39.90 + 51.30 + 23.30 + 28.50 + 5.70 + 5.70 + 5.60 + 8.64 + 13.60 = 209.24 = l.86, l.102.
- Margins: 23.62 / 135.57 = 17.42%; 13.65 / 135.57 = 10.07% (l.77). Both on Total Income, so other income is inside.
- YoY: 79.91%, 65.46%, 45.09% all fall inside the rounding range of the two-decimal figures (l.64-66).
- Implied share count: 13.65 / 5.46 = 2.500 Cr; 9.41 / 3.76 = 2.503 Cr. Flat. No dilution visible.
- Geography of H1 inflow: Hyderabad 141.60 (67.7%), Karnataka 48.54 (23.2%), Maharashtra 13.50, New Delhi 5.60. Ties FP-08.

## 2. FINDINGS TABLE

id | check | ledger row ref | line | short verbatim quote | classification | forward implication
---|---|---|---|---|---|---
PR-01 | F16 | R009-R013, R023, R024, R075-R077, R164 | l.64-66; l.77; l.170-171 | "EBITDA margin stood at 17.42%, while Net Profit margin was 10.07%" | FORWARD-SIGNAL | The release gives no H1 FY26 margin (18.94% and 12.49% derived; FP-16). Derived H2 FY26 from this document alone (FY26 minus H1 FY26; FY26 is printed as "Revenue", mixed basis per R164): income 106.28, EBITDA 19.02 (17.90%), NP 11.03 (10.38%). On the deck's FY26 total income of 182.10 the H2 EBITDA margin is 17.82%. EBITDA margin runs 18.94% to 17.90% to 17.42% over three halves; NP margin 12.49% to 10.38% to 10.07%. Half on half, income grew 27.6%, EBITDA 24.2% and NP 23.8%. The "Power-Packed" headline (l.54) rests on the YoY base. Sequentially, profit still grows slower than income. Observable: H2 FY27 EBITDA margin vs 17.42%. Extends FP-03.
PR-02 | F6 | R125, R126 | l.94-95 | "we continue to progress in line with our targets for the year" | FORWARD-SIGNAL | No FY27 number appears. Spear fact 1 says the earlier press release carried Rs 275-300 Cr and the 17-Aug-2026 call said 250-300. The earlier release is not an input here, so the drop is Spear-reported, not verified. H2 needs 139.69-164.69 Cr of revenue (FN Section 5), which is +31% to +55% on H2 FY26. Record: FY26 guided 225, 200, 190 vs 181.64 actual; Q1 FY27 50-60 vs 48.23. An unquantified "in line" claim after two misses cannot be tested. A4: restate the number and its basis (revenue or total income) on record. Deck equivalent FP-13.
PR-03 | F6 | R028, R033-R069, R127-R138 | l.103; l.106-153 | "Orders to be Executed Over 7-17 Months" | AMBIGUOUS | Derived tenor split of the 209.24 Cr H1 inflow: orders at 12 months or less = 94.74 Cr (orders 1, 2, 6-11); orders at 13 months or more = 114.50 Cr (order 3 39.90 "over 13-17 months", order 4 51.30 "within 13", order 5 23.30 "within 13"). Award dates are not given. Even an award on 1-Apr-2026 plus 13 months lands in FY28 [INFERENCE]. If dispatch comes at term end, at most 94.74 Cr of H1 inflow can bill in FY27, so the H2 need of 139.69-164.69 Cr rests mainly on the opening book. If "within" means staggered dispatch, more bills in FY27. The three long orders are all Hyderabad (2 named as "company", 1 "EPC company"). A4: share of 565.80 scheduled for dispatch by 31-Mar-2027.
PR-04 | F16 | R018, R029, R148, R159 | l.70; l.88 | "Current order book stands at over 565.80Cr as on 21st October, 2026" | AMBIGUOUS | The release drops the deck's "Consolidated" label and the Danya 83.04 Cr line (FP-07). It adds an "over" floor at l.70 that the CMD quote at l.88 omits ("stands at 565.80Cr"). Date is post period. GST basis, executed vs pending, and Danya inclusion are not stated. No 30-Sep-2026 book is given. R159 stays unresolved. A4: book at 31-Mar-2026 and 30-Sep-2026 on one stated basis.
PR-05 | F16 | R079, R101, R102, R156, R075-R077 | l.61; l.157-162; l.170 | "Key Consolidated Financial Highlights" | AMBIGUOUS | Every number is consolidated, yet Danya Electric is never named. The "About" text describes only the parent's 1994 firm and 2005 company. Danya is a partnership firm, 90% held, with the MD at 7.5% (FN Section 5 item 2, results l.1008-1010). A reader of the release alone cannot see a related-party firm inside the numbers. The deck at least names it (FP-14). A4: add to the Danya question set (FN-03, FN-05, FN-07).
PR-06 | F16 | R089-R099, R103, R105 | l.106-153; l.159-161 | "has emerged as a prominent supplier to local electric utilities" | AMBIGUOUS | None of the 11 H1 buyers is a utility. None sits in Tamil Nadu (home state, l.159) or Kerala (Kannur). Hyderabad is 67.7% of inflow. The boilerplate describes a customer base the H1 inflow does not show. Reading 1: stale boilerplate. Reading 2: a real shift to private and EPC buyers, with the fixed-price and concentration risk of FP-04 and FP-08. Ties FP-19 (government share rose in H1 revenue while H1 inflow is all non-utility).
PR-07 | F14 | R015, R018, R029, R164, R088, R157, R158, R165 | l.67-68; l.70 vs l.88; l.64 vs l.170; l.90 | "consolidated Revenue of  181.64 Cr" | NEUTRAL-FACT | (a) H1 is reported as Total Income (135.57, including 0.26 other income against revenue 135.31 per FP) while FY26 is reported as "Revenue" (181.64; total income 182.10 per FP-17c). The guidance base is ambiguous. (b) Order book "over 565.80Cr" (l.70) vs "565.80Cr" (l.88). (c) EPS value on the wrong line (resolved). (d) "newly inaugurated Kannur facility" carries no date. (e) Rupee glyph lost three times (text-layer issue, not drafting). Each is immaterial. Together they repeat the light-review pattern of FP-17 and FP-18.

Not repeated (cited): 330 kV orders vs "Up to 220 kV" capability (FP-06; release l.111, l.152 restates both). PVC 70-75% with falling margins (FP-04; release l.80). Margin attribution to raw materials only (FP-03; release l.79-83). Kannur utilisation not stated (FP-11, FP-13; release l.90-91). Warrants absent (FP-12). No half-year balance sheet or cash flow (FP-09).

## 3. CHECKLIST SCORECARD

check | status | basis
---|---|---
F1 | N.A. | Press release carries no statement template. Ledger ZERO_STANDING count is 0.
F2 | N.A. | Consolidated figures only (l.61). No standalone column. S-vs-C work is in FN-02 to FN-05 and FP-01.
F3 | N.A. | No cost lines in the release. Danya cost analysis in FN-06 and FP-02.
F4 | N.A. | No auditor report or Other Matters. "Unaudited" only (l.29, l.58). Unaudited Danya ratio in FN-07.
F5 | N.A. | No EoM or going concern paragraph. No prior release extract to diff.
F6 | FINDING | Lexicon hits: "expected to support" (l.91), "to be executed" (l.103, l.107), "will not be" (l.177, disclaimer only), plus 11 dated-by-tenor delivery commitments. Unquantified FY27 target (PR-02). Inflow tenor split (PR-03). Register in Section 4.
F7 | PASS | Only lexicon hit is "subject to certain risks and uncertainties" (l.175), generic safe-harbour text. "around 70-75%" (l.80) is covered in FP-04. No new hedge on lumpiness or concentration.
F8 | N.A. | No tax line in the release. ETR work in FN-11, FN-12 and FP (F8).
F9 | N.A. | No OCI. AS reporter (results F9).
F10 | PASS | EPS 5.46 vs 3.76, +45.21%, ties NP growth 45.09% within rounding. Implied shares 2.500 and 2.503 Cr, flat. No share count printed. Warrant omission recurs but is already FP-12.
F11 | N.A. | No net worth or reserves figure in the release.
F12 | N.A. | No segment data.
F13 | N.A. | No board outcome in the release. The cover letter (l.29-36) refers only to the results.
F14 | FINDING | Basis and drafting inconsistencies (PR-07).
F15 | N.A. | No consolidation list and no prior release. Danya's absence is a framing point, logged under F16 (PR-05).
F16 | FINDING | Margin comparators omitted and half trend down (PR-01). Order book basis dropped and floor added (PR-04). Danya not named (PR-05). Stale utility positioning (PR-06). FY27 number absent (PR-02, logged under F6).
F17 | N.A. | Not a concall. Spear coverage is in Section 5 for A4.

## 4. COMMITMENT REGISTER (F6)

commitment | implied date | ref | status word
---|---|---|---
FY27 "in line with our targets for the year", no number | 31-Mar-2027 | l.94 | underway
Kannur ramp: "production and capacity utilisation scaling up as planned"; plan not stated | undated | l.90-91 | underway
Added capacity "expected to support execution of our growing order book" and "larger and higher-capacity transformer opportunities" | undated | l.91-92 | initiated
Margin levers: "procurement efficiency, better product mix and operating leverage as volumes scale up" | undated | l.82-83 | initiated
565.80 Cr book gives "healthy revenue visibility for the coming quarters" | coming quarters | l.88 | underway
Order 1: 13.50 Cr, Maharashtra EPC, 20 MVA, "within 7 months" | award + 7 months (award date NOT DISCLOSED) | l.106-108 | initiated
Order 2: 13.50 Cr, Hyderabad, 112.5 MVA 330 kV, "11-month" | award + 11 months | l.110-112 | initiated
Order 3: 39.90 Cr, Hyderabad EPC, 20 MVA, "over 13-17 months" | award + 13-17 months; latest Feb-2028 | l.114-117 | initiated
Order 4: 51.30 Cr, Hyderabad, 20 MVA, "within 13 months" | award + 13 months | l.119-122 | initiated
Order 5: 23.30 Cr, Hyderabad, 160 MVA 220 kV, "within 13 months" | award + 13 months | l.124-126 | initiated
Order 6: 28.50 Cr, Karnataka EPC, 20 MVA, "8-month" | award + 8 months | l.128-131 | initiated
Order 7: 5.70 Cr, Karnataka, 20 MVA, "within 12 months" | award + 12 months | l.133-136 | initiated
Order 8: 5.70 Cr, Karnataka, 20 MVA, "12-month" | award + 12 months | l.138-140 | initiated
Order 9: 5.60 Cr, New Delhi EPC, 20 MVA 66/11 kV, "within 11 months" | award + 11 months | l.142-145 | initiated
Order 10: 8.64 Cr, Karnataka EPC, 20 MVA, "within 11 months" | award + 11 months | l.147-149 | initiated
Order 11: 13.60 Cr, Hyderabad, 112.5 MVA 330 kV, "11-month" | award + 11 months | l.151-153 | initiated

## 5. SPEAR LOAD-BEARING FACTS: WHAT THIS RELEASE SAYS

1. FY27 guide: no number (l.94). See PR-02.
2. Danya Electric: not named anywhere (PR-05). Legal form, inter-company sales and minority share: NOT DISCLOSED in this document.
3. CFO vs capex, borrowings, inventory, payables: NOT DISCLOSED (no balance sheet or cash flow). See FP-09 and FN Section 5.
4. Revenue vs PAT: H1 total income +79.91% vs NP +45.09% (l.64-66); half on half +27.6% vs +23.8% (PR-01). Kannur utilisation: NOT DISCLOSED (l.90-91); Spear's 20-25% is not restated.

## 6. FLAGGED FOR A4

FORWARD-SIGNAL: PR-01, PR-02. AMBIGUOUS: PR-03, PR-04, PR-05, PR-06. Separating observations: H2 FY27 EBITDA margin vs 17.42%; the FY27 number and its basis; the share of 565.80 Cr due for dispatch by 31-Mar-2027; the 30-Sep-2026 book on a stated basis with Danya split out; the count of utility customers in the book.

```yaml
stage: A3-forensics
company: "SUPREMEPWR"
quarter: "h1fy27"
doctype: "pressrelease"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/supremepwr-h1fy27/work/forensics_pressrelease_supremepwr_h1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: PASS
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "PR-01", check: "F16", line: "l.64-66; l.77; l.170-171", classification: "FORWARD-SIGNAL", implication: "H1FY26 margins omitted; derived EBITDA margin 18.94 -> 17.90 (H2FY26) -> 17.42%, NP 12.49 -> 10.38 -> 10.07%; HoH income +27.6% vs NP +23.8%; headline rests on YoY base"}
  - {id: "PR-02", check: "F6", line: "l.94-95", classification: "FORWARD-SIGNAL", implication: "FY27 'in line with our targets' with no number; Spear says earlier release carried 275-300 (not verified here); H2 needs 139.69-164.69 Cr after FY26 and Q1 misses"}
  - {id: "PR-03", check: "F6", line: "l.103; l.106-153", classification: "AMBIGUOUS", implication: "H1 inflow 94.74 Cr at <=12 months vs 114.50 Cr at >=13 months (all Hyderabad); award dates undisclosed; long orders likely bill in FY28 if dispatch at term end, so FY27 H2 rests on opening book"}
  - {id: "PR-04", check: "F16", line: "l.70; l.88", classification: "AMBIGUOUS", implication: "Order book 'over 565.80Cr' drops deck's Consolidated label and Danya 83.04 line; post-period date; GST/executed/Danya basis unstated (FP-07)"}
  - {id: "PR-05", check: "F16", line: "l.61; l.157-162; l.170", classification: "AMBIGUOUS", implication: "Consolidated numbers with Danya (90% partnership firm, MD 7.5%) never named; related-party structure invisible to release reader (FP-14)"}
  - {id: "PR-06", check: "F16", line: "l.106-153; l.159-161", classification: "AMBIGUOUS", implication: "'prominent supplier to local electric utilities' vs zero utility, zero Tamil Nadu/Kerala buyers in 11 H1 orders; Hyderabad 67.7% of inflow (FP-08, FP-19)"}
  - {id: "PR-07", check: "F14", line: "l.67-68; l.70 vs l.88; l.64 vs l.170; l.90", classification: "NEUTRAL-FACT", implication: "H1 on Total Income vs FY26 on Revenue (guidance base ambiguous); order book 'over' vs exact; EPS layout offset; Kannur inauguration undated"}
forward_signals: ["PR-01", "PR-02"]
ambiguous: ["PR-03", "PR-04", "PR-05", "PR-06"]
commitments:
  - {commitment: "FY27 progress 'in line with our targets for the year', unquantified", implied_date: "31-Mar-2027", ref: "l.94", status_word: "underway"}
  - {commitment: "Kannur ramp, utilisation 'scaling up as planned'; plan not stated", implied_date: "undated", ref: "l.90-91", status_word: "underway"}
  - {commitment: "Added capacity to support order book and larger-rating opportunities", implied_date: "undated", ref: "l.91-92", status_word: "initiated"}
  - {commitment: "Margin levers: procurement, product mix, operating leverage", implied_date: "undated", ref: "l.82-83", status_word: "initiated"}
  - {commitment: "565.80 Cr book gives revenue visibility for coming quarters", implied_date: "coming quarters", ref: "l.88", status_word: "underway"}
  - {commitment: "11 H1 orders, 209.24 Cr, execution 7-17 months (per-order register in report Section 4)", implied_date: "award + 7 to 17 months; award dates NOT DISCLOSED; latest Feb-2028", ref: "l.103; l.106-153", status_word: "initiated"}
gate_a3: pass
blank_checks: []
analyst_note: "The release restates the deck; most issues are already FP or FN findings and are cited. Two new derived points matter. First, the half trend (PR-01): FY26 minus H1 FY26 gives an H2 FY26 EBITDA margin of about 17.9%, so margins fell for a third straight half. The 45% YoY profit headline hides a sequential pattern where profit still lags income. Second, the inflow tenor (PR-03): 114.50 Cr of the 209.24 Cr H1 inflow carries 13 months or more, so it likely bills in FY28. That puts the H2 FY27 need of 139.69-164.69 Cr mostly on the opening book, whose size and basis are not stated (PR-04, FP-07). Read together with the unquantified 'in line with targets' claim (PR-02) and the FY26 and Q1 misses, the conservative reading is guidance risk for FY27. R162 is resolved: labels and order texts pair in sequence. R159 stays open."
```
