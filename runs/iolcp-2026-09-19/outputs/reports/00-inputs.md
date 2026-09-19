# B00 — Stage 0 input validation (IOLCP, 2026-09-19)

Orchestrator stage. The block at outputs/blocks/B00-inputs.yaml is the full
record: spear gate (OVERRIDE, Step-1 intake), four load-bearing facts,
sector cap row (Pharma / CDMO, 38x, chunk 05) with evidence, reporting units
(INR Cr throughout), document identity manifest, freshness pairs, input gaps
and collector-defect resolutions.

Corpus verdict: CORPUS GAPPED-FRESHNESS. Missing mate: the CARE Ratings
rationale for the 30-Jun-2026 reaffirmation. The 04-Jul-2025 rationale is
the newest rating text held.

Tooling: every PDF pre-extracted to page-marked .txt beside it, OCR fallback
(rapidocr) on pages with no text layer. Log: inputs/_extraction-log.txt.

LESSONS PRE-READ (orchestrator memory, not passed to stages):
- OPEN: Amendment 14 fade guard; canary needs API key; cross-family grader
  deferred; fetch_bse_announcements first live test (this run: it WORKED but
  returned only the last ~30 days of a 12-month window, 7 of 105 rows);
  pending prompt-branch items 1-3 (stage 10 conservative-fill line,
  Amendment 6 rounding, OR-9).
- Tagged lessons for sector "Pharma / CDMO" or archetype: none tagged.
  Archetype not yet declared (Mental Model unsigned).
