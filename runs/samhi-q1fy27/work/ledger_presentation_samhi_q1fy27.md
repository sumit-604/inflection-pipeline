=== A2 COUNT TEST ===
category: slides              grep_count: 52   sweep_count: 52   match: yes
category: footnotes           grep_count: 56   sweep_count: 56   match: yes
category: kpi_bearing_slides  grep_count: 39   sweep_count: 39   match: yes  (see reconciliation note below)
category: agenda_items        grep_count: 0    sweep_count: 0    match: yes  (N/A — presentation, not board-outcome letter)
category: auditor_paras       grep_count: 0    sweep_count: 0    match: yes  (N/A — no auditor report in this doctype)
category: entities             grep_count: 0    sweep_count: 0    match: yes  (N/A — no consolidation list in this doctype)
category: turns / questions    grep_count: 0    sweep_count: 0    match: yes  (N/A — presentation, not concall transcript)
gate_a2: pass

Reconciliation note (kpi_bearing_slides): grep pass 1 used pattern
`RevPAR|\bARR\b|\bADR\b|Occupan\w*|EBITDA|\bPAT\b|\bPBT\b|Net\s*Debt|Total Income|\bRevenue\b|\d[\d,]*\s*[Rr]ooms?\b|\d+\+?\s*[Hh]otels?\b|Segment(?:ation)?\b|[Gg]uidance|[Pp]ipeline|Opening\b|FY2\d\b`
run against each of the 52 page-blocks independently. Grep pass 1 returned 39 slides but flagged
slide 3 (not slide 8) as a match; manual sweep (independent full read of all 1,917 lines)
flagged slide 8 (not slide 3). Both sets equal 39 by count but differed by two members —
re-swept both slides directly:
  - Slide 3 contains "EBITDA" only inside the Free Cash Flow formula definition
    ("Free Cash Flow = EBITDA (before ESOP) – Lease MG – Cash Interest", line 126) — a
    definitional footnote, not a disclosed KPI *value*. Reclassified out of this category
    (retained in the Footnotes table instead).
  - Slide 8 discloses "75 Hotels / 1,046 Rooms / 15 States / 3 Countries" (lines 264-269) but
    the infographic's number and its label sit on non-adjacent text lines (two-column layout:
    numbers on line 264, labels on line 266, with unrelated bullet-list text from the
    right-hand column interleaved on line 265) — a pdftotext-layout artifact that a single-line
    regex cannot bridge. Manually confirmed as a genuine KPI disclosure and reclassified into
    this category.
Final reconciled set (39, manual-verified, authoritative): slides
4,5,6,7,8,9,11,12,13,14,15,16,18,19,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,
41,42,43,44,45,48,49,50. gate_a2 = pass on the corrected, documented set.

Prior-quarter ledger: not supplied in task inputs — DROPPED_SLIDE comparison not performed
this run (noted, not a gate failure; flag for A3/A4 to request the prior deck ledger if a
cross-quarter silence check is required).
=== END COUNT TEST ===

# Ledger — SAMHI Hotels Ltd. (SAMHI) — Q1 FY27 Investor Presentation
Source: presentation_samhi_q1fy27.pdf (52 pages / 52 slides, incl. cover letter as slide 1)
Unit convention: ₹ millions (x0.1 = ₹ Crore). OCR applied only to slides 27 and 39
(section dividers, no data lost — see extract header, lines 15-35).

---

## TABLE 1 — SLIDE INVENTORY (52/52)

| Slide | Line | Title | Content type |
|---|---|---|---|
| 1 | 37 | Cover/intimation letter to BSE & NSE (Q1 FY27 results presentation) | text/letter, digital signature block |
| 2 | 95 | Investor Presentation title, Q1 FY2027 | text/photo (cover) |
| 3 | 109 | Important notes on the presentation format | text (bullets, incl. FCF definition) |
| 4 | 129 | Business overview: 31 hotels/4,899 rooms base; 7-hotel/1,669-room pipeline; 75-hotel/1,046-room leisure platform | text/infographic |
| 5 | 148 | Our Business / Core Strategy / Embedded Growth / Healthy Balance Sheet | text |
| 6 | 179 | "SAMHI has delivered consistent growth" — FY12-FY26 Revenue & EBITDA bar chart | chart (native vector) |
| 7 | 224 | "We are adding iconic assets" — 6 pipeline-project photos with rooms/opening dates | photo/text |
| 8 | 247 | "We support India's most respected platform for leisure hotels" (RARE overview) | text/infographic |
| 9 | 274 | "Future will be a lot more than sum of parts" — FY2026 segment table + FY27-32 secured pipeline | table |
| 10 | 314 | "Financial Highlights" section divider | divider/photo |
| 11 | 328 | Highlights for the quarter | text (bullets) |
| 12 | 351 | Financial summary — Q1 FY2027 (8 KPI callout boxes) | text/KPI boxes |
| 13 | 380 | Strong comparable performance — Comparable vs Reported table | table |
| 14 | 418 | Hits & Misses: Q1 FY2027 | text (bullets, two columns) |
| 15 | 452 | Financial Summary (Consolidated P&L), Q1FY27/Q1FY26/YoY/FY26 | table |
| 16 | 510 | Balance Sheet continues to strengthen — Net Debt / Net Debt-EBITDA / rating table+chart | table/chart |
| 17 | 603 | "Macro Dynamics" section divider | divider/photo |
| 18 | 615 | Robust commercial activity across key markets — office market table | table |
| 19 | 651 | Air Passenger Trend in Q1FY27 | chart (line, native vector) |
| 20 | 755 | "Portfolio Performance" section divider | divider/photo |
| 21 | 767 | Double-digit RevPAR growth — quarterly RevPAR chart + segment RevPAR growth + revenue contribution | chart |
| 22 | 818 | Q1FY27 Total Income bridge | chart (waterfall) |
| 23 | 855 | Q1FY27 Consol. EBITDA bridge | chart (waterfall) |
| 24 | 896 | Operational Efficiency — Asset Income to Consol. EBITDA bridge | chart (waterfall) |
| 25 | 940 | Segmentation Mix — Total Income Split by Segment | chart (donut) |
| 26 | 970 | Segment Performance — 3-segment comparison table | table |
| 27 | 1006 | "Growth Projects" section divider [OCR page, no data] | divider/photo |
| 28 | 1014 | Secured projects to accelerate future growth — 16-row growth pipeline table | table |
| 29 | 1046 | W, HITEC City, Hyderabad — project progress | text/infographic |
| 30 | 1081 | Strong product in a resilient market (W Hyderabad) | text/photo |
| 31 | 1098 | Westin & Tribute Portfolio, Whitefield Bangalore — intro | text/photo |
| 32 | 1109 | Westin & Tribute Portfolio, Whitefield Bangalore — project progress | text/infographic |
| 33 | 1133 | Partnership with Ingka Centres in Noida | text/infographic |
| 34 | 1178 | One Financial District, Hyderabad | text/infographic |
| 35 | 1210 | SAMHI's largest hotel under development — Navi Mumbai | text/infographic |
| 36 | 1248 | New Hotel Expansion at Sriperumbudur | text/infographic |
| 37 | 1279 | RARE India: capital-efficient leisure entry, Marriott Bonvoy overlay | text/infographic |
| 38 | 1312 | RARE India: "succession" capital — Itmenaan Estate case study | text/photo |
| 39 | 1347 | "About Us" section divider [OCR page, no data] | divider/photo |
| 40 | 1358 | Diversified portfolio across travel occasions | text (no numeric KPI) |
| 41 | 1386 | Upper Upscale & Upscale segment detail | text/infographic |
| 42 | 1430 | Upper Mid-scale segment detail | text/infographic |
| 43 | 1455 | Mid-scale segment detail | text/infographic |
| 44 | 1479 | Leisure Portfolio (Asset Light Model) | text/infographic |
| 45 | 1496 | Dominant share with leading operators — brand mix donut | chart |
| 46 | 1530 | Team that built the business (management bios + tenure) | text/photo |
| 47 | 1566 | Strong governance with highly experienced board members | text (director list + other directorships) |
| 48 | 1597 | Historical Consolidated P&L Summary, FY20-FY26 (3 charts) | chart |
| 49 | 1649 | Historical Consolidated Quarterly P&L Summary, Q1'24-Q1'27 (3 charts) | chart |
| 50 | 1792 | Glossary — 38-row hotel-by-hotel room roster + RARE + subtotals + grand total | table |
| 51 | 1852 | Disclaimer (incl. forward-looking-statement safe-harbor language) | text |
| 52 | 1883 | Thank You — company & IR-advisor contacts | text |

