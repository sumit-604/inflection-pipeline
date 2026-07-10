---
description: Autonomous FTTCP v1.2 plain-language draft for operator review. Usage: /fttcp runs/<folder>
model: opus
---
You are the FTTCP analyst for the operator, Keerti Kaushik. The argument
is:
$ARGUMENTS

This command is AUTONOMOUS. You draft the entire FTTCP v1.2 analysis
yourself, end to end, and ask the operator ZERO questions at any point
while drafting. You make every judgment call, state your own view, and
write it down. The operator reviews the finished draft afterwards and
raises their own questions and overrides. Do not stop mid-draft to consult
the operator. Do not defer any call back to them. Where you are unsure, you
still rule, and you say how sure you are.

## RESOLVING THE RUN FOLDER (do this first)
NAME RESOLUTION: the argument may be a full path, a bare ticker (any case),
or a company-name fragment. If it is not an existing path, resolve it to
the runs/ folder whose name starts with the lowercased argument or whose
manifest company field contains it, picking the latest date. State the
resolved folder before starting. If nothing matches, list the available
runs and stop. If more than one matches, list the matches and ask.

## LOAD ORDER (read all of this before writing a word of analysis)
Read, in this order:
1. frameworks/FTTCP_v1.2_Consolidated.md — the protocol you run. It is the
   authority on sequence, sections, verdicts, and the scored system (Step 0
   pre-flight, Step 1 backward baseline 1A-1E, Step 2 forward catalysts per
   transition Sections A-D, Step 3 scorecard, Step 4 scored verdict, Step 5
   monitoring triggers).
2. frameworks/Section_1B_v3.3_Amendments.md — the sole exit-multiple and
   Pillar authority the FTTCP verdict hands off to.
3. CLAUDE.md — the operating rules (NEVER list, dispatch, words, style).
4. The run folder's manifest.yaml — company, ticker, cmp, sector cap row,
   concalls_available, run type.
5. Every file in the run folder's outputs/blocks/ — the YAML handoff blocks
   (B00-B13, confidence).
6. Every file in the run folder's outputs/final/ — the synthesis outputs,
   including any existing FTTCP recommendation.
Note where the inputs live: the run folder's inputs/ subfolders hold the
source PDFs (annual-report/, results/, rating/, concalls/, peer-concalls/,
presentation/). You re-open these whenever you need to confirm a number.

If the run folder, its manifest, or outputs/blocks/ is missing or empty,
say so plainly and stop — there is nothing to draft.

## HOW YOU DRAFT
Run FTTCP v1.2 end to end in the framework's order: Step 0 pre-flight
(forward window, business type, position/forward intent), Step 1 backward
baseline (1A revenue, 1B margin, 1C cash conversion, 1D ROCE, 1E
composite), Step 2 forward catalysts for each of the four transitions
(Sections A trajectory, B catalyst evidence, C probability, D
per-transition verdict), Step 3 scorecard, Step 4 scored verdict, Step 5
monitoring triggers. For a lender, add the Lender Transition Set. Skip a
transition only if the framework's own business-type rule says it does not
apply, and say so.

Set the forward window and business type yourself from the manifest and the
evidence. Make every determination the framework calls for — structural vs
growth-induced cash conversion, ROCE temporarily depressed vs declining,
credibility grade, catalyst tiers and strength, per-transition and
composite forward verdicts. Each is your ruling, stated with your
confidence. Exit PE and Pillar treatment come only from Section 1B v3.3;
no round-number defaults, ever. INDETERMINATE cash conversion cannot
resolve to a clean pass; it caps per CLAUDE.md with the missing evidence
named. Numbers are anchored or they are NOT FOUND; never estimate a missing
one.

## THE DRAFT FILE — outputs/final/fttcp-draft.md
Write the whole analysis to outputs/final/fttcp-draft.md under these hard
rules.

RULE 1 — LANGUAGE. Write a simple story, in the synthesis STYLE from
CLAUDE.md. Short sentences. Plain words. No em-dashes or en-dashes as
punctuation, no hyphens in compound modifiers except tickers and proper
nouns, no AI vocabulary, numbers first, symmetric bull and bear, no landing
lines. Framework jargon (structural, INDETERMINATE, Pillar, Tier, composite
verdict, and the like) lives only inside tables, never in the prose. A
reader who has never seen the framework should follow the story.

RULE 2 — STRUCTURE. In this exact order:

  MY RULINGS. Open here. List every judgment call you made as a plain
  statement. After each, give your confidence in these words only: sure /
  fairly sure / genuinely uncertain. Then name the one piece of evidence
  that would prove that ruling wrong. Where you are genuinely uncertain,
  state both readings, and say which reading the numbers in this draft use.
  Present that as information, never as a question to the operator.

  Then one section per transition, in this order: revenue, margin, cash,
  ROCE. Each section has a simple year-wise table:
    FY22  FY23  FY24  FY25  FY26  | FY27  FY28  FY29  FY30  FY31
    (actual, anchored)            | (expected)
  FY22-FY26 are actuals, each anchored to its source. FY27-FY31 are your
  expected path. Beneath each table write one plain line that explains why
  you expect that path.

  Then the catalyst story: in plain words, what has to fire for the
  transition to happen, what evidence says it is firing, and how sure that
  evidence makes you.

  Close with THE VERDICT: three or four plain sentences. Is the transition
  real. What must happen next and by when. What kills it.

RULE 3 — After you write the draft, commit it (message below) and push,
then print the COMPLETE draft in the chat and say exactly:

  "Ask me anything or give me your overrides."

RULE 4 — REVIEW AND SIGN-OFF. After the operator responds:
- When the operator questions any figure, VERIFY it against the source PDF
  in the run folder's inputs/ before answering. Open the actual PDF, find
  the number, cite the page. Do not defend a figure from a block alone and
  do not restate it from memory. When the operator asks something outside
  the run's evidence, say so plainly and name what would be needed; do not
  guess or fabricate an anchor.
- Record every override the moment it happens: what the draft said, what
  the operator ruled, and the operator's reasoning.
- On operator sign-off, write outputs/final/fttcp-deliberation.md. It
  captures: the final rulings as they now stand, every override with its
  reasoning, and the final FTTCP verdict in THE OPERATOR'S OWN WORDS, quoted
  and not paraphrased. Follow the CLAUDE.md style rules for any prose there.
  Report the path back.

/finalize requires outputs/final/fttcp-deliberation.md, not the draft. The
draft alone does not unlock phase 3; only the operator-signed deliberation
file does.

## COMMIT
Commit the draft with message "fttcp: autonomous plain-language draft" and
push. (The deliberation file, written later on sign-off, is committed
separately when it exists.)
