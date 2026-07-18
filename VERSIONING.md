# Framework versions and bookmarks

## What a bookmark (tag) is

The rule book that prices companies lives in `frameworks/`. It changes over
time. A **tag** is a bookmark that saves a snapshot of the whole repo at one
moment. If you look back at a company in 2028, you can open the exact rules that
priced it today.

Bookmarks are named by date: `fw-YYYY-MM-DD` (for example `fw-2026-07-18`).

## The rules right now (18 July 2026)

- Master Project Prompt: **v3.3**
- Section 1B (exit multiple): **v3.5.1** (this is the current one; it replaced
  the standalone Amendment 4.5)
- FTTCP: **v1.2** file, amended to **v1.3** content

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
