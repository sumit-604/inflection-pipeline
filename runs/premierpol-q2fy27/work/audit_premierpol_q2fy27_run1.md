# A5 ADVERSARY / COMPLETENESS AUDIT: PREMIER POLYFILM LIMITED (PREMIERPOL), Q2 FY27

Agent: A5 adversary, claude-opus-5-5. Audit date: 2026-10-17.
Inputs read: A4 review (runs/premierpol-q2fy27/work/review_premierpol_q2fy27.md, 575 lines), A1 fulltext (extracted/premierpol-results-q2fy27-fulltext.md, body L1 to L522), A1 structured file (R001 to R401), A2 ledger. The source PDF, inputs/ and A3 were not opened.
Anchor convention: "L###" = A1 fulltext body line. "rev L###" = A4 review file line. "R###" = A1 structured row. All money in Rs lakhs unless marked Cr (1 Cr = 100 lakhs).

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Heading (rev line) | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | rev L459 | 13 lines (rev L460 to L472); within the 10 to 20 line band (Quarterly Results protocol, not the Document Review Protocol) | present |
| 2. Sector intelligence | rev L474 | 6 bullets; tiered FILED / INFERENCE / PENDING LIVE VERIFICATION | present |
| 3. Business-model intelligence | rev L482 | 6 bullets; unit economics, cost structure, model drift with two readings | present |
| 4. Competition intelligence | rev L490 | 5 bullets; peer set tagged INFERENCE, strengths and weaknesses anchored | present |
| 5. Forward map | rev L497 | Make-or-break line plus 7 catalysts, each with a bull and a bear fork; six dated, one undated (M4, rev L502; STYLE S-7) | present |

Gate result: PASS. All five parts present and non-empty.

---

## 1. COVERAGE AUDIT

Method: a fresh line-by-line pass over the A1 fulltext (L1 to L522), then a grep of the structured file for each fulltext line that carries a token or a template label. The result was diffed against the A2 ledger and A2 count test. Every ledger row was then checked for a citation or an explicit disposition in A4.

| Category | A2 count | A5 fresh count | Orphan rows (ledger, absent from A4) | Status |
|---|---|---|---|---|
| Notes | 5 (+1 unnumbered R384) | 5 (+1): L152, L153-L154, L155-L156, L157, L158; unnumbered L165 | none | PASS |
| Line items (financial tables) | 96 lines / 310 cells | 105 token-bearing lines / 337 cells | none | FAIL, A2 (A5-M1) |
| Zero-standing cells | 23 cells | 49 cells, plus 1 unexplained numeric token ("2", L96) | none | FAIL, A2 (A5-M1) |
| Qualifiers (incl. blank-in-source rows) | 40 | 42 (adds L94 Exceptional Items, L128 Details of debt securities; both blank rows) | none | FAIL, A2 (A5-M1) |
| Agenda items | 1 | 1 (L25 to L30: standalone unaudited results only) | none | PASS |
| Auditor paragraphs | 5 | 5: title L428 (para 1 scope L451 merged into R396 "title/scope"), para 2 L461, para 3 L477, conclusion fragment L490 to L502, garble marker R400 | none | PASS |
| Entities | 23 | 23 (L2, L3, L15 x2, L21, L32, L49, L61, L62 x4, L152 x2, L153 x2, L155, L172, L415, L442, L466, L480, L483) | none | PASS |
| Dates | 19 | 19 (L10, L18, L25, L28, L35, L71 x4, L152, L172, L179, L182, L307, L312, L315, L408, L435, L516) | none | PASS |
| Footnote markers unresolved | 4 | 4 (L37, L95, L131, L521). L160 "Vl" and L166 "D" are signature-area OCR noise, not footnote markers | none | PASS |
| Identifiers / meeting times | 9 | 9 (L5, L6, L21, L35 x2, L67, L174, L513, L515) | R312, R314 (CIN_OCR_MISMATCH), R316 (UDIN_UNRESOLVED) | FAIL, A3 (A5-M2) |
| FORWARD statements | 0 | 0. Grep for acqui, stake, merger, expect, outlook, guidance, propos, expan, capacity, plan, "will be" returns only blank CF template labels (L237, L239, L278) | none | PASS |
| Turns / questions / slides | 0 | 0 (results filing only; no concall, no deck) | none | PASS |
| Structured IDs referenced in ledger | 401 of 401 | 401 of 401 (R001-R310 by line-item ranges, R311-R319 s3, R320-R342 s7, R343-R361 s9, R362-R401 s10; all 40 qualifiers checked by ID) | none | PASS |

### 1A. Fresh-pass units missing from the structured file and the ledger (A5-M1, MISSING, loop A2)

Grep of the structured file for these line anchors returns no rows. The only exception is L98, which has two of its three tokens captured (R097, R098).

