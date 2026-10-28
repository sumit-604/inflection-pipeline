# NOTION PAYLOAD — UNIMECH Q2 FY27 (FOR OPERATOR APPROVAL; NOT WRITTEN)

Write gate (operator ruling 2026-10-03): no approval was given in this run, and the batch instruction says "do not write to Notion". Nothing below was written. Claude web (or a later approved run) executes it.

Target page: COMPANIES MASTER, "Unimech Aerospace and Manufacturing Ltd"
Page id: 36fbb2b9d3ab814e8a31e6b1f305f9f9
URL: https://app.notion.com/p/36fbb2b9d3ab814e8a31e6b1f305f9f9
Page state read live: 28-Oct-2026 (last edit 26-Oct-2026 17:16 UTC; snapshot runs/unimech-q2fy27/work/notion_page_unimech_2026-10-28.md). Re-fetch before writing; if the page changed after 26-Oct-2026, merge, do not overwrite.

## A. update_properties

Decision Status: NOT WRITTEN (operator only). Stays WATCHLIST / BUY ON DIPS.

| Property | Current | Proposed |
|---|---|---|
| Current Market Price | 1616 | 1638 (screener.in, 28-Oct-2026 08:48 IST) |
| Analysis Date | 2026-10-26 | 2026-10-28 |
| Key Notes | (audit trail, latest 26-Oct-2026) | PREPEND the line in A1, keep every prior entry |

### A1. Key Notes line to PREPEND (pipes inside the text escaped as \|)

```
28-Oct-2026 \| Q2 FY27 QUARTERLY REVIEW (/run-quarterly; results 27-Oct, call 28-Oct ASR) \[FILED, runs/unimech-q2fy27/work/review_unimech_q2fy27.md; A5 COMPLETE after 1 loop\]: Rev Rs123.00 Cr (+98.4% YoY, Hobel inside from 27-Apr), op EBITDA 39.84% (29.92% LY), PAT Rs31.77 Cr (clean Rs30.56 Cr ex Rs1.22 Cr prior-period tax). Firm order book Rs266 Cr, down 2nd quarter (Rs280.3 Cr Q1); Rs855 Cr headline adds Rs589 Cr non-binding LTA/award; "8x" compares unlike bases (firm +153%). H1 CFO/PAT 0.896x: Pillar 2 upgrade NOT MET. Net cash Rs479.71 Cr to Rs65.45 Cr; borrowings +43.6% to Rs160.98 Cr; goodwill Rs321.99 Cr = 40.3% of equity; filed ROCE 14.9% (call ~20%, unverified). Saudi JV ~USD 30 Mn joint investment: Unimech's remaining 51% about Rs108 Cr vs about Rs26 Cr net cash after ODI; equity raise early CY2027. Honeywell LTA effective 1-Apr-2026, filed 208 days later, no value. IPO Rs250 Cr fully used; CARE "Deviation: None" vs company "Yes"; CARE total row Rs153.30 vs Rs247.80 Cr of object rows. CRISIL silent 6th call; segment margins refused as policy, trigger (c) untestable until FY27 AR. Triggers (a) (b) (c) NOT fired; (d) PARTIAL / WATCH (persistence leg confirmed; cumulative hygiene ruling pending). Credibility Grade C (46.9%); Promoter Verdict downgrade candidate (operator). Separating observation: Q3 firm order book (bull >= Rs300 Cr, bear < Rs266 Cr), about Feb-2027. Price Rs1,638 (screener.in, 28-Oct 08:48 IST), 7.7x Rs213 entry. No trigger fired. WATCHLIST / BUY ON DIPS unchanged (operator-only). Position: None.
```

## B. insert_content, position: end (split across sequential inserts)

Insert the following, in order, as full content (complete tables, never summaries). Escape `|` inside table cells as `\|` where a cell carries a literal pipe.

1. Heading: `# Q2 FY27 QUARTERLY REVIEW (quarter ended 30-Sep-2026) — filed 27-Oct-2026, call 28-Oct-2026`
2. The full merged review, file `runs/unimech-q2fy27/work/review_unimech_q2fy27.md` (1,241 lines after loop 1), from its first line to the end of section "5. FORWARD MAP". It INCLUDES the LOOP 1 CHANGE LOG and the PLAIN-LANGUAGE BRIEF (summary narrative, sector, business-model, competition intelligence, forward map). Drop only the trailing YAML block. Suggested split: inserts at the "# SECTION A", "# SECTION B", "## LOOP 1 CHANGE LOG" and "# PLAIN-LANGUAGE BRIEF" headings (four to six inserts).
3. Heading `## A3 forensics (completeness proof)` then the F1-F17 status table and the findings table from each of:
   - `runs/unimech-q2fy27/work/forensics_results_unimech_q2fy27.md` (R-A3-01..25)
   - `runs/unimech-q2fy27/work/forensics_presentation_unimech_q2fy27.md` (D-A3-01..27)
   - `runs/unimech-q2fy27/work/forensics_pressrelease_unimech_q2fy27.md` (P-A3-01..10)
   - `runs/unimech-q2fy27/work/forensics_concall_unimech_q2fy27.md` (C-A3-01..25)
   - `runs/unimech-q2fy27/work/forensics_loop1_addendum_unimech_q2fy27.md` (D-A3-28, C-A3-26)
4. Heading `## A5 audit verdict` then:
   - Loop 0: INCOMPLETE. 0 FACTUAL, 5 MISSING (M1 A2 question count; M2 utilisation qualifier; M3 other-income heads; M4 Hobel acquisition economics; M5 Honeywell effective date), 1 CONTRADICTION (C1 Saudi funding gap on an unanchored SAR 60M), 9 STYLE. Source `runs/unimech-q2fy27/work/audit_unimech_q2fy27.md`.
   - Loop 1: COMPLETE. C1 and M1-M5 CLOSED; drift check PASS (27 diff hunks map to patches P01-P34); 5 STYLE notes logged. Source `runs/unimech-q2fy27/work/audit_loop1_unimech_q2fy27.md`.
   - Coverage: 17 notes / 65 turns (25 analyst questions) / 26 slides + 3 press-release pages, all reviewed; structured IDs 953 / 670 / 123 / 257 plus supporting 261 / 68 / 31, zero orphans.
5. Heading `## Run record` then: branch claude/qr-unimech-q2fy27-1b1895, commit hash (fill from the run's commit), session-cost total 2,909,985 tokens, 1 correction loop.

## C. Not proposed in this save
- Decision Status, Entry Price Max, Margin of Safety Price, Position Size, Promoter Verdict: operator only.
- Tracker rows (DOWNSTREAM SIGNAL TRACKER): none proposed. The review's forward map names candidates (Saudi second tranche date, Q3 firm order book, Honeywell first PO); Role 5.5 decides.
