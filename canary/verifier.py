#!/usr/bin/env python3
"""
Canary — silent model-drift detector for the Inflection Alpha pipeline.

Why this exists
---------------
Valuations run on `claude-opus-4-8`, a dateless alias. During capacity events
the provider can reroute requests to fallback weights with no notice and no log
entry. If that happens on a valuation day, the numbers shift underneath the
operator with nothing recorded. This script is the canary in the coal mine: a
tiny, fixed probe run daily whose only job is to notice "the model serving my
requests is not the same thing it was yesterday" and, on drift, block the
pipeline until a human looks.

What it does
------------
Sends ONE fixed, low-temperature prompt to the target model N times, then
fingerprints each reply:
  - the `model` field the server reports (an explicit-reroute signal), and
  - `stop_reason`, and
  - sha256 of the first PREFIX_CHARS characters of the text output.
It compares every probe's fingerprint against a calibrated set of known-good
fingerprints in golden.json. A reported-model change is a hard fail. A novel
output fingerprint on a majority of probes is drift. On either, it writes
canary/DRIFT.flag and exits non-zero; the pipeline gate refuses to run until
the operator reviews and clears it.

No third-party dependencies. Standard library only, so cron never breaks on a
missing package. The API key is read from ANTHROPIC_API_KEY at run time.

Usage
-----
  python canary/verifier.py --calibrate        # after a known-good day: seed golden.json
  python canary/verifier.py                     # daily check (default); exit 1 on drift
  python canary/verifier.py --check-gate        # pipeline gate: exit 1 iff DRIFT.flag present
  python canary/verifier.py --clear             # operator clears drift after review
  python canary/verifier.py --selftest          # offline logic test, no API key needed

Cost: ~4 tiny probes/day, roughly $0.10/month.
"""

import argparse
import hashlib
import json
import os
import ssl
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
GOLDEN_PATH = os.path.join(HERE, "golden.json")
STATE_PATH = os.path.join(HERE, "state.json")
DRIFT_FLAG = os.path.join(HERE, "DRIFT.flag")

ENDPOINT = "https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION = "2023-06-01"

# ---------------------------------------------------------------------------
# Fingerprinting
# ---------------------------------------------------------------------------

def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def extract_text(content):
    """Concatenate the text blocks of a Messages API response `content` array."""
    if not isinstance(content, list):
        return ""
    parts = []
    for block in content:
        if isinstance(block, dict) and block.get("type") == "text":
            parts.append(block.get("text", ""))
    return "".join(parts)


def fingerprint(resp_body, prefix_chars):
    """Turn a Messages API response body into a comparable fingerprint."""
    text = extract_text(resp_body.get("content"))
    prefix = text[:prefix_chars]
    return {
        "model": resp_body.get("model"),
        "stop_reason": resp_body.get("stop_reason"),
        "output_sha256": hashlib.sha256(prefix.encode("utf-8")).hexdigest(),
        "sample_prefix": prefix[:120],
    }


# ---------------------------------------------------------------------------
# API call (stdlib only)
# ---------------------------------------------------------------------------

def _ssl_context():
    ctx = ssl.create_default_context()
    ca = os.environ.get("CANARY_CA_BUNDLE") or os.environ.get("SSL_CERT_FILE")
    if ca and os.path.exists(ca):
        ctx.load_verify_locations(ca)
    return ctx


def call_model(api_key, model, request_spec, retries=4):
    """One Messages API call. Returns (body_dict, response_headers). Retries on
    transient network / 429 / 5xx with exponential backoff (2,4,8,16s)."""
    payload = {
        "model": model,
        "max_tokens": request_spec["max_tokens"],
        "temperature": request_spec.get("temperature", 0),
        "messages": [{"role": "user", "content": request_spec["prompt"]}],
    }
    system = request_spec.get("system")
    if system:
        payload["system"] = system
    data = json.dumps(payload).encode("utf-8")
    headers = {
        "content-type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": ANTHROPIC_VERSION,
    }
    ctx = _ssl_context()
    delay = 2
    last_err = None
    for attempt in range(retries):
        req = urllib.request.Request(ENDPOINT, data=data, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=60, context=ctx) as r:
                body = json.loads(r.read().decode("utf-8"))
                resp_headers = {k.lower(): v for k, v in r.headers.items()}
                return body, resp_headers
        except urllib.error.HTTPError as e:
            code = e.code
            last_err = f"HTTP {code}: {e.read().decode('utf-8', 'replace')[:300]}"
            if code in (408, 409, 429) or 500 <= code < 600:
                pass  # transient, retry
            else:
                raise RuntimeError(last_err)  # 4xx (auth, bad request) — do not retry
        except (urllib.error.URLError, TimeoutError, ssl.SSLError) as e:
            last_err = f"network: {e}"
        if attempt < retries - 1:
            time.sleep(delay)
            delay *= 2
    raise RuntimeError(f"probe failed after {retries} attempts: {last_err}")


