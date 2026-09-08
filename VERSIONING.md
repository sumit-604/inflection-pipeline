# Framework versions and bookmarks

## What a bookmark (tag) is

The rule book that prices companies lives in `frameworks/`. It changes over
time. A **tag** is a bookmark that saves a snapshot of the whole repo at one
moment. If you look back at a company in 2028, you can open the exact rules that
priced it today.

Bookmarks are named by date: `fw-YYYY-MM-DD` (for example `fw-2026-07-18`).

## The rules right now (08 September 2026)

- Master Project Prompt: **v3.7** (Growth Symmetry companion, Rules F to J:
  mandatory Second-Order Section, Entrepreneur Ledger, steelman ordering,
  paired success catalogue, depth by default). The file is still named
  `Master_Project_Prompt_v3_6.md`; the path is a stable injection target,
  the version is in the banner.
- Section 1B (exit multiple): the **seven-layer set** — v3.3 Amendments +
  v3.5.1 Reconciliation + v3.6 Amendments + v3.7 Amendments (commodity
  converters, 20-Aug) + v3.8 Amendments (exit-basis symmetry and option
  resolution, 23-Aug) + v3.9 Amendments (relative valuation cross-check
  step 1C, 26-Aug; forward-expectation exit framework, Amendments 21-25,
  07-Sep) + v3.10 Amendments (growth symmetry in projections and
  weighting, Amendment 26, 08-Sep). Where they overlap, v3.10 governs the
  items it names, then v3.9, then v3.8, then v3.7, then v3.6, then
  v3.5.1, then v3.3.
- FTTCP: **v2.3** Consolidated (v2.2 probabilistic catalyst credit and
  Section C.2; v2.3 Step 4.5 Second-Order Section). File keeps the
  `FTTCP_v2_1_Consolidated.md` stem for pipeline-pointer stability.
- Quarterly Results Review Protocol: **v1.4** (Concall protocol: v1.1)
- Annual Report Analysis Protocol: **v1.3**
- Debt Capacity Assessment: **v1.0**
- Market-Implied Assumptions: **v1.0**
- Downstream Source Discovery Protocol: **v1.0**
- Success catalogue: created 08-Sep-2026, **0 of 4 names**; Rule I is not
  enforced in Role 3 until it holds four
- macro-sheet.md: referenced by the v3.6 stage 11 reads, NOT yet committed
  (open action; Amendment 15 relative PE is not computable until it lands)

## How each run remembers its rules

Every `/finalize` writes `outputs/final/provenance.yaml` into the run folder. It
records the git commit and the nearest bookmark the run used. So each company's
folder already says which rules priced it. The bookmark is the easy human label;
the git commit is the exact, permanent one.

## Making a new bookmark (do this after merging to main)

Bookmarks belong on the `main` copy, after a change is merged. To make one:

```
git checkout main
git pull
git tag -a fw-2026-07-18 -m "Master v3.3 / Section 1B v3.5.1 / FTTCP v1.2 (v1.3 content)"
git push origin fw-2026-07-18
```

Make a new bookmark whenever you change a framework file and merge it. See the
existing bookmarks any time with `git tag`.

## Branch discipline

- `main` is the good copy. It always has coherent, working rules.
- Do work on a branch (like `claude/...`), then merge into `main`.
- Bookmark `main` after a framework change lands there.
