# A5 AUDIT: NEOCHEM (Neochem Bio Solutions Limited), H1 FY27 (q2fy27)

Agent A5, adversary and completeness auditor. Model claude-opus-5-5. Run date 2026-10-29.

Inputs read: A4 review (592 lines), A1 results fulltext (292 lines) and structured file (R001-R363), A1 intimation fulltext (102 lines) and structured file (I001-I033), A2 results ledger (176 lines).
Not read: the source PDF, anything under inputs/, A3 forensics, orchestrator commentary. No step needed the source, so no pipeline error is raised.

Cite keys: FT = results fulltext line. IT = intimation fulltext line. RV = A4 review line. LG = A2 ledger line. Rnnn and Innn = A1 row IDs. Values in Rs Lakhs unless marked Cr (Lakhs x 0.01 = Cr).

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate, run first)

**DELIVERABLE-COMPLETENESS: narrative PRESENT | sector PRESENT | business model PRESENT | competition PRESENT | forward map PRESENT. Gate PASS.**

| Part | Heading | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | RV 476 | RV 478-484: four paragraphs, about 235 words, about 16 rendered lines. The Quarterly Results protocol governs, so the 10-20 line spec applies. Covers growth, quality, three same-half events, posture. | present |
| 2. Sector intelligence | RV 486 | RV 488: single segment, margin pattern, CCO end markets, NOT DISCLOSED items named. | present |
| 3. Business-model intelligence | RV 490 | RV 492-496: cost structure, working-capital cycle, funding source, model shift. | present |
| 4. Competition intelligence | RV 498 | RV 500: no peer set passed, Indofil link, price risk, Q9 test, Role 2 gap named. | present |
| 5. Forward map | RV 502 | RV 504-513: one make-or-break reading plus eight catalysts. Each has a Bull and a Bear fork. Five are dated. Four are marked "Undated" because the filing gives no date (honest NOT FOUND; see S4). | present |

---

## 1. COVERAGE AUDIT

**Method.** I ran a fresh line sweep and grep pass over FT 1-292 and IT 1-102, without reference to A2's counts. Grep checks run:
- Numbered items `^\d\. `: agenda items at FT 39, 42, 45, 53; Notes 1-9 at FT 221, 224, 227, 229, 231, 233, 234, 236, 238.
- Cash flow notes: FT 287 (Note 1), FT 288 (Note 2), FT 290 (Note 3).
- Audit-report terms (Emphasis, Other Matter, Going Concern, qualified, adverse, disclaim): zero hits in the review report. The single "Qualified" hit is FT 75, "Qualified Chartered Accountant".
- Group and related-party terms (subsidiar, associate, joint venture, related part, consolidat, contingent, pledge, dividend): zero hits.
- "warrant": FT 139 only (nil both dates).
- Blank-valued table rows `| | |$`: FT 141, 145, 200, 207 are line items with no value in any column. The other hits are section headings.

### Coverage table

| Category | A2 count | Fresh count (A5) | Orphan rows | Status |
|---|---|---|---|---|
| Structured IDs | 363 (LG 4) | 363: NUMBER R001-R273 (273), ENTITY R274-R302 (29), FORWARD R303-R306 (4), DATE R307-R329 (23), QUALIFIER R330-R363 (34). Every ID maps to a ledger row (range sweep below). | none | MATCH |
| Notes | 12 (LG 5) | 12: Notes 1-9 (FT 221-239) and CF Notes 1-3 (FT 287-290) | none. R343-R355 and R358-R363 cited at RV 19; each note tabled at RV 64-75 | MATCH |
| Line items (value-bearing labels) | 99 (LG 6) | 99: balance sheet 31 (FT 137-174), results 27 (FT 184-215), cash flow 37 (FT 248-286), cash recon 4 (FT 288-290). Also 4 blank-valued labels (FT 141, 145, 200, 207), each nil by subtotal tie-out (S1). | R005-R006 (FT 139); R041-R044 (FT 163-164) | **FAIL** |
| Line-item value rows | 243 (LG 7) | 243: balance sheet 62; results 99 (108 cells less 9 blank cells: FT 198 col 3; FT 209 cols 1-3; FT 210 cols 2-3; FT 211 cols 2-4); cash flow 74; recon 8 | as above | MATCH (count) |
| Zero-standing | 42 (LG 8) | 42: balance sheet 6 (FT 139, 163, 164 x2 each); results 15 (FT 190 x4, 198 x1, 204 x2, 205 x4, 209 x1, 210 x2, 211 x1); cash flow 18 (FT 251 x2, 252, 253 x2, 255, 261 x2, 266, 271 x2, 274 x2, 278 x2, 280 x2, 281); recon 2 (FT 288 FDs); NIL complaints 1 (FT 227-228) | R005, R006, R041, R042, R043, R044 uncited | **FAIL** (6 of 42) |
| Agenda items | 4 (LG 9) | 4: FT 39, 42, 45, 53 | R236-R237 meeting-times row (LG 83-85) | **FAIL** |
| Auditor paras | 7 (LG 10) | 8 units: letterhead and title FT 93-95; addressee FT 96-97; subject FT 98-100; introduction FT 101-104; responsibility FT 105-110; scope FT 111-117; conclusion FT 121-126; signature FT 127-129. The delta is definitional (signature block counted separately). Every unit maps to R249-R256, R279, R293-R295, R300, R317, R335-R338. No Emphasis of Matter, Other Matter, Going Concern or modified-opinion paragraph exists. | none | MATCH (definitional; S11) |
| Entities | 29 (LG 11) | 29 material entities (R274-R302). Generic organs and statutes (Board of Directors FT 37, 105, 221; Companies Act FT 107, 116, 225) are not separate rows. No subsidiary, associate or JV is named. | none | MATCH |
| Annexure tables | 1 (LG 12) | 1 table, FT 67-90: 4 rows x 3 persons = 12 cells. Every cell maps to a ledger row (R244-R248, R280-R282, R287-R292, R304, R312-R314, M1, M2). Sub-cell fragments sit only in the fulltext (S6). | none | MATCH |
| Signature blocks | R255, R321, R328, M3 (LG 110) | 5 blocks: FT 63, 175-176, 216-217, 240-241, 291-292. All five map (R255, R321, M3, R328, M3). | none | MATCH |
| MISSING_FROM_STRUCTURED | M1-M3 (LG 134-136) | Confirmed at FT 88-90 (M1), FT 83 (M2), FT 216 and 291 (M3). A4 read all three (RV 20). | none | carried |
| Intimation rows (A1 only; no A2 ledger by design) | n/a | 33 rows: NUMBER 8, ENTITY 12, FORWARD 3, DATE 7, QUALIFIER 3, matching the header. A fresh sweep of IT 1-102 finds no material unit absent from the structured file (line-ref drift in S5; minor entities in S12). | n/a. A4 states all 33 read (RV 21) and cites I014, I017-I019, I021, I023-I025, I028, I031. | PASS |

### Ledger-row disposition sweep

The A2 ledger holds 49 rows: 46 disposition rows (LG 20-131) and M1-M3 (LG 134-136). I checked each row against A4 by row ID, ID range, or FT line cite. **46 rows are cited. 3 rows are orphans.** None of the three has a citation, an FT line cite, or a "reviewed, no finding" mark.