| Fulltext line | Label | Tokens as read | Cells | Note |
|---|---|---|---|---|
| L86 | (g) Other Expenses (header row) | "-", "-" | 2 | nil header cells |
| L94 | Exceptional Items | none (blank row) | 0 | A4 relies on this blank row at rev L57, L92, L175, L198 by reading the fulltext; the ledger has no row for it |
| L96 | 6 Tax Expenses (header row) | "2", "-" | 2 | "2" is an unexplained numeric token. It enters no total, because current tax equals total tax in every interim column (L97 vs L99: 330/330, 306/306, 299/299, 636/636, 523/523) and FY26 casts (1,079 + 13 = 1,092). It reads as OCR of a dash (L86 shows "-" in the same pattern) |
| L98 | Deferred Tax | "0", "-", "13" | 1 extra | A1 captured "0" (R097) and "13" (R098) only; the "-" cell is uncaptured |
| L104 | Tax Expenses of discontinued Operations | "-" x5 | 5 | template nil line; L103 (R111-R116) was captured, L104 to L106 were not |
| L105 | Net Profit/(Loss) from discontinued Operations after tax | "-", "-", "-", "f", "“", "=" | 6 | nil, OCR glyphs |
| L106 | Share of Profit/(Loss) of associates and JVs | "-", "S", "a", "z", "a" | 5 | nil, OCR glyphs; corroborates Note 5 (L158) |
| L128 | Details of debt securities | none (blank row) | 0 | bears on F-01: no listed debt securities |
| L373 | TOTAL NON CURRENT FINANCIAL LIABILITIES | ".", "‘i" | 2 | nil subtotal; bears on F-01: any debt is not on a non-current financial line |
| L377 | Deferred government grants non current | "_" | 1 | nil |
| L390 | Deferred government grants, current | "us", "=" | 2 | nil, OCR glyphs |
| L393 | Liabilities in disposal group held for sale | "“" | 1 | nil |

Fresh totals: line items 96 + 9 = 105 (L86, L96, L104, L105, L106, L373, L377, L390, L393); cells 310 + 27 = 337; zero-standing cells 23 + 26 = 49; qualifiers or blank rows 40 + 2 = 42 (L94, L128). A2's YAML reports `missing_from_structured: []`, which is wrong. No A4 number changes. L94, L128 and L373 are evidence the ledger should carry.

### 1B. Orphan rows (A5-M2, MISSING, loop A3)

A4's preamble says "Ledger IDs 401 of 401 referenced ... No ledger row is unreviewed" (rev L15). A5 accepts that blanket mark for unflagged rows. Rows that carry a named A2 flag (ledger s11 "Flags raised", A2 YAML flags_raised) need their own disposition. A4 disposes ZERO_STANDING (rev L15, L92), FOOTNOTE_UNRESOLVED (F-13, rev L435), OCR_UNREADABLE R046 (rev L87), PERIOD_COLUMN_UNRESOLVED (rev L211) and OCR_AMBIGUOUS R289 (F-10, rev L18). A grep of the review for "CIN" and "UDIN" returns no match. Two flags are therefore undisposed:
- R312 / R314, CIN_OCR_MISMATCH (L5 "L52109DL1992PLC049590" vs L67 "152109DL1992PLC049590"). This reads as OCR of "L" as "1". A "reviewed, no finding" line closes it.
- R316, UDIN_UNRESOLVED (L515, garbled). The UDIN is the identifier that authenticates the limited review report. With paragraphs 3 to 4 garbled (R400) and the UDIN unreadable, this copy cannot be authenticated. It belongs with the F-03 AMBER flag, Q14 and M2.

### 1C. Existing label conflict, already incorporated (no new finding)

A1 assigns the CF values on L194 and L196 to the labels above them (R195-R198). On that assignment the H1 current-receivable change is an increase of 3, while the balance sheet shows a fall of 162 (4,126 to 3,964, L342). A4 surfaces this as A4-04 (rev L238), keeps the conservative F-11 reading and routes an image re-read to A1 (M1, rev L406). This is adequate.

---

## 2. ARITHMETIC AUDIT

