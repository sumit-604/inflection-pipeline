# DOCUMENT REVIEW PROTOCOL v1.0
## The lean analytical protocol for a standalone document review (A4)

This is the protocol A4 loads for a DOCUMENT REVIEW: a single standalone
document (a corporate / investor presentation, a press release, a one-off
disclosure) read on its own, not as part of a full results-filing or concall
quarter. It exists so A4 does not carry the full framework to read one deck.

DRAFT for operator maintenance. It codifies the document-review steps A4
already performs; it invents no new analysis. Keerti maintains frameworks; this
file is versioned for the same amendment discipline.

## WHAT THIS PROTOCOL DOES NOT LOAD (the token discipline)
A document review does NOT need and MUST NOT load: the Master Project Prompt,
FTTCP, the Section 1B layer set, the full RDE / Annual Report manual, the
Quarterly Concall Analysis Protocol (Role 5, no transcript here), or the
Quarterly Results Review Protocol (Role 4) in full. Those govern valuation and
full-filing review, which run downstream. A document review feeds them; it does
not run them. The Section 1B destination PE, the FTTCP verdict, and Role 1
valuation are OUT OF SCOPE for this pass and are named only by reference.

## AUTHORITY AND SCOPE
The extraction-discipline authority is the quarterly orchestrator (enumeration
before interpretation, line-number citation, standalone AND consolidated,
zero-value lines are data). This protocol governs only how A4 turns the A1-A3
artifacts into a document-review write-up. Where a number needs a valuation
verdict, this pass FLAGS it for the downstream chain; it never sets a price.

## PRE-THESIS vs THESIS-CHECK FRAMING (set this first)
- If a live Notion thesis exists for the company (Decision Status, entry zone,
  tripwires, monitoring checklist, fetched fresh by the orchestrator), frame the
  review as a THESIS CHECK: reconcile the document against the thesis and verify
  the Decision Status before any HOLD/ADD/TRIM/EXIT framing.
- If NO Notion thesis exists yet, the orchestrator passes the SPEAR PASS
  template instead. Frame the output as a PRE-THESIS READ: what the document
  says about POND / CATCH / PRICE and whether it argues for a spear pass, NOT a
  thesis check. State plainly "no Notion thesis; pre-thesis read."

## THE STEPS (run in order, over the A1-A3 artifacts)
1. LEDGER RECONCILIATION PREAMBLE. State: "Ledger contains N disclosure units
   (slides / claims). All N reviewed. A3 findings incorporated: [ids]." If any
   row is unreviewed, stop and return the unreviewed rows.
2. EXTRACTION TABLES. Every headline metric the document carries, each cell a
   line-anchored number or the literal ND. Never estimate. Standalone AND
   consolidated wherever both appear; the gap is a first-class metric.
3. YoY / QoQ WALKS where the document gives the periods; the PAT bridge if the
   financials are present.
4. STANDALONE-vs-CONSOLIDATED GAP (from A3 F2) as a first-class metric: trend,
   decomposition (JV/associate, subsidiary, eliminations), direction.
5. CASH-QUALITY NOTE. A presentation rarely carries a cash-flow statement; when
   it does not, cash conversion is INDETERMINATE and the verdict caps at
   PROCEED WITH CAVEATS with the missing evidence named. Never let INDETERMINATE
   resolve silently to PROCEED.
6. THESIS / SPEAR RECONCILIATION. Reconcile the document against the passed
   Notion Decision Status (thesis check) or the Spear load-bearing facts
   (pre-thesis read). Verify Decision Status before any position framing.
7. FORWARD-TARGET REGISTER. Every dated or dateable management commitment and
   target the document carries (from A3 F6 / the A1 FORWARD rows), each with its
   implied date, for the promise-vs-delivery tracker and the catalyst timeline.
8. QUESTIONS FOR MANAGEMENT. EVERY A3 finding classified FORWARD-SIGNAL or
   AMBIGUOUS generates at least one question. A finding that produces no question
   and no monitoring item has not been processed.
9. MONITORABLES / CATALYST LIST, seeded by the A3 commitment register (F6) and
   any forward items, each with its implied date.
10. PLAIN-LANGUAGE BRIEF (MANDATORY every run; the final narrative section):
    (1) SUMMARY NARRATIVE (10-20 lines, plain, numbers first, no jargon, no AI
    vocabulary), (2) SECTOR INTELLIGENCE, (3) BUSINESS-MODEL INTELLIGENCE,
    (4) COMPETITION INTELLIGENCE. Provenance-label every figure: prior Notion /
    peer work vs this document's own content; name any metric the document did
    not disclose.

## VERDICT SET (unchanged from house rules)
PROCEED / PROCEED WITH CAVEATS / PROCEED WITH FLAGS / REWORK / INSUFFICIENT
EVIDENCE. No STOP verdict. Company quality never halts. Decision Status changes
only when a pre-committed trigger formally fires: flag, the human decides.

## OUT OF SCOPE (named by reference only, never loaded or computed here)
Section 1B destination PE, the exit multiple, FV CAGR / Amendment 19 entry-zone
work, the FTTCP verdict, and Role 1 valuation. A document review that finds a
valuation-relevant fact FLAGS it for the downstream chain and stops there.
