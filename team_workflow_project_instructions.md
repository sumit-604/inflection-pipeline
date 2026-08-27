CLAUDE WEB × CLAUDE CODE — TEAM WORKFLOW v2 FOR COMPANY ANALYSIS

Version 2, 26-Aug-2026. Supersedes v1. Written after the INDIAGLYCO cycle, which took seventeen operator hand-offs and five versions of one file to reach a verdict. The target for v2 is five hand-offs per company. Everything in v1 that is not changed below still applies.

Why v2 exists (the four leaks it plugs)

1. Claude web wrote the handover dossier before Claude Code's extraction answers existed, then patched it four times.
2. Claude web's extraction questions were standing questions that Claude Code could have answered at Halt 1 without any live-web input.
3. FTTCP scored one consolidated entity when the dossier declared three, and the run was discarded.
4. Small hygiene failures cost whole trips: missing commit hashes, page IDs referenced but not carried in the ferry text, edits scoped so narrowly that two sections of one file contradicted each other, and separate Notion approvals for routine note updates.

The five hand-offs (v2 sequence)

Hand-off 1 — Halt 1 with the Standing Extraction Annex (Claude Code → operator → Claude web). `/run-pipeline` delivers everything v1 delivered at Halt 1 PLUS the annex in Section 6 (below), already answered from corpus. The annex is not optional. A Halt 1 without a completed annex is INCOMPLETE and Claude web returns it.

Hand-off 2 — One dossier, written once (Claude web → operator → repo). Claude web runs the corpus verification gate, the mental-model stress test, the live-web research brief, the vertical work, source discovery, and the tracker writes, then writes `inputs/research/web-handover-dossier.md` ONCE, complete, including Section 6 Gate Pre-Rulings (below). No placeholder slots. If a fact is unavailable it is written as NOT DISCLOSED with the reason, not as a slot to fill later. The operator commits it. One commit, message `<ticker>: web handover dossier v1`.

Hand-off 3 — FTTCP per entity, one gate card per entity (Claude Code → operator). `/fttcp` reads the dossier's declared entity count. If the count is greater than one, it produces one Step 3 scorecard, one composite, one verdict and one P/E gate card PER ENTITY, and carries any consolidated figure only as a reconciliation line. Each gate card shows Claude Code's draft ruling and Claude web's pre-ruling from dossier Section 6 side by side, with both reasonings. The operator rules once, on that card.

Hand-off 4 — Operator ruling and verdict sentence (operator → Claude Code). The operator answers each gate card and gives the verdict sentence in her own words. Claude Code runs stages 14 and 15 and `/finalize`.

Hand-off 5 — Read and save (Claude web, no ferry). Claude web clones the run branch, reads the final files directly, saves to Notion under the approval tiers below, and runs the publication check. Nothing is pasted.

Anything beyond these five is a defect. When it happens, the reason goes into LESSONS_ARCHIVE.md as a one-line entry so the next cycle can remove it.

Section 6 of every Halt 1: the Standing Extraction Annex

Claude Code answers these ten questions from corpus, quote-then-comment, filename and page anchor on every number, NOT DISCLOSED where absent, before Halt 1 is delivered. They are the same ten for every company.

1. Units. For every per-unit figure the pipeline uses or derives (realisation per tonne, revenue per case, price per litre, ARPU), quote the printed figure with its unit exactly as printed, state whether it covers one product or a basket, and if no per-unit figure is printed say so and give the volume and revenue lines from which one can be derived.
2. Segment capital and debt. Segment assets, segment liabilities, capital employed and any borrowings allocated by segment, latest two periods. If borrowings are unallocated, say so and quote the total.
3. Guidance versus aspiration. Every forward number management has stated, classified as (a) guidance with a period, (b) aspiration without a period, (c) capacity or capability only. Quote each.
4. Concentration. Product, customer and geography concentration as disclosed; top product share and top customer share; NOT DISCLOSED if absent.
5. Promise ledger. Every tracked promise with date made, delivery status and evidence anchor, in a table.
6. Restated bases. Whether prior-period comparatives are restated for any reorganisation, transfer or reclassification; quote the note; quote the comparative as printed in the latest filing.
7. Corporate-action clauses. For any scheme, demerger, merger, preferential issue or buyback in the corpus: the definitions of any undertaking, the liability allocation clauses, the ratios, the appointed and effective dates. If the scheme is not in the corpus, say so and name the filing to fetch.
8. Related-party perimeter. Every promoter-group entity named in the AR's RPT note with the nature and amount of transactions, latest year.
9. Pledge and shareholding. Promoter pledge and holding for the last twelve quarters as filed; institutional holding latest.
10. Verification. The filename and date of every document quoted in the annex, and the corpus commit hash.

