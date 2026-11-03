---
description: Shallow funnel for a batch of companies. Sonnet agents build each corpus, Opus agents write each card, then a run table. Usage: /shallow <name or ticker>, <name or ticker>, ...
---
You are running the SHALLOW FUNNEL for these companies:
$ARGUMENTS

Spec: screens/SHALLOW_ANALYSIS_FRAMEWORK.md. Rules for the corpus: screens/README.md.
You are the orchestrator. You do not read corpus documents and you do not write
cards yourself. Start this session on Sonnet 5.5 (operator ruling 2026-11-04):
orchestration is mechanical, and each agent carries its own model in its
frontmatter (shallow-corpus on Sonnet, shallow-card on Opus).

## Steps

1. Resolve identities. For each name, find the NSE symbol / BSE code with the
   Bull AI `search_companies` tool (free) or the screener.in search. Record name,
   ticker, screener URL, and market capitalisation with its source and date (Bull
   AI company record or Trendlyne). An ambiguous name: pick the listed match the
   operator most plausibly means, and say so in the run table. A company that
   already has a card dated within 30 days is skipped and listed as such.
2. Corpus. Dispatch one `shallow-corpus` agent per company, up to 4 at a time,
   each with: company name, ticker, screener URL. Keep each returned YAML block;
   do not open the corpora.
3. Cards. For each company whose corpus status is complete or partial, dispatch
   one `shallow-card` agent, up to 4 at a time, with: ticker, corpus path, and the
   market cap line from step 1. A blocked corpus gets no card; list it.
4. Run table. Write screens/forward-view-<YYYY-MM-DD>.md from the returned YAML
   blocks, in the format of screens/forward-view-2026-09-21.md: ticker, verdict,
   posture, FY+1 PAT, growth, forward PE, basis tier, load-bearing check.
   Sort PROCEED first, then by growth against forward PE.
5. Record the run in screens/README.md under a new "## Run, <date>" heading:
   names, verdicts, corpus gaps that recurred, and any reader or collector defect
   the agents reported. Keep it short.
6. Commit on the current branch (git commit -q). Raw PDFs stay gitignored.

Context economy: never paste an agent's card into this session. Read only the
YAML blocks. Run commands quiet (git status --short, git commit -q).
