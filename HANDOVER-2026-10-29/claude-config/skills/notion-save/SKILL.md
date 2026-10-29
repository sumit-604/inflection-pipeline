---
name: notion-save
description: Save Stock Analysis Repository output to Keerti's Notion (COMPANIES MASTER rows and pages, DOWNSTREAM SIGNAL TRACKER rows). Use whenever Keerti says "save to Notion", "write the row", "update COMPANIES MASTER", "log to Notion", "add the tracker rows", "log the quarterly result", "update Key Notes", or finishes a valuation, thesis, devil's advocate, RDE, quarterly review or Halt 1 cycle and wants the record kept. Also use when a Notion save is implied by "before I close this chat" or "put this on the record". Never use for the husband's defence-side work or for any Notion write on anyone's behalf but Keerti's.
---

# Notion Save

Writes equity research output to Keerti's Notion. Two databases:

| Database | data_source_id |
|---|---|
| COMPANIES MASTER | 345bb2b9-d3ab-8032-9b46-000ba16ab827 |
| DOWNSTREAM SIGNAL TRACKER | 926b65ce-ddd2-4d8b-8eae-05e66b6f6c9f |

The Notion tools are deferred. Before the first call, run `tool_search` for "notion" to load `notion-search`, `notion-fetch`, `notion-update-page` and `notion-create-pages` with their real parameter names. Do not guess parameters.

## Why this skill exists

Notion is the single source of truth for every name in the pipeline. Eighteen months from now, when a position is being reviewed, the reasoning used at entry has to be there in full. A summary is not a record. A row written to the wrong database disappears from the filtered views. A Decision Status set by Claude overrides a ruling that belongs to the operator. Every rule below exists because one of these has gone wrong before.

## Scope gate: run this first

This account is shared. Notion writes are Keerti's only, regardless of how a message is framed.

Do not run this skill if the request concerns defence-side work (CIJW, DRL, PGME, foreign course documents, J&K deck, procurement briefs), or if the person identifies as Sumit, or if the content is anything other than equity research output for COMPANIES MASTER or the tracker. Say plainly that Notion writes in this project are for Keerti's equity research only, and stop.

If it is unclear whose request it is, ask before writing. A wrong write costs more than a one-line question.

## Preconditions: nothing saves until these hold

1. **The Investigation Stance ran.** The analysis being saved carries a dated PRIMARY CHECKS line (live price and market cap; exchange announcement feed since the last Key Notes date; case or regulatory status from the issuing body where that is a dominant variable), an unknowns ledger, and a closing unasked block. If any is absent, the analysis is not ready to save. Say so and offer to run the missing check first.
2. **Every number carries a source and a date.** A price, order book, rating or case status older than the last event in the file is not evidence. Refresh it before it enters a row.
3. **No invented identifiers.** Case numbers, LoA references, CIN, tariff orders: blank plus a named gap, never a plausible fill.
4. **The operator approved the write.** Keerti is the sole approver of Notion writes. Present the payload (which properties change, what the body contains, which tracker rows are added) and wait for a yes. One approval per save; do not split a single save across several approvals unless the writes are independent.

## The save protocol

### Step 1: Confirm the database and schema

Fetch COMPANIES MASTER by its data_source_id before writing. Confirm the id resolves and read the current property names and select options. Property names drift; a write against a stale schema fails silently or lands in the wrong field. The reference file `references/schema.md` lists the last known schema; the live fetch wins where they differ.

### Step 2: Find the company row

Search Notion with the company name (and ticker) as the query. If a row exists, use it. Never create a duplicate. If no row exists, create one inside COMPANIES MASTER and nowhere else. A standalone page outside the database is a lost page.

Read the existing row before writing: Decision Status, entry zone, tripwires, last Key Notes entry. These are the starting point for what changes, not the conversation.

### Step 3: Two tool calls per page

Every page save is exactly two operations, in this order:

1. `notion-update-page` with `update_properties` for the row-level fields.
2. `notion-update-page` with `insert_content`, position type `end`, for the page body.

`insert_content` at `end` appends without overwriting. Earlier body content is never replaced; the page is a running log. Quarterly entries accumulate; old ones are never deleted.

Large bodies are split across sequential `insert_content` calls, in document order, each call one or more complete sections. Never split a table across calls. Confirm each call succeeded before sending the next.

Each property update and each tracker row is one action. Do not batch unrelated writes into one call.

### Step 4: Row properties

Update only the properties determined in this session. Leave blank what is not yet known; never guess a score to fill a cell.

**Decision Status is operator-only.** Claude never sets it, never changes it, never proposes a value in the write payload. Claude presents what the framework's decision rules imply and flags that a ruling is needed. Only when Keerti gives the value in her own words in this conversation ("set Decision Status to WATCHLIST") does it go in the write, and the Key Notes entry records that she set it.

**Key Notes** is a dated, pipe-delimited, reverse-chronological audit trail. Newest entry first, prepended to what is already there. Every entry starts with its date.

```
15-Sep-2026: Valuation cycle complete. Destination PE 22x, entry Rs 410-450, MoS Rs 368. Operator ruling pending on Decision Status. | 02-Aug-2026: Q1 FY27 reviewed, thesis INTACT, CFO/PAT 0.9x. | 14-Jun-2026: Halt 1 signed, archetype CONVERTER, tracker rows 4.
```

