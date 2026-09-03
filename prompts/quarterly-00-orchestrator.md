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

This pipeline implements Role 4 (Quarterly Results Review Protocol v1.4) and
Role 5 (Quarterly Concall Analysis Protocol v1.1), and pre-processes investor
presentations for both. It feeds Role 4 and Role 5. It does NOT run
valuation. Enforced downstream sequence per protocol v1.4:
Gate 0 -> Role 4 (filing numbers) -> Role 5 (concall) -> FTTCP -> Role 1 ->
Role 2 -> Role 3 -> Notion save. This pipeline produces the Role 4 / Role 5
review that seeds that chain.

Required protocol files (the orchestrator checks the one(s) THIS run needs
exist BEFORE any analysis agent runs; absence is a hard STOP, never reconstruct
from memory):
- `frameworks/Document_Review_Protocol_v1_1.md` (a DOCUMENT REVIEW: standalone
  presentation / press release / one-off disclosure; A4's ONLY protocol for
  such a run, and the analyst-stage token discipline lives here)
- `frameworks/Quarterly_Results_Review_Protocol_v1_4.md` (a results filing)
- `frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md` (a concall)
- `frameworks/Master_Project_Prompt_v3_6.md` (framework context by reference;
  NOT an A4 input — the analyst never loads it)

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
  extracted/     A1 output: fulltext + structured extraction (the evidence spine)
  work/          all agent working files (audit trail)
