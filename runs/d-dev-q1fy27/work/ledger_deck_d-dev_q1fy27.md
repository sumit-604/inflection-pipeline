# A2 ENUMERATION LEDGER — Investor Presentation (Deck), D-DEV / DEEDEV, Q1 FY27
Source: /home/user/inflection-pipeline/runs/d-dev-q1fy27/work/extract_deck_d-dev_q1fy27.txt (36 pages, form-feed delimited, OCR-verified pages: 2,3,4,10,11,14,17,25,26,29,31,33,35)
Prior-quarter deck ledger: NOT PROVIDED / NOT FOUND in runs/ tree — DROPPED_SLIDE check is N/A this run (see section 11).
Unit convention: Rs. Crores (x1) unless marked % or MTPA/MT/MW/sqm/x (ratio).
Row-ID convention: prefix-NNN, one row = one line, grep-countable via `^\| PREFIX-`.

=== A2 COUNT TEST ===
category: slides             grep_count: 36   sweep_count: 36   match: yes
category: financial_metrics  grep_count: 132  sweep_count: 132  match: yes
category: forward_looking    grep_count: 34   sweep_count: 34   match: yes
category: order_book         grep_count: 26   sweep_count: 26   match: yes
category: capacity_rows      grep_count: 34   sweep_count: 34   match: yes
category: chart_data_points  grep_count: 80   sweep_count: 80   match: yes
category: shareholding_mkt   grep_count: 8    sweep_count: 8    match: yes   (supplementary, not gated)
category: entities            grep_count: 4    sweep_count: 4    match: yes   (supplementary, not gated)
category: directors_officers  grep_count: 13   sweep_count: 13   match: yes   (supplementary, not gated)
category: footnotes           grep_count: 5    sweep_count: 5    match: yes   (supplementary, not gated)
gate_a2: pass
=== END COUNT TEST ===

Grep basis used per category (run against this file after authoring, to reconcile against the manual sweep count built slide-by-slide from the extract):
- slides: `grep -c "^| SLD-" ledger_deck_d-dev_q1fy27.md`
- financial_metrics: `grep -c "^| FM-" ledger_deck_d-dev_q1fy27.md`
- forward_looking: `grep -c "^| FL-" ledger_deck_d-dev_q1fy27.md`
- order_book: `grep -c "^| OB-" ledger_deck_d-dev_q1fy27.md`
- capacity_rows: `grep -c "^| CAP-" ledger_deck_d-dev_q1fy27.md`
- chart_data_points: `grep -c "^| CH-" ledger_deck_d-dev_q1fy27.md`
- shareholding_mkt: `grep -c "^| SH-" ledger_deck_d-dev_q1fy27.md`
- entities: `grep -c "^| ENT-" ledger_deck_d-dev_q1fy27.md`
- directors_officers: `grep -c "^| DIR-" ledger_deck_d-dev_q1fy27.md`
- footnotes: `grep -c "^| FN-" ledger_deck_d-dev_q1fy27.md`

Note on category boundaries (stated explicitly so overlap is not mistaken for double-count error): a number that lives inside a chart (donut/bar/line) is enumerated once under CH by construction; the same underlying disclosure fact (e.g. closing order book ₹2,428.20 Cr) is separately enumerated under OB where it appears again as prose/table text on a different slide. Overlap across categories is expected and intentional — each category is a complete, independently countable sweep of its own unit type, not a deduplicated master list. FM is scoped to non-chart-rendered table/stat-box/narrative financial figures only; chart-embedded financial trend figures (p19, p27, p29, p33, p34) are enumerated under CH, not double-booked into FM.

---

## 1. SLD — Slide Index (36 slides, one row per slide = unit boundary)

| ID | Slide | Title / Content | Content Type | Line (extract) |
|---|---|---|---|---|
| SLD-01 | p1 | Reg. 30 cover letter to BSE/NSE | text/letter | 23 |
| SLD-02 | p2 | Title slide — Investor Presentation Q1 FY27 | text/cover | 71 |
| SLD-03 | p3 | Contents (01 About DEE / 02 Business Overview / 03 Financial Overview) | text | 86 |
| SLD-04 | p4 | Section divider "01 About DEE" | divider/photo | 107 |
| SLD-05 | p5 | About DEE: A Scaled, Integrated Process Piping Leader | text+stat callouts | 121 |
| SLD-06 | p6 | FY26: Milestones That Shaped Our Growth | table+narrative | 155 |
| SLD-07 | p7 | Translating Engineering Leadership into Long-Term Value Creation (Investment rationale wheel) | text+2 stat callouts | 189 |
| SLD-08 | p8 | A Multi-Decade Journey of Consistent Execution (timeline) | text/timeline+stats | 219 |
| SLD-09 | p9 | Board Of Directors | text/bios (6 directors) | 249 |
| SLD-10 | p10 | Experienced Leadership (senior mgmt photos) | text/bios (4 people) | 284 |
| SLD-11 | p11 | Experienced Leadership (regional/subsidiary heads) | text/bios (3 people) | 309 |
| SLD-12 | p12 | Design-to-Delivery Execution Model | process diagram, no figures | 334 |
| SLD-13 | p13 | Management Commentary (CMD quote) | text/quote | 366 |
| SLD-14 | p14 | Section divider "02 Business Overview" | divider/photo | 402 |
| SLD-15 | p15 | Diversified Business Portfolio (6 sub-segments) | text, no figures | 417 |
| SLD-16 | p16 | Q1FY27 Quarterly Snapshot Consolidated | table/stat-box+highlights | 448 |
| SLD-17 | p17 | Q1 FY27 Order Inflow and Closing Orderbook | 2 donut charts | 481 |
| SLD-18 | p18 | Segmental Highlights – Q1 FY27 | table+2 pie charts+narrative | 515 |
| SLD-19 | p19 | Core Business Performance | 3 trend charts+stat box | 545 |
| SLD-20 | p20 | Core Business Highlights | text, mixed figures | 584 |
| SLD-21 | p21 | Core Business – Specialized Process Piping Solutions | text | 610 |
| SLD-22 | p22 | Core Business – Heavy Fabrication & Infrastructure | text | 637 |
| SLD-23 | p23 | Strategically Positioned Global Manufacturing & Service Footprint | text/facility list | 666 |
| SLD-24 | p24 | Scaling Up Through New Facilities (Anjar) | text | 702 |
| SLD-25 | p25 | Diversified customer base across geographies | text+map graphic | 737 |
| SLD-26 | p26 | Diverse Clientele Across Critical Industries | icon grid+logo wall, no figures | 762 |
| SLD-27 | p27 | Non Core Business – Power Generation | text+small bar chart | 795 |
| SLD-28 | p28 | Non Core – Highlights | text | 827 |
| SLD-29 | p29 | Vision 2030 & Strategic Roadmap (Revenue Trajectory) | chart+guidance panel | 858 |
| SLD-30 | p30 | Vision 2030 & Strategic Roadmap (Industry Drivers / Margin Levers / Flywheel) | text, mostly qualitative | 892 |
| SLD-31 | p31 | Section divider "03 Financial Overview" | divider/photo | 935 |
| SLD-32 | p32 | Q1 FY27 – Consolidated P&L | table (11 rows x 6 cols) | 949 |
| SLD-33 | p33 | Q1 FY27 Key Performance Indicators | 3 bar charts | 973 |
| SLD-34 | p34 | FY26 Key Performance Indicators | 4 five-year trend charts | 1119 |
| SLD-35 | p35 | Capital Market Overview | market data+donut chart | 1157 |
| SLD-36 | p36 | Safe Harbor / Contact | disclaimer+contacts | 1198 |

