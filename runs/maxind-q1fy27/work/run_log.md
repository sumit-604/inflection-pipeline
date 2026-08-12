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
- A1 concall: PASS (100% coverage, 141 lines, text source).
- A2 concall: PASS (count test reconciled: 69 turns / 21 questions / 79 mgmt numbers / 24 fwd-hedge phrases / 1 zero-standing).
- A3 concall: PASS (F1-F17 all statused; 13 findings line-cited; 6 forward-signal, 4 ambiguous).
- A4 analyst: complete (concall-only Role 5; Role 4 N.A.). Verdict PROCEED WITH FLAGS; cash INDETERMINATE; WATCHLIST held; OVERPROMISER-WATCH archetype.
- A5 adversary: loop 1 INCOMPLETE (1 gap: missing surviving bear counter on capital pillar) -> A4 revised -> loop 2 COMPLETE.
- Notion save: DONE (4 content inserts + Key Notes prepend; Decision Status unchanged WATCHLIST; 3 dated entries preserved).

## Verdict summary
- Protocol verdict: PROCEED WITH FLAGS. Cash conversion: INDETERMINATE (CFO refused; missing evidence named).
- No pre-committed thesis-broken trigger fired. Q2 AACSL-loss + Noida-handover compound trigger ARMED.
- Checklist net-negative: item 4 -> GREEN (AGEasy breakeven reaffirmed); item 8 -> RED (standalone treasury Rs21cr); item 2 -> RED-on-Q1-count (0 completed possessions); items 1/3/9 UNKNOWN.
- Flags: FLAG-PROMOTER CONCERN (promoter absent), FLAG-CASH INDETERMINATE (sharpened), FLAG-GATE0 AVOID, new STANDALONE-TREASURY-RED, CAPITAL-QUALITY.

## Clean run note
Clean run mechanically (all gates passed first attempt except A5 loop 1, which is the intended adversarial catch, resolved in 1 loop). No toolchain blocker (text concall, no PDF tools needed). No results filing or presentation supplied this quarter (concall-only); Role 4 deferred.
