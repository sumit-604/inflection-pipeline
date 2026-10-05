# VERIFIER A: NUMERICAL ACCURACY, AVANA, run 2026-10-05 (B12a)

Model claude-sonnet-5-5. Fresh context. Inputs: stage reports 01-gate0, 02-notes (pass1, pass2, consolidation), 03-ardeep, 04-bizmodel, 05-concall, 06-peers, 07-emoat, 08-promoter, 09-tam, and blocks B00 to B09. Sources: AR FY26 text (pp.99-127 are transcriptions), RHP text, results re-filing text, announcements, SHP XBRL, screener sheets (AVANA, DANISH, SPCL, MARINE), DANISH transcripts, SPCL deck.

Units: lakh in AR, RHP and results; Cr in screener. Conversions at 100 lakh = 1 Cr were checked and are not counted as findings.

## Result in one line

0 CRITICAL, 5 MAJOR, 7 MINOR. All 32 mandatory-tier Gate 0 scorecard inputs tie to source. Every finding below is a source-fidelity finding and stands until the source PDF clears it.

## Findings table

| # | Severity | Report location | Claimed (anchor) | Source truth (location) | Note |
|---|---|---|---|---|---|
| 1 | MAJOR | 03-ardeep.md Phase 3C, margin waterfall bullet | Travelling expenses fell 18.89 (AR p116) | 86.36 to 65.47 = fall of 20.89 (AR p116, Note 24). 02-notes-pass1 12c prints 20.89. | Subtraction slip. Not a verdict-card or pillar input, so MAJOR. Other movers in the sentence tie. |
| 2 | MAJOR | 08-promoter.md 2C | "The FY26 AR lists contingent items of Rs 9.97 Cr" | FY26 = 679.22 lakh = Rs 6.79 Cr (481.42 + 196.16 + 1.64; AR p119, Note 25 item 3). Rs 9.97 Cr (996.52 lakh) is the FY25 comparative. | Year label wrong. FY26 figure is Rs 3.18 Cr lower. |
| 3 | MAJOR | B00-inputs.yaml LBF4 | H1 stub "Rs 36.28 Cr revenue" | Revenue from operations 3,574.71 lakh = Rs 35.75 Cr (RHP p72, p226). 3,628.32 lakh = Rs 36.28 Cr is total income. | Basis mislabel carried from the step-1 brief. Later stages use 3,574.71 correctly. |
| 4 | MAJOR | 02-notes-pass1.md section 4, concentration bullet | Top-5 38.79% (H1 FY26) vs 22.42% (FY25), "RHP p.12056" | Values are in RHP p38 and p169-170. Page 12056 does not exist. | Figures right, sole anchor invalid. LBF2 is load-bearing, so ANCHOR NOT FOUND is MAJOR. |
| 5 | MAJOR | 09-tam.md 3C and B09 input_gaps | 886 vs 600 panels "AR p74"; capacity 600/70,000 and 1,500/1,75,000 "RHP p105" | 886 and 62,034: AR p85. AR p74 is the ratio table. Capacity figures: RHP p104. | Values match B03, B04, B07. Anchors off. Feeds FLAG-CAPACITY. |
| 6 | MINOR | 01-gate0.md E2; B01 data_notes | 100% promoter holding "31-Dec-2023" (RHP p.92) | RHP p92: 100% "as on December 31, 2025, the date of this RHP" | Value and -26.36pp correct. Date label wrong. Score unaffected. |
| 7 | MINOR | 01-gate0.md Data notes | CFO 676.66, PAT 831.23 "(RHP p.290, p.32)" | Both at RHP p290. PAT also at p31, not p32. | Primary anchor holds. |
| 8 | MINOR | 01-gate0.md Block B note; B01 data_notes | RHP projected 205 days vs computed 136.5 | 136.5 is revenue basis. RHP 205 is cost-of-goods basis (RHP p113 text). Like-for-like 176.8 (B03 3B). | Unlabelled basis in the comparison sentence. No score touched. |
| 9 | MINOR | 06-peers.md Q3 | DANISH IPO "100% completed" (May-26 page 4) | May-2026 transcript page 5 | Quote exists one page later. |
| 10 | MINOR | 08-promoter.md and B08 | "RHP p.21283 region"; "AR pp.2397-2417 region"; "printed p.211" for promoters not related; RF35 "txt page 54" | Pages 21283 and 2397-2417 do not exist. Not-related line is pdf p217 = printed p212. RF35 is pdf p53. | Facts exist; anchors wrong or off by one. |
| 11 | MINOR | 09-tam.md Method 3; B09 | Aartech FY25 revenue Rs 39.33 Cr ("web") | RHP p119, p122: 3,635.22 lakh = Rs 36.35 Cr | Unanchored web figure that conflicts with the filed figure, no basis label. Feeds peer floor only. |
| 12 | MINOR | 05 1A; 07 4B; 08; 09 5D; B09 | Approximate anchors ("p~36-40 region", "line ~10682", "p~190", "p~14") | Order book 5,223.65 is at RHP p49 and p172. FX 88.79 at RHP line 1703. | Values exist in the RHP. Anchors are regions, not pages. |

