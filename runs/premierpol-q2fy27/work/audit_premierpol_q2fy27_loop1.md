# A5 ADVERSARY / COMPLETENESS AUDIT: PREMIER POLYFILM LIMITED (PREMIERPOL), Q2 FY27 (loop 1)

Audited: runs/premierpol-q2fy27/work/review_premierpol_q2fy27.md (A4 loop 1, 640 lines).
Inputs read: A1 fulltext (body lines 1 to 522), A1 structured file (R001 to R401), A2 ledger (loop 1, incl. section 10A X001 to X012), A4 review.
Not opened: source PDF, anything under inputs/, A3 forensics, orchestrator commentary, the prior A5 audit.
Anchors: "L" = A1 fulltext body line; "R" = A1 structured row; "X" = A2 ledger-only row; "RL" = A4 review line. Units in Rs lakh unless marked Cr.
Finding IDs continue the loop-0 series (A5-F1, A5-C1, A5-M1 to M4, S-1 to S-10 are closed). New IDs: A5-F2, A5-M5, A5-M6, S-11 to S-18.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Part | Heading in review | Content | Status |
|---|---|---|---|
| (1) Summary narrative | RL518 "1. SUMMARY NARRATIVE" | RL519 to RL533, 15 lines (band 10 to 20). Numbers, cause, cash, debt, next decision. | present |
| (2) Sector intelligence | RL535 "2. SECTOR INTELLIGENCE" | RL536 to RL541, six bullets; tiers and PENDING LIVE VERIFICATION marked. | present |
| (3) Business-model intelligence | RL543 "3. BUSINESS-MODEL INTELLIGENCE" | RL544 to RL549, six bullets incl. three readings and WC. | present |
| (4) Competition intelligence | RL551 "4. COMPETITION INTELLIGENCE" | RL552 to RL556, five bullets; peers marked INFERENCE. | present |
| (5) Forward map | RL558 "5. FORWARD MAP" | RL559 to RL567, eight dated items, each with a bull and a bear fork. | present |

Gate result: PASS. All five parts present and non-empty.

---

## LOOP-0 FIX VERIFICATION (from the review text only)

| Loop-0 id | Fix claimed (RL17 to RL24) | Verified in review | Status |
|---|---|---|---|
| A5-F1 | "Four steady quarters" removed | No occurrence remains. RL217, RL390, RL512, RL523 to RL524 carry Q1 FY26 37.24%, Q2 FY26 37.29%, H2 FY26 combined 37.16%. | fixed |
| A5-C1 | +400 other current financial assets allocated once | RL287 (operating drag only), RL291 (excluded from Reading B). | fixed |
| A5-M3 | Price-led third reading and Q16 | RL197 to RL198, RL416, RL445, RL546. | fixed |
| A5-M4 | Like-for-like CCC and substance WC | RL265, RL270 to RL273, RL549. | fixed |
| A5-M1 / M2 | X-rows counted, CIN and UDIN disposed | RL30, RL38, RL44, RL45, RL94. | fixed |

---

## 1. COVERAGE AUDIT

Method: a fresh line-by-line pass over the A1 fulltext. I counted every line that carries a value token, then every nil token, note, entity, date, identifier, qualifier, agenda item and auditor paragraph. I diffed the result against the A2 ledger and the structured file. Then I checked each ledger row for a citation or a disposition in the A4 review.

| Category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Notes | 5 (+1 unnumbered, R384) | 5 (L152, L153 to L154, L155 to L156, L157, L158) + 1 (L165) | none | PASS |
| Line items with values | 105 (96 structured + 9 X) | 105: P&L p2 28 lines, p3 10, CF 21, BS p6 25, BS p7 21 | none | PASS |
| Value cells | 337 (310 + 27) | 337: P&L 134, p3 56, CF 36, BS 84, X-rows 27 | none | PASS |
| Zero-standing cells | 49 (23 + 26) | 49 (L86 2, L96 1, L98 2 incl. R097, L103 6, L104 5, L105 6, L106 5, L331 2, L348 2, L351 2, L370 2, L371 2, L372 2, L373 2, L377 1, L378 2, L382 2, L390 2, L393 1) | none | PASS |
| Qualifiers | 42 (40 + X002, X008) | 42; no value-bearing qualifier omitted (blank template rows: S-14) | none | PASS |
| Agenda items | 1 (R365) | 1 (L25 to L30, results only) | none | PASS |
| Auditor paragraphs | 5 (R396 to R400) | 5 (title and scope incl. para 1 L428 to L459; para 2 L461; para 3 L477; conclusion fragment L490; garbled marker) | none | PASS |
| Entities | 23 (R320 to R342) | 23 | none | PASS |
| Dates | 19 (R343 to R361) | 19 (other date tokens repeat these) | none | PASS |
| Identifiers | 9 (R311 to R319) | 9, plus 6 immaterial contact or reference tokens (S-13) | none | PASS |
| Footnote markers unresolved | 4 | 4 (L37, L95, L131, L521); other glyphs are signature or stamp noise | none | PASS |
| Turns / questions / slides | 0 | 0 (results filing only) | none | PASS |
| Structured IDs referenced in ledger | 401 of 401 | 401 of 401 (R001 to R310 contiguous ranges; R311 to R319; R320 to R342; R343 to R361; R362 to R401 checked one by one) | none | PASS |
| Ledger rows cited or dispositioned in A4 | 413 | 413. Cited by ID or line in Steps 0 to 5 and 8.5; the remainder sit under RL30 ("413 of 413", "No ledger row is unreviewed") and the RL35 to RL47 disposition table. X001 and X012 are covered by the ZERO_STANDING row RL37 and the X001 to X012 row RL38. | none | PASS |

