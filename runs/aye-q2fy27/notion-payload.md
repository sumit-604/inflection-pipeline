# NOTION PAYLOAD: AYE Q2 FY27 quarterly review (NOT WRITTEN)

Status: NOT WRITTEN. Two gates block the write.
1. A5 verdict is INCOMPLETE after the one permitted correction loop (open item below). The orchestrator saves to Notion only after A5 COMPLETE.
2. Write gate (operator ruling 2026-10-03): the operator must approve this exact payload in-run. The operator was away; no approval was given.
Decision Status is never written by this pipeline.

## Target page
- Page: "Aye Finance Limited", COMPANIES MASTER
- URL: https://app.notion.com/p/3a6bb2b9d3ab81f18365f37559223a59
- Page ID: 3a6bb2b9-d3ab-81f1-8365-f37559223a59

## Call 1: update_properties (PREPEND to Key Notes, keep every prior entry)
Properties to change:
- "Key Notes": prepend the line below, then " \| " and the existing Key Notes text unchanged.
- "Analysis Date": 2026-10-23
- Do NOT touch "Decision Status" (stays HELD), "Entry Price Max", "Margin of Safety Price", "Position Size", "Current Market Price".

Key Notes line to prepend (exact text):

23-Oct-2026 Q2 FY27 quarterly review (/run-quarterly, results + deck + MACHINE ASR concall; official transcript not yet filed): PROCEED WITH FLAGS, HOLD 4% at Rs132 (branch 8A), Decision Status HELD unchanged, no thesis-broken trigger fired. A5 adversary INCOMPLETE after one correction loop (one bookkeeping item open, no figure or verdict affected). Headline: PAT Rs86.72 cr (+151% YoY, +16% QoQ); GNPA 4.20% (Q1 4.49%); PCR 62.42% (Q1 63.80%); CRAR 41.01%. Quality flags: DA gain Rs10.12 cr (Q1 nil) plus ECL stock fall Rs13 cr (287 to 274) exceed the QoQ PBT rise of Rs18.65 cr; H1 impairment 163.31 = write-offs 155.56 + settlements 8.30 - 0.55; total ECL cover 4.17% to 3.85%; Q2 write-offs+settlements ~Rs95 cr vs ~Rs69 cr Q1 [inference]. Add-gate FAILS (1 of 4 legs): (i) gross slippage undisclosed for the third event, pre-committed bear reading; (ii) PCR 62.42% passes; (iii) FY27 bands repeated verbatim, not refined; (iv) bank-lender unwaived covenant count not disclosed. NEW: auditor-qualified security-cover certificate, (PAR90+write-off)/GLP covenant breach on NCD INE501X07588 for a second quarter (waived), reason cites higher delinquencies this FY; ISIN redeems 17-Nov-2026. Leading indicators: Bucket 1 CE 52.8% (Q1 54.5%), UP Sep 47.6%, mortgage PAR X +1pp, disbursement +10% YoY, new-customer +23% vs repeat -16%. Mgmt now guides FY27 credit cost ~3.5% (needs H2 ~3.05% vs Q2 3.82%). CFO absent from all Q2 filing signatures; CTO replaced; Alpha Wave India left the >5% list. Notion GNPA history needs correcting: deck gives Sep-25 GNPA 4.84%. Single cleanest Q3 metric: credit cost with total ECL cover (bull <=3.3% with cover >=3.85%; bear >3.82% or cover <3.85%). CMP on file Rs162 (13-Oct) is stale. Operator rulings pending: second loop for A5 open item; 4 tracker candidates. Repo: runs/aye-q2fy27/work/review_aye_q2fy27.md (commit hash in the run report). Decision Status unchanged (operator-only).