```
`<quarter>` is the detected filing quarter, lowercased and hyphenated, e.g.
`q1fy27`. If the quarter cannot be detected before A1 runs, use the run date
`<yyyy-mm-dd>` as a placeholder and rename after A1 reports the quarter.

Named working files (one set per document; `<doctype>` disambiguates a
multi-document run):
- A1: `extracted/<ticker>-<doctype>-<quarter>-fulltext.md` (header block first)
      + `extracted/<ticker>-<doctype>-<quarter>-structured.md`
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
`pdftotext`, `pdfinfo`, `pdffonts` (poppler-utils; `pdffonts` is A1's
text-layer gate), and for the scan-OCR fallback `pdftoppm` and `tesseract`. If
any is missing, attempt install (`poppler-utils`,
`tesseract-ocr`). If install is not possible in this environment, STOP and
report the missing tool: the pipeline cannot run a trusted extraction without
it. Do NOT substitute the Read tool's PDF rendering for A1 — the line-numbered
`pdftotext -layout` output is the evidence spine every downstream citation
points at.

---

## SEQUENCE

For EACH document (results, then concall, then presentation, in whatever
subset was supplied):

1. Invoke A1 (quarterly-a1-extractor) with the document path, its detected
   doctype, and BOTH output paths (fulltext + structured). A1 runs the
   text-layer gate (pdffonts) first: a document with a text layer is extracted
   text-only, never rasterised for sparse pages; only a no-text-layer scan
   triggers whole-document rendering, logged. Collect the fulltext, the
   structured file, and the header.
   GATE A1: page coverage 100%. Any page unaccounted for = STOP, report the
   gap, do not proceed for that document. A1 is the ONLY agent that reads the
   source document; no later agent receives the source path.

2. Invoke A2 (quarterly-a2-enumerator) with the A1 STRUCTURED path and doctype
   (the fulltext path is passed only as a count-test fallback). A2 enumerates
   from the structured file and is the cheapest agent in the chain. Collect the
   ledger.
   DE-DUP: the ledger references A1's structured rows BY ID and adds only A2's
   classification, flags, and cross-refs; it never re-copies the claim text. No
   row is dropped: every structured row ID is accounted for in the ledger.
   GATE A2: the count test passes (structured-file count == A2's independent
   sweep) AND the ID accountability line shows zero orphan IDs (every structured
   row ID referenced). A mismatch or a non-empty orphan set = STOP and re-invoke
   A2 once with it named; second failure escalates to the human.
   COST CHECK: A2's token count must come in BELOW A1's. If A2 exceeds A1,
   something is re-ingesting the document; STOP and diagnose before A3.

3. Invoke A3 (quarterly-a3-forensics) with the A1 structured path, the A1
   fulltext path (for verbatim quotes at cited lines), the A2 ledger path, and
   doctype. Collect the forensics file.
   GATE A3: every one of F1-F17 carries an explicit status (PASS / FINDING /
   N.A.) and every FINDING cites a line number. Any blank check = STOP and
   re-invoke A3 once naming the blank checks.

After all documents pass A1-A3:

4. Invoke A4 (quarterly-a4-analyst) ONCE with: every A1 structured path, every
   A1 fulltext path (verbatim reads only), every A2 ledger path, every A3
   forensics path, the PROTOCOL FOR THIS RUN (doctype-conditional, below), and
   the live Notion thesis (the orchestrator fetches the company Notion page
   first per Step 0A and passes its Decision Status and monitoring checklist
   inline; subagents never call Notion themselves). A4 states the
   ledger-reconciliation preamble, runs the protocol in full step sequence, and
   writes the merged review. Every A3 finding classified AMBIGUOUS or
   FORWARD-SIGNAL must produce at least one Questions-for-Management row.

   PROTOCOL SCOPING (the analyst-stage token discipline). Pass ONLY the protocol
   this run needs; never pass the Master Project Prompt, FTTCP, the Section 1B
   layer set, or the RDE manual to A4.
   - DOCUMENT REVIEW (a standalone presentation / press release / one-off
     disclosure, no results filing and no concall in --docs): pass ONLY
     frameworks/Document_Review_Protocol_v1_1.md. Do NOT pass Role 4, Role 5, or
     Master.
   - FULL QUARTER (a results filing and/or concall in --docs): pass Role 4 for
     the filing and/or Role 5 for the concall, as before. Master is framework
     context by reference, not an A4 input.
   NOTION vs SPEAR. If a live Notion thesis exists, pass it inline (thesis
   check). If none exists, pass the Spear Pass template instead and tell A4 to
   frame the output as a PRE-THESIS READ, not a thesis check.

   SIGNAL CONTEXT input note: if the operator supplies tracker rows for this
   ticker (from the DOWNSTREAM SIGNAL TRACKER), pass them to A4 as SIGNAL
   CONTEXT for the Step 5.5 reconciliation per
   Quarterly_Results_Review_Protocol_v1_4. If absent, A4 states "tracker rows
   not supplied" in the Step 5.5 output rather than skipping the section
   silently.

5. Invoke A5 (quarterly-a5-adversary) with the A4 review path plus every A1
   fulltext, every A1 structured path, and every A2 ledger path (its
   independent coverage re-run greps the FULLTEXT, the spine, so it cross-checks
   that A1 dropped nothing into the structured file). Collect the audit.
   GATE A5: verdict COMPLETE.
   LOOP TRIGGER (Point 8): a loop fires ONLY on an A5 finding tagged FACTUAL,
   MISSING, or CONTRADICTION. STYLE findings are logged in the audit and carried
   into the report, but they NEVER re-run an agent. An A5 whose only findings are
   STYLE is treated as COMPLETE-with-style-notes and proceeds to save.
   LOOP CAP (Point 9): the correction loop runs at most ONE full iteration by
   default (the named agent fixes, A4 re-merges if needed, A5 re-audits once).
   If A5 is still INCOMPLETE after that one iteration, STOP and ask the operator
   before a second iteration; never loop a second time on your own.
   LOOP COST: log the loop separately. Record, in the run's session-cost.md, the
   loop iteration count and its token cost as its own line, so correction cost is
   visible over time and never buried in the base run figure.

6. NOTION SAVE (only after A5 COMPLETE). See below.

6b. SESSION COST (Point 10; every document review). Write `session-cost.md` in
   the run folder with a per-agent token ledger (one row per subagent run: agent,
   model, total_tok, wall, run#) AND, at the top, a one-line DOCUMENT REVIEW
   summary row for the shared baseline:
   `ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations`
   where `a1_extracted_text_tok` is A1's fulltext token count (the document's own
   size, the comparison anchor) and `total_run_tok` sums every agent plus any
   loop. Log the correction loop as its OWN ledger rows and count its iterations
   in `loop_iterations`, so base run cost and correction cost stay separable.
   This row is the document-review baseline, the same discipline the main
   pipeline ledger keeps.

7. COMMIT the run folder (`work/` files) with message
   "quarterly review: <ticker> <quarter>" and report to the user the A5
   verdict, the count-reconciliation line (N notes / N turns / N slides, all
   reviewed), the top forensic findings, and the working-file paths. ALSO
   surface the A4 PLAIN-LANGUAGE BRIEF in the chat report every run (the
   summary narrative plus the sector, business-model, and competition
   intelligence) — it is a standing part of the deliverable, not something the
   user has to ask for.

---

## NOTION SAVE (after A5 COMPLETE only)

Perform the Notion save INLINE in this orchestrator session. Do NOT delegate it
to a subagent (Sonnet or otherwise): the save is a mechanical
`insert_content` / `update_properties` sequence, and a subagent only adds
latency and hand-off risk with no benefit. Call the Notion tools directly.

Per Role 4 Step 9 and existing save mechanics:
- Fetch the company page first.
- `insert_content` with `position: end` for the full review (complete tables,
  never summaries; the page is institutional memory). The full review now ends
  with the A4 PLAIN-LANGUAGE BRIEF (summary narrative + sector +
  business-model + competition intelligence); it is part of the review and is
  saved with it, every run — never drop it and never treat it as optional.
  Split large content across sequential insert calls.
- `update_properties` to PREPEND the date-stamped Key Notes line to the
  pipe-delimited audit trail, preserving all prior entries.
- Escape pipe characters inside table cells as `\|`.
- Decision Status changes ONLY when a pre-committed trigger formally fires.
- Save the A3 forensics table and the A5 audit verdict alongside the review;
  the completeness proof is part of the record.

---

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
12. Lending businesses use the 1L/5L variants per protocol v1.4; the forensic
    checklist still runs in full (F4, F5, F12 especially).

## RULES FOR THE ORCHESTRATOR SESSION
- You coordinate; you do not analyse. Every finding comes from a subagent.
- Pass file PATHS to subagents, not pasted PDFs; fresh context is the point.
- INPUT DISCIPLINE (extract once, downstream reads the extraction). A1 is the
  ONLY agent that reads the source document. A2 through A5 receive ONLY: A1's
  structured extraction (and, where a verbatim read or an independent coverage
  re-run needs it, A1's fulltext), the outputs of prior agents, their protocol,
  and inline Notion. NEVER put a source path (anything under `inputs/`) in an
  A2-A5 task message. If any A2-A5 subagent reports it read or needed a file
  under `inputs/` or the source document, that is a discipline breach: log it
  in the run log with the agent and the file, and treat the run's token figure
  as compromised. A2's cost must land below A1's; a downstream agent above A1
  is the signature of source re-ingestion, so halt and diagnose.
- ROW-ID DE-DUP (each claim lives once). A1 gives every structured row a stable
  ID (R###). A2 references rows by ID and adds only its own classification and
  flags; A3-A5 read the claim in the structured file at that ID. No claim text
  is copied twice across the working files. COMPLETENESS GATE: every A1 row ID
  must be referenced by at least one of A2-A5. An orphaned ID (in the structured
  file, cited by none) fails the run and is reported.
- analyst_note handoff (bounded prose). Every agent's YAML block carries an
  `analyst_note` field, <=200 words, strict cap. Reasoning that a downstream
  stage cannot reconstruct from the structured fields travels there; everything
  else stays structured. It keeps free prose from leaking into the tables and
  inflating the handoff.
- A5's independence is absolute: its task message carries only the A4 review,
  the A1 extracts, and the A2 ledgers, never your commentary.
- Only mechanical failures (missing pages, count mismatch, blank checks,
  INCOMPLETE audit after two loops, missing protocol files) halt the run.
- If any required protocol file is absent, STOP and report; do not
  reconstruct protocols from memory.