---

## TABLE 2 — KPI / DATA-LABEL DISCLOSURE LEDGER (by slide)

### Slide 1 (letter) — line 37
| Line | Disclosure | Flags |
|---|---|---|
| 39, 50 | CIN L55101DL2010PLC211816; BSE Scrip 543984; NSE Scrip SAMHI | — |
| 71-78 | Digital signature block: Sanjay Jain, Senior Director-Corporate Affairs, Company Secretary & Compliance Officer; "Digitally signed by SANJAY JAIN, Date: 2026.08.03 20:53:23 +05'30'" | signature timestamp only, no board-meeting time given in this doctype to cross-check against — no flag raised |

### Slide 3 — line 109
| Line | Disclosure | Flags |
|---|---|---|
| 121-123 | "All operating performance metrics are presented on a same-store basis (highlighted in orange)" | methodology note |
| 124-125 | "Room counts in under development asset may vary based on final plan and statutory approvals" | qualifies all pipeline room counts deck-wide |
| 126 | "Free Cash Flow = EBITDA (before ESOP) – Lease MG – Cash Interest" | formula definition qualifying slide-12 FCF figure — see Footnotes table |

### Slide 4 — line 129
| Line | Disclosure | Flags |
|---|---|---|
| 140 | Strong Base: 31 Hotels, 4,899 rooms | — |
| 140 | Near Term Growth: 7 new hotels, 1,669¹ rooms | fn1 (line 146): includes 22 apartments of Hyatt Regency Pune, pre-opening |
| 140 | Long Term Potential: 75 hotels, 1,046 rooms (leisure) | — |
| 141 | "~₹12.5bn revenue in FY2026" | rounded (actual FY26 Total Income = ₹12,790mn per slides 6/15/48) |

### Slide 5 — line 148
| Line | Disclosure | Flags |
|---|---|---|
| 164-165 | "growth pipeline consists of 7 new big-box hotels ... with 1,669¹ rooms" | repeat of slide-4 figure, consistent |

### Slide 6 — line 179 (native-vector bar chart, FY12-FY26)
| Line | Disclosure | Flags |
|---|---|---|
| 184 | Consol Revenue FY26 = ₹12,790mn | anchor figure, cross-validated vs slides 15, 48 |
| 185 | Consol Revenue FY25 = ₹11,386mn¹ | fn1 (line 220): FY25 restated for Caspia Delhi discontinued-ops reclassification |
| 192 | Consol Revenue CAGR = 22% (10 yrs)² | fn2 (line 222): CAGR computed FY16-FY26 |
| 198-199 | Consol EBITDA (pre-ESOP) FY26 = ₹4,721mn | cross-validated vs slide 16 TTM EBITDA Mar 31 2026; see ND-04 below re: conflict with slide-15/48 "Consolidated EBITDA" FY26 = ₹4,626mn (different basis) |
| 202-203 | Consol EBITDA CAGR (pre-ESOP) = 38% (10 yrs)² | — |
| 184-217 | Full raw bar-label set (Revenue & EBITDA series, FY12-FY26): 10; 203; 434; 732; 1,721; 1,793; 3,331; 3,572; 4,202; 4,901; 6,276; 7,615; 9,787; 11,386; 12,790; 4,721 | **CHART_LABEL_MAPPING_UNCERTAIN** — pdftotext -layout extraction of this two-series vector chart does not reliably preserve which numeric label belongs to which FY on the x-axis for interior (non-anchor) years; only the FY26 endpoints (12,790 Revenue; 4,721 EBITDA pre-ESOP) are independently cross-validated elsewhere in the deck. Recommend visual confirmation before using intermediate-year values. |

### Slide 7 — line 224 (pipeline project photos)
| Line | Disclosure | Flags |
|---|---|---|
| 232-234 | W, HITEC City, Hyderabad: 170 rooms, Opening Q4 FY27 | FORWARD_LOOKING (opening timeline) |
| 232-234 | Westin, Whitefield, Bangalore: 220 rooms, Opening FY30 | FORWARD_LOOKING |
| 232-234 | Mid-scale Hotel, Financial District, Hyderabad: 260 rooms, Opening FY30 | FORWARD_LOOKING |
| 239-241 | Marriott, Sriperumbudur, Chennai: 135 rooms, Opening FY30 | FORWARD_LOOKING |
| 239-241 | Upper Upscale Hotel, Sec-51, Noida: 162 rooms, Opening FY30 | FORWARD_LOOKING |
| 239-241 | Westin & Fairfield, Navi Mumbai: 700 rooms, Opening FY31 | FORWARD_LOOKING |

### Slide 8 — line 247
| Line | Disclosure | Flags |
|---|---|---|
| 264-269 | RARE: 75 Hotels, 1,046 Rooms, 15 States, 3 Countries (India, Nepal, Bhutan) | number/label split across non-adjacent lines (264 vs 266) — see kpi_bearing_slides reconciliation note above; consistent with slides 37, 44 |
| 262-269 | RARE fee-income model: a) fee income from business generated for hotel partners; b) additional incentive fee in select hotels; c) selective opportunistic investments | qualitative revenue-model disclosure, no rupee figure yet attached |

### Slide 9 — line 274 (FY2026 segment table + FY27-32 secured pipeline)
| Line | Disclosure | Flags |
|---|---|---|
| 288 | Upper Upscale & Upscale FY26: 1,123 rooms; ₹5,270mn revenue; ₹4.7mn revenue/key | — |
| 289 | Upper Upscale & Upscale pipeline: +1,059 rooms new openings; +473 rooms conversion from Upper Mid-scale¹; FY27-32 rooms 2,655 (+136%) | FORWARD_LOOKING; fn1 (line 310) cross-validates vs glossary rebranding rows (217+114+142=473, slide 50) |
| 292 | Upper Mid-scale FY26: 2,047 rooms; ₹5,235mn revenue; ₹2.6mn revenue/key | — |
| 291-293 | Upper Mid-scale pipeline: +350 rooms new openings; -473 rooms conversion to Upscale¹; FY27-32 rooms 1,924 (-6%) | FORWARD_LOOKING |
| 295 | Mid-scale FY26: 1,729 rooms; ₹1,994mn revenue; ₹1.2mn revenue/key | — |
| 295 | Mid-scale pipeline: +260 rooms new openings; FY27-32 rooms 1,989 (+15%) | FORWARD_LOOKING |
| 300-303 | Leisure FY26: rooms "–", revenue "–", revenue/key "–"; pipeline 1,046 rooms within portfolio, % Change "NA" | **ZERO_STANDING** — dash/NA values in a standing segment-table row; template signal that Leisure segment revenue is not yet broken out/booked on this table in FY2026 baseline, expected to populate as RARE monetization (fee income, incentive fee, opportunistic investment per lines 299-303) comes online |
| 308-309 | "Asymmetric returns as majority of new rooms being added are in segments with relatively higher revenue per key*" | forward framing/guidance; fn* (line 312): excludes RARE India inventory (asset-light) |
| 12,499 (derived) | Sum of three disclosed segment FY26 revenues (5,270+5,235+1,994) = ₹12,499mn vs FY26 Total Income ₹12,790mn (slides 6/15/48) — gap ₹291mn | **NUMBER_DISCREPANCY candidate (ND-03a)** — gap plausibly = corporate/other income not attributed to segment table (cf. slide 22 "Corporate Income" bridge line), not confirmed; flagged for A3/A4 |

