# Repo layout proposal, October 2026

Date: 2026-10-03. Report only. Nothing here is implemented.

## Measurements (this cloud container)

| Measure | Value |
|---|---|
| `.git` size (pack) | 6.9 GB (6.84 GiB pack) |
| Working tree | 4.8 GB |
| `runs/` | 4.8 GB, 7,217 files, 105 run folders on main |
| PDFs under `runs/` | 1,904 files, 4.7 GB (about 98% of `runs/`) |
| Intermediates (`work/`, `extracted/`) | 342 files in `work/`, 13 MB in `extracted/` |
| Commits on main touching `runs/` | 1,375 of 1,766 (78%) |
| `git status` | 0.04 s |
| `git checkout main` (about 70 files differ) | 0.06 s |
| `git stash` over the full tree (observed this session) | more than 4 minutes, in its `reset --hard` step |
| Session clone | shallow by default; still checks out the full 4.8 GB tree |

Reading: day-to-day commands are fast. The cost sits in three places:
1. Every cloud session clones and checks out 4.8 GB of PDFs, most of which belong to runs it never touches.
2. Any whole-tree rewrite (stash, reset, a checkout across many run folders) is slow.
3. History grows by every PDF ever committed. A deleted PDF still costs clone time.

## Option (a): move `runs/` to a separate repository

Create `inflection-runs` for `runs/`. This repo keeps prompts, frameworks, agents, `companies/` and the audits. A session attaches the runs repo, or only the one run folder through a sparse checkout.

- **What it breaks.** All four commands resolve `runs/<folder>` relative to this repo: `/run-pipeline`, `/fttcp`, `/finalize` and `/run-quarterly`. `/step1` and the collector (`tools/collector/collect_to_repo.py`) push corpora into `runs/`. The run PR flow becomes a PR in the runs repo, while `companies/` and `LESSONS_ARCHIVE.md` updates stay here, so a run spans two repos and two PRs. The session-start hook and the verifiers' absolute-path rule need the new root.
- **Fix.** Add one `RUNS_ROOT` setting that every command and agent reads. Update the 29 `runs/...` path statements in 11 files (commands, prompts, agents, collector, CLAUDE.md). Teach the collector the second remote. Run one migration that copies `runs/` with its history (`git filter-repo --path runs/`).
- **Work.** About one focused day plus a test run. Medium risk: every path statement must change in the same commit.
- **Gain.** This repo drops to tens of MB. The runs repo still carries the full PDF weight.

## Option (b): keep `runs/` here, stop committing intermediates

Ignore `runs/*/work/**`, `runs/*/extracted/**` (except `*.txt` text caches) and OCR scratch.

- **What it breaks.** Little. The TOOLING GATE text cache (`.txt` beside each PDF) must stay committed, or every stage re-extracts. Verifier A loses the ability to re-check an intermediate after the session ends.
- **Work.** One `.gitignore` commit and a note in run-pipeline.md.
- **Gain.** Almost none. The intermediates are 13 MB against 4.7 GB of PDFs. **Not recommended** as a fix for size.

## Option (c): Git LFS for the bulky files

Track `runs/**/*.pdf` (and `*.xlsx`, images) with Git LFS. Sessions clone with `GIT_LFS_SKIP_SMUDGE=1` and pull only the run they work on: `git lfs pull --include "runs/<folder>/**"`.

- **What it breaks.**
  - The cloud container needs `git-lfs` installed (setup script) and authenticated LFS access.
  - The collector must run `git lfs install` on the operator's machine.
  - Any command or verifier that opens a PDF in a folder it did not pull sees a pointer file. That is why the four commands each need one "pull this run's PDFs" step at stage 0.
  - Past PDFs stay in plain history unless history is rewritten. A rewrite (`git lfs migrate import`) force-pushes main and breaks every open branch and PR.
- **Storage.** GitHub LFS has its own storage and bandwidth quota (paid data packs above the free tier). 4.7 GB of PDFs, re-downloaded by every session, will exceed the free tier quickly.
- **Work.** Half a day for new files only. Plus one coordinated rewrite day if the history is cleaned.

## Option (d), cheapest first step: sparse checkout per session

No repo change. Start cloud sessions with a sparse checkout that includes everything except `runs/`, plus the one run folder the session works on. The `create_session` call and environment settings support `sparse_checkout_paths`. A session that needs another run adds its folder to the sparse set.

- **What it breaks.** A session cannot read a run it did not include. That matters for a COST SPIKE check (the prior run's `session-cost.md`) and for the company-memory links. Fix: include `runs/*/session-cost.md` and `runs/*/manifest.yaml` in the sparse pattern; both are small.
- **Work.** One line in the session-start instructions. The commands stay unchanged.
- **Gain.** A session checks out tens of MB, not 4.8 GB. The pack download stays, but shallow clones already limit it.

## Recommendation

1. Start with **(d)** now. It removes most per-session cost at zero risk and changes no command.
2. Decide on **(a)** within the quarter. The repo grows by about one run folder per working day, and history only grows.
3. Skip **(b)** for size; it saves 13 MB.
4. Use **(c)** only if the runs must stay in this repo and the LFS quota cost is acceptable.

## Follow-up answers (operator questions, 2026-10-03)

### Does option (a) rewrite this repo's history?

No, not as written. Option (a) copies the `runs/` history into the new repository (`git filter-repo --path runs/` on a throwaway clone) and then removes `runs/` from this repo with an ordinary commit. That keeps every branch, PR and hash here valid. The cost: this repo's pack stays at about 6.8 GB, so a full clone stays as slow as today. Only checkouts get small.

Shrinking the clone needs a history rewrite of this repo (`git filter-repo --invert-paths --path runs/`) and a force-push of `main`. That changes every commit hash, breaks every open branch and PR, and forces every existing clone to re-clone. Do it at most once, after open PRs are merged or closed, and only by explicit ruling.

### Duplicate PDFs by hash (main at 41b18319)

| Measure | Value |
|---|---|
| PDFs on main | 1,903 |
| Unique contents | 1,643 |
| Duplicate groups | 231 |
| Extra copies | 260 |
| Size of extra copies | 0.44 GB of 4.95 GB (9%) |
| Groups spanning 2+ run folders | 213 (0.31 GB) |

Git already stores each unique PDF once in its pack, so duplicates cost checkout disk, not clone download. Most duplicates are legitimate: a company's own transcript reused as a peer transcript in another run.

Six look like corpus errors, worth checking before those runs are reused:

| Run | Finding |
|---|---|
| cleanmax-2026-09-01 | Holds six Vinyas documents: the Vinyas prospectus filed as an annual report, the Vinyas FY2023-24 annual report, and four Vinyas investor presentations. The CLEANMAX corpus is contaminated with another company's filings. |
| gaudiumivf-2026-07-16 | `Annual_Report_2020.pdf` is byte-identical to `10.3 Annual Report FY 2024-25.pdf`. The run has no real FY2020 report. |
| vinyas-2026-09-01 | `Annual_Report_2015.pdf` is byte-identical to the FY2023-24 SME annual report. |
| azad-2026-07-12 | The annual-report file is byte-identical to the file in rating/. One of them is misfiled. |
| sfl-2026-07-14 | The presentation file is byte-identical to a file in screening/. |
| kronox-2026-08-30 | `inputs/annual-report/1718019653328.pdf` is the June 2024 IPO prospectus, not an annual report (found while testing the AR section index). |

Full list of duplicate groups: produced in the session that wrote this file; re-run with `git ls-tree -r -l origin/main runs/` and group by blob hash.
