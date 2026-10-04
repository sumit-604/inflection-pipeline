# CLAUDE.md — Inflection Alpha Pipeline

Equity research pipeline for Indian small/micro-cap GARP transition
analysis. Operator: Keerti Kaushik. Strategy: transition alpha, 25% CAGR
target, 3-5 year holds.

## NEVER
- Never use any exit PE from outside Section 1B (v3.3 base + v3.5.1 +
  v3.6 + v3.7 + v3.8 + v3.9 + v3.10 amendment layers in frameworks/; later
  layers govern overlaps). It is the sole exit multiple authority. No
  round-number defaults, ever. There is no numeric ceiling but the sector
  cap; "never above 20x" language is void (v3.10 Amendment 26.5).
- Never anchor a base case to the audited past (v3.10 Amendment 26). Base
  revenue runs off the 26.1 basis hierarchy, with historical CAGR shown as
  the cross-check and used as the base only when no forward evidence
  exists. Base margin runs off the 26.2 destination-mix bridge; the
  trailing 3-year average is the BEAR input, except for margin-reset names,
  where the bear margin comes from the evidence bridge (operator ruling
  OR-11, approved 2026-09-28). Weights key to the trailing
  four quarters of Role 5 delivery, never whole-company history.
- Never shade an input to be safe. State the most evidenced path, name the
  two readings and the one observation that separates them, and put the
  conservatism in position size (v3.10 Amendment 26.3; v3.9 Amendment 25
  sets size as the margin of safety for fast-growth names; OR-31). This binds Role 1
  projections; it does not touch the document-reading protocols, where
  conservative interpretation of filed evidence still stands.
- Never construct a Year-N exit price on a different earnings basis than
  the entry, and never carry a within-hold option slice into the exit as
  an unresolved probability (v3.8 Amendment 18).
- Never present an entry zone without the Amendment 19 FV CAGR and
  return-source classification; an entry discount is only interpretable
  against how fast fair value itself grows.
- Never deliver a Role 2, Role 6, or FTTCP output without the
  Second-Order Section (Master v3.7 Rule F). Five linkage chains minimum,
  each with a labelled [INFERENCE]. A chain with no inference is a
  summary. Live-web links this container cannot reach are marked PENDING
  LIVE VERIFICATION and named, never fabricated.
- Never run Role 3 against a bull case that was not built to depth
  (Master v3.7 Rule H). Confirm the forward basis, the margin bridge, five
  chains, and a filled Entrepreneur Ledger first. If one is missing, STOP
  and return to Role 2. A devil's advocate against a thin bull is void.
- Never treat building as a footnote to governance (Master v3.7 Rule G).
  Role 2 Section 3G ledgers what the promoter built, raised, deployed, and
  delivered under constraint, and states its Pillar 3 line. The ledger
  never lifts a cap set by a promoter AVOID or an INTEGRITY concern; for a
  STRUCTURE concern, three of four evidenced ledger heads size as TRUSTWORTHY,
  with each concern a named tripwire (operator ruling OR-14).
- Never answer a failure-catalogue pattern-match without the nearest
  success name and the observable difference (Master v3.7 Rule I). While
  frameworks/success_catalogue.md holds fewer than four names, say
  "success catalogue pending" and continue.
- Never be a cheerleader, and never be a coroner (Master v3.7 Rule J). A
  bull claim and a bear claim carry the identical bar: tier the evidence,
  trace the chain, name the confirming observation. Depth is the default;
  if the operator has to say "go deeper", the output failed.
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
- claude-opus-5-5 (Opus 5.5), effort xhigh: stage 11 valuation, stage 15
  devil's advocate, verifiers B and C, quarterly A5, and the /fttcp session
  (start that session on Opus 5.5 at xhigh; the command pins no model)
- claude-opus-5-5 (Opus 5.5), effort high: stage 13 synthesis, stage 14
  thesis, quarterly A3-A4
