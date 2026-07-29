# CLAUDE.md — Inflection Alpha Pipeline

Equity research pipeline for Indian small/micro-cap GARP transition
analysis. Operator: Keerti Kaushik. Strategy: transition alpha, 25% CAGR
target, 3-5 year holds.

## NEVER
- Never use any exit PE from outside Section 1B v3.3 (frameworks/). It is
  the sole exit multiple authority. No round-number defaults, ever.
- Never halt a run on company quality. Flags propagate; only mechanical
  failures halt. There is no STOP verdict; the verdict set is PROCEED /
  PROCEED WITH CAVEATS / PROCEED WITH FLAGS / REWORK / INSUFFICIENT
  EVIDENCE.
- Never let INDETERMINATE cash conversion silently resolve to PROCEED.
  It caps at PROCEED WITH CAVEATS with the missing evidence named.
- Never treat low institutional ownership as a risk. UA multiplier per
  Amendment 3: min(Raw x 1.25, Sector Cap), all three qualifiers evidenced.
- Never conflate the Emerging Moat scan (stage 7) with FTTCP (inside
  stage 11). Separate analyses, separate names.
- Never estimate a missing number. NOT FOUND is the only valid fill.
- Never credit one quality improvement through two mechanisms.
- Never write X posts here. Publish candidates are flagged only.
- Never let a maker verify its own work. Verifiers get fresh contexts
  and artifact paths only.

## DISPATCH (model per subagent, already set in .claude/agents frontmatter)
- opus: stage 11 valuation, stage 13 synthesis, verifiers B and C
- sonnet: all document-reading stages (1-9), verifier D
- haiku: stage 10 assembly, verifier A
Do not upgrade a stage's model without editing its agent file.

## WORDS
- "done" for a stage = full report written AND valid YAML block emitted
- "anchored" = every number followed by (source, page/note)
- "flag" = surfaced prominently in the verdict, decision stays human

## MEMORY
/run-pipeline, /fttcp, /finalize, and /compost sessions read LESSONS.md at
start (it carries operational run history and is ~18k tokens; lighter sessions
that do not touch pipeline operations skip it to keep context lean). Every
/run-pipeline, /fttcp, and /finalize session appends one dated entry at close:
what broke or dragged this run, in one line each; write 'clean run' if nothing.
Never delete
entries; promotion to a prompt file gets noted under PROMOTED TO LAW.

Per-company memory lives in companies/<TICKER>.md, written or updated at
/finalize close and read as COMPANY MEMORY by /run-pipeline stage 0 and by
/fttcp. It carries the one-line thesis, Decision Status and entry zone,
operator rulings with dates, active tripwires, the optionality register
summary, and links to every run folder for the ticker. It is memory to
weigh, never anchored evidence.

## STRUCTURE
- prompts/       stage instructions, single source of truth
- frameworks/    Master v3.3, Section 1B v3.3, FTTCP v1.2 (Keerti
                 maintains; stage 11 reads at run time; amendments here
                 propagate with zero pipeline edits)
- runs/<ticker>-<date>/   one folder per run, see runs/_template
                 (inputs/_textcache/ holds stage-0 page-marked .txt per PDF
                 plus <ar>__INDEX.yaml; section-scoped stages read AR slices)
- companies/<TICKER>.md   durable per-company memory, written at /finalize,
                 read as COMPANY MEMORY by /run-pipeline stage 0 and /fttcp
- LESSONS.md     operational memory, read by pipeline commands at start,
                 appended at close
- .claude/agents/         subagent definitions with model routing
- /run-pipeline runs/<folder>   executes everything
- /run-quarterly TICKER --docs ...   quarterly review pipeline (Role 4/5):
                 five gated agents A1 extractor -> A2 enumerator -> A3
                 forensic notes -> A4 analyst -> A5 adversary; enumeration
                 before interpretation; writes runs/<ticker>-<quarter>/work/;
                 needs the two Quarterly_*_Protocol files in frameworks/

## STYLE (synthesis outputs only)
No em-dashes or en-dashes as punctuation. No hyphens in compound
modifiers except tickers/proper nouns. No AI vocabulary. Numbers first.
Symmetric bull-bear. No landing lines. Headline is 6-7 words.