---

## 2. FM — Financial Metrics (financial-overview slides), with period columns

### p6 — FY26 Milestones (lines 155-188)
| ID | Metric | Period(s) carried | Value | Line |
|---|---|---|---|---|
| FM-001 | Revenue | FY25 | 827 | 161-162 |
| FM-002 | Revenue | FY26 | 1,142 | 162 |
| FM-003 | Revenue YoY% | FY26 vs FY25 | 38% | 163 |
| FM-004 | Op.EBITDA | FY25 | 124 | 162 |
| FM-005 | Op.EBITDA | FY26 | 189 | 162 |
| FM-006 | Op.EBITDA YoY% | FY26 vs FY25 | 53% | 163 |
| FM-007 | PAT | FY25 | 44 | 168-169 |
| FM-008 | PAT | FY26 | 77 | 169 |
| FM-009 | PAT YoY% | FY26 vs FY25 | 77% | 170 |
| FM-010 | Order Book (cross-ref OB) | FY25 | 1,228 | 169 |
| FM-011 | Order Book (cross-ref OB) | FY26 | 1,940 | 169 |
| FM-012 | Order Book YoY% | FY26 vs FY25 | 58% | 170 |

### p16 — Q1FY27 Quarterly Snapshot Consolidated (lines 448-479)
| ID | Metric | Period(s) carried | Value | Line |
|---|---|---|---|---|
| FM-013 | Revenue | Q1 FY27 | ₹294.5 | 457 |
| FM-014 | Revenue YoY% | Q1FY27 vs Q1FY26 | 31.6% | 455 |
| FM-015 | Revenue QoQ% | Q1FY27 vs Q4FY26 | (18.6)% | 457 |
| FM-016 | ROCE | Q1 FY27 | NA — **ZERO_STANDING** (line item present, value not disclosed this quarter) | 456-457 |
| FM-017 | Op.EBIDTA | Q1 FY27 | ₹49.7 | 463-465 |
| FM-018 | Op.EBIDTA YoY% | Q1FY27 vs Q1FY26 | 38.7% | 462 |
| FM-019 | Op.EBIDTA QoQ% | Q1FY27 vs Q4FY26 | (21.8)% | 465 |
| FM-020 | Op.EBIDTA Margin | Q1 FY27 | 16.9% | 465 |
| FM-021 | Net Profit | Q1 FY27 | ₹16.1 | 472-474 |
| FM-022 | Net Profit YoY% | Q1FY27 vs Q1FY26 | 22.4% | 471 |
| FM-023 | Net Profit QoQ% | Q1FY27 vs Q4FY26 | (41.9)% | 474 |
| FM-024 | Net Profit Margin | Q1 FY27 | 5.5% | 476 |

### p18 — Segmental Highlights table (lines 515-543)
| ID | Metric | Period(s) carried | Value | Line |
|---|---|---|---|---|
| FM-025 | Core-Business Revenue | Q1 FY27 | 278.4 | 522 |
| FM-026 | Core-Business Revenue | Q4 FY26 | 342.4 | 522 |
| FM-027 | Core-Business QoQ% | Q1FY27 vs Q4FY26 | (18.7%) | 522 |
| FM-028 | Core-Business Revenue | Q1 FY26 | 209.3 | 522 |
| FM-029 | Core-Business YoY% | Q1FY27 vs Q1FY26 | 33.0% | 522 |
| FM-030 | Core-Business Revenue | FY26 | 1,086.5 | 522 |
| FM-031 | Non Core-Business Revenue | Q1 FY27 | 16.1 | 524 |
| FM-032 | Non Core-Business Revenue | Q4 FY26 | 19.2 | 524 |
| FM-033 | Non Core-Business QoQ% | Q1FY27 vs Q4FY26 | (16.0%) | 524 |
| FM-034 | Non Core-Business Revenue | Q1 FY26 | 14.5 | 524 |
| FM-035 | Non Core-Business YoY% | Q1FY27 vs Q1FY26 | 11.2% | 524 |
| FM-036 | Non Core-Business Revenue | FY26 | 55.5 | 524 |
| FM-037 | Total Revenue | Q1 FY27 | 294.5 | 525 |
| FM-038 | Total Revenue | Q4 FY26 | 361.6 | 525 |
| FM-039 | Total Revenue QoQ% | Q1FY27 vs Q4FY26 | (18.6%) | 525 |
| FM-040 | Total Revenue | Q1 FY26 | 223.8 | 525 |
| FM-041 | Total Revenue YoY% | Q1FY27 vs Q1FY26 | 31.6% | 525 |
| FM-042 | Total Revenue | FY26 | 1,142.0 | 525 |

### p18 — Segmental narrative (lines 528-543)
| ID | Metric | Period(s) carried | Value | Line |
|---|---|---|---|---|
| FM-043 | Process Piping Solutions Revenue | Q1 FY27 | ₹263 crore | 532 |
| FM-044 | Process Piping Solutions Revenue | Q1 FY26 | ₹194.5 crore | 532-533 |
| FM-045 | Process Piping Solutions YoY% | Q1FY27 vs Q1FY26 | 35.2% | 533 |
| FM-046 | Heavy Fabrications Revenue | Q1 FY27 | ₹15.3 crore | 535 |
| FM-047 | Heavy Fabrications Revenue | Q1 FY26 | ₹14.8 crore | 535 |
| FM-048 | Heavy Fabrications YoY% | Q1FY27 vs Q1FY26 | 3.6% | 535-536 |
| FM-049 | Power generation Revenue | Q1 FY27 | ₹16.1 crore | 541 |
| FM-050 | Power generation Revenue | Q1 FY26 | ₹14.5 crore | 541-542 |
| FM-051 | Power generation YoY% | Q1FY27 vs Q1FY26 | 11.2% | 542 |
| FM-052 | Revised Malwa tariff | forward, "revised" | ₹5.44/kWh — **flag TARIFF_INCONSISTENCY** (cross-ref FM-062, FM-065 which give ₹5.22 / ₹5.437) | 543 |

