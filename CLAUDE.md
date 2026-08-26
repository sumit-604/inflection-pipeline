# CLAUDE.md — Inflection Alpha Pipeline

Equity research pipeline for Indian small/micro-cap GARP transition
analysis. Operator: Keerti Kaushik. Strategy: transition alpha, 25% CAGR
target, 3-5 year holds.

## NEVER
- Never use any exit PE from outside Section 1B (v3.3 base + v3.5.1 +
  v3.6 + v3.7 + v3.8 + v3.9 amendment layers in frameworks/; later layers
  govern overlaps). It is
  the sole exit multiple authority. No round-number defaults, ever.
- Never construct a Year-N exit price on a different earnings basis than
  the entry, and never carry a within-hold option slice into the exit as
  an unresolved probability (v3.8 Amendment 18).
- Never present an entry zone without the Amendment 19 FV CAGR and
  return-source classification; an entry discount is only interpretable
  against how fast fair value itself grows.
- Never produce a Role 1 valuation without the Section 1A Method
  Suitability Matrix and method triangulation; the Section 1B destination
  PE governs the exit multiple, it does not replace method selection.
- Never feed spot-year ROCE or rupee-denominated WC trends into Section
  1B or FTTCP for a CONVERTER-classified name (v3.7 Amendment 17).
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
- Never emit a final synthesis or Notion payload without the
  BUSINESS UNDERSTANDING NARRATIVE (five questions, prose, before the
  verdict card). A verdict without understanding is a shallow summary;
  the operator reads the narrative first.
- Never run /fttcp or any valuation on an unsigned Mental Model
  Declaration or a Halt 1 decision other than PROCEED.

## DISPATCH (model per subagent, already set in .claude/agents frontmatter)
- opus: stage 11 valuation, stage 13 synthesis, verifiers B and C
- sonnet: all document-reading stages (1-9), verifier D
- haiku: stage 10 assembly, verifier A
Do not upgrade a stage's model without editing its agent file.

## WORDS
- "done" for a stage = full report written AND valid YAML block emitted
- "anchored" = every number followed by (source, page/note)
- "flag" = surfaced prominently in the verdict, decision stays human

## SESSION DISCIPLINE (prompt cache)
- Model and effort are fixed at session start and never changed mid-session:
  switching either busts the prompt cache and re-prefills the whole
  conversation at full price. This governs the session's own model and is
  separate from subagent DISPATCH (each stage runs its own agent at its
  frontmatter model, which is not a mid-session switch). If a different
  session model is needed, start a fresh session.
- Run commands quiet by default so their output does not flood context on
  every use: git commit -q, git status --short, git log --oneline -n N
  (never a bare git log / git diff over a large range); pip install -q;
  apt-get install -y -qq; redirect verbose PDF-extraction output. The
  collect_to_repo.py collector runs on the operator's machine, out of
  session; in-session it appears only as collect_to_repo.py --push-again.
- Any session that commits a framework or prompt amendment must end by
  opening a PR to main the same day. Run outputs and framework amendments
  go in SEPARATE commits so recovery stays surgical.
- Framework/prompt amendments and run outputs travel on SEPARATE branches
  and PRs; an amendment never rides a run PR.

## MEMORY
/run-pipeline, /fttcp, /finalize, and /compost sessions read the ACTIVE
LESSONS.md at start (the lean working memory, hard budget under 1,500 tokens:
named failure catalogue, recurring patterns, promoted-to-law fixes, open
actions). Lighter sessions that do not touch pipeline operations skip it. The
full dated run history lives in LESSONS_ARCHIVE.md (never deleted), read only
by /compost and by humans. Every /run-pipeline, /fttcp, and /finalize session
appends one dated entry at close to LESSONS_ARCHIVE.md, NOT to the active
file: what broke or dragged this run, one line each; write 'clean run' if
nothing. LESSONS.md is orchestrator-session memory only; no stage or verifier
subagent receives it. When /compost promotes a pattern into the active
LESSONS.md, one old active lesson is reviewed for archiving so the token
budget holds; the promotion is noted under PROMOTED TO LAW.

Per-company memory lives in companies/<TICKER>.md, written or updated at
/finalize close and read as COMPANY MEMORY by /run-pipeline stage 0 and by
/fttcp. It carries the one-line thesis, Decision Status and entry zone,
operator rulings with dates, active tripwires, the optionality register
summary, and links to every run folder for the ticker. It is memory to
weigh, never anchored evidence.

## STRUCTURE
- prompts/       stage instructions, single source of truth
- frameworks/    Master v3.6, Section 1B layer set (v3.3/v3.5.1/v3.6/v3.7/v3.8/v3.9),
                 FTTCP v2.1, Quarterly v1.4, AR v1.3 (Keerti
                 maintains; stage 11 reads at run time; amendments here
                 propagate with zero pipeline edits), plus
                 Downstream_Source_Discovery_Protocol_v1_0.md (source
                 registry for downstream signal candidates; Role 5.5
                 verifies against it in claude.ai)