| Orphan ledger row | Ledger line | What it holds | Why it matters | Grep evidence in review |
|---|---|---|---|---|
| R005-R006 | LG 46 | Money received against share warrants, nil both dates (FT 139) | This row is direct evidence for A4's "no dilutive instruments" (RV 54). A4 rests that only on basic EPS = diluted EPS. | No "R005", "R006", "warrant", or line 139 |
| R041-R044 | LG 47 | Asset-side "Deferred Tax Liabilities (net)" nil, and Long Term loans and advances nil, both dates (FT 163-164; label note R358) | No long-term loan asset exists. Any loan given can only sit in ST loans and advances (1,019.20, FT 171), non-current investments (509.07, FT 162) or other non-current assets (499.22, FT 165). That bears on Q3, Q13 and Q14. | No "R041" to "R044", or lines 163-164 |
| R236-R237 | LG 83-85 | Board meeting from 05:20 PM to 06:30 PM, 70 minutes (FT 38). A2 raised it as a materiality flag (LG 143). | The timing bears on A4-OBS-1. The NSE file stamp NEOCHEM_27102026185320 (FT 20, R273) reads as 27-Oct-2026 18:53:20, 23 minutes after close [INFERENCE: stamp read as a timestamp]. | No "R236", "R237", "05:20", "06:30", or "minutes" |

A4 writes "363 of 363 structured IDs referenced" and "Unreviewed rows: none" (RV 19, RV 22). Both restate A2's count test; neither is a per-row disposition. Under the coverage rule each orphan is a FAIL that returns to A3. **Finding F1, MISSING, loop A3.**

### Missing from ledger

**None at the unit level.** The fresh pass did find content that A1 and A2 do not carry as rows: four blank-valued Schedule III labels, Annexure A sub-cell fragments, a signatory-initial variant, and intimation line-ref drift. None of it carries a value. Each blank line ties to nil, and the rest changes no number. They are logged as STYLE (S1, S5, S6, S7, S12), not as missing_from_ledger.

---

## 2. ARITHMETIC AUDIT

I recomputed every metric from FT values in Lakhs, then converted to Cr. Rounding tolerance: 0.01 Cr, 0.1 percentage point, or 1 bp when the inputs are rounded.