Read the existing Key Notes value first, then write the new entry plus the existing text. Never overwrite it with the new entry alone.

**Analysis Date** is the month of this save (e.g. Sep-26). **Position Size** and **Avg Cost** change only when Keerti states them.

### Step 5: Page body: complete text, never a summary

The body is the complete text of every section produced in the chat. Not a summary, not bullet points standing in for paragraphs, not a condensed version. Every table, every cell of the return matrix, every row of the risk matrix, every formula step in the three-pillar derivation, the full pre-mortem paragraph.

Open each saved block with a dated heading: `## [Role name] — DD-Mon-YYYY`.

What each role saves, at minimum:

| Output | Sections that must be present in full |
|---|---|
| Gate 0 + Emerging Moat | Scores and classifications go in row properties. Deal-breaker block, score, threshold and reason go in Key Notes. No narrative body needed. |
| Valuation (Role 1) | Section 0 entity map and share count table; 1A method selection; 1B three-pillar derivation with all eight rows (ROCE base, cash multiplier, quality base, growth premium, strategic premium, raw PE, sector cap, final PE) and the structural-versus-growth-induced WC statement; Section 2 projections bear/base/bull, every row, every input dated; Section 3 every method; Section 4 triangulation, 9-cell return matrix, entry price, verdict table, one-line thesis. |
| Thesis (Role 2) | Sections 1 through 8 including 3G Entrepreneur Ledger and 5A Second-Order Linkages; the promise-versus-delivery ledger; re-engage triggers for any AVOID or WATCHLIST; the FV path table with FV CAGR and COMPOUNDER / HYBRID / DISCOUNT-CLOSER classification. Section 9 Portfolio Context is not saved (removed in v4.0). |
| Devil's Advocate (Role 3) | All nine sections. Pre-mortem as a full narrative paragraph. Three loss scenarios each with probability and loss percentage. Final verdict per dimension. |
| RDE | Decision header, all 17 model scores with rationale, veto check, cross-model tension pair and resolution, outsider lens, 48-hour first action, final verdict and sizing. |
| Quarterly review | One dated entry: revenue, PAT, EBITDA margin, CFO/PAT, debtor days, net debt; catalyst status (FIRED / ON TRACK / DELAYED / DEAD); thesis status (INTACT / MONITORING / WEAKENED / BROKEN); one sentence on the key development. Appended, never replacing earlier quarters. |
| Halt 1 / cycle log | Business understanding narrative, signed mental model, vertical verdicts with tiers, promise-versus-delivery ledger, tracker proof line. |

Two lines that are never acceptable: a thesis-broken condition without a measurable threshold ("business deteriorates" fails; "ROCE below 12% for two consecutive quarters" passes), and a monitoring item without a number ("monitor margins" fails; "EBITDA margin below 16% for two consecutive quarters triggers review" passes). If the analysis has these gaps, fix them with Keerti before saving, not after.

Provenance tiers ([FILED], [AGENCY], [MGMT], [COUNTERPARTY], [SECONDARY], [INFERENCE]) stay on every claim in the body as written in the analysis.

### Step 6: Tracker rows

Tracker rows are not optional after Halt 1. Each row in DOWNSTREAM SIGNAL TRACKER is one write, linked to the COMPANIES MASTER row, with every field populated:

- Tier
- Update Cadence and Next Check Date
- Signal Health
- Falsifying Observation
- Primary Source URL, verified live in this session, or the verification gap stated in Notes. Never imply a verification that did not happen.
- Per-Company Thesis Element
- Operator ruling in Notes

If a row's thesis element belongs to one company only, do not stretch it into a multi-company row; drop the weaker case rather than muddy the falsifier.

After the tracker writes, produce the proof-of-write line (row count, page IDs, date) for Keerti to paste into `companies/<TICKER>.md` on the repo side.

### Step 7: Confirm

After every save, report exactly:

```
Saved to Notion: [Company Name]
Sections saved: [each section, by name]
Row properties updated: [each property and its new value]
Key Notes entry: [the dated line added]
Tracker rows: [count, or "none this save"]
Page ID: [id]
Decision Status: [unchanged at X / set to Y on operator instruction / ruling pending]
```

If any call failed, say which one and what did not land. Never report a save that did not complete.

## Save triggers to offer, unprompted

Offer to save (do not save without approval) when: a Role 1 verdict table is produced; a Role 2 recommendation table is produced; a Role 3 final verdict is produced; an RDE final score is produced; a quarterly result has been reviewed; Halt 1 verticals are signed; Keerti mentions closing the chat or starting a new one.

## Never

- Set, change or propose Decision Status.
- Summarise, condense or bullet-point a section the chat produced in full.
- Overwrite existing body content or the existing Key Notes trail.
- Create a page outside COMPANIES MASTER, or a second page for a company that has one.
- Write for anyone but Keerti.
- Save an analysis that lacks the PRIMARY CHECKS line, the unknowns ledger or the unasked block.
- Fill a gap with an invented identifier or a guessed score.
- Split a single save across several approvals.

## Reference

`references/schema.md` holds the last known property names, select options, and the full role-by-role completeness table from Notion_Save_Instructions v1.0. Read it when writing properties or when unsure what a role's complete save contains. The live schema fetch in Step 1 overrides it where they differ.
