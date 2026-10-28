# Run log — SYNGENE q2fy27 (/run-quarterly, batch 2026-10-28, batch 2)

Session: qr-syngene, Opus 5.5 orchestrator. Worktree branch claude/qr-syngene-q2fy27-f49780, cut from run/quarterly-q2fy27-2026-10-28.

## Setup
- Sparse checkout: tools/sparse_session.sh runs/syngene-q2fy27 (tree 92 MB).
- Checkout guard: git fetch origin main OK; diff over .claude/ prompts/ frameworks/ CLAUDE.md LESSONS.md empty. PASS.
- Protocol files present: Quarterly_Results_Review_Protocol_v1_4.md, Quarterly_Concall_Analysis_Protocol_v1_1.md, Document_Review_Protocol_v1_1.md, Master_Project_Prompt_v3_6.md.
- Toolchain: pdftotext, pdfinfo, pdffonts, pdftoppm on PATH; tesseract at C:/Program Files/Tesseract-OCR/tesseract.exe.
- Company memory: companies/SYNGENE.md read (SHALLOW WATCH, Halt 1 28-Sep-2026; tripwires T1-T10; re-engage R1-R3).
- Notion: COMPANIES MASTER page 3e9bb2b9d3ab8168afd5ca86954e8113 fetched live 28-Oct (read only). Snapshot saved to work/notion_snapshot_2026-10-28.md. Decision Status blank (operator-only). No Notion write in this run (batch standing instruction 6).
- Prior-quarter quarterly extracts: none in repo (Q1 FY27 PDFs exist only as Step-1 inputs in runs/syngene-2026-09-15). Diffs against prior quarter rely on the comparative columns inside this quarter's filing.

## Document class detection (content, first pages)
| File | Pages | Class | Basis |
|---|---|---|---|
| Syngene_Q2FY27_Results.pdf | 11 | results | "Outcome of the Board Meeting", Un-audited financial results standalone and consolidated, Reg 33 |
| Syngene_Q2FY27_Investor_Presentation.pdf | 32 | presentation | Reg 30 cover letter + slide pages, sparse text per page |
| Syngene_Q2FY27_Press_Release.pdf | 9 | pressrelease (A1 doctype presentation-class narrative) | Reg 30 cover, press release headline "Syngene reports sequential revenue growth of 13% in Q2 FY27" |
| Syngene_Change_In_Management.pdf | 4 | disclosure (A1 only; fact carried to A4 as governance item) | Reg 30 Schedule III Part A Para A(7) change in management |
| Concall transcript | n/a | concall | ABSENT at run start (call 28-Oct 09:00; recording not posted). Re-check before A4. |

## Agent runs
(see session-cost.md for tokens)
- A1 results / presentation / pressrelease / disclosure: GATE A1 pass on all four (11/11, 32/32, 9/9, 4/4 pages). Results and press-release statement pages had scrambled -layout text; A1 used pdftotext -raw after a render check (logged in each header).
- A2 results / presentation / pressrelease: GATE A2 pass (828/828, 350/350, 879/879 IDs; zero orphans). Each A2 below its A1 in tokens. Deck M01-M09 and press-release L32 postal codes carried as MISSING_FROM_STRUCTURED ledger rows (non-financial); no A1 loop.
- A3 results / presentation / pressrelease: GATE A3 pass (F1-F17 all statused in each block). 16 + 17 + 26 findings.
- Disclosure (change in management): A1 only, per coordinator instruction; facts go to A4 as a governance item.
- Transcript check before A4 (28-Oct 18:18 IST): concall_audio/Syngene_Q2FY27_Concall_Transcript_ASR.txt ABSENT. Folder empty. A4 runs on filed documents only; Role 5 protocol not passed.
- A4 (28-Oct): PROCEED WITH FLAGS; T3 FIRED; T4 FIRED (conservative, contested); no re-engage trigger.
- A5 loop 0: INCOMPLETE (3 FACTUAL, 4 MISSING, 2 CONTRADICTION, 8 STYLE), all looped to A4. Loop-0 review and audit kept as *.loop0.md.
- Correction loop 1: A4 resumed and fixed the nine items (diff 56 lines, all at patch sites). A5 resumed and re-audited: COMPLETE, style notes only, no drift.
- Notion: no write. Payload in notion-payload.md (Key Notes line carries the two qualifiers A5 asked for at L1-S5; no number changed).
- Agent temp folders (work/a1_*_tmp, work/a2_*_tmp) deleted before commit; no page images remained.
- Close-out: session-cost.md, then operator-brief.md, then commit.
