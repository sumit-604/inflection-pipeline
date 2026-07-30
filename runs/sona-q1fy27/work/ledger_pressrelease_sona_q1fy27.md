# A2 ENUMERATOR LEDGER — SONACOMS Q1 FY27 — pressrelease doctype (routed as "presentation")

Source: extract_pressrelease_sona_q1fy27.txt (4-page press release + Reg-30 cover letter, 183
extract lines, no slides). Per injected task instructions this document is enumerated as a
press release: every reported financial figure, every management quote, every operational
metric, every order-book/capex/margin claim, every named entity/program, plus the
administrative/regulatory scaffolding (cover letter, signature, contacts, disclaimer,
boilerplate) that the base anti-miss mandate requires me not to drop.

Atomic unit chosen per category: for multi-metric bullets (e.g. line 71 has both a BEV-share
% and a BEV-growth %), the BULLET is the count-test unit; every individual figure inside it is
still listed in full in the row content so no number is lost.

```
=== A2 COUNT TEST ===
category: headline_claims              grep_count: 4   sweep_count: 4   match: yes
category: financial_figures             grep_count: 5   sweep_count: 5   match: yes
category: management_quotes             grep_count: 1   sweep_count: 1   match: yes
category: operational_highlights        grep_count: 2   sweep_count: 2   match: yes
category: order_book_entries            grep_count: 3   sweep_count: 3   match: yes
category: named_entities_programs       grep_count: 16  sweep_count: 16  match: yes
category: forward_looking_statements    grep_count: 3   sweep_count: 3   match: yes
category: regulatory_administrative     grep_count: 10  sweep_count: 10  match: yes
category: signatories_contacts          grep_count: 3   sweep_count: 3   match: yes
category: footnotes                     grep_count: 1   sweep_count: 1   match: yes
category: boilerplate_about             grep_count: 3   sweep_count: 3   match: yes
category: zero_standing_line_items      grep_count: 0   sweep_count: 0   match: yes
gate_a2: pass
total_disclosure_units: 51
=== END COUNT TEST ===
```

Grep commands used (all against extract_pressrelease_sona_q1fy27.txt):
- headline: `sed -n '56,60p'` non-blank count
- financial_figures bullets: `sed -n '68,76p' | grep -c "•"` = 5
- management quote: `grep -c "commented:"` = 1
- Key Developments bullets total: `sed -n '98,129p' | grep -c "•"` = 5; order-only via
  `grep -c -E "•\s+Sona Comstar has received"` = 3; non-order = 5-3 = 2
- order book entries: `grep -n -E "•\s+Sona Comstar has received"` = lines 119,123,126
- named entities: 15 distinct-pattern greps (Sona Comstar 2.0, Robotics and Physical AI,
  Sensors and Software, DENSO, North American OEM x2 [order-1 and order-3 counterparties
  counted separately], New Age OEM, Archetype, BSE Ltd, National Stock Exchange, Vivek
  Vikram Singh, Pankaj Gupta, Ankit Agrawal, Prerna Rao, issuer name, facility footprint) sum
  to 16
- forward-looking triggers: `grep -in -E "ambition|aspiration|forward-looking|next decade|
  undertakes no obligation|target another"` = 3 distinct paragraph groups (lines 81, 99-112,
  173-178)
- admin/regulatory anchors: `grep -n -E "date|BSE Ltd|NSE|Scrip Code|Subject|Regulation 30|
  Kindly take|Enclosed|Results Release|For immediate publication|- ENDS -"` = 14 raw lines,
  collapsed to 10 logical rows (line 17 splits into 2 addressee rows; the 3x repeated page
  header collapses to 1 row)
- footnote: `grep -c '\*\*'` = 1
- About paragraphs: manual paragraph-break sweep of lines 135-148 = 3
- zero_standing: no tabular financial statement in this document (prose bullets only) → 0/0

---

## 1. HEADLINE CLAIMS (page 2 banner, lines 56-60)

| # | Line | Content | Flags |
|---|------|---------|-------|
| H1 | 56 | Main headline: "Sona BLW Precision Forgings Ltd. announces Q1 FY27 Results" | |
| H2 | 58 | Sub-headline: "Announced entry in new growth vertical- Robotics & Physical AI" | NAMED_PROGRAM |
| H3 | 59 | Sub-headline: "Highest-ever Revenue, BEV Revenue and BEV revenue share in a quarter" | |
| H4 | 60 | Sub-headline: "Revenue grows 54% YoY, EBITDA grows 49%, and PAT grows 45% YoY" | RESTATED_CLAIM (repeated at lines 70/72/73 and again in quote line 86) |

