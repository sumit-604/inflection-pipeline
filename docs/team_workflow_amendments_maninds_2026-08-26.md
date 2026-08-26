# Web-side amendments to team_workflow_project_instructions.md

Source: MANINDS relative-valuation directive, operator 2026-08-26. Prepared 2026-08-26.

`team_workflow_project_instructions.md` lives at claude.ai project-instruction
level, not in this repo (see CLAUDE.md TEAM WORKFLOW and CHANGES.md). Claude
Code cannot edit it. This file is the ferry payload. The operator applies the
edits below to the claude.ai project instructions the same day, so the web-side
manual and the repo amendment land together.

The repo-side companion is Section 1B v3.9 Amendment 20 (new step 1C), the
stage-11 wrapper step 11 in prompts/11-valuation-pipeline.md, the LESSONS.md
PROMOTED TO LAW entry, and the MANINDS Correction C6. All on the same branch
and PR.

Why this is a web step: step 1C needs a LIVE peer table. Claude Code holds no
live market data, so it cannot populate or govern step 1C. Claude web owns the
step; the pipeline marks the slot PENDING LIVE PEER TABLE and lets the pillar
destination govern until the live table lands.

---

## Edit 1 — Phase 2 / post-pillar, new step: run the Section 1B step 1C cross-check

Add to the Phase 2 valuation-support steps, after the pillar-approval gate and
before the verdict card is drafted:

> Run Section 1B step 1C (v3.9 Amendment 20). Build a LIVE peer table of 4-6
> listed peers: trailing P/E, clean/forward P/E, ROCE, growth, net debt,
> governance. Every figure carries its source and date. Identify the quality
> and value clusters on normalised (clean/forward) earnings. Place the subject
> against each cluster with every adjustment named and signed (quality, growth,
> governance, size/liquidity, cyclicality/converter). Rule bear/base/bull
> relative exit multiples on the entry-consistent earnings basis. Compare the
> pillar destination against the base-case adjusted peer base: pillar >30%
> below (pillar < 0.70x) → the relative multiple governs (bounded by the
> sector cap), pillar shown as a cross-check; else the pillar governs and the
> peer table is the cross-check. Print the divergence either way. When the
> relative multiple governs, recompute the exit price, FV path, FV CAGR,
> return-source label, and entry zone on the governing multiple.

## Edit 2 — "Standing rules", add one rule (the Correction 6 guard)

Add to the "Standing rules" list:

> Peer multiples for the step 1C cross-check are LIVE and DATED. Multiples
> pulled from memory are stale and barred. A peer table without live, dated,
> sourced figures cannot govern; the pillar destination governs until the live
> table lands.

## Edit 3 — "What you always do" list, add one item

Add to the "What you always do" list:

> On any valuation, supply the live step 1C peer table before the verdict card.

## Edit 4 — Annual maintenance, add the sector-cap review

Add to the standing maintenance actions:

> Review the Section 1B sector caps annually against live peer medians. Where a
> sector's live peer median clean/forward multiple has moved durably from the
> cap, re-rule the cap against the median and log the ruling in the Section 1B
> cap table with its date and evidence. A per-run cross-check never breaches a
> cap on its own; the annual review is the only channel that moves one.

---

## Confirmation checklist for the operator

- [ ] Step 1C cross-check added to Phase 2 after the pillar gate, before the verdict card.
- [ ] Correction 6 live-and-dated peer-multiple guard added to "Standing rules".
- [ ] "Supply the live step 1C peer table" added to "What you always do".
- [ ] Annual sector-cap review against live peer medians added to maintenance.
