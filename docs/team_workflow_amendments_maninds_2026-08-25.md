# Web-side amendments to team_workflow_project_instructions.md

Source: MANINDS 2026-08-21 lessons directive. Prepared 2026-08-25.

`team_workflow_project_instructions.md` lives at claude.ai project-instruction
level, not in this repo (see CLAUDE.md TEAM WORKFLOW and CHANGES.md). Claude
Code cannot edit it. This file is the ferry payload. The operator applies the
four edits below to the claude.ai project instructions the same day, so the
web-side manual and the repo amendments land together.

The repo-side companion of this directive (LESSONS.md entry and the stage 0
Freshness Pair Check in prompts/00-orchestrator.md, prompts/09b-halt1-dossier.md,
and .claude/commands/run-pipeline.md) is on the same branch and PR.

---

## Edit 1 — Phase 2, new step (0) before (a)

Insert as the first step of Phase 2, ahead of the current step (a), and
re-letter nothing (the new step is (0)):

> (0) Claude web independently lists inputs/ from the repo clone and
> reconciles it against the expected document set before reading the dossier.
> The corpus audit line is verified, not trusted.

Rationale: on MANINDS the 09b corpus audit named the missing Q1FY27 concall
as a gap, but the operator only found it several Phase 2 turns in. Reconciling
inputs/ first, before reading the dossier, catches the gap at the top of
Phase 2. The repo-side Freshness Pair Check now also caps the gate on this
class of gap, so the two checks reinforce each other.

## Edit 2 — "What you always do" list, add one item

Add to the "What you always do" list:

> List inputs/ first.

## Edit 3 — "Standing rules", add one rule

Add to the "Standing rules" list:

> Claude web reads the repo (read-only clone, work/extracted/ included);
> ferried extraction prompts are for uncommitted session state only.

## Edit 4 — Amendment 17 phrasing correction

Find the converter phrasing that reads (approximately):

> converter multiple 0.5×ROCE+7.5

Replace it with:

> converter slices take through-cycle ROCE into the standard Pillar 1
> formula (17.1) and do not inherit the core multiple on resolution (18.3).

Rationale: the old phrasing stated a wrong converter multiple. The corrected
text points at the governing clauses (Section 1B v3.7 Amendment 17.1 and the
v3.8 Amendment 18.3 resolution rule) instead of a bare formula.

---

## Confirmation checklist for the operator

- [ ] Phase 2 step (0) inserted before (a).
- [ ] "List inputs/ first." added to "What you always do".
- [ ] Repo read-only-clone rule added to "Standing rules".
- [ ] Amendment 17 converter phrasing corrected.