Every derived metric was recomputed from the raw lakh cells. Recomputed values are exact (lakh) or shown to three decimals.

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| P&L casts, six columns (Total income, Total expenses, PBT, tax, PAT, TCI) | tie | tie. Q2 FY27: 11,506 + 112 = 11,618; 6,843 + 217 - 78 + 888 + 24 + 118 + 2,295 = 10,307; 1,311; 981; 763. Q1 FY27 8,851 / 1,214 / 908 / 1,292. Q2 FY26 7,313 / 1,100 / 801 / 656. H1 FY27 19,158 / 2,525 / 1,889 / 2,055. H1 FY26 13,986 / 1,924 / 1,401 / 1,413. FY26 29,846 / 4,280 / 3,188 / 3,091 | L75 to L110 | PASS |
| H1 FY27 finance cost (OCR "At", R046) | 44 | 19,158 - (11,804 + 921 + 65 + 1,708 + 236 + 4,380) = 44; also 20 + 24 = 44 | L84, L92 | PASS |
| Net revenue, GST-net (Q2 FY26 / Q1 FY27 / Q2 FY27 / H1 FY26 / H1 FY27 / FY26) | 72.64 / 87.33 / 101.43 / 137.20 / 188.76 / 296.58 Cr | 7,264 / 8,733 / 10,143 / 13,720 / 18,876 / 29,658 | L75 less L87 | PASS |
| Material cost | 45.55 / 58.08 / 69.82 / 86.07 / 127.90 / 186.22 | 4,555 / 5,808 / 6,982 / 8,607 / 12,790 / 18,622 | L80 + L81 + L82 | PASS |
| Gross margin, net revenue | 37.29 / 33.49 / 31.16 / 37.27 / 32.24 / 37.21% | 37.293 / 33.494 / 31.164 / 37.267 / 32.242 / 37.211% | derived | PASS |
| Operating EBITDA (PBT + D + FC - OI) | 11.33 / 12.93 / 13.41 / 20.45 / 26.34 / 45.94 | 1,133 / 1,293 / 1,341 / 2,045 / 2,634 / 4,594 | L95, L85, L84, L76 | PASS |
| Op EBITDA margin, net revenue | 15.60 / 14.81 / 13.22 / 14.91 / 13.95 / 15.49% | 15.598 / 14.806 / 13.221 / 14.905 / 13.954 / 15.490% | derived | PASS |
| Op EBITDA margin, reported revenue | 13.62 / 12.92 / 11.65 / 12.98 / 12.24 / 13.56% | 13.623 / 12.922 / 11.655 / 12.975 / 12.244 / 13.556% | derived | PASS |
| Reported EBITDA; margin on net revenue | 12.29 / 13.52 / 14.53 / 21.94 / 28.05 / 48.30; 16.92 / 15.48 / 14.33 / 15.99 / 14.86 / 16.29% | 1,229 / 1,352 / 1,453 / 2,194 / 2,805 / 4,830; 16.919 / 15.481 / 14.325 / 15.991 / 14.860 / 16.286% | derived | PASS |
| Core PBT (PBT - OI) | 10.04 / 11.55 / 11.99 / 17.75 / 23.54 / 40.44 | 1,004 / 1,155 / 1,199 / 1,775 / 2,354 / 4,044 | L95 less L76 | PASS |
| OI / PBT | 8.73 / 4.86 / 8.54 / 7.74 / 6.77 / 5.51% | 8.727 / 4.860 / 8.543 / 7.744 / 6.772 / 5.514% | derived | PASS |
| Effective tax rate | 27.18 / 25.21 / 25.17 / 27.18 / 25.19 / 25.51% | 27.182 / 25.206 / 25.172 / 27.183 / 25.188 / 25.514% | L99 / L95 | PASS |
| PAT margin, net / reported revenue | 11.03 / 10.40 / 9.67 / 10.21 / 10.01 / 10.75%; 9.63 / 9.07 / 8.53 / 8.89 / 8.78 / 9.41% | 11.027 / 10.397 / 9.672 / 10.211 / 10.007 / 10.749%; 9.631 / 9.075 / 8.526 / 8.889 / 8.781 / 9.407% | L108 | PASS |
| GST / reported revenue | 12.66 / 12.72 / 11.85 / 12.95 / 12.25 / 12.49% | 12.661 / 12.722 / 11.846 / 12.950 / 12.254 / 12.487% | L87 / L75 | PASS |
| A3 F-09 basis check (Rep EBITDA / GST-net total income) | 14.2% vs 16.7% | 1,453 / 10,255 = 14.169%; 1,229 / 7,360 = 16.698% | L77, L87 | PASS |
| Q2 YoY set | net rev +39.63%; reported +38.34%; GM -613 bps; Op EBITDA +18.36%; margin -238 bps; D&A +1.72%; FC +84.62%; EBIT +20.26%; OI +16.67%; core PBT +19.42%; PBT +19.18%; PAT +22.47%; EPS +23.68% | +39.634%; +38.343%; -612.9 bps; +18.358%; -237.7 bps; +1.724%; +84.615%; +20.256% (1,017 to 1,223); +16.667%; +19.422%; +19.182%; +22.472%; +23.684% | derived | PASS |
| H1 YoY set | net rev +37.58%; Op EBITDA +28.80%; margin -96 bps; core PBT +32.62%; PBT +31.24%; PAT +34.83%; EPS +34.33% | +37.580%; +28.802%; -95.1 bps; +32.620%; +31.237%; +34.832%; +34.328% | derived | PASS (margin bps is a rounding artefact, S-1) |
| Opex ratio (employee + other excl. GST / net revenue) | 21.70% to 17.94%, +376 bps | 21.696% to 17.943%, +375.3 bps (and -612.9 + 375.3 = -237.7 ties to the margin change) | L83, L88 | PASS (rounding, S-2) |
| Q1 to Q2 FY27 Op EBITDA margin | -159 bps | -158.5 bps | derived | PASS |
| ETR effect on Q2 PAT | +0.26 Cr | 1,311 x (0.271818 - 0.251716) = 26.35 | L95, L99 | PASS |
| QoQ table (Q1 FY26 and H2 FY26 derived) | Q1 FY26 64.56 / 37.24% / 14.13% / 7.71; H2 FY26 159.38 (79.69 avg) / 37.16% / 15.99% / 22.69 (11.35 avg); +12.52%, +9.71%, +9.59%, +16.15%; core PBT QoQ +3.81% | Q1 FY26: 6,456; 2,404 / 6,456 = 37.237%; 912 / 6,456 = 14.126%; 771. H2 FY26: 15,938; 5,923 / 15,938 = 37.163%; 2,549 / 15,938 = 15.993%; 2,269. Growth +12.516%, +9.705%, +9.587%, +16.146%; +3.810% | H1 FY26 less Q2 FY26; FY26 less H1 FY26 | PASS |
| PAT bridge Q2 YoY | +1,074 / -622 / -113 / -131 / (208) / -2 / -11 / +16 / (211) / -57 / +26 = 180 | 2,879 x 0.372935 = 1,073.7; 10,143 x (-0.061291) = -621.7; gross profit check 3,161 - 2,709 = 452; tax check 57 - 26 = 31 = 330 - 299 | L80 to L99 | PASS |
| Recurring split; PAT ex OI and ETR | 78.9% / 6.5% / 14.4%; 9.43 Cr, +17.73% | 142.0 / 11.65 / 26.35 lakh = 78.9 / 6.5 / 14.6%; (1,311 - 16) x 0.728182 = 943.0; +17.73% | derived | PASS (14.4% uses rounded 26, S-3) |
| CFO cast (H1 FY27) and FY26 CFO derived | 1,322; 2,670 | 2,525 - 726 = 1,799; - 477 = 1,322; 1,322 - 957 - 179 = 186; 504 + 186 = 690 = L343. FY26: -581 + 2,759 + 492 = 2,670; 1,085 - 581 = 504 | L189 to L298 | PASS |
| CFO / PAT | 0.70x H1 FY27; 0.84x FY26 | 0.6998x; 0.8375x | L231, L108 | PASS |
| FCF | 17.75 FY26; 7.41 H1; 2.86 (Reading A) | 2,670 - 895 = 1,775; 1,322 - 581 = 741; 741 - 455 = 286 | L245, L271 | PASS |
| Trade WC (inv + rec - pay) | 70.79 to 71.06 Cr | 5,027 + 4,126 - 2,074 = 7,079; 5,029 + 3,964 - 1,887 = 7,106 | L339, L342, L383 | PASS |
| Days (rec / inv / pay / CCC) | FY26 44.44 / 98.53 / 40.65 / 102.32; H1 33.72 / 71.96 / 27.00 / 78.68; rec on net 50.78 / 38.43 | 44.437 / 98.532 / 40.651 / 102.32; 33.721 / 71.955 / 26.999 / 78.68; 50.779 / 38.430 | L339, L342, L383, L75, L80-L82 | PASS (basis issue, see AR-3) |
| Net cash, BS basis | 16.68 to 19.36 Cr | 504 + 1,164 = 1,668; 690 + 1,246 = 1,936 | L341, L343 | PASS |
| D/E-implied debt and net debt | 18.40-19.87 / 17.61-19.29; net debt 1.72-3.19 / (0.07)-(1.75) | 0.125-0.135 x 14,720; 0.105-0.115 x 16,775; less 1,668 / 1,936 | L147, L364 | PASS |
| ROCE | H1 32.63% / 29.15%; FY26 32.90% | (2,525 + 44) x 2 / 15,747.5 = 32.627%; / (15,747.5 + 1,879.4) = 29.149%; (4,280 + 81) / 13,253.5 = 32.905% (opening 10,728 + 1,059) | L95, L84, L364, L130, L126 | PASS |
| Trailing four quarters; annualised Q2 PAT | PAT 36.76; net rev 348.14; EPS 3.50; 39.24 | 3,188 - 1,401 + 1,889 = 3,676; 29,658 - 13,720 + 18,876 = 34,814; 3.04 - 1.34 + 1.80; 981 x 4 | L102, L139 | PASS |
| EPS share-basis anomaly | 981 / 1,059 = 0.926 vs 0.94; implied about 1,044 (band 1,038 to 1,049) | 0.9263; 1,043.6; band 1,038.1 to 1,049.2. Cross-column intersection of all six EPS bands is 1,047.1 to 1,049.2 | L102, L126, L139 | PASS (precision, S-4) |
| Capitalisation bridge | X = 234; 234 + 347 = 581 | 6,009 - 6,011 + 236 = 234; 397 - 50 = 347; sum 581 = L245 | L320, L321, L85, L245 | PASS |
| Reading B sum | 82 + 92 + 400 = 574 | arithmetic ties | L330, L341, L346 | PASS on arithmetic; allocation conflict at A5-C1 |
| BS casts with the four F-10 cells | cells excluded; Q15 bull answer 142 / 130 / 232 / 628 | DTA = 8,437 - 6,407 - 1,309 - 579 = 142; other NCFA = 1,309 - 1,077 = 232; NCL = 5,502 - 4,874 = 628; DTL = 628 - 498 = 130. All 31-03-2026 casts tie. L329 subtotal 6,407 = 6,009 + 397 + 1 (PPE + CWIP + intangibles) | L329 to L398 | PASS (A4 exclusion correct) |
| Other Equity movement | H1 +2,055 = TCI; FY26 non-TCI reduction 158 | 15,716 - 13,661 = 2,055 = L110 H1; 10,728 + 3,091 - 13,661 = 158 | L361, L110, L130 | PASS |
| GST share, Q1 FY26 and H2 FY26 | 13.27%; 12.09% | 988 / 7,444 = 13.272%; 2,191 / 18,129 = 12.086% | L75, L87 | PASS |
| Material cost / net revenue | 68.84% vs 62.71% | 68.836% vs 62.707% | derived | PASS |
| Treasury share of OI line; alt reading | 45.6%; +93 | 78 / 171 = 45.61%; 171 - 78 = 93 | L268, L269, L76 | PASS |
| Finance-cost add-back gap | 12 H1; FY26 57 vs 81 | 44 - 32 = 12; 81 - 57 = 24 | L191, L84 | PASS |

