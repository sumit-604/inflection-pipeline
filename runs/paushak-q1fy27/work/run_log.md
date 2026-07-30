# Run Log — PAUSHAK Q1 FY27 Quarterly Review

## Setup (orchestrator)
- Invoked: `/run-quarterly PAUSHAK --docs <uploaded results PDF>`
- Date: 2026-07-30
- Branch: claude/paushak-quarterly-analysis-1lg8ur

## Precheck results
- Protocol files: PRESENT (Results v1.2, Concall v1.1, Master v3.3)
- Toolchain: installed poppler-utils + tesseract-ocr this session (pdftotext, pdfinfo, pdftoppm, tesseract all resolve)
- Company memory file companies/PAUSHAK.md: ABSENT (Notion page exists; see thesis packet below)

## Document class detection
- 1 document, 4 pages. Reg 33 markers ("Unaudited Financial Results", "Outcome of Board Meeting",
  "Limited Review Report"), BSE Scrip 532742 / NSE PAUSHAKLTD. Quarter ended 30 June 2026.
- CLASS = results. Quarter = q1fy27.
- Page char density: p1=1244, p2=2220, p3=2767, p4=555. Page 4 low-density (likely limited review report /
  signature page) -> A1 to apply OCR fallback per its protocol.

## No concall / presentation supplied
- Role 5 (concall) not run this pass. Role 4 (results) only. AGM was 30-Jul-2026 (today); concall/AR to follow.

## NOTION THESIS PACKET (live fetch 2026-07-30; page "Paushak" in COMPANIES MASTER)
Passed inline to A3 (monitoring checklist) and A4 (thesis). Subagents do not call Notion.

- Decision Status: **HELD** (4% position, avg cost Rs 424; CMP at last review Rs 480, MTM +13%)
- Gate 0: GOOD, 93/160 (core 75, moat 18/60). EM: MOAT STRENGTHENING, 38/100.
- Latest review = FY26 AR review (Role 6 v1.1), dated 03-Jul-26. Governs current thesis.
- **Re-entry / accumulation zone: Rs 100-125 (MoS Rs 100).** CMP Rs 480 = 3.8x MoS. Entry Price Max property = 125.
- Prob-weighted FV Rs 245 (compressed from Rs 506). Base FV Rs 267 (from Rs 510). Destination PE 17-21x (mid 19x).
- Revised FY28 EPS: Bear 8.15 / Base 14.03 / Bull 20.88. Probabilities re-weighted 40/45/15.
- Hurdle Ratio 0.45 vs benchmark 1.953 = FAIL. HOLD as momentum via chandelier daily-close exit.
- Trim ladder: Rs 500 -> 3%, Rs 550 -> 2%, Rs 600 -> 1%.

### Active tripwires / monitoring checklist for Q1 FY27 (the reason this review exists)
1. **West Asia RM cost spike (March 2026) unabsorbed in selling prices -> Q1 FY27 GROSS-MARGIN HEADWIND flagged.**
   Watch gross margin and material cost % this quarter.
2. **Add-back trigger TIGHTENED to ALL FIVE conditions in Q1 FY27** before the position can be re-rated up:
   (a) revenue > Rs 65 Cr, (b) utilization > 50%, (c) core Op PBT > Rs 13 Cr, (d) EBITDA margin >= 28%,
   (e) named customer/contract disclosure. Any miss = no add-back.
3. **Exports inflection (Growth Trigger 3, PARTIALLY FIRING):** FY26 exports +68.5% YoY to 17.35% of revenue.
   Watch whether export momentum sustains; export rev > 20% YoY confirms China+1 thesis.
4. **MPP-8 plant:** capex essentially done (FY26 capital commitments Rs 5.62 Cr, down 91%). Watch utilization ramp.
5. **Standalone-vs-consolidated PAT gap** and any Other Income windfall (FY26 Q4 was rescued by Rs 8.21 Cr OI =
   Nirayu preference redemption, an RPT with controlling company). Scrutinize Other Income quality this quarter.
6. **Governance yellow:** COO Chintan Gosaliya exited 31-Mar-26; Jain Parkash appointed WTD-only. Management Grade C.
7. **Institutional holding falling** (0.54% -> 0.25%) = informed avoidance. Watch shareholding pattern if disclosed.
8. China+1 named-contract narrative silence = DROPPED tracker item.