| Metric | A4 value (RV) | Recomputed (Lakhs unless stated) | Source line (FT) | Status |
|---|---|---|---|---|
| Op EBITDA H1 FY27 | 12.04 Cr (RV 125, 136) | 1,045.59 + 68.40 + 126.79 - 37.12 = 1,203.66 | 185, 193, 194, 197 | MATCH |
| Op EBITDA H2 FY26 | 11.26 Cr | 1,047.31 + 61.22 + 152.29 - 134.88 = 1,125.94 | same | MATCH |
| Op EBITDA H1 FY26 | 8.59 Cr | 732.83 + 63.17 + 198.23 - 135.03 = 859.20 | same | MATCH |
| Op EBITDA FY26 | 19.85 Cr | 1,780.14 + 124.39 + 350.52 - 269.91 = 1,985.14 | same | MATCH |
| Op EBITDA on reported PBT H2 FY26 / FY26 | 10.64 / 19.23 Cr (RV 126) | 1,064.06 / 1,923.25 | 201 | MATCH |
| Op EBITDA margin H1 FY26 / H2 FY26 / H1 FY27 / FY26 | 18.75 / 17.36 / 17.46 / 17.93% (RV 127) | 18.747 / 17.357 / 17.464 / 17.933% | 184 | MATCH |
| Reported EBITDA (four periods) | 9.94 / 11.99 / 12.41 / 21.93 Cr (RV 128) | 994.23 / 1,198.94 / 1,240.78 / 2,193.16 | 193, 194, 201 | MATCH |
| Reported EBITDA margin | 21.69 / 18.48 / 18.00 / 19.81% (RV 129) | 21.693 / 18.483 / 18.002 / 19.812% | 184 | MATCH |
| Gross margin | 35.82 / 30.12 / 30.70 / 32.48% (RV 130) | 1,641.47/4,583.16 = 35.815; 1,953.90/6,486.78 = 30.121; 2,116.12/6,892.43 = 30.702; 3,595.36/11,069.94 = 32.479% | 184, 188, 189 | MATCH |
| Core PBT ex-OI | 5.98 / 8.51 (9.12) / 10.08 / 14.48 (15.10) Cr (RV 131) | 597.80 / 850.55 (912.43) / 1,008.47 / 1,448.34 (1,510.23) | 185, 197, 201 | MATCH |
| OI / PBT | 18.43 / 13.69 / 3.55 / 15.71% (RV 132) | 18.426 / 13.687 / 3.550 / 15.709% | 185, 201 | MATCH |
| Total tax | 1.84 / 3.31 / 2.61 / 5.16 Cr (RV 114) | 184.44 / 331.14 / 260.90 / 515.59 | 203-206 | MATCH |
| ETR (ex true-up) | 25.17 / 33.60 (30.40) / 24.95 / 30.01 (28.17)% (RV 133) | 25.168 / 33.604 (30.396) / 24.953 / 30.007 (28.167)% | 201, 203-206 | MATCH |
| PAT margin | 11.97 / 10.09 / 11.38 / 10.86% (RV 134) | 11.965 / 10.086 / 11.385 / 10.864% | 184, 212 | MATCH |
| Implied weighted shares | 171.33 / 138.03 / 121.32 / 138.08 lakh (RV 56) | 784.69/4.58; 654.28/4.74; 548.38/4.52; 1,202.66/8.71 | 212, 214 | MATCH |
| H1 + H2 FY26 EPS; balancing H2 EPS | 9.26; 4.19 (RV 58) | 4.52 + 4.74 = 9.26; 8.71 - 4.52 = 4.19 | 214 | MATCH |
| Revenue YoY | +50.4% (RV 146) | 6,892.43 / 4,583.16 = 1.50386 | 184 | MATCH |
| Op EBITDA YoY | +40.1% (RV 147) | 1,203.66 / 859.20 = 1.40091 | derived | MATCH |
| Op EBITDA margin YoY | -129 bps (RV 148) | -128.3 bps unrounded; -129 bps from the rounded margins | derived | MATCH (rounding; S3) |
| D&A YoY / Finance cost YoY | +8.3% / -36.0% (RV 149-150) | 1.08279 / 0.63961 | 193, 194 | MATCH |
| EBIT (operating) YoY | 7.96 to 11.35 Cr, +42.6% (RV 151) | 796.03 to 1,135.26; 1.42615 | derived | MATCH |
| OI YoY | -72.5% (RV 152) | 37.12 / 135.03 = 0.27490 | 185 | MATCH |
| Core PBT YoY | +68.7% (RV 153) | 1,008.47 / 597.80 = 1.68697 | derived | MATCH |
| Reported PBT / PAT / EPS YoY | +42.7% / +43.1% / +1.3% (RV 154-156) | 1.42678 / 1.43092 / 1.01327 | 201, 212, 214 | MATCH |
| Gross margin YoY | -511 bps (RV 161) | 30.702 - 35.815 = -511.3 bps | derived | MATCH |
| Employee cost YoY | +3.5% (RV 161) | 421.05 / 406.72 = 1.03523 | 192 | MATCH |
| PPE / borrowings change | +55.3% / +85.9% (RV 164) | 3,092.68/1,991.32 = 1.55308; 3,308.13/1,779.35 = 1.85918 | 143, 149, 159 | MATCH |
| FY26 OI without a shown source | 2.57 Cr; 256.74; about 15% of PBT (RV 165, Q12) | 269.91 - 13.04 - 0.13 = 256.74; 256.74 / 1,718.25 = 14.94% | 185, 254, 255 | MATCH |
| HoH revenue | +41.5% / +6.3% (RV 179-180) | 6,486.78/4,583.16 = 1.41535; 6,892.43/6,486.78 = 1.06253 | 184 | MATCH |
| Run-rate vs FY26 half average | 55.35 Cr; +24.5% (RV 186) | 11,069.94 / 2 = 5,534.97; 1.24525 | 184 | MATCH |
| H1 PPE additions | about 11.76 Cr (RV 187) | 1,101.36 + 68.40 + 5.84 = 1,175.60 | 159, 194, 272 | MATCH |
| PAT bridge: revenue contribution | +8.27 Cr (RV 196) | 2,309.27 x 0.358151 = 827.07 | 184, derived | MATCH |
| PAT bridge: gross margin change | -3.52 Cr (RV 197) | 2,116.12 - 2,468.53 = -352.41 | derived | MATCH (0.01) |
| PAT bridge: other operating cost | -1.30 Cr (RV 198) | 912.47 - 782.27 = 130.20 | 191, 192, 195 | MATCH |
| PAT bridge: D&A / finance / OI | -0.05 / +0.71 / -0.98 Cr (RV 199-201) | 5.23 / 71.44 / -97.91 | 185, 193, 194 | MATCH |
| PAT bridge: tax at prior ETR / ETR change | -0.79 / +0.02 Cr (RV 202-203) | 312.76 x 0.251681 = 78.72; 263.16 - 260.90 = 2.26 | 201-206 | MATCH |
| PAT bridge: components vs PAT change | 236.29 vs 236.31 (RV 205) | 312.75 - 78.72 + 2.26 = 236.29; 784.69 - 548.38 = 236.31 | 212 | MATCH (0.02, stated by A4) |
| PAT bridge: % of PAT change | 350.0 / -149.1 / -55.1 / -2.2 / 30.2 / -41.4 / -33.3 / 1.0% | 349.99 / -149.13 / -55.10 / -2.21 / 30.23 / -41.43 / -33.31 / 0.96% | derived | MATCH |
| Operating items share of PBT change; finance; OI | 3.39 Cr = 108.5%; 22.8%; -31.3% (RV 209) | 339.22 / 312.76 = 108.46%; 22.84%; 31.30% | derived | MATCH |
| OI reversion PAT; core PAT ex-OI | +0.73 Cr to 8.58 Cr; 7.57 vs 4.47 Cr, +69.2% (RV 210) | 97.91 x 0.7505 = 73.48 (858.17); 756.86 vs 447.33 = 1.6919 | derived | MATCH |
| Borrowings rise; short-term part | 15.29 Cr; 10.57 Cr (RV 211) | 1,528.78; 1,057.00 | 143, 149 | MATCH |
| Other Expenses YoY | +35.7% (RV 213) | 418.73 / 308.57 = 1.35700 | 195 | MATCH |
| CFO / PAT | -1.41x / -0.13x (RV 224) | -1,693.78/1,202.66 = -1.4084; -105.25/784.69 = -0.1341 | 212, 267 | MATCH |
| Capex; multiple of FY26 | 2.95 / 14.45 Cr; 4.9x (RV 225) | 295.44 / 1,445.46; 4.893 | 273 | MATCH |
| FCF | -19.89 / -15.51 Cr (RV 226) | -1,989.22 / -1,550.71 | 267, 273 | MATCH |
| Working-capital change | -35.82 / -13.19 Cr (RV 227) | -3,582.06 / -1,318.69 | 257-265 | MATCH |
| H1 CFO bridge | -105.25 (RV 243) | 1,213.43 - 1,318.69 - 0.00 = -105.26 vs filed -105.25 | 256, 266, 267 | MATCH (0.01, stated by A4) |
| Receivable days | 127.8 / 136.7 / 160.7 (RV 228, 241) | 127.80 / 136.70 / 160.65 | 169, 184 | MATCH |
| Inventory days | 154.8 / 117.5 (RV 229) | 154.83 / 117.46 | 168, 188, 189 | MATCH |
| Payable days | 67.8 / 46.4 (RV 230) | 67.85 / 46.35 | 150, 188, 189 | MATCH |
| Cash conversion cycle | 207.8 to 214.8, +7.0 (RV 231) | 136.7 + 117.5 - 46.4; 127.8 + 154.8 - 67.8 | derived | MATCH |
| Net debt; short-term share | 17.61 to 32.90 Cr, +15.28; 83.6% (RV 234) | 1,761.25; 3,289.64; 1,528.39; 2,766.55/3,308.13 = 83.63% | 143, 149, 170 | MATCH |
| Debt / equity | 0.23 / 0.38 (RV 235) | 0.2257 / 0.3816 | 140, 143, 149 | MATCH |
| ST loans and advances | +8.02 Cr, 4.7x (RV 236) | 802.18; 1,019.20/217.02 = 4.696 | 171 | MATCH |
| ST provisions change vs H1 tax provision | +2.63 Cr = provision (RV 237) | 263.16 vs 263.15 | 154, 203 | MATCH |
| 18-month PAT vs CFO | 19.87 vs -17.99 Cr (RV 247) | 1,987.35 vs -1,799.03 | 212, 267 | MATCH |
| CFO if H1 tax were paid | -3.68 Cr (RV 248) | -105.25 - 263.15 = -368.40 | 203, 267 | MATCH |
| MSME share of payables | 65.7% (RV 230) | 1,162.79 / 1,770.76 = 65.67% | 150, 151 | MATCH |
| Cash on hand share | 97.5% (RV 74) | 18.03 / 18.49 = 97.51% | 288 | MATCH |
| ST advances share of WC outflow | 60.8% (RV 387) | 802.18 / 1,318.69 = 60.83% | 262 | MATCH |
| Inventory rise | +38.1% (RV 394) | 4,040.97 / 2,925.39 = 1.38134 | 168 | MATCH |
| Capex funded outside term debt | 67% (RV 456) | 1 - 471.78/1,445.46 = 67.36% | 273, 277 | MATCH |
| Filed trailing PE | PAT 14.39 Cr; 12.4x; 105/4.52 = 23.2 (RV 462) | 654.28 + 784.69 = 1,438.97; 179/14.39 = 12.44; 23.23. CMP and market cap are SECONDARY (screener), not in the extract. | 212, 214 | MATCH (inputs partly SECONDARY; S10) |
| Materials share of sales (brief) | about 69% (RV 492) | 4,776.31 / 6,892.43 = 69.30% | 188, 189 | MATCH |
| Pillar 1 inputs | EBIT 11.35 Cr; equity 86.69 Cr; borrowings 33.08 Cr (RV 342) | 1,135.26; 8,669.16; 3,308.13 | 140, 143, 149 | MATCH |

