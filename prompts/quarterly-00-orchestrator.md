# QUARTERLY ANALYSIS AGENT PIPELINE ORCHESTRATOR v1.0
## Five-agent extraction-first review of Reg 33 filings, concalls, presentations

This is the authority on sequence, gates, working files, and the Notion save
for `/run-quarterly`. It implements the Quarterly Analysis Agent Pipeline
master prompt (July 2026). This orchestrator governs EXTRACTION and
COMPLETENESS. The protocol files govern ANALYSIS. Where this orchestrator and
a protocol file conflict on analysis, the protocol file wins. Where they
conflict on extraction discipline, this orchestrator wins.

The pipeline exists because a casual text-layer read of SOUTHWEST Q1 FY27 on
20 July 2026 missed a zero-value "Profit on sale of share in subsidiary"
line, a widening standalone-vs-consolidated PAT gap resting on unaudited JV
numbers, a shell-subsidiary structure, an Annual Report approval buried in
Board Outcome agenda item 7, forward-commitment phrases inside Note 5, an
actuarial OCI swing, and a persistent deferred-tax shield. Every one was
recoverable with a structured `pdftotext + grep + sed` pass; none from a
casual read. The mechanism is not "read more carefully." The mechanism is
enumeration before interpretation.

---

## PIPELINE POSITION AND PROTOCOL AUTHORITY

This pipeline implements Role 4 (Quarterly Results Review Protocol v1.2) and
Role 5 (Quarterly Concall Analysis Protocol v1.1), and pre-processes investor
presentations for both. It feeds Role 4 and Role 5. It does NOT run
valuation. Enforced downstream sequence per protocol v1.2:
Gate 0 -> Role 4 (filing numbers) -> Role 5 (concall) -> FTTCP -> Role 1 ->
Role 2 -> Role 3 -> Notion save. This pipeline produces the Role 4 / Role 5
review that seeds that chain.

Required protocol files (the orchestrator checks these exist BEFORE any
analysis agent runs; absence is a hard STOP, never reconstruct from memory):
- `frameworks/Quarterly_Results_Review_Protocol_v1_2.md`
- `frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md`
- `frameworks/Master_Project_Prompt_v3.3.md` (framework context, already present)

All figures in Rs Crores. Filing units (Lakhs / Crores / Millions) are
detected and converted AT EXTRACTION, with the conversion factor stated in
the A1 extraction header.

---

## AGENT ARCHITECTURE

Five agents, strict sequence, hard gates between each. No agent begins until
the prior agent's gate passes. Every agent writes a named file to the run
folder's `work/` directory so the audit trail survives the session.

```
A1 EXTRACTOR -> A2 ENUMERATOR -> A3 FORENSIC NOTES -> A4 ANALYST -> A5 ADVERSARY
```

A1, A2, A3 run PER DOCUMENT. A4 runs ONCE, merging every document's extract,
ledger, and forensics into a single protocol-ordered review (Role 4 first,
Role 5 second, presentation findings feeding both). A5 audits A4 once.

---

## FAST PATH — STANDALONE CONCALL TRANSCRIPT (default for a lone concall)

When the run is a SINGLE conference-call transcript and nothing else — `--docs`
resolves to exactly one document, it classifies as `concall`, and no Reg 33
`results` filing or other new document is part of the same run — do NOT spawn
five separate agents. The A1-A2-A3-A4 separation buys little on one short
born-digital transcript, and five sequential Opus contexts (each re-reading the
protocol files, none able to parallelise across the gates) is the wrong cost for
the value. Use this collapsed path instead:

- The ORCHESTRATOR performs A1 + A2 + A3 + A4 itself, inline, and writes the
  SAME named `work/` artifacts (`extract_concall_...txt`, `ledger_concall_...md`,
  `forensics_concall_...md`, `review_..._q<n>fy<yy>.md`) so the audit trail is
  byte-for-byte what the full pipeline would produce. Every gate is still
  self-enforced and recorded: A1 100% coverage (verbatim save for a pasted/text
  transcript; `pdftotext` if it is a PDF), A2 the two-way count test on
  turns / questions / management-numbers, A3 every applicable forensic check
  (F6 forward-commitment mining, F7 hedge mining, F17 silence audit, plus
  F1/F8/F14 as applicable) with a line cite per FINDING, A4 the Role 5 review
  with the promise-vs-delivery register and the Questions-for-Management table.
- Then spawn EXACTLY ONE agent: A5 (quarterly-a5-adversary), fresh context,
  task message carrying ONLY the A4 review, the A1 extract, and the A2 ledger.
  This preserves the one separation that actually matters — a maker cannot grade
  its own work — and keeps the COMPLETE/INCOMPLETE gate (max two loops).
- Notion save, commit, and report are unchanged.

This fast path is ONLY for a lone concall. The moment a run includes a Reg 33
results filing, an investor presentation, OR more than one document, revert to
the full five-agent per-document chain below — the enumeration-before-
interpretation separation earns its cost on filings and multi-document merges.
A5's independence is never collapsed, on either path.