## Struck before emit (rule 5b), 7 rows

1. 03 "275.83 = 32.4% of 850.00": true value 32.45%. Rounding, cosmetic.
2. Gate 0 gross margin 40.62% vs 03 40.61%: screener 2-decimal Cr rounding vs lakh. Basis, labelled.
3. 09 FY23-FY26 revenue CAGR 43.5% vs Gate 0 43.4%: 43.45% on either set of rounded inputs.
4. 08 FII 1.10% and DII 8.54% labelled "media": both match the SHP XBRL (FPI Cat I 0.011, domestic institutions 0.0854). Tier label only.
5. Gate 0 FY25 total assets 4,838.69 vs AR 4,838.68: Gate 0 cites results p11, which prints 4,838.69. Faithfully transcribed.
6. Gate 0 FY23 EBITDA margin 6.72% vs RHP 6.76%: screener rounded Cr vs RHP lakh. Basis.
7. 07 FY25 headcount 121 vs RHP PF table 117: year-end headcount (RHP p176 attrition table, line 12657) vs EPFO-registered count. Different measures.

## What was checked and tied (no finding)

- Gate 0: all 84 screener cells in the source table (AVANA FY20-FY26, 12 lines) match the Data_Sheet. ROCE rows (7), ROE rows (7), median ROCE 17.79%, median ROE 13.79%, EBITDA margins FY20-FY26, all CAGRs (24.5%, 45.8%, 43.4%, 8.0%), cumulative CFO 15.59 and PAT 27.02, capex 13.76 / 213.02 / 23.47 / 750.23 lakh, FCF row, WC day rows (payables 575.65, 676.29, 927.17, 1,328.84 lakh), D1-D4, E1, E3, E4 (679.22 / 5,908.03 = 11.50%), the peer margins and GM proxies from the three peer sheets (DANISH 17.73% / 26.8%, SPCL 12.12% / 23.99%, MARINE 10.77% / 29.51%), market caps, FAT 15.8x and 8.4x with CWIP, receivable-day moves (74.4 to 96.7), H1 and H2 margin split (870.11 on 4,811.17 = 18.1%; 762.61 on 3,574.71 = 21.3%), WC certificate lines.
- 02 and 03: balance sheet, P&L and cash flow lines (AR p99-102), Notes 2-25 totals and roll-forwards, receivable ageing, inventory, warranty roll (431.99 + 41.81 - 151.65 = 322.15), IPO utilisation table, IPO expense apportionment arithmetic, related-party table (476.03), contingent items, ratio note recomputations (ROCE 27.98% on long-term debt, payable turnover 2.55 on the sum), Board attendance (9 of 19), median pay and CEO ratios, FY27 pay proposals (8.33 + 6.21 + 7.67 + 6.26 = 28.47 a month = 341.64), RHP-vs-AR restatement gaps (103.44, 35.04, 76.02 vs 60.17).
- 04 and 07: RHP mix, channel and state tables, repeat-customer and order-book figures, unit economics arithmetic, incremental margin, R&D, headcount and attrition, FAT arithmetic (205.8% and 245.3%), +114% capacity ceiling.
- 05 and 06: guidance rows against RHP and BO19Aug text, peer sheet ratios (days, growth, CFO, borrowings), DANISH and SPCL page-level quotes (about 25 of them).
- 08: shareholding, lock-in, AIF 6,75,000 (2.98%), GST order 14.67 lakh split, RPT shares of PAT and revenue, IPO and OFS arithmetic.
- 09: FX conversions (all USD to Rs Cr lines), TAM and SAM arithmetic, SOM and CAGR arithmetic, capacity cross-check arithmetic.