Arithmetic result: no mismatch above rounding. Three rounding-level items are logged as STYLE (S-1, S-2, S-3).

---

## 3. ADVERSARIAL READ

### AR-1. Claim: revenue growth is real and the cost base is fixed
A4 text: "Revenue growth is not in doubt; unit margin is." (rev L360). "Strong growth" (rev L133). "The headline growth is real at the operating level." (rev L152). "Fixed costs are light ... That operating leverage absorbed about 376 bps of the 613 bps gross-margin loss." (rev L485, also L151).

Strongest bear counter, from the same extract:
- The filing gives revenue in value only. Volume and realisation are not disclosed; A4 itself says so (rev L480).
- Gross profit rose 16.69% (2,709 to 3,161; L75, L80-L82, L87) against net revenue +39.63%. Material cost rose 53.28% (4,555 to 6,982).
- Conversion costs (employee plus other expenses excl. GST) rose 15.48% (1,576 to 1,820; L83, L88). Employee cost +14.58% (775 to 888), other expenses +16.35% (801 to 932).
- If conversion costs move with volume, volume grew near 15%, and price or mix carried the rest of the 39.63%. Revenue carried by resin pass-through reverses when resin falls. The 375 bps opex-ratio gain then reverses too, because it came from a larger denominator, not from fixed-cost leverage [INFERENCE].
- The quarterly cost pattern points both ways. Other expenses rose 14.78% QoQ (812 to 932, L88) against net revenue +16.15%, a near-proportional move. From Q2 FY26 to Q1 FY27 they rose only 1.37% (801 to 812) against +20.22%. The extract cannot tell fixed cost from variable cost.