## DISPATCH (model per agent, set in .claude/agents frontmatter)
- sonnet: A1 extractor, A2 enumerator (mechanical, completeness-critical)
- opus:   A3 forensic notes, A4 analyst, A5 adversary
Do not upgrade an agent's model without editing its agent file. The extraction
agents are mechanical but total; the interpretation agents are Opus because a
miss here is the failure this pipeline exists to prevent.

---

## RUN FOLDER AND WORKING FILES

`/run-quarterly TICKER --docs results.pdf [concall.pdf] [presentation.pdf]`

The orchestrator resolves TICKER and creates (if absent):
```
runs/<ticker>-<quarter>/
  inputs/        source PDFs copied or referenced here
  work/          all agent working files (audit trail)
```
`<quarter>` is the detected filing quarter, lowercased and hyphenated, e.g.
`q1fy27`. If the quarter cannot be detected before A1 runs, use the run date
`<yyyy-mm-dd>` as a placeholder and rename after A1 reports the quarter.

Named working files (master-prompt filenames, one set per document):
- A1: `work/extract_<doctype>_<ticker>_<quarter>.txt` + header block
- A2: `work/ledger_<doctype>_<ticker>_<quarter>.md`
- A3: `work/forensics_<ticker>_<quarter>.md` (one per document, doctype in title)
- A4: `work/review_<ticker>_<quarter>.md` (single merged review)
- A5: `work/audit_<ticker>_<quarter>.md`

`<doctype>` is one of `results` | `concall` | `presentation`.

---

## DOCUMENT CLASS DETECTION (orchestrator does this per file)

Detect class per file from content, not filename:
- Reg 33 / "Unaudited Financial Results" / "Statement of ... Results" /
  Board Outcome markers -> `results`
- Speaker-turn structure (Moderator / analyst-firm / "Ladies and gentlemen") ->
  `concall`
- Slide structure (few words per page, page = slide, chart-heavy) ->
  `presentation`
If a file is ambiguous, read the first two pages and decide; record the
decision in the run log.

---

## TOOLCHAIN PRECHECK (orchestrator, at session start)

Extraction is mechanical and mandatory. Before A1, verify the toolchain:
`pdftotext`, `pdfinfo` (poppler-utils), and for OCR fallback `pdftoppm` and
`tesseract`. If any is missing, attempt install (`poppler-utils`,
`tesseract-ocr`). If install is not possible in this environment, STOP and
report the missing tool: the pipeline cannot run a trusted extraction without
it. Do NOT substitute the Read tool's PDF rendering for A1 — the line-numbered
`pdftotext -layout` output is the evidence spine every downstream citation
points at.

---

## SEQUENCE

If the run is a lone concall transcript, take the FAST PATH above instead of
this five-agent chain (orchestrator does A1-A4 inline, one A5 adversary). The
sequence below is the full pipeline for results filings and multi-document runs.

For EACH document (results, then concall, then presentation, in whatever
subset was supplied):

1. Invoke A1 (quarterly-a1-extractor) with the document path and its detected
   doctype. Collect its extract file and header.
   GATE A1: page coverage 100%. Any page unaccounted for = STOP, report the
   gap, do not proceed for that document.

2. Invoke A2 (quarterly-a2-enumerator) with the A1 extract path and doctype.
   Collect the ledger.
   GATE A2: the count test passes (grep count == manual sweep count for
   notes / turns / slides). A mismatch = STOP and re-invoke A2 once with the
   mismatch named; second mismatch escalates to the human.

3. Invoke A3 (quarterly-a3-forensics) with the A1 extract path, the A2 ledger
   path, and doctype. Collect the forensics file.
   GATE A3: every one of F1-F17 carries an explicit status (PASS / FINDING /
   N.A.) and every FINDING cites a line number. Any blank check = STOP and
   re-invoke A3 once naming the blank checks.

After all documents pass A1-A3:

4. Invoke A4 (quarterly-a4-analyst) ONCE with: every A1 extract path, every
   A2 ledger path, every A3 forensics path, the protocol file paths, and the
   live Notion thesis (the orchestrator fetches the company Notion page first
   per Step 0A and passes its Decision Status and monitoring checklist inline;
   subagents never call Notion themselves). A4 states the ledger-reconciliation
   preamble, runs Role 4 and/or Role 5 in full step sequence, and writes the
   merged review. Every A3 finding classified AMBIGUOUS or FORWARD-SIGNAL must
   produce at least one Questions-for-Management row.

5. Invoke A5 (quarterly-a5-adversary) with the A4 review path plus every A1
   extract and A2 ledger path (for its independent coverage and arithmetic
   re-run). Collect the audit.
   GATE A5: verdict COMPLETE. INCOMPLETE loops back to the named failing agent
   with the specific gap stated. Maximum two loops; a third failure escalates
   to the human with the unresolved gap stated plainly.