## Call 2..N: insert_content, position end (split across sequential inserts; escape "|" in table cells as "\|")
Content, in this order, complete tables, never summaries:
1. Heading: "# Q2 FY27 Quarterly Review (2026-10-23): A5 INCOMPLETE after loop 1 (bookkeeping item open)"
2. The full A4 review: runs/aye-q2fy27/work/review_aye_q2fy27.md, lines 1-1152 (everything before the trailing YAML block), INCLUDING the PLAIN-LANGUAGE BRIEF (lines 1087-1151).
3. A3 forensics tables (completeness proof):
   - runs/aye-q2fy27/work/forensics_results_aye_q2fy27.md (F1-F17 status table and findings table)
   - runs/aye-q2fy27/work/forensics_presentation_aye_q2fy27.md (same)
   - runs/aye-q2fy27/work/forensics_concall_aye_q2fy27.md (same)
4. A5 audit verdict: runs/aye-q2fy27/work/audit_aye_q2fy27.md, the verdict line, the findings-by-type lists, and the full "RE-AUDIT AFTER LOOP 1" section.
5. Open item line: "A5 open item R1-1/R1-2: review preamble lines 33-34 count pre-loop ledgers (755 + M01-M05; 913); corrected ledgers hold results M01-M07 and presentation M01-M02. Results M07 (CS cover-letter signature 11:39:14, R:L1438) is an orphan row. Fix is a two-row table edit plus one 'reviewed, no finding' line; no figure, flag, verdict or position moves. Needs operator approval for a second loop (cap = one)."

## Optional: DOWNSTREAM SIGNAL TRACKER (payload only; operator rules first)
Data source: collection://926b65ce-ddd2-4d8b-8eae-05e66b6f6c9f. Affected Companies: https://app.notion.com/p/3a6bb2b9d3ab81f18365f37559223a59

Update existing row "AYE - Bucket 1 collection efficiency (quarterly)" (https://app.notion.com/p/3f8bb2b9d3ab81d6b493e2597f1a2049):
- Last Observation Value: "Bucket 1 CE 52.8% Q2 FY27 (Q1 54.5%); UP Sep 47.6% (lowest of nine months shown); Rajasthan Q2 avg 55.6% vs 59.9%; PAR X 6.94% (business update said 6.88%); GNPA 4.20% (business update said 4.30%) [FILED, results + deck 21-Oct-2026]. Mgmt: no identified cause; recovery 'post November', then 'December' [MGMT, ASR concall 22-Oct-2026]."
- Last Observation Date: 2026-10-21; Direction vs Prior: Falling; Signal Health: Threatens (unchanged). Next Check Date: 2027-01-08 (Q3 business update, estimated).
- Notes (prepend): "2026-10-23: secondary report of covenant breach CONFIRMED from the filing: auditor security-cover certificate qualified on INE501X07588 (PAR90+write-off)/GLP covenant, second quarter, waiver received."

Update existing row "AYE - Disbursement growth YoY vs AUM growth" (https://app.notion.com/p/3f8bb2b9d3ab81489a27d58bcf6a286b):
- Last Observation Value: "Q2 FY27 disbursement Rs1,403 cr +10% YoY; H1 Rs2,622 cr; new-customer disbursement +23% YoY, repeat -16% [MGMT, ASR]; AUM Rs7,597 cr +26% YoY [FILED 21-Oct-2026]. No new branches in H1; 30+ planned in Q3 [MGMT]."
- Last Observation Date: 2026-10-21; Direction vs Prior: Flat; Signal Health: Threatens (unchanged).

Candidate new rows (Case B, proposed by A4 Step 5.5C; create only on operator ruling):
1. AYE - Drought declarations MH/KA/MP (monthly; falsifier: Rest States Bucket 1 CE below 55.7% with drought districts widening)
2. AYE - Insurance-commission regulation (event-driven; FY28 fee headwind, size not disclosed)
3. AYE - Policy repo rate path (event-driven; ROA sensitivity 3 bps FY27 / 6 bps FY28 per mgmt)
4. AYE - Pre-IPO holders above 5% (quarterly shareholding; Alpha Wave India 7.8% at Jun left the list)