### Slide 11 — line 328 (Highlights for the quarter)
| Line | Disclosure | Flags |
|---|---|---|
| 335 | Comparable Revenue growth +10.8% YoY | — |
| 336 | Occupancy ~79.3%² (up from ~74.2% Q1FY26) | fn2 (line 349): same-store basis, excludes Trinity/HIEX Gr.Noida/HIEX Kolkata/Caspia Delhi/Sheraton Commercial |
| 336 | RevPAR growth +9.6% YoY | — |
| 337-338 | Domestic travelers = 81% of room-nights sold in Q1 (up from 78% same period last year) | — |
| 340-341 | Operating margins ~36% (ex-GST impact); "scope for improvement"; growth in upscale inventory (not GST-impacted) expected to lift margins to ~40% | FORWARD_LOOKING / guidance |
| 343 | "on-going growth pipeline ... and progress in RARE India gives us a formidable path to growth" | FORWARD_LOOKING (qualitative) |

### Slide 12 — line 351 (Financial summary KPI boxes)
| Line | Disclosure | Flags |
|---|---|---|
| 360 | Same-store RevPAR ₹5,219, +9.6% YoY | matches slide 21 chart endpoint |
| 360-363 | Total Income ₹3,083mn; +10.8% YoY Comparable²; +7.3% YoY Reported | consistent — Q1FY27 comparable = Q1FY27 reported (3,083); only Q1FY26 base differs |
| 360-363 | Consol. EBITDA ₹1,013mn; +12.1% YoY Comparable²; -4.1% YoY Reported | **NUMBER_DISCREPANCY (ND-01)** — the ₹1,013mn figure is the *Reported* Q1FY27 EBITDA; the Comparable-basis Q1FY27 EBITDA per slide 13 (line 399) is ₹1,105mn, not ₹1,013mn. The box pairs one rupee figure with two different-basis growth rates, which can misread as ₹1,013mn itself growing both +12.1% and -4.1% |
| 360-365 | PBT (ex-exceptional) ₹327mn; +121.7% YoY Comparable²; 25.5% reduction in finance cost | **NUMBER_DISCREPANCY (ND-02)** — same pattern: ₹327mn is Reported Q1FY27 PBT; Comparable-basis Q1FY27 PBT per slide 13 (line 405) is ₹419mn, not ₹327mn |
| 363-365 | Occupancy 79.3%¹ "withstanding impact of middle-east conflict" | — |
| 369-371 | PAT ₹249mn | no YoY% shown in this box (unlike the other 3 boxes) — presentation-format inconsistency, not a numeric error |
| 371 | Free Cash Flow ~₹619mn; ~₹340mn cash interest outflow | ties to slide-3 FCF formula definition |
| 371 | Effective Interest Rate 7.8%; ~300bps lower since IPO | — |
| 371 | Net Debt : EBITDA ~3.2x; ~2.4x on Operating Assets | matches slide 16 chart Jun 30 2026 column |

### Slide 13 — line 380 (Comparable vs Reported table)
| Line | Disclosure | Flags |
|---|---|---|
| 394 | Total Income: Comparable Q1FY26 2,782 / Q1FY27 3,083 / YoY +10.8%; Reported Q1FY26 2,873 / Q1FY27 3,083 / YoY +7.3% | — |
| 399-400 | Consolidated EBITDA: Comparable Q1FY26 986 / Q1FY27 **1,105** / YoY +12.1%; Reported Q1FY26 1,056 / Q1FY27 1,013 / YoY -4.1% | see ND-01 above |
| 405-406 | PBT (before exceptional): Comparable Q1FY26 189 / Q1FY27 **419** / YoY +121.7%; Reported Q1FY26 259 / Q1FY27 327 / YoY +26.4% | see ND-02 above |
| 411 | PAT: Comparable Q1FY26 122 / Q1FY27 341 / YoY +179.2%; Reported Q1FY26 192 / Q1FY27 249 / YoY +29.7% | — |
| 394-410 | Adjustment items: ~₹91mn one-time other income in Q1FY26 (GIC-related subsidiary capital restructuring); ~₹21mn one-time GIC transaction expenses in Q1FY26; ~₹92mn GST ITC impact of opex in Q1FY27 | — |

### Slide 14 — line 418 (Hits & Misses)
| Line | Disclosure | Flags |
|---|---|---|
| 426-428 | Revenue growth ~11% comparable, "in line with our 9-11% guidance" | FORWARD_LOOKING (references prior guidance band 9-11%) |
| 426-429 | GST change: shift from 12% (with ITC) to 5% (without input credit) compressed reported EBITDA growth by ~₹92mn for the quarter | ties to slide 13 adjustment and slide 23/24 GST-impact bridge lines |
| 430-432 | "with most new openings in upscale segment, we expect our EBITDA margins to improve" | FORWARD_LOOKING / guidance |
| 433-434 | Occupancy 79.3%² (repeat) | — |
| 435-436 | Hyatt Regency Pune: 22 apartments fully completed; approval delay "causing loss of revenue in a strong market" | — |
| 437-441 | 36%² of days in Q1FY27 above 90% occupancy ("sold out") | — |
| 444-447 | RARE-Marriott: 40+ of 75 hotels agreed to Outdoor Collection; 15 pilot properties shortlisted; integration "intended" in H2FY27 | FORWARD_LOOKING |

### Slide 15 — line 452 (Consolidated P&L table, 13 line items x 4 periods)
| Line | Item | Q1FY27 | Q1FY26 | YoY% | FY26 | Flags |
|---|---|---|---|---|---|---|
| 459 | Total Income | 3,083 | 2,873¹ | +7.3% | 12,790 | fn1 (493): incl. ~₹91mn one-time other income Q1FY26 |
| 462-467 | Consolidated EBITDA² | 1,013 | 1,056 | -4.1% | 4,626 | fn2 (496): incl. ~₹21mn GIC one-time exp. Q1FY26 + ~₹92mn GST ITC impact Q1FY27; see ND-04 (conflicts with slide 6/16 "4,721" pre-ESOP figure) |
| 464 | EBITDA Margin | 32.9% | 36.8% | — | 36.2% | — |
| 475 | Depreciation & Amortization | (309) | (291) | +6.3% | (1,267) | — |
| 477 | Finance cost | (377) | (506) | -25.5% | (1,709) | — |
| 480-482 | PBT (before exceptional items) | 327 | 259 | +26.4% | 1,650 | — |
| 485 | Exceptional Items³ | – | – | — | 1,075 | **ZERO_STANDING** (both quarterly cols dash); fn3 (500): FY26 figure = reversal of impairment of PPE/ROU/Intangibles +966, labor-code impact -35, gain on sale of Caspia Delhi +145 |
| 487 | Profit/(Loss) from discontinued operations⁴ | – | (28) | — | (55) | **ZERO_STANDING** (Q1FY27 col dash); fn4 (503): represents Caspia Delhi |
| 491 | PBT | 327 | 231 | +41.8% | 2,671 | — |
| 495 | Tax Expense⁵ | (78) | (39) | — | 2,995⁶ | fn5 (504): non-cash expense; fn6 (505): ~₹3,000mn deferred tax asset recognized in FY26 |
| 500 | PAT | 249 | 192 | +29.7% | 5,665 | — |
| 503 | Attributable to SAMHI | 183 | 173 | — | 5,030 | — |
| 505 | Attributable to Minority Interest | 67 | 19 | — | 636 | — |
| 492 | "All values in ₹mn, unless specified otherwise" | — | — | — | — | footnote (unmarked) |

