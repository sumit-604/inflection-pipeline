# Notion payload: KNACK Q2 FY27 quarterly review (NOT WRITTEN; awaiting operator approval)

Status: not sent. Batch standing instruction 6 (28-Oct-2026) says no Notion write in this session. The orchestrator write gate (operator ruling 2026-10-03) needs explicit operator approval in the run. This file is the payload for that approval. Execute it from claude.ai or an approved session.

Pre-write check done 28-Oct-2026 (read only): COMPANIES MASTER (data source `collection://345bb2b9-d3ab-8032-9b46-000ba16ab827`) holds NO Knack page. Searches "Knack Packaging" and "KNACK 544814" returned none. So this payload CREATES a new row. Re-search before writing, in case a page was added since.

## Step 1. Create the page (one row in COMPANIES MASTER)

Parent: data source `collection://345bb2b9-d3ab-8032-9b46-000ba16ab827`

Properties (names as used in the sibling WEWORK payload; check them against the live schema before writing):

| Property | Type | Value |
|---|---|---|
| Name | title | Knack Packaging Ltd (KNACK) |
| Ticker | text | KNACK |
| Sector | text | Packaging: printed laminated woven PP (PLWPP) bags, pinch-bottom bags, FIBC |
| SECTOR | select | Packaging if that option exists in the live schema; otherwise Other |
| Current Market Price | number | 197 |
| Analysis Date | text | 28-Oct-2026 |
| date:Analysis Date 1:start | date | 2026-10-28 |
| Key Notes | text | (line below) |
| Decision Status | select | DO NOT WRITE. Leave empty. The operator sets it. |

Key Notes line (first entry; no prior audit trail exists):

```
28-Oct-2026 Q2 FY27 quarterly review (pre-thesis read, /run-quarterly): PROCEED WITH FLAGS; A5 COMPLETE after 1 loop. Rev from ops +52.5% YoY to Rs 294.76 Cr [FILED], price-led (tonnes about +13% [MGMT, ASR]). Operating EBITDA margin ex-OI 13.59% (-807 bps QoQ); gross margin 34.64% vs 42.07% in Q1 [FILED, INFERENCE]; press-release 16.35% includes OI on total income. PAT +21.2% to Rs 25.02 Cr, about 71% from OI and a one-time DT credit; OI 29% of PBT; filed H1 interest Rs 6.13 Cr vs Q2 OI Rs 9.70 Cr. H1 CFO/PAT 0.40x (INDETERMINATE-WITH-DIRECTION). Mexico JV carrying value nil; funded beyond equity, counterparty undisclosed. IPO capex 0.22% spent; plant due Oct-2027. Next: Q3 gross margin by 14-Feb-2027 (bull >=40%, bear <=36%). No thesis on record; no trigger fired; no Spear line. Run: runs/knack-q2fy27 (commit in hand-over note).
```

No pre-committed trigger fired: there is no thesis, tripwire or trigger on record for this name.

## Step 2. Page content (insert_content, position: end, sequential inserts)

Insert these repo files verbatim, in this order. Complete tables, never summaries. Escape `|` inside table cells as `\|` where Notion needs it. Split large files across sequential inserts.

1. `runs/knack-q2fy27/work/review_knack_q2fy27.md`: the full A4 merged review (loop 1), Sections A, B, C, the Questions-for-Management table (28 rows in 4A, 27 in the YAML list), monitorables, and the PLAIN-LANGUAGE BRIEF (summary narrative, sector, business model, competition, forward map, indicative forward table). The brief is part of the review and is saved with it.
2. A3 forensics tables, one per document, verbatim:
   - `runs/knack-q2fy27/work/forensics_results_knack_q2fy27.md` (covers the press release, results pp. 17-19)
   - `runs/knack-q2fy27/work/forensics_deck_knack_q2fy27.md`
   - `runs/knack-q2fy27/work/forensics_concall_knack_q2fy27.md`
3. A5 audit verdict: `runs/knack-q2fy27/work/audit_knack_q2fy27.md` (re-audit, COMPLETE; loop-0 audit at `audit_knack_q2fy27_loop0.md` for the record).
4. Optional: `runs/knack-q2fy27/operator-brief.md` (indicative FY27E / FY28E and forward PE; not a Role 1 valuation).

Header block to put above item 1:

```
Q2 FY27 MERGED QUARTERLY REVIEW (RESULTS + DECK + CONCALL ASR; press release = results Annexure B), Knack Packaging Ltd (KNACK, BSE 544814)
Run: /run-quarterly, 28-29 Oct 2026, runs/knack-q2fy27. Pre-thesis read: no prior Notion page, no Spear line.
Verdict: PROCEED WITH FLAGS. A5: COMPLETE after 1 correction loop.
Concall source is a machine transcript (faster-whisper small.en); every call number is management tier and unverified.
```

## Step 3. Downstream Signal Tracker candidates (payload only; review Step 5.5C)

Four candidate rows, Case B (create new). None is written. Each needs live verification first. KNACK has zero tracker signals, below the three-signal floor (OR-17).

| Candidate | Reason | Source status |
|---|---|---|
| India PP raffia/homopolymer list price (monthly) | Primary input; pass-through lag of 3 to 4.5 months (cc L278-287) | PENDING LIVE VERIFICATION |
| Container freight index, Asia to US/Europe (weekly/monthly) | Red Sea freight cited as a margin headwind (press L831-833) | PENDING LIVE VERIFICATION |
| Single animal-nutrition customer contract, ~Rs 150 Cr/yr (approximate), to Dec-2028 | About 18% of FY26 revenue; counterparty not named in filings | Counterparty identity not confirmed |
| Sayem Knack (Mexico JV) monthly sales tonnage vs 120-130 MT breakeven | JV is the fastest-growing P&L drag | Company disclosure only (ASR) |

## What this payload does not do

- It does not set Decision Status, Entry Price Max, Margin of Safety Price or Position Size.
- It does not write tracker rows. Step 3 lists candidates only.
- It does not run any valuation. Steps 6.5, 7 and 8D are deferred to /fttcp and Role 1 (OR-30).