Survives: YES. A4 names two margin readings (resin lag; mix or price cuts, rev L487). It does not name the third: price-led revenue on modest volume, where the operating leverage is inflation in the denominator. Graft into Step 2 diagnostic 2 (rev L151), Step 8C (rev L360) and Business-Model bullet 3 (rev L485). State gross profit +16.69% beside revenue +39.63%. Add the separating observation: a volume or realisation figure (add it to the IR email), or the Q3 FY27 opex ratio if revenue moves with resin. Finding A5-M3, MISSING, loop A4.

### AR-2. Claim: margin was steady for four quarters, then broke
A4 text: "Gross margin held near 37.2% for four quarters, then fell to 33.49% in Q1 FY27 and to 31.16% in Q2 FY27 [FILED, derived]." (rev L464). The same claim appears at rev L174, L334, L453 and L561. A steady run followed by a sudden break is the pattern that best fits the bull reading: resin cost rose, pass-through lags, margin recovers (rev L360, L487).

Strongest bear counter, from the same extract:
- Only three FY26 margin points can be derived. Q1 FY26 is 37.24% (H1 FY26 less Q2 FY26). Q2 FY26 is 37.29%. H2 FY26 combined is 37.16% (FY26 less H1 FY26). Anchors: L75, L80-L82, L87.
- Q3 FY26 and Q4 FY26 are not filed separately. A4's own Step 3 table marks them ND (rev L165, L166).
- An H2 average of 37.16% fits a steady Q3 and Q4. It equally fits a strong Q3 followed by a Q4 already below 37%. The extract cannot tell these apart.
- If the fall began in Q4 FY26, it has run for three quarters, not two. That weighs against a short pass-through lag and toward the mix or price reading [INFERENCE].

Survives: YES. "Four quarters" is stated as FILED, derived, and the extract does not support it. Finding A5-F1, FACTUAL, loop A4. Fix at all five lines: "Gross margin was 37.24% in Q1 FY26, 37.29% in Q2 FY26 and 37.16% across H2 FY26 combined (Q3 and Q4 not filed separately), then 33.49% in Q1 FY27 and 31.16% in Q2 FY27." Add one line: the H2 average cannot exclude a Q4 FY26 decline.

### AR-3. Claim: working capital is tight and the balance sheet is strong
A4 text: "Trade WC is not the drag ... receivable and inventory days improved." (rev L242). CCC "-23.64 days ... Improved on mixed bases" (rev L224). "Trade working capital is tight" (rev L488). "low debt on any reading, ROCE above 29% on any reading" (rev L492).