**Filing tie-outs behind A4's "arithmetic ties" statement (RV 119).** All hold within 0.01:
- Expense lines sum to Total Expenses: H1 FY27 5,883.97 exact; H2 FY26 5,574.34 vs 5,574.35 filed; H1 FY26 and FY26 exact (FT 188-196).
- Total revenue less total expenses = line V: H1 FY27 1,045.58 vs 1,045.59; other periods exact (FT 186, 196, 197).
- H1 FY26 + H2 FY26 = FY26 on every line, within 0.01 (cost of materials 7,357.28 vs 7,357.29; deferred tax -5.11 vs -5.10).
- PBT less tax = PAT: H2 FY26 654.29 vs 654.28; H1 FY26 548.39 vs 548.38; other periods exact (FT 201-212).
- Balance sheet: total equity and liabilities ties on both dates. Current liabilities tie exactly. Non-current liabilities 713.96 vs 713.95 and 238.33 vs 238.34. Non-current assets 4,378.02 vs 4,378.01. Shareholders' funds 7,884.48 vs 7,884.47 (FT 137-174).
- Reserves rose 784.68 (FT 138) against PAT 784.69 (FT 212). No dividend or other reserve movement.
- Capex reconciles to the cash flow: PPE net change 1,101.36 + D&A 68.40 + disposal 5.84 + CWIP change 269.74 + intangibles change 0.13 = 1,445.47, against purchase of fixed assets 1,445.46 (FT 159-161, 194, 272, 273).
- Non-current investments 625.00 less the H1 sale of 115.93 = 509.07 exactly (FT 162, 270).
- Cash: 18.10 + 0.39 = 18.49 (FT 284-286). Bank 0.46 + cash on hand 18.03 = 18.49 (FT 288-290).

**Result: zero mismatches above rounding. arithmetic_mismatches = [].**

---

## 3. ADVERSARIAL READ

I selected the three most positive claims in A4. Each bear counter below uses the same extracted text only.

### Claim 1. "Core PBT rose 68.7%; PAT understates core growth; the growth came from the business itself."
A4 locations: RV 153, RV 162 ("Headline PAT growth (+43.1%) understates core growth. The headline is real, not treasury-driven."), RV 478 ("Profit from operations alone rose faster, by 68.7% (FILED). Treasury income fell, so the growth came from the business itself."), RV 423 (Key Notes line), RV 589 (analyst note).

