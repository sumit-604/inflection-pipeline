# QUARTERLY RUN LOG — MAXIND Q1 FY27

Orchestrator: /run-quarterly (concall-only)
Run date: 2026-08-12
Ticker: MAXIND (Max India Limited)
Quarter: Q1 FY27 (quarter ended 30 June 2026)

## Setup and prechecks
- **Docs supplied:** ONE concall transcript (plain text, operator-pasted). No Reg 33 results filing, no investor presentation supplied this run. => Concall-only quarterly review (Role 5). Role 4 (results) not run; Results protocol not required.
- **Protocol-file check:** Quarterly_Concall_Analysis_Protocol_v1_1.md PRESENT; Master_Project_Prompt_v3.3.md PRESENT. Results protocol NOT required (no results filing). PASS.
- **Toolchain precheck:** pdftotext/pdfinfo/pdftoppm/tesseract MISSING; apt install failed (restricted env). NOT ON CRITICAL PATH — input is already plain text; A1 rule 4 saves text concall verbatim and line-numbers directly (no pdftotext/OCR needed). No PDF/image pages in scope. PASS.
- **Document-class detection:** speaker-turn structure ("Ladies and gentlemen", moderator, "We take the next question from the line of ...", analyst firm names) => **concall**. Recorded.
- **Run folder:** runs/maxind-q1fy27/ (inputs/, work/). Transcript at inputs/concall_maxind_q1fy27.txt.

## Company memory + Notion (fetched live 2026-08-12)
- companies/MAXIND.md: ABSENT (Phase-1 run maxind-2026-07-24 never finalized; reached B02-pass1 only). Prior operator-context.md carries a 6-month operational summary — treated as NON-ANCHORED lead only.
- Notion page: "Max India Ltd (MAXIND)" (3a8bb2b9-d3ab-8129-af53-e4688a879c19). Live thesis extracted:
  - **Decision Status: WATCHLIST** (analysis date 2026-07-28; "DEEP WATCH leaning FAVOURABLE, monitor toward BUY-ON-DIPS"). CMP context ₹182.
  - **Entry ladder:** MoS BUY ≤ ₹120 | 25% CAGR entry ₹120-150 | Fair value ₹150-220 | Overvalued > ₹220. SOTP fair value ₹152-222 (midpoint ~₹187).
  - **FTTCP composite +3/8:** Revenue FIRING (+2), Margin STARTING (+1), Cash STARTING (+1), ROCE DECLINING (-1).
  - **Active flags:** FLAG-PROMOTER CONCERN; FLAG-CASH INDETERMINATE; FLAG-GATE0 AVOID.
  - **Thesis-broken triggers:** Q2 FY27 AACSL segment loss > ₹35 Cr/Q AND CBPL handovers < 100 units by end-Q2 FY27; Chairman comp dissent > 25% at next renewal; new fraud/CARO qualification; subsidiary impairment charge.
  - **Single cleanest Q1 FY27 metric:** AACSL segment loss/revenue ratio (FY26 1.03x; target < 0.85x by Q4 FY27); also CBPL Phase 1 handover count.

## Sequence status
- A1 concall: PENDING