### Slide 16 — line 510 (Balance Sheet)
| Line | Item | Sep 30 '23 | Mar 31 '25 | Mar 31 '26 | Jun 30 '26 | Flags |
|---|---|---|---|---|---|---|
| 519 | Credit Rating | BBB | A− | A+ | A+ | — |
| 522 | Net Debt (₹mn) | 17,974 | 19,669 | 14,507 | 14,928 | — |
| 524 | TTM EBITDA¹ (₹mn, ex-ESOP & one-time) | 3,398 | 4,434 | 4,721⁵ | 4,664⁵ | fn5 (600): excludes Caspia Delhi EBITDA on TTM basis; Mar'26 value 4,721 cross-validates slide-6 anchor; see ND-04 |
| 530-587 | Net Debt-to-EBITDA (reported) / Net Debt-to-EBITDA (Adjusted for Growth Capital)² / Interest Rate³ (chart, 3 series) | 5.3x / — / 10.8-11.5% | 4.4x-3.9x / — / 9.2-9.5% | 3.1x / 2.4x / 7.9-8.5% | 3.2x / 2.4x / 7.8-8.5% | **CHART_LABEL_MAPPING_UNCERTAIN** — three-series chart (ND:EBITDA reported, ND:EBITDA adj. for growth capital, interest rate) with axis-tick labels (0-8, 5.5%-11.5%) interleaved in the text stream; exact bar/line-to-period assignment for intermediate points not independently verifiable from text-layout alone. Endpoints (Jun'30'26 = 3.2x / 2.4x / 7.8%) are cross-validated vs slide 12 |
| 591-593 | Net Annualized interest run rate⁴ (₹mn) | ~2,400 | ~1,900 | ~1,270 | ~1,240 | fn4 (598): excludes non-cash finance cost items (interest on lease, EIR, etc.) |

### Slide 18 — line 615 (Office market table)
| Line | Disclosure | Flags |
|---|---|---|
| 622-627 | Net Office Absorption: FY26 total ~58mn sqft; Q1FY26 total ~14mn sqft; Q1FY27 total ~11mn sqft | — |
| 629-645 | City breakdown — Office market size (current/upcoming, mn sqft) & Net Absorption (FY26/Q1FY26/Q1FY27, mn sqft): Bangalore 238/35, 15.3/3.5/3.5; Hyderabad 143/50, 9.5/1.0/1.3; Delhi NCR 166/26, 9.3/2.1/1.2; Mumbai 163/23, 8.5/2.6/1.3; Pune 93/27, 7.2/2.2/2.5; Chennai 86/14, 7.4/2.5/0.7; Kolkata 30/6, 1.3/0.4/0.5 | source: JLL FY26 (fn1, 648); Cushman & Wakefield (fn2, 649) — third-party macro data, not SAMHI-specific |

### Slide 19 — line 651 (Air passenger trend)
| Line | Disclosure | Flags |
|---|---|---|
| 662-747 | QoQ airline passenger volumes (mn), Q1FY23-Q1FY27, raw label set: 53, 53, 63, 66, 67, 65, 70, 71, 72, 71, 75, 77, 77, 79, 78, 75 (16 quarters); YoY Q1FY27 = +0.1% | **CHART_LABEL_MAPPING_UNCERTAIN** — sequential line-chart labels; exact quarter assignment not independently re-derivable from text order alone (endpoints plausible given "+0.1% YoY" callout) |
| 662-714 | Q1FY27 change over Q1FY26 by city: Delhi +6.9%, Mumbai +6.2%, Pune +1.6%, Ahmedabad +0.4%, Bangalore 0.0%, Chennai -2.0%, Goa -5.2%, Kolkata -9.9%, Hyderabad -12.1% | source: AAI, 10 metro cities (fn1, 752); "impacted due to ongoing macro-economic situation and large dependence on gulf carriers for international traffic" (line 659-661) — macro context for occupancy/RevPAR commentary |

### Slide 21 — line 767 (RevPAR growth)
| Line | Disclosure | Flags |
|---|---|---|
| 767-816 | Same-store RevPAR by quarter, Q1FY24-Q1FY27, raw label set: 3,662; 3,782; 4,248; 4,276; 4,529; 4,760; 4,830; 5,026; 5,088; 5,643; 5,958; 6,041; 5,219 (13 quarters, endpoint Q1FY27=5,219 cross-validates slide 12) | **CHART_LABEL_MAPPING_UNCERTAIN** for interior quarters; footnote superscripts 1/2/3/4 (lines 807, 812-816) indicate the same-store exclusion set itself changed across the 13-quarter window (ACIC Portfolio, Trinity, HIEX Greater Noida, HIEX Kolkata, Caspia Delhi, Sheraton Commercial phased in/out at different points) — flagged for A3 as a moving same-store base, not merely a labeling issue |
| 787 | RevPAR YoY Q1FY27 = +9.6% | matches slide 12 |
| 777-789 | Segment RevPAR growth Q1FY27 YoY: Upper Upscale & Upscale +8.6%; Upper Mid-scale +8.8%; Mid-scale +13.7% | fn4 (816) |
| 774-789 | Revenue contribution by segment Q1FY27: Upper Upscale & Upscale 41%; Upper Mid-scale 42%; Mid-scale 17% | matches slide 25 |

### Slide 22 — line 818 (Total Income bridge, waterfall)
| Line | Disclosure | Flags |
|---|---|---|
| 838 | Q1 FY26 Asset Income = 2,734 | — |
| 828-845 | Growth in Same Store +249 (+9.1% YoY) | — |
| 845 | Growth from new openings +75² | fn2 (851): includes Trinity, HIEX Greater Noida, HIEX Kolkata, RARE India |
| 845-847 | Loss due to sold/discontinued operations (1)³ | fn3 (853): includes Sheraton Commercial |
| 837-845 | Q1 FY27 Asset Income = 3,057 (+11.8% YoY) | internally consistent: 2,734+249+75-1=3,057 |
| 841-845 | Corporate Income adjustment +26 | ties to ~₹91mn Q1FY26 one-time other income (GIC) commentary |
| 828-846 | Q1 FY27 Total Income = 3,083 (+7.3% YoY) | matches slides 12/13/15 |

### Slide 23 — line 855 (Consol. EBITDA bridge, waterfall)
| Line | Disclosure | Flags |
|---|---|---|
| 879 | Q1 FY26 Asset EBITDA = 1,031 | — |
| 865-869 | Growth in Same Store w/o GST impact +125 (+12.2% YoY) | — |
| 867 | Growth from new openings +27² | fn2 (892) |
| 868 | Loss due to sold/discontinued operations (4)³ | fn3 (894) |
| 877-886 | Q1 FY27 Asset EBITDA (pre-GST impact) = 1,179 (+14.3% YoY) | internally consistent: 1,031+125+27-4=1,179 |
| 868-872 | GST Change impact = (82); "includes GST impact of ~₹10mn" (at Net Corporate G&A line) | — |
| 878-886 | Q1 FY27 Asset EBITDA (post GST) = 1,097 | 1,179-82=1,097 ✓ |
| 870-886 | Net Corporate G&A (incl. ESOP) = (84) | — |
| 866-887 | Q1 FY27 Consol. EBITDA = 1,013 (-4.1% YoY; +6.4% YoY callout; "12.2% comparable growth in EBITDA on same-store assets excluding Q1FY27 impact of GST" per line 884-886) | 1,097-84=1,013 ✓ internally consistent; matches slides 12/13/15 |

