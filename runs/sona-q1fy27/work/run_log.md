# Run Log — Sona BLW Precision Forgings (SONACOMS) Q1 FY27 Quarterly Review

Pipeline: /run-quarterly (five-agent extraction-first)
Run date: 2026-07-23
Quarter: Q1 FY27 (quarter ended 30 June 2026)
Operator: Keerti Kaushik

## Setup and prechecks
- Protocol files present: Quarterly_Results_Review_Protocol_v1_2.md,
  Quarterly_Concall_Analysis_Protocol_v1_1.md, Master_Project_Prompt_v3.3.md — PASS
- Toolchain: pdftotext, pdfinfo, pdftoppm, tesseract installed (apt-get, after
  apt-get update fixed stale poppler pin) — PASS
- Company memory file companies/SONACOMS.md: ABSENT (no prior file). Notion
  fetched live instead.

## Document class detection
| Doc | File | Pages | Class |
|-----|------|-------|-------|
| 1 | results_sona_q1fy27.pdf (was 70651f11) | 10 | results (Reg 33 Board Outcome + Unaudited Standalone & Consolidated Results + limited review reports) |
| 2 | presentation_sona_q1fy27.pdf (was d1b6a836) | 41 | presentation (Investor Presentation, Reg 30) |
| 3 | pressrelease_sona_q1fy27.pdf (was 07f7bee8) | 4 | presentation-class (Press Release, Reg 30 management narrative). Routed as doctype=presentation with distinct filenames; no concall transcript supplied. |

Note: no concall transcript in --docs, so Role 5 has no concall input this run;
A4 runs Role 4 (filing) fully and treats the presentation + press release as
management-narrative inputs feeding Role 4.

## Live Notion thesis (fetched 2026-07-23; page last edited 2026-07-13)
- Decision Status: WATCHLIST / AVOID at CMP Rs 609
- Destination PE: ~22.5x (revised down from 24x after FY26 AR deep dive)
- Base FY29 EPS Rs 16 -> Base FY29 fair value ~Rs 384 (negative CAGR from CMP)
- Return matrix: 0/9 cells >=25% CAGR, 0/9 cells >=15% CAGR
- Buyable trigger: CMP <=Rs 185 AND ROCE >18% AND Novelic KAM resolved
- Entry levels: 25% CAGR entry ~Rs 197; MoS ~Rs 157; quality-hold ~Rs 385
- Position size: None. Promoter Verdict: TRUSTWORTHY (Aureus 28.02%, no pledge)
- Q1 FY27 gate: BINDING (this review is that gate)

### Active tripwires / monitoring checklist (passed inline to A3, A4)
1. ROCE <14% for 2 consecutive years -> PERMANENT AVOID
2. Forced block sale from control dispute -> PERMANENT AVOID
3. Novelic KAM impairment materially exceeds Rs 350 Cr
4. CFO/PAT below 1.0x sustained (FY26 was 1.05x; monitoring)
5. Corporate guarantee expansion
6. Margin compression watch (FY26 EBITDA 24.7%, -270bps)
7. Working capital stretch (FY26 receivable days +22, CFO/PAT 1.05x)
8. Railway diversification delivery (Escorts Kubota transition; FY26 railway
   Rs 973 Cr rev + Rs 149 Cr PAT in 10mo)
9. BEV anchor customer weakness (order book ~70% EV programs)
10. India revenue mix rising (FY26 51% vs 29%) — Trigger #3 already fired
    (diversification, constructive)

### FY26 baseline for YoY comparison
- Revenue FY26 ~Rs 4,449-4,475 Cr (+25.5% YoY)
- EBITDA margin 24.7% (-270bps); ROE 13.2% (-450bps); ROCE ~16%
- Reported PAT FY26 Rs 629 Cr (adj ~Rs 670 Cr); EPS ~Rs 10.1
- Order book Rs 23,700 Cr (~70% EV programs)
- Novelic: Rs 350 Cr investment, Rs 19 Cr FY26 loss, impairment indicator
- Total voting capital anchor: 62,20,34,837 shares (paid-up Rs 622.03 Cr)
