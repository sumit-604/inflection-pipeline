# A2 ENUMERATION LEDGER — MANINDS Corporate Presentation, filed 2026-09-01
Doctype: presentation (37-slide deck, Reg 30 filing) | Ticker: MANINDS | Quarter tag: 2026-09
Source: runs/maninds-corppres-2026-09/work/extract_presentation_maninds_2026-09.txt (1366 lines)
Prior-quarter ledger: NOT PROVIDED — DROPPED_SLIDE category cannot be tested this run (flag: NO_PRIOR_LEDGER).

Unit convention (per A1 header, carried into every row below where a conversion applies):
- Slides marked ₹ Cr / USD Mn directly: conversion_factor = x1 (no conversion needed).
- Tables pp.28–32 (INR Millions, except EPS): conversion_factor = x0.1 (Cr = Millions / 10).
- NPC table p.26 (SAR M / USD M): source-inline constants — SAR/INR 23.955, SAR/USD 3.75 (pegged),
  CY2025 Revenue = INR ~1,898.9 Cr, PAT = INR ~343.6 Cr. Used as given; not re-derived.

=== A2 COUNT TEST ===
category: slides                          grep_count: 37   sweep_count: 37   match: yes
  (grep -c "^===== PAGE" on the extract = 37; manual sweep of page-marker sections = 37;
  matches page_count_pdfinfo / formfeed_count in the A1 header.)