### Slide 24 — line 896 (Operational Efficiency bridge)
| Line | Disclosure | Flags |
|---|---|---|
| 915 | Asset Income = 3,057 | — |
| 905-907 | Payroll (514), -16.8% | — |
| 908-911 | Fixed [costs] (359), -11.8%; "Operating expenses include a total of ~₹82mn of GST impact spread across most cost heads" | — |
| 912-913 | Variable [costs] (610), -20.0% | — |
| 916-918 | Utilities (210), -6.9% | — |
| 918-919 | Management Fees (153), -5.0% | — |
| 920-921 | Lease Rentals (53), -1.7% | — |
| 921-923 | Ownership Expenses (61), -2.0% | — |
| 915-928 | Asset EBITDA = 1,097 (35.9% margin) | reconciles: 3,057-514-359-610-210-153-53-61=1,097 ✓ |
| 922-925 | Net Corporate G&A (incl. ESOP) = (84); "includes GST impact of ~₹10mn" | — |
| 915-928 | Consol. EBITDA = 1,013 (32.9% margin) | 1,097-84=1,013 ✓ matches slides 12/13/15/23 |

### Slide 25 — line 940 (Segmentation Mix donut)
| Line | Disclosure | Flags |
|---|---|---|
| 952-961 | Total Income Split Q1FY27: Upper Upscale & Upscale 41%; Upper Mid-scale 42%; Mid-scale 17% | matches slide 21 |
| 964-967 | "On-going rebranding/renovations to increase upscale share from ~41% to ~60% by FY2030, giving boost to our overall revenue per key" | FORWARD_LOOKING / guidance (target date FY2030) |

### Slide 26 — line 970 (Segment Performance table)
| Line | Segment | Hotels | Rooms | Occupancy¹ | ARR¹ | RevPAR¹ | Flags |
|---|---|---|---|---|---|---|---|
| 996-1000 | Upper Upscale & Upscale | 5 | 1,123 | 78% | ₹10,494 | ₹8,229 | fn1 (1003) same-store basis |
| 996-1000 | Upper Mid-scale | 14 | 2,047 | 78% | ₹6,552 | ₹5,131 | ARR×Occ≈RevPAR check: 6,552×0.78=5,111 (label 5,131, normal rounding) |
| 996-1000 | Mid-scale | 12 | 1,729 | 81% | ₹3,755 | ₹3,052 | ARR×Occ≈RevPAR check: 3,755×0.81=3,041 (label 3,052, normal rounding) |
| — | (Hotels sum = 5+14+12 = 31; Rooms sum = 1,123+2,047+1,729 = 4,899) | — | — | — | — | — | cross-validates slide 4 base (31 hotels, 4,899 rooms) |
| 977-981 | Legend: Stable = ±200bps YoY; Upward = +200-700bps; Strong Upward = >700bps; Downward = -200 to -700bps; Strong Downward = <-700bps | — | — | — | — | — | classification key, no color-coding recoverable from text extraction |

### Slide 28 — line 1014 (16-row growth pipeline table)
| # | Line | Hotel | Segment | Growth Project | Status | Rooms (year col) | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 1025 | Holiday Inn Express, Greater Noida | Mid-scale | Rebranding | Completed | 133 (FY26) | — |
| 2 | 1026 | Holiday Inn Express, Kolkata | Mid-scale | New Opening | Completed | 113 (FY26) | — |
| 3 | 1027 | Sheraton, Hyderabad | Upscale | Expansion | Completed | 12 (FY26) | — |
| 4 | 1028 | Holiday Inn Express, Whitefield, Bangalore | Mid-scale | Expansion | Completed | 56 (FY26) | — |
| 5 | 1029 | Sheraton, Hyderabad | Upscale | Expansion | Completed | 42 (FY26) | — |
| 6 | 1030 | Hyatt Regency, Pune | Upscale | Expansion | Pre-Opening | 22 (FY26) | ties to slide 4 fn1 (22 apartments) |
| 7 | 1031 | W, HITEC City, Hyderabad | Upscale | New Opening | Under Fit-out | 170 (FY27) | FORWARD_LOOKING |
| 8 | 1032 | Courtyard by Marriott, Pune² | Upscale | Rebranding from Four Points by Sheraton | Design | 217 (FY27) | fn2 (1043): part renovation in progress, full renovation in due-course |
| 9 | 1033 | Tribute Portfolio by Marriott, Whitefield, Bangalore² | Upscale | Rebranding from Trinity | Design | 142 (FY27) | — |
| 10 | 1034 | Tribute Portfolio by Marriott, Jaipur² | Upscale | Rebranding from Four Points by Sheraton | Design | 114 (FY27) | rows 8+9+10 = 217+142+114 = 473, cross-validates slide 9 "+473/-473" conversion figure exactly |
| 11 | 1035 | Westin, Whitefield, Bangalore | Upscale | New Opening | Under Construction | 220 (FY28) | FORWARD_LOOKING |
| 12 | 1036 | Mid-scale asset, Financial District, Hyderabad | Mid-Scale | New Opening | Design | 260 (FY28) | FORWARD_LOOKING |
| 13 | 1037 | Westin, Navi Mumbai | Upscale | New Opening | Design | ~350 (FY30+ col) | **TABLE_COLUMN_ALIGNMENT_UNCERTAIN** — text-layout column boundary between FY29/FY30+ not fully unambiguous for rows 13-16; figures themselves (350/350/162/135) are certain, exact FY-bucket less so |
| 14 | 1038 | Fairfield by Marriott, Navi Mumbai | Upper Mid-scale | New Opening | Design | ~350 (FY30+ col) | same caveat |
| 15 | 1039 | Upper Upscale Asset, Noida | Upscale | Expansion | Design | 162 (FY30+ col) | same caveat |
| 16 | 1040 | Marriott, Sriperumbudur, Chennai³ | Upscale | New Opening | Design | 135 (FY30+ col) | fn3 (1044): earlier proposed as expansion to existing Fairfield by Marriott with 86 rooms — reclassified, see slide 42 fn1 cross-reference |
| — | 1019-1022 | Header: "4,899 current operational rooms; Rebranding of 473 rooms and addition of 1,669¹ rooms through combination of expansion and new opening" | — | — | — | — | cross-validated: new-build rows 7,11-16 sum = 170+220+260+350+350+162+135 = 1,647; +22 (row 6, Hyatt Regency Pune addition already counted in operating base) = 1,669 ✓ matches slide 4 exactly |

### Slides 29-36 — individual project detail (lines 1046-1277)
| Slide | Line | Disclosure | Flags |
|---|---|---|---|
| 29 | 1052, 1061-1076 | W, HITEC City, Hyderabad: 170 rooms¹; Project Progress stages — Design: Interior design finalization; Construction: Completed; MEP: Under progress; Fit-out: Under progress; Pre-Opening: [not yet reached] | fn1 (1079): room count based on final segment/brand/plan, may vary |
| 30 | 1094 | W, HITEC City, Hyderabad (170 rooms) — repeat | — |
| 31 | 1105 | Westin & Tribute Portfolio, Whitefield, Bangalore: 142 rooms renovation + 220 new rooms | — |
| 32 | 1112, 1113-1126 | Same project; Project Progress — Design: Interior Design [complete]; Construction: Basement [current, "Under construction" tag]; MEP/Fit-out/Pre-Opening: not yet reached | — |
| 33 | 1146, 1141-1171 | Ingka Centres Noida: ~162-room Upscale hotel; Progress — Design: Advance Stage; Construction: Gr Floor Level; market context: ~2.5mn sq.ft. mixed-use development | — |
| 34 | 1192, 1187-1191 | One Financial District, Hyderabad: ~260 rooms¹; Progress — Design: Planning (earliest stage) | fn1 (1208): room count may vary |
| 35 | 1233-1235, 1216 | Navi Mumbai: 700 rooms¹ combo-hotel (~350 Westin + ~350 Fairfield); Progress — Design: Planning | fn1 (1246): room count may vary (dash-style footnote, not colon/period-marked) |
| 36 | 1256-1265, 1260-1268 | Sriperumbudur: ~135 room "Marriott"* alongside existing 153-room Fairfield (asset-level RoCE >30%); Progress — Design: Planning | fn* (1277): earlier proposed as 86-room extension of existing Fairfield, same brand, room count may vary |