### p19 — Core Business Performance, stat-box (chart-embedded trend figures enumerated separately under CH-012 to CH-029)
| ID | Metric | Period(s) carried | Value | Line |
|---|---|---|---|---|
| FM-053 | Core Business Revenue | Q1 FY27 | 278.4 | 560 |
| FM-054 | Core Business Revenue YoY% | Q1FY27 vs Q1FY26 | 33.0% | 562 |
| FM-055 | Core Business Op.EBIDTA | Q1 FY27 | 49.6 (note: consol Op.EBIDTA on p16/p32 is 49.7 — core-only figure, not a discrepancy) | 566 |
| FM-056 | Core Business Op.EBIDTA YoY% | Q1FY27 vs Q1FY26 | 36.4% | 568 |
| FM-057 | Core Business Op.EBIDTA Margin | Q1 FY27 | 17.8% | 572-573 |
| FM-058 | Core Business Op.EBIDTA Margin chg | YoY | 40 bps | 575 |

### p27 — Non Core Business – Power Generation narrative (lines 795-825)
| ID | Metric | Period(s) carried | Value | Line |
|---|---|---|---|---|
| FM-059 | Abohar Biomass capacity | standing | 8 MW | 801 |
| FM-060 | Muktsar Biomass capacity | standing | 6 MW | 818-819 |
| FM-061 | Total operational capacity | standing | 14 MW | 814-815 |
| FM-062 | Malwa Power tariff (revised) | current | ₹5.22/kWh — **flag TARIFF_INCONSISTENCY** (cross-ref FM-052 ₹5.44, p13 ₹5.224) | 818-819 |
| FM-063 | Malwa Power tariff (prior) | prior | ₹3.50/kWh | 819 |
| FM-064 | Retrospective tariff recovery | FY26 | ~₹5.14 crore | 819-820 |
| FM-065 | Malwa Power tariff (escalated) | FY27 | ₹5.437/kWh — cross-ref FM-052 ₹5.44/kWh (rounding, consistent) | 820-821 |
| FM-066 | FY27 revenue estimate (power+pellets) | forward FY27 | ~₹80 crore (duplicate of p13 guidance, see FL-006) | 823-824 |

### p32 — Q1 FY27 Consolidated P&L (master table, 11 rows x 6 period columns; lines 949-971)
| ID | Metric | Period column | Value | Line |
|---|---|---|---|---|
| FM-067 | Revenue from Operations | Q1 FY27 | 294.5 | 958 |
| FM-068 | Revenue from Operations | Q4 FY26 | 361.6 | 958 |
| FM-069 | Revenue from Operations | QoQ% | (18.6%) | 958 |
| FM-070 | Revenue from Operations | Q1 FY26 | 223.8 | 958 |
| FM-071 | Revenue from Operations | YoY% | 31.6% | 958 |
| FM-072 | Revenue from Operations | FY26 | 1,142 | 958 |
| FM-073 | Op. EBITDA | Q1 FY27 | 49.7 | 959 |
| FM-074 | Op. EBITDA | Q4 FY26 | 65.9 | 959 |
| FM-075 | Op. EBITDA | QoQ% | (24.5%) | 959 |
| FM-076 | Op. EBITDA | Q1 FY26 | 35.9 | 959 |
| FM-077 | Op. EBITDA | YoY% | 38.7% | 959 |
| FM-078 | Op. EBITDA | FY26 | 189.3 | 959 |
| FM-079 | Op. EBITDA margin (%) | Q1 FY27 | 16.9% | 960 |
| FM-080 | Op. EBITDA margin (%) | Q4 FY26 | 18.2% | 960 |
| FM-081 | Op. EBITDA margin (%) | QoQ | (134bps) | 960 |
| FM-082 | Op. EBITDA margin (%) | Q1 FY26 | 16.0% | 960 |
| FM-083 | Op. EBITDA margin (%) | YoY | 86bps | 960 |
| FM-084 | Op. EBITDA margin (%) | FY26 | 16.6% | 960 |
| FM-085 | Add: Other Income | Q1 FY27 | 2.5 | 961 |
| FM-086 | Add: Other Income | Q4 FY26 | 1.7 | 961 |
| FM-087 | Add: Other Income | QoQ% | 41.7% | 961 |
| FM-088 | Add: Other Income | Q1 FY26 | 4.1 | 961 |
| FM-089 | Add: Other Income | YoY% | -39.4% | 961 |
| FM-090 | Add: Other Income | FY26 | 16.6 | 961 |
| FM-091 | Less: Interest Expenses | Q1 FY27 | 17.2 | 962 |
| FM-092 | Less: Interest Expenses | Q4 FY26 | 15.9 | 962 |
| FM-093 | Less: Interest Expenses | QoQ% | 7.9% | 962 |
| FM-094 | Less: Interest Expenses | Q1 FY26 | 11.5 | 962 |
| FM-095 | Less: Interest Expenses | YoY% | 49.8% | 962 |
| FM-096 | Less: Interest Expenses | FY26 | 56.2 | 962 |
| FM-097 | Less: Depreciation & Amortisation | Q1 FY27 | 15.0 | 963 |
| FM-098 | Less: Depreciation & Amortisation | Q4 FY26 | 13.9 | 963 |
| FM-099 | Less: Depreciation & Amortisation | QoQ% | 8.1% | 963 |
| FM-100 | Less: Depreciation & Amortisation | Q1 FY26 | 12.7 | 963 |
| FM-101 | Less: Depreciation & Amortisation | YoY% | 17.9% | 963 |
| FM-102 | Less: Depreciation & Amortisation | FY26 | 53.5 | 963 |
| FM-103 | PBT | Q1 FY27 | 20.1 | 964 |
| FM-104 | PBT | Q4 FY26 | 37.9 | 964 |
| FM-105 | PBT | QoQ% | (47.1%) | 964 |
| FM-106 | PBT | Q1 FY26 | 15.8 | 964 |
| FM-107 | PBT | YoY% | 27.1% | 964 |
| FM-108 | PBT | FY26 | 96.2 | 964 |
| FM-109 | Taxes | Q1 FY27 | 4.0 | 965 |
| FM-110 | Taxes | Q4 FY26 | 10.2 | 965 |
| FM-111 | Taxes | QoQ% | (61.1%) | 965 |
| FM-112 | Taxes | Q1 FY26 | 2.6 | 965 |
| FM-113 | Taxes | YoY% | 50.6% | 965 |
| FM-114 | Taxes | FY26 | 19.1 | 965 |
| FM-115 | Profit After Tax | Q1 FY27 | 16.1 | 966 |
| FM-116 | Profit After Tax | Q4 FY26 | 27.7 | 966 |
| FM-117 | Profit After Tax | QoQ% | (41.9%) | 966 |
| FM-118 | Profit After Tax | Q1 FY26 | 13.1 | 966 |
| FM-119 | Profit After Tax | YoY% | 22.4% | 966 |
| FM-120 | Profit After Tax | FY26 | 77.2 | 966 |
| FM-121 | Profit After Tax margin (%) | Q1 FY27 | 5.5% | 967 |
| FM-122 | Profit After Tax margin (%) | Q4 FY26 | 7.7% | 967 |
| FM-123 | Profit After Tax margin (%) | QoQ | (219bps) | 967 |
| FM-124 | Profit After Tax margin (%) | Q1 FY26 | 5.9% | 967 |
| FM-125 | Profit After Tax margin (%) | YoY | (41bps) | 967 |
| FM-126 | Profit After Tax margin (%) | FY26 | 6.8% | 967 |
| FM-127 | EPS (Diluted) | Q1 FY27 | 2.32 | 968 |
| FM-128 | EPS (Diluted) | Q4 FY26 | 3.99 | 968 |
| FM-129 | EPS (Diluted) | QoQ% | (41.8%) | 968 |
| FM-130 | EPS (Diluted) | Q1 FY26 | 1.9 | 968 |
| FM-131 | EPS (Diluted) | YoY% | 22.2% | 968 |
| FM-132 | EPS (Diluted) | FY26 | 11.14 | 968 |