## Coverage statement

Mandatory tier: 32 of 32 checked. The tier is the 32 Gate 0 scorecard inputs (A1-A4, B1-B4, C1-C4, D1-D4, E1-E4, M1-M12). Each was re-derived from its source cells. No verdict card and no Section 1B pillar section exist in the reports in front of me (stages 10, 11 and 13 have not run), so those two sub-tiers hold zero figures. No mandatory figure was skipped for a missing source.

Sample tier: about 1,050 material figures counted in the reports. Rule: a figure is material if it feeds a flag, a score, a table cell or a judgment sentence, counted once per distinct value. 640 were checked (60%), in the order Gate 0 and LBF inputs, 03 notes and ratios, 02 passes, 04 and 07 RHP tables, 05 guidance rows, 06 peer ratios and quotes, 08 promoter and RPT figures, 09 TAM arithmetic.

Not checkable from the inputs (about 45 figures): web vendor and government market sizes in 09 (MnM, Ken, Straits, IMARC, CEA/loktej, JMK, ICICI Direct, PIB NEP-T ckm and GVA, InVed); media figures in 08 (chittorgarh, Glassdoor, businesstoday LTP); MARINE deck financial slides (images). These are named, not skipped silently. They are not in the mandatory tier.

Reading limits: AR pp.99-127 are transcriptions of page images and the original results PDF is scanned. I read the text files. Damaged OCR digits were settled by tie-outs across documents (other income 97.01 in the OCR vs 97.21 in the AR; total income 8,483.09 ties to 97.21). I did not reopen page images; no finding rests on a digit I could not tie.

Acceptance rate: 640 checked, 23 flawed figures (3 value mismatches, 20 anchor or basis defects), 617 clean = 96.4%.

## Gate note

Findings 1 to 12 are source-fidelity findings. Findings 1 to 5 and 6, 7, 9, 10 carry `source_fidelity: true`. Findings 8, 11 and 12 are weak-anchor or unlabelled-basis items marked `source_fidelity: false`. There is no CRITICAL, so Verifier A does not trigger REWORK under OR-29. The acceptance rate is above 60% on a denominator of 640.