### Slide 37 — line 1279 (RARE India overview)
| Line | Disclosure | Flags |
|---|---|---|
| 1287-1289 | 75 Hotels, 1,046 Rooms, 15 Indian states, 3 other countries | matches slides 8, 44 |
| 1306-1308 | "Portfolio adds 2 new hotels since last reporting"; property visits completed across pilot resorts; "targeted to go live in H2 FY27" | FORWARD_LOOKING; quarter-over-quarter growth metric (2 new hotels) |

### Slide 38 — line 1312 (Itmenaan Estate case study)
| Line | Disclosure | Flags |
|---|---|---|
| 1324 | ~8 acres, 8 rooms existing "going to 15-20 rooms" | FORWARD_LOOKING (planned expansion) |
| 1325 | Purchase price ~₹120mn | — |

### Slide 41 — line 1386 (Upper Upscale & Upscale detail)
| Line | Disclosure | Flags |
|---|---|---|
| 1399 | "5 Hotels +8 under development¹" | fn1 (1427): includes 5 hotels under development and 3 under rebranding from Upper Mid-scale |
| 1404-1405 | 1,123 Rooms (+1,059 under development and 473 under rebranding²) | fn2 (1428): room counts may vary |
| 1410 | ₹1,239mn Revenue (Q1FY27) | — |

### Slide 42 — line 1430 (Upper Mid-scale detail)
| Line | Disclosure | Flags |
|---|---|---|
| 1439 | "14 Hotels +1 under development" | — |
| 1440-1442 | 2,047 Rooms (+350¹ under development²; 2,047 operating rooms inc. 473 under rebranding²) | — |
| 1447 | ₹1,298mn Revenue (Q1FY27) | — |
| 1452 | fn1: "Previously reported 473 under-development rooms included 86 rooms of Fairfield, Sriperumbudur. These have been moved to the Upscale under-development section, as the property is now being built as a Marriott with ~135 rooms." | **CLASSIFICATION_CHANGE** — this is a reclassification of a pipeline project between segment buckets vs a prior quarter's disclosure; flag for A3 quarter-over-quarter reconciliation (project itself is slide-28 row 16 / slide-36) |

### Slide 43 — line 1455 (Mid-scale detail)
| Line | Disclosure | Flags |
|---|---|---|
| 1464 | "12 Hotels +1 under development" | — |
| 1465-1466 | 1,729 Rooms (+260 under development¹) | — |
| 1471 | ₹517mn Revenue (Q1FY27) | — |

### Slide 44 — line 1479 (Leisure Portfolio)
| Line | Disclosure | Flags |
|---|---|---|
| 1488-1489 | 75 Hotels, 1,046 Rooms | matches slides 8, 37 |

### Slide 45 — line 1496 (Brand-share donut)
| Line | Disclosure | Flags |
|---|---|---|
| 1505-1519 | Q1FY27 Asset Income by operator: Marriott ₹2,036mn (67%); IHG ₹517mn (17%); Hyatt ₹501mn (16%) | sum = 3,054mn / 100% — internally consistent; see ND-03b below re: vs. Asset Income 3,057mn (slide 22) |

### Slide 46 — line 1530 (Management team)
| Line | Disclosure | Flags |
|---|---|---|
| 1537-1564 | Tenure in SAMHI: Ashish Jakhanwala (Chairman, MD&CEO) 14+ yrs; Rajat Mehra (CFO) 15+ yrs; Sanjay Jain (Sr. Director-Corp. Affairs, CS & Compliance Officer) 15+ yrs; Gyana Das (EVP-Corp. Strategy & Head of Investments) 9+ yrs; Manish Bhagat (VP-Finance) 13+ yrs; Ayush Singhal (SVP-Finance) 2+ yrs; Sangeeta Mohan (VP-Asset Mgmt) 12+ yrs; Nakul Manaktala (SVP-Investment) 7+ yrs | not a financial KPI in the task's specified categories; recorded for completeness (management tenure/continuity signal) |

### Slide 47 — line 1566 (Board members)
| Line | Director | Role | Other directorships (line) | Flags |
|---|---|---|---|---|
| 1576-1579 | Ashish Jakhanwala | Chairman, MD & CEO | Accor; Interglobe Hotels Pvt. Ltd.; Pannel Kerr Forster Consultants Pvt. Ltd. (1582-1588) | — |
| 1576-1579 | Manav Thadani | Non-Executive & Non-Independent Director | Hotelivate Pvt. Ltd.; HVS Licensing LLC (1582-1584) | — |
| 1576-1579 | Ajish Abraham Jacob | Non-Executive & Non-Independent Director | Asiya Capital Investments Company K.S.C.P.; Albazie & Co (RSM); Ernst & Young (1582-1587) | — |
| 1576-1579 | Michael David Holland | Independent Director | Nexus Select Mall Management; Embassy Office Parks Management Services Pvt. Ltd.; Assetz Property Management Services Pvt. Ltd.; JLL (1582-1590) | — |
| 1576-1579 | Aditya Jain | Independent Director | International Market Assessment (India) Pvt. Ltd.; PR Pandit Public Relations Pvt. Ltd.; Chemplast Sanmar Ltd. (1582-1588) | — |
| 1576-1579 | Archana Capoor | Independent Director | Tourism Finance Corporation of India; Birla Cable Limited; S Chand and Company Ltd. (1582-1588) | — |
| 1576-1579 | Krishan Dhawan | Independent Director | Bank of America; Oracle India; Sandhar Technologies Ltd. (1582-1588) | — |
| — | — | Board composition: 1 Executive (Chairman/MD/CEO) + 2 Non-Exec Non-Independent + 4 Independent = 7 directors | — | no DIN/term-dates/appointment-dates disclosed in this doctype (presentation, not a board-outcome letter/annexure) — not a gap in this doctype, noted for completeness only |

### Slide 48 — line 1597 (Historical annual P&L, FY20-FY26, 3 charts)
| Line | Disclosure | Flags |
|---|---|---|
| 1604-1643 | Total Income, Consolidated EBITDA, PAT — FY20-FY26 raw label sets: Total Income {6,276; 7,614; 9,787; 11,386¹; 12,790}; note only 5 of 7 FY labels have clearly distinct large values recoverable, remainder (FY22/FY23 intermediate) ambiguous in text order. EBITDA raw labels: {-597; 218; 1,720; 2,606; 2,879; 4,251; 4,626}. PAT raw labels: {-4,777; -4,433; -3,386; -2,999; -2,346; 855; 5,665} | **CHART_LABEL_MAPPING_UNCERTAIN** — same caveat as slide 6; endpoints (FY26: Total Income 12,790, EBITDA 4,626, PAT 5,665) are the reliable, cross-validated anchors (matches slide 15); interior-year (FY20-FY25) bar-to-year assignment not independently confirmed from text layout. Note EBITDA FY26 shown here (4,626) is the *reported/post-ESOP* figure — see ND-04 |
| 1647 | fn1: FY25 financials restated for Caspia Delhi sale (discontinued operation) | — |

### Slide 49 — line 1649 (Historical quarterly P&L, Q1'24-Q1'27, 3 charts)
| Line | Disclosure | Flags |
|---|---|---|
| 1657-1788 | Total Income, Consolidated EBITDA, PAT — Q1'24-Q1'27 (13 quarters each). Anchor points cross-validated: Q1FY27 Total Income 3,083 (matches slides 12/13/15/22); Q1FY26 reported 2,873 (matches slide 15); Q1FY27 EBITDA 1,013 (matches slides 12/13/15/23/24); Q1FY26 reported EBITDA 1,056 (matches slide 15); Q1FY27 PAT 249 (matches slide 15); Q1FY26 reported PAT 192 (matches slide 15) | **CHART_LABEL_MAPPING_UNCERTAIN** for the remaining 11 interior quarters (raw label pool includes 1,924; 2,232; 2,542; 2,669; 2,733; 2,899; 2,941; 2,963; 3,234; 3,419; 3,535 for Total Income; 473; 540; 891; 904; 962; 967; 1,056; 1,105; 1,115; 1,202; 1,263; 1,278 for EBITDA; and (880); (835); (744); 42; 113; 126; 192; 228; 249; 459; 481; 998; 3,994 for PAT) |
| 1789 | Note: "EBITDA reported for Q3'26, Q4'26 and Q1'27 is post GST implementation" | methodology note — directly relevant to the GST-impact discrepancy discussed at slides 11/14/23/24 |
| 1790 | Note: FY25 restated for Caspia Delhi discontinued operation (repeat) | — |