Strongest bear counters, from the same extract:
- (a) Days basis. A4 divides the 31-03-2026 balances by full-year FY26 flows, and the 30-09-2026 balances by H1 FY27 flows. Revenue rose through FY26, so the full-year denominator understates the year-end run-rate. On H2 FY26 flows (182 days): receivable days 41.42 (4,126 / 18,129 x 182), inventory days 91.35 (5,027 / 10,015 x 182), payable days 37.69 (2,074 / 10,015 x 182), CCC 95.08. Against H1 FY27 at 78.68, the like-for-like gain is 16.40 days, not 23.64. The direction holds. The size is about 30% smaller. Survives.
- (b) Substance. A4's own bull answer to Q5 calls the other-current-asset rise "GST input credit or advances to resin suppliers" (rev L377). Both are trade working capital in substance. On that reading, trade WC plus other current assets rose from 78.14 Cr (7,079 + 735) to 84.31 Cr (7,106 + 1,325), +7.90%, while A4 reports trade WC as flat (+0.27 Cr). "Trade WC is not the drag" holds in form only. Survives. It links to A5-C1, which covers the allocation of the cash-flow drag.
- (c) ROCE and debt. The ROCE numerator includes the Other Operating Income line, which holds treasury income (rev L63). The denominator holds about 30 Cr of cash and investments. Strip both out. H1 FY27 operating EBIT is 2,398 (2,634 - 236), annualised 4,796, over average operating capital of 12,914.5 (equity less cash, current and non-current investments: 12,067 at 31-03-2026, 13,762 at 30-09-2026; L330, L341, L343, L364). That gives 37.14%, or 32.42% with D/E-implied debt added. On debt, D/E prints at most 0.13 (L147). "Details of debt securities" is blank (L128). Total non-current financial liabilities carry no value (L373). So any debt is small and short-term. Counter fails: the ROCE and low-debt claims stand on the extract.

Survives: (a) and (b) YES, (c) NO. Graft (a) and (b) into Step 5 (rev L224, L242) and Business-Model bullet 6 (rev L488). Finding A5-M4, MISSING, loop A4.

### Mandatory acquisition-economics probe
Not triggered. The filing describes no acquisition, purchase of a business or stake buy. The grep for acqui, stake, merger, amalgam and takeover returns only blank CF template labels (L237, L239, L278). The investing lines for obtaining control of subsidiaries (L233 to L235) carry no values. Note 5 says there is no subsidiary, associate or JV (L158). Non-current investments rose 92 (985 to 1,077, L330) and current investments rose 82 (1,164 to 1,246, L341). Their 174 combined rise sits near H1 FY27 OCI of +166 (L109). That pattern reads as fair-value marks, not a stake purchase [INFERENCE]. No consideration and no target earnings exist, so no price-to-earnings multiple can be stated.

---

## FINDINGS (typed)

| ID | Type | Agent | Finding | Lines |
|---|---|---|---|---|
| A5-F1 | FACTUAL | A4 | "Four steady quarters" of gross margin near 37.2% is not filed. Only Q1 FY26 (37.24%), Q2 FY26 (37.29%) and H2 FY26 combined (37.16%) can be derived; Q3 and Q4 FY26 are ND. Restate at all five lines and note that the H2 average cannot exclude a Q4 FY26 decline. | rev L174, L334, L453, L464, L561; L75, L80-L82, L87; rev L165-L166 |
| A5-C1 | CONTRADICTION | A4 | Other current financial assets +400 (1,186 to 1,586, L346) is used twice. Rev L242 places it in the CFO drag. Rev L236 places it in Reading B of the 455 investing outflow (L271). It cannot be in both. The review also never states that the CF other-current-assets adjustment of 1,084 (L197) exceeds the balance-sheet rise of 590 (735 to 1,325, L349) by 494, and Q5 (rev L377) presents the two numbers as one. Current plus non-current investments rose 174 (L330, L341) against H1 OCI of +166 (L109), so most of Reading B may be non-cash fair-value marks. Fix: state the 494 gap, allocate the +400 once, and carry the OCI reading. The conservative FCF of 2.86 Cr (Reading A) gains support, and the FCF range of 2.86 to 7.41 Cr stands. | rev L236, L242, L377; L197, L271, L330, L341, L346, L349, L109 |
| A5-M1 | MISSING | A2 | 12 fulltext lines are absent from the structured file and the ledger (table 1A): L86, L94, L96, L98 (third token), L104, L105, L106, L128, L373, L377, L390, L393. Total 27 cells and 2 blank rows. A2's `missing_from_structured: []` is wrong. Recount line_items (105), zero_standing (49) and qualifiers (42). No A4 number changes. | as listed |
| A5-M2 | MISSING | A3 | Orphan rows R312 and R314 (CIN_OCR_MISMATCH) and R316 (UDIN_UNRESOLVED) carry A2 flags with no disposition in A4. The unreadable UDIN (L515) means the review report cannot be authenticated from this copy. Tie it to F-03 AMBER, Q14 and M2. | L5, L67, L515; ledger s3, s11 |
| A5-M3 | MISSING | A4 | Surviving bear counter AR-1. Name the price-led third reading: gross profit +16.69% and conversion costs +15.48% against net revenue +39.63%, with volume ND. Name its separating observation. | rev L151, L360, L485, L487; L75, L80-L83, L87, L88 |
| A5-M4 | MISSING | A4 | Surviving bear counter AR-3 (a) and (b). The like-for-like CCC gain is 16.40 days (95.08 to 78.68), not 23.64. The supplier-advance substance means trade WC plus other current assets rose 78.14 to 84.31 Cr (+7.90%). | rev L224, L242, L377, L488; L339, L342, L349, L383 |

---

## VERDICT

