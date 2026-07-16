#!/usr/bin/env python3
"""Extract the LAST fenced ```yaml block from a report .md into blocks/<name>.yaml."""
import sys, re, pathlib
report = pathlib.Path(sys.argv[1])
name = sys.argv[2]  # e.g. B01
txt = report.read_text()
blocks = re.findall(r"```ya?ml\s*\n(.*?)```", txt, re.DOTALL)
if not blocks:
    print(f"NO YAML BLOCK FOUND in {report}", file=sys.stderr); sys.exit(1)
out = report.parent.parent / "blocks" / f"{name}.yaml"
out.write_text(blocks[-1].strip() + "\n")
print(f"extracted {len(blocks)} block(s); wrote last -> {out} ({len(blocks[-1])} chars)")