## 2. FINANCIAL FIGURES — Key Financial Highlights bullets (lines 68-75)

| # | Line | Content (all figures in the bullet) | Flags |
|---|------|--------------------------------------|-------|
| F1 | 70 | Revenue Rs. 1,310 crores, +54% YoY | |
| F2 | 71 | BEV revenue share 44% (all-time high, Q1); BEV revenue +107% YoY | |
| F3 | 72 | EBITDA Rs. 303 crores; margin 23.1%; +49% YoY | |
| F4 | 73 | PAT Rs. 181 crores; net profit margin 13.6%; +45% YoY | |
| F5 | 75 | "We won three orders which include one EV program, one hybrid program and one ICE program" | ORDER_COUNT_AMBIGUITY — cross-check vs order-book table below: itemized bullets describe 1 (order1) + 2 (order2, bundled as one "program") + 1 (order3) = 4 individual orders across 3 programs, not literally "three orders" |

Note: cover letter (line 30-32) states the enclosed results are "unaudited Standalone and
Consolidated Financial Results," but none of F1-F4 is labeled standalone or consolidated —
only one unlabeled figure set is given for each metric. Flag **STD_CONSOL_UNSPECIFIED** on
the whole table.

## 3. MANAGEMENT QUOTE (lines 80-91)

| # | Line | Speaker / designation | First 15 words | Flags |
|---|------|------------------------|-----------------|-------|
| Q1 | 80-91 | Mr Vivek Vikram Singh, MD & Group CEO | "Q1 FY27 marks the unveiling of Sona Comstar 2.0—our ambition to grow tenfold again over" | FORWARD_LOOKING (tenfold-in-a-decade ambition); restates F1-F4 and H4 in prose (RESTATED_CLAIM); asserts new business "spanning India, Europe and North America" — **UNSUBSTANTIATED_GEOGRAPHY_CLAIM**: the itemized order-book bullets (line 119-128) name only a "North American OEM" (x2) and an unspecified "New Age OEM" — no India or Europe order is itemized anywhere in this document to substantiate the Europe/India portion of the claim |

## 4. OPERATIONAL HIGHLIGHTS — Key Developments, non-order bullets (lines 98-129)

| # | Line | Content | Flags |
|---|------|---------|-------|
| O1 | 99-113 | Sona Comstar 2.0 strategy unveiled: aspiration to repeat 10x revenue growth over the next decade (ending FY35) that was achieved in the past decade (ending FY25); 3 stated pillars: (1) accelerate new product verticals organically and inorganically, (2) increase focus on Eastern world markets, (3) target a new long-term tech growth pillar — intelligent and connected systems, alongside electrification | FORWARD_LOOKING / GUIDANCE; RESTATED_CLAIM (same 10x ambition as Q1) |
| O2 | 114-118 | Expansion of existing "Sensors and Software" vertical into "Robotics and Physical AI": (1) mission-critical components/subsystems for Robotics and Physical AI, (2) perception stack + ER&D services for Robotics and Physical AI platforms, (3) developing/manufacturing selected full-stack robot platforms | NAMED_PROGRAM |

## 5. ORDER-BOOK / CAPEX / MARGIN CLAIMS (lines 119-128, footnoted at 129)

| # | Line | Customer (as disclosed) | Product / program | Order-book addition | Production start | Flags |
|---|------|--------------------------|--------------------|----------------------|-------------------|-------|
| B1 | 119-122 | "an existing customer, a North American OEM of ICE and Electric Passenger Vehicles" | Differential assemblies, hybrid PV platform | Rs 6.4 billion (= Rs 640 cr per header conversion note) | H2 FY29 | FORWARD_LOOKING (timeline); ANONYMIZED_CUSTOMER |
| B2 | 123-125 | "a New Age OEM of Electric two wheelers" — TWO orders | Hub wheel traction motors | Rs 900 million (= Rs 90 cr) | H2 FY26 | FORWARD_LOOKING; ANONYMIZED_CUSTOMER; MULTI_ORDER_BUNDLE (2 individual orders reported as 1 program line) |
| B3 | 126-128 | "an existing customer, a North American OEM of ICE and Electric Passenger Vehicles" | Differential gears, ICE PV platform | Rs 2.1 billion (= Rs 210 cr) | H2 FY28 | FORWARD_LOOKING; ANONYMIZED_CUSTOMER; **POSSIBLE_DUPLICATE_ENTITY** — description is verbatim-identical to B1's counterparty; document does not disclose whether B1 and B3 are the same customer or two different ones |

Order-book figures are stated in Rs billion/million per the A1 header's conversion note
(billion -> x100 cr, million -> x0.1 cr); downstream agents must apply that conversion, not
this ledger.