Note: no "net worth" or "working capital" line items appear anywhere in the deck (p32 table stops at EPS; no balance-sheet slide). This is a disclosure gap relative to the ENUMERATE task brief's watch-list, not an enumeration miss — confirmed absent by full-deck sweep (see section 12, flag DECK_NO_BALANCE_SHEET).

---

## 3. FL — Forward-Looking / Guidance Items

| ID | Slide | Statement | Quantified? | Line |
|---|---|---|---|---|
| FL-001 | p7 | "Capex cycle nearing completion" | No — **UNQUANTIFIED_FORWARD** | 193 |
| FL-002 | p13 | Deferred ~₹25 crore revenue "expected to be recognized in the coming quarter" | Yes (₹25 cr) | 371-373 |
| FL-003 | p13 | Seamless pipe facility "expected to contribute meaningfully as utilization improves" | No — **UNQUANTIFIED_FORWARD** | 379-381 |
| FL-004 | p13 | Anjar pipe fabrication facility "continues to scale up steadily" | No — **UNQUANTIFIED_FORWARD** | 381-383 |
| FL-005 | p13 | ₹300 cr preferential-issue proceeds "expected to materially reduce leverage and finance costs, improve return ratios" | Partially (₹300cr actual; effect unquantified) | 386-388 |
| FL-006 | p13 | 72,000 MTPA biomass pellet facility, "estimated revenue generation of ₹80 crore in FY27" | Yes (₹80 cr FY27) | 392-393 |
| FL-007 | p13 | Pellet business "expected to provide a meaningful contribution ... over the coming quarters" | No — **UNQUANTIFIED_FORWARD** | 394-395 |
| FL-008 | p13 | "expect operating leverage, profitability, and cash flows to strengthen further, supporting a gradual reduction in debt" | No — **UNQUANTIFIED_FORWARD** | 399-400 |
| FL-009 | p16 | Deferred revenue "expected to be recognized in the coming quarter" (footnote, dup. of FL-002) | Yes (₹25 cr) | 478-479 |
| FL-010 | p16 | Biomass pellet facility, "full benefit expected from Q2 FY27" | No — **UNQUANTIFIED_FORWARD** | 475 |
| FL-011 | p18 | Power generation "expected to benefit further from a full-quarter pellet plant contribution from Q2 FY27" | No — **UNQUANTIFIED_FORWARD** | 542-543 |
| FL-012 | p27 | "FY27 revenue from power and biomass pellets estimated at ~₹80 crore" (dup. of FL-006) | Yes (₹80 cr) | 823-824 |
| FL-013 | p27 | "APTEL appeal ongoing for further optimization" (Malwa tariff) | No — **UNQUANTIFIED_FORWARD** | 821 |
| FL-014 | p28 | Pellet plant initiative "expected to offset current cash burn, stabilize segment profitability, and restore historical margin levels" | No — **UNQUANTIFIED_FORWARD** | 844-847 |
| FL-015 | p28 | Additional pellet capacity "proposed to be housed under the InVIT" | No — **UNQUANTIFIED_FORWARD** | 852-855 |
| FL-016 | p29 | Revenue Trajectory FY27E | Yes | 1,500 Cr — 869/876/885 |
| FL-017 | p29 | Revenue Trajectory FY28E | Yes | 1,800 Cr — 869/876/885 |
| FL-018 | p29 | Revenue Trajectory FY30E | Yes | 2,500 Cr — 864/876/885 |
| FL-019 | p29 | Revenue CAGR FY26-30E | Yes | ~22% — 880/886 |
| FL-020 | p29 | FY27 Order Visibility | Yes | 2,000 Cr — 868/887 |
| FL-021 | p29 | Bid Success Rate | Yes | 40% — 870/887 |
| FL-022 | p29 | Op.EBITDA margin guidance by FY30 | Yes | 19-20% — 862/873/888 |
| FL-023 | p29 | Op.EBITDA CAGR FY26-30 | Yes | ~26% — 874/888 |
| FL-024 | p29 | PAT guidance (% of revenue) by FY30 | Yes | 9-10% — 878/889 |
| FL-025 | p29 | PAT CAGR FY26-30 | Yes | ~30% — 879/889 |
| FL-026 | p30 | Domestic Thermal Expansion (industry) | Yes | 220 GW → 300 GW (80 GW addition by FY32) — 902-903 |
| FL-027 | p30 | Domestic Refining Expansion (industry) | Yes | 258 → 310 MMTPA by 2030 — 905-907 |
| FL-028 | p30 | Nuclear (industry) | Yes | ~8 GW → 100 GW by FY47 — 919-920 |
| FL-029 | p30 | Data Centers capex (industry) | Yes | $0.5T+ → $1T by 2026 — 927-928 |
| FL-030 | p30 | Data Center piping opportunity ratio (company) | Yes | ~₹25 Cr piping per 25MW — 929-930 |
| FL-031 | p30 | Asset turns target (company) | Yes | <2x → ~3.5x by FY30 — 921-922 |
| FL-032 | p30 | Planned maintenance capex (company) | Yes | INR 15-20 Cr — 926-927 |
| FL-033 | p30 | Semiconductors — "Multi-$bn fabs pipeline" | No — **UNQUANTIFIED_FORWARD** | 932-933 |
| FL-034 | p36 | Safe Harbor forward-looking-statement disclaimer (blanket qualifier for all above, esp. p29/p30 Vision-2030 targets) | N/A — disclaimer, not a claim | 1200-1219 |