**INCOMPLETE.**
- Loop back to: **A2** (earliest failing agent; the cascade then runs A3 and A4).
- A2 (MISSING, A5-M1): add the 12 missing fulltext lines and 27 cells. Correct `missing_from_structured`. Recount line items, zero-standing cells and qualifiers.
- A3 (MISSING, A5-M2): dispose orphan rows R312, R314 and R316.
- A4 (FACTUAL, A5-F1): restate the "four steady quarters" claim at rev L174, L334, L453, L464 and L561.
- A4 (CONTRADICTION, A5-C1): remove the double use of other current financial assets +400 (rev L236 vs L242). State the 1,084 vs 590 gap. Carry the investments +174 vs OCI +166 reading.
- A4 (MISSING, A5-M3, A5-M4): graft the surviving AR-1 and AR-3 counters.
- The protocol verdict PROCEED WITH FLAGS and all A4 numbers stand. The fixes change wording, one reading allocation and two grafts. They change no table value.

---

## STYLE NOTES (logged, no re-run)

- S-1. H1 Op EBITDA margin change shown as -96 bps (rev L147). The exact value is -95.1 bps (14.905% to 13.954%). A4 subtracted rounded percentages. Use -95 bps.
- S-2. The opex-ratio gain is shown as +376 bps (rev L151, L485). The exact value is +375.3 bps. Use +375 bps, so that -613 + 375 = -238 ties.
- S-3. The ETR share of the PAT change is 14.4% (rev L197, L202) on the rounded 26 lakh. Unrounded, 26.35 lakh gives 14.6%.
- S-4. Implied weighted shares are given as "about 1,044 lakh" (rev L43, L338, Q9 rev L381). The six EPS rounding bands intersect at 1,047.1 to 1,049.2 lakh, so about 1,048, or 10 to 12 lakh shares below 1,059. This sits inside A4's stated band.
- S-5. Rev L231 anchors equity 147.20 to "L147". L147 is the D/E ratio. Equity sits at L364 (14,720) and L364 (16,775).
- S-6. Rev L49, Note 2 row: "understate by about 12% of revenue" should read "understate by about 12% in relative terms (the GST share of reported revenue)".
- S-7. The forward-map entry for M4 (rev L502) is undated ("Next exchange filings"). Give a dated check, for example "check BSE/NSE announcements by the Q3 FY27 review, 14-02-2027".
- S-8. The A2 ledger zero-standing header says "23 cells, 13 line items" but lists 10 line items. The 13 holds only if the three blank-in-source rows (R373, R376, R388) are counted. Label it as such.
- S-9. A4 does not dispose R233 / R234 (LABEL_MISALIGNED_OCR, 6,407 / 6,062; in-table flag only, not in A2 s11). The row casts as PPE + CWIP + intangibles (6,009 + 397 + 1; 6,011 + 50 + 1). One disposition line closes it.
- S-10. R141-R146, reserves line. A2 suspected a column misread. A4 uses 10,728 as FY26 opening (rev L331) without stating the basis. The Q1 FY27 column's 13,661 equals the 31-03-2026 Other Equity (L361), so the line carries previous year-end reserves. That makes 10,728 the 31-03-2025 figure, and A4's use is correct. State the basis in one line.

---

