# Cross-family verifiers

Verifiers B and C grade Opus output on Opus — same model family, same training
priors, same aesthetic about what a good verdict looks like. On FTTCP, the
pipeline's most consequential step (its ROCE forward verdict is the sole
authority for Role 1 Pillar 1), within-family grading is the softest link in the
chain. This directory holds the out-of-family checks.

## `fttcp_crossgrade.py` — cross-family FTTCP grader

Grades the written FTTCP draft against the FTTCP v1.2 rubric using a model from a
**different family** (Gemini by default; GPT-5.6 / OpenAI selectable).

**Grader-only, never a maker.** It does not re-run the analysis, produce a
verdict, or invent a number. It reads the artifact the Claude maker already wrote
plus the rubric, and returns PASS / FAIL / UNCERTAIN per rubric criterion with the
location in the draft. Grading against a fixed rubric does not reward-hack the way
generating from ambiguous inputs does — which is exactly why a cross-family
*grader* is safe here even though a cross-family *maker* (e.g. GPT-5.6 Sol, the
highest reward-hacking rate METR has published) is explicitly banned from the
pipeline. It never edits the draft and never overrides the maker's verdict; the
grade is advisory, weighed by the operator.

**It does not replace Verifier A.** Source fidelity — whether a cited number is
actually true in the source PDF — stays Verifier A's non-overridable hard gate.
This grader checks rubric *adherence*: cap application, single-credit, round-down,
verdict logic, anchor *presence*. It flags an unanchored number; it does not
adjudicate a number's truth.

### Run

```bash
# Gemini (default). Needs GEMINI_API_KEY (or GOOGLE_API_KEY).
python verifiers/fttcp_crossgrade.py runs/<ticker>-<date>

# GPT-5.6 / OpenAI. Needs OPENAI_API_KEY.
python verifiers/fttcp_crossgrade.py runs/<ticker>-<date> --provider openai --model gpt-5.6

# Offline logic test, no key:
python verifiers/fttcp_crossgrade.py --selftest
```

It reads `outputs/final/fttcp-draft.md` (falling back to `fttcp-deliberation.md`
or `fttcp-recommendation.md`) and writes `outputs/final/fttcp-crossgrade.md`.

### Exit codes

- `0` — graded, adherence PASS/CONCERNS.
- `1` — graded, at least one CRITICAL rubric violation (surface it prominently).
- `3` — skipped, no cross-family key configured. `/fttcp` treats this as a flag,
  not a halt: it notes the check did not run and drops FTTCP confidence one notch.

### Wiring

`/fttcp` runs this after writing the draft and before commit, and folds the grade
summary into what it prints for operator review. The outcome is recorded in
`fttcp-deliberation.md` at sign-off. The grade is advisory throughout; it never
overrides the operator's verdict and never edits the analysis.

### Notes

- Standard library only, no dependencies. The API key is read at run time.
- Model ids default to `gemini-2.5-pro` / `gpt-5.6`; override with `--model` if the
  provider's current id differs.
- `temperature: 0`, JSON-mode output; the rubric criteria are fixed in the script
  so grades are comparable across runs.