## 6. NAMED ENTITIES / PROGRAMS (first-mention line, all mention lines noted)

| # | Entity | Type | First line | All lines | Flags |
|---|--------|------|------------|-----------|-------|
| E1 | Sona Comstar 2.0 | Strategy/brand name | 80 | 80, 99 | |
| E2 | Robotics and Physical AI | New business vertical | 58 | 58, 82, 115-117 | NAMED_PROGRAM |
| E3 | Sensors and Software | Prior vertical name (being expanded) | 114 | 114 | |
| E4 | DENSO | External partner | 82 | 82 | new partnership announced this quarter |
| E5 | North American OEM (order B1 counterparty) | Customer, anonymized | 119 | 119-122 | ANONYMIZED_CUSTOMER |
| E6 | North American OEM (order B3 counterparty) | Customer, anonymized | 126 | 126-128 | ANONYMIZED_CUSTOMER; POSSIBLE_DUPLICATE_ENTITY vs E5 |
| E7 | New Age OEM of Electric two wheelers | Customer, anonymized | 123 | 123-125 | ANONYMIZED_CUSTOMER |
| E8 | Archetype | External PR/IR agency | 162 | 162, 165-166 | |
| E9 | BSE Ltd. | Exchange / regulatory recipient | 17 | 17, 147 | |
| E10 | National Stock Exchange of India Ltd. (NSE) | Exchange / regulatory recipient | 19 | 19-20, 147-148 | |
| E11 | Vivek Vikram Singh | Person — MD & Group CEO | 80 | 80 | quoted management spokesperson |
| E12 | Pankaj Gupta | Person — SVP (Legal), Company Secretary & Compliance Officer | 39 | 39-47 | signatory |
| E13 | Ankit Agrawal | Person — Head of Investor Relations | 165 | 165, 167 | company-side contact |
| E14 | Prerna Rao | Person — Archetype contact | 165 | 165-166 | external PR contact |
| E15 | Sona BLW Precision Forgings Limited / Sona Comstar | Issuer itself | 39 | throughout | |
| E16 | Manufacturing & R&D footprint: India, USA, Serbia, Mexico, China | Facility locations (grouped) | 138 | 138-139 | |

## 7. FORWARD-LOOKING / GUIDANCE STATEMENTS (cross-referenced, not double-counted against Q1/O1)

| # | Line | Content | Flags |
|---|------|---------|-------|
| G1 | 80-81 | Quote: "our ambition to grow tenfold again over the next decade" (informal restatement, see Q1) | FORWARD_LOOKING |
| G2 | 99-113 | Bullet: formal Sona Comstar 2.0 strategy statement — 10x revenue growth aspiration by FY35 + 3 strategic pillars (see O1) | FORWARD_LOOKING; RESTATED_CLAIM (same target as G1) |
| G3 | 172-179 | Standard safe-harbor / forward-looking-statements disclaimer | **TEMPLATE_ARTIFACT** — disclaimer text refers to statements "made or discussed at the conference call," but no conference call is otherwise referenced anywhere in this 4-page press release; likely reused boilerplate from a concall-disclaimer template |

Note: the three production-start timelines (B1 H2 FY29, B2 H2 FY26, B3 H2 FY28) are also
forward-looking but are tagged FORWARD_LOOKING directly on their order-book rows (Section 5)
rather than re-listed here, to avoid double-counting in the gate.

## 8. REGULATORY / ADMINISTRATIVE (cover letter scaffolding, page 1 + recurring page headers)

| # | Line | Content | Flags |
|---|------|---------|-------|
| R1 | 15 | Letter date: "23rd July, 2026" | matches signature timestamp date (line 40-44); does NOT match body dateline (see R-flag DATE_MISMATCH under R6/quote area below) |
| R2 | 17-18 | Addressee: BSE Ltd., Regd Office Floor-25, Phiroze Jeejeebhoy Towers, Dalal Street, Mumbai-400001 | |
| R3 | 19-20 | Addressee: National Stock Exchange of India Ltd., Listing Deptt, Exchange Plaza, BKC, Bandra (East), Mumbai-400051 | |
| R4 | 21 | Identifiers: BSE Scrip Code 543300; NSE Scrip SONACOMS | |
| R5 | 24 | Subject line: "Press Release" | |
| R6 | 28-32 | Regulatory citation: Reg 30 + Schedule III, SEBI LODR Regulations 2015; encloses unaudited Standalone and Consolidated Financial Results, quarter ended 30 June 2026 | STD_CONSOL_UNSPECIFIED (see Section 2 note) |
| R7 | 35 | Closing instruction: "Kindly take the same on record." | |
| R8 | 49 | "Enclosed: As above" | |
| R9 | 51-52, 107-108, 157-158 | Repeated page-header label "Results Release / For immediate publication" (appears identically on pages 2, 3, and 4) | |
| R10 | 132 | "- ENDS -" marker | |

