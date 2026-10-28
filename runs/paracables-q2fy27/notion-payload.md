# NOTION PAYLOAD: PARACABLES Q2 FY27 quarterly review (NOT WRITTEN)

Status: proposed only. Nothing was written to Notion (batch instruction 6; /run-quarterly write gate). The operator approves, then claude.ai or a later Claude Code session executes.

Gate note: the orchestrator rule saves to Notion only after A5 COMPLETE. A5 ended INCOMPLETE with one open item, C1: three slide-index cells in the deck ledger (work/ledger_presentation_paracables_q2fy27.md lines 49, 52, 54). C1 changes no review number and no verdict-card number. The operator decides whether that blocks the save.

Run folder: runs/paracables-q2fy27/ on branch claude/qr-paracables-q2fy27-a220cd (commit hash in the session report and in operator-brief.md).

## 1. COMPANIES MASTER page

- Page: "Paramount Communications", id 345bb2b9-d3ab-808f-9f1d-e0960dc67726, https://app.notion.com/p/345bb2b9d3ab808f9f1de0960dc67726
- Fetch the page first. It was last edited 2026-10-26 17:17 UTC when this run read it.

### 1a. Properties

| Property | Action | Value |
|---|---|---|
| Decision Status | DO NOT WRITE | stays WATCHLIST / AVOID (operator-only). No pre-committed trigger formally fired. |
| Key Notes | PREPEND (keep every prior entry after a `\|` separator) | see 1b |
| Analysis Date | set | 2026-10-28 |
| Current Market Price | set | 63.8 (screener.in, 28-Oct-2026 08:48 IST) |

### 1b. Key Notes line to prepend (exact text)

```
28-Oct-2026 Q2 FY27 /run-quarterly REVIEW [FILED results + deck + release; call = machine ASR, unverified]: verdict PROCEED WITH FLAGS; cash INDETERMINATE-WITH-DIRECTION. SA op margin 7.30% (+596 bps YoY, all from an unexplained other-expense reversal; gross margin -147 bps); core PBT 28.59; H1 CFO (31.89), second negative H1; receivable days ~66; Rs 73.39 Cr issue proceeds "utilised", objects unnamed, call says supplier payments; Narmadapuram ~Rs 33 Cr of Rs 300 Cr visible, LT debt not tied; ROCE 13.7% pre-build (~10.1% with plant capital); Q3 tariff clawback to strip; credibility 66.7% (n=3) Grade B provisional (33-75% on rescoring); tracker has 2 signals, both internal (OR-17 floor of 3 external fails). Indicative FY27E PAT 92.4 / FY28E 95.6, 23.1x / 22.3x at Rs 63.8 (not Role 1). A5 INCOMPLETE: 1 ledger-index item (C1) after 1 loop. AVOID unchanged (operator-only).
```

When pasted into the pipe-delimited audit trail, no `|` appears inside this line.

### 1c. Page content (insert_content, position: end, split across sequential inserts)

Insert in this order, full text, never summaries:
1. Heading: "Q2 FY27 Quarterly Review: /run-quarterly, 28 Oct 2026"
2. runs/paracables-q2fy27/work/review_paracables_q2fy27.md, the whole file (Role 4, Role 5, Sections C to E, monitorables, the PLAIN-LANGUAGE BRIEF, and the correction loop log). Escape `|` inside table cells as `\|`.
3. A3 forensics tables: runs/paracables-q2fy27/work/forensics_results_paracables_q2fy27.md, forensics_concall_paracables_q2fy27.md, forensics_presentation_paracables_q2fy27.md, forensics_pressrelease_paracables_q2fy27.md (the F1-F17 scorecard and findings table of each).
4. A5 audit verdict: the "## VERDICT" table and the "## RE-AUDIT (loop 1)" section of runs/paracables-q2fy27/work/audit_paracables_q2fy27.md.

## 2. DOWNSTREAM SIGNAL TRACKER (collection://926b65ce-ddd2-4d8b-8eae-05e66b6f6c9f)

Proposed by A4, review Step 5.5C. None written.

Updates (Case A):
- Row "PARACABLES — Receivables exit DSO + operating CFO (structural-vs-timing)" (https://app.notion.com/p/3d7bb2b9d3ab8176a156f884579d1a28): Last Observation Date 2026-10-28; Last Observation Value "30-Sep-2026 filed: trade receivables Rs 394.79 Cr, ~64-68 days; H1 FY27 standalone CFO -Rs 31.89 Cr (inventory build and payables paydown); receivable leg reads timing, CFO leg threatens"; Direction vs Prior Falling (days); Signal Health Neutral, pending the operator's ruling on the CFO leg (the Falsifying Observation's "operating CFO negative again" is met on a literal reading).
- Row "PARACABLES — Preferential-issue allottees + promoter warrant conversion" (https://app.notion.com/p/3d7bb2b9d3ab81c7ab0ce748179ee2c6): Last Observation Date 2026-10-28; Last Observation Value "30-Sep-2026: 72,00,000 promoter warrants unconverted; balance due Rs 22.68 Cr; warrants ~Rs 14.4 in the money at the 30-Sep deck market cap, so conversion is arbitrage and non-conversion is the informative outcome"; Direction Flat; Signal Health Neutral.

New rows (Case B), Affected Companies = the COMPANIES MASTER page above:
1. "PARACABLES — Narmadapuram capex build (CWIP + capital advances) and LT debt tie-up". Tier 2 - Trajectory; Company Filing-Event; Quarterly. Falsifying Observation: at 31-Mar-2027, CWIP plus capital advances below half of the Rs 300 Cr Phase 1 while the Q1 FY28 date stands means date-slip risk.
2. "LME aluminium price (Paramount metal input)". Tier 2 - Trajectory; Sector-Macro Proxy; Monthly. Basis: aluminium is over 75% of metal value consumed (call, ASR).
3. "US tariff regime on Indian cable imports (post-IEEPA framework)". Tier 2 - Trajectory; Sector-Macro Proxy; Event-Driven. Basis: exports 28.2% of Q2 revenue.
4. "HTLS reconductoring tender awards (PGCIL and state transcos)". Tier 2 - Trajectory; Customer Capex Disclosure; Event-Driven. Basis: Rs 200+ Cr HTLS book, tenders under bid.

Rows 2 to 4 are EXTERNAL. With them the company would clear the OR-17 floor of three external signals. Each needs a Primary Source URL chosen in claude.ai against the Downstream Source Discovery Protocol; none was verified in this run.
