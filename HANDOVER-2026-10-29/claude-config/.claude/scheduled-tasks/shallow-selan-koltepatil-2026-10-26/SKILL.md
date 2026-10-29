---
name: shallow-selan-koltepatil-2026-10-26
description: One-time shallow analysis (screens/ funnel) for Antelopus Selan Energy and Kolte-Patil Developers per screens/SHALLOW_ANALYSIS_FRAMEWORK.md.
---

Run the SHALLOW analysis (the screens/ funnel, not the deep pipeline) for two companies, in the repo at C:\Users\SUMIT SHARMA\repos\inflection-pipeline. Operator: Keerti Kaushik.

Companies:
1. Antelopus Selan Energy Ltd (formerly Selan Exploration Technology). Likely NSE symbol SELAN, BSE code 530075. Confirm the current symbol and code before use.
2. Kolte-Patil Developers Ltd. Likely NSE symbol KOLTEPATIL, BSE code 532924. Confirm before use.

Authorities. Read these first and follow them exactly:
- CLAUDE.md (repo root), especially OPERATOR VOICE, STYLE, and "Never estimate a missing number. NOT FOUND is the only valid fill."
- screens/SHALLOW_ANALYSIS_FRAMEWORK.md (the spec: Business Understanding Narrative with five questions first, then the twelve steps, step 13 forward view with forward bottom line and forward PE, then the /step1 verdict card).
- screens/README.md (how the corpus is built, which tools fetch what, and the corpus defects section).
- Use one recent card as the shape reference, for example screens/cards/SOLARA.md. Do not copy its content.
Do NOT read LESSONS.md (this is a light session). Do not run /run-pipeline, /step1, /fttcp, or any valuation beyond the step 13 forward view.

Work per company:
1. Build the corpus under screens/corpus/<TICKER>/ as the README describes: latest annual report, last two quarterly results, every concall transcript and presentation available for the last 4-6 quarters, credit-rating rationales, key exchange filings. Write MANIFEST.md and a .txt beside every PDF with ===== PAGE n ===== markers. Download into the corpus folder only; keep any helper scripts in the session scratchpad; run Python that reads downloaded files with -I.
2. Integrity check (fix from the 2026-10-18 run): open every PDF after download. If it fails to parse, re-fetch with resume (curl -C -) until it parses, and check byte counts where the file name carries one. Record any file that stays broken in MANIFEST.md.
3. Write screens/cards/<TICKER>.md from the held corpus only. Every number anchored (file, page). Target 1,900 to 2,600 words. For Kolte-Patil, use the real-estate lens (pre-sales, collections, launches pipeline, land bank, net debt, project-level margins; note any change in promoter or strategic shareholder). For Antelopus Selan, use the oil-and-gas E&P lens (production volumes, realisation vs crude, block/licence validity, capex and field development, the Antelopus transaction and the new promoter group).
4. Add a short dated section to screens/README.md for this run (2026-10-26): names, verdicts, corpus gaps, any broken files.

Git: create branch screens/shallow-2026-10-26 from the current HEAD (git switch -c). Commit ONLY screens/cards/, screens/corpus/ for these two names, and screens/README.md. Never stage data/chartink/ or any other modified file. Use git commit -q, message "screens: shallow cards for <TICKER1>, <TICKER2> (2026-10-26); run record", ending with the line: Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>. Do not push and do not open a PR. End the report with the commit hash and git log -1 --stat.

Budget: the weekly quota is small. Work the two names one after the other in this session, no parallel subagents. Keep command output trimmed. If a source is unreachable (login wall, blocked site), mark NOT FOUND with where it was looked for and continue; never fill from memory.

Final report, in STE plain English, under 15 lines per name: verdict (PROCEED to /step1, WATCH, or PASS), the 2-4 load-bearing facts, corpus gaps, card path, commit hash.