# ---------------------------------------------------------------------------
# golden.json
# ---------------------------------------------------------------------------

def load_golden():
    if not os.path.exists(GOLDEN_PATH):
        raise SystemExit(f"golden.json not found at {GOLDEN_PATH}. Run --calibrate first.")
    with open(GOLDEN_PATH) as f:
        g = json.load(f)
    if not g.get("calibrated"):
        raise SystemExit(
            "golden.json is UNCALIBRATED (calibrated: false). On a known-good day run:\n"
            "  ANTHROPIC_API_KEY=... python canary/verifier.py --calibrate\n"
            "The canary fails closed until it has a known-good baseline."
        )
    return g


def write_golden(g):
    with open(GOLDEN_PATH, "w") as f:
        json.dump(g, f, indent=2)
        f.write("\n")


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def require_key():
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        raise SystemExit("ANTHROPIC_API_KEY is not set in the environment.")
    return key


def cmd_calibrate(args):
    """Run many probes on a known-good day and record every distinct fingerprint
    as accepted. Capturing natural low-temperature variation up front keeps the
    daily check from crying wolf on ordinary token jitter."""
    key = require_key()
    with open(GOLDEN_PATH) as f:
        g = json.load(f)
    model = args.model or g.get("target_model")
    if not model:
        raise SystemExit("No target_model in golden.json and no --model given.")
    req = g["request"]
    prefix_chars = g.get("prefix_chars", 200)
    n = args.probes or 12
    seen = {}
    print(f"Calibrating {model}: {n} probes...")
    for i in range(n):
        body, _ = call_model(key, model, req)
        fp = fingerprint(body, prefix_chars)
        seen[fp["output_sha256"]] = fp
        print(f"  probe {i+1}/{n}: model={fp['model']} stop={fp['stop_reason']} "
              f"sha={fp['output_sha256'][:12]} | {fp['sample_prefix']!r}")
    g["calibrated"] = True
    g["target_model"] = model
    g["calibrated_at"] = now_iso()
    g["accepted"] = list(seen.values())
    g["accepted_models"] = sorted({fp["model"] for fp in seen.values()})
    write_golden(g)
    print(f"\nWrote {len(seen)} distinct accepted fingerprint(s) for model(s) "
          f"{g['accepted_models']} to golden.json.")
    print("Review the sample_prefix values above look sane, then commit golden.json.")


def cmd_check(args):
    """Daily drift check. Exit 0 = clean, 1 = drift (flag written, pipeline blocked)."""
    key = require_key()
    g = load_golden()
    model = g["target_model"]
    req = g["request"]
    prefix_chars = g.get("prefix_chars", 200)
    accepted_hashes = {a["output_sha256"] for a in g["accepted"]}
    accepted_models = set(g.get("accepted_models") or [a["model"] for a in g["accepted"]])
    n = args.probes or 4

    probes = []
    for i in range(n):
        body, hdrs = call_model(key, model, req)
        fp = fingerprint(body, prefix_chars)
        fp["request_id"] = hdrs.get("request-id") or hdrs.get("x-request-id")
        fp["reported_model_novel"] = fp["model"] not in accepted_models
        fp["output_novel"] = fp["output_sha256"] not in accepted_hashes
        probes.append(fp)

    model_changed = any(p["reported_model_novel"] for p in probes)
    novel_count = sum(1 for p in probes if p["output_novel"])
    majority_novel = novel_count > n // 2  # strict majority of probes drifted

    if model_changed:
        status = "DRIFT"
        reason = "reported model field differs from calibrated baseline (explicit reroute)"
    elif majority_novel:
        status = "DRIFT"
        reason = f"{novel_count}/{n} probes produced novel output fingerprints"
    elif novel_count > 0:
        status = "WARN"
        reason = f"{novel_count}/{n} probes novel (within tolerance; likely temperature jitter)"
    else:
        status = "CLEAN"
        reason = "all probes match a known-good fingerprint"

    state = {
        "ran_at": now_iso(),
        "target_model": model,
        "status": status,
        "reason": reason,
        "novel_count": novel_count,
        "probes": probes,
        "calibrated_at": g.get("calibrated_at"),
    }
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)
        f.write("\n")

    print(f"[canary] {status}: {reason}")
    for i, p in enumerate(probes):
        marks = []
        if p["reported_model_novel"]:
            marks.append("MODEL-CHANGED")
        if p["output_novel"]:
            marks.append("novel-output")
        tag = (" <- " + ", ".join(marks)) if marks else ""
        print(f"  probe {i+1}: model={p['model']} stop={p['stop_reason']} "
              f"sha={p['output_sha256'][:12]}{tag}")

    if status == "DRIFT":
        with open(DRIFT_FLAG, "w") as f:
            json.dump(state, f, indent=2)
            f.write("\n")
        print(f"\n[canary] DRIFT flag written to {DRIFT_FLAG}")
        print("[canary] Pipeline is BLOCKED. Review the probes above; if the change is")
        print("[canary] legitimate (e.g. an intended model upgrade), re-calibrate:")
        print("[canary]   python canary/verifier.py --calibrate")
        print("[canary] Otherwise investigate the reroute before running any valuation.")
        print("[canary] To clear the block after review: python canary/verifier.py --clear")
        return 1

    # A clean run clears any stale WARN noise but never auto-clears a DRIFT flag.
    return 0