**Bear counter.** The 68.7% is PBT less other income, so it sits after interest. Finance costs fell 71.44 Lakhs, from 198.23 to 126.79 (FT 193). That is 17.4% of the 410.67 Lakh core PBT gain. The saving came from FY26 debt repayment funded by the share issue: equity +4,706.54 (FT 281); long-term borrowings -1,358.11 (FT 277); short-term borrowings -424.97 (FT 279). The same issue raised the weighted share count from about 121.3 lakh to 171.3 lakh and held EPS to +1.3% (FT 214). Without the financing effect, operating EBIT grew 42.6% (A4's own line, RV 151). That is in line with PAT (+43.1%) and below revenue (+50.4%). So PAT growth does not understate operating growth. The saving is also reversing: borrowings rose 85.9% in the half (FT 143, 149), and H1 FY27 drew 1,528.78 in new debt (FT 277, 279).

**Survives?** Yes. A4 states the finance-cost share in Step 4 (RV 209, "Lower finance costs add 0.71 Cr (22.8%)"). Its conclusions at RV 162 and RV 478 contradict its own EBIT line (RV 151). The operator reads the brief first, so the contradicted sentence leads. **Must be grafted. Finding F2, CONTRADICTION, loop A4.**

**Graft text (exact):**
- RV 478: replace "Profit from operations alone rose faster, by 68.7% (FILED). Treasury income fell, so the growth came from the business itself." with: "Operating profit before interest and other income rose 42.6% (FILED, derived). That matches the profit growth. Profit before tax without other income rose 68.7% (FILED, derived). About a sixth of that gain is lower interest (FILED). The FY26 share issue repaid debt, so interest fell. Debt is rising again, up 85.9% in the half (FILED)."
- RV 162: replace "Headline PAT growth (+43.1%) understates core growth. The headline is real, not treasury-driven." with: "71.44 Lakhs of the 410.67 Lakh core PBT gain (17.4%) is lower finance cost after the FY26 equity-funded debt paydown (FT 193, 277, 279, 281). Operating EBIT grew 42.6% (RV 151), in line with PAT (+43.1%) and below revenue (+50.4%). The headline is not treasury-driven. But 17.4% of core growth is a financing effect, and it is reversing (borrowings +85.9%, FT 143, 149)."
- RV 423 and RV 589: replace "core PBT +68.7%" with "operating EBIT +42.6% (core PBT +68.7% incl. a 0.71 Cr interest saving)".

### Claim 2. "Employee cost rose only 3.5% on 50.4% revenue growth, which recovered most of the gross margin loss / That operating leverage held the margin up."
A4 locations: RV 161, RV 492.

**Bear counter.** The leverage exists only against H1 FY26, the smallest half in the filing. Against the previous half, which comes after the share issue, it is absent:
- Gross margin rose 58.1 bps HoH (30.121% to 30.702%; FT 184, 188, 189).
- Operating EBITDA margin rose only 10.6 bps (17.357% to 17.464%).
- The gap is opex. (Manufacturing + employee + other expenses) / revenue rose 47.5 bps, from 12.764% (827.95 / 6,486.78) to 13.239% (912.47 / 6,892.43).
- The driver is Other Expenses, up 29.5% HoH (323.30 to 418.73, FT 195; +95.43 Lakhs) against revenue +6.3%. As a share of revenue it rose 109 bps (4.98% to 6.08%).
- A4 itself names Other Expenses as the likeliest P&L home of any expensed fraud loss (RV 213; Note 9, FT 238-239), but tests it only YoY (+35.7%).
- Employee cost (FT 192) carries none of the new CFO and CCO. Both start 27-Oct-2026 (FT 44, 47), after the period end. Their cost is NOT DISCLOSED.

**Survives?** Yes. A4 has no HoH opex test. Its forward step-ups name D&A and interest only (RV 164, RV 334), not employee cost. **Must be grafted. Finding F3, MISSING, loop A4.**

**Graft text (exact):**
- RV 161, append: "Sequentially (H2 FY26 to H1 FY27) the leverage is absent. Gross margin rose 58 bps, but operating EBITDA margin rose only 10.6 bps, because opex/revenue rose 47.5 bps. Other Expenses rose 29.5% HoH (323.30 to 418.73 Lakhs, FT 195) against revenue +6.3%. That +95.43 Lakhs is the likeliest home of any expensed fraud loss (Note 9). Employee cost (FT 192) excludes the CFO and CCO appointed from 27-Oct-2026 (FT 44, 47)."
- RV 492: replace "That operating leverage held the margin up." with: "That held the margin up against last year (FILED). Against the previous half, other expenses rose 29.5% while sales rose 6.3% (FILED). The new CFO and CCO start on 27-Oct-2026, so their pay is not in these numbers (FILED)."
- RV 334 [P-A21-3], append: "Employee cost also steps up from H2 FY27 (CFO and CCO from 27-Oct-2026; amount NOT DISCLOSED)."

### Claim 3. "Revenue +50.4% YoY, strong growth; H1 FY27 is the highest half; growth is real in the P&L."
A4 locations: RV 146, RV 160, RV 186, RV 478, RV 589.

**Bear counter.** Each period on file shows working capital absorbing the growth, and the receivables part of that is never quantified in A4:
- FY26 trade receivables rose 2,344.66 (FT 259). That is 65.5% of the FY26 working-capital outflow of 3,582.06 (FT 257-265), 21.2% of FY26 revenue (11,069.94, FT 184), and 1.95x FY26 PAT (1,202.66, FT 212).
- Bad debts are 0.00 in both periods (FT 251), and no provision line exists.
- Implied receivables at 31-Mar-2025 are 2,527.68 [derived from FT 169 and 259; assumes no write-off]. So receivables rose 92.8% in FY26.
- In H1 FY27, sequential revenue growth slowed to 6.3%. The cash drain moved to inventories (-1,115.58, FT 258) and ST advances (-802.18, FT 262).
- Total assets rose 27.1% in six months (11,711.52 to 14,886.73, FT 156). Annualised revenue / total assets fell from 1.11x (6,486.78 x 2 / 11,711.52) to 0.93x (6,892.43 x 2 / 14,886.73) [derived; doubles one half, seasonality unknown].

**Survives?** Yes. A4 shows the FY26 working-capital total (RV 227) and the receivable-day base spread (RV 228, RV 249), but not the receivables build. The build is the largest cash item in FY26 and bears directly on A4's "structural or growth-induced" test (RV 249). The HoH +6.3% is in Step 3 (RV 180, RV 184) but absent from the brief summary. **Must be grafted. Finding F4, MISSING, loop A4.**

**Graft text (exact):**
- RV 249, after "they sit high on either base.", insert: "FY26 working capital was receivables-led. Trade receivables rose 2,344.66 Lakhs (FT 259): 65.5% of the FY26 WC outflow of 3,582.06, 21.2% of FY26 revenue and 1.95x FY26 PAT. Bad debts were 0.00 and no provision line exists (FT 251). Implied 31-Mar-2025 receivables are 2,527.68 [derived, assumes no write-off], so receivables rose 92.8% in FY26. In H1 FY27 the drain moved to inventories (-1,115.58, FT 258) and ST advances (-802.18, FT 262). Total assets rose 27.1% in the half (FT 156) against revenue +6.3% HoH. Annualised revenue / total assets fell from 1.11x to 0.93x [derived]."
- RV 478, after "That is 50.4% more than a year earlier (FILED).", insert: "Against the previous half, sales rose only 6.3% (FILED)."
- RV 494, after "So each rupee of growth needs fresh funding.", insert: "In FY26, money owed by customers rose Rs 23.45 Cr, about twice that year's profit (FILED)."

### Mandatory acquisition-economics probe

**Not triggered as an acquisition.** The filing describes no acquisition, business purchase or stake buy. The nearest items:
- (a) An unnamed non-current investment bought for 625.00 in FY26 (FT 270, shown as negative "proceeds"; sign note R359). It was cut to 509.07 by an H1 FY27 sale of 115.93, at book, with profit on sale 0.00 (FT 162, 255, 270).
- (b) Capex of 1,445.46 (FT 273), with no capacity, cost or date.

Neither item has a named target, price, PAT, ROCE, debt or customer data. So price / target PAT is **NOT FOUND**, and no earnings multiple can be stated or stress-tested. The bear reading (an undisclosed and possibly related investee or borrower) already sits in A4 at Q13 and Q14 (RV 397-398), with related-party bear answers. No graft is needed. S8 logs the at-book exit and the implied yield as a sharper link between Q13 and Q14.

### Other positive claims considered and not selected
- "CFO deficit narrowed" (RV 223-224). A4 already counters it: payables stretch and nil tax paid (RV 248).
- "Receivable days improved 8.9 days" (RV 228). A4 shows the base sensitivity (RV 241, RV 249). The receivables counter is folded into Claim 3.
- "Unmodified review conclusion" (RV 81). A4 already caveats limited-review scope and the reviewer's silence on the fraud.

---

## FINDINGS REGISTER (typed)

| ID | Type | Finding | Evidence | Loop |
|---|---|---|---|---|
| F1 | MISSING | Three orphan ledger rows: R005-R006, R041-R044, R236-R237. None is cited or dispositioned in A4. | LG 46, 47, 85; FT 38, 139, 163-164; grep of review: zero hits | A3 |
| F2 | CONTRADICTION | Claim 1. RV 478 "Profit from operations alone rose faster, by 68.7%" and RV 162 "PAT growth understates core growth" contradict RV 151 (operating EBIT +42.6%, about equal to PAT +43.1%). 17.4% of the core PBT gain is interest saved by the FY26 equity-funded paydown. | FT 143, 149, 193, 214, 277, 279, 281 | A4 |
| F3 | MISSING | Claim 2. Sequential operating leverage is absent: Other Expenses +29.5% HoH vs revenue +6.3%; op EBITDA margin +10.6 bps on +58.1 bps gross margin. CFO and CCO cost from 27-Oct-2026 is not in H1. | FT 44, 47, 184, 188-195 | A4 |
| F4 | MISSING | Claim 3. FY26 receivables +2,344.66 = 65.5% of the FY26 WC outflow and 1.95x FY26 PAT, no provision; total assets +27.1% in H1 vs revenue +6.3% HoH. Absent from the review. | FT 156, 174, 184, 212, 251, 257-265 | A4 |
| F5 | MISSING | Dropped qualifier. The review report reads "the applicable Indian Accounting Standards ... or other applicable accounting standards, as the case may be" (FT 106-108), and its conclusion cites "the applicable accounting standards" (FT 123). A4 quotes only "Indian Accounting Standards" and calls it a framework conflict (RV 65, 403, 460, 554, 582). The wording covers an AS filer, which fits Note 2 (FT 224-226) and CF Note 1, AS 3 (FT 287). One of the "seven drafting inconsistencies" may not be one. | FT 106-108, 123, 224-226, 287 | A4 |
| F6 | FACTUAL | "CFO since 2018" (RV 452, RV 574) is not supported. Annexure A says "Associated with the Company since 2018" and "has overseen the financial management" (FT 84-86). The start of the CFO designation is not stated. | FT 84-86 | A4 |

**Exact fixes for F1, F5 and F6** (F2-F4 graft text is in Section 3):
- F1 (A3): give each orphan a disposition, then A4 carries it.
  - R005-R006: "reviewed, no finding". Nil warrants confirm no dilutive instrument and support RV 54.
  - R041-R044: "reviewed, no finding". No long-term loan asset exists. Loans given can sit only in ST loans and advances 1,019.20, non-current investments 509.07 or other non-current assets 499.22 (FT 162, 165, 171). This feeds Q3, Q13 and Q14.
  - R236-R237: finding or no finding at A3's call. The board met 70 minutes (FT 38). The NSE file stamp NEOCHEM_27102026185320 (FT 20) suggests filing at 18:53:20, 23 minutes after close [INFERENCE].
- F5 (A4):
  - RV 65: replace "The review report cites 'Indian Accounting Standards' (lines 106-107). Framework wording conflicts (A3-20a)." with: "The review report cites 'the applicable Indian Accounting Standards ... or other applicable accounting standards, as the case may be' (FT 106-108), and its conclusion cites 'the applicable accounting standards' (FT 123). The wording covers an AS filer and does not conflict with Note 2. CF Note 1 cites AS 3 (FT 287)."
  - Q19 (RV 403, RV 554): replace the first two sentences with: "Note 2 and CF Note 1 cite Indian GAAP and AS 3; the review report uses generic Ind AS-or-other wording. Please confirm the framework."
  - F-12 (RV 460, RV 582): re-count the A3-20 list without the Ind AS item, or state why it stays.
- F6 (A4): at RV 452 and RV 574, replace "CFO since 2018" with "with the company since 2018 (FT 84); start of CFO tenure NOT DISCLOSED".

None of F1-F6 changes A4's protocol verdict (PROCEED WITH FLAGS, RV 468). F2-F4 add bear weight to the cash and quality flags. F5 and F6 trim two governance overstatements.

---

## VERDICT

**INCOMPLETE.** Failing agent: **A3** (orphan rows, F1, MISSING). The same correction loop carries the A4 grafts F2 (CONTRADICTION), F3 (MISSING), F4 (MISSING), F5 (MISSING) and F6 (FACTUAL). Re-run order: A3 dispositions three rows, then A4 grafts F2-F6 and carries the dispositions, then A5 re-audits. Plain-language brief gate: PASS. Arithmetic: PASS, zero mismatches. Missing-from-ledger: none.

---

## STYLE NOTES (logged; no loop, no re-run)

- **S1.** Four blank-valued Schedule III labels are not enumerated by A1 or A2: FT 141 (share application money), 145 (other long-term liabilities), 200 (extraordinary items), 207 (MAT credit entitlement). Blank cells at FT 198 col 3 and FT 209-211 are also not enumerated. Each ties to nil: line VII = line IX in all periods; PBT less tax = PAT within 0.01; non-current liabilities and total equity and liabilities tie within 0.01. A2 could add a BLANK_AS_FILED row. No number changes.
- **S2.** The A2 ledger lists R176 in the cash flow non-zero range (R174-R187, LG 59) and also in the cash flow ZERO_STANDING row (LG 63). It lists R177 twice (LG 59). Cosmetic.
- **S3.** Op EBITDA margin YoY: A4 gives -129 bps from rounded margins. Unrounded it is -128.3 bps. Within rounding.
- **S4.** Forward map: four catalysts are "Undated" (RV 507-510). That is an honest NOT FOUND. Each could carry its first observable checkpoint (H2 FY27 inside the FY27 audited results, by 30-May-2027).
- **S5.** A1 line-ref drift; no value is affected. I001 is at IT 26 (row says 33). I003 is at IT 35 (says 36). I005 is at IT 102 (says 101). I009 is at IT 21-22 (says 20). R239 is at FT 49 (says 48). R247 is at FT 85 (says 84). The R335 quote is at FT 117 (row says 95).
- **S6.** Some Annexure A fragments exist only in the fulltext: Nair's end markets (FT 82-83); Shah's sectors and SAP work (FT 78-79); Solanki "has overseen the financial management" (FT 85-86); no term stated for any person (FT 73-74). A4 cited the fulltext directly. The ledger's Annexure row also lists R284 (MD Makati), who is not in Annexure A.
- **S7.** The balance-sheet signatory reads "Swapnil B. Makati" (FT 175). Elsewhere it reads "Swapnil R Makati" (FT 216, 240, 291) and "SWAPNIL RAMESHBHAI MAKATI" (FT 63). A4 does not mention it. It may be a connector rebuild artefact. Check it with the F-01 NSE verification, and add it to the A3-20 list if confirmed.
- **S8.** The non-current investment exit was at book: 625.00 - 115.93 = 509.07 exactly, with profit on sale 0.00 (FT 162, 255, 270). H1 interest income of 27.34 (FT 254) is about 9.6% annualised on the average holding of 567.04 [INFERENCE]. Q13 and Q14 could name the investment and other non-current assets (499.22, FT 165) as candidate interest sources.
- **S9.** Competition brief (RV 500): "from a larger player" sits outside the [INFERENCE] tag. Indofil's size is not in the filing.
- **S10.** F-14 (RV 462): 105 / 4.52 uses the H1 FY26 EPS, the oldest half. The latest half gives 105 / 4.58 = 22.9x. Neither reproduces 23.3. The filed trailing PE of 12.4x stands. The "single half-year EPS" inference is weak and could say so.
- **S11.** Auditor paragraphs: A5 counts 8 units (signature block FT 127-129 separate); A2 counts 7. Definitional only; every unit maps to ledger rows.
- **S12.** Intimation: the Zoom platform (IT 42) and the host domain atlascapital.in (IT 100-102) are not entity rows. The invitation names the host "NeoAtlas Capital Advisory LLP" (IT 78). Immaterial.

---

## RE-AUDIT LOOP 1 (2026-10-29; the one permitted iteration)

**Scope.** This pass re-audits the patched A4 review (632 lines) against F1-F6, then runs a drift check over every line. The inputs are the same as before: the A1 fulltexts and structured files, and the A2 ledger. I did not read the A3 forensics. I checked A3's loop-1 dispositions as A4 carries them. A fresh grep of the results fulltext confirms the cited lines are unchanged: FT 20, 38, 44, 47, 73-74, 84, 108, 123, 139, 156, 164, 169, 195, 251, 259.

Cite key: RV' = patched review line. RV = first-pass review line.

### Finding status

| Finding | Type | Fix location (RV') | Check at fulltext lines | Status |
|---|---|---|---|---|
| F1 | MISSING | 22-25; carried at Q3 (390), Q13 (400), YAML 561, 571 | R005-R006 "reviewed, no finding": FT 139 nil on both dates; FT 214-215 basic = diluted; FT 137 share capital 1,712.08 on both dates. R041-R044 "finding, carried" (A3-20 item b; A3-02): FT 163-164 nil; FT 144 liability-side net DTL 52.81 / 55.06; candidate loan homes 1,019.20 (FT 171), 509.07 (FT 162), 499.22 (FT 165). R236-R237 "reviewed, no finding": FT 38, 05:20 to 06:30 PM; file stamp at FT 20; the 23-minute gap is tagged [INFERENCE]. Every ledger row is now cited or dispositioned. | RESOLVED |
| F2 | CONTRADICTION | 165, 426, 481, YAML 614 | FT 193: 198.23 to 126.79 = 71.44; 71.44 / 410.67 = 17.4%. FT 277, 279, 281 show the paydown and the issue. FT 143, 149: borrowings +85.9%. RV' 165 and RV' 481 now agree with RV' 154 (operating EBIT +42.6%). The Key Notes line (RV' 426) leads with operating EBIT. Grep finds no "operations alone" and no "understates core" outside the change log. RV' 156, "Grew faster than reported PBT", stays and is true (68.7% vs 42.7%). | RESOLVED |
| F3 | MISSING | 164, 337, 495, YAML 611 | FT 195: 323.30 to 418.73 = +29.5%, +95.43. Opex ratio 827.95 / 6,486.78 = 12.76% to 912.47 / 6,892.43 = 13.24%, so +47.5 bps. Gross margin +58.1 bps; op EBITDA margin +10.6 bps. FT 44 and 47: hires from 27-Oct-2026. The fraud-home sentence carries [INFERENCE]. | RESOLVED |
| F4 | MISSING | 252, 481, 497, YAML 612 | FT 259: 2,344.66, which is 65.5% of 3,582.06, 21.2% of 11,069.94 and 1.95x 1,202.66. FT 251: bad debts 0.00. 2,527.68 and +92.8% are tagged derived, with a no-write-off caveat. FT 156: total assets +27.1%. Turnover 1.11x to 0.93x, tagged derived with a seasonality caveat. | RESOLVED |
| F5 | MISSING | 68, 406, 463, YAML 577, 605 | FT 106-108 qualifier now quoted; FT 123 conclusion wording quoted; FT 287 AS 3 cited. The drafting count reads six at RV' 406, 463 and 605, consistent with "items b to g". Grep finds no residual "seven" outside the change log. | RESOLVED |
| F6 | FACTUAL | 455, YAML 597 | FT 84: "Associated with the Company since 2018". CFO tenure start is stated as NOT DISCLOSED. Grep finds no residual "CFO since 2018". | RESOLVED |

### Drift check

**Method.** I compared the patched review line by line against the first-pass review. Two offsets apply: +3 lines after RV' 25, and the change-log insert at RV' 520-537.

**Lines that changed:** 22-25, 68, 164, 165, 252, 337, 390, 400, 406, 426, 455, 463, 481, 495, 497; the change log (520-537); and YAML 561, 571, 577, 597, 605, 611, 612, 614 and 616-630.

**Lines that did not change:** every other line. That includes:
- Step 1, the derived-metrics table, and the Step 3, 4 and 5 tables.
- Steps 5.5, 6, 7 and 8.
- Q1-Q2, Q4-Q12, Q14-Q18 and Q20-Q21.
- The monitorables, flags F-01 to F-03, F-05 to F-11 and F-13 to F-16, and the protocol verdict.
- The sector, competition and forward-map sections of the brief.

**Result.** No extraction number or derived number moved. Every new number in the changed lines recomputes from the fulltext (see the fix table). The protocol verdict PROCEED WITH FLAGS, cash conversion INDETERMINATE-WITH-DIRECTION and branch 8A-W are unchanged. **No new FACTUAL, MISSING or CONTRADICTION finding.**

**Brief gate re-check.** All five parts are present. The summary narrative is now about 275 words, about 18 rendered lines, still inside the 10-20 line spec.

### New STYLE notes (logged; no loop)

- **S13.** The change log's Fix 7 row (RV' 532) lists the YAML Q13 edit but not the YAML Q3 edit (RV' 561, "LT loans line nil"). The edit itself is correct (FT 164).
- **S14.** Two provenance tags in the brief: "About a sixth of that gain is lower interest (FILED)" (RV' 481) and "about twice that year's profit (FILED)" (RV' 497). Both are derived ratios, so "(FILED, derived)" matches the brief's own convention. This tag came from A5's own graft text.
- **S15.** "Any loan given can sit only in ST loans and advances, non-current investments or other non-current assets" (RV' 24; same list at Q13, RV' 400). This repeats A5's own F1 wording. Other current assets (616.57, FT 172) is a fourth possible home in a loose SME presentation. No number changes.
- **S16.** A4 withdrew A3-20 item (a) at the A4 layer (RV' 68, 530). If the A3 forensics record still lists item (a), align it at the next A3 pass. The A3 file is not an A5 input, so I have not verified this.
- **S1-S12.** A4 actioned none of them. Each stays logged.

### Loop 1 verdict

**COMPLETE.** F1-F6 are resolved. Drift: clean. No new FACTUAL, MISSING or CONTRADICTION finding. Four new STYLE notes (S13-S16) are logged without a loop. loop_back_to: "". The review may proceed to the Notion save step.

---

```yaml
stage: A5-adversary
company: "NEOCHEM"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
verdict: INCOMPLETE   # initial audit verdict; loop_1.verdict governs after correction loop 1
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows:
    - "R005-R006 (ledger line 46): share warrants nil both dates, fulltext line 139; not cited or dispositioned in A4"
    - "R041-R044 (ledger line 47): asset-side DTL and Long Term loans and advances nil both dates, fulltext lines 163-164; not cited or dispositioned in A4"
    - "R236-R237 (ledger line 85): board meeting 05:20 PM to 06:30 PM, fulltext line 38; A2 materiality flag; not cited or dispositioned in A4"
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "Core PBT +68.7%; PAT understates core growth; growth came from the business itself (review lines 162, 423, 478, 589)"
    counter: "17.4% of the 410.67 Lakh core PBT gain is a 71.44 Lakh interest saving from the FY26 equity-funded debt paydown, the same issue that held EPS to +1.3%; operating EBIT grew 42.6% (review line 151), in line with PAT +43.1% and below revenue +50.4%; borrowings since rose 85.9%"
    source_line: "results fulltext lines 143, 149, 193, 214, 277, 279, 281"
    type: CONTRADICTION
  - claim: "Employee cost +3.5% on revenue +50.4%: operating leverage held the margin up (review lines 161, 492)"
    counter: "Sequentially the leverage is absent: Other Expenses +29.5% HoH (323.30 to 418.73) vs revenue +6.3%; opex/revenue +47.5 bps; op EBITDA margin +10.6 bps on +58.1 bps gross margin; CFO and CCO cost from 27-Oct-2026 not yet in H1"
    source_line: "results fulltext lines 44, 47, 184, 188-195"
    type: MISSING
  - claim: "Revenue +50.4% YoY, strong growth; growth is real in the P&L (review lines 146, 160, 478, 589)"
    counter: "FY26 receivables rose 2,344.66 Lakhs (65.5% of the FY26 WC outflow, 21.2% of FY26 revenue, 1.95x FY26 PAT) with bad debts 0.00 and no provision; H1 FY27 HoH growth 6.3% while total assets rose 27.1%; annualised revenue/total assets 1.11x to 0.93x"
    source_line: "results fulltext lines 156, 174, 184, 212, 251, 257-265"
    type: MISSING
findings_by_type:
  factual:
    - "F6: 'CFO since 2018' (review lines 452, 574) not supported; fulltext lines 84-86 say associated with the company since 2018; start of CFO tenure NOT DISCLOSED. Loop A4."
  missing:
    - "F1: orphan ledger rows R005-R006, R041-R044, R236-R237 not cited or marked reviewed, no finding in A4. Loop A3."
    - "F3: Claim 2 counter (sequential opex +47.5 bps; Other Expenses +29.5% HoH; senior hires after period end) absent from review. Loop A4."
    - "F4: Claim 3 counter (FY26 receivables +2,344.66 Lakhs = 1.95x FY26 PAT, no provision; total assets +27.1% vs revenue +6.3% HoH) absent from review. Loop A4."
    - "F5: review report qualifier 'or other applicable accounting standards, as the case may be' (fulltext line 108) dropped; review lines 65, 403, 460, 554, 582 call it a framework conflict. Loop A4."
  contradiction:
    - "F2: review line 478 'Profit from operations alone rose faster, by 68.7%' and line 162 'PAT growth understates core growth' contradict review line 151 operating EBIT +42.6%. Loop A4."
  style:
    - "S1: blank-valued Schedule III labels (fulltext lines 141, 145, 200, 207) not enumerated; each ties to nil"
    - "S2: ledger lists R176 in both CF non-zero and ZERO_STANDING rows; R177 listed twice"
    - "S3: op EBITDA margin YoY -129 bps from rounded margins; unrounded -128.3 bps"
    - "S4: four forward-map catalysts undated; add first observable checkpoint"
    - "S5: A1 line-ref drift on I001, I003, I005, I009, R239, R247, R335; no value affected"
    - "S6: Annexure A sub-cell fragments only in fulltext; ledger Annexure row lists R284 (not in Annexure A)"
    - "S7: BS signatory 'Swapnil B. Makati' (line 175) vs 'Swapnil R Makati' (lines 216, 240, 291); verify with NSE original"
    - "S8: investment exit at book (625.00 - 115.93 = 509.07, zero profit); interest 27.34 about 9.6% annualised on average holding [INFERENCE]; link Q13 and Q14"
    - "S9: 'from a larger player' (review line 500) sits outside the INFERENCE tag"
    - "S10: F-14 inference uses H1 FY26 EPS 4.52; latest half gives 22.9x; neither gives 23.3; filed 12.4x stands"
    - "S11: auditor paras 8 units (A5) vs 7 (A2); definitional"
    - "S12: intimation Zoom platform and atlascapital.in domain not entity rows; immaterial"
loop_back_to: "A3"   # initial audit; loop_1.loop_back_to governs after correction loop 1
gap: "A3: disposition three orphan ledger rows absent from A4: R005-R006 (share warrants nil, fulltext line 139), R041-R044 (asset-side DTL and LT loans and advances nil, lines 163-164), R236-R237 (board meeting 05:20-06:30 PM, line 38). Same loop, A4 then grafts: F2 CONTRADICTION, align review lines 162, 423, 478, 589 with line 151 (operating EBIT +42.6%; 71.44 of the 410.67 Lakh core PBT gain is FY26 equity-funded interest saving, now reversing); F3 MISSING, add sequential opex test (Other Expenses +29.5% HoH, line 195; margin +10.6 bps on +58.1 bps gross margin; CFO and CCO cost from 27-Oct-2026); F4 MISSING, add FY26 receivables build 2,344.66 Lakhs (line 259) = 65.5% of FY26 WC outflow, 1.95x FY26 PAT, no provision (line 251); F5 MISSING, restore 'or other applicable accounting standards, as the case may be' (line 108) at review lines 65, 403, 460; F6 FACTUAL, replace 'CFO since 2018' at review lines 452, 574 with 'with the company since 2018 (line 84); CFO tenure start not disclosed'. Exact graft text is in the audit file."
style_notes:
  - "S1 blank Schedule III labels nil by tie-out; A2 may add BLANK_AS_FILED row"
  - "S2 ledger R176/R177 double listing"
  - "S3 -129 vs -128.3 bps rounding"
  - "S4 undated catalysts could carry first checkpoint"
  - "S5 A1 line-ref drift, values unaffected"
  - "S6 Annexure fragments fulltext-only; R284 misfiled in Annexure row"
  - "S7 signatory initial B vs R; verify against NSE original"
  - "S8 investment exit at book and implied yield; link Q13 and Q14"
  - "S9 Indofil size claim outside INFERENCE tag"
  - "S10 F-14 PE inference weak; filed 12.4x stands"
  - "S11 auditor paragraph unit definition"
  - "S12 intimation minor entities"
analyst_note: "Arithmetic is clean. I recomputed every derived metric in A4 from the fulltext and found no mismatch above rounding; capex ties to 0.01 Lakhs once CWIP and intangibles are added. The failures are coverage and framing. Three ledger rows carry no citation or disposition in A4: share warrants nil, long-term loans and advances nil, and the board meeting times. The rule sends orphans to A3; the fix is three disposition lines. The larger issue is A4's lead positive claim. 'Profit from operations alone rose 68.7%' contradicts A4's own EBIT line of +42.6%. 17.4% of the core PBT gain is interest saved by the FY26 equity issue, the same issue that held EPS to +1.3%, and borrowings have since risen 85.9%. Against the previous half, operating leverage is absent: other expenses rose 29.5% while sales rose 6.3%. FY26 receivables rose 2,344.66 Lakhs, about twice FY26 PAT, and A4 never states it. The Ind AS 'conflict' drops the report's 'or other applicable accounting standards' hedge. None of this moves PROCEED WITH FLAGS. It changes what the operator reads first. Blank Schedule III lines are STYLE because every subtotal ties to nil."
loop_1:
  date: "2026-10-29"
  status: complete
  verdict: COMPLETE
  review_audited: "runs/neochem-q2fy27/work/review_neochem_q2fy27.md (patched, 632 lines; change log lines 520-537)"
  plain_language_brief: "all five parts present; narrative about 275 words, about 18 rendered lines"
  findings_status:
    - id: F1
      type: MISSING
      status: resolved
      review_lines: "22-25; carried at 390 (Q3), 400 (Q13), yaml 561, 571"
      check: "fulltext lines 38, 137, 139, 144, 162-165, 171, 214-215 hold; every ledger row now cited or dispositioned"
    - id: F2
      type: CONTRADICTION
      status: resolved
      review_lines: "165, 426, 481, yaml 614"
      check: "fulltext line 193 gives 71.44 = 17.4% of 410.67; brief and Diag 3 now agree with operating EBIT +42.6% (review line 154)"
    - id: F3
      type: MISSING
      status: resolved
      review_lines: "164, 337, 495, yaml 611"
      check: "fulltext line 195 gives +29.5% HoH; opex ratio +47.5 bps; hires at lines 44, 47; fraud-home sentence tagged INFERENCE"
    - id: F4
      type: MISSING
      status: resolved
      review_lines: "252, 481, 497, yaml 612"
      check: "fulltext lines 156, 251, 259 hold; derived items carry caveats"
    - id: F5
      type: MISSING
      status: resolved
      review_lines: "68, 406, 463, yaml 577, 605"
      check: "fulltext lines 106-108, 123, 287 quoted; drafting count six everywhere; no residual 'seven' outside change log"
    - id: F6
      type: FACTUAL
      status: resolved
      review_lines: "455, yaml 597"
      check: "fulltext line 84 quoted; CFO tenure start NOT DISCLOSED; no residual 'CFO since 2018'"
  arithmetic_mismatches: []
  drift_check: "clean. Only logged lines changed, plus one unlogged but correct YAML Q3 edit (review line 561). No extraction or derived number moved. Protocol verdict, cash conversion and branch unchanged."
  new_findings_by_type:
    factual: []
    missing: []
    contradiction: []
    style:
      - "S13: change log Fix 7 (review line 532) omits the YAML Q3 edit at line 561; edit correct (fulltext line 164)"
      - "S14: derived ratios at review lines 481 ('about a sixth') and 497 ('about twice') tagged FILED; 'FILED, derived' fits the brief convention (A5's own graft wording)"
      - "S15: 'loan can sit only in' list (review lines 24, 400) omits other current assets 616.57 (fulltext line 172); A5's own F1 wording"
      - "S16: A4 withdrew A3-20 item (a) at A4; align the A3 record at the next A3 pass (not verified; A3 not an A5 input)"
  loop_back_to: ""
  gap: ""
  style_notes:
    - "S13 change log omits YAML Q3 edit"
    - "S14 two derived ratios tagged FILED"
    - "S15 loan-home list omits other current assets"
    - "S16 A3 record may still carry A3-20(a)"
    - "S1-S12 not actioned; stay logged"
  analyst_note: "All six findings are fixed at the review lines I named. Each fix checks against the unchanged fulltext. A4 changed only the lines it logged, plus one correct but unlogged edit to YAML Q3. No number in Steps 1 to 8 moved. The Key Notes line now leads with operating EBIT +42.6% and keeps core PBT +68.7% with its interest share stated. The drafting count is six. What remains is style: two derived ratios carry a FILED tag, and my own F1 wording on where a loan can sit leaves out other current assets. Verdict COMPLETE. The protocol verdict PROCEED WITH FLAGS is unchanged."
```
