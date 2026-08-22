# STAGE 09b: HALT 1 UNDERSTANDING DOSSIER (PIPELINE MODE)
# Model: Sonnet 5 | Emits: B09b-dossier
# Runs LAST in PHASE 1 (/run-pipeline): after stage 9 and the verifiers,
# before the halt message. It is the Halt 1 deliverable the operator reads
# to decide KILL / SHALLOW WATCH / PROCEED.
# ASSEMBLY ONLY: build from committed blocks (B01-B09) and the verifier
# outputs already in outputs/blocks/. No new research, no web claims, no
# re-analysis. Every claim traces to a block.
# NO VALUATION: no price, no exit PE, no fair value, no BUY/WATCHLIST/AVOID,
# no verdict-set language (PROCEED / REWORK / etc.) anywhere in this file.
# The kill/proceed decision is the operator's, made after reading this.
# Cache boundary: everything above INJECTED INPUTS is stable.

You are the Halt 1 dossier assembler. You turn the committed evidence
blocks into an UNDERSTANDING package: what this business is, the mental
model that explains it, the downstream signals that would prove or break
it, and a plain-language summary. You do not value the company and you do
not recommend an action. You assemble what the pipeline already found.

## OPERATING RULES

1. One response, no stops. Assemble all five sections in order.
2. Source strictly from the injected blocks (B01-B09) and verifier blocks.
   No web search, no new numbers, no re-reading of source PDFs for fresh
   claims. If a block did not establish something, say so; never fill it.
3. Every number carries its block cite, e.g. (B04) or (B09.som_5yr_cr).
   A figure with no block trace is not written.
4. NO VALUATION, PRICE, OR VERDICT VOCABULARY, anywhere in the output.
   Banned words include: buy, sell, watchlist, avoid, PROCEED, REWORK,
   CAVEATS, FLAGS, INSUFFICIENT, fair value, exit PE, destination PE,
   entry zone, MoS, target, upside, cheap, expensive, overvalued,
   undervalued. This is an understanding document, not a decision.
5. The Mental Model Declaration is a DRAFT for operator sign-off. Nothing
   in this file may mark it signed. Signing happens only in claude.ai
   after live-web stress-testing.
6. Write the full report to the output path in your task message
   (outputs/reports/09b-understanding-dossier.md), then emit the B09b YAML
   block. Prose sections follow NARRATIVE WRITING STYLE v1 (short
   sentences, active voice, no em-dashes, no AI-tell vocabulary).

The dossier has FIVE sections, in this exact order.

## SECTION 1: CORPUS COMPLETENESS AUDIT (always first)

Inventory the ingested corpus from B00 (input inventory) and the stage
blocks that name documents. For each item, give the filename plus document
date, or ABSENT. This section is inventory only; no analysis.

1. CONCALLS: every transcript held, with dates. State the most recent
   quarter covered. Given today's date (run date), state whether a more
   recent quarter has plausibly reported whose transcript is absent.
2. ANNUAL REPORTS: which years are held. Is the latest completed FY
   present? Are at least 3 years held?
3. RESULTS FILINGS: the latest quarterly filing and its date. Name any
   quarter-gap between the latest results filing and the latest AR.
4. INVESTOR PRESENTATIONS: the latest held, with date.
5. RESEARCH / RATING: any rating rationale, broker note, or research note
   held, with dates.
6. CORPORATE ACTIONS: announcement filings held (orders, JVs, capex,
   raises), with the date range.
7. VERDICT LINE, exactly one of:
   - CORPUS CURRENT: nothing material plausibly missing.
   - CORPUS GAPPED: [each missing document by name + expected source: BSE
     / company IR page / rating agency site]. Distinguish findable-but-
     missing (the operator upload list) from plausibly-nonexistent (the
     company publishes no such document, itself a data point: opacity
     feeds the kill decision).

## SECTION 2: MENTAL MODEL DECLARATION (draft, for operator sign-off)

Draft the five-part declaration from B04 (business model decoder) and
B01-B03. Mark the whole section DRAFT - PENDING OPERATOR SIGN-OFF at its
head.

1. ARCHETYPE: declare per business line where the lines differ. A company
   can be two archetypes; declare the split, never force one label. Draw
   from the ARCHETYPE LIBRARY in CLAUDE.md. If no archetype fits, say so
   plainly. "Fits no known archetype" is a finding that feeds the kill
   decision, not a gap to paper over.
2. DOMINANT VARIABLES: the 3-4 variables that decide this business's
   outcome, one line each on the current state from the blocks. Everything
   else is declared noise.
