# Notion payload: NETWEB Q2 FY27 (NOT WRITTEN)

Status: NOT WRITTEN. Batch instruction 6 (runs/_batch-q2fy27-1028.md) says "Do not write to Notion. Write notion-payload.md in the run folder for the operator's approval." The /run-quarterly write gate also needs the operator's explicit approval in the run. No approval was given. claude.ai or the operator executes this payload.

Decision Status: NEVER WRITTEN by /run-quarterly. Current value HELD. No change proposed by this run. A breached pre-committed trigger is flagged below; the operator decides.

## Target

- Page: COMPANIES MASTER, "Netweb Technologies India Ltd"
- Page ID: 353bb2b9-d3ab-8114-8b87-c619f5507cb6
- URL: https://app.notion.com/p/353bb2b9d3ab81148b87c619f5507cb6
- Data source: collection://345bb2b9-d3ab-8032-9b46-000ba16ab827
- Page state when read: last edited 2026-10-26 17:13 UTC. Fetch the page again before writing; if it changed after that time, merge, do not overwrite.
- Note: the page already holds a claude.ai section "Q2 FY27 Results Review: cash gate fails, QIP funded inventory, 25-Oct-2026". This payload adds the pipeline review of the same quarter plus the call. It does not replace that section.

## Properties

- Decision Status: leave unchanged (HELD). Never written by this pipeline.
- Current Market Price: optional, 4404 (screener.in, 28-Oct-2026 08:48 IST, from _CMP_snapshot_2026-10-28.md). Operator's choice.
- Analysis Date: 2026-10-28
- Key Notes: PREPEND this line, then " | ", then the existing pipe-delimited trail unchanged (escape any "|" inside the line as "\|"):

```
28-Oct-2026: Q2 FY27 /run-quarterly (results + earnings deck + strategy deck + press release + call; call evidence is a machine transcript, unverified; A5 COMPLETE after 1 loop). Verdict PROCEED WITH FLAGS; cash conversion INDETERMINATE-WITH-DIRECTION (adverse). Q2 rev Rs 1,323.28 Cr (+335.7% YoY), PAT Rs 136.66 Cr, Op EBITDA margin 14.91%; margin after finance cost 13.11% vs 14.66% (-155 bps). H1 CFO -Rs 639.15 Cr, CFO/PAT -2.88x; inventory Rs 804.84 to 1,930.69 Cr; Q2 finance cost Rs 23.80 Cr vs Rs 12.95 Cr all FY26. QIP Rs 1,200 Cr bridge closes from the deck: 767 used + 403 unused + 30 issue budget; company net cash Rs 124.4 to 13.6 Cr. Filed H1 column non-additive by Rs 5.22 Cr (H1 margin 15.07% filed vs 14.83% added). Call: FY27 target Rs 4,000 Cr implies H2 about 30% below Q2; H1 margin "not to be quoted for the entire year"; growth band floor 35% to 30% unacknowledged; no CFO figure, "no pressure" on cash; Rubin offered "by January"; Taiwan R&D WOS approved, cost TBD. FLAG: thesis-broken #1 BREACHED on the H1 reading; firing is operator ruling (1), open. Checklist #1, #5, #6, #11 RED. Indicative FY27E/FY28E PAT Rs 399.42 / 515.97 Cr, fwd PE 65.5x / 50.7x at Rs 4,404 (not Role 1). Decision Status unchanged (operator-only). Repo: runs/netweb-q2fy27, branch claude/qr-netweb-q2fy27-a60c5c, commit "quarterly review: NETWEB q2fy27" (hash in the run report).
```

## Content (insert_content, position: end, split across sequential inserts)

Insert, verbatim and in this order (escape "|" inside table cells as "\|"):

1. Header line: "Q2 FY27 QUARTERLY REVIEW (/run-quarterly, 2026-10-28). Results, earnings deck, strategy deck, press release and call. Call evidence is a machine transcript; every call number is management tier, unverified. Thesis check against Decision Status HELD."
2. The full merged review: runs/netweb-q2fy27/work/review_netweb_q2fy27.md (Section A Role 4, Section B Role 5, Section C combined verdict, monitorables, REVISION LOG (loop 1), and the PLAIN-LANGUAGE BRIEF as the final section). Complete tables, never a summary. The closing YAML block may be omitted from the Notion copy.
3. The five A3 forensics tables (F1-F17 status table and findings list of each):
   - runs/netweb-q2fy27/work/forensics_results_netweb_q2fy27.md (RES-A3-01..17)
   - runs/netweb-q2fy27/work/forensics_presentation_netweb_q2fy27.md (PRS-A3-01..19)
   - runs/netweb-q2fy27/work/forensics_strategy_netweb_q2fy27.md (STR-F6-a..F17-b)
   - runs/netweb-q2fy27/work/forensics_pressrelease_netweb_q2fy27.md (PR-FN01..12)
   - runs/netweb-q2fy27/work/forensics_concall_netweb_q2fy27.md (CC-A3-01..22)
4. A5 audit verdict: the final YAML block of runs/netweb-q2fy27/work/audit_netweb_q2fy27.md (LOOP 1 RE-AUDIT section).
5. The operator brief: runs/netweb-q2fy27/operator-brief.md (indicative estimates; not a Role 1 valuation).

## Flags for the Key Notes reader

- Pre-committed trigger: thesis-broken #1 ("FY27 CFO/PAT below 0.50x cumulative") is BREACHED on the H1 reading. If the operator rules that H1 counts, the page's Position Management rule says exit regardless of the Chandelier. Not executed, not written.
- Open operator rulings carried from the 25-Oct and 26-Oct entries: (1) does H1 fire #1; (2) FY27-alone vs cumulative reading; (3) CCC method; (4) QIP dilution vs the 15 pp promoter limit; (5) the Rs 5,500 trim at the Rs 5,813 high.
- Pillar-relevant facts flagged for /fttcp and Role 1 (OR-30): cash multiplier input (H1 CFO/PAT -2.88x), ROCE and ROE on post-QIP equity (ROE 21.1% on closing equity), growth-visibility inputs (book Rs 2,629.0 Cr, L1 Rs 652.5 Cr, book plus L1 down about Rs 73 Cr QoQ). Review Steps 6.5, 7 and Role 5 Step 8D.
- Role 5.5: tracker rows not supplied; fewer than three signals exist. Five new signal candidates are listed in review Step 5.5C (payload rows only, not written).
- Company memory file companies/NETWEB.md does not exist. This run did not create it.