---

## 4. OB — Order Book / Order Inflow Disclosures

| ID | Slide | Item | Value | Line |
|---|---|---|---|---|
| OB-001 | p6 | Order Book | FY25 = ₹1,228 Cr | 169, 174 |
| OB-002 | p6 | Order Book | FY26 = ₹1,940 Cr | 169, 174 |
| OB-003 | p6 | Order Book YoY growth | 58% | 170, 174 |
| OB-004 | p6 | Key order won | ₹170 Cr domestic power orders | 176 |
| OB-005 | p6 | Key order won | USD 40 Mn+ LOI, global OEM (conversion underway) | 180-182 |
| OB-006 | p6 | Key order won | ₹173 Cr multi-geography orders | 184-186 |
| OB-007 | p6 | Key order won | ₹58 Cr first seamless pipe order | 174-175 |
| OB-008 | p6 | Key order won | ₹20 Cr international LOI (Taiwan) | 177-178 |
| OB-009 | p6 | Key order won | ~₹90 Cr windmill tower order | 181-182 |
| OB-010 | p6 | Key order won | ₹70 Cr Thailand inflows (March) | 184-185 |
| OB-011 | p7 | Closing Order Book | ₹2,428.20 Cr | 215-217 |
| OB-012 | p7 | Order Executed (YTD) | ₹294.37 Cr — **flag TERMINOLOGY_CHECK**: distinct metric from OB-013 "YTD Order Intake" on p17; both labeled YTD but represent different things (executed vs new orders won) | 215-217 |
| OB-013 | p17 | Order Inflow, center label | ₹780.87 Cr YTD Order Intake | 494-495, 509 |
| OB-014 | p17 | Order Inflow split | Process Piping Solutions = 89% | 500-501, 508 |
| OB-015 | p17 | Order Inflow split | Heavy Fabrication = 9% | 489, 508 |
| OB-016 | p17 | Order Inflow split | Power = 2% | 487, 508 |
| OB-017 | p17 | Order Inflow split | Gas — legend present, share not numerically visible — **ZERO_STANDING** | 508 |
| OB-018 | p17 | Closing Order Book, center label | ₹2,428.20 Cr as on Jun'26 | 494-495, 511 |
| OB-019 | p17 | Closing Order Book split | Process Piping Solutions = 93% | 500-501, 510 |
| OB-020 | p17 | Closing Order Book split | Heavy Fabrication = 7% | 488, 510 |
| OB-021 | p17 | Closing Order Book split | Gas — legend present, share not numerically visible — **ZERO_STANDING** | 510 |
| OB-022 | p17 | Closing Order Book split | Power — legend present, share not numerically visible — **ZERO_STANDING** | 510 |
| OB-023 | p20 | Order book (repeat) | ₹2,428 crore | 605-606 |
| OB-024 | p29 | Executable Order Book | 2,428 Cr | 867, 887 |
| OB-025 | p29 | FY27 Order Visibility (also FL-020) | 2,000 Cr | 868, 887 |
| OB-026 | p29 | Bid Success Rate (also FL-021) | 40% | 870, 887 |

Cross-check: closing order book value is consistent across every slide that restates it — OB-011 (p7) = OB-018 (p17) = OB-023 (p20) = OB-024 (p29) = ₹2,428(.20) Cr, and matches management commentary p13 line 397 ("₹2,428 crore"). No discrepancy found; flagged as confirmed-consistent, not as an issue.

---

## 5. CAP — Capacity Rows (by facility / segment)

| ID | Slide | Facility / Segment | Capacity | Line |
|---|---|---|---|---|
| CAP-001 | p5 | Manufacturing facilities, total count | 7 (across India and Thailand) | 145-149 |
| CAP-002 | p5 | Global standing claim | "Amongst Top 5 players in the world by installed process piping capacity" | 146-152 |
| CAP-003 | p5 | New Anjar facility commissioned | qualitative, no capacity figure on this slide (see CAP-016/026/027/028/029) | 152-153 |
| CAP-004 | p8 | Installed Capacity — Piping (company total) | 93,500 MTPA | 246 |
| CAP-005 | p8 | Installed Capacity — Heavy Fabrication (company total) | 32,400 MTPA | 247 |
| CAP-006 | p8 | Anjar capacity ramped & Seamless Plant commissioned, 2025-26 | qualitative marker (see CAP-016/026 for MTPA) | 234-237 |
| CAP-007 | p20 | Piping capacity (repeat of CAP-004) | 93,500 MTPA | 589 |
| CAP-008 | p20 | Heavy Fabrication capacity (repeat of CAP-005) | 32,400 MTPA | 590 |
| CAP-009 | p22 | Anjar total process piping capacity, increasing to | 30,000 MTPA | 660-661 |
| CAP-010 | p23 | Palwal, Haryana — combined capacity (3 units) | 36,000 MT | 670 |
| CAP-011 | p23 | Palwal Unit I — high-pressure piping/induction bends | 9,000 MT | 671-672 |
| CAP-012 | p23 | Palwal Unit II — industrial fittings | 3,000 MT | 673 |
| CAP-013 | p23 | Palwal Unit III — piping spools/systems | 24,000 MT | 674 |
| CAP-014 | p23 | Anjar Support & Structure Fabrication Unit | 3,000 MT | 678 |
| CAP-015 | p23 | Anjar Heavy Fabrication | 32,400 MT | 679 |
| CAP-016 | p23 | Anjar Pipe Fabrication Unit | 30,000 MT | 680 |
| CAP-017 | p23 | Anjar Seamless Plant | 7,000 MT | 681 |
| CAP-018 | p23 | Numaligarh Pipe Fabrication Unit | 6,000 MT | 686 |
| CAP-019 | p23 | Bangkok, Thailand — Fabrication | 14,500 MTPA | 689 |
| CAP-020 | p23 | Abohar Biomass (Punjab, Power Generation) | 8 MW | 697 |
| CAP-021 | p23 | Muktsar Biomass (Punjab, Power Generation) | 6 MW | 698 |
| CAP-022 | p23 | Summary — Piping division installed capacity (repeat) | 93,500 MTPA | 700 |
| CAP-023 | p23 | Summary — Heavy Fabrication division installed capacity (repeat) | 32,400 MTPA | 700 |
| CAP-024 | p23 | Summary — facility count (repeat of CAP-001) | "seven facilities in India and Thailand" | 700 |
| CAP-025 | p23 | Chennai — Engineering Service | no capacity/MT figure disclosed — **ZERO_STANDING** (facility named, no capacity quantified, unlike every other listed facility) | 689-690 |
| CAP-026 | p24 | Anjar Seamless Pipe Plant (repeat of CAP-017) | 7,000 MTPA | 717-718 |
| CAP-027 | p24 | Anjar Pipe Fabrication Unit (repeat of CAP-016) | 30,000 MTPA | 717 |
| CAP-028 | p24 | Anjar production capacity (ex-heavy fab), prior level | 6,000 MTPA | 721-722 |
| CAP-029 | p24 | Anjar production capacity (ex-heavy fab), grew to, by Sep'25 | 30,000 MTPA | 722-723 |
| CAP-030 | p27 | Abohar Biomass Power Plant capacity (repeat of CAP-020) | 8 MW | 800-801 |
| CAP-031 | p27 | Muktsar Biomass Power Plant capacity (repeat of CAP-021) | 6 MW | 818-819 |
| CAP-032 | p27 | Total operational capacity, Abohar + Muktsar (cross-ref FM-061) | 14 MW | 814-815 |
| CAP-033 | p27 | Abohar plant area | 205,681.48 sqm | 800 |
| CAP-034 | p27 | Muktsar plant area | 141,829.67 sqm | 818 |

