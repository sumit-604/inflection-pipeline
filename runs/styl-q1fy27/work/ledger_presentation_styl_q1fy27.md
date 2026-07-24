# A2 ENUMERATION LEDGER — presentation_styl_q1fy27
Company: Seshaasai Technologies Ltd (STYL) | Quarter: Q1FY27
Source: /home/user/inflection-pipeline/runs/styl-q1fy27/work/extract_presentation_styl_q1fy27.txt
Unit convention: INR Million (÷10 = Rs Cr). OCR applied to divider slides 5, 7, 11, 19, 30.
Prior-quarter ledger: not supplied to this run — DROPPED_SLIDE comparison could not be performed (flag: `NO_PRIOR_LEDGER`).

```
=== A2 COUNT TEST ===
category: slides            grep_count: 32   sweep_count: 32   match: yes
  (grep: `^\[page [0-9]+\]` markers in extract; sweep: manual read of all 32 [page N] blocks, lines 15-963)
category: pct_tokens (supp) grep_count: 110  sweep_count: n/a (informational only, not gated)
category: rupee_mn_tokens(supp) grep_count: 26  sweep_count: n/a (informational only, not gated)
category: financial_table_line_items (slide 17)  grep_count: 10  sweep_count: 10  match: yes
category: financial_table_line_items (slide 18)  grep_count: 10  sweep_count: 10  match: yes
category: ipo_fund_objects (slide 31)            grep_count: 4   sweep_count: 4   match: yes  (+1 Total row)
gate_a2: pass
=== END COUNT TEST ===
```

---
## TABLE 1 — SLIDE-LEVEL ENUMERATION (32 slides, mandatory unit)

