# DOCUMENT REVIEW PROTOCOL v1.1
## The lean analytical protocol for a standalone document review (A4)

Version: 1.1
Maintainer: Keerti (frameworks are operator-maintained; this file follows the
same amendment discipline as the rest of frameworks/).

This is the protocol A4 loads for a DOCUMENT REVIEW: a single standalone
document (a corporate / investor presentation, a press release, a one-off
disclosure) read on its own, not as part of a full results-filing or concall
quarter. It exists so A4 does not carry the full framework to read one deck. It
codifies the document-review steps A4 performs; it invents no new analysis.

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

## CROSS-REFERENCES (the A1-A3 artifacts this protocol reads)
These are the named inputs the steps below cite. Definitions so the protocol
reads standalone.
- A3 F2 — STANDALONE-vs-CONSOLIDATED DECOMPOSITION (quarterly forensic check
  F2): the S-vs-C gap on revenue, EBITDA components, and PAT for every period
  shown, decomposed into JV/associate share, subsidiary contribution, and
  eliminations, with the gap trended across periods.
- A3 F6 — FORWARD-COMMITMENT PHRASE MINING (quarterly forensic check F6): every
  dated or dateable management commitment mined from the document ("expected
  by", "commissioning", "will be completed", "is underway"), each with the
  commitment, its implied date, and the source line.
- A1 FORWARD rows — the FORWARD-typed rows in A1's structured extraction: every
  forward-looking statement (guidance, target, planned capex, monetisation
  plan, dated commitment), each with its page/line anchor and stable row ID.
- A3 F16 — DROPPED AND REFRAMED DISCLOSURES (used by the Silence Audit): metrics
  shown in a prior deck and absent now, changed chart baselines, softened
  guidance, changed order-book definitions.

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
5. CASH-QUALITY NOTE.
   a. No cash-flow statement AND no balance sheet: cash conversion is
      INDETERMINATE; the verdict caps at PROCEED WITH CAVEATS with the missing
      evidence named.
   b. A balance sheet is present but NO cash-flow statement: do NOT stop at
      INDETERMINATE. Compute from the balance sheet, across the periods shown:
      net debt (total borrowings minus cash and current investments); the
      working-capital-days trend (inventory + receivable days minus payable
      days); and inventory growth and receivables growth versus revenue growth.
      If working-capital days are widening, or inventory or receivables are
      outgrowing revenue, name the direction. Classify cash conversion
      INDETERMINATE-WITH-DIRECTION (deteriorating / improving), state the
      direction and the balance-sheet lines it rests on, and cap the verdict at
      PROCEED WITH CAVEATS.
   Never let INDETERMINATE or INDETERMINATE-WITH-DIRECTION resolve silently to
   PROCEED.
6. THESIS / SPEAR RECONCILIATION. Reconcile the document against the passed
   Notion Decision Status (thesis check) or the Spear load-bearing facts
   (pre-thesis read). Verify Decision Status before any position framing.
7. FORWARD-TARGET REGISTER. Every dated or dateable management commitment and
   target the document carries (from A3 F6 and the A1 FORWARD rows), each with
   its implied date, for the promise-vs-delivery tracker and the catalyst
   timeline.
8. QUESTIONS FOR MANAGEMENT. EVERY A3 finding classified FORWARD-SIGNAL or
   AMBIGUOUS generates at least one question. A finding that produces no question
   and no monitoring item has not been processed.
9. MONITORABLES / CATALYST LIST, seeded by the A3 commitment register (F6) and
   any forward items, each with its implied date.
10. SILENCE AUDIT (run before the brief). Name what a document of THIS type
    would normally carry that this one omits. For an investor / results
    presentation: a cash-flow statement, segment revenue and margin, per-share
    EPS, a net-debt reconciliation, the prior-period comparative on a changed
    metric, the order-book executed-vs-pending split, related-party detail. For
    a press release: the financial table behind the headline and the auditor's
    review status. List each omission and mark it ROUTINE or a SILENCE SIGNAL. A
    metric shown last period and dropped now is a silence signal: cross-
    reference A3 F16. Sustained silence on a deteriorating metric is a
    confirmatory negative, not a neutral gap.
11. PLAIN-LANGUAGE BRIEF (MANDATORY every run; the final narrative section).
    Four labelled parts: (1) SUMMARY NARRATIVE, (2) SECTOR INTELLIGENCE,
    (3) BUSINESS-MODEL INTELLIGENCE, (4) COMPETITION INTELLIGENCE.
    - STYLE. The SUMMARY NARRATIVE follows Narrative_Writing_Style_v1.md (STE
      plus Zinsser: short sentences, active voice, numbers first, no AI tells)
      and the Dhruva-Research output style. Length is the house standard: 200 to
      400 words (Narrative_Writing_Style_v1.md Section 6), not a line count.
    - PROVENANCE. Label every figure with the house five-tier evidence system,
      never a two-way prior-vs-this-document split:
      FILED (audited or exchange-filed financials, Reg 30/33 disclosures) |
      AGENCY (rating agency or regulator: CRISIL / ICRA / CARE / SEBI) |
      MGMT (management claim: presentation narrative, concall, AR commentary,
      guidance) | SECONDARY (industry association or sector-focused independent
      research) | INFERENCE (analyst inference from data patterns or sector
      logic). Defaults for a presentation: narrative claims default MGMT, the
      financial-statement tables default FILED, forward targets default MGMT.
      Override a default only with a source that earns a higher tier. Name any
      metric the document did not disclose.

## LOOP BEHAVIOR (the correction loop; A4 on a loop iteration)
A5 returns findings tagged FACTUAL / MISSING / CONTRADICTION / STYLE. Only
FACTUAL, MISSING, and CONTRADICTION reach A4; STYLE findings are logged and do
not loop. On a loop pass A4:
- addresses EACH FACTUAL / MISSING / CONTRADICTION finding EXPLICITLY, naming the
  finding id, the change made, and the line or row it lands on;
- cites the change so the re-audit can trace it;
- does NOT re-run steps A5 did not challenge — those carry forward unchanged.
The review is regenerated whole so it stays self-contained, but the loop edit is
surgical: every change traces to a named A5 finding, and nothing unchallenged is
reworked.

## VERDICT SET (the process verdict; canonical per CLAUDE.md and Master v3.6)
PROCEED / PROCEED WITH CAVEATS / PROCEED WITH FLAGS / REWORK / INSUFFICIENT
EVIDENCE. No STOP verdict. Company quality never halts; only a mechanical
failure does. This is the PROCESS verdict on the review's soundness. It is NOT
the investment Decision Status (BUY / WATCHLIST / INSUFFICIENT CONVICTION /
AVOID), which the human sets downstream. A document review flags; the human
decides. Decision Status changes only when a pre-committed trigger formally
fires.

## OUT OF SCOPE (named by reference only, never loaded or computed here)
Section 1B destination PE, the exit multiple, FV CAGR / Amendment 19 entry-zone
work, the FTTCP verdict, and Role 1 valuation. A document review that finds a
valuation-relevant fact FLAGS it for the downstream chain and stops there.

## CHANGELOG
- v1.1 — Step 10 provenance switched from a two-way prior-vs-document label to
  the house five-tier system (FILED / AGENCY / MGMT / SECONDARY / INFERENCE)
  with presentation defaults; the brief now cites Narrative_Writing_Style_v1.md
  and the Dhruva-Research output style and adopts the 200-400 word house length.
  Added the CROSS-REFERENCES section (A3 F2, A3 F6, A1 FORWARD, A3 F16). Step 5
  extended: a balance sheet without a cash-flow statement yields
  INDETERMINATE-WITH-DIRECTION (net debt, WC-days trend, inventory/receivables
  vs revenue growth, direction named). Added a SILENCE AUDIT step before the
  brief. Added a LOOP BEHAVIOR section. Confirmed the process verdict set
  against the canonical list and distinguished it from the Decision Status
  recommendation set. Dropped the DRAFT marker; added version and changelog.
- v1.0 — Genesis. Extracted the document-review analytical steps from A4 into a
  lean protocol so the analyst stage stops loading the full framework for a
  single standalone document (document-review token-discipline fix).