def cmd_check_gate(args):
    """Called by pipeline commands at start. Exit 1 iff a drift flag is present."""
    if os.path.exists(DRIFT_FLAG):
        print(f"[canary] BLOCKED: {DRIFT_FLAG} present. Model drift is unresolved.")
        print("[canary] Run `python canary/verifier.py --clear` after review to unblock.")
        return 1
    print("[canary] gate open (no drift flag).")
    return 0


def cmd_clear(args):
    if os.path.exists(DRIFT_FLAG):
        os.remove(DRIFT_FLAG)
        print(f"[canary] cleared {DRIFT_FLAG}. Pipeline unblocked.")
    else:
        print("[canary] no drift flag to clear.")
    return 0


def cmd_selftest(args):
    """Offline test of the fingerprint + decision logic. No API key, no network."""
    print("Running offline selftest...")
    # Simulated calibrated baseline: two known-good outputs.
    baseline_a = {"model": "claude-opus-4-8", "stop_reason": "end_turn",
                  "content": [{"type": "text", "text": "A bright canary warns miners before the invisible gas turns deadly below."}]}
    baseline_b = {"model": "claude-opus-4-8", "stop_reason": "end_turn",
                  "content": [{"type": "text", "text": "A small canary warns miners before the invisible gas turns deadly below."}]}
    fp_a = fingerprint(baseline_a, 200)
    fp_b = fingerprint(baseline_b, 200)
    assert fp_a["output_sha256"] != fp_b["output_sha256"], "distinct texts must hash differently"
    assert fingerprint(baseline_a, 200)["output_sha256"] == fp_a["output_sha256"], "hash must be stable"
    accepted_hashes = {fp_a["output_sha256"], fp_b["output_sha256"]}
    accepted_models = {"claude-opus-4-8"}

    def classify(bodies, n):
        probes = [fingerprint(b, 200) for b in bodies]
        for p in probes:
            p["reported_model_novel"] = p["model"] not in accepted_models
            p["output_novel"] = p["output_sha256"] not in accepted_hashes
        model_changed = any(p["reported_model_novel"] for p in probes)
        novel = sum(1 for p in probes if p["output_novel"])
        if model_changed:
            return "DRIFT"
        if novel > n // 2:
            return "DRIFT"
        if novel > 0:
            return "WARN"
        return "CLEAN"

    # Case 1: all probes match baseline -> CLEAN
    assert classify([baseline_a, baseline_a, baseline_b, baseline_a], 4) == "CLEAN"
    # Case 2: one odd probe out of four -> WARN (tolerated jitter)
    drifted = {"model": "claude-opus-4-8", "stop_reason": "end_turn",
               "content": [{"type": "text", "text": "Completely different phrasing that was never seen during calibration at all."}]}
    assert classify([baseline_a, baseline_a, baseline_a, drifted], 4) == "WARN"
    # Case 3: majority of probes novel -> DRIFT
    assert classify([drifted, drifted, drifted, baseline_a], 4) == "DRIFT"
    # Case 4: reported model field changed -> DRIFT regardless of output
    rerouted = {"model": "claude-fallback-x", "stop_reason": "end_turn",
                "content": [{"type": "text", "text": baseline_a["content"][0]["text"]}]}
    assert classify([baseline_a, baseline_a, baseline_a, rerouted], 4) == "DRIFT"
    print("  fingerprint stability: ok")
    print("  CLEAN / WARN / DRIFT(majority) / DRIFT(model-change) decisions: ok")
    print("selftest PASSED")
    return 0


def main():
    p = argparse.ArgumentParser(description="Model-drift canary for the Inflection Alpha pipeline.")
    g = p.add_mutually_exclusive_group()
    g.add_argument("--calibrate", action="store_true", help="seed golden.json from a known-good day")
    g.add_argument("--check-gate", action="store_true", help="pipeline gate: exit 1 iff drift flag present")
    g.add_argument("--clear", action="store_true", help="clear the drift flag after operator review")
    g.add_argument("--selftest", action="store_true", help="offline logic test, no API key")
    p.add_argument("--model", help="override target model (calibration only)")
    p.add_argument("--probes", type=int, help="number of probes (default: 12 calibrate / 4 check)")
    args = p.parse_args()

    if args.selftest:
        sys.exit(cmd_selftest(args))
    if args.calibrate:
        sys.exit(cmd_calibrate(args))
    if args.check_gate:
        sys.exit(cmd_check_gate(args))
    if args.clear:
        sys.exit(cmd_clear(args))
    sys.exit(cmd_check(args))


if __name__ == "__main__":
    main()