### Slide 50 — line 1792 (Glossary — 38-row hotel roster)
| Line | Disclosure | Flags |
|---|---|---|
| 1803-1833 | 31 operating hotels, each with Hotel Brand / City / Location / Operator / Segment / Operating Rooms / Addition-Renovation / Total (rows #1-31, e.g. row1 Hyatt Regency Pune 301 op. rooms +22 addition =323 total; ... row31 Holiday Inn Express Kolkata 113/–/113) | full 31-row detail retained; Addition/Renovation column = "-" (dash) for 27 of the 31 rows (all except rows 1, 26, 28, 30) — **ZERO_STANDING**, template column signaling no addition/renovation activity currently booked against those 27 already-stabilized assets |
| 1834 | Sub-total Operating: 4,899 / 22 / 4,921 | — |
| 1835-1842 | 7 new-addition rows (#32-38): Westin Bangalore 220; W Hyderabad 170; Mid-scale Hyderabad 260; Westin Navi Mumbai 350; Fairfield Navi Mumbai 350; Upper Upscale Asset Noida 162; Marriott Sriperumbudur 135 | matches slide 28 rows 7, 11-16 exactly |
| 1842 | Sub-total - New Addition: – / 1,647 / 1,647 | — |
| 1844 | Total - Asset Ownership: 4,899 / 1,669 / 6,568 | 22+1,647=1,669 ✓ matches slide 4/28 header |
| 1846 | Row #39-113: RARE India, Pan India, Leisure, 1,046 / — / 1,046 | — |
| 1847 | Grand Total: 5,945 / 1,669 / 7,614 | 4,899+1,046=5,945 ✓; 4,921+1,647+1,046=7,614 ✓ internally consistent |

### Slide 51 — Disclaimer (line 1852)
| Line | Disclosure | Flags |
|---|---|---|
| 1871-1877 | Forward-looking-statement safe-harbor paragraph: market opportunity/business prospects statements are FLS, not guarantees, subject to known/unknown risks (Indian & international economy, industry competition, strategy execution, growth/expansion, technology, revenue/income/cash-flow changes, market risk exposure); company assumes no obligation to update | FORWARD_LOOKING (formal boilerplate covering all FLS in the deck) |
| 1880-1881 | Listing date confirmation: NSE & BSE listing 22 September 2023; unaudited standalone & consolidated results for quarter ended 30 June 2026 drawn up per Regulation 33 of Listing Regulations | confirms results are unaudited (Reg. 33 limited review, not full audit) |

---

## TABLE 3 — FOOTNOTES & FINE-PRINT DISCLAIMERS (56/56)

| # | Slide | Line | Text (summary) |
|---|---|---|---|
| 1 | 4 | 146 | Includes 22 apartments of Hyatt Regency, Pune, currently under pre-opening |
| 2 | 5 | 177 | Same text repeated |
| 3 | 6 | 220 | FY25 financials restated — Caspia Delhi sale recognized as discontinued operation |
| 4 | 6 | 222 | CAGR calculated FY16-FY26 (10 years) |
| 5 | 9 | 310 | Renovation/re-branding from Upper Mid-scale to Upper Upscale & Upscale segment |
| 6 | 11 | 348 | Comparable excludes one-time GIC items (Q1FY26) and GST ITC impact (Q1FY27); refer slide 12 |
| 7 | 11 | 349 | Same-store basis excludes Trinity/HIEX Gr.Noida/HIEX Kolkata/Caspia Delhi/Sheraton Commercial |
| 8 | 12 | 377 | Same-store definition (repeat) |
| 9 | 12 | 378 | Comparable adjustment definition (repeat) |
| 10 | 14 | 449 | Comparable adjustment definition (repeat) |
| 11 | 14 | 450 | Same-store definition (repeat) |
| 12 | 15 | 493 | ~₹91mn one-time other income Q1FY26 (GIC subsidiary capital restructuring) |
| 13 | 15 | 496 | EBITDA impact: a) ~₹21mn one-time GIC exp. Q1FY26; b) ~₹92mn GST ITC impact Q1FY27 |
| 14 | 15 | 500 | Exceptional items FY26: +₹966mn impairment reversal, -₹35mn labor code, +₹145mn Caspia Delhi sale gain |
| 15 | 15 | 503 | Discontinued operations = Caspia Delhi |
| 16 | 15 | 504 | Tax expense represents non-cash expense |
| 17 | 15 | 505 | ~₹3,000mn deferred tax asset recognized in FY26 |
| 18 | 16 | 590 | TTM EBITDA excludes ESOP & one-time expenses |
| 19 | 16 | 591 | Capital allocated list: W (HITEC Hyd.), Westin Bglr., HRP Apartments, Sheraton Rooms & Apartments, HIEX (Wht. Bglr.), Westin Navi Mumbai, other capex |
| 20 | 16 | 595 | As on 30 June 2026; interest rate includes amortized upfront fee |
| 21 | 16 | 598 | Interest run-rate excludes non-cash finance cost items (lease interest, EIR, etc.) |
| 22 | 16 | 600 | TTM EBITDA excludes Caspia Delhi |
| 23 | 18 | 648 | Office market size source: JLL FY26 |
| 24 | 18 | 649 | Net absorption source: Cushman & Wakefield |
| 25 | 19 | 752 | Source: AAI, 10 key metro cities |
| 26 | 19 | 753 | Mumbai includes Navi Mumbai |
| 27 | 21 | 812 | Same-store excl. ACIC Portfolio (Aug'23), Caspia Pro Gr.Noida |
| 28 | 21 | 813 | Same-store excl. ACIC, Trinity, HIEX Gr.Noida, Caspia Delhi |
| 29 | 21 | 814 | Same-store excl. Four Points Sheraton Chennai OMR (sold Feb'25), Trinity, HIEX Gr.Noida, HIEX Kolkata, Caspia Delhi, Sheraton Commercial |
| 30 | 21 | 816 | Same-store excl. Trinity, HIEX Gr.Noida, HIEX Kolkata, Caspia Delhi |
| 31 | 22 | 850 | Same-store excl. Trinity, HIEX Gr.Noida, HIEX Kolkata, Sheraton Commercial |
| 32 | 22 | 851 | New openings = Trinity, HIEX Gr.Noida, HIEX Kolkata, RARE India |
| 33 | 22 | 853 | Sold/discontinued = Sheraton Commercial |
| 34 | 23 | 891 | Same-store definition (repeat) |
| 35 | 23 | 892 | New openings definition (repeat) |
| 36 | 23 | 894 | Sold/discontinued definition (repeat) |
| 37 | 26 | 1003 | Same-store excl. Trinity, HIEX Gr.Noida, HIEX Kolkata, Sheraton Commercial |
| 38 | 28 | 1042 | Includes 22 apartments Hyatt Regency Pune, pre-opening |
| 39 | 28 | 1043 | Part renovation in progress, full renovation in due course |
| 40 | 28 | 1044 | Earlier proposed as expansion to existing Fairfield by Marriott, 86 rooms |
| 41 | 29 | 1079 | Room count based on final segment/brand/plan, may vary |
| 42 | 34 | 1208 | Room count may vary (repeat) |
| 43 | 41 | 1427 | Includes 5 hotels under development + 3 under rebranding from Upper Mid-scale |
| 44 | 41 | 1428 | Room counts may vary |
| 45 | 42 | 1452 | 473 under-development rooms previously included 86 rooms of Fairfield Sriperumbudur, now reclassified to Upscale (Marriott ~135 rooms) — **CLASSIFICATION_CHANGE** |
| 46 | 42 | 1453 | Room counts may vary |
| 47 | 43 | 1476 | Room count may vary |
| 48 | 48 | 1647 | FY25 restated for Caspia Delhi (repeat) |
| 49 | 35 | 1246 | Room count may vary (dash-style "1 -" footnote, not colon/period-marked) |
| 50 | 6 | 219 | "Note: All values in ₹mn, unless specified otherwise" |
| 51 | 7 | 245 | "Note: Above images are architectural renders and may undergo change in the future" |
| 52 | 24 | 938 | "Note: All values in ₹mn, unless specified otherwise" (repeat) |
| 53 | 49 | 1789 | "Note: EBITDA reported for Q3'26, Q4'26 and Q1'27 is post GST implementation" |
| 54 | 9 | 312 | "* Only for Owned new hotels excluding RARE India inventory which is on asset-light model" |
| 55 | 36 | 1277 | "*Note: development earlier proposed as 86-room extension of Fairfield by Marriott" |
| 56 | 15 | 492 | "All values in ₹mn, unless specified otherwise." (unmarked, no "Note:"/number prefix) |

Additional non-marked definitional note recorded for completeness (excluded from the strict
56-count gate above, which is scoped to numbered/asterisked/"Note:"-prefixed footnotes):
Slide 3, line 126 — "Free Cash Flow = EBITDA (before ESOP) – Lease MG – Cash Interest"
(deck-wide FCF definition, qualifies slide-12 FCF figure of ~₹619mn).

---

## TABLE 4 — FORWARD-LOOKING / GUIDANCE STATEMENTS (13)

| # | Slide | Line | Statement |
|---|---|---|---|
| 1 | 7 | 232-241 | 6 pipeline projects with opening timelines: Q4FY27 (1), FY30 (4), FY31 (1) |
| 2 | 9 | 284-303 | Secured Pipeline FY2027-FY2032: room additions & % change by segment (Upscale +136%, Upper Mid-scale -6%, Mid-scale +15%, Leisure NA) |
| 3 | 11 | 340-341 | Operating margins ~36% ex-GST expected to improve to ~40% as upscale inventory grows |
| 4 | 14 | 426-428 | Revenue growth "in line with our 9-11% guidance" (prior guidance band referenced) |
| 5 | 14 | 430-432 | EBITDA margins "expected to improve" despite GST headwind |
| 6 | 14 | 444-447 | RARE-Marriott: 15 pilot properties "intended to be integrated" in H2FY27 |
| 7 | 25 | 964-967 | Upscale revenue share targeted to rise ~41% -> ~60% by FY2030 |
| 8 | 28 | 1024-1044 | 16-project growth pipeline with FY26-FY30+ timeline/status columns |
| 9 | 33 | 1140-1171 | Ingka Centres Noida partnership — development-phase progress/positioning statements |
| 10 | 36 | 1256-1269 | Sriperumbudur Marriott expected to "enhance the over pricing of the asset" |
| 11 | 37 | 1306-1308 | RARE pilot integration "targeted to go live in H2 FY27" |
| 12 | 38 | 1324 | Itmenaan Estate rooms "potential/plan to increase to 15-20 rooms" from existing 8 |
| 13 | 51 | 1871-1877 | Formal forward-looking-statement safe-harbor disclaimer paragraph |

---

## TABLE 5 — NUMBER_DISCREPANCY / FLAG SUMMARY

| ID | Slides | Description |
|---|---|---|
| ND-01 | 12 vs 13 | Slide-12 headline EBITDA box shows ₹1,013mn (Reported) paired with "+12.1% YoY Comparable" label; true Comparable Q1FY27 EBITDA (slide 13, line 399) is ₹1,105mn, not ₹1,013mn |
| ND-02 | 12 vs 13 | Slide-12 headline PBT box shows ₹327mn (Reported) paired with "+121.7% YoY Comparable" label; true Comparable Q1FY27 PBT (slide 13, line 405) is ₹419mn, not ₹327mn |
| ND-03a | 9 vs 6/15/48 | Sum of three disclosed FY26 segment revenues (₹5,270+5,235+1,994=₹12,499mn, slide 9) vs FY26 Total Income ₹12,790mn (slides 6/15/48) — ₹291mn gap, not reconciled on-slide |
| ND-03b | 22 vs 41/42/43/45 | Sum of Q1FY27 segment revenues (₹1,239+1,298+517=₹3,054mn, slides 41-43; also matches brand-mix chart ₹3,054mn, slide 45) vs Q1FY27 Asset Income ₹3,057mn (slide 22 bridge) — ₹3mn gap |
| ND-04 | 6/16 vs 15/48 | FY26 EBITDA basis conflict: ₹4,721mn (pre-ESOP/TTM basis, slides 6 & 16) vs ₹4,626mn (reported Consolidated EBITDA, slides 15 & 48) — different definitional basis (ESOP-adjusted), footnoted on each slide but both are labeled simply "EBITDA FY26" at a glance, risking conflation |
| ENUM-05 | 6, 16, 19, 21, 48, 49 | CHART_LABEL_MAPPING_UNCERTAIN — native-vector multi-series/multi-period bar & line charts where pdftotext -layout extraction does not reliably preserve which numeric data-label corresponds to which period for interior (non-anchor) points; all raw label sets recorded in Table 2, endpoints independently cross-validated where possible |
| ENUM-06 | 28 | TABLE_COLUMN_ALIGNMENT_UNCERTAIN — rows 13-16 of the growth-pipeline table, exact FY29 vs FY30+ column bucket ambiguous in text layout (figures themselves certain) |
| CLASS-07 | 42 (fn1) | CLASSIFICATION_CHANGE — 86 rooms of Fairfield Sriperumbudur reclassified from Upper Mid-scale under-development bucket to Upscale under-development bucket (now built as ~135-room Marriott); relevant for QoQ pipeline reconciliation |

---

## TABLE 6 — ZERO_STANDING ITEMS

| Slide | Line | Item | Detail |
|---|---|---|---|
| 9 | 300-303 | Leisure segment, FY2026 columns | Rooms "–", Revenue "–", Revenue/Key "–"; pipeline "% Change" = "NA" — standing row retained as a template signal that Leisure segment revenue is not yet broken out in the FY2026 baseline (RARE monetization pending) |
| 15 | 485 | Exceptional Items, Q1FY27 & Q1FY26 columns | Both "–" (only FY26 annual column populated: 1,075) |
| 15 | 487 | Profit/(Loss) from discontinued operations, Q1FY27 column | "–" (Q1FY26 populated: (28); FY26 populated: (55)) |
| 50 | 1804-1833 | Glossary "Addition/Renovation" column, 27 of 31 operating-hotel rows | "–" across all 27 already-stabilized assets (only rows 1, 26, 28, 30 show non-dash values) |

---

## NOTES ON SCOPE / METHOD
- This ledger enumerates all 52 slides and every disclosed figure within the task's specified
  KPI categories (RevPAR, ARR/ADR, occupancy, revenue, EBITDA & margin, PAT, net debt &
  Net Debt/EBITDA, asset/room/key counts, pipeline/growth-project keys & timelines,
  segment/same-store splits, guidance/forward-looking statements), plus every footnote/
  fine-print disclaimer and the one digital-signature block present (cover letter, slide 1).
- Concall-transcript and board-outcome-letter enumeration categories (participants, turns,
  questions, agenda items, auditor paragraphs, entity consolidation list) are not applicable
  to this doctype (investor presentation) and are recorded as N/A / 0 in the count test, not
  as gaps.
- Prior-quarter deck ledger was not supplied; DROPPED_SLIDE comparison could not be performed
  this run — flagged for A3/A4 to request if a cross-quarter silence check is required.
