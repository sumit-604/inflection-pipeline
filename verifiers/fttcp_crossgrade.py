#!/usr/bin/env python3
"""
Cross-family FTTCP grader — an out-of-family third opinion on the FTTCP output.

Why this exists
---------------
FTTCP is the most consequential adversarial step in the pipeline: its ROCE
forward verdict is the sole authority for Role 1 Pillar 1, so an error here
propagates into every valuation number. Verifiers B and C grade Opus output on
Opus — same family, same training priors, same aesthetic about what a good
FTTCP verdict looks like. That is the softest link in the chain. This script
adds a grader from a DIFFERENT model family (Gemini by default; GPT-5.6/OpenAI
selectable) whose only job is to grade the written FTTCP draft against the
FTTCP v1.2 rubric.

Grader-only, never a maker
--------------------------
It does NOT re-run the analysis, generate a verdict, or invent a number. It
reads the artifact the Claude maker already wrote plus the rubric, and for each
rubric criterion returns PASS / FAIL / UNCERTAIN with the location in the
artifact. This is deliberate: grading against a fixed rubric does not reward-hack
the way generating from ambiguous inputs does, which is the whole reason a
cross-family grader is safe here even when a cross-family maker would not be. It
never sees the maker's chain of reasoning — only the written draft, the rubric,
and (for anchor-presence checks) nothing beyond the draft's own citations. It
never edits the draft and never overrides the maker's verdict; its output is an
advisory grade the operator weighs.

It does NOT replace Verifier A. Source fidelity (does a number exist in the
source PDF) remains Verifier A's non-overridable hard gate. This grader checks
rubric ADHERENCE — cap application, single-credit, round-down, verdict logic,
anchor PRESENCE — not whether a cited number is true.

No third-party dependencies. Standard library only. The API key is read at run
time from the provider's env var.

Usage
-----
  python verifiers/fttcp_crossgrade.py <run folder>          # grade the FTTCP draft
  python verifiers/fttcp_crossgrade.py <run folder> --provider openai --model gpt-5.6
  python verifiers/fttcp_crossgrade.py --selftest            # offline, no key

Exit codes: 0 grade written (adherence PASS/CONCERNS) · 1 grade written with a
CRITICAL rubric violation · 3 skipped (no cross-family key configured).
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error
import ssl
from datetime import datetime, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUBRIC_PATH = os.path.join(REPO, "frameworks", "FTTCP_v1.2_Consolidated.md")

# The fixed rubric the cross-family model grades against. Derived from the
# FTTCP v1.2 DISCIPLINE rules and the CLAUDE.md NEVER list. Kept explicit so the
# grade is structured and comparable across runs even if the model does not
# fully parse the framework file (which is also supplied, as the authority).
CRITERIA = [
    ("exit_pe_source", "Every exit / destination PE comes only from Section 1B v3.3; no round-number defaults."),
    ("single_credit_roce", "ROCE recovery credited via Pillar 1 OR Strategic Premium, never both; the route is stated in writing."),
    ("no_hybrid_labels", "No hybrid transition labels; where a transition falls between two states it is rounded DOWN."),
    ("kernex_cap", "Where a transition is missing with no observable catalyst, the conservative (Kernex) cap is applied, not loosened."),
    ("indeterminate_cash", "INDETERMINATE cash conversion caps the disposition at PROCEED WITH CAVEATS with the missing evidence named; never a clean pass."),
    ("composite_in_range", "The composite score is the sum of the four transition scores and sits in the stated band (roughly -4 to +8)."),
    ("anchoring_present", "Every quantitative claim is followed by a (source, page/note) anchor, or is written NOT FOUND; no estimated fills."),
    ("step2e_governor", "Step 2E loosens a verdict only on net documented ACTION by one state; management vision alone never moves a verdict or lifts the cap."),
    ("forward_window", "The forward window is 3m primary / 6m secondary / 12m for ROCE (or 6m+12m for semi-annual reporters), stated."),
    ("sector_cap_row", "The sector cap row used is a real row from the Section 1B table and fits what the business is; any corrected row is stated."),
    ("verdict_logic", "The scored verdict, cap state, and any TRIM rule follow from the scorecard as written, with the single decisive print named."),
    ("no_fabricated_catalyst", "No catalyst is fabricated to fill a table; NONE FOUND is used where evidence is absent."),
]

GRADER_SYSTEM = (
    "You are a cross-family compliance grader for an equity-research protocol called FTTCP v1.2. "
    "You grade ADHERENCE of an already-written analysis to a fixed rubric. You are NOT an analyst. "
    "You must NOT re-run the analysis, produce your own FTTCP verdict, change any number, or invent "
    "any figure or catalyst. You judge only what is written in the supplied draft against the rubric. "
    "For a criterion you cannot judge from the draft alone, return UNCERTAIN — never guess. "
    "Source-fidelity (whether a cited number is actually true in the source PDF) is out of your scope; "
    "you only check whether an anchor is PRESENT. Output strictly the JSON schema requested, nothing else."
)


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def build_prompt(rubric_text, artifact_text):
    crit_lines = "\n".join(f'- id "{cid}": {desc}' for cid, desc in CRITERIA)
    schema = {
        "overall_adherence": "PASS | CONCERNS | FAIL",
        "criteria": [{"id": "<criterion id>", "verdict": "PASS | FAIL | UNCERTAIN",
                      "location": "<where in the draft, or NOT PRESENT>", "note": "<one line>"}],
        "critical_violations": ["<criterion id(s) whose FAIL would change the FTTCP verdict or valuation>"],
        "maker_verdict_as_written": "<the composite score and verdict exactly as the draft states it>",
        "grader_divergence": "<if you believe the rubric was misapplied in a way that would change the verdict, state it in one line; else empty>",
    }
    return (
        "RUBRIC CRITERIA (grade each):\n" + crit_lines +
        "\n\nYou also have the full FTTCP v1.2 framework as the governing authority:\n"
        "<<<FRAMEWORK\n" + rubric_text[:60000] + "\nFRAMEWORK>>>\n\n"
        "THE DRAFT TO GRADE (this is the maker's written output; grade only what is here):\n"
        "<<<DRAFT\n" + artifact_text[:120000] + "\nDRAFT>>>\n\n"
        "Return ONLY this JSON shape (no prose, no code fence):\n" + json.dumps(schema, indent=2)
    )


# ---------------------------------------------------------------------------
# Providers (stdlib only). Each returns the model's raw text output.
# ---------------------------------------------------------------------------

def _ssl_ctx():
    ctx = ssl.create_default_context()
    ca = os.environ.get("SSL_CERT_FILE")
    if ca and os.path.exists(ca):
        ctx.load_verify_locations(ca)
    return ctx


def _post(url, headers, body):
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=120, context=_ssl_ctx()) as r:
        return json.loads(r.read().decode("utf-8"))


def call_gemini(model, system, prompt):
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        return None, "no GEMINI_API_KEY / GOOGLE_API_KEY in env"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
    body = {
        "systemInstruction": {"parts": [{"text": system}]},
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0, "maxOutputTokens": 4096, "responseMimeType": "application/json"},
    }
    resp = _post(url, {"content-type": "application/json"}, body)
    try:
        return resp["candidates"][0]["content"]["parts"][0]["text"], None
    except (KeyError, IndexError):
        return None, f"unexpected Gemini response: {json.dumps(resp)[:300]}"


def call_openai(model, system, prompt):
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        return None, "no OPENAI_API_KEY in env"
    url = "https://api.openai.com/v1/chat/completions"
    body = {
        "model": model,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": prompt}],
        "temperature": 0,
        "response_format": {"type": "json_object"},
    }
    headers = {"content-type": "application/json", "authorization": f"Bearer {key}"}
    resp = _post(url, headers, body)
    try:
        return resp["choices"][0]["message"]["content"], None
    except (KeyError, IndexError):
        return None, f"unexpected OpenAI response: {json.dumps(resp)[:300]}"


PROVIDERS = {"gemini": call_gemini, "openai": call_openai}
DEFAULT_MODEL = {"gemini": "gemini-2.5-pro", "openai": "gpt-5.6"}


# ---------------------------------------------------------------------------
# Grade rendering
# ---------------------------------------------------------------------------

def parse_grade(raw):
    """Tolerant JSON parse — strip a stray code fence if the model added one."""
    s = raw.strip()
    if s.startswith("```"):
        s = s.split("\n", 1)[1] if "\n" in s else s
        s = s.rsplit("```", 1)[0]
    return json.loads(s)


def render_markdown(grade, provider, model, run_folder):
    lines = [
        f"# FTTCP Cross-Family Grade — {os.path.basename(run_folder.rstrip('/'))}",
        "",
        f"Grader: {provider} / {model} (out-of-family, grader-only). Generated {now_iso()}.",
        "Advisory. It never overrides the maker verdict, never edits the draft, and does",
        "not adjudicate whether a cited number is true (that is Verifier A's hard gate).",
        "",
        f"**Overall adherence: {grade.get('overall_adherence','?')}**",
        f"Maker verdict as written: {grade.get('maker_verdict_as_written','?')}",
    ]
    div = grade.get("grader_divergence")
    if div:
        lines += ["", f"**Grader divergence:** {div}"]
    crit = grade.get("critical_violations") or []
    if crit:
        lines += ["", f"**CRITICAL rubric violations:** {', '.join(crit)}"]
    lines += ["", "| Criterion | Verdict | Location | Note |", "| --- | --- | --- | --- |"]
    for c in grade.get("criteria", []):
        lines.append(f"| {c.get('id','')} | {c.get('verdict','')} | {c.get('location','')} | {c.get('note','')} |")
    lines += ["", "```yaml", "stage: fttcp-crossgrade",
              f"provider: {provider}", f"model: {model}",
              f"overall_adherence: \"{grade.get('overall_adherence','')}\"",
              f"critical_violations: {json.dumps(crit)}",
              f"grader_divergence: {json.dumps(div or '')}", "```", ""]
    return "\n".join(lines)


def load_artifact(run_folder):
    for name in ("fttcp-draft.md", "fttcp-deliberation.md", "fttcp-recommendation.md"):
        p = os.path.join(run_folder, "outputs", "final", name)
        if os.path.exists(p):
            with open(p) as f:
                return p, f.read()
    return None, None


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_grade(args):
    run_folder = args.run_folder
    if not run_folder or not os.path.isdir(run_folder):
        raise SystemExit(f"run folder not found: {run_folder}")
    art_path, artifact = load_artifact(run_folder)
    if not artifact:
        raise SystemExit(f"no FTTCP artifact in {run_folder}/outputs/final/ (need fttcp-draft.md or fttcp-deliberation.md)")
    with open(RUBRIC_PATH) as f:
        rubric = f.read()

    provider = args.provider
    model = args.model or DEFAULT_MODEL[provider]
    caller = PROVIDERS[provider]
    prompt = build_prompt(rubric, artifact)
    raw, err = caller(model, GRADER_SYSTEM, prompt)
    if raw is None and err and err.startswith("no "):
        print(f"[crossgrade] SKIPPED: {err}. Cross-family check did not run this session.")
        print("[crossgrade] Configure the provider key to enable it; treat FTTCP confidence as one notch lower.")
        return 3
    if raw is None:
        raise SystemExit(f"[crossgrade] provider error: {err}")

    grade = parse_grade(raw)
    out_md = render_markdown(grade, provider, model, run_folder)
    out_path = os.path.join(run_folder, "outputs", "final", "fttcp-crossgrade.md")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        f.write(out_md)

    print(f"[crossgrade] graded {os.path.basename(art_path)} with {provider}/{model}")
    print(f"[crossgrade] overall adherence: {grade.get('overall_adherence')}")
    crit = grade.get("critical_violations") or []
    if crit:
        print(f"[crossgrade] CRITICAL rubric violations: {', '.join(crit)}")
    if grade.get("grader_divergence"):
        print(f"[crossgrade] divergence: {grade['grader_divergence']}")
    print(f"[crossgrade] wrote {out_path}")
    return 1 if crit else 0


def cmd_selftest(args):
    print("Running offline selftest (no network, no key)...")
    prompt = build_prompt("RUBRIC BODY", "MAKER DRAFT with composite +5 of 8, PROCEED WITH FLAGS.")
    assert "RUBRIC CRITERIA" in prompt and "THE DRAFT TO GRADE" in prompt
    assert "single_credit_roce" in prompt and "indeterminate_cash" in prompt
    # Parser tolerates a stray code fence and a clean object.
    canned = """```json
{"overall_adherence":"CONCERNS","criteria":[{"id":"exit_pe_source","verdict":"PASS","location":"handoff block","note":"20x from Section 1B"},{"id":"single_credit_roce","verdict":"FAIL","location":"Pillar 1 + Strategic","note":"double credited"}],"critical_violations":["single_credit_roce"],"maker_verdict_as_written":"+5 of 8, PROCEED WITH FLAGS","grader_divergence":"single-credit breach would lift destination PE"}
```"""
    grade = parse_grade(canned)
    assert grade["overall_adherence"] == "CONCERNS"
    assert grade["critical_violations"] == ["single_credit_roce"]
    md = render_markdown(grade, "gemini", "gemini-2.5-pro", "runs/demo-2026-07-18")
    assert "**CRITICAL rubric violations:** single_credit_roce" in md
    assert "grader_divergence" in md and "stage: fttcp-crossgrade" in md
    assert len(CRITERIA) == 12
    # A clean object without a fence also parses.
    assert parse_grade('{"overall_adherence":"PASS","criteria":[]}')["overall_adherence"] == "PASS"
    print("  prompt assembly: ok")
    print("  JSON parse (fenced + clean): ok")
    print("  markdown + YAML render, critical-violation surfacing: ok")
    print("selftest PASSED")
    return 0


def main():
    p = argparse.ArgumentParser(description="Cross-family FTTCP rubric-adherence grader (grader-only).")
    p.add_argument("run_folder", nargs="?", help="path to runs/<ticker>-<date>/")
    p.add_argument("--provider", choices=list(PROVIDERS), default="gemini",
                   help="cross-family provider (default: gemini)")
    p.add_argument("--model", help="model id (default: provider default)")
    p.add_argument("--selftest", action="store_true", help="offline logic test, no key")
    args = p.parse_args()
    if args.selftest:
        sys.exit(cmd_selftest(args))
    sys.exit(cmd_grade(args))


if __name__ == "__main__":
    main()