Missing from ledger (fresh pass found, ledger lacks): none material. Six contact and reference tokens are logged as S-13. Blank template rows are logged as S-14.

Coverage note. R196, R198 and R200 (FY26 column of L194, L196, L197) are in the ledger and fall under A4's blanket disposition. But A4's Step 5 table describes them as blank. That is an analysis error, not an orphan row. See A5-F2.

---

## 2. ARITHMETIC AUDIT

I recomputed every derived cell from the raw lakh figures in the fulltext. Tolerance is rounding at the printed precision. Result: 0 mismatches.

| Metric (A4 location) | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Net revenue Q2 FY26 / Q1 FY27 / Q2 FY27 / H1 FY26 / H1 FY27 / FY26 (RL113) | 72.64 / 87.33 / 101.43 / 137.20 / 188.76 / 296.58 | 7,264 / 8,733 / 10,143 / 13,720 / 18,876 / 29,658 lakh | L75 less L87 | PASS |
| P&L cast, all six columns (RL136) | ties | Total expenses 7,313 / 8,851 / 10,307 / 13,986 / 19,158 / 29,846; PBT 1,100 / 1,214 / 1,311 / 1,924 / 2,525 / 4,280; PAT 801 / 908 / 981 / 1,401 / 1,889 / 3,188; TCI ties | L77 to L110 | PASS |
| H1 FY27 finance cost (RL120) | 0.44 | 19,158 less 19,114 = 44; also 20 + 24 = 44 | L84, L92 | PASS |
| Material cost, six columns (RL142) | 45.55 / 58.08 / 69.82 / 86.07 / 127.90 / 186.22 | 4,555 / 5,808 / 6,982 / 8,607 / 12,790 / 18,622 | L80 to L82 | PASS |
| Gross margin on net revenue (RL143) | 37.29 / 33.49 / 31.16 / 37.27 / 32.24 / 37.21% | 37.293 / 33.494 / 31.164 / 37.267 / 32.242 / 37.211% | derived | PASS |
| Operating EBITDA (RL144) | 11.33 / 12.93 / 13.41 / 20.45 / 26.34 / 45.94 | 1,133 / 1,293 / 1,341 / 2,045 / 2,634 / 4,594 | L76, L84, L85, L95 | PASS |
| Op EBITDA margin, net (RL145) | 15.60 / 14.81 / 13.22 / 14.91 / 13.95 / 15.49% | 15.597 / 14.806 / 13.221 / 14.905 / 13.954 / 15.490% | derived | PASS |
| Op EBITDA margin, reported (RL146) | 13.62 / 12.92 / 11.65 / 12.98 / 12.24 / 13.56% | 13.623 / 12.922 / 11.655 / 12.975 / 12.244 / 13.556% | derived | PASS |
| Reported EBITDA and margin (RL147 to RL148) | 12.29 to 48.30; 16.92 / 15.48 / 14.33 / 15.99 / 14.86 / 16.29% | 1,229 / 1,352 / 1,453 / 2,194 / 2,805 / 4,830; 16.919 / 15.481 / 14.325 / 15.991 / 14.860 / 16.286% | derived | PASS |
| Core PBT, OI/PBT (RL149 to RL150) | 10.04 to 40.44; 8.73 / 4.86 / 8.54 / 7.74 / 6.77 / 5.51% | 1,004 / 1,155 / 1,199 / 1,775 / 2,354 / 4,044; 8.727 / 4.860 / 8.543 / 7.744 / 6.772 / 5.514% | derived | PASS |
| ETR (RL151) | 27.18 / 25.21 / 25.17 / 27.18 / 25.19 / 25.51% | 27.182 / 25.206 / 25.172 / 27.183 / 25.188 / 25.514% | L95, L99 | PASS |
| PAT margins (RL152 to RL153) | 11.03 / 10.40 / 9.67 / 10.21 / 10.01 / 10.75%; 9.63 / 9.07 / 8.53 / 8.89 / 8.78 / 9.41% | 11.027 / 10.397 / 9.672 / 10.211 / 10.007 / 10.749%; 9.631 / 9.075 / 8.526 / 8.889 / 8.781 / 9.407% | derived | PASS |
| GST / reported revenue (RL154) | 12.66 / 12.72 / 11.85 / 12.95 / 12.25 / 12.49% | 12.661 / 12.722 / 11.846 / 12.950 / 12.254 / 12.487% | L75, L87 | PASS |
| A3 basis note (RL156) | 14.2% vs 16.7% | 1,453 / 10,255 = 14.169%; 1,229 / 7,360 = 16.698% | L77, L87 | PASS |
| Step 2 YoY set (RL166 to RL180) | +39.63%, +38.34%, GP +16.69%, -613 bps, conv. +15.48%, Op EBITDA +18.36%, -238 bps, D&A +1.72%, FC +84.62%, EBIT +20.26%, OI +16.67%, core PBT +19.42%, PBT +19.18%, PAT +22.47%, EPS +23.68% | 39.634, 38.343, 16.685, -612.9 bps, 15.482, 18.358, -237.6 bps, 1.724, 84.615, 20.256, 16.667, 19.422, 19.182, 22.472, 23.684% | derived | PASS |
| Opex ratio bridge (RL188) | 21.70% to 17.94%, +375 bps; -613 + 375 = -238 | 21.696% to 17.943%, +375.3 bps | L83, L88 | PASS |
| H1 YoY set (RL184) | +37.58, +28.80, -95 bps, +32.62, +31.24, +34.83, +34.33% | 37.580, 28.802, -95.1 bps, 32.620, 31.237, 34.832, 34.328% | derived | PASS |
| Reading 3 cost pattern (RL197) | other exp. +14.78% vs net rev +16.15% QoQ; +1.37% vs +20.22% | 14.778 vs 16.146%; 1.373 vs 20.223% | L88, L75, L87 | PASS |
| Q1 FY26 derived (RL206, RL214) | 64.56; GM 37.24%; Op EBITDA 912 lakh, 14.13%; core PBT 7.71 | 6,456; 2,404 / 6,456 = 37.237%; 824 + 117 + 24 - 53 = 912, 14.126%; 771 | H1 FY26 less Q2 FY26 | PASS |
| H2 FY26 derived (RL210, RL214) | 159.38 (79.69 avg); GM 37.16%; Op EBITDA 2,549, 15.99%; core PBT 22.69 | 15,938; 5,923 / 15,938 = 37.163%; 2,356 + 236 + 44 - 87 = 2,549, 15.993%; 2,269 | FY26 less H1 FY26 | PASS |
| QoQ run-rates (RL207 to RL212, RL217) | +12.52%, +9.71%, +9.59%, +16.15%; core PBT +3.81% | 12.516, 9.705, 9.587, 16.146, 3.810% | derived | PASS |
| H1 FY27 quarter averages (RL220) | 94.38 / 13.17 / 11.77 | 9,438 / 1,317 / 1,177 | derived | PASS |
| PAT bridge (RL231 to RL243) | 1,074; -622; -113; -131; 208; -2; -11; +16; 211; -57; +26; 180 | 2,879 x 0.372935 = 1,073.7; 10,143 x -0.061291 = -621.7; 211 x 0.271818 = 57.4; 1,311 x 0.020102 = 26.35; 211 - 57.4 + 26.4 = 180.0 | derived | PASS |
| Bridge shares (RL231 to RL243) | 596.7, -345.6, -62.8, -72.8, 115.6, -1.1, -6.1, 8.9, 117.2, -31.7, 14.4 (14.6 unrounded)% | same | derived | PASS |
| Recurring split (RL246) | 1.42 Cr, 78.9%; 6.5%; 14.6% | 195 x 0.728182 = 142.0; 11.65 / 180 = 6.47%; 26.35 / 180 = 14.64% | derived | PASS |
| Reversion case (RL247) | 9.69; 9.43; +17.73% | 9.81 - 0.12; 1,295 x 0.728182 = 943.0; 943 / 801 - 1 = 17.73% | derived | PASS |
| CF cast H1 FY27 (RL255) | 1,799; 1,322; 186; 690 | 2,525 - 726; 1,799 - 477; 1,322 - 957 - 179; 504 + 186 | L189 to L298 | PASS |
| FY26 CFO by cast (RL255) | 2,670 | -581 + 2,759 + 492 = 2,670; 1,085 - 581 = 504 | L272, L290, L292, L296 | PASS |
| Investing and financing casts | (957), (2,759), (179) | 1 - 581 + 2 + 76 - 455; 4 - 895 + 4 + 48 - 1,920; -147 - 32 | L244 to L290 | PASS |
| CFO/PAT, capex, FCF (RL259 to RL262) | 0.84x, 0.70x, 65%, 17.75, 7.41, 2.86 | 0.8375, 0.6998, 64.9%, 1,775, 741, 286 | derived | PASS |
| Trade WC and substance WC (RL264 to RL265) | 70.79 / 71.06; 78.14 / 84.31 (+7.90%); 90.00 / 100.17 (+11.30%) | 7,079 / 7,106; 7,814 / 8,431 (+7.896%); 9,000 / 10,017 (+11.30%) | L339, L342, L383, L349, L346 | PASS |
| Day counts, mixed basis (RL266 to RL269) | 44.44 / 33.72; 98.53 / 71.96; 40.65 / 27.00; CCC 102.32 / 78.68 | 44.44 / 33.72; 98.53 / 71.96; 40.65 / 27.00; 102.32 / 78.68 | derived; H1 = 183 days | PASS |
| Day counts, like-for-like (RL270 to RL273) | 41.42; 91.35; 37.69; CCC 95.08, -16.40 days, about 30% smaller | 41.42; 91.35; 37.69; 95.08; -16.40; 30.6% smaller | H2 FY26 182 days, revenue 18,129, material 10,015 | PASS |
| BS movements (RL274 to RL278) | PPE -0.02; CWIP +3.47 (about 8x); other NCA +4.80; OCA +5.90 (+80%); OCFA +4.00 | -2; +347 (7.94x); +480; +590 (80.3%); +400 | L320, L321, L336, L349, L346 | PASS |
| Net cash, BS basis (RL279) | 16.68 / 19.36 | 504 + 1,164; 690 + 1,246 | L343, L341 | PASS (see A5-M6 on content) |
| D/E-implied debt (RL280) | 18.40 to 19.87; 17.61 to 19.29; net 1.72 to 3.19 / (0.07) to (1.75) | 0.125 to 0.135 x 14,720; 0.105 to 0.115 x 16,775; derived | L147, L364 | PASS |
| Capitalisation bridge (RL285) | X = 234; 234 + 347 = 581 | 6,011 + X - 236 = 6,009 | L320, L321, L85, L245 | PASS |
| OCA reconciliation (RL287) | 494 gap; 94 residual | 1,084 - 590; 1,084 - 990 | L197, L349, L346 | PASS |
| Reading B (RL291) | 174 vs OCI 166 | 82 + 92 | L341, L330, L109 | PASS |
| A4-04 layout tie (RL294) | 162 exact; 2 vs (3) | 4,126 - 3,964 = 162; 5,029 - 5,027 = 2 | L342, L339 | PASS |
| Interest add-back gap (RL302) | 12 lakh H1; FY26 57 vs 81 | 44 - 32; 81 - 57 = 24 | L191, L84 | PASS |
| ROCE H1 FY27 (RL356) | 32.63%; 29.15% | 5,138 / 15,747.5 = 32.63%; 5,138 / (15,747.5 + 1,879) = 29.15% | L95, L84, L364, L147 | PASS |
| ROCE FY26 (RL387) | 32.90% | 4,361 / ((11,787 + 14,720) / 2) = 32.90% | L95, L84, L130, L126, L364 | PASS |
| Trailing four quarters (RL385) | PAT 36.76; net rev 348.14; EPS 3.50; annualised 39.24 | 3,676; 34,814; 3.50; 981 x 4 | derived | PASS |
| EPS share basis (RL76) | 0.926; 1,044 (1,038 to 1,049); intersection 1,047 to 1,049 | 981 / 1,059; 981 / 0.94; bands: Q2 FY26 lower 1,047.1, Q2 FY27 upper 1,049.2 | L102, L126, L139 | PASS |
| OI treasury share (RL96) | 78 = 45.6% of 171; alt. lift 93 | 78 / 171 = 45.61% | L268, L269, L76 | PASS |
| Material share, GST shares (RL337, RL540) | 68.84% vs 62.71%; 13.27%, 12.09% | 6,982 / 10,143; 4,555 / 7,264; 988 / 7,444; 2,191 / 18,129 | derived | PASS |
| Q8 non-TCI reduction (RL437) | 158 | 10,728 + 3,091 - 13,661 = 158; H1: 13,661 + 2,055 = 15,716 exact | L130, L110, L361 | PASS |
| Reg 33 dates (RL420, RL466, RL468, RL473) | 14-02-2027; 30-05-2027; 14-08-2027 | 31-12 + 45 days; 31-03 + 60; 30-06 + 45 | rule | PASS |