```yaml
stage: A5-adversary
company: "PREMIERPOL"
quarter: "Q2 FY27"
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
  orphan_rows: ["R312", "R314", "R316"]
  missing_from_ledger: ["L86 Other Expenses header (2 cells)", "L94 Exceptional Items (blank row)", "L96 Tax Expenses header (2 cells incl. unexplained token '2')", "L98 Deferred Tax (third token '-')", "L104 Tax of discontinued ops (5 cells)", "L105 Net profit discontinued ops (6 cells)", "L106 Share of associates/JVs (5 cells)", "L128 Details of debt securities (blank row)", "L373 Total NC financial liabilities (2 cells)", "L377 Deferred govt grants NC (1 cell)", "L390 Deferred govt grants current (2 cells)", "L393 Liabilities held for sale (1 cell)"]
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "Revenue growth is not in doubt; operating leverage absorbed 376 bps (rev L360, L133, L152, L151, L485)", counter: "Volume and price split is ND. Gross profit +16.69% (2,709 to 3,161) and conversion costs +15.48% (1,576 to 1,820) against net revenue +39.63%. If conversion costs track volume, revenue is partly price-led and the opex gain is denominator inflation that reverses with resin. Name it as a third reading with its separating observation.", source_line: "L75, L80-L83, L87, L88", type: MISSING}
  - {claim: "Gross margin held near 37.2% for four quarters, then fell (rev L464, L174, L334, L453, L561)", counter: "Q3 and Q4 FY26 are not filed. Only Q1 FY26 37.24%, Q2 FY26 37.29% and H2 FY26 combined 37.16% derive. The fall may have begun in Q4 FY26, which weighs against a short resin-lag reading.", source_line: "L75, L80-L82, L87; rev L165-L166", type: FACTUAL}
  - {claim: "Trade WC is not the drag; CCC improved 23.64 days (rev L242, L224, L488)", counter: "On H2 FY26 flows the 31-03-2026 CCC was 95.08 days, so the like-for-like gain is 16.40 days. A4's own Q5 bull answer (supplier advances, GST credit; rev L377) is trade WC in substance: trade WC plus other current assets rose 78.14 to 84.31 Cr (+7.90%).", source_line: "L75, L80-L82, L339, L342, L349, L383", type: MISSING}
findings_by_type:
  factual:
    - "A5-F1 (A4): 'four steady quarters' of gross margin near 37.2% is not filed; only Q1 FY26 37.24%, Q2 FY26 37.29%, H2 FY26 combined 37.16% derive (L75, L80-L82, L87). Restate at rev L174, L334, L453, L464, L561."
  missing:
    - "A5-M1 (A2): 12 fulltext lines absent from structured file and ledger (L86, L94, L96, L98 third token, L104, L105, L106, L128, L373, L377, L390, L393; 27 cells, 2 blank rows); missing_from_structured wrongly empty."
    - "A5-M2 (A3): orphan rows R312, R314 (CIN_OCR_MISMATCH) and R316 (UDIN_UNRESOLVED) have no A4 disposition; unreadable UDIN (L515) belongs with F-03 AMBER, Q14, M2."
    - "A5-M3 (A4): surviving counter AR-1, price-led third reading (gross profit +16.69%, conversion costs +15.48% vs net revenue +39.63%) not named."
    - "A5-M4 (A4): surviving counter AR-3, like-for-like CCC gain 16.40 days not 23.64; supplier-advance substance lifts trade WC plus OCA 78.14 to 84.31 Cr."
  contradiction:
    - "A5-C1 (A4): other current financial assets +400 (L346) used in both the CFO drag (rev L242) and Reading B of the 455 investing outflow (rev L236); CF OCA adjustment 1,084 (L197) vs BS OCA rise 590 (L349), 494 gap unstated; investments +174 vs H1 OCI +166 (L109) suggests Reading B is non-cash marks."
  style:
    - "S-1 H1 margin change -96 bps should be -95 bps (rev L147)."
    - "S-2 opex ratio +376 bps should be +375 bps (rev L151, L485)."
    - "S-3 ETR share 14.4% on rounded 26 lakh; 14.6% unrounded (rev L197, L202)."
    - "S-4 implied shares about 1,048 lakh on cross-column EPS bands, not 1,044 (rev L43, L338, L381)."
    - "S-5 equity anchor L147 should be L364 (rev L231)."
    - "S-6 Note 2 row 'about 12% of revenue' should read relative 12% (rev L49)."
    - "S-7 forward-map M4 entry undated (rev L502)."
    - "S-8 A2 zero-standing header '13 line items' lists 10 plus 3 blank rows."
    - "S-9 R233/R234 subtotal 6,407 undisposed; casts as PPE + CWIP + intangibles."
    - "S-10 reserves 10,728 basis (previous year-end reserves) unstated at rev L331."
loop_back_to: "A2"
gap: "A2: add 12 fulltext lines missing from structured file and ledger (L86, L94, L96, L98 third token, L104, L105, L106, L128, L373, L377, L390, L393; 27 cells), fix missing_from_structured, recount line_items 105, zero_standing 49, qualifiers 42. A3: dispose orphan rows R312/R314 (CIN_OCR_MISMATCH) and R316 (UDIN_UNRESOLVED, tie to F-03). A4: (1) FACTUAL restate 'four steady quarters' at rev L174, L334, L453, L464, L561; (2) CONTRADICTION allocate other current financial assets +400 once (rev L236 vs L242), state the 1,084 vs 590 gap (L197, L349) and the investments +174 vs OCI +166 reading; (3) MISSING graft AR-1 (price-led third reading, gross profit +16.69%) and AR-3 (like-for-like CCC gain 16.40 days; supplier-advance substance)."
style_notes: ["S-1 -96 to -95 bps (rev L147)", "S-2 +376 to +375 bps (rev L151, L485)", "S-3 ETR share 14.6% unrounded (rev L197, L202)", "S-4 implied shares about 1,048 lakh (rev L43, L338, L381)", "S-5 equity anchor L364 not L147 (rev L231)", "S-6 GST understatement is relative 12% (rev L49)", "S-7 date the M4 forward-map entry (rev L502)", "S-8 A2 zero-standing line-item label", "S-9 dispose R233/R234 fixed-asset subtotal", "S-10 state reserves 10,728 basis (rev L331)"]
analyst_note: "Verdict INCOMPLETE on six loop findings. The A2 and A3 items are mechanical: nil template rows, two blank rows, and three identifier rows whose A2 flags A4 never disposed. They change no A4 number, so the re-run can stay narrow. The A4 items carry substance. One: 'four steady quarters' is not filed. Q3 and Q4 FY26 exist only as an H2 average of 37.16%, so the margin fall may have begun in Q4 FY26, which weakens the resin-lag reading. Two: the cash-flow other-current-assets adjustment (1,084) exceeds the balance-sheet rise (590) by 494, and A4 uses the +400 other current financial assets twice. Investments rose 174 against H1 OCI of +166, so Reading B may be non-cash marks; the conservative FCF of 2.86 Cr gains support. Three: gross profit rose 16.69% and conversion costs 15.48% against revenue +39.63%, so volume against price is open. P&L and cash-flow casts tie; the balance sheet ties with the four F-10 cells at cast values 142, 130, 232, 628. No arithmetic mismatch above rounding. No acquisition in the filing."
```
