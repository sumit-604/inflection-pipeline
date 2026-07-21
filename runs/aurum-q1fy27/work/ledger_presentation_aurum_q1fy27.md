# A2 COMPLETENESS LEDGER — Aurum PropTech, Q1 FY27, Investor Presentation

Source: `extract_presentation_aurum_q1fy27.txt` (34 pages / 34 formfeeds / 1101
content lines per A1 header; OCR pages 3, 10, 14, 18, 23, 25, 27; 100% page
coverage). Disclosure unit = slide. No prior-quarter presentation ledger was
supplied with this task, so the `DROPPED_SLIDE` diff (item 3 of the
INVESTOR PRESENTATION enumeration rules) cannot be run this cycle — flagged
`DATA_GAP_PRIOR_LEDGER` below rather than silently skipped.

```
=== A2 COUNT TEST ===
category: slides                 grep_count: 34   sweep_count: 34   match: yes
category: ocr_slides              grep_count: 7    sweep_count: 7    match: yes
category: footnotes/source_lines  grep_count: 8    sweep_count: 8    match: yes
category: line_items (P&L table, slide 26)
                                   grep_count: 17   sweep_count: 17   match: yes
                                   (raw digit-line grep on the table's line
                                   span first returned 18; the extra hit was
                                   the wrapped narrative annotation "...ratios
                                   from Q1FY26 to Q1FY27" beside the table,
                                   not a table row — excluded after re-sweep,
                                   pattern refined to label+two-decimal-value
                                   rows, both counts then agree at 17)
category: board_directors         grep_count: 8    sweep_count: 8    match: yes
                                   (raw designation/name-line grep returned 9
                                   hits because "Mr. Ashish Deora" wraps
                                   across two source lines; deduped to 8
                                   unique directors on re-sweep)
category: leadership_team         grep_count: 12   sweep_count: 12   match: yes
category: digital_signature_blocks grep_count: 1   sweep_count: 1    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

---

## TABLE 1 — Slide-by-slide master enumeration (34/34)

Printed footer number = PDF page number − 1 for all content slides (verified
by direct grep of trailing footer digits: page 3→"2", page 4→"3", page
26→"25", page 27's OCR garble even contains a stray misread "26" at its own
footer position, consistent with the pattern). Page 1 (cover letter) and
page 2 (subsidiary note) carry no printed footer.

| Slide (pg) | Printed # | Line start | OCR? | Title / Topic | Content type | Key disclosures (anchored) | Flags |
|---|---|---|---|---|---|---|---|
| 1 | — | 15 | No | Reg. 30 cover letter to BSE/NSE | Text (regulatory letter) | BSE Scrip 539289, NSE symbol AURUM (l.25); digitally signed by Pranali Pratap Desale, Company Secretary & Compliance Officer, 2026.07.21 08:51:38 +05'30' (l.44-52) | SIGNATURE_BLOCK |
| 2 | — | 54 | No | Subsidiary-attribution note + AI-generation watermark | Text | "All products/services... operated through wholly-owned subsidiaries & other subsidiaries" (l.55) | — |
| 3 | 2 | 61 | Yes | Disclaimer | Text (legal) | Forward-looking-statement language, no-offer/no-solicitation language (l.67-91) | OCR_SOURCED |
| 4 | 3 | 101 | No | Quarterly Financial Performance Q1FY27 vs Q1FY26 | Chart (3 charts, jumbled column order in extraction) | Total Income ₹Cr: Q1FY26=77, Q1FY27=121, +57% YoY (l.108-126); segment split of the 121: Rental 56, Distribution 56, Others 9 (l.110,118,124); Adj. EBITDA%: -3% → 10%, +1320bps (l.107,115-116); PBT Margin%: -14% → 2%, +1590bps (l.119-123) | RECONCILE_CHECK (Others=9 here vs Capital=₹2Cr on slide 5) |
| 5 | 4 | 130 | No | Segmental Financial Performance Q1FY27 | Table/infographic | Rental 46% mix, ₹56Cr revenue, ₹2Cr segment profit (l.135-143); Distribution 46% mix, ₹56Cr revenue, ₹8Cr segment profit (l.135-143); Capital <2% mix, ₹2Cr revenue, (₹5) Lakhs segment LOSS (l.135-143); footnote: other income excluded, ₹6.24Cr finance cost/unallocable expense removed from segmental split (l.167) | RECONCILE_CHECK, footnote qualifies headline segment numbers |
| 6 | 5 | 169 | No | Key Business Performance Metrics Q1FY27 vs Q1FY26 | Table (5-column KPI grid) | Consolidated: +57% Total Income growth, +1320bps Adj EBITDA%, +1590bps PBT margin% (l.176-177); Rental Marketplace: 9,278 Signed Units (-28%), 16,463 Beds under Mgmt (-8%), ₹34Cr Rent Collected/GMV, 81% Occupancy, ₹25L Net Revenue/Team Member (l.187-196); Distribution/Data Analytics: 276 Projects (+20%), 1,34,221 Leads Sold (+77%), ₹1.3Cr Rev/Team Member (l.187-196); Real estate CRM: 11,814 Active Licenses (+41%), 53% Gross Margin, ₹48L Rev/Team Member (l.187-196); Home buying advisory: 6,621 Transactions, ₹784Cr Value of homes sold, ₹32L/₹27L Rev/Team Member (l.187-196) | column-to-metric mapping ambiguous in raw extraction order — flag for A3/A4 verification against source PDF layout |
| 7 | 6 | 207 | No | Key Business Updates (qualitative, per offering) | Text (bullets with embedded stats) | 9,200+ rentable units, 4,855 houses, 320 rooms signed, 25 live Nestaway Select clusters, 4.3+ avg rating (l.220-233); 255+ active co-living spaces, 16+ cities, HelloWorld 2.0 rebrand (l.220-229); 145+ active clients, 275+ projects signed, 1,34,000+ leads sold (+77% YoY), AI suite launch — Aurum Lens/Converse/Qonvo (l.220-234); 20+ new developers onboarded, 400+ new licenses, 18 customers on AI Calling (l.220-233); 155+ active developer clients, 11 active mandates, 60% YoY gross commission growth (l.220-233) | — |
| 8 | 7 | 241 | No | Business Value Optimization — AI Transformation | Text (qualitative, no hard numbers) | AI stack narrative across 4 value-chain stages (service/retention, demand/marketing, sales conversion, transaction/closure) | — |
| 9 | 8 | 273 | No | Approval of 100% acquisition of Housing.com | Text/infographic (M&A announcement) | Housing.com: ₹301Cr FY25 revenue, 12Mn+ MAU, 58Mn+ monthly traffic, 1Mn+ active listings, 1,700+ active developers, 18,500+ active partners, 11,500+ paying consumers (l.279-284); deal: 1,97,93,309 new Aurum equity shares issued to REA India (all-equity consideration), REA India total post-deal stake ~24.9% (l.298-300) | MATERIAL_TRANSACTION, RPT_WATCH (REA India becomes ~24.9% shareholder — future related-party lens) |
| 10 | 9 | 306 | Yes | Section divider — "About Us, Our Offerings" | Photo/graphic | OCR near-total failure; only "9" (footer) and "Generated by Aurum AI Team" watermark recovered (l.327-328) | OCR_SOURCED, LOW_INFORMATION_CONTENT |
| 11 | 10 | 330 | No | Emergence of PropTech in India | Chart + text | PropTech market USD Bn: CY20=2.74, CY25=20, CY30=87.61 (l.334-341); >90% buyers use digital channels, 58% use virtual tours, 60% S&M budget on digital, 75% channel partners use tech tools (l.354-367); 5-era adoption timeline Early2000s→2000-2010→2011-2019→2020-2025→Current (l.335-367); source: CareEdge, Knight Frank, Grant Thornton (l.370) | — |
| 12 | 11 | 372 | No | About us | Table (talent pool by city) + stats | Talent pool: Delhi NCR 273, Bangalore 251, Mumbai 179, Pune 169, Hyderabad 40, Other Cities 145 (l.380-390); 10 Entrepreneurs, 10+ Products, 1000+ Team Members, 1100+ developer relations, 25,000+ Active Customers, 25,700+ Rental Units Capacity (l.395-401); footnote "Data as on 30th June 2026" (l.405) | — |
| 13 | 12 | 407 | No | Our Key PropTech Offerings (Rental/Distribution/Capital taxonomy) | Text (qualitative, no numbers) | Segment taxonomy overview only | ZERO_STANDING-adjacent (no metrics on this slide at all — flagged as a genuinely data-free slide, not a missed enumeration) |
| 14 | 13 | 435 | Yes | Section divider — "Rental PropTech Opportunity, Offerings" | Photo/graphic | OCR near-total failure; only footer "13" and watermark recovered (l.451-452) | OCR_SOURCED, LOW_INFORMATION_CONTENT |
| 15 | 14 | 454 | No | PropTech Opportunity Rentals | Chart + table | Rental market USD Bn: CY20=0.8, CY25=6.1, CY30=26.7 (l.458-469); demand 2 crore rental units, 23x demand-supply gap, organized supply 9 lakh units (l.474-485); age-band pricing: 18-26yrs ₹8,500-16,000 rent, 27-34yrs ₹20,000-80,000 rent (l.461-472); source: Aurum Research, Care EDGE (l.491) | — |
| 16 | 15 | 493 | No | Nestaway | Text (business model) | 10% recurring commission (owner side), 5% blended commission (tenant side) (l.498-499) | — |
| 17 | 16 | 524 | No | HelloWorld | Text/infographic | Agreement tenure 5-7 yrs (property sourcing), lock-in typically 1-2 yrs (l.538-544); 16+ cities presence, 255+ co-living spaces, 16,460+ rental units under management (l.547-558) | — |
| 18 | 17 | 566 | Yes | Section divider — "Distribution PropTech Opportunity, Offerings" | Photo/graphic | Only footer "17" and watermark recovered (l.570-571) | OCR_SOURCED, LOW_INFORMATION_CONTENT |
| 19 | 18 | 573 | No | PropTech Opportunity Distribution | Text/infographic | Total distribution spend opportunity ₹39,000 crore, broken into ₹1,000 crore aggregator websites, ₹4,000 crore social media, ₹34,000 crore channel sales (l.577-605) | — |
| 20 | 19 | 620 | No | Aurum Analytica | Text/infographic | 150M+ social profiles data lake (l.631); marquee-client stats: 14,000+ properties marketed, 275+ projects, 1,20,000+ agents community, 145+ clients, $1.25Bn+ property value transaction enabled (l.645-649) | — |
| 21 | 20 | 653 | No | Sell.Do | Text/infographic | Marquee-client stats: $25Bn+ inventory sold, 15+ years RE experience, 50Mn+ leads managed, 7 days set-up & deploy, 45Mn+ customer interactions managed (l.681-685) | — |
| 22 | 21 | 689 | No | PropTiger | Text/infographic | Marquee-client stats: 44,000+ happy customers, 350+ relationship managers, 10+ cities, ₹30,000Cr+ homes sold, ₹5,000Cr+ loans facilitated (l.717-721) | — |
| 23 | 22 | 724 | Yes | Section divider — "Capital PropTech Opportunity" | Photo/graphic | Only footer "22" and watermark recovered (l.728-729) | OCR_SOURCED, LOW_INFORMATION_CONTENT |
| 24 | 23 | 731 | No | PropTech Opportunity Capital | Text/infographic | 300 family offices at avg AUM USD 100 million; INR 561 Billion net inflows by individual investors; ₹50,000 Cr.+ SM-REIT-able supply across India (l.737-756) | — |
| 25 | 24 | 765 | Yes | Section divider (untitled) | Photo/graphic | OCR near-total failure; only footer "24" and watermark recovered (l.777-778) | OCR_SOURCED, LOW_INFORMATION_CONTENT |
| 26 | 25 | 780 | No | Profit & Loss — Reconciliation of Adjusted EBITDA | Table (financial) | Full 17-row P&L build-up and 3 ratio rows — see Table 3 below for line-by-line enumeration; Note on Ind AS 116 RoU treatment (l.811-813) | CORE_FINANCIAL_TABLE, ZERO_STANDING (see Table 3) |
| 27 | 26 | 815 | Yes | Section divider (untitled) | Photo/graphic | OCR complete failure — no legible content beyond stray digit fragments and watermark (l.862-866) | OCR_SOURCED, LOW_INFORMATION_CONTENT |
| 28 | 27 | 868 | No | Strong Fundamentals | Text (qualitative) | GRC framework description; Vision/Values statement; capital-stack taxonomy (Intellectual/Human/Social & Brand/Ecosystem/Financial Capital) (l.873-898) — no hard numbers | — |
| 29 | 28 | 902 | No | Value Creation Journey (group history) | Timeline/text | IOL Netcom 1999 (exited 2005), SpiceJet 2006 (exited 2008), RenewPower 2009 (exited 2013), Aurum RealEstate 2009 (current), Aurum PropTech 2020 (current) (l.913-924) | — |
| 30 | 29 | 928 | No | Our Board of Directors (1 of 2) | Text (bios) | 4 director bios — see Table 5 rows 1-4 | — |
| 31 | 30 | 967 | No | Our Board of Directors (2 of 2) | Text (bios) | 4 director bios — see Table 5 rows 5-8 | — |
| 32 | 31 | 1003 | No | Our Leadership Team (1 of 2) | Table (bios) | 6 leadership bios — see Table 6 rows 1-6 | — |
| 33 | 32 | 1048 | No | Our Leadership Team (2 of 2) | Table (bios) | 6 leadership bios — see Table 6 rows 7-12; row 7 (Onkar Shetye) duplicates the board bio on slide 30 | DUAL_LISTING |
| 34 | 33 | 1094 | No | Thank You / IR contact | Text | Contact: Rihen Shah, Investor Relations, rihen.shah@aurumproptech.in (l.1103-1104); closing forward-looking-statement disclaimer (l.1107-1109) | — |

### DROPPED_SLIDE check
No prior-quarter presentation ledger was supplied in this task's injected
inputs. This diff could not be run. Flag `DATA_GAP_PRIOR_LEDGER` — A3/A4
should source the Q4 FY26 (or Q1 FY26, for YoY deck-structure comparison)
presentation ledger before closing this gap, since a dropped slide is
itself a disclosure signal per the enumerator's operating rules.

---

## TABLE 2 — Footnotes / source lines qualifying a headline number (8/8)

| # | Line | Slide (pg) | Text (verbatim, truncated) |
|---|---|---|---|
| 1 | 55 | 2 | "Note: All products and services mentioned in this presentation are operated through our wholly-owned subsidiaries & other subsidiaries" |
| 2 | 128 | 4 | "Notes: As on 30th June 2026. Figures rounded off." |
| 3 | 166-167 | 5 | "Notes: As on 30th June 2026. Figures rounded off. Other income excluded from segmental income. Finance cost & other un-allocable expense of ₹6.24 crores removed from segmental breakup." |
| 4 | 205 | 6 | "Notes: 1. As on 30th June 2026. Figures rounded off. 2. Revenue per team member annualized for the year basis quarterly revenue." |
| 5 | 370 | 11 | "Source: CareEdge, Knight Frank, Grant Thornton and other industry reports" |
| 6 | 405 | 12 | "Notes: Data as on 30th June 2026." |
| 7 | 491 | 15 | "Source: Aurum Research, Care EDGE" |
| 8 | 811-813 | 26 | "Note: - Ind AS 116 requires lessees to record a right-of-use (RoU) asset and a lease liability... The costs here are net of all such considerations." |

(The two full-slide legal disclaimers — slide 3 opening disclaimer and slide
34 closing disclaimer — are enumerated as slide content type in Table 1, not
duplicated here; they qualify the whole deck, not a single headline number.)

---

## TABLE 3 — Financial table line items: P&L — Reconciliation of Adjusted EBITDA (slide 26, 17/17)

All figures ₹ Cr. unless stated. Q1 FY26 → Q1 FY27.

| # | Line | Line item | Q1 FY26 | Q1 FY27 | Flags |
|---|---|---|---|---|---|
| 1 | 785 | PBT / Total Income (%) | -14.0% | 1.9% | — |
| 2 | 786 | EBITDA / Total Income (%) | 28.4% | 31.9% | — |
| 3 | 787 | Adjusted EBITDA / Adjusted Income (%) | -3.0% | 10.2% | — |
| 4 | 792 | Adjusted Income (TIr) | 73.26 | 117.80 | — |
| 5 | 793 | Add: Other income related to RoU assets | 3.71 | 2.99 | — |
| 6 | 795 | Total Income (TI) | 76.96 | 120.79 | — |
| 7 | 796 | Less: Employee benefits costs & Other expenses | 55.09 | 82.22 | — |
| 8 | 797 | EBITDA | 21.87 | 38.56 | — |
| 9 | 800 | Add: ESOP Costs | 1.22 | 0.81 | — |
| 10 | 801 | Less: Other income related to RoU assets | 3.71 | 2.99 | — |
| 11 | 803 | Less: Long term lease payments | 21.61 | 24.31 | — |
| 12 | 804 | Adjusted EBITDA (before ESOP & RoU), EBITDAr | -2.23 | 12.07 | — |
| 13 | 805 | Less: ESOP Costs | 1.22 | 0.81 | — |
| 14 | 806 | Less: Finance costs | 1.66 | 1.06 | — |
| 15 | 807 | Less: Depreciation costs | 5.67 | 6.39 | — |
| 16 | 808 | Less: Impact of IND AS | (blank/nil) | 1.47 | `ZERO_STANDING` — line exists as a template row; nil in Q1FY26, populated in Q1FY27, no explanatory note on which IND AS item |
| 17 | 809 | PBT (before Exceptional Items) | -10.78 | 2.35 | — |

---

## TABLE 4 — Digital signature blocks (1/1)

| Line | Signatory | Designation | Timestamp | Context |
|---|---|---|---|---|
| 44-52 | Pranali Pratap Desale | Company Secretary & Compliance Officer | 2026.07.21 08:51:38 +05'30' | Cover letter forwarding the Investor Presentation under Reg. 30; presentation itself dated "July 21, 2026" (l.16), same day as signature — no board-meeting timing conflict applicable to this doctype (no board outcome letter in this filing) |

---

## TABLE 5 — Board of Directors bios (8/8, slides 30-31)

| # | Line | Name | DIN | Role | Background (first clause) |
|---|---|---|---|---|---|
| 1 | 933-939 | Mr. Ashish Deora | NOT FOUND | Non-Executive Chairman | First-generation entrepreneur, three decades building businesses across mining, telecom, aviation, renewable energy, RealEstate, PropTech; founder of Aurum Ventures |
| 2 | 943-945 | Ramashrya Yadav | NOT FOUND | Non-Executive Director | Harvard Business School alumnus, 26+ years real estate/banking/investments; founded India's first RE-focused asset mgmt firm |
| 3 | 950-953 | Onkar Shetye | NOT FOUND | Executive Director | 18 years multisectoral experience (India/Europe/Africa); IIM Ahmedabad alumnus; with Aurum Group since June 2012 |
| 4 | 958-962 | Vasant Gujarathi | NOT FOUND | Independent Director | Chartered Accountant, 38 years experience incl. 22 years as Partner at PwC India; ICAI fellow |
| 5 | 972-974 | Ajit Joshi | NOT FOUND | Independent Director | Global business leader, 37+ years across technology/healthcare/renewables; MBA Symbiosis |
| 6 | 979-982 | Padma Deosthali | NOT FOUND | Independent Director | Social scientist, 23+ years public health/gender equity, led CEHAT 11 years; PhD TISS |
| 7 | 987-990 | Lakshmi Naga Potluri | NOT FOUND | Independent Director | Business leader across entrepreneurship/VC/global biz dev; current CRO at Tira Beauty; MBA Columbia |
| 8 | 995-998 | Dr. Ashim A. Desai | NOT FOUND | Independent Director | ENT surgeon, three decades experience; Chief ENT Surgeon ABR Desai ENT Hospital, Mumbai |

DIN not disclosed anywhere in this presentation for any director — `NOT
FOUND` recorded per operating rule (never estimate a missing number).
Term dates and inter-director relationships also not disclosed in this
doctype (would live in the AGM notice / annual report, not the investor
deck) — flagged as out-of-scope-for-doctype rather than `NOT FOUND` gaps.

---

## TABLE 6 — Leadership Team bios (12/12, slides 32-33)

| # | Line | Name | Role | Prior organizations |
|---|---|---|---|---|
| 1 | 1010-1015 | Ajay Kumar | Co-Founder and MD, MonkTechLabs | Monk Tech Labs, Cozee Homes, Mu Sigma |
| 2 | 1018-1020 | Balaji Varadharajan | Co-Founder and MD, MonkTechLabs | Monk Tech Labs, Cozee Homes, TVS Motor Company |
| 3 | 1022-1026 | Ismail Khan | Chief Business Officer, NestAway | NestAway, TaxiForSure, IBM |
| 4 | 1028-1032 | Jitendra Jagadev | Co-Founder and CEO NestAway, CEO at HelloWorld | Nestaway, Cisco, Philips |
| 5 | 1035-1037 | Ketan Sabnis | CEO at Sell.do | Amazon India |
| 6 | 1041-1044 | Kunal Karan | CFO, Aurum PropTech | Majesco, Mastek, Reliance |
| 7 | 1055-1057 | Onkar Shetye | Executive Director, Aurum PropTech | Aurum RealEstate Developers, Accenture, Cognizant | 
| 8 | 1059-1063 | Prakash Tejwani | CEO & Executive Director at Aurum Analytica, Non-Executive Director at PropTiger | Pitney Bowes, AL Maya Dubai |
| 9 | 1066-1072 | Ram Yadav | Founder and CEO, Integrow | Edelweiss, Orbit Corporation, Shapoorji Pallonji |
| 10 | 1074-1079 | Sahil Rathore | Chief Business Officer, Aurum Analytica | Pitney Bowes, Appirio (A Wipro Company) |
| 11 | 1082-1084 | Vinayak Katkar | Co-Founder at Sell.do | Sun Microsystems |
| 12 | 1087-1091 | Vishal Sharma | Chief Technical Officer, Aurum Analytica | Karachain, UX Army |

Row 7 (Onkar Shetye) is the same individual enumerated as board Executive
Director in Table 5 row 3 — flag `DUAL_LISTING` (board + operating
leadership role; not a miss, a cross-reference note for A3/A4).

---

## SUMMARY OF FLAGS RAISED

- `OCR_SOURCED` — slides 3, 10, 14, 18, 23, 25, 27 (7 slides; matches A1
  header's ocr_pages list exactly)
- `LOW_INFORMATION_CONTENT` — slides 10, 14, 18, 23, 25, 27 (section-divider
  photo slides where OCR recovered near-nothing beyond a footer digit and
  the "Generated by Aurum AI Team" watermark; slide 3, also OCR'd, is
  excluded from this flag because its legal-disclaimer text was
  substantially recovered)
- `RECONCILE_CHECK` — slide 4 (Total Income segment split: Rental 56 /
  Distribution 56 / Others 9) vs slide 5 (Rental ₹56Cr / Distribution ₹56Cr
  / Capital ₹2Cr, with (₹5) Lakhs segment loss on Capital) — the "Others"
  figure on slide 4 and the "Capital" figure on slide 5 do not obviously
  reconcile to each other even after the ₹6.24Cr unallocable-expense
  footnote on slide 5; not resolved here, surfaced for A3/A4 arithmetic
  check
- `MATERIAL_TRANSACTION` / `RPT_WATCH` — slide 9, Housing.com acquisition,
  all-equity consideration to REA India, REA India reaching ~24.9% of
  Aurum PropTech post-transaction (a related-party lens for future
  quarters once REA India crosses reporting thresholds)
- `ZERO_STANDING` — slide 26 P&L table, "Less: Impact of IND AS" row, nil
  in Q1FY26, ₹1.47Cr in Q1FY27
- `DUAL_LISTING` — Onkar Shetye, listed as both board Executive Director
  (slide 30) and operating Executive Director in the Leadership Team
  (slide 33)
- `DATA_GAP_PRIOR_LEDGER` — no prior-quarter presentation ledger supplied;
  `DROPPED_SLIDE` diff not run this cycle
- `SIGNATURE_BLOCK` — slide 1 cover letter digital signature, timestamp
  noted for completeness (no timing conflict found for this doctype)