Balance-sheet cast with the F-10 cells at their cast values (my own check): DTA 142 (8,437 less the other NCA lines), other NCFA 232 (1,309 - 1,077), DTL 130 and total NCL 628 (5,502 - 4,874 = 628 = 498 + 130). Total assets 22,277 and 20,162 tie both sides. This supports the RL444 Q15 bull values (142 / 130 / 232 / 628).

Independent CF cast on the A4-06 allocation (RL287). Hidden H1 FY27 operating adjustments = total (726) less the visible rows (32 - 3 + 162 - 1,084 = -893) = +167 lakh (L191 to L224). Hidden flows I can identify, excluding other current financial assets: D&A +236 (L85), trade payables -187 (L383), other current liabilities +127 (L386), provisions +56 (L374, L388), other current financial liabilities -94 (L384), and interest and dividend income -78 (L268, L269). Their sum is +60. With the +400 inside the 1,084, the residual is +107. If the +400 sat in a separate line (L200), the residual would be about +507. The cast supports A4's allocation. The blank-L200 argument does not support it (S-15).

---

## 3. ADVERSARIAL READ

The three most positive claims in A4's review are tested below. Each bear counter is built from the A1 extract only.

### Claim 1. "The headline growth is real in rupees at the operating level" (RL189; RL166, RL519 to RL520: net revenue +39.63%, core PBT +19.42%)
Strongest bear counter: gross profit rose 16.69% and conversion costs 15.48% against net revenue +39.63% (L75, L80 to L83, L87, L88). So volume may have grown near 15%, with resin price carrying the rest. QoQ core PBT rose 3.81% on revenue up 16.15% (L95, L76). About 3.3 pp of the PAT growth is an ETR base effect (26 / 801, L97, L99).
Survives? The counter is supported, but A4 already carries it: Reading 3 (RL197 to RL198), the Step 3 QoQ line (RL217), the ETR line (RL241) and the reversion case (RL247). No graft is needed. One extra datum (S-18): Q2 FY27 traded purchases fell to 217 lakh, 3.1% of material cost, from 704 lakh (12.1%) in Q1 FY27 (L81). So the Q2 gross-margin fall is not a traded-goods mix effect. That narrows Reading 2. Status: does not survive beyond the existing text.