**DATE_MISMATCH (critical):** line 64 datelines the press release body "Gurgaon, India, April
30, 2026," reporting results "for the quarter ended June 30th, 2026." April 30, 2026 is BEFORE
the quarter it purports to report on even ended, and is three months before the actual filing/
signature date of 23rd July 2026 (R1, and digital signature line 40-44). This is very likely a
stale dateline carried over verbatim from the prior quarter's (Q4 FY26) press release template
— a mechanical drafting error, not a results anomaly, but one that A3/A4 should note since it
signals a templating/QC gap in the disclosure process itself.

**DOCTYPE_MISMATCH:** this file is routed with doctype=presentation but is in fact a 4-page
press release plus Reg-30 cover letter — no slides, no investor-deck structure. Noted so
downstream stages do not expect slide-numbered content that does not exist in this artifact.

## 9. SIGNATORIES & CONTACTS

| # | Line | Person | Role | Flags |
|---|------|--------|------|-------|
| S1 | 39-47 | Pankaj Gupta | SVP (Legal), Company Secretary and Compliance Officer — digitally signed 2026.07.23 16:07:42 +05'30' | No board-meeting time is disclosed anywhere in this document, so the "signature before board meeting concluded" check cannot be run against this artifact (N/A, not a Board Outcome letter) |
| S2 | 165, 167 | Ankit Agrawal | Head of Investor Relations (company-side contact), ankit.agrawal@sonacomstar.com | |
| S3 | 162, 165-166 | Prerna Rao | Archetype (external PR agency contact), Tel +91 98738 79787, prerna.rao@archetype.co | |

## 10. FOOTNOTES

| # | Line | Content | Qualifies | Flags |
|---|------|---------|-----------|-------|
| N1 | 129 | "**refer to Investor Presentation" | Qualifies all three order-book value/timeline claims (B1-B3, lines 119-128) | EXTERNAL_REFERENCE_UNVERIFIED — this extract does not include the referenced Investor Presentation; order-book figures in this document cannot be cross-verified against it within this artifact |

## 11. BOILERPLATE — "About Sona BLW Precision Forgings Limited" (lines 135-148)

| # | Line | Content |
|---|------|---------|
| A1 | 135-139 | Company overview: founded 1995, HQ Gurugram; global supplier with manufacturing/assembly facilities, R&D centres, engineering capability centres across India, USA, Serbia, Mexico, China |
| A2 | 140-146 | Business description: driveline & traction motor solutions for the EV market; brake systems, couplers, suspension systems for the railway industry; R&D/engineering capabilities in precision forging, mechanical/electrical systems, radar sensors, base and application software |
| A3 | 147-148 | Listing information: BSE (Code 543300) and NSE (Symbol SONACOMS); website reference |

## 12. ZERO/NIL/DASH-VALUED STANDING LINE ITEMS

None. This document contains no tabular financial statement (only narrative bullets), so
there is no multi-period line-item grid in which a zero/nil/dash standing item could appear.
`ZERO_STANDING` count = 0, sweep-confirmed by inspection of the entire 183-line extract for
any table structure (none found).

---

## FLAGS RAISED (summary, deduplicated)

- DATE_MISMATCH (critical — R1/body dateline line 64 vs signature/letter date)
- DOCTYPE_MISMATCH (routed as presentation; is actually a press release + cover letter)
- STD_CONSOL_UNSPECIFIED (Section 2, R6)
- ORDER_COUNT_AMBIGUITY (F5 vs B1-B3)
- UNSUBSTANTIATED_GEOGRAPHY_CLAIM (Q1 — "India, Europe and North America" vs itemized orders)
- POSSIBLE_DUPLICATE_ENTITY (E5 vs E6 / B1 vs B3 counterparty)
- ANONYMIZED_CUSTOMER (E5, E6, E7 / B1, B2, B3)
- MULTI_ORDER_BUNDLE (B2 — two orders reported as one program line)
- NAMED_PROGRAM (H2, E2, O2)
- FORWARD_LOOKING (H4-adjacent, Q1, O1, G1-G3, B1-B3 timelines)
- RESTATED_CLAIM (H4/F1-F4/Q1 financial figures repeated 3x; G1/G2 10x-decade ambition repeated 2x)
- TEMPLATE_ARTIFACT (G3 disclaimer references a "conference call" not otherwise present)
- EXTERNAL_REFERENCE_UNVERIFIED (N1)