---

## 6. CH — Chart Data Points (every [CHART]-tagged and chart-shaped visual)

### p17 — Order Inflow / Closing Order Book (2 donut charts)
| ID | Chart | Data point | Line |
|---|---|---|---|
| CH-001 | Order Inflow donut | Process Piping Solutions = 89% | 500-501, 508 |
| CH-002 | Order Inflow donut | Heavy Fabrication = 9% | 489, 508 |
| CH-003 | Order Inflow donut | Power = 2% | 487, 508 |
| CH-004 | Order Inflow donut | Center value = ₹780.87 Cr YTD Order Intake | 494-495, 509 |
| CH-005 | Closing Order Book donut | Process Piping Solutions = 93% | 500-501, 510 |
| CH-006 | Closing Order Book donut | Heavy Fabrication = 7% | 488, 510 |
| CH-007 | Closing Order Book donut | Center value = ₹2,428.20 Cr as on Jun'26 | 494-495, 511 |

### p18 — Revenue split pie charts (2 charts)
| ID | Chart | Data point | Line |
|---|---|---|---|
| CH-008 | % Q1FY27 Revenue Split | Core = 95% | 524-527 |
| CH-009 | % Q1FY27 Revenue Split | Non Core = 5% | 524-527 |
| CH-010 | % Q1FY27 Core Revenue Split | Process Piping Solutions = 94% | 536-540 |
| CH-011 | % Q1FY27 Core Revenue Split | Heavy Fabrication = 6% | 536-540 |

### p19 — Core Business trend charts (3 charts x 6 periods: FY23/FY24/FY25/FY26/Q1FY26/Q1FY27)
| ID | Chart | Period | Value | Line |
|---|---|---|---|---|
| CH-012 | Revenue | FY23 | 521 | 552-557 |
| CH-013 | Revenue | FY24 | 707 | 552-557 |
| CH-014 | Revenue | FY25 | 745 | 552-557 |
| CH-015 | Revenue | FY26 | 1,087 | 552-557 |
| CH-016 | Revenue | Q1 FY26 | 209 | 552-557 |
| CH-017 | Revenue | Q1 FY27 | 278 | 552-557 |
| CH-018 | Op. EBITDA | FY23 | 56 | 563-567 |
| CH-019 | Op. EBITDA | FY24 | 85 | 563-567 |
| CH-020 | Op. EBITDA | FY25 | 107 | 563-567 |
| CH-021 | Op. EBITDA | FY26 | 195 | 563-567 |
| CH-022 | Op. EBITDA | Q1 FY26 | 36 | 563-567 |
| CH-023 | Op. EBITDA | Q1 FY27 | 50 | 563-567 |
| CH-024 | Operating PBT | FY23 | -6.8 | 569-577 |
| CH-025 | Operating PBT | FY24 | 5 | 569-577 |
| CH-026 | Operating PBT | FY25 | 24 | 569-577 |
| CH-027 | Operating PBT | FY26 | 93 | 569-577 |
| CH-028 | Operating PBT | Q1 FY26 | 14 | 569-577 |
| CH-029 | Operating PBT | Q1 FY27 | 19 | 569-577 |

### p27 — Non-Core Revenue small bar chart
| ID | Chart | Period | Value | Line |
|---|---|---|---|---|
| CH-030 | Revenue – Q1 FY27 (Non-Core) | Q1 FY26 | 14 | 799-810 |
| CH-031 | Revenue – Q1 FY27 (Non-Core) | Q1 FY27 | 16 | 799-810 |

### p29 — Vision 2030 Revenue Trajectory chart
| ID | Chart | Period | Value | Line |
|---|---|---|---|---|
| CH-032 | Revenue Trajectory | FY25A | 827 | 864-876, 885 |
| CH-033 | Revenue Trajectory | FY26A | 1,142 | 864-876, 885 |
| CH-034 | Revenue Trajectory | FY27E | 1,500 Cr — forward, cross-ref FL-016 | 864-876, 885 |
| CH-035 | Revenue Trajectory | FY28E | 1,800 Cr — forward, cross-ref FL-017 | 864-876, 885 |
| CH-036 | Revenue Trajectory | FY30E | 2,500 Cr — forward, cross-ref FL-018 | 864-876, 885 |

### p33 — Q1 FY27 KPI bar charts (3 charts)
| ID | Chart | Data point | Line |
|---|---|---|---|
| CH-037 | Revenue bar chart | Q1 FY26 = 224 | 1103-1109, 1113 |
| CH-038 | Revenue bar chart | Q4 FY26 = 362 | 1103-1109, 1113 |
| CH-039 | Revenue bar chart | Q1 FY27 = 295 | 1103-1109, 1113 |
| CH-040 | Revenue bar chart | Callout 31.6% YoY | 981, 1113 |
| CH-041 | Revenue bar chart | Callout (18.6)% QoQ | 981, 1113 |
| CH-042 | Op.EBITDA & Margin chart | Q1 FY26 EBITDA = 35.9 | 1060-1080, 1114 |
| CH-043 | Op.EBITDA & Margin chart | Q1 FY26 margin = 16.0% | 1043, 1114 |
| CH-044 | Op.EBITDA & Margin chart | Q4 FY26 EBITDA = 65.9 | 1060, 1114 |
| CH-045 | Op.EBITDA & Margin chart | Q4 FY26 margin = 18.2% | 1026, 1114 |
| CH-046 | Op.EBITDA & Margin chart | Q1 FY27 EBITDA = 49.7 | 1068, 1114 |
| CH-047 | Op.EBITDA & Margin chart | Q1 FY27 margin = 16.9% | 1037, 1114 |
| CH-048 | Op.EBITDA & Margin chart | Callout 38.7% YoY | 981, 1114 |
| CH-049 | Op.EBITDA & Margin chart | Callout (24.5%) QoQ | 981, 1114 |
| CH-050 | PAT & Margin chart | Q1 FY26 PAT = 13.1 | 1098, 1115 |
| CH-051 | PAT & Margin chart | Q1 FY26 margin = 5.9% | 1061, 1115 |
| CH-052 | PAT & Margin chart | Q4 FY26 PAT = 27.7 | 1093, 1115 |
| CH-053 | PAT & Margin chart | Q4 FY26 margin = 7.7% | 1049, 1115 |
| CH-054 | PAT & Margin chart | Q1 FY27 PAT = 16.1 | 1098, 1115 |
| CH-055 | PAT & Margin chart | Q1 FY27 margin = 5.5% | 1061, 1115 |
| CH-056 | PAT & Margin chart | Callout 22.4% YoY | 981, 1115 |
| CH-057 | PAT & Margin chart | Callout (41.9%) QoQ | 981, 1115 |