If a company throws up a question outside these ten, Claude web may add up to two extra prompts, but those travel inside the dossier's open-items section, not as a separate ferry.

Section 6 of every dossier: Gate Pre-Rulings

Claude web writes, for each entity, its draft answer to every operator gate the pipeline will raise, with reasoning: P/E base per pillar, cash multiplier band with structural/growth-induced call, growth premium and whether Amendment 16 opens, earnings basis, sector cap row, option inputs with reference frames, and any Amendment 17/18/19 treatment. Claude Code copies these onto the gate card beside its own draft. The operator sees both at once and rules once. Where operator ruling overrides both drafts, Claude Code records the override with the operator's stated reasoning and the sensitivity (what the number would have been on the default track).

Per-entity rule for FTTCP and Role 1

If the dossier declares more than one entity, or the corpus shows a demerger, spin-off or listing of a subsidiary inside the projection window, the pipeline scores and values PER ENTITY from the first pass. A consolidated pass is never the decision surface. Where standalone balance sheets do not yet exist, the operator may rule that allocation is carried as an ESTIMATE; every leverage-, cash- or ROCE-dependent cell then carries the tag [ESTIMATE, X1] and the affected stages re-run when the filed number arrives.

Ferry hygiene (both sides)

* Self-contained ferry blocks. Any text the operator carries between us contains everything needed to act on it: page IDs, file paths, hashes, exact replacement text. A reference to "the IDs above" or "my earlier message" is a defect.
* Hash by default. Every Claude Code report that involves a commit ends with the commit hash and `git log -1 --stat`. Claude web verifies against the repo; the operator never has to ask.
* Dependency alignment. When an edit changes a status, ruling or gate in one section, Claude Code aligns every dependent section (header status, supersessions, blocking list, open items) in the same commit, and lists what it aligned. "Keep everything not named" never produces a file that contradicts itself.
* Corrections stay visible. When a document overturns a Claude web inference, it is logged as Correction N in the dossier and in Notion Key Notes. Five happened on INDIAGLYCO. That is the system working.
* Documents uploaded to claude.ai are read there. Never ferried to Claude Code. Corpus documents are read by Claude Code. Each document is paid for once.

Notion approval tiers (Claude web)

* Standing approval (no gate): tracker row Notes and Last Observation updates, Signal Health changes, Key Notes prepends that record work done, page-body records of filings read, corrections.
* Explicit approval (operator says "write"): Decision Status, Entry Price Max, Margin of Safety Price, Position Size, creation of new COMPANIES MASTER rows, creation of new tracker rows, any deletion. Claude web batches everything under standing approval into one pass per session and reports what was written.

Calendar and repo memory

* Claude web adds record dates, listing dates, results dates and tracker check dates to the operator's Google Calendar when they become known, with the entry tests in the description.
* `companies/<TICKER>.md` carries one line per ruling, one proof line per Notion write, and the dossier commit hash. Claude web supplies these lines inside the same message as the work, never as a separate follow-up.

Gates the pipeline enforces (unchanged from v1, with two additions)

* Halt 1 gate: stage 09b dossier + Section 6 annex complete + operator signed mental model + PROCEED recorded.
* Role 5.5 tracker gate: tracker proof in companies file; minimum three EXTERNAL signals per entity (company-narrated rows do not count toward the floor; they may exist as internal telemetry).
* Handover input gate: dossier exists with Section 6 pre-rulings; absence = STOP.
* Entity-count gate (new): `/fttcp` and stage 11 refuse to run a single consolidated pass when the dossier declares more than one entity.
* P/E gate and Amendments 16-19: unchanged, but presented per entity with both drafts.
* Finalize gate (new): report includes hashes and `--stat` for every commit; missing = incomplete.

What we never do (v1 list, plus)

* Write a dossier with unfilled slots.
* Run a consolidated FTTCP on a multi-entity dossier.
* Ferry a block that references something outside itself.
* Report a commit without its hash.
* Ask the operator to approve a routine Notion note.

End of v2. Replace the project-knowledge copy of team_workflow_project_instructions.md with this file and ferry the implementation prompt to Claude Code.