- runs/<ticker>-<date>/   one folder per run, see runs/_template
- companies/<TICKER>.md   durable per-company memory, written at /finalize,
                 read as COMPANY MEMORY by /run-pipeline stage 0 and /fttcp
- LESSONS.md     ACTIVE operational memory (lean, <1,500 tokens), read by
                 pipeline commands at start
- LESSONS_ARCHIVE.md   full dated run history (never deleted), appended at
                 close, read only by /compost and humans
- anti-ai-writing-style.md   house style for all reader facing prose
                 (synthesis narratives, recommendations, X posts); the
                 STYLE authority the orchestrator and stage 13 cite
- Narrative_Writing_Style_v1.md   STE (ASD-STE100 Simplified Technical
                 English) plus Zinsser; the operator voice authority cited
                 by OPERATOR VOICE below and by the closing narrative
                 section of every analysis
- .claude/agents/         subagent definitions with model routing
- /run-pipeline runs/<folder>   executes everything
- /run-quarterly TICKER --docs ...   quarterly review pipeline (Role 4/5):
                 five gated agents A1 extractor -> A2 enumerator -> A3
                 forensic notes -> A4 analyst -> A5 adversary; enumeration
                 before interpretation; writes runs/<ticker>-<quarter>/work/;
                 needs the two Quarterly_*_Protocol files in frameworks/

## PIPELINE SEQUENCE (operator-gated)
/run-pipeline (evidence, stages 0-9 + verifiers + 09b dossier) -> HALT 1:
operator reads the dossier, resolves corpus gaps, signs the Mental Model in
claude.ai, decides KILL / SHALLOW / PROCEED -> claude.ai: live
verification, verticals to depth, Role 5.5 tracker writes -> /fttcp
(deliberation) -> Role 1 valuation -> /finalize. Understanding precedes
deliberation. Deliberation precedes valuation. Nothing after Halt 1 runs on
an unsigned model.

## TEAM WORKFLOW — Claude Code and Claude web
Claude Code reads the heavy corpus once (PDFs, ARs, transcripts) and holds
the repo. It has NO live web access. Claude web (claude.ai) does live
verification, cross-checks, tracker and Notion writes. It must NOT re-read
corpus documents. It asks Claude Code via operator-ferried extraction
prompts (quote-then-comment, NOT DISCLOSED allowed, filename+date
verification mandatory). Filed documents beat inference. Every claim
carries its evidence tier. The pipeline produces payloads. claude.ai
executes writes. Each document is paid for once.
The claude.ai project carries a parallel operating manual at
project-instruction level (team_workflow_project_instructions);
web-side rules bind Claude web the same way this file binds Code.

## ARCHETYPE LIBRARY (mental model declarations draw from this; extend via operator ruling only)
- Build-to-spec component maker: customer capex cycle, design-win pipeline,
  content per unit, input-cost pass-through.
- Commodity converter (Section 1B v3.7 Amendment 17 binds): spread (output
  minus input price), utilisation, cycle position, cost-curve rank.
- Brand/franchise consumer: volume growth, pricing power, distribution
  reach, gross margin, advertising efficiency.
- Order-book business (EPC/defence/capital goods): order inflow,
  book-to-bill, execution pace, working capital, margin on backlog.
- Outsourcing partner (CDMO/EMS/IT services): client concentration, wallet
  share, capacity fill, contract stickiness, price per unit.
- Licence/scarcity business: licence or quota validity, renewal risk,
  regulated price, capacity cap, entry-barrier durability.
- Lender (framework variant exists): AUM growth, NIM, asset quality
  (GNPA and credit cost), RoA and RoE.
- Platform/network: active users, take rate, unit economics per
  transaction, network density, retention.

## OPERATOR VOICE (STE — all conversation, not only outputs)
Every reply to the operator uses Simplified Technical English (ASD-STE100,
codename STE) plus Zinsser. This governs ordinary chat, diagnosis, and
status updates, not only synthesis outputs. Full spec:
Narrative_Writing_Style_v1.md. The load-bearing rules, always on:
- One idea per sentence. 20 words or fewer. Split a long thought in two.
- Active voice. The subject does the action.
- One meaning per word per reply. Plain word over jargon. Gloss a term the
  first time it must appear.
- Cut every word that carries no information ("it is worth noting that",
  "in terms of", "at this point in time").
- No em-dashes or en-dashes as punctuation. Use a full stop, a comma, or
  restructure the sentence.
- No hedging filler (arguably, somewhat, essentially, fundamentally,
  significantly). No AI tells ("not just X but Y", participial openers like
  "Looking at...", empty -ly adverbs, robust/holistic/seamless,
  journey/landscape/ecosystem).
- Numbers first. Say the thing the simplest way that still says it.
Structured blocks keep their format. Tables, scorecards, Section 1B math,
FTTCP verdict cards, YAML, and Notion payloads are not prose. This rule is
silent on them.

## STYLE (synthesis outputs only)
No em-dashes or en-dashes as punctuation. No hyphens in compound
modifiers except tickers/proper nouns. No AI vocabulary. Numbers first.
Symmetric bull-bear. No landing lines. Headline is 6-7 words.