```yaml
stage: B12a
company: "AVANA"
run_date: "2026-10-05"
model: claude-sonnet-5-5
status: complete
numbers_checked: 640
mandatory_checked: 32
mandatory_total: 32
findings:
  - {severity: "MAJOR", location: "03-ardeep.md Phase 3C P&L line walk (margin waterfall bullet)", claimed: "travelling expenses fell 18.89 (AR p116)", source_truth: "travelling expenses 86.36 (FY25) to 65.47 (FY26) = fall of 20.89 (AR p116, Note 24; 02-notes-pass1.md 12c prints 20.89 correctly)", note: "Subtraction error in lakh. Not a verdict-card or pillar input, so MAJOR not CRITICAL. The other movers in the same sentence tie (marketing 30.44, legal 23.95, sales promotion 20.19, freight 47.45, labour 47.16).", source_fidelity: true}
  - {severity: "MAJOR", location: "08-promoter.md 2C Tax and revenue (second sentence of the FY26 AR contingent-items remark)", claimed: "FY26 AR lists contingent items of Rs 9.97 Cr", source_truth: "FY26 contingent total is 679.22 lakh = Rs 6.79 Cr (481.42 + 196.16 + 1.64, AR p119 Note 25 item 3). Rs 9.97 Cr (996.52 lakh) is the FY25 comparative column.", note: "Year mislabelled. The correct FY26 figure is lower by Rs 3.18 Cr. The 0.35 Cr drop quoted beside it is FY25 AR 996.52 vs FY25 RHP 1,031.56 (RHP p33), so the sentence mixes years.", source_fidelity: true}
  - {severity: "MAJOR", location: "B00-inputs.yaml load_bearing_facts LBF4", claimed: "H1 stub = Rs 36.28 Cr revenue", source_truth: "H1 FY26 revenue from operations 3,574.71 lakh = Rs 35.75 Cr (RHP p72 and p226; RES p10 H1 column). 3,628.32 lakh = Rs 36.28 Cr is TOTAL INCOME including other income 53.61.", note: "Basis mislabel (total income called revenue). Origin is the step-1 brief carried into B00 without a verbatim-quote mark. Downstream stages use 3,574.71 correctly. H1 PAT 5.61 Cr matches (560.74 lakh).", source_fidelity: true}
  - {severity: "MAJOR", location: "02-notes-pass1.md section 4 Trade receivables, customer concentration bullet", claimed: "top-5 38.79% for H1 FY26 vs 22.42% FY25 (RHP p.12056)", source_truth: "Values 38.79% and 22.42% exist in the RHP at p38 and p169-170 (table lines 2554, 12090). Page 12056 does not exist (399-page document; 12056 is a text-file line number).", note: "Figures are right; the sole anchor in this section is invalid. LBF2 is a load-bearing fact, so a missing anchor is MAJOR under rule 5. Other stages cite p38-39 and p168-169 correctly.", source_fidelity: true}
  - {severity: "MAJOR", location: "09-tam.md 3C capacity cross-check and B09 input_gaps", claimed: "FY26 panels produced 886 vs 600 stated (148%, AR p74); installed 600 panels and 70,000 relays, new 1,500 and 1,75,000 (RHP p105)", source_truth: "886 and 62,034 are in AR p85 (Annexure table, lines 4267, 4274); AR p74 is the MD&A ratio table. 600 / 70,000 and 1,500 / 1,75,000 are in RHP p104 (lines 7999, 8056, 8075); RHP p105 starts at line 8083.", note: "Values are right and match B03, B04 and B07 (which cite AR p85 and RHP p104). The 09 anchors are one or more pages off. Feeds FLAG-CAPACITY, so material.", source_fidelity: true}
  - {severity: "MINOR", location: "01-gate0.md E2 line and B01 data_notes E2", claimed: "100% promoter holding at 31-Dec-2023 (RHP p.92)", source_truth: "RHP p92: 8 shareholders hold 1,74,69,408 shares = 100%, 'Details as on December 31, 2025 being the date of this RHP' (p92, line 6996 context)", note: "100% and the -26.36pp arithmetic are correct (100 - 73.64). Only the date label is wrong (2023 vs 2025). Scorecard value E2 unaffected.", source_fidelity: true}
  - {severity: "MINOR", location: "01-gate0.md Data notes, FY25 source conflict", claimed: "RHP restated CFO 676.66 lakh, PAT 831.23 lakh (RHP p.290, p.32)", source_truth: "Both figures are at RHP p290 (lines 20600, 20561). PAT 831.23 is at RHP p31 (line 2086); p32 does not contain it.", note: "Primary anchor p290 holds, so the claim stands; the secondary anchor p.32 should read p.31.", source_fidelity: true}
  - {severity: "MINOR", location: "01-gate0.md Block B note and B01 data_notes (WC days)", claimed: "RHP projected FY26 NWC cycle 205 days; computed 136.5", source_truth: "136.5 is on a revenue basis for all three legs. The RHP 205 uses inventory days on cost of goods sold and payables on purchases (RHP p113 text, lines 8685-8689, 8703-8704). Like-for-like on the RHP definition is 176.8 days (B03 3B, AR p99, p113, p115).", note: "Unlabelled basis difference in the comparison sentence (the table above it is labelled revenue basis). Does not touch a score. 205 and 136.5 are each correct on their own basis.", source_fidelity: false}
  - {severity: "MINOR", location: "06-peers.md Q3 (DANISH IPO proceeds line)", claimed: "DANISH IPO proceeds '100% completed' by 31-Mar-2026 (May-26, page 4)", source_truth: "Quote is on May-2026 transcript page 5 (line 180, page 5 starts line 169); page 4 holds the order book remark only", note: "Peer contrast point; quote exists verbatim one page later.", source_fidelity: true}
  - {severity: "MINOR", location: "08-promoter.md 1B, 3E; B08 adverse_findings rank 5; B08 evidence", claimed: "'RHP p.21283 region'; 'AR pp.2397-2417 region'; Promoters not related 'printed p.211'; RF35 education 'printed p.48 (txt page 54)'", source_truth: "Pages 21283 and 2397-2417 do not exist (line-number slips). 'Our Promoters are not related to each other' is at RHP pdf p217 = printed p212 (line 15655). RF35 education text is at pdf p53 (line 4085), printed p48, so 'txt page 54' should read 53.", note: "Facts exist in the source; page anchors wrong or off by one. Non-numeric or minor numeric content only.", source_fidelity: true}
  - {severity: "MINOR", location: "09-tam.md Method 3 peer table and B09", claimed: "Aartech Solonics FY25 revenue Rs 39.33 Cr ('web', no URL)", source_truth: "RHP p119 and p122 print Aartech FY25 revenue from operations 3,635.22 lakh = Rs 36.35 Cr (consolidated)", note: "Unanchored web figure that differs from the in-corpus filed figure with no basis label. Feeds the peer floor (83.86 + 39.33 = 123 Cr, 2.0% of TAM). Effect on SAM or SOM: none.", source_fidelity: false}
  - {severity: "MINOR", location: "05-concall.md 1A; 07-emoat.md 4B; 08-promoter.md; 09-tam.md 5D and B09 stale_data_flags", claimed: "Approximate anchors: 'RHP p~36-40 region, grep line 3805' (order book 5,223.65); 'RHP p~170-171'; 'RHP line ~10682'; 'RHP p~190'; 'RHP p~14' (FX 88.79)", source_truth: "Order book 5,223.65 is at RHP p49 (line 3805) and p172 (line 12232); the values quoted are correct. FX 88.79 is at RHP line 1703. Cited regions are approximate, not page anchors.", note: "Weak anchors only. Every value checked exists in the RHP.", source_fidelity: false}
critical_count: 0
major_count: 5
minor_count: 7
false_positives_struck: 7
material_universe: 1050
acceptance_rate: 96.4
coverage_note: "MANDATORY TIER 32 of 32 checked. Tier = the 32 Gate 0 scorecard inputs (A1-A4, B1-B4, C1-C4, D1-D4, E1-E4, M1-M12) in 01-gate0.md and B01; each was re-derived from its source cells (screener Data_Sheet FY20-FY26 for AVANA and the three peer sheets, results re-filing pp.10-12, RHP pp.92, 225, 290, AR p99-101, p119, SHP XBRL). All 32 inputs tie. No verdict card and no Section 1B pillar section exist in the reports in front of me (stages 10, 11, 13 not yet run), so those two sub-tiers hold zero figures; they are not a silent skip. SAMPLE TIER: 640 figures checked of about 1,050 material figures counted (60%). Material = any figure that feeds a flag, score, table cell or judgment sentence, counted once per distinct value. Order of work: Gate 0 and LBF inputs, 03 AR notes and ratios, 02 passes, 04 and 07 RHP tables, 05 guidance rows, 06 peer sheet ratios and about 25 transcript quotes, 08 promoter and RPT figures, 09 TAM arithmetic. Not checkable from the inputs (about 45 figures): 09 vendor and government market sizes taken from web snippets (MnM, Ken, Straits, IMARC, CEA/loktej, JMK, ICICI Direct, PIB NEP-T ckm/GVA, InVed); 08 media figures (chittorgarh, Glassdoor, businesstoday LTP); MARINE deck financial slides (images). AR pp.99-127 are image transcriptions and the original results PDF is scanned; I read the text files and used overlapping tie-outs (results re-filing vs AR, cash flow vs notes) to settle damaged digits (for example other income 97.01 in the OCR vs 97.21 in the AR, total income 8,483.09 ties to 97.21). I did not reopen the page images. Four 08/09 items rest on the Reg 31(4) transcription and XBRL (73.64%, pledge flags, AIF 6,75,000 locked-in) and all tie."
```
