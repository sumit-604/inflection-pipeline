# Canary — silent model-drift detector

`claude-opus-4-8` is a dateless alias. During capacity events the provider can
reroute requests to fallback weights with no notice and no log entry. If that
happens on a valuation day, the numbers shift underneath you and nothing records
it. This canary runs a fixed probe daily and, on drift, blocks the pipeline until
you review.

It is a bird in the coal mine, not an analyst: one dumb repeated check whose only
job is to notice *"the model serving my requests changed."* Standard library
only, no dependencies, so cron never breaks on a missing package. Cost is roughly
$0.10/month (four tiny probes a day).

## How it decides

Each probe fingerprints the reply three ways:
- the `model` field the server reports — a reported-model change is an **immediate
  hard fail** (explicit reroute),
- `stop_reason`, and
- sha256 of the first 200 chars of the output.

Because low-temperature output still jitters at the token level, `--calibrate`
captures the natural variation up front (many probes on a known-good day → a set
of accepted fingerprints). The daily check then flags:
- **CLEAN** — every probe matches a known-good fingerprint.
- **WARN** — a minority of probes novel (tolerated jitter; logged, not blocking).
- **DRIFT** — the reported model changed, **or** a strict majority of probes
  produced novel fingerprints. Writes `DRIFT.flag`, exits non-zero, blocks the
  pipeline.

## First-time setup (in your environment, where the API key lives)

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python canary/verifier.py --selftest        # offline sanity check, no key needed
python canary/verifier.py --calibrate       # on a KNOWN-GOOD day only
# review the printed sample sentences look sane, then:
git add canary/golden.json && git commit -m "canary: calibrate golden baseline"
```

Calibrate only when you trust the current model state. Everything after is
measured against that baseline.

## Daily run (cron)

```
30 7 * * * /home/user/inflection-pipeline/canary/run-daily.sh >> /home/user/inflection-pipeline/canary/canary.log 2>&1
```

`run-daily.sh` loads the key from `~/.inflection.env` (keep it out of git) and
runs the check. On drift it prints loudly; add your own notification hook if you
want a push.

## When drift fires

1. Read `canary/state.json` — the probes and the reason.
2. If the change is **legitimate** (an intended model upgrade you decided on),
   re-calibrate: `python canary/verifier.py --calibrate`, commit the new golden.
3. If the change is **unexplained**, do not run valuations. Investigate the
   reroute first.
4. Clear the block after review: `python canary/verifier.py --clear`.

## Blocking the pipeline (activation — one line per command, your call)

The canary already blocks by writing `DRIFT.flag`. To make `/run-pipeline`,
`/fttcp`, and `/finalize` actually refuse to start while drift is unresolved, add
this gate check at the top of each command's setup:

```bash
python canary/verifier.py --check-gate || { echo "Canary drift unresolved — aborting."; exit 1; }
```

`--check-gate` exits 1 iff `DRIFT.flag` is present, so it is a cheap local check
with no API call. This wiring touches the pipeline command files, so it is left
for you to approve separately rather than bundled in here.

## Files

- `verifier.py` — the canary (calibrate / check / gate / clear / selftest).
- `golden.json` — calibrated baseline. Committed so a thesis can be tied to the
  model state that produced it. Ships **uncalibrated**; fails closed until seeded.
- `run-daily.sh` — cron wrapper.
- `state.json` — last run result (git-ignored; runtime artifact).
- `DRIFT.flag` — present only while drift is unresolved (git-ignored).