### p34 — FY26 KPI five-year trend charts (4 charts x 5 years FY22-FY26). **Flag CHART_YEAR_MAPPING_AMBIGUOUS: p34 is NOT in the OCR-verified page list; year-to-bar correspondence is inferred from pdftotext -layout column spacing only and could not be independently confirmed. All 5 values per chart are captured; which value belongs to which FY year should be verified against the source image before being cited as an anchored, year-specific number.**
| ID | Chart | Value (year unconfirmed) | Line |
|---|---|---|---|
| CH-058 | Debt to Equity (x) | 0.70 | 1131, 1136 |
| CH-059 | Debt to Equity (x) | 0.85 | 1130, 1136 |
| CH-060 | Debt to Equity (x) | 1.02 | 1129, 1136 |
| CH-061 | Debt to Equity (x) | 0.89 | 1130, 1136 |
| CH-062 | Debt to Equity (x) | 0.73 | 1131, 1136 |
| CH-063 | Net Debt to EBITDA (x) | 3.88 | 1126, 1135 |
| CH-064 | Net Debt to EBITDA (x) | 4.09 | 1126, 1135 |
| CH-065 | Net Debt to EBITDA (x) | 3.76 | 1127, 1135 |
| CH-066 | Net Debt to EBITDA (x) | 4.02 | 1126, 1135 |
| CH-067 | Net Debt to EBITDA (x) | 3.81 | 1126, 1135 |
| CH-068 | Return on Capital Employed (%) | 5.30% | 1150, 1155 |
| CH-069 | Return on Capital Employed (%) | 6.60% | 1149, 1155 |
| CH-070 | Return on Capital Employed (%) | 8.80% | 1147, 1155 |
| CH-071 | Return on Capital Employed (%) | 9.80% | 1146, 1155 |
| CH-072 | Return on Capital Employed (%) | 8.20% | 1147, 1155 |
| CH-073 | Return on Equity (%) | 1.90% | 1152, 1155 |
| CH-074 | Return on Equity (%) | 3.20% | 1151, 1155 |
| CH-075 | Return on Equity (%) | 6.00% | 1148, 1155 |
| CH-076 | Return on Equity (%) | 7.00% | 1147, 1155 |
| CH-077 | Return on Equity (%) | 9.10% | 1145, 1155 |

### p35 — Shareholding Pattern donut
| ID | Chart | Data point | Line |
|---|---|---|---|
| CH-078 | Shareholding Pattern donut | Promoters = 65% | 1170-1176, 1185 |
| CH-079 | Shareholding Pattern donut | FII + DII = 19% | 1168, 1185 |
| CH-080 | Shareholding Pattern donut | Public = 16% | 1163-1164, 1185 |

---

## 7. SH — Shareholding / Market Data (p35, supplementary — non-chart-rendered figures; shareholding % slices themselves are CH-078/079/080 above)

| ID | Item | Value | Line |
|---|---|---|---|
| SH-001 | Current Market Price (CMP) | ₹658 (footnoted "as on 04.08.26") | 1166, 1187 |
| SH-002 | 52 Week High | ₹760 | 1167, 1188 |
| SH-003 | 52 Week Low | ₹183 | 1167, 1188 |
| SH-004 | Market Capitalization | ₹4,952 Cr | 1169, 1189 |
| SH-005 | No. Shares Outstanding | 7.52 Cr | 1172, 1190 |
| SH-006 | NSE ticker | DEEDEV (non-numeric identifier) | 1174, 1191 |
| SH-007 | BSE code | 544198 (non-numeric identifier; cross-ref cover letter p1 line 34) | 1176, 1192 |
| SH-008 | Marquee Investors (logos) | Kotak Mutual Fund, LIC Mutual Fund, Tata Mutual Fund — qualitative, no figures | 1186 |

Provenance flag (not a live discrepancy): raw tesseract OCR pass on p35 misread the Rupee glyph as a leading digit ("INR 3658", "24,952 Cr."); A1 extraction corrected this via direct image inspection and text-layer cross-check (line 1195). SH-001 and SH-004 above use the corrected values. Flag **OCR_CORRECTED** carried forward for A3/A4 awareness, not for re-litigation.

---

## 8. ENT — Subsidiary / Entity Mentions

| ID | Entity | Relationship / Role | Line |
|---|---|---|---|
| ENT-001 | DEE Fabricom India Private Limited (DFIPL) | Wholly-owned subsidiary; operates the Heavy Fabrication manufacturing base at Anjar, Gujarat | 653-654 |
| ENT-002 | Malwa Power Private Limited (MPPL) | DEE's wholly-owned subsidiary; operates the Muktsar biomass power plant | 821 |
| ENT-003 | DEE Piping Systems (Thailand) | Overseas manufacturing/CEO entity (K. Kris, CEO); Bangkok fabrication facility | 226-227, 325-326, 687-689 |
| ENT-004 | Malwa Power (Muktsar) — leadership cross-ref | Mr. B S Jangra listed as "CEO - Malwa Power Private Limited" on leadership slide (cross-ref ENT-002) | 317-319 |

---

## 9. DIR — Directors / Leadership (bios, not gated but enumerated per instruction to enumerate every named individual with role)