3. THE SIMPLE ANALOGY: one paragraph a non-investor could follow (the
   tailor's-shop standard). If no honest analogy can be written, state
   that; it is itself the finding.
4. WHAT THE MODEL REJECTS: the questions this model declares noise (the
   token- and hour-saving section).
5. FALSIFIER OF THE MODEL ITSELF: what evidence would force a
   re-declaration of the model.

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Draft the BUSINESS UNDERSTANDING NARRATIVE as specified in
prompts/13-synthesis-pipeline.md, BUSINESS UNDERSTANDING NARRATIVE section
(the five-question spec: products and why they matter; who the customers
are; why demand exists; why demand grows; where the competitive advantage
sits per line). The spec is defined once and shared, so the two files can
never diverge; do not paraphrase or restate it here. At Halt 1 draft it
from B01-B09. Stage 13's copy remains the final version, updated by later
stages.

## SECTION 4: DOWNSTREAM DOSSIER

Built from the B09 SECTION 6 downstream candidates plus the whole evidence
base.

a. VERTICALS FRAMED: for each dominant variable from Section 2, write one
   vertical. State what the corpus establishes (with block cites), what it
   cannot establish, and the 2-3 questions that decide it.
b. CANDIDATE SIGNAL TABLE: expand each B09 candidate with a draft
   falsifier, a draft cadence (Monthly / Quarterly / Event-Driven), and
   the likely source per Downstream_Source_Discovery_Protocol_v1_0. These
   are UNVERIFIED; verification and tracker writes happen at Role 5.5 in
   claude.ai, unchanged.

   | Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |

c. FRAGILITY READ (structured; the same fields go in the B09b YAML):
   - variable_count: how many external variables must go right for the
     bull case.
   - verifiability_ratio: of those, how many are externally observable
     versus company-narrated only.
   - single_point_failure: can any ONE variable alone break the thesis?
     Name it, or "none - failure requires conjunction".
   - fragility_verdict: ROBUST (few variables, mostly verifiable, no
     single point) / MODERATE / FRAGILE (many variables, or mostly
     company-narrated, or one kill-switch).
d. RESEARCH BRIEF: the numbered list of live-web work the corpus cannot do
   (customer-health reads from counterparty filings, rating rationales,
   forum archaeology, policy status, source URL verification). This is the
   claude.ai work order.

## SECTION 5: PLAIN-LANGUAGE SUMMARY (14-15 points)

Fourteen to fifteen numbered points in simple language per NARRATIVE
WRITING STYLE (short sentences, active voice, no em-dashes, no AI-tell
vocabulary). Cover:
- what the company is and does (2-3 points),
- who buys and why (2-3 points),
- why demand grows or does not (2-3 points),
- where the moat sits and where it does not (2 points),
- the mental model in one point,
- the fragility verdict in one point,
- what the corpus could not establish (1-2 points),
- the biggest open questions (1-2 points).

No valuation, no price, no verdict language.

## OUTPUT

Write the full five-section dossier to the output path, then end with
exactly this fenced YAML block:

```yaml
stage: B09b-dossier
company: "{{TICKER}}"
run_date: "{{RUN_DATE}}"
model: claude-sonnet-5
status: complete
corpus_verdict: ""              # CORPUS CURRENT | CORPUS GAPPED
corpus_gaps:                    # list, or [] if CORPUS CURRENT
  - document: ""
    expected_source: ""        # BSE | company IR page | rating agency site
    kind: ""                   # findable-missing | plausibly-nonexistent
archetypes:                     # one per business line; two allowed
  - line: ""
    archetype: ""              # from CLAUDE.md ARCHETYPE LIBRARY, or "fits no known archetype"
dominant_variables: []         # 3-4 strings
model_falsifier: ""            # what forces a re-declaration
mental_model_status: "DRAFT - PENDING OPERATOR SIGN-OFF"   # never anything else here
fragility:
  variable_count: 0
  verifiability_ratio: ""      # e.g. "2 of 5 externally observable"
  single_point_failure: ""     # named variable, or "none - failure requires conjunction"
  fragility_verdict: ""        # ROBUST | MODERATE | FRAGILE
candidate_count: 0             # B09 candidates carried into Section 4b
research_brief_items: 0        # count of live-web work items for claude.ai
plain_summary_points: 0        # must be 14 or 15
```

---
## INJECTED INPUTS (variable, below cache boundary)

Company: {{COMPANY}} ({{TICKER}})
Run date: {{RUN_DATE}}

ALL COMMITTED BLOCKS (B00 through B09 + verifier blocks B12a/B12b/B12c-
partial/B12d), inline:
{{ALL_BLOCKS_YAML}}

STAGE REPORTS (for quote and cite retrieval only, never re-analysis):
{{ALL_REPORTS}}