6. OPERATOR BRIEF (mandatory — the run is NOT complete without it). Produce the
   three-part plain-language brief per the OPERATOR BRIEF spec below. Write it as
   the executive header of `work/review_<ticker>_<quarter>.md` and show it in
   full in chat. This is the operator's primary deliverable: a run that ends
   without it has failed to deliver, however complete the analysis underneath.

7. NOTION SAVE (only after A5 COMPLETE). See below. Save the Operator Brief as a
   callout at the top of the appended review section.

8. COMMIT the run folder (`work/` files) with message
   "quarterly review: <ticker> <quarter>" and report to the user. The report
   LEADS with the full Operator Brief, then gives the A5 verdict, the
   count-reconciliation line (N notes / N turns / N slides, all reviewed), the
   top forensic findings, and the working-file paths.

---

## NOTION SAVE (after A5 COMPLETE only)

Per Role 4 Step 9 and existing save mechanics:
- Fetch the company page first.
- `insert_content` with `position: end` for the full review (complete tables,
  never summaries; the page is institutional memory). Split large content
  across sequential insert calls.
- `update_properties` to PREPEND the date-stamped Key Notes line to the
  pipe-delimited audit trail, preserving all prior entries.
- Escape pipe characters inside table cells as `\|`.
- Decision Status changes ONLY when a pre-committed trigger formally fires.
- Save the A3 forensics table and the A5 audit verdict alongside the review;
  the completeness proof is part of the record.

---

## OPERATOR BRIEF (mandatory closing deliverable — every run, both paths)

Every quarterly run ends with a plain-language brief written for the operator,
not the analyst. Without it the run has not delivered, no matter how complete
the tables are. It follows the house STYLE: no em-dashes or en-dashes as
punctuation, no hyphenated compound modifiers except tickers and proper nouns,
no AI vocabulary, numbers first, symmetric bull and bear, no landing lines.
Plain words a non-specialist reads once and understands. Three parts, in this
order and these lengths (line counts are firm, not approximate):

1. SUMMARY (10 to 12 lines). The whole analysis as a narrative: what the
   company reported this quarter, the verdict and why, the strongest positive
   and the strongest caveat, the cash and valuation stance, and the single
   thing to watch next quarter. No tables, no jargon, no line citations.

2. SECTOR AND COMPETITIVE INTELLIGENCE (6 to 7 lines). Where the industry is
   heading and how this company sits against its competitors, in plain
   language. Draw on the concall's industry commentary, the peer / TAM evidence
   in the run folder or companies/<TICKER>.md, and the Notion business context.
   Name the tailwinds and the threats symmetrically.

3. BUSINESS MODEL, WHAT IS UNIQUE (5 to 6 lines). A simple explanation of how
   the company actually makes money and what is genuinely unusual or hard to
   replicate about it. Draw on the business-model and moat evidence (stage-4 /
   stage-7 blocks or companies/<TICKER>.md if present) and the concall.

The orchestrator writes this INLINE. It already holds the merged review, every
extract, the Notion page (the "One line" and business sections), and any
company memory, so the brief needs no fresh document reads and costs almost
nothing. Do NOT spawn a separate agent for it unless the operator asks: a
separate agent would re-read everything to produce 25 lines. If an input is
genuinely thin this quarter (for example no peer data), say so in one honest
clause rather than padding to hit the line count.

## NON-NEGOTIABLE RULES

1. Enumeration before interpretation. No agent forms a view before the ledger
   exists and reconciles.
2. Line-number citation or it did not happen. Every finding, number, and quote
   carries its line number (or turn / slide number).
3. Zero-value lines are data. Never drop a nil row from an extraction table.
4. The text layer is not trusted for image-heavy pages. OCR fallback is
   mandatory when the per-page character test fails.
5. Standalone AND consolidated, always both. The gap is a first-class metric.
6. Auditor paragraphs are read verbatim and diffed against the prior quarter,
   never summarised from memory.
7. Board Outcome agenda items beyond item 1 are enumerated and assessed.
8. Every ambiguous or forward-signal finding becomes a management question.
9. Notion is fetched live before analysis; Decision Status is verified before
   any position framing.
10. Conservative bias on interpretation, zero bias on extraction.
11. Pipeline summaries never substitute for primary documents; on conflict the
    primary text wins and the contradiction is logged.
12. Lending businesses use the 1L/5L variants per protocol v1.2; the forensic
    checklist still runs in full (F4, F5, F12 especially).

## RULES FOR THE ORCHESTRATOR SESSION
- You coordinate; you do not analyse. Every finding comes from a subagent.
- Pass file PATHS to subagents, not pasted PDFs; fresh context is the point.
- A5's independence is absolute: its task message carries only the A4 review,
  the A1 extracts, and the A2 ledgers, never your commentary.
- Only mechanical failures (missing pages, count mismatch, blank checks,
  INCOMPLETE audit after two loops, missing protocol files) halt the run.
- If any required protocol file is absent, STOP and report; do not
  reconstruct protocols from memory.