- claude-sonnet-5-5 (Sonnet 5.5), effort medium: stages 1, 4, 6, 09b,
  10 assembly, verifier D, quarterly A2; effort high (set in the file):
  verifier A; effort low: quarterly A1; default (high): stages 2, 3, 5,
  7, 8, 9
- No stage runs on Haiku 4.5 (operator ruling 2026-10-04: stage 10 and
  verifier A moved to Sonnet 5.5; Verifier A's independence comes from a
  fresh context and the source page, not the model family)
Do not upgrade a stage's model without editing its agent file.
The model and effort in .claude/agents/*.md frontmatter are the operator's
rulings. A session never overrides them on the belief that the file is stale.
If the file looks stale, run the stale-checkout guard instead.

## OPERATOR RULINGS (dated; Section 1B rulings live in .claude/skills/section-1b/SKILL.md)
Standing pipeline rulings:
- Standing ruling 2026-10-04 (forward application): framework rulings apply
  to names analysed from the ruling date forward. Closed names are not
  re-derived under a new ruling; their record stands as of the run that
  produced it.
October 2026 audit, ruled 2026-10-04 (audits/RULINGS_2026-10.md item numbers):
- OR-15 (item 36): /finalize Rule H loop. A stage 15 steelman-gate miss
  re-runs stage 14 once, then stage 15; a second miss marks Role 3 VOID,
  flagged, and the run continues.
- OR-16 (item 39): /fttcp override sensitivity shows the number on each
  draft (Claude Code's and the dossier pre-ruling), not the more
  conservative one.
- OR-17 (item 40): /fttcp Role 5.5 gate needs three EXTERNAL tracker signals
  per entity. A dated "Tracker floor: OVERRIDE YYYY-MM-DD (operator,
  reason)" line in companies/<TICKER>.md lets it proceed below the floor;
  the gate names the shortfall either way.
- OR-18 (item 46): AR protocol margin of safety follows the Master evidence
  scale (20/30/40%), or position size for fast-growth names (A25).
- OR-19 (item 47): AR protocol Going Concern and FIRED thesis-broken
  conditions carry to the IMMEDIATE EXIT overlay; the review completes.
- OR-23 (item 52): Master Conviction Test. Stage 15 states the 3x exposure
  as % of portfolio (capital base NOT FOUND unless supplied) and hands the
  imagined-state questions to the operator.
- OR-24 (item 54): quarterly-cadence downstream signals feed the 12-month
  window (FTTCP governs; the Master's 6-12 month text is aligned).
- OR-26 (item 59): Quarterly Results conservative bias binds the reading
  of filed evidence (Steps 0-6); Steps 6.5-7 follow A26.3 / A25.
- OR-29 (items 66, 78): REWORK fires on a CONFIRMED Verifier A CRITICAL or
  an acceptance rate below 60% on a denominator of 4 or more.
- OR-30 (items 81, 82): /run-quarterly A4 defers Role 4 Steps 6.5/7 and
  Role 5 Step 8D to /fttcp and Role 1 and flags pillar-relevant facts.

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
  Exception: /step1 runs it with --dry-run on the operator's desktop.
- Sparse checkout (operator ruling 2026-10-03): a pipeline session first runs
  tools/sparse_session.sh runs/<folder> [more folders]. It keeps everything
  outside runs/, runs/_template/, every run's session-cost.md and
  manifest.yaml, and the named run folders, so the tree is about 80 MB, not
  4.8 GB. Add a folder the same way when a session needs it;
  tools/sparse_session.sh --off restores the full tree. Never run git stash or
  git reset --hard over a full checkout.
- Run tools/dry_check.sh before merging any PR that touches .claude/,
  prompts/, frameworks/ or tools/ (operator ruling 2026-10-03).
- Stale-checkout guard (operator ruling 2026-10-04): /run-pipeline, /step1,
  /fttcp, /finalize and /run-quarterly start with `git fetch origin main` and
  `git diff --quiet origin/main -- .claude/ prompts/ frameworks/ CLAUDE.md LESSONS.md`.
  A non-empty diff or a failed fetch stops the command before it reads any
  framework file. The session-start hook syncs only on the web, so on a local
  checkout this guard is the only check.
- Any session that commits a framework or prompt amendment must end by
  opening a PR to main the same day. Run outputs and framework amendments
  go in SEPARATE commits so recovery stays surgical.
- Framework/prompt amendments and run outputs travel on SEPARATE branches
  and PRs; an amendment never rides a run PR.
- Any PR that changes frameworks/, .claude/skills/section-1b/ or an operator
  ruling also updates claude-web/PROJECT_INSTRUCTIONS.md (the claude.ai
  project instructions), or says in the PR description why not.

## FERRY AND COMMIT HYGIENE (both sides; team workflow v2)
- Hash by default. Every report a command produces that involves a commit
  ends with the commit hash and `git log -1 --stat`. Claude web verifies
  against the repo; the operator never has to ask. A commit reported without
  its hash is incomplete.
- Dependency alignment. When an edit changes a status, ruling, or gate in one
  section, align every dependent section (header status, supersessions,
  blocking list, open items) in the SAME commit, and list what you aligned.
  "Keep everything not named" never produces a file that contradicts itself.
- Self-contained ferry blocks. Any text the operator carries between Claude
  Code and Claude web contains everything needed to act on it: page IDs, file
  paths, hashes, exact replacement text. A reference to "the IDs above" or "my
  earlier message" is a defect.
- Each document is paid for once. Corpus documents are read by Claude Code;
  documents uploaded to claude.ai are read there. Neither ferries a document
  to the other.
- Every run ends with session-cost.md (see run-pipeline close-out). It travels
  with run outputs, never on the framework branch.
- Deferred work is recorded. A commit message or PR description that says
  "open action", "left for later" or "recorded as" needs a matching line in
  LESSONS.md or LESSONS_ARCHIVE.md: the commit itself changes one of those
  files, or a line names the commit's 8-character hash or the PR as "#N".
  The session-start hook runs .claude/hooks/lessons-phrase-check.py over
  commits and PRs since 2026-09-15 and reports any item without a match.
  It reports; it never blocks a session.

## MEMORY
/run-pipeline, /fttcp, /finalize, and /compost sessions read the ACTIVE
LESSONS.md at start (the lean working memory, hard budget under 1,500 tokens:
named failure catalogue, recurring patterns, promoted-to-law fixes, open
actions). Lighter sessions that do not touch pipeline operations skip it. The
full dated run history lives in LESSONS_ARCHIVE.md (never deleted), read only
by /compost and by humans. Every /run-pipeline, /fttcp, and /finalize session
appends one dated entry at close to LESSONS_ARCHIVE.md, NOT to the active
file: what broke or dragged this run, one line each; write 'clean run' if
nothing. /finalize writes that entry in the fixed table of its step 8c and
adds a LESSONS.md OPEN ACTIONS line only for rows still OPEN. LESSONS.md is
orchestrator-session memory only; no stage or verifier
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
- frameworks/    Master v3.7 (file Master_Project_Prompt_v3_6.md; the path
                 is stable, the version is in the banner), Section 1B layer set
                 (v3.3/v3.5.1/v3.6/v3.7/v3.8/v3.9/v3.10),
                 FTTCP v2.3, Quarterly v1.4, AR v1.3, plus
                 success_catalogue.md (Rule I; operator fills, 0 of 4
                 names, not yet enforced) (Keerti
                 maintains; stage 11 reads the section-1b skill, so an
                 amendment here reaches stage 11 only when the matching
                 .claude/skills/section-1b/references chunk is regenerated
                 in the same commit), plus
                 Downstream_Source_Discovery_Protocol_v1_0.md (source
                 registry for downstream signal candidates; Role 5.5
                 verifies against it in claude.ai)
- claude-web/PROJECT_INSTRUCTIONS.md   repo copy of the claude.ai project
                 instructions (v4.1); the operator pastes it into the
                 project settings and keeps the two in sync
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

## SPEAR GATE (spear before shield; operator ruling 28-Aug-2026)
The framework grew shield-first: verify everything, then value. Inverted by
operator ruling. A SPEAR PASS runs FIRST, on live web, by Claude web, before
any pipeline machinery. Heavy pipeline runs only on a SPEAR HIT or an explicit
operator override. The spear hands the pipeline its priority verification
targets, the load-bearing facts. Claude Code does not run the four-step
spear below. Operator ruling 2026-09-05: the /step1 intake, run by Claude
Code with live web and grounded in the corpus it collects, replaces the web
spear. It writes "Spear: OVERRIDE <date> (operator standing ruling
2026-09-05: Step-1 intake replaces the web spear)", which satisfies the gate.

The four steps:
- POND. Live-web opportunity size in numbers. How large is the market the
  business fishes in.
- CATCH. A 3-year careful/fair/dream revenue and profit guess, anchored to
  observed conversion evidence, never to hope.
- PRICE. Per-share scenario values, probability weighting, and the entry price
  that clears the 25% CAGR target.
- VERDICT. HIT / WATCH / MISS against CMP.

Gate rule. /run-pipeline and /fttcp on a new name require a line in
companies/<TICKER>.md, above the Mental Model block, in one of two forms:
- Spear: HIT YYYY-MM-DD - entry <= Rs X - load-bearing facts: [2-4 items]
- Spear: OVERRIDE YYYY-MM-DD (operator)
If neither line exists, STOP. Direct the operator to run /step1, or the spear
pass with Claude web, first. The pipeline never runs a new name shield-first.

The load-bearing facts named in the Spear line are the run's FIRST
verification priority. Stage 0 carries them; every later stage checks them
before its own work.

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
the repo. Its live web is limited to WebSearch and WebFetch in /step1 and
stages 8 and 9; a failed search marks the stage partial, and nothing is
filled from memory. Claude web (claude.ai) does live
verification, cross-checks, tracker and Notion writes. It must NOT re-read
corpus documents. It asks Claude Code via operator-ferried extraction
prompts (quote-then-comment, NOT DISCLOSED allowed, filename+date
verification mandatory). Filed documents beat inference. Every claim
carries its evidence tier. The pipeline produces payloads. One approved
exception (operator ruling 2026-10-03): /run-quarterly writes Notion
in-session, only after the operator approves the printed payload in that
run, and never writes Decision Status. Otherwise claude.ai
executes writes. Each document is paid for once.
The claude.ai project carries a parallel operating manual at
project-instruction level (team_workflow_project_instructions);
web-side rules bind Claude web the same way this file binds Code. The repo
keeps the current text of that manual at team_workflow_project_instructions.md
(v2, five hand-offs: standing extraction annex at Halt 1, per-entity FTTCP and
Role 1, gate pre-rulings, hash-and-ferry hygiene). The repo copy and the
claude.ai project copy are kept in sync by the operator.

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

## QUALITY LADDER (mental model Part B1 names two endpoints on this; adjust via operator ruling only)
The transition thesis is a climb up this ladder. Part B1 of the Mental Model
Declaration names the tier the business LEAVES (FROM) and the tier it CLAIMS
to reach (TO), per line where lines transition differently. Rungs run low to
high. Each rung is defined by pricing power and by ROCE durability, not by
size. A business can sit between rungs; "fits no rung" is a finding, not a
gap to paper over. Per-archetype the rung labels specialise (a lender's ladder
runs on asset quality and RoA, not product spec); declare the specialised rung
where the archetype needs it. The Section 1B footprint on each rung is a
NEIGHBOURHOOD, not a computed number: Stage 11 derives the actual destination
PE from the framework; the rung only says where on the ladder that number
should land.
- R0 NON-OPERATING / ACCOUNTING-DRIVEN. Earnings not from an operating
  business (revaluations, one-offs, holding relics). No operating destination
  PE; SOTP/NAV or floor treatment. A transition FROM here must first prove an
  operating engine exists.
- R1 COMMODITY PRICE-TAKER. No pricing power; ROCE cyclical around cost of
  capital; cash volatile. ~12x neighbourhood.
- R2 COST-ADVANTAGED CONVERTER. Margin from cost position, not price; durable
  mid-teens ROCE; Amendment 17 converter multiple caps converter slices.
  ~15-17x neighbourhood.
- R3 VALUE-ADDED / SPEC'D SUPPLIER. Spec-in and switching costs give partial
  pricing power; ROCE 20-25% with stickiness. ~19x neighbourhood.
- R4 FRANCHISE / SHARE-OF-WALLET LEADER. Customer capture and repeat
  economics; ROCE 25-30% durable, strong cash. ~21x neighbourhood.
- R5 BRAND / SCARCITY OWNER. Pricing power from brand or structural scarcity;
  ROCE >30%; strategic-premium eligible. ~24x + strategic premium.
Two rules bind the ladder:
- Re-rating engine = the Stage 11 destination-PE delta implied by the rung
  migration; recognition gap = whether current PE already sits at the TO
  rung's neighbourhood. Stage 11 computes; the ladder names.
- Rung-jump base rate: one rung per 2-3 years. A claimed multi-rung leap
  requires extraordinary proof and is itself a red flag.
The alpha the strategy hunts is a real climb of one or more rungs that the
market has not yet repriced (the recognition gap, Part B4).

## TRANSITION DECISION MATRIX (Stage 13 / gate recommendation applies this; adjust via operator ruling only)
Maps the signed model's three state variables to a transition POSTURE. The
posture informs the gate recommendation and the value-trap test; it never
replaces the five-verdict set and never sets a price. The variables:
PROOF GATE (fired / not fired, Part B3), UGLINESS (ARTIFACT-OF-CLIMB /
STRUCTURAL-FEATURE, Part B5), RECOGNITION GAP (open = TO not yet priced /
closed = TO already priced, Part B4, resolved at Stage 11).
- Proof FIRED + ARTIFACT + gap OPEN -> RE-RATING LIVE. The prime setup: the
  climb is proven, the ugly optic is temporary, the market has not repriced.
  Constructive; the BUY still gates on Role 1 valuation and the Hurdle.
- Proof FIRED + ARTIFACT + gap CLOSED -> EARNINGS-ONLY. Climb real but
  already priced; the re-rating engine is spent, returns ride EPS CAGR alone.
  Actionable only if growth clears the Hurdle without help from re-rating.
- Proof NOT FIRED + ARTIFACT + gap OPEN -> RESEARCH / WATCH. Narrative until
  the proof gate fires (Part B3). Not a trade; watch the gate.
- Proof NOT FIRED + ARTIFACT + gap CLOSED -> PRICED NARRATIVE (TRAP). Clean
  optics, transition narrated but unproven, TO state already priced. The most
  seductive cell: no ugliness warns you off, and the downside is double (the
  transition fails AND the multiple compresses). AVOID or hard WATCH with no
  position until the proof gate fires AND the price re-opens the gap.
- Proof NOT FIRED + STRUCTURAL -> VALUE-TRAP RISK. The ugly optic looks
  permanent; classify DEEP WATCH or AVOID unless the classification is
  disproven.
- Proof FIRED + STRUCTURAL -> CONTRADICTION. The gate says climbing, the
  ugliness says decaying; a flag to resolve, not a posture. Re-examine the
  classification before any verdict.
- gap CLOSED + STRUCTURAL -> AVOID. Priced and not really climbing.
State space exhaustive: 2x2x2 = 8 states, all mapped. The two STRUCTURAL rows
each cover both gap states, with gap CLOSED + STRUCTURAL -> AVOID as the
dominating overlay.

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
