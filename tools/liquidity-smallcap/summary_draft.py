#!/usr/bin/env python3
"""Draft the one-page summary from out/results.json and data/gaps.md.

It fills in numbers only: the best-leading measure, its lag, its r, and the
rolling-window months where the link ran the wrong way. A person reads the
draft against the chart and writes SUMMARY.md. The script never writes
SUMMARY.md itself.

Run: python summary_draft.py   (writes out/SUMMARY_DRAFT.md)
"""
from __future__ import annotations

import json
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = Path(os.environ.get("LSC_DATA", HERE / "data"))
OUT = Path(os.environ.get("LSC_OUT", HERE / "out"))
WORDS = {"net_laf": "net LAF (banking-system cash with the RBI)",
         "cd_3m": "the 3-month CD rate (what banks pay for 3-month money)",
         "mtf_nse": "the NSE MTF book (broker loans to buy shares)",
         "mtf_combined": "the NSE + BSE MTF book"}


def main() -> None:
    r = json.loads((OUT / "results.json").read_text())
    best = sorted(r["best"], key=lambda b: -(b["pearson"] * b["expected"]))
    L = ["# Draft: which money measure leads small caps", "",
         f"Months tested: {r['months']}. Numbers only; write SUMMARY.md from this.", ""]
    if not best:
        L.append("No measure had enough months to test.")
    else:
        top = best[0]
        L += [f"Best lead: {WORDS[top['measure']]}, {top['lag']} month(s) ahead, "
              f"r {top['pearson']:+.2f} on {top['n']} months "
              f"(95% bar {top['bar95']:.2f}; "
              f"{'clears' if top['clears_bar'] else 'does not clear'} it; "
              f"sign {'as expected' if top['right_sign'] else 'AGAINST expectation'}).", ""]
        L.append("Each measure at its best lead (lag 1 to 3):")
        for b in best:
            L.append(f"- {WORDS[b['measure']]}: lag {b['lag']}, r {b['pearson']:+.2f}, "
                     f"n {b['n']}, {'clears' if b['clears_bar'] else 'below'} bar, "
                     f"{'right' if b['right_sign'] else 'wrong'} sign")
        L += ["", "Rolling 12-month windows where the link ran the wrong way:"]
        for k, f in r["failures"].items():
            L.append(f"- {k} (lag {f['lag']}): {', '.join(f['runs']) or 'none'}")
    gaps = DATA / "gaps.md"
    if gaps.exists():
        L += ["", "Gaps: see data/gaps.md."]
    (OUT / "SUMMARY_DRAFT.md").write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