category: financial_table_line_items_p28-30  grep_count: 60   sweep_count: 60   match: yes
  (p28 Standalone P&L = 12 line items, p29 Consolidated P&L = 12, p30 Balance Sheet = 36
  [16 liabilities-side + 20 assets-side captions]. Caption-pattern grep (matching each row's
  text label, not requiring an adjacent digit) confirms all 60. A pure-digit grep pass run
  first found only 35 of p30's 36 rows — it cannot see "Current Tax Assets", which is dash
  ("-") in FY24/FY25/FY26 alike and carries no digit token. Re-swept and added as
  ZERO_STANDING; caption-grep then confirmed 36/36. This is the GATE A2 mismatch-then-resolve
  instance for this run — named per instruction #4.)
category: chart_data_points_p31-32 (individual values, not ledger rows)  grep_count: 63   sweep_count: 63   match: yes
  (p31 Historical Consolidated Performance = 28 individual values [Total Income 4 pts; Gross
  Profit value+margin 4+4; EBITDA value+margin 4+4; PAT value+margin 4+4]; p32 Quarterly Trend
  = 35 [Total Income 5 pts; Gross Profit value+margin 5+5; EBITDA value+margin 5+5; PAT
  value+margin 5+5]. First-pass manual sweep undercounted at 4/5 pts per named chart (missed
  that each chart carries a VALUE series AND a separate MARGIN% series); numeric-token grep
  ([\d,]+\.?\d*%?) on the two page blocks caught 28 and 35 tokens exactly (footer page numbers
  and the p32 footnote's incidental digits excluded) and forced the re-sweep — mismatch
  resolved before emitting. NOTE: the ledger itself represents each chart SERIES as one row
  with FY/quarter values in columns (9 rows p31, 9 rows p32 = 18 ledger rows), so this
  63-count is a value-level count, not a row-level count; row-level counts are in the
  slide-by-slide SUMMARY COUNTS below.)
category: npc_summary_p26                 grep_count: 24   sweep_count: 28   match: yes (reconciled)
  (24 = caption-matched structured rows: 16 P&L + 5 cash/liquid-assets table + 3 return ratios.
  28 = 24 + units-note + Zero-Debt checkmark claim + orderbook note + conversion-constant
  footer [4 non-caption rows], none of which a caption-grep targets by design — reconciled by
  category definition, not a numeric gap. Ledger table for slide 26 carries exactly 28 rows.)
category: named_entities                  grep_count: 48   sweep_count: 48   match: yes
  (board/mgmt 11 [p8] + domestic/intl clients 12 [p14, one row per name after re-sweep — see
  mismatch note] + certifications/accolades 6 [p15] + NPC direct clients 9 [p22] + NPC EPC
  contractors 10 [p23] = 48; each name grep-confirmed present at least once in its page block.
  First-draft sweep of p14 had consolidated all 5 domestic and all 7 international names into
  2 combined rows instead of 12 one-per-name rows, inconsistent with the one-row-per-name
  convention used on p8/p22/p23 — caught on internal consistency re-check and re-swept to 12
  rows before emitting.)
category: forward_looking_flagged         grep_count: 23   sweep_count: 23   match: yes
  (22 distinct forward-dated / guidance / target figures, tagged FORWARD_LOOKING throughout
  Table 2, plus 1 FORWARD_LOOKING_GOVERNANCE context row for the blanket disclaimer (slide 36)
  = 23. A script scan restricted to Table 2 rows containing the string "FORWARD_LOOKING"
  returned 23 on first pass; the Forward-Looking Register (Table 3) was initially drafted by
  hand at only 14 curated rows before this script check — re-swept and expanded to all 23 to
  match Table 2 exactly before emitting. Named as a second GATE A2 mismatch-then-resolve
  instance for this run.)
category: total_ledger_rows               grep_count: 439  sweep_count: 439  match: yes
  (mechanical count of markdown table data rows in the emitted ledger file: 37 Slide
  Inventory rows [Table 1] + 379 per-slide disclosure-content rows across all 37 slides
  [Table 2] + 23 Forward-Looking Register rows [Table 3, a cross-referenced subset of Table 2,
  not additive new content]. Verified by an independent script parsing "| ... |" rows against
  their header/separator lines, re-run after the p14 and forward-looking-register fixes above;
  final pass returned 439.)
gate_a2: pass
=== END COUNT TEST ===

---

## SLIDE INVENTORY (Table 1 of 3 — 37 rows, one per slide)

| Slide | Title / Header | Content type | Line range |
|---|---|---|---|
| 1 | Regulation 30 covering letter to BSE/NSE | text (letter) | 35–85 |
| 2 | Corporate Presentation 2026 (cover) | text (title page, decorative) | 86–91 |
| 3 | Business Overview | text (section divider) | 92–94 |
| 4 | Company at a glance | text+infographic (KPI blocks) | 95–131 |
| 5 | A Business Built for Scale | text+infographic | 132–174 |
| 6 | Global Presence, Manufacturing Footprint & Offices | map+photo (OCR) | 175–245 |
| 7 | Journey So Far | timeline/infographic | 246–300 |
| 8 | Experienced Management governed by a Strong Board | text+photo (bios) | 301–343 |
| 9 | Manufacturing Facilities | text+photo | 345–368 |
| 10 | LSAW Pipe | text (spec table) | 370–395 |
| 11 | HSAW Pipe | text (spec table) | 397–422 |
| 12 | ERW Pipe | text (spec table, partly incomplete — see flags) | 424–463 |
| 13 | Coating | text (spec table) | 465–490 |
| 14 | Marquee Clientele across Globe | logo grid (OCR) | 492–535 |
| 15 | Accolades & Certifications | certificate images (OCR, garbled) | 536–693 |
| 16 | Jammu Plant Update | infographic (3 KPI blocks) | 694–712 |
| 17 | Merino Shelters: Monetization of Non-Core Assets | infographic+text | 713–739 |
| 18 | Strategic Acquisition (NPC divider) | text+icons (OCR) | 741–755 |
| 19 | Transaction at a Glance | table+text | 756–793 |
| 20 | Acquisition Structure & Financing | diagram | 794–821 |
| 21 | About National Pipe Company Limited | table+diagram | 823–862 |
| 22 | NPC Key Clients | logo grid | 864–889 |
| 23 | NPC Key Clients Contd.. | logo grid | 891–917 |
| 24 | Why Acquisition Is Better Than Greenfield | comparison table+text | 919–956 |
| 25 | How this Acquisition Creates Value | infographic | 957–1004 |
| 26 | NPC — Financial Summary | table (P&L + cash + ratios) | 1005–1041 |
| 27 | Financial Overview | text (section divider) | 1042–1045 |
| 28 | Annual Standalone Financial Performance | table (INR Mn) | 1046–1083 |
| 29 | Annual Consolidated Financial Performance | table (INR Mn) | 1084–1121 |
| 30 | Consolidated Balance Sheet | table (INR Mn, 2-column) | 1122–1163 |
| 31 | Historical Consolidated Financial Performance | 4 bar charts (INR Mn) | 1164–1200 |
| 32 | Quarterly Consolidated Financial Performance Trend | 4 bar charts (INR Mn) | 1202–1251 |
| 33 | Next 5 years Goal | text (section divider) | 1252–1255 |
| 34 | Piping Towards Higher Utilization Through Global Diversification | text (strategy + guidance) | 1256–1291 |
| 35 | List of Abbreviations | text (glossary) | 1292–1321 |
| 36 | Disclaimer | text (forward-looking-statement disclaimer) | 1323–1356 |
| 37 | THANK YOU / IR contacts | text | 1358–1366 |

DROPPED_SLIDE check: no prior-quarter deck ledger was supplied to this run (flag NO_PRIOR_LEDGER
at header). Cannot test which, if any, slides present in a prior deck are absent here. A3/A4
should source the prior corporate presentation (if one exists) to run this check retroactively.

---

## DISCLOSURE UNITS (Table 2 of 3 — every figure, claim, target, name, chart point, by slide)

Flags key: FORWARD_LOOKING = guidance/target/future-dated figure; ZERO_STANDING = nil/dash
standing line item; OCR_GARBLED = OCR text degraded, value uncertain; NOT_FOUND = labelled field
with no value given in source; RECONCILE_CHECK = flagged for A3 cross-check against another
figure in this or another document; DUP = same figure restated elsewhere in the deck.

### Slide 1 — Covering letter
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 36 | Filing date | September 1, 2026 | |
| 39–45 | Addressee 1 | BSE Limited; Scrip Code 513269 | |
| 39–45 | Addressee 2 | National Stock Exchange; Scrip ID MANINDS | |
| 47 | Subject | Corporate Presentation | |
| 49–50 | Regulatory basis | Regulation 30, SEBI (LODR) Regulations 2015 | |
| 54–56 | Filing purpose/date | Investor/Analyst Meeting held same day, Sep 1 2026 | |
| 64–76 | Digital signature block | Signatory RAHUL RAWAT; timestamp 2026.09.01 11:19:14 +05'30' | |
| 81–82 | Signatory | Rahul Rawat, Company Secretary | |

### Slide 2 — Cover page
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 88–90 | Title text | "Corporate Presentation 2026"; OCR confirms no additional figures on decorative cover | ZERO content beyond title |

### Slide 3 — Section divider
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 93 | Divider text | "Business Overview" — no data | |

### Slide 4 — Company at a glance
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 103 | Track record | 3 Decades of experience | |
| 104 | Capacity claim | 1.6Mn+ MTPA*, API grade LSAW/HSAW/ERW/Coating | footnoted, see L130 |
| 103/110 | Revenue FY22 | ₹2,178 Cr | |
| 103/110 | Revenue FY26 | ₹3,592 Cr | RECONCILE_CHECK vs p29 Total Income 35,925 INR Mn = ₹3,592.5 Cr (matches); vs p29 Revenue-from-Operations line 35,639 INR Mn = ₹3,563.9 Cr (differs — this KPI block uses "Total Income" not "Revenue from Operations" as its FY26 revenue figure) |
| 101–102 | CAGR, revenue FY22→FY26 | 13.4% | |
| 109 | Facility count | 3 state-of-the-art manufacturing facilities | |
| 109 | Geographic reach | Present across 30+ Countries | |
| 110/118 | EBITDA FY22 | ₹218 Cr | |
| 110/118 | EBITDA FY26 | ₹468 Cr | DUP — ties to p29 Consolidated EBITDA 4,679 INR Mn = ₹467.9 Cr |
| 108 | CAGR, EBITDA FY22→FY26 | 21.0% | |
| 116 | Production lines | 10 | |
| 116 | Cumulative pipe supply | 20,000+ KM supplied since inception | |
| 116 | CAGR, PAT FY22→FY26 | 13.8% | |
| 118 | PAT FY22 | ₹102 Cr | |
| 118 | PAT FY26 | ₹171 Cr | DUP — ties to p29 Consolidated PAT 1,705 INR Mn = ₹170.5 Cr |
| 124 | FY26 ROCE | 18.4% | |
| 124 | FY26 ROE | 9.2% | |
| 124 | FY26 Networth | ₹2,087 Cr | |
| 129 | Claim | "Strong Global Presence with critical and complex projects executed worldwide" | qualitative |
| 130 | Footnote | "1.6Mn MTPA includes NPC capacity of 0.43Mn MTPA" | footnote qualifying L104 |

### Slide 5 — A Business Built for Scale
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 137 | Tagline | "Expanding footprint, unlocking capacity across India and Saudi Arabia" | |
| 140 | Section header | "Operating Today" | |
| 144 | India capacity | 1.2Mn+ MTPA | |
| 145 | NPC (Saudi) acquired capacity | 430,000 MTPA | DUP — ties to p19/p21 |
| 148 | Location | Anjar (Gujarat) and Pithampur (M.P.) | |
| 151 | Product claim | Large Diameter Pipes: LSAW, HSAW, ERW and Specialized Coating | |
| 154 | India segment FY26 revenue | ₹3,564 Cr | RECONCILE_CHECK vs slide-4 total FY26 revenue ₹3,592 Cr and vs p29 Revenue-from-Operations ₹3,563.9 Cr (this figure ties almost exactly to Revenue-from-Operations, not to the Total-Income figure used on slide 4 — a basis inconsistency across the deck worth A3 flagging) |
| 148 | NPC capacity split | 250k MT HSAW + 180k MT LSAW | |
| 151 | Certification claim | Aramco-approved vendor | |
| 151–155 | Competitive claim | "Only company in KSA with manufacturing facilities in both LSAW and HSAW capabilities" | |
| 159 | Section header | "Upcoming Greenfield Expansion" | |
| 163–164 | Dammam Coating Plant (KSA) capacity & timeline | 4.0 Mn sq.m; Production Targeted Mar'2027 | FORWARD_LOOKING |
| 164 | Jammu Stainless Steel Plant capacity & timeline | 22,000 MTPA; Production Targeted Mar'2027 | FORWARD_LOOKING; DUP vs p16 |
| 167 | Product claim | 3LPE, FBE and internal coating | |
| 167–169 | Margin claim | "Adds a value-added margin layer" | qualitative, no % given |
| 169–171 | Product/end-market claim | SS seamless mother/pilgered pipes for chemical, defence, marine, nuclear, power, refinery | FORWARD_LOOKING (new line not yet in production) |
| 173 | Strategic claim | "Completes the delivered-pipe offering" | |

### Slide 6 — Global Presence, Manufacturing Footprint & Offices (OCR)
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 178 | Title | Global Presence, Manufacturing Footprint & Offices | |
| 192–193 | Facility 1 | Anjar, Gujarat — LSAW, HSAW & Coating | OCR_GARBLED (page in ocr_pages list) |
| 195–196 | Facility 2 | Pithampur, Madhya Pradesh — HSAW & Coating | OCR_GARBLED |
| 198–199 | Facility 3 | Dhahran, Saudi Arabia — LSAW & HSAW (NPC-MISIC) | OCR_GARBLED |
| 201 | Facility 4 | MSSTL stainless plant, Jammu — under commissioning | OCR_GARBLED |
| 204–206 | Office 1 | Mumbai — Corporate & Registered Office | OCR_GARBLED |
| 207 | Office 2 | New Delhi — Regional Office | OCR_GARBLED |
| 208 | Office 3 | Dubai, UAE — DIFC | OCR_GARBLED |
| 210 | Office 4 | Al Khobar, Saudi Arabia — NPC (MISIC) office | OCR_GARBLED |
| 212–235 | Regional presence claim | Map marks presence across America, Europe, Central Asia, Middle East, Southeast Asia, Far East (6 regions) | OCR_GARBLED, qualitative |

### Slide 7 — Journey So Far (timeline; 18 milestones)
| Line | Year | Milestone | Flags |
|---|---|---|---|
| 249–251 | 1996 | LSAW pipe plant at Pithampur, M.P., capacity 50,000 TPA | |
| 249–252 | 2007 | USD 225mn order from USA; two new HSAW lines of 200,000 MT each | |
| 248–252 | 2019 | First Indian company to export 80-inch diameter, 18-mtr-long, 24mm-thick pipe for water sector project | |
| 253–257 | 1999 | HSAW Plant established, 50,000 TPA & LSAW increased to 135,000 TPA | |
| 254–257 | 2012 | Strategic relationship with Kobe Steel Ltd., Japan | |
| 256–258 | 2023 | ERW unit, 1,25,000 TPA at Anjar, Gujarat; hydrogen pipe testing | |
| 249–252 | 2019 (cont.) | 5-year MoU signed with Aramco Asia India | |
| 254–266 | 2023 | Acquired 100% equity stake in NPC, Saudi Arabia for USD 102 Mn (~₹1,000 Cr) via wholly-owned MISIC | DUP vs p7/19/20/25 conversion; ₹1,000 Cr approximation vs later-stated ₹1,130–1,150 Cr orderbook figure — different metric, not a contradiction, but note both are round "~" estimates |
| 265–268 | 2024 | Additional 50,000 TPA ERW capacity added | |
| 273 | — | Era band labels: 1970–1999, 2000–2006, 2007–2012, 2013–2017, 2018–2024, 2025, FY2026 | |
| 279–282 | 2001 | Coating plant (PE & CTE) at 2mn & 1.6mn sq.mtr | |
| 286–288 | 2005 | New pipe & coating complex, 365,000 TPA LSAW at Anjar, Gujarat | |
| 292–294 | 2006 | 7MW windmill installed in Gujarat for captive consumption | |
| 281–284 | 2016 | Commissioned 5,600 Ton Hydraulic JCO press at Gujarat Plant, developed in-house | |
| 289–292 | 2017 | Concrete Weight Coating (CWC) Plant for offshore pipe projects, 1,25,000 cubic meters p.a. | |
| 281–285 | 2025 | Installed advanced Spiral Mill and PU Coating Facility in Pithampur, expanding capacity by 50,000 TPA | |
| 288–290 | 2025 | Approved as certified vendor of Qatar Energy LNG | |
| 293–294 | 2025 | Merino Shelters Real Estate Asset Monetized | DUP — detail at p17 |

### Slide 8 — Management & Board (11 named individuals)
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 304–310 | Chairman | Dr. Ramesh C. Mansukhani — PhD Int'l Economics & Finance; 50 years in manufacturing; 4 decades industrial experience | |
| 304–315 | Managing Director | Mr. Nikhil Mansukhani — Univ. of London / King's College UK; with company since 2011; 9+ years in steel pipes | |
| 321–330 | Independent Director | Mr. Narendra Mairpady — Ex-Chairman, Indian Overseas Bank; 4 decades banking experience | |
| 321–332 | Independent Director | Mr. Rabi Bastia — Padma Shri; Hydrocarbon industry veteran | |
| 334–339 | Independent Director | Mrs. Renu Jalan — Arts, Marketing, Finance background | |
| 334–339 | Independent Director | Mrs. Esha Padmanabhan Achan — 33 years finance experience, incl. Glenmark, Bajaj | |
| 321–325 | CFO | Mr. Sandeep Kumar Garg | |
| 325–327 | Company Secretary | Mr. Rahul Rawat | DUP vs slide 1/37 |
| 321–322 | Sr. VP – Operations | Mr. Jaspreet Bhatia | |
| 325–327 | Plant Head – Anjar | Mr. Swatantra Joshi | |
| 332–333 | Plant Head – Pithampur | Mr. Sushil Shukla | |

### Slide 9 — Manufacturing Facilities
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 348–349 | Facility footprint | Anjar (Gujarat) + Pithampur (M.P.), combined ~182 acres | |
| 350 | Combined capacity | >1.2 million TPA | DUP vs p5 |
| 352 | Certifications | ISO 9001:2015, ISO 14001:2015, ISO 45001:2018 | |
| 364 | Anjar logistics claim | Easy/fast access to Kandla & Mundra port | |
| 365 | Pithampur logistics claim | Close to national highway; strategically located for domestic market | |

### Slide 10 — LSAW Pipe
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 376 | Outside Diameter | 16" to 56" | |
| 377 | Wall Thickness | 6 mm to 55 mm | |
| 379 | Pipe Length (max) | 12.20 Meters | |
| 381 | Grade | Up to API 5L X-80 | |
| 386–390 | Technology claim | CNC-controlled automatic JCO / 3-Roll Bender (CHR Haeusler, Switzerland); high-speed welding stations | |

### Slide 11 — HSAW Pipe
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 402 | Outside Diameter | 12" to 120" | |
| 404 | Wall Thickness | 6 mm to 25.40 mm | |
| 405 | Pipe Length (max) | 18 meters | |
| 406 | Grade | Up to API 5L X-80 | |
| 412 | Mill design claim | 2-Step HSAW mill; forming/GMAW at one stage, final welding at separate stations | |
| 415–417 | Salient feature 1 | Two-step high-speed mill with online coil-to-coil joining | |
| 415–417 | Salient feature 2 | Coil ultrasonic testing, 100% coverage | |
| 415–417 | Salient feature 3 | 4 inside and 4 outside SAW welding lines | |
| 415–417 | Salient feature 4 | Fully automatic weld ultrasonic testing equipment | |
| 415–417 | Salient feature 5 | Pipe tracking system for complete traceability | |

### Slide 12 — ERW Pipe
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 434 | Coil handling capacity | Entry section handles 32 ton coil weight | |
| 438–439 | QC claim | Strip ultrasonic, 100% coverage, 10% overlap; strip edge milling | |
| 442–445 | Welding tech | FFX Roll Forming with Automation; High-Frequency (1000 KW) Welding | |
| 447–449 | QC claim | Online weld-bead monitoring system for internal bead scarfing | |
| 451–454 | Precision claim | Sizing/pipe milling saw section; close length tolerance | |
| 456–459 | Finishing claim | End facing, hydro tester, offline ultrasonic welding, magnetic particle inspection | |
| 431–459 | Round Pipe OD/WT/Length/Grade | Column headers printed twice ("Outside Diameter / Wall Thickness / Pipe Length / Grade") with NO values filled in for either occurrence — actual round-pipe dimensions not captured in text or OCR (page 12 not in ocr_pages list) | NOT_FOUND — 4 sub-fields (OD, WT, Length, Grade) all missing; genuine data gap, likely a graphic-only value the extraction did not pick up |
| 450–452 | Square/Rect Hollow Section size | 132×132 to 350×350 and 172×92 to 500×200 & 450×250 | |
| 454 | Square/Rect Wall Thickness | 4.0 to 14.0 mm | |
| 456 | Square/Rect Pipe Length | 5.8 to 18.2 Meter | |
| 458 | Square/Rect Grade | IS: 4923, DIN 2440 | |

### Slide 13 — Coating
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 470–471 | External coating systems | FBE/DFBE; 3LPE/3LPP Coating | |
| 474 | Internal coating pipe diameter | 12" to 130" and above | |
| 476 | Internal coating plant capacity | 5 million sq. meters per annum | |
| 481 | CWC OD range | Ø8" to Ø56" | |
| 482 | CWC Wall Thickness | 6 mm – 55.0 mm | |
| 483 | CWC Pipe Length | 9 to 12.2 meter | |
| 484 | CWC Concrete Thickness | 30 to 190 mm | |
| 485 | CWC Coating Capacity | 100 m³/Hr | |

### Slide 14 — Marquee Clientele across Globe (OCR)
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 507–519 | Domestic client 1 | Reliance Industries | OCR_GARBLED |
| 507–519 | Domestic client 2 | Larsen & Toubro | OCR_GARBLED |
| 507–519 | Domestic client 3 | Bharat Petroleum | OCR_GARBLED |
| 507–519 | Domestic client 4 | Gujarat State Petronet | OCR_GARBLED |
| 507–519 | Domestic client 5 | Likely ONGC (garbled: "y ON MA N Ltd") | OCR_GARBLED — name uncertain, flag for verification |
| 523–534 | International client 1 | NPCC | OCR_GARBLED |
| 523–534 | International client 2 | ConocoPhillips | OCR_GARBLED |
| 523–534 | International client 3 | Petrobras | OCR_GARBLED |
| 523–534 | International client 4 | Hyundai Engineering Co., Ltd. | OCR_GARBLED |
| 523–534 | International client 5 | Technip | OCR_GARBLED |
| 523–534 | International client 6 | Shell Global Solutions | OCR_GARBLED |
| 523–534 | International client 7 | Petronas | OCR_GARBLED |

### Slide 15 — Accolades & Certifications (OCR, heavily garbled)
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 546–568 | API Monogram certificate #1 | Anjar, Gujarat; Effective Feb 28, 2024; Expiry May 14, 2027 | OCR_GARBLED |
| 640–663 | API Monogram certificate #2 | License No. 2B-0088; Anjar, Gujarat; Effective May 14, 2024; Expiry May 14, 2027 | OCR_GARBLED; two API certificates with different effective dates for the same plant — RECONCILE_CHECK (scope/renewal difference unclear from OCR) |
| 577–587 | ISO/IEC 27001:2013 | Information Security Management System, assessed by G4S Management Ltd | OCR_GARBLED |
| 604–616 | NABL accreditation | Certificate of Accreditation, Testing Laboratory, Man Industries (India) Ltd | OCR_GARBLED |
| 618–637 | ISO 9001:2015 | Certificate of Registration | OCR_GARBLED |
| 665–684 | ISO 3183:2019 | Certificate of Compliance — steel pipe for petroleum/natural gas transportation systems | OCR_GARBLED |

### Slide 16 — Jammu Plant Update
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 699 | Status claim | "Status as of Q1 FY27" | |
| 709 | Capacity | 22,000 MTPA (stainless steel seamless pipe) | DUP vs p5 |
| 709 | Capex incurred | ₹350 Cr (till Q1 FY27) | actual-to-date, not forward |
| 710 | Total planned capex | ~₹600 Cr for the facility | FORWARD_LOOKING (implies ~₹250 Cr remaining spend) |
| 709 | Production timeline | Mar 2027 | FORWARD_LOOKING; DUP vs p5 |

### Slide 17 — Merino Shelters (Real Estate Monetization)
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 723–724 | Land parcel | 6 Acres, Opp. D.Y Patil Stadium, Navi Mumbai | |
| 723–725 | Profit-share | Company's share of profit in sale of developed area: 30% | |
| 723–724 | Upfront cash received | Rs.70 Cr, after JDA, in Q4FY25 | |
| 723–725 | Guided annual cashflow | Rs.80–120 Cr, from FY28 | FORWARD_LOOKING |
| 731–733 | JDA partner | Paradise Green-Spaces LLP (Paradise Group) | |
| 732 | Guided revenue | Rs.700–800 Cr over next 5–6 years | FORWARD_LOOKING |
| 737 | Regulatory status | Commencement Certificate received for ~20,00,000 sq. ft; RERA registration obtained | |
| 737–738 | Launch guidance | Project launch on track for Mid-September 2026 | FORWARD_LOOKING |
| 738 | Guided cashflow | Expected Rs.35–50 Cr Cashflow in FY27 | FORWARD_LOOKING |

### Slide 18 — Strategic Acquisition (NPC divider, OCR)
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 748–753 | Claim 1 | Manufacturing Synergies | qualitative, OCR_GARBLED |
| 748–753 | Claim 2 | Immediate EBITDA Accretion | qualitative, OCR_GARBLED |
| 749 | Claim 3 | Vision 2030 Play | qualitative, OCR_GARBLED |
| 753 | Claim 4 | Vision 2030 Aligned | qualitative, OCR_GARBLED |

### Slide 19 — Transaction at a Glance
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 761 | Stake acquired | 100% | |
| 762 | Consideration | USD 102 Mn | DUP throughout deck |
| 760–764 | Acquired capacity | 430,000 MT annual production (HSAW+LSAW) | |
| 763 | Certification claim | Aramco Approved, since more than two decades | |
| 771–773 | Acquirer | MAN International Steel Industries Company (MISIC), wholly owned subsidiary of MANINDS | |
| 775–777 | Target | National Pipe Company Limited (NPC), Kingdom of Saudi Arabia | |
| 779 | Transaction type | Acquisition of 100% equity stake in NPC Limited | |
| 782 | Total consideration | USD 102 Million | DUP of L762 |
| 784 | Financing mix | Debt USD 70 million + Equity USD 32 Million | |
| 786–787 | Cash & liquid assets | USD 83.0 Million | DUP vs p26 |
| 787 | Net worth (NPC) | USD 158.6 Million | DUP vs p26 |
| 770–773 | Rationale 1 | Market Access — AVL status with Saudi Aramco | |
| 775–778 | Rationale 2 | Capacity Scale — 430,000 MT combined; existing NPC+Man Group capacity crosses 1.2M MT | |
| 780–784 | Rationale 3 | Saudi Vision 2030 positioning | FORWARD_LOOKING (macro thesis) |
| 785–789 | Rationale 4 | Integrated Player — Dammam coating facility + NPC = end-to-end offering | |

### Slide 20 — Acquisition Structure & Financing
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 803–804 | Ticker | BSE 513269 \| NSE MANINDS | |
| 805–807 | Ownership | MISIC 100% owned by MANINDS | |
| 800–804 | Transaction | MISIC acquires 100% stake in NPC, KSA, for USD 102 Mn | DUP |
| 817 | Equity | USD 32 Mn | DUP |
| 817 | Debt | USD 70 Mn | DUP |
| 817 | Total | USD 102 Mn | DUP |

### Slide 21 — About National Pipe Company Limited
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 828–830 | Annual installed capacity | 430,000 MT | DUP |
| 827–831 | Plant configuration | 1 HSAW & 1 LSAW mill, fully integrated | |
| 828–830 | Aramco relationship | 2+ decades | |
| 827–831 | Certification | API 5L & 2B Certified, Grade B through X80 | |
| 837 | Total installed capacity | 430,000 MTPA | DUP |
| 840–844 | HSAW capacity/mix | 250,000 MT, 58% of total capacity | |
| 847–851 | LSAW capacity/mix | 180,000 MT, 42% of total capacity | |
| 856 | HSAW OD range | 20" – 88" (will be upgraded to 120") | FORWARD_LOOKING |
| 858 | LSAW OD range | 24" – 60" | |
| 859–860 | Wall Thickness range | 6.4 mm – 45 mm | |
| 838–853 | Process description | Pipe Manufacturing (HSAW/LSAW welding methods described) | |
| 838–853 | Process description | Testing & Inspection methods described | |
| 838–853 | Planned expansion | Value-added expansion post-acquisition: external/internal coating mill (FBE, 3LPE, epoxy) | FORWARD_LOOKING |

### Slide 22 — NPC Key Clients (Direct)
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 867 | Relationship claim | 40+ Year relationships with Saudi/GCC leading organizations | |
| 876–877 | Client 1 | Saudi Aramco — Primary Client, 40+ Years | |
| 876–877 | Client 2 | KOC — Kuwait Oil Company | |
| 876–877 | Client 3 | Qatar Petroleum — State Oil Company, Qatar | |
| 876–877 | Client 4 | Bapco Refining — Bahrain Petroleum Company | |
| 882–883 | Client 5 | Saudi Water Authority (SWA) | |
| 882–883 | Client 6 | SWPC — Saudi Water Partnership Company | |
| 882–883 | Client 7 | WTTCO — Water Transmission Company, KSA | |
| 882–884 | Client 8 | National Water Co. — Water Transmission, KSA | |
| 882–884 | Client 9 | ADWEA — Abu Dhabi Water & Electricity Authority | |

### Slide 23 — NPC Key Clients Contd. (EPC Contractors)
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 903 | Contractor 1 | McDermott — Global EPC Contractor | |
| 903 | Contractor 2 | L&T — Larsen & Toubro ECC | |
| 903 | Contractor 3 | SAIPEM — Global EPC Contractor | |
| 903 | Contractor 4 | Subsea 7 — Offshore & Subsea EPC | |
| 903 | Contractor 5 | Hyundai E&C — Engineering & Construction | |
| 910 | Contractor 6 | Sapura — Global EPC Contractor | |
| 910 | Contractor 7 | Petrofac — Oilfield Services & EPC | |
| 910 | Contractor 8 | Lamprell — Engineering & Construction | |
| 910 | Contractor 9 | NPCC — National Petroleum Construction Co. | |
| 910 | Contractor 10 | S.S.E.M. — Saudi Services & EPC Co. | |

### Slide 24 — Why Acquisition Is Better Than Greenfield
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 924 | Framing claim | Build-vs-buy analysis: acquiring NPC vs building a greenfield mill | |
| 931–932 | Capital outlay — Acquire | ~US$102 Mn (US$70 Mn debt + US$32 Mn equity) | DUP |
| 931–932 | Capital outlay — Greenfield | ₹1,500–1,600 Cr (mill, coating line, utilities, land, working capital) | counterfactual estimate, not an actual spend |
| 933–935 | What money buys — Acquire | Capacity + approvals + customers + order book + US$83 Mn cash & liquid assets | DUP |
| 933–935 | What money buys — Greenfield | Capacity only | counterfactual |
| 937 | Time to first revenue — Acquire | Immediate, against existing order book | |
| 937 | Time to first revenue — Greenfield | Three years or more | counterfactual |
| 939 | Time to Aramco approval — Acquire | Already held, continuously since 2005 | |
| 939 | Time to Aramco approval — Greenfield | 1–2 years of plant audits and test lots | counterfactual |
| 941 | Order book day one — Acquire | US$120 Mn, with L1 status on further orders | DUP vs p26 |
| 941 | Order book day one — Greenfield | Nil | ZERO_STANDING (explicit nil comparator) |
| 943 | Earnings accretive — Acquire | 15–18% EBITDA Margin and 11–14% PAT margin | FORWARD_LOOKING / guidance-adjacent (NPC's marketed forward economics, not the CY2025 actuals on p26 which show 24.8% EBITDA margin / 18.1% PAT margin) — RECONCILE_CHECK vs p26 actuals |
| 943 | Earnings accretive — Greenfield | "Takes time to ramp up" | qualitative counterfactual |
| 949–951 | Risk claim 1 | "Zero Revenue & Approvals Cannot Be Built" — years of servicing capex with no approved-vendor sales | |
| 949–951 | Risk claim 2 | "Commissioning Slippage" avoided by acquisition | |
| 949–955 | Risk claim 3 | "Customers From Zero" — no relationships/track record in greenfield case | |
| 954–955 | Closing rationale | "MAN secured an operating platform... accelerating market entry without adding new supply to Saudi Arabia" | |

### Slide 25 — How this Acquisition Creates Value
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 962–968 | Synergy claim 1 | ~1.60 MTPA combined steel procurement synergy | |
| 965–968 | Synergy claim 2 | Dammam coating & double-joint facility to enable value-added services | FORWARD_LOOKING |
| 962–965 | Synergy claim 3 | NPC's 430,000 MTPA capacity offers utilization headroom as throughput ramps | FORWARD_LOOKING |
| 993–997 | Order book (repeat) | US$120 Mn immediate order book | DUP vs p24/p26 |
| 992–1000 | Balance sheet (repeat) | US$83 Mn cash & liquid assets; zero debt at closing | DUP vs p19/p26 |
| 984–988 | Vendor status (repeat) | Aramco approved-vendor status held since 2005 | DUP |
| 972–981 | Synergy category label 1 | Revenue & Margin synergies | |
| 972–981 | Synergy category label 2 | Cost synergies | |
| 972–981 | Synergy category label 3 | Capital synergies | |
| 972–981 | Synergy category label 4 | Customer moat / increase wallet share | |
| 972–981 | Synergy category label 5 | Operating leverage | |
| 972–981 | Synergy category label 6 | Faster capacity monetization | |

### Slide 26 — NPC Financial Summary (CY2025, SAR M / USD M) — dense table page
| Line | Unit | SAR M | USD M | Flags |
|---|---|---|---|---|
| 1008 | Units note | "Figures in SAR M & USD M \| CY2025" | |
| 1013 | Revenue | 792.7 | 211.4 | |
| 1014 | Gross Profit | 214.1 | 57.1 | |
| 1015 | Gross Margin (%) | — | 27.0% | |
| 1016 | EBITDA | 196.7 | 52.5 | |
| 1017 | EBITDA Margin (%) | — | 24.8% | RECONCILE_CHECK vs p24's marketed "15–18% EBITDA Margin" |
| 1018 | Depreciation | 31.8 | 8.5 | |
| 1019 | EBIT | 164.9 | 44.0 | |
| 1021 | EBIT Margin (%) | — | 20.8% | |
| 1022 | Finance Cost | 3.7 | 1.0 | |
| 1023 | Other Income | 0.8 | 0.2 | |
| 1025 | PBT | 162.0 | 43.2 | |
| 1027 | PBT Margin (%) | — | 20.4% | |
| 1029 | Tax & Zakat | 18.5 | 4.9 | |
| 1030 | Tax Rate (%) | — | 11.4% | |
| 1032 | PAT | 143.5 | 38.3 | |
| 1034 | PAT Margin (%) | — | 18.1% | RECONCILE_CHECK vs p24's marketed "11–14% PAT margin" |
| 1014 | Cash & Bank Balances (Apr'26) | 142.5 | 38.0 | |
| 1015 | Trade Receivables (Apr'26) | 48.8 | 13.0 | |
| 1016 | Finished Goods Inventory (Apr'26) | 120.0 | 32.0 | |
| 1017 | Total Cash & Liquid Assets (Apr'26) | 311.3 | 83.0 | DUP vs p19/p24/p25 |
| 1018 | Net Worth (Apr'26) | 594.9 | 158.6 | DUP vs p19 |
| 1020 | Debt claim | "Zero Debt — Debt-free company" | |
| 1024 | ROE (%) | — | 25.7% | |
| 1026 | ROCE (%) | — | 29.5% | |
| 1028 | ROA (%) | — | 22.5% | |
| 1031–1033 | Orderbook note | USD 120 Million (₹1,130–1,150 crore), incl. executed to date; L1 status on additional orders; "healthy bid pipeline reflecting strong near-term order inflow visibility" | DUP order-book figure; FORWARD_LOOKING (bid-pipeline visibility clause) |
| 1038 | Conversion footer | SAR/INR 23.955; SAR/USD 3.75 (pegged); CY2025 Revenue = INR ~1,898.9 Cr; PAT = INR ~343.6 Cr | source-inline constants, used as given |

### Slide 27 — Section divider
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 1044 | Divider text | "Financial Overview" — no data (OCR confirms garbled decorative background only) | |

### Slide 28 — Annual Standalone Financial Performance (INR Millions; x0.1 = Rs Cr)
| Line | Particular | FY26 (INR Mn) | FY25 (INR Mn) | Y-o-Y | FY26 Rs Cr | FY25 Rs Cr | Flags |
|---|---|---|---|---|---|---|---|
| 1049 | Units note | "*All figures reported in INR Millions, except for EPS" | | | | | |
| 1054 | Revenue from Operations | 34,552 | 31,182 | 10.8% | 3,455.2 | 3,118.2 | |
| 1056 | Other Income | 531 | 542 | (2.0)% | 53.1 | 54.2 | |
| 1058 | Total Income | 35,083 | 31,724 | 10.6% | 3,508.3 | 3,172.4 | |
| 1060 | Operating expenses | 30,155 | 28,415 | 6.1% | 3,015.5 | 2,841.5 | |
| 1062 | EBITDA* | 4,928 | 3,309 | 48.9% | 492.8 | 330.9 | |
| 1064 | EBITDA Margins (%) | 14.0% | 10.4% | 360 Bps | | | |
| 1066 | Depreciation and amortization | 756 | 433 | 74.6% | 75.6 | 43.3 | |
| 1068 | Finance costs | 1,542 | 1,022 | 50.9% | 154.2 | 102.2 | |
| 1070 | PBT | 2,630 | 1,854 | 41.8% | 263.0 | 185.4 | |
| 1072 | Tax | 672 | 484 | 39.0% | 67.2 | 48.4 | |
| 1074 | PAT | 1,958 | 1,370 | 42.8% | 195.8 | 137.0 | |
| 1076 | PAT Margins (%) | 5.6% | 4.3% | 130 Bps | | | |
| 1080 | Footnote | "EBITDA is inclusive of Other Income, since it's operational in nature" | | | | | qualifies EBITDA rows |

### Slide 29 — Annual Consolidated Financial Performance (INR Millions; x0.1 = Rs Cr)
| Line | Particular | FY26 (INR Mn) | FY25 (INR Mn) | Y-o-Y | FY26 Rs Cr | FY25 Rs Cr | Flags |
|---|---|---|---|---|---|---|---|
| 1087 | Units note | "*All figures reported in INR Millions, except for EPS" | | | | | |
| 1092 | Revenue from Operations | 35,639 | 35,054 | 1.7% | 3,563.9 | 3,505.4 | RECONCILE_CHECK vs slide-5 ₹3,564 Cr (matches) and vs slide-4 ₹3,592 Cr (does not match — slide 4 uses Total Income) |
| 1094 | Other Income | 286 | 200 | 43.2% | 28.6 | 20.0 | |
| 1096 | Total Income | 35,925 | 35,253 | 1.9% | 3,592.5 | 3,525.3 | DUP — ties to slide-4 ₹3,592 Cr FY26 "Revenue" KPI |
| 1098 | Operating expenses | 31,246 | 31,690 | (1.4)% | 3,124.6 | 3,169.0 | |
| 1100 | EBITDA* | 4,679 | 3,563 | 31.3% | 467.9 | 356.3 | DUP — ties to slide-4 ₹468 Cr |
| 1102 | EBITDA Margins (%) | 13.0% | 10.1% | 290 Bps | | | |
| 1104 | Depreciation and amortization | 789 | 453 | 74.4% | 78.9 | 45.3 | |
| 1106 | Finance costs | 1,520 | 1,027 | 48.1% | 152.0 | 102.7 | |
| 1108 | PBT | 2,370 | 2,084 | 13.7% | 237.0 | 208.4 | |
| 1110 | Tax | 665 | 552 | 20.4% | 66.5 | 55.2 | |
| 1112 | PAT | 1,705 | 1,532 | 11.3% | 170.5 | 153.2 | DUP — ties to slide-4 ₹171 Cr |
| 1114 | PAT Margins (%) | 4.7% | 4.3% | 40 Bps | | | |
| 1118 | Footnote | "EBITDA is inclusive of Other Income, since it's operational in nature" | | | | | qualifies EBITDA rows |

### Slide 30 — Consolidated Balance Sheet (FY24/FY25/FY26, INR Millions; x0.1 = Rs Cr)
| Line | Particular (Equity & Liabilities) | FY24 | FY25 | FY26 | Flags |
|---|---|---|---|---|---|
| 1125 | Units note | "*All figures reported in INR Millions" | | | |
| 1130 | Equity Share Capital | 324 | 324 | 375 | |
| 1132 | Other Equity | 13,725 | 15,749 | 20,490 | |
| 1134 | Shareholders Fund | 14,049 | 16,073 | 20,865 | |
| 1138 | Long-term Borrowings | 1,363 | 1,385 | 2,402 | |
| 1139 | Lease Liabilities (non-current) | 141 | 156 | 610 | |
| 1140 | Deferred tax liabilities (net) | 258 | 276 | 258 | |
| 1142 | Other long term liabilities | 42 | 73 | 97 | |
| 1144 | Total Non-current Liabilities | 1,803 | 1,890 | 3,367 | |
| 1148 | Short-term Borrowings | 1,722 | 3,175 | 2,595 | |
| 1149 | Lease Liabilities (current) | 34 | 47 | 674 | |
| 1150 | Trade payables | 5,028 | 12,002 | 14,712 | |
| 1152 | Current tax liabilities | 54 | 21 | 275 | |
| 1154 | Other financial liabilities | 278 | 301 | 5,797 | |
| 1156 | Other current liabilities | 1,184 | 4,283 | 1,921 | |
| 1158 | Total Current Liabilities | 8,300 | 19,829 | 25,974 | |
| 1159 | Total Equity and Liabilities | 24,152 | 37,792 | 50,206 | |

| Line | Particular (Assets) | FY24 | FY25 | FY26 | Flags |
|---|---|---|---|---|---|
| 1131 | Property, Plant and Equipment | 5,234 | 5,539 | 6,546 | |
| 1133 | Right-of-use Assets | 163 | 186 | 1,389 | |
| 1135 | Capital WIP | 305 | 1,334 | 3,258 | |
| 1136 | Goodwill on Consolidation | 639 | 688 | 688 | |
| 1137 | Investment Properties | 14 | 14 | 14 | |
| 1138 | Intangible assets | - | 5 | 3 | ZERO_STANDING (FY24 "-") |
| 1139 | Trade Receivables (non-current) | 967 | 973 | 2,385 | |
| 1140 | Other Financial Assets (non-current) | 173 | 524 | 154 | |
| 1141 | Other Non-current Assets | 658 | 1,023 | 438 | |
| 1143 | Total non-current assets | 8,154 | 10,286 | 14,875 | |
| 1147 | Inventories | 6,456 | 12,685 | 15,350 | |
| 1148 | Investments | 2,280 | 260 | 708 | |
| 1149 | Trade Receivables (current) | 3,551 | 8,959 | 10,098 | |
| 1150 | Cash & Bank Balances | 2,549 | 3,792 | 6,572 | |
| 1151 | Loans | 22 | 2 | 157 | |
| 1153 | Other Financial Assets (current) | 105 | 98 | 201 | |
| 1155 | Other Current Assets | 1,035 | 1,710 | 2,245 | |
| 1157 | Current Tax Assets | - | - | - | ZERO_STANDING — all three periods dash. Grep-by-digit misses this row entirely; caught only on manual sweep. This is the row named in the GATE A2 mismatch-and-resolve note above. |
| 1158 | Total Current Assets | 15,998 | 27,506 | 35,331 | |
| 1159 | Total Assets | 24,152 | 37,792 | 50,206 | |

### Slide 31 — Historical Consolidated Financial Performance (4 bar charts, FY23–FY26, INR Millions)
| Line | Series | FY23 | FY24 | FY25 | FY26 | Flags |
|---|---|---|---|---|---|---|
| 1167 | Units note | "*All figures reported in INR Millions, except for EPS" | | | | |
| 1174–1180 | Total Income* — value | 22,703 | 31,942 | 35,253 | 35,925 | DUP FY25/FY26 vs p29 |
| 1174–1180 | Gross Profit* — value | 4,973 | 7,907 | 7,905 | 13,639 | RECONCILE_CHECK — FY26 jump to 13,639 (38.0% margin) vs FY23-25 range 4,973-7,907 (21.9-24.8%) is a step-change out of trend, flag for A3 forensic review of composition (NPC consolidation partial-period effect from May 2026 acquisition is a plausible driver, per p32 footnote, but the deck does not itself reconcile this jump) |
| 1178 | Gross Profit* — margin (%) | 21.9% | 24.8% | 22.4% | 38.0% | RECONCILE_CHECK — same flag as above |
| 1187–1195 | EBITDA* — value | 1,760 | 2,932 | 3,563 | 4,679 | DUP FY25/FY26 vs p29 |
| 1191–1193 | EBITDA* — margin (%) | 7.8% | 9.2% | 10.1% | 13.0% | DUP vs p29 |
| 1187–1195 | PAT — value | 670 | 1,051 | 1,532 | 1,705 | DUP FY25/FY26 vs p29 |
| 1193–1194 | PAT — margin (%) | 3.0% | 3.3% | 4.3% | 4.7% | DUP vs p29 |
| 1198 | Footnote | "Total Income is inclusive of Other Income, since it's operational in nature" | | | | |

### Slide 32 — Quarterly Consolidated Financial Performance Trend (4 bar charts, Q1FY26–Q1FY27, INR Millions)
| Line | Series | Q1FY26 | Q2FY26 | Q3FY26 | Q4FY26 | Q1FY27 | Flags |
|---|---|---|---|---|---|---|---|
| 1204–1205 | Units note | "*All figures reported in INR Millions, except for EPS" | | | | | |
| 1209–1212 | Total Income* — value | 7,736 | 8,148 | 8,386 | 11,655 | 10,650 | |
| 1208–1218 | Gross Profit* — value | 1,833 | 2,128 | 3,409 | 6,269 | 3,820 | RECONCILE_CHECK vs p31 FY26 annual GP 13,639 — sum of quarterly GP shown here (1,833+2,128+3,409+6,269=13,639) reconciles exactly to FY26 annual, confirming the p31 FY26 jump is genuine per this deck's own arithmetic, concentrated in Q3-Q4 FY26 |
| 1216–1218 | Gross Profit* — margin (%) | 23.7% | 26.1% | 40.6% | 53.8% | 35.9% | RECONCILE_CHECK — same step-change pattern, Q3/Q4 FY26 |
| 1226–1234 | EBITDA* — value | 806 | 1,018 | 1,376 | 1,480 | 1,553 | |
| 1229–1236 | EBITDA* — margin (%) | 10.4% | 12.5% | 16.4% | 12.7% | 14.6% | |
| 1226–1233 | PAT — value | 276 | 370 | 550 | 509 | 614 | |
| 1232–1236 | PAT — margin (%) | 3.6% | 4.5% | 6.6% | 4.4% | 5.8% | |
| 1242–1250 | Footnote | "Q1 FY27 financials reflect only 40 days of NPC's contribution, following completion of 100% acquisition on 21st May 2026... full financial impact and earnings contribution from NPC are expected to be reflected from Q2 FY27 onwards" | | | | | IMPORTANT — governs interpretation of every Q1FY27 figure on this page; feeds directly into A3/A4 base-rate questions on Q2FY27 guidance |

### Slide 33 — Section divider
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 1254 | Divider text | "Next 5 years Goal" — no data (OCR confirms garbled decorative background only) | |

### Slide 34 — Piping Towards Higher Utilization Through Global Diversification (5-year strategy/guidance page)
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 1259–1264 | Framing | "Optimize overall utilization by relocating spare capacity... diversifying into high-growth geographies... shifting mix toward higher-margin products" | |
| 1263–1268 | Strategy 1 | Relocation of spare capacity: identify overseas locations with demand visibility | FORWARD_LOOKING |
| 1263–1274 | Strategy 2 | Diversification into new geographies using existing product offering | FORWARD_LOOKING |
| 1263–1281 | Strategy 3 | Focus on higher-margin products: prioritize Stainless Steel pipes, coating and bends | FORWARD_LOOKING |
| 1285–1288 | Strategy 4 | Optimizing production: debottlenecking to enhance capacity utilization | FORWARD_LOOKING |
| 1277–1279 | Guidance target 1 | Revenue CAGR of 20–25% over next 5 years, led by capacity relocation + new-geography entry | FORWARD_LOOKING — headline 5-year guidance |
| 1281–1286 | Guidance target 2 | EBITDA margin improving to a long-term stable rate of 15%, driven by utilization, SS mix shift, value-added offerings, geographic diversification | FORWARD_LOOKING — headline 5-year guidance; RECONCILE_CHECK vs FY26 actual consolidated EBITDA margin of 13.0% (p29) — implies ~200bps further expansion sought |

### Slide 35 — List of Abbreviations
| Line | Abbreviation | Expansion |
|---|---|---|
| 1296 | API | American Petroleum Institute |
| 1298 | FBE | Fusion Bonded Epoxy Coating |
| 1300 | DEBE | Dual Fusion Bonded Coating (likely "DFBE" — possible typo in source) |
| 1302 | CWC | Concrete Weight Coating |
| 1304 | NDT | Non-Destructive Testing |
| 1306 | CNC | Computer Numeric Control |
| 1308 | GMAW | Gas Metal Arc Welding |
| 1310 | LPE | 3 Layer Polyethylene Coating |
| 1312 | LPP | 3 Layer Polypropylene Coating |
| 1314 | ERW | Electric Resistance Welded |
| 1316 | HSAW | Helically Submerged Arc Welded |
| 1318 | LSAW | Longitudinal Submerged Arc Welded |

### Slide 36 — Disclaimer
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 1327–1351 | Forward-looking-statement disclaimer | Standard risk-factor disclaimer; governs interpretation of every guidance/target figure in this deck (Company disclaims obligation to update forward-looking statements) | FORWARD_LOOKING_GOVERNANCE — applies as context to all FORWARD_LOOKING rows above, not a figure itself |

### Slide 37 — Thank You / IR contacts
| Line | Unit | Detail | Flags |
|---|---|---|---|
| 1363–1366 | Contact 1 | Mr. Vijay Gyanchandani, DGM – Investor Relations; +91 9619438448; Vijay.gyanchandani@maninds.org | |
| 1363–1365 | Contact 2 | Mr. Rahul Rawat, Company Secretary; cs@maninds.org | DUP vs slide 1/8 |

---

## FORWARD-LOOKING / GUIDANCE REGISTER (Table 3 of 3 — every FORWARD_LOOKING-flagged row in
Table 2, cross-referenced here; 23 rows = 22 distinct forward-dated figures/targets + 1
governance/context row for the blanket disclaimer)

| # | Slide | Line | Figure | Flag |
|---|---|---|---|---|
| 1 | 5 | 163–164 | Dammam Coating Plant (KSA), 4.0 Mn sq.m — Production Targeted Mar'2027 | FORWARD_LOOKING |
| 2 | 5 | 164 | Jammu Stainless Steel Plant, 22,000 MTPA — Production Targeted Mar'2027 | FORWARD_LOOKING; DUP vs p16 |
| 3 | 5 | 169–171 | SS seamless mother/pilgered pipes for chemical, defence, marine, nuclear, power, refinery — new line not yet in production | FORWARD_LOOKING |
| 4 | 16 | 710 | Total planned capex ~₹600 Cr for Jammu facility (vs ₹350 Cr incurred to Q1 FY27; implies ~₹250 Cr remaining spend) | FORWARD_LOOKING |
| 5 | 16 | 709 | Jammu production timeline: Mar 2027 | FORWARD_LOOKING; DUP vs p5 |
| 6 | 17 | 723–725 | Rs.80–120 Cr guided annual cashflow from FY28 (Merino Shelters) | FORWARD_LOOKING |
| 7 | 17 | 732 | Rs.700–800 Cr guided revenue over next 5–6 years (Merino Shelters) | FORWARD_LOOKING |
| 8 | 17 | 737–738 | Project launch on track for Mid-September 2026 (Merino Shelters) | FORWARD_LOOKING |
| 9 | 17 | 738 | Expected Rs.35–50 Cr cashflow in FY27 (Merino Shelters) | FORWARD_LOOKING |
| 10 | 19 | 780–784 | Saudi Vision 2030 positioning (macro thesis) | FORWARD_LOOKING |
| 11 | 21 | 856 | HSAW OD 20"–88", will be upgraded to 120" (NPC) | FORWARD_LOOKING |
| 12 | 21 | 838–853 | Planned value-added expansion post-acquisition: coating mill (NPC) | FORWARD_LOOKING |
| 13 | 24 | 943 | Earnings accretive: 15–18% EBITDA margin, 11–14% PAT margin (NPC, marketed forward economics) | FORWARD_LOOKING; RECONCILE_CHECK vs p26 CY2025 actuals (24.8% EBITDA margin / 18.1% PAT margin) |
| 14 | 25 | 965–968 | Dammam coating & double-joint facility to enable value-added services | FORWARD_LOOKING |
| 15 | 25 | 962–965 | NPC's 430,000 MTPA capacity offers utilization headroom as throughput ramps | FORWARD_LOOKING |
| 16 | 26 | 1031–1033 | Healthy bid pipeline, "strong near-term order inflow visibility" (NPC orderbook) | FORWARD_LOOKING (qualitative) |
| 17 | 34 | 1263–1268 | Strategy: relocation of spare capacity to overseas locations with demand visibility | FORWARD_LOOKING |
| 18 | 34 | 1263–1274 | Strategy: diversification into new geographies using existing product offering | FORWARD_LOOKING |
| 19 | 34 | 1263–1281 | Strategy: focus on higher-margin products — Stainless Steel, coating, bends | FORWARD_LOOKING |
| 20 | 34 | 1285–1288 | Strategy: optimizing production via debottlenecking | FORWARD_LOOKING |
| 21 | 34 | 1277–1279 | Revenue CAGR of 20–25% over next 5 years | FORWARD_LOOKING — headline 5-year guidance |
| 22 | 34 | 1281–1286 | EBITDA margin to long-term stable rate of 15% | FORWARD_LOOKING — headline 5-year guidance; RECONCILE_CHECK vs FY26 actual 13.0% (p29) |
| 23 | 36 | 1327–1351 | Blanket forward-looking-statement disclaimer | FORWARD_LOOKING_GOVERNANCE (context, not a figure) |

---

## SUMMARY COUNTS

- Slides enumerated: 37 / 37 (Table 1, Slide Inventory)
- Content-bearing slides (at least 1 disclosure unit beyond the bare title): 33 of 37
  (all except pure dividers/cover: slides 2, 3, 27, 33)
- Per-slide disclosure-content rows (Table 2, all 37 slides): 379
- Financial table line items (pp.28–30, structured P&L/Balance Sheet captions): 60
- Chart data points (pp.31–32, individual values incl. margin series): 63,
  carried in 18 ledger rows (9 series-rows per page x 2 pages, each row spanning
  multiple FY/quarter columns)
- NPC financial-summary rows (p.26, one slide): 28 total
  (24 caption-matched P&L/cash/ratio rows + 4 non-caption rows: units note, Zero-Debt claim,
  orderbook note, conversion-constant footer)
- Named entities (board/mgmt, clients, certifications, EPC contractors), one row each: 48
- Zero/dash-valued standing items (ZERO_STANDING): 3
  (p30 Intangible assets FY24 dash; p30 Current Tax Assets all-3-periods dash;
  p24 Greenfield order-book-on-day-one "Nil")
- OCR_GARBLED-flagged rows: 31 (slides 6, 14, 15, 18 — all 4 pages in the A1 header's
  ocr_pages list that carry named/dated content; p27 and p33, also in ocr_pages, are
  content-free dividers and carry no OCR_GARBLED rows)
- NOT_FOUND rows: 1 (slide 12, Round Pipe OD/WT/Length/Grade — 4 labelled sub-fields with no
  value given in source, combined into a single ledger row)
- Forward-looking / guidance units distinctly flagged: 23 rows in Table 2 (22 distinct
  forward-dated figures/targets + 1 FORWARD_LOOKING_GOVERNANCE context row for the blanket
  disclaimer), all cross-referenced in Table 3, Forward-Looking Register
- RECONCILE_CHECK flags raised for A3: 12 rows across 5 distinct issues (slide-4-vs-slide-5-
  vs-p29 revenue-basis inconsistency [Total Income vs Revenue from Operations], 3 rows;
  p24 NPC margin guidance vs p26 NPC CY2025 actuals, 2 rows; two API Monogram certificates
  with different effective dates for the same plant, 1 row; p31 FY26 gross-profit step-change,
  cross-checked and confirmed by p32's quarterly sum, 2 rows; p26/p34 EBITDA-margin-guidance
  vs FY26 actual, 1 row; remaining rows are DUP cross-references noted inline)
- Total ledger rows emitted (Table 1 + Table 2 + Table 3, mechanically counted): 439