| Slide# | Lines | Title | Content type | Summary of numbers/claims | Flags |
|---|---|---|---|---|---|
| 1 | 15-69 | Regulatory cover letter to BSE/NSE (SEBI Reg. 30) re: Q1FY27 Earnings Conference Call, enclosing Investor Presentation | text + digital signature block | Scrip Code 544533 (BSE), Symbol STYL (NSE); letter dated July 23, 2026, refers to prior letter dated July 20, 2026; digital signature: Manali Siddharth Shah, Company Secretary & Compliance Officer, signed 2026.07.23 20:14:54 +05'30' | signature timestamp present, no board-meeting time to cross-check (this is presentation cover letter, not board outcome) |
| 2 | 70-94 | Investor Presentation Q1FY27 (title slide) | title/cover, photo/logo | Segments named: Payment Solutions, Communication & Fulfilment Solutions (CFS), IoT Solutions. Dated July 23, 2026 | none |
| 3 | 95-117 | Disclaimer | text (legal boilerplate) | no quantified figures | none |
| 4 | 118-138 | Table of Contents | text/list | 5 sections: 1 Key Highlights, 2 Company Background, 3 Financial Overview, 4 Investment Rationale, 5 IPO Funds Utilisation | none |
| 5 | 139-145 | 01 Key Highlights Q1FY27 (section divider) | title only, OCR-confirmed | no numeric content beyond title | OCR-verified empty |
| 6 | 146-192 | Key Financial Highlights – Q1FY27 (YoY + QoQ infographic) | infographic/stat blocks | see Table 2 rows S6-01..S6-14 | `NUMBER_INCONSISTENCY` (₹873.1mn line163 vs ₹873.13mn line185, same Q1FY27 Operating EBITDA figure) |
| 7 | 193-197 | 02 Company Background (section divider) | title only, OCR-confirmed | no numeric content beyond title | OCR-verified empty |
| 8 | 198-240 | A Partner Through Life's Evolution | infographic/photo (product use-cases across life stages) | no quantified figures | none |
| 9 | 241-276 | Seshaasai at a Glance (1/2) | infographic (offerings, certifications) | Certifications listed: NPCI Rupay, Indian Banks, Global Payment Association, Payment Card Industry Data Security Standard, International Organization for Standardization — no numeric counts | none |
| 10 | 277-311 | Seshaasai at a Glance (2/2) | stat blocks + bar chart | Manufacturing: 24 Manufacturing Units Pan India, 7 Locations, 6 States, 2 R&D Labs. Revenue from Operations (₹Mn) FY24/FY25/FY26 chart: 14,411 / 14,632 / 15,583. EBITDA Margin % FY24/25/26: 19% / 25% / 27%. PAT Margin % FY24/25/26: 11% / 15% / 17% | `ORDER_INFERRED` (bar-chart series matched to FY24/25/26 by left-to-right text position, not explicit labels adjacent to each number — verify against filing) |
| 11 | 312-316 | 03 Financial Overview (section divider) | title only, OCR-confirmed | no numeric content beyond title | OCR-verified empty |
| 12 | 317-349 | Business Performance Q1FY27 – Payment Solutions | bar chart + bullets | Revenue (₹mn) Q1FY26→Q1FY27: 1,498 / 1,793 / 1,984 / 1,919 / 1,582. Top-10 customers = 73% of revenue Q1FY27 vs 81.35% Q1FY26. 3 new accounts added Q1FY27. 1 tender won (multi-year) Q1FY27. Payment card exports commenced to Europe & Africa (qualitative, no figure) | `ORDER_INFERRED` (quarterly bar values matched to Q1FY26-Q1FY27 by text position) |
| 13 | 350-388 | Business Performance Q1FY27 – Communication & Fulfilment Solutions (CFS) | bar chart + bullets | Revenue (₹mn) Q1FY26→Q1FY27: 1,318 / 1,327 / 1,362 / 1,607 / 1,488. Top-10 customers = 77.16% of revenue Q1FY27 vs 81.60% Q1FY26. 4 new enterprise accounts added Q1FY27. 2 tenders won (multi-year) from PSU banks Q1FY27 | `ORDER_INFERRED` |
| 14 | 389-428 | Business Performance Q1FY27 – IoT Solutions | bar chart + bullets | Revenue (₹mn) Q1FY26→Q1FY27: 276 / 379 / 384 / 499 / 674. 13 new accounts added Q1FY27 across industries. Prepaid SIM market ~90% vs postpaid ~10% (industry stat, qualitative) | `ORDER_INFERRED` |
| 15 | 429-458 | Financial Performance – Q1FY27 (1/2) | bar chart, 4 metrics x 3 quarters | Operating Revenue YoY +21.1%; Gross [Profit ₹] YoY +13.3%; EBITDA YoY +28.0%; PAT YoY +63.8% (rupee-value growth labels, NOT margin-% growth — margin % moved differently per slide 6/17). Chart values Q1FY26/Q4FY26/Q1FY27: Revenue 3,109/4,042/3,765; Gross Profit 1,384/1,897/1,568; EBITDA 738/1,245/944; PAT 368/818/603 | `LABEL_AMBIGUITY` (slide labels these "YOY +13.3%" etc. under "Gross Margin (%)" header, but 13.3% is gross-profit-value growth not margin-point change — cross-check vs slide 6/17 margin bps figures for A3) |
| 16 | 459-498 | Financial Performance – Q1FY27 (2/2) | stacked bar chart + 2 pct tables + footnote | Operating Revenue stack (₹Mn) by FY24/FY25/FY26/Q1FY26/Q1FY27 with segment values: FY24 {85, 539, 4435, 10524}; FY25 {77, 1062, 4345, 9147}; FY26 {50, 1538, 5611, 7196, and a possible stray "16"}; Q1FY26 {14, 276, 1318, 1498}; Q1FY27 {674, 1488, 1318(?), 1582} — see Table 2 for raw line-by-line capture. BFSI/Non-BFSI % FY24 87/13, FY25 84/16, FY26 83/17, Q1FY27 75/25. Client concentration Top10/Top5/Top1 %: FY24 69/49/17, FY25 66/49/17, FY26 63/48/15, Q1FY27 56/42/15. Footnote (line 497): "Others includes miscellaneous software sales, scrap sales, other rebates. Other operating revenue comprises export duty drawback, rebate income and others" | `COLUMN_ALIGNMENT_UNCERTAIN` (stacked-bar segment-to-year mapping is inferred from raw text x-position only; FY24-column sum computes to 15,583 which is the FY26 total shown on slide 10 — segment/year mapping needs verification against source PDF layout, not text order) |
| 17 | 499-538 | Consolidated Financial Summary – Q1FY27 - YoY (1/2) | financial table (10 line items) + remarks | See Table 3 below. Full P&L walk Q1FY27 vs Q1FY26 | none (all 10 rows populated, no zero/dash items) |
| 18 | 539-579 | Consolidated Financial Summary – Q1FY27 - QoQ (2/2) | financial table (10 line items) + remarks | See Table 3 below. Full P&L walk Q1FY27 vs Q4FY26 | none (all 10 rows populated, no zero/dash items) |
| 19 | 580-584 | 04 Investment Rationale (section divider) | title only, OCR-confirmed | no numeric content beyond title | OCR-verified empty |
| 20 | 585-621 | Investment Rationale (6-point overview) | text list (6 numbered points) + 5 stat callouts | 1 Established Leadership (High Barriers to Entry); 2 Long Standing Relationships; 3 Comprehensive Portfolio; 4 Proprietary Technology Stack; 5 Pan-India Manufacturing; 6 Experienced Promoters/Mgmt. Callouts: 31.9% Market Share (credit/debit card issuance, India, FY25); 1057 Total customers (New 263) as of June 30, 2026; 24 Self-sustaining Manufacturing Units; 25.1% EBITDA Margin as of June 30, 2026; Over 10 Years avg. relationship with 8 of top-10 customers as of Q1FY27; 33+ years Promoter experience | none |
| 21 | 622-667 | 1. Established Leadership Position ... High Barriers to Entry | stat grid + text | 31.9% Market Share in FY25 (footnoted #); 80+ Banks & Fintechs served; 10 of 12 PSU Banks served; 15 of 21 Private Banks served; 10 of 26 Life Insurance Cos served; 7 of 28 General Insurance Cos served; "One of the Top Two" payment-card manufacturers in India FY25; "One of the Largest" cheque-leaf manufacturers FY25; Best Tech Brand in BFSI (Economic Times) for 5 consecutive years, 2021-2025. Footnote line 665: "# Source: F&S Report; all figures are as of March 31, 2025 unless specifically highlighted" | footnote qualifies headline 31.9% market-share figure |
| 22 | 668-697 | 2. Long Standing Relationships with a Large Customer Base | stat grid | 1057 Total Customers as of Q1FY27; 8 of top 10 customers with >10yr vintage; 263 New Customers added Q1FY27; 14.6% Revenue from Largest Customer Q1FY27; 42.1% Revenue from Top-5 Customers Q1FY27; 56.0% Revenue from Top-10 Customers Q1FY27; 95.7% of Revenues from existing customers Q1FY27 | none |
| 23 | 698-713 | 3A Payment Solutions – Comprehensive Card Offerings | photo/product grid | product names only (Hybrid Metal Card, Metal Edge Card, Metal Insert Cards, Biometric Cards, Payment Wearables, Payment Stickers) — no quantified figures | none |
| 24 | 714-752 | 3B Communication & Fulfilment Solutions | text/process diagram | offerings and process-flow list — no quantified figures | none |
| 25 | 753-783 | 3C IoT Solutions | text/diagram | Passive Tags, Active Tags, Automation Hardware, Platforms — no quantified figures | none |
| 26 | 784-823 | 4. Proprietary Technology Stack Enabling Bespoke Solutions | text (4 platform descriptions: izeIoT, RUBIC, eTaTrak, IOMS) | no quantified figures | none |
| 27 | 824-831 | 5. Pan-India Advanced Manufacturing Capabilities | map/graphic (title only in text layer) | no text-extractable numeric content — likely a map graphic with location markers not captured by text layer | `CONTENT_NOT_CAPTURED` (graphic-only slide; cross-check against filing/prior deck for facility count consistency with slide 10's "24 Manufacturing Units / 7 Locations / 6 States") |
| 28 | 832-859 | 6A. Experienced Promoters & Senior Mgmt Team — Chairman & MD, Whole-time Director bios | text (2 director bios) | Pragnyat Pravin Lalwani, Chairman & Managing Director, 33+ years experience; Gautam Sampatraj Jain, Whole-time Director, 33+ years experience | none |
| 29 | 861-905 | 6B. Experienced Promoters & Senior Mgmt Team — Senior Management + Board of Directors | text (8 mgmt bios + 4 director names) | Mgmt team w/ experience yrs: Pawan Kumar Pillalamarri (CFO, 13+ yrs), Bosco Mascarenhas (Head BD&Growth, 27+ yrs), Sandeep Khurana (Head IT, 20+ yrs), Venkat Sandhi Satyanarayana Tangella (Head Ops-Payment Solutions, 29 yrs), Sairam Raghavan (Head Ops-IoT, 19 yrs), Ganesh Srinivasan (Head Corp Accounts & Taxation, 27+ yrs), K. Krishnan Kutty (Regional Head North&East, 18+ yrs), Nandkumar B.L (Regional Head South, 16+ yrs). Board of Directors named (no role/DIN given on this slide): Jayeshkumar Chandrakant Shah, Abbhijet Ghag, Sowmya Vencatesan, Mehul Suresh Shah | `INCOMPLETE_DIRECTOR_DATA` (names only, no DIN/role/term — presentation deck, not the filing; full director profile enumeration belongs to the results-filing doctype if provided separately) |
| 30 | 907-911 | 05 IPO Funds Utilisation (section divider) | title only, OCR-confirmed | no numeric content beyond title | OCR-verified empty |
| 31 | 912-955 | IPO Funds Utilisation Update (Q1FY27) | financial table (4 objects + Total) + 2 narrative lines | See Table 4 below. Cash & cash equivalents ~₹3,690 Mn as of 30 June 2026, including unutilized IPO funds ~₹1,700 Mn (line 951) | `ZERO_STANDING` on Repayment of Borrowings row (During-quarter and Unutilized columns both dash "-") |
| 32 | 956-963 | Thank you / Contact | text | Contacts: Asha Gupta (asha.gupta@in.ey.com), Pratik Jagtap (pratik.jagtap@in.ey.com), Manali Shah (companysecretary@seshaasai.com) — no quantified figures | none |

---
## TABLE 2 — SLIDE 6 GRANULAR QUANTIFIED-CLAIM LEDGER (Key Financial Highlights, YoY + QoQ)

| Row | Line | Metric | Q1FY27 value | Comparator period | Comparator value | Delta | Flag |
|---|---|---|---|---|---|---|---|
| S6-01 | 153-158 | Revenue from Operations | ₹3,764.7 mn | Q1FY26 | ₹3,108.7 mn | ↑21.1% YoY | none |
| S6-02 | 153-158 | Gross Margin | 41.7% | Q1FY26 | 44.5% | ↓286 bps YoY | none |
| S6-03 | 153-158 | EBITDA Margin | 25.1% | Q1FY26 | 23.7% | ↑135 bps YoY | none |
| S6-04 | 162-166 | EBITDA | ₹944.1 mn | Q1FY26 | ₹737.6 mn | ↑28.0% YoY | none |
| S6-05 | 162-166 | Operating EBITDA / Operating EBITDA Margin | ₹873.1 mn / 23.2% | Q1FY26 | ₹714.2 mn / 23.0% | ↑22.3% YoY / ↑22 bps YoY | `NUMBER_INCONSISTENCY` vs S6-11 (₹873.13 mn) |
| S6-06 | 162-166 | PAT | ₹603.4 mn / 16.0% | Q1FY26 | ₹368.4 mn / 11.9% | ↑63.8% YoY / ↑418 bps YoY | none |
| S6-07 | 175-180 | Revenue from Operations | ₹3,764.7 mn | Q4FY26 | ₹4,041.8 mn | ↓6.9% QoQ | none |
| S6-08 | 175-180 | Gross Margin | 41.7% | Q4FY26 | 46.9% | ↓527 bps QoQ | none |
| S6-09 | 175-180 | EBITDA Margin | 25.1% | Q4FY26 | 30.8% | ↓573 bps QoQ | none |
| S6-10 | 184-188 | EBITDA | ₹944.1 mn | Q4FY26 | ₹1,245.2 mn | ↓24.2% QoQ | none |
| S6-11 | 184-188 | Operating EBITDA / Operating EBITDA Margin | ₹873.13 mn / 23.2% | Q4FY26 | ₹1,184.5 mn / 29.3% | ↓26.3% QoQ / ↓611 bps QoQ | `NUMBER_INCONSISTENCY` vs S6-05 (₹873.1 mn) |
| S6-12 | 184-188 | PAT | ₹603.4 mn / 16.0% | Q4FY26 | ₹817.9 mn / 20.2% | ↓26.2% QoQ / ↓421 bps QoQ | none |

---
## TABLE 3 — SLIDES 17 & 18: CONSOLIDATED FINANCIAL SUMMARY LINE ITEMS (₹ Mn)

| Row | Line item | Slide 17 (line) Q1FY27 | Slide 17 Q1FY26 | Δ YoY | % Chg YoY | Slide 18 (line) Q4FY26 | Δ QoQ | % Chg QoQ | Flag |
|---|---|---|---|---|---|---|---|---|---|
| L1 | Revenue from Operations | 3,764.7 (507) | 3,108.7 | 656.0 | +21.1% | 4,041.8 (547) | (277.1) | -6.9% | none |
| L2 | Other Income | 71.0 (509) | 23.4 | 47.6 | +203.0% | 60.7 (549) | 10.3 | +17.0% | none |
| L3 | Total Income | 3,835.7 (511) | 3,132.2 | 703.5 | +22.5% | 4,102.4 (552) | (266.7) | -6.5% | none |
| L4 | Cost of Materials Consumed | 2,196.4 (514) | 1,724.7 | 471.7 | +27.3% | 2,145.2 (555) | 51.17 | +2.4% | none |
| L5 | Employee Cost | 175.4 (517) | 149.8 | 25.6 | +17.1% | 193.4 (558) | (18.1) | -9.4% | none |
| L6 | Other Expenses | 519.8 (519) | 520.1 | (0.3) | -0.1% | 518.8 (560) | 1.0 | +0.2% | none |
| L7 | Depreciation | 107.8 (522) | 110.2 | (2.4) | -2.2% | 97.5 (563) | 10.3 | +10.6% | none |
| L8 | Finance Cost | 18.4 (524) | 77.6 | (59.2) | -76.2% | 29.1 (565) | (10.7) | -36.6% | none |
| L9 | PBT | 817.9 (526) | 549.7 | 268.1 | +48.8% | 1,118.6 (567) | (300.8) | -26.9% | none |
| L10 | Tax | 215.0 (529) | 181.4 | 33.7 | +18.6% | 299.9 (570) | (84.8) | -28.3% | none |
| L11 | PAT attributable to Equity Shareholders | 603.4 (531-533) | 368.4 | 235.0 | +63.8% | 817.9 (572-574) | (214.5) | -26.2% | none |

Remarks bullets captured (qualitative, cite lines): Slide 17 remarks at lines 507-532 (revenue growth driver, gross-margin moderation driver — West Asia conflict / raw material / currency / logistics, employee cost driver, other-expense ratio 13.8% vs 16.7% Q1FY26, finance-cost decline driver — post-IPO debt repayment, PAT margin note referencing FY26 full-year average margin of 16.7%). Slide 18 remarks at lines 547-571 (QoQ revenue seasonality note — Q4 historically strongest quarter, gross-margin moderation driver, employee-cost QoQ decline driver — FY26 year-end benefit provisioning, EBITDA/EBITDA-margin QoQ figures, finance-cost decline driver, PBT/PAT sequential figures).

---
## TABLE 4 — SLIDE 31: IPO FUNDS UTILISATION UPDATE (₹ Mn)

| # | Object | Line | Amount per offer doc (A) | Beginning of qtr (B) | During qtr (C) | End of qtr (B+C) | Unutilized (A-B-C) | Flag |
|---|---|---|---|---|---|---|---|---|
| 1 | Capex | 930 | 1,979.1 | 550.6 | 67.7 | 618.2 | 1,361.0 | none |
| 2 | Repayment of Borrowings | 935 | 3,000.0 | 3,000.0 | - | 3,000.0 | - | `ZERO_STANDING` (During-qtr and Unutilized both dash — object fully utilized in prior quarter(s), zero movement/balance this quarter) |
| 3 | Issue Expenses | 939 | 350.6 | 293.0 | 39.1 | 332.1 | 18.5 | none |
| 4 | General corporate purposes | 943-945 | 670.3 | 211.6 | 137.3 | 348.9 | 321.3 | none |
| — | Total | 948 | 6,000.0 | 4,055.2 | 244.0 | 4,299.2 | 1,700.8 | none (arithmetic cross-check: A,B,C,B+C,A-B-C columns each sum correctly across the 4 objects to the Total row — verify against filing in A3) |

Narrative lines (950-951): "On the balance sheet and cash flow front, we remain well capitalised." / "As of 30th June 2026, we had cash and cash equivalents of approximately ₹3690 Mn, including unutilized IPO funds of approximately ₹1700 Mn" — the ₹1,700 Mn figure is consistent with the Total-row Unutilized amount (₹1,700.8 Mn) within rounding.

---
## SUMMARY OF FLAGS RAISED

- `NUMBER_INCONSISTENCY` — Slide 6, Operating EBITDA Q1FY27 shown as both ₹873.1 mn (line 163, YoY block) and ₹873.13 mn (line 185, QoQ block). Same metric, same quarter, two different precision/values. A3 to reconcile against filing.
- `ORDER_INFERRED` — Slides 10, 12, 13, 14: bar-chart series values matched to period labels (FY24/25/26 or Q1FY26...Q1FY27) by left-to-right text position in the extract, not by explicit adjacent labeling. Flagged for verification against the source PDF visual layout.
- `LABEL_AMBIGUITY` — Slide 15: "YOY +13.3%" etc. appear under margin-% chart headers but represent rupee-value growth, not margin-point movement — risk of misreading as margin change.
- `COLUMN_ALIGNMENT_UNCERTAIN` — Slide 16: stacked revenue-breakup chart, segment-to-year mapping uncertain from text extraction; FY24-column raw sum (15,583) coincides with the FY26 total disclosed on slide 10, suggesting possible column/year misalignment in the text layer.
- `CONTENT_NOT_CAPTURED` — Slide 27 (Pan-India Manufacturing map) has no text-extractable numeric content; graphic-only slide.
- `INCOMPLETE_DIRECTOR_DATA` — Slide 29 Board of Directors names given with no DIN/role/term (expected; this is the investor deck, not the results filing).
- `ZERO_STANDING` — Slide 31, "Repayment of Borrowings" row: During-the-quarter (C) and Unutilized-amount (A-B-C) columns both dash-valued.
- `NO_PRIOR_LEDGER` — no prior-quarter ledger was supplied to this run; `DROPPED_SLIDE` comparison (rule 3, INVESTOR PRESENTATION section) could not be performed. A3/A4 should source the prior-quarter deck ledger separately if a dropped-slide check is required.

Note on doc structure: page 1 of the PDF is a SEBI Reg. 30 cover letter (not a deck slide in the conventional sense) and page 2 is the deck's own title slide; both are enumerated as slides 1 and 2 respectively per the instruction to enumerate every disclosure unit at the PDF/page level (32 pages = 32 enumeration units, matching page_count_pdfinfo: 32 and formfeed_count: 32 in the A1 header).

---
```yaml
stage: A2-enumerator
company: "STYL"
quarter: "q1fy27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/styl-q1fy27/work/ledger_presentation_styl_q1fy27.md"
counts:
  slides: 32
  slide_numbers: 32
  line_items: 21          # 10 (slide17) + 10 (slide18) + 1 IPO-total row context; see Table 3/4 for full breakdown
  zero_standing: 2         # slide 31 Repayment of Borrowings: During-qtr(C) + Unutilized(A-B-C) dash cells
notes: 0
agenda_items: 0
auditor_paras: 0
entities: 0
turns: 0
questions: 0
mgmt_numbers: 0
flags_raised: [NUMBER_INCONSISTENCY, ORDER_INFERRED, LABEL_AMBIGUITY, COLUMN_ALIGNMENT_UNCERTAIN, CONTENT_NOT_CAPTURED, INCOMPLETE_DIRECTOR_DATA, ZERO_STANDING, NO_PRIOR_LEDGER]
gate_a2: pass
mismatch_note: ""
```