| ID | Slide | Name | Role | Line |
|---|---|---|---|---|
| DIR-001 | p9 | Krishan Lalit Bansal | Promoter, Chairman & Managing Director | 253-259 |
| DIR-002 | p9 | Shikha Bansal | Whole-time Director | 263-269 |
| DIR-003 | p9 | Shruti Aggarwal | Whole-time Director | 263, 270-272 |
| DIR-004 | p9 | Shilpi Barar | Independent Director | 275-277 |
| DIR-005 | p9 | Bhisham Kumar Gupta | Independent Director | 275, 278-280 |
| DIR-006 | p9 | Ashwani Kumar Prabhakar | Independent Director | 275, 280-283 |
| DIR-007 | p10 | Krishan Lalit Bansal (repeat of DIR-001) | Promoter, Chairman & Managing Director | 292-294 |
| DIR-008 | p10 | Brham Prakash Yadav | Chief Financial Officer | 293-295 |
| DIR-009 | p10 | Pankaj Agarwal | Chief Operating Officer | 299-300 |
| DIR-010 | p10 | Ranjan Kumar Sarangi | CS & Compliance Officer | 299-301 |
| DIR-011 | p11 | Mr. B S Jangra | CEO - Malwa Power Private Limited | 317-319 |
| DIR-012 | p11 | Mr. Gaurav Narang | Sr. Vice President | 318-319 |
| DIR-013 | p11 | K. Kris | CEO - DEE Piping Systems (Thailand) | 324-326 |

---

## 10. FN — Footnotes / Fine-Print / Disclaimers Qualifying Headline Numbers

| ID | Slide | Footnote text (paraphrase) | Line |
|---|---|---|---|
| FN-001 | p16 | "~₹25 crore" revenue deferred (Middle East geopolitical disruption + customer issues); expected recognized next quarter | 478-479 |
| FN-002 | p32 | "Q4FY26 Op. EBITDA includes a net positive impact on account of Labour Code" — **flag UNQUANTIFIED**: qualifies the Q4 FY26 EBITDA/margin comparison column but the quantum of the impact is not disclosed on this slide | 970 |
| FN-003 | p35 | "*CMP is as on 04.08.26" | 1177, 1193 |
| FN-004 | p35 | "As of August 2026" (general as-of date for the capital-market slide) | 1181, 1194 |
| FN-005 | p36 | Safe Harbor forward-looking-statement disclaimer (full text) — blanket qualifier for every guidance/estimate number in the deck, most materially p29/p30 Vision-2030 targets and p16 highlights | 1200-1219 |

---

## 11. DROPPED_SLIDE Check

No prior-quarter deck or prior-quarter ledger was supplied as input to this run (PRIOR_LEDGER_PATH not provided; no matching file found under runs/ for an earlier D-DEV quarter). DROPPED_SLIDE enumeration is therefore **N/A this run** — cannot be performed without a comparison baseline. This should be flagged to the orchestrator: if a Q4 FY26 or earlier D-DEV deck exists elsewhere, a DROPPED_SLIDE pass should be run against it before A3/A4 treat this deck's disclosure scope as complete.

---

## 12. Flags Summary (raised, not resolved — enumeration only)

- **ZERO_STANDING** — OB-017, OB-021, OB-022 (Gas / Power order-book-and-inflow segment shares present in chart legend but no numeric value visible/disclosed); CAP-025 (Chennai facility named with no capacity/MT figure, unlike every other facility on the same slide); FM-016 (ROCE = "NA" on p16 quarterly snapshot).
- **TARIFF_INCONSISTENCY** — Malwa/Muktsar biomass tariff cited as ₹5.224/kWh (p13, line 391), ₹5.22/kWh (p27, line 818-819), ₹5.437/kWh escalated (p27, line 820-821), and ₹5.44/kWh "revised" (p18, line 543). Values are close enough to be rounding of the same underlying figure but four slightly different figures appear across three slides for what should be one number — surfaced for A3/A4 to confirm same-basis.
- **TERMINOLOGY_CHECK** — OB-012 "Order Executed (YTD)" = ₹294.37 Cr (p7) vs OB-013 "YTD Order Intake" = ₹780.87 Cr (p17): both labeled YTD, materially different values and different underlying concepts (execution vs new-order intake); risk of reader conflation.
- **UNQUANTIFIED_FORWARD** — FL-001, FL-003, FL-004, FL-007, FL-008, FL-010, FL-011, FL-013, FL-014, FL-015, FL-033 (qualitative forward/guidance language with no anchored number).
- **CHART_YEAR_MAPPING_AMBIGUOUS** — CH-058 through CH-077 (all four p34 FY22-FY26 trend charts): page 34 was not in the OCR-verified page list, and year-to-bar mapping is inferred from raw text-layer column spacing only.
- **UNQUANTIFIED** — FN-002 (Labour Code impact on Q4 FY26 EBITDA cited but not quantified).
- **OCR_CORRECTED** (provenance note, not a live issue) — SH-001, SH-004 (p35 CMP and Market Cap; raw tesseract OCR misread Rupee glyph as a leading digit, corrected via image inspection per A1 extraction notes, line 1195).
- **DECK_NO_BALANCE_SHEET** — no net worth, net debt/borrowings (as a standing balance-sheet figure; Debt/Equity and Net Debt/EBITDA ratios on p34 are the closest proxies), or working-capital line item appears anywhere in the 36-slide deck. Confirmed by full sweep, not an enumeration gap.
- **DROPPED_SLIDE** — N/A this run, no prior-quarter baseline supplied (see section 11).

---

## Master Count Reconciliation (recap)

| Category | Grep pattern | Grep count | Manual sweep count | Match |
|---|---|---|---|---|
| Slides | `^\| SLD-` | 36 | 36 | yes |
| Financial metrics | `^\| FM-` | 132 | 132 | yes |
| Forward-looking | `^\| FL-` | 34 | 34 | yes |
| Order-book | `^\| OB-` | 26 | 26 | yes |
| Capacity rows | `^\| CAP-` | 34 | 34 | yes |
| Chart data points | `^\| CH-` | 80 | 80 | yes |
| Shareholding/market (supplementary) | `^\| SH-` | 8 | 8 | yes |
| Entities (supplementary) | `^\| ENT-` | 4 | 4 | yes |
| Directors (supplementary) | `^\| DIR-` | 13 | 13 | yes |
| Footnotes (supplementary) | `^\| FN-` | 5 | 5 | yes |

**GATE A2: PASS**

```yaml
stage: A2-enumerator
company: "D-DEV"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/d-dev-q1fy27/work/ledger_deck_d-dev_q1fy27.md"
counts:
  slides: 36
  slide_numbers: 36
  financial_metrics: 132
  forward_looking: 34
  order_book: 26
  capacity_rows: 34
  chart_data_points: 80
  shareholding_market: 8
  entities: 4
  directors_officers: 13
  footnotes: 5
flags_raised: [ZERO_STANDING, TARIFF_INCONSISTENCY, TERMINOLOGY_CHECK, UNQUANTIFIED_FORWARD, CHART_YEAR_MAPPING_AMBIGUOUS, UNQUANTIFIED, OCR_CORRECTED, DECK_NO_BALANCE_SHEET, DROPPED_SLIDE]
gate_a2: pass
mismatch_note: ""
```
