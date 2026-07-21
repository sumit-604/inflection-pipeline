# RUN LOG — /run-quarterly INDIAMART Q1 FY27

Run date: 2026-07-21
Orchestrator: quarterly-00-orchestrator v1.0

## Precheck
- Protocol files present: Results v1.2, Concall v1.1, Master v3.3 — PASS
- Toolchain: pdftotext/pdfinfo/pdftoppm/tesseract installed (poppler-utils + tesseract-ocr via apt cache) — PASS
- Company memory companies/INDIAMART.md: ABSENT (first per-company file)
- Notion page: FOUND (id 345bb2b9-d3ab-80fd-a1db-cd98e3968666), fetched live

## Document classification (by content, not filename)
| Upload | Pages | md5 | Class | Notes |
|---|---|---|---|---|
| eb272dcc (D1) | 16 | 099a778f… | results | Board Outcome + Reg 33 audited results + auditor report. Quarter ended 30 Jun 2026 = Q1 FY27 |
| aa8822f7 (D2) | 69 | — | presentation | Investor Presentation Q1 FY27 |
| 691f96c0 (D3) | 5 | — | pressrelease | Results Press Release. NOT a concall (no speaker turns; earnings webinar hosted later, recording pending) |
| 0d93eddb (D4) | 16 | 099a778f… | DUPLICATE of D1 | byte-identical md5 to D1 — DROPPED, not processed |

Effective document set: results (D1), presentation (D2), pressrelease (D3).
No concall transcript supplied → Role 5 (Concall Protocol) has no primary
document this quarter; the press release carries management narrative and is
enumerated for every quantitative claim and management quote.

## Live Notion thesis (passed inline to A3/A4)
- Decision Status: HELD (2% position, trimmed from 3% post Q4 FY26)
- Cost Rs 2,015 | Entry Price Max Rs 1,439 | MoS Rs 1,151 | Destination PE 30x
- Gate 0: 133/160 EXCELLENT | EM 41/100 MOAT EXPANSION UNDERWAY
- Thesis status: WEAKENED post Q4 FY26. Q1 FY27 explicitly flagged the DECISION EVENT.
- Thesis-break conditions: EBITDA <30% for 2Q OR paying suppliers <209k for 2Q.
- Promoter: TRUSTWORTHY-with-flags (2yr Rule 11(g) audit-trail pattern; Goodwill KAM added FY26).
- Prior-quarter reference figures (Q4/FY26): active buyers 41M (-3% YoY first-ever decline);
  top-10% ARPU decel 17%→9%; ~50% SOM saturation admitted; Busy +81% rev FY26 (Rs 119Cr);
  treasury Rs 3,618Cr; CFO/PAT 1.46x.

### Monitoring checklist (Green / Red)
1. Net paying suppliers (seq): G net adds >2,000 & base >222k | R net adds <0 or base <215k
2. Active buyers (LTM): G >42M | R <40M any quarter
3. Unique business inquiries: G >28M/q | R <25M or -5% YoY 2Q
4. Top 10% ARPU growth YoY: G >9% sustained | R <8% 2 consec q
5. Standalone EBITDA margin: G 33-37% | R <30% 2 consec q
6. CFO/PAT (rolling 12m): G >1.0x | R <0.8x 2Q
7. Busy Infotech billing growth YoY: G >25% | R <20% or margin declining
8. Promoter shareholding: G 48.5-49.5% & 0% pledge | R <47% or any pledge
9. Treasury Other Income (rolling 4Q): G Rs 180-280Cr | R seq drop >50%
10. Auditor commentary: G clean unmodified | R any qualification / KAM escalation / auditor change

## Gate log
### GATE A1 (page coverage 100%)
- results: PASS — 16pp, 16 formfeeds, 727 lines, units Millions (x0.1 to Cr), no OCR
- presentation: PASS — 69pp, 69 formfeeds, 2050 lines, units Crores (ops counts in M/K per footnotes), OCR pages 5,10,36,42,54,59,62
- pressrelease: PASS — 5pp, 5 formfeeds, 194 lines, units Crores, no OCR
All three A1 gates PASS.

### GATE A2 (count test)
- results: PASS — 14 notes, 65 line items, 1 zero-standing, 2 agenda items, 16 auditor paras, 13 entities. Flags: SIGNATURE_BEFORE_MEETING_CONCLUDED x2, ENTITY_CHANGE 4/13, ENTITY_UNAUDITED_MGMT_FURNISHED (IB MonotaRO exit), NEW_ENTITY_PENDING (IndiaMART Finance Ltd WOS), GOING_CONCERN_LANGUAGE
- presentation: PASS — 69 slides, 462 numbers, 1 zero-standing
- pressrelease: PASS — 3 bullets, 24 quant claims, 11 line items, 1 mgmt quote, 25 figures NOT_IN_FILING (filing is P&L-only, Q1 normal)
All three A2 gates PASS.

### GATE A3 (all F1-F17 marked, findings line-cited)
- results: PASS — F2/F4/F6/F7/F12/F13/F14/F15 FINDINGs. Key: Busy segment result (6)->(27) widening losses; C-below-S PAT gap narrowed 7.53->2.21pp; new WOS financial-services entry; ~12.2% PAT not principal-auditor audited; MD/CEO signed ~2h50m before board concluded
- presentation: PASS — F1/F6/F7/F10/F11/F16/F17 FINDINGs. Key: net supplier attrition -1,852 buried under 0% headline (Red item1); active buyers -3%->-5% 2nd consec (Red item2); Busy EBITDA margin 16%->9% YoY% omitted (Red item7); declining KPIs printed w/o minus sign; ~340Cr dividend outflow Q2FY27; promoter pledge status silent
- pressrelease: PASS — F1/F16/F17 FINDINGs. Key: headline 40% standalone EBITDA vs 35% consol; consol PAT 172<176 standalone; standalone CFO/PAT 0.87; growth realization-led ARPU undisclosed; Q1 stated AUDITED (unusual) no auditor commentary
All three A3 gates PASS.

### A4 analyst: running (merged Role 4 review; Role 5 has no concall transcript this quarter)