### Claim 2. Working-capital discipline: "Trade WC flat in form while revenue rose 39.63% YoY" (RL264); the CCC improved by 16.40 days like-for-like (RL273); "receivable days near 34" is listed as a strength (RL553, RL549)
Strongest bear counter: the 31-03-2026 base that every day-count gain starts from came after a large FY26 build. The audited FY26 column of the cash flow shows three values:
- (1,829.00) at L194 (R196)
- (422.00 at L196 (R198)
- (64.00) at L197 (R200)
Two label readings:
- A1's labels, which A4 keeps as the conservative read for F-11 (RL294): current trade receivables rose 1,829 lakh in FY26, from about 2,297 lakh at 31-03-2025 to 4,126 (L342), about +80%. Non-current receivables rose 422.
- The A4-04 layout reading, which ties the H1 FY27 cells exactly to the balance sheet (162 vs 162, 3 vs 2; L339, L342): inventories rose 1,829 lakh, from about 3,198 to 5,027 (+57%). Current receivables rose 422, from about 3,704 (+11%).
On either reading, inventory plus receivables grew about 22.51 Cr in FY26. That is 70.6% of FY26 PAT (3,188, L108). The H1 FY27 gains (inventory days 91.35 to 71.96, receivable days 41.42 to 33.72) start from that elevated base. They may be a partial unwind of a FY26 build, not a structural tightening.
The cash drag also changed lines rather than going away. It sat in trade items in FY26 and in other current assets in H1 FY27 (L197). CFO/PAT was below 1.0x in both periods (0.84x, 0.70x).
One more point: RL264 sets a six-month WC change against YoY quarterly growth. The matching comparison is half on half: net revenue +18.43% (H1 FY27 188.76 vs H2 FY26 159.38 Cr) (S-16).
Survives? Yes. The FY26 values are filed (L194, L196, L197). A4 never states what the (1,829) means on either reading. A4's Step 5 table calls the FY26 WC rows "ND (rows blank)" (RL263), which is wrong (A5-F2). Must be grafted (A5-M5).

### Claim 3. Balance-sheet strength: "(19.36) net cash" (RL279; RL531) and "low debt on any reading, ROCE above 29% on any reading" (RL553)
Strongest bear counter: both net-cash readings (RL279, RL280) treat 12.46 Cr of current investments (L341) as cash. The extract does not show that these investments are cash-like.
- The investment book rose 174 lakh in H1 against H1 OCI of +166 (L330, L341, L109). The review's own Reading B (RL291) reads this as fair-value marks.
- OCI swung +384 and (218) lakh in Q1 and Q2 FY27 (L109). Each swing is larger than the full FY26 OCI of (97). So part of the book is marked to market through OCI [INFERENCE; the current vs non-current split of the marks is ND].
- On cash alone (6.90 Cr, L343) against the D/E-implied debt of 17.61 to 19.29 Cr (L147, L364), net debt is 10.71 to 12.39 Cr. That is 0.06x to 0.07x of equity.
What survives of the claim:
- "Low debt on any reading" survives.
- "ROCE above 29%" survives. Without treasury income and without cash and investments, H1 FY27 ROCE is about 32.4% (with D/E-implied debt) to 37.1% (without it). Basis: 4,796 lakh annualised EBIT ex-OI over an average of 12,915 to 14,794 lakh.
- The net-cash framing does not survive. The brief offers two outcomes, 19.36 Cr net cash "or close to zero", both depending on where the debt sits (RL531). A third outcome, net debt of about 11 to 12 Cr, depends on what the current investments are. A4 does not name it.
Survives? Yes, as a missing qualifier. Must be grafted (A5-M6).

### Mandatory acquisition-economics probe
Not triggered. The extract describes no acquisition, purchase of a business, or stake buy:
- Control-acquisition and equity-purchase rows (L233 to L243) carry no values.
- Note 5 says there is no subsidiary, associate or JV (L158).
- No deal is named.
The only purchases are PPE (581 lakh, L245) and an undescribed investing outflow (455 lakh, L271). Neither has a target or target earnings, so no price-to-earnings multiple can be formed. The undisclosed build (CWIP 397, other NCA 579; L321, L336) is already flagged under F-08 and Q2.

---

## FINDINGS

| ID | Type | Finding | Evidence | Loop to | Fix |
|---|---|---|---|---|---|
| A5-F2 | FACTUAL | Step 5 row "Working capital change (CF)" gives FY26 as "ND (rows blank)". The audited FY26 column carries three WC adjustments: (1,829.00) L194, (422.00 L196, (64.00) L197, gross (23.15) Cr. Only the FY26 total-adjustments and offsetting rows are absent from the text layer. | RL263; L194, L196, L197; R196, R198, R200 | A4 | Restate the FY26 cell: "total adjustments ND (not in text layer); filed WC rows (18.29) L194, (4.22) L196, (0.64) L197, gross (23.15); payables and other rows ND". |
| A5-M5 | MISSING | Surviving bear counter against Claim 2 (WC discipline). On either label reading, FY26 built about 22.51 Cr of inventory plus receivables. Receivables rose about 80% on A1's labels; inventories rose about 57% on A4-04. The H1 FY27 day-count gains start from that elevated base, and the cash drag moved from trade items to other current assets. A4 cites the (1,829) only as a layout token (RL294) and never states its meaning. | L194, L196, L339, L342, L108; RL264 to RL273, RL294, RL298, RL433, RL549, RL553 | A4 | Graft the counter (text below) into Step 5 (after RL273 and into the structural-vs-growth answer RL298), the F-11 conservative read (RL294), Q4 (RL433: add the FY26 1,829), brief part 3 (RL549), brief part 4 (RL553: qualify "receivable days near 34") and verdict flag 7 (RL512). |
| A5-M6 | MISSING | Surviving bear counter against Claim 3 (net cash). Both net-cash readings count 12.46 Cr of current investments as cash. The investment book moves with OCI (+174 vs +166; +384 and (218) quarterly). On cash only against D/E-implied debt, net debt is 10.71 to 12.39 Cr. The qualifier is absent from the net-cash rows and the brief. | L109, L330, L341, L343, L147, L364; RL279 to RL280, RL300, RL355, RL531 | A4 | Graft the qualifier (text below) into the Step 5 net-debt rows, the Step 5 net-debt question (RL300), Step 6A (RL355) and brief part 1 (RL531). Link Q12 (RL441). |

Contradictions between agents or cells: none new. The A2 label inconsistency (X004/X013 vs X002/X008) is cosmetic. A4 already records and resolves it (RL49) (S-11).

### Graft text for A4 (suggested; A4 may tighten wording, numbers must stay)

A5-M5, Step 5 paragraph after the like-for-like rows:
"FY26 base effect (A5-M5). The audited FY26 cash flow shows (1,829) at L194 and (422) at L196. On A1's labels, kept here as the conservative read for F-11, current trade receivables rose 1,829 lakh in FY26, from about 2,297 lakh at 31-03-2025 (+80%), and non-current receivables rose 422. On the A4-04 layout reading, which ties both H1 FY27 cells to the balance sheet, inventories rose 1,829 lakh (from about 3,198, +57%) and current receivables 422 (from about 3,704, +11%). On either reading, inventory plus receivables grew about 22.51 Cr in FY26, 70.6% of FY26 PAT [FILED, derived]. The H1 FY27 day-count gains start from that elevated 31-03-2026 base. The cash drag moved from trade items in FY26 to other current assets in H1 FY27. CFO/PAT was below 1.0x in both periods (0.84x, 0.70x). Net FY26 WC change is ND: payables and other FY26 rows are not in the text layer."

A5-M5, Q4 extension: "...and the FY26 1,829 lakh increase at L194, which the filing's label order assigns to current receivables: is it receivables or inventories, and what was the 31-03-2025 balance?"

A5-M5, brief part 3 addition: "The 31-03-2026 base came after a FY26 build of about 22.51 Cr in inventory and receivables, so part of the H1 gain may be an unwind [FILED, derived; INFERENCE]."

A5-M6, Step 5 net-debt qualifier:
"Both readings count current investments of 12.46 Cr (L341) as cash. The investment book rose 174 lakh in H1 against H1 OCI of +166 (L109), and OCI swung +384 and (218) lakh in Q1 and Q2 FY27. So part of the book is marked to market [INFERENCE; current vs non-current split ND, F-05]. On cash alone (6.90 Cr, L343) against D/E-implied debt of 17.61 to 19.29 Cr, net debt is 10.71 to 12.39 Cr (0.06x to 0.07x equity). Debt stays low on every reading. Net cash depends on both the debt location (Q3) and the investments being cash-like (Q12)."

A5-M6, brief part 1 (RL531) replacement:
"So net cash is 19.36 Cr, or close to zero, or net debt of about 11 to 12 Cr. The answer depends on where the debt sits and on what the 12.46 Cr of current investments are [INFERENCE]."

---

## VERDICT

**INCOMPLETE.** Failing agent: A4. Gaps:
- A5-F2 (FACTUAL): the Step 5 FY26 working-capital cell misstates the filed FY26 rows.
- A5-M5 (MISSING): surviving bear counter on the FY26 inventory and receivable build, against the WC-discipline claim.
- A5-M6 (MISSING): surviving bear counter on current investments in net cash.
Coverage passes (no orphan rows, nothing missing from the ledger). Arithmetic passes (0 mismatches). The deliverable gate passes. No loop to A2 or A3.

---

## STYLE NOTES (logged, no re-run)

- S-11. A2 count-test line 11 names the blank rows "X004 L94, X013 L128". Section 10A numbers them X002 and X008, and X013 does not exist. A4 records this at RL49. A2 should correct it at next touch. Counts are unaffected.
- S-12. A2 section 2 header says "23 cells, 13 line items". The list holds 10 zero-standing line items. The 13 appears to include the 3 blank-in-source rows (R373, R376, R388) listed below it. State the split.
- S-13. Six contact and reference tokens are not enumerated: L5 company email (A4 uses it at RL454), L6 website, L10 letter reference "PPL/SECT/2026-2027", L416 auditor phone, L417 and L419 auditor address (Rohini, Delhi), L426 auditor email. They are attributes of R320, R343 and R338. No value is lost.
- S-14. Blank template rows are enumerated only where material (X002, X008, R373, R376, R388, R390, R395). Examples left out: L141 to L143, L282, L286, L332, L344, L345. No value is lost. One caution for F-01 and F-07: the FY26 financing total (492) at L290 has no visible parts, so the text layer drops FY26 financing values. A blank L286 (dividends paid) or L282 (proceeds from borrowings) is not evidence of nil for FY26.
- S-15. RL287 says the blank L200 makes the 1,084 the only home for the +400. That reason is weak, because the same text layer drops D&A (L206), which must carry 236 for CFO to cast. Replace it with the cast: hidden adjustments +167 against about +60 identifiable; residual +107 with the +400 inside the 1,084, about +507 if separate. The cast supports the allocation, so the conclusion stands.
- S-16. RL264 sets a six-month trade-WC change against Q2 YoY revenue growth of 39.63%. The matching comparison is half on half: net revenue +18.43% (188.76 vs 159.38 Cr). The direction stands.
- S-17. Q8's bull answer "AGM held with the dividend booked in Q3 FY27" (RL437) conflicts with Ind AS recognition. A dividend is recognised when shareholders approve it. An AGM held by 30-09-2026 that declared a dividend would show in H1 equity, but H1 equity moved exactly by TCI. A Q3 booking implies an AGM after 30-09-2026, which is the bear answer. Suggested bull: "AGM held by 30-09-2026, no dividend declared, reason stated (capex funding)". The FY26 reduction of 158 lakh matches about Rs 0.15 per share on 1,059 lakh shares [INFERENCE].
- S-18. Traded-goods datum not used. Purchases of stock-in-trade were 217 lakh in Q2 FY27, 3.1% of material cost. They were 704 lakh (12.1%) in Q1 FY27 and 215 lakh (4.7%) in Q2 FY26 (L81). So the Q2 gross-margin fall is not a traded-goods mix effect, which narrows Reading 2 to manufactured mix, exports or price. H1 traded purchases rose 134% YoY (394 to 921), part of H1 growth.

---

```yaml
stage: A5-adversary
loop: 1
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
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "Trade WC flat while revenue grew; CCC improved 16.40 days like-for-like; receivable days near 34 as a strength (RL264-RL273, RL549, RL553)", counter: "31-03-2026 base follows a FY26 build of about 22.51 Cr in inventory plus receivables: CF FY26 (1,829) L194 and (422) L196; current receivables +80% on A1 labels or inventories +57% on the A4-04 layout; drag moved from trade items (FY26) to other current assets (H1 FY27); CFO/PAT below 1.0x in both periods", source_line: "L194, L196, L197, L339, L342, L108", type: MISSING}
  - {claim: "Net cash 19.36 Cr BS basis; answer depends only on debt location (RL279, RL531)", counter: "Both readings count 12.46 Cr current investments as cash; investment book +174 vs H1 OCI +166 and quarterly OCI +384/(218) show market marks; cash-only vs D/E-implied debt gives net debt 10.71-12.39 Cr (0.06-0.07x equity); low debt survives, net-cash framing needs the qualifier", source_line: "L109, L330, L341, L343, L147, L364", type: MISSING}
findings_by_type:
  factual:
    - "A5-F2: Step 5 RL263 says FY26 WC rows ND (rows blank); FY26 column carries (1,829) L194, (422) L196, (64) L197 (R196, R198, R200), gross (23.15) Cr. Loop A4."
  missing:
    - "A5-M5: surviving bear counter vs WC-discipline claim; FY26 inventory plus receivable build about 22.51 Cr (70.6% of FY26 PAT) not stated; graft into Step 5, F-11 read, Q4, brief parts 3-4, flag 7. Loop A4."
    - "A5-M6: surviving bear counter vs net-cash claim; current investments 12.46 Cr counted as cash with OCI-linked marks; net debt 10.71-12.39 Cr on cash-only reading; graft into Step 5 net-debt rows, RL300, Step 6A, brief part 1. Loop A4."
  contradiction: []
  style:
    - "S-11: A2 count-test labels X004/X013 vs section 10A X002/X008"
    - "S-12: A2 section 2 '13 line items' = 10 zero-standing + 3 blank-in-source rows"
    - "S-13: six immaterial contact/reference tokens unenumerated (L5, L6, L10, L416, L417/L419, L426)"
    - "S-14: blank template rows not enumerated; FY26 financing parts dropped by text layer, so blank L282/L286 is not evidence of nil"
    - "S-15: RL287 blank-L200 argument weak; CF cast (hidden +167 vs about +60 identifiable) supports the allocation"
    - "S-16: RL264 six-month WC change vs YoY growth; half-on-half net revenue +18.43%"
    - "S-17: Q8 bull answer conflicts with Ind AS dividend recognition on approval"
    - "S-18: traded purchases 3.1% of Q2 FY27 material cost vs 12.1% Q1 FY27; margin fall not traded-goods mix"
loop_back_to: "A4"
gap: "A5-F2 (FACTUAL): restate Step 5 FY26 WC cell with filed rows (1,829) L194, (422) L196, (64) L197. A5-M5 (MISSING): graft FY26 inventory/receivable build counter (about 22.51 Cr; +80% receivables on A1 labels or +57% inventories on A4-04) into Step 5, F-11 read, Q4, brief parts 3-4, flag 7. A5-M6 (MISSING): graft current-investments qualifier (net debt 10.71-12.39 Cr on cash-only reading) into Step 5 net-debt rows, RL300, Step 6A, brief part 1."
style_notes:
  - "S-11 A2 X-ID labels in count test"
  - "S-12 A2 zero-standing line-item sub-count"
  - "S-13 immaterial identifiers unenumerated"
  - "S-14 blank template rows; FY26 financing parts dropped"
  - "S-15 replace blank-L200 reasoning with CF cast"
  - "S-16 half-on-half revenue +18.43% for the WC juxtaposition"
  - "S-17 Q8 bull answer dividend timing"
  - "S-18 traded-goods datum narrows Reading 2"
analyst_note: "Arithmetic is clean: every derived cell in Steps 1 to 6.5 recomputes within rounding, and the balance sheet casts once the four F-10 cells take their cast values (142/130/232/628). Coverage is clean: 105 line items, 337 cells, 49 nil cells and 413 ledger rows match a fresh fulltext pass. Loop-0 fixes are in. The new gap is the FY26 cash-flow column. A4 calls the FY26 WC rows blank, but L194, L196 and L197 carry (1,829), (422) and (64). On either label reading, inventory plus receivables rose about 22.51 Cr in FY26, so the H1 day-count gain starts from an elevated base and the cash drag changed lines rather than vanished. Second, both net-cash readings treat 12.46 Cr of current investments as cash while the review's own Reading B ties the investment book to OCI marks. A CF cast (hidden adjustments +167 lakh vs about +60 identifiable) supports A4's +400 allocation; the blank-L200 argument does not, because the same text layer drops D&A. The grafts sharpen flag 7 and the net-debt range; on my read they do not move the PROCEED WITH FLAGS verdict."
```
