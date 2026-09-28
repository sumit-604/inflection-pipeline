#!/usr/bin/env python3
"""Extract the LAST fenced yaml block from a stage report into outputs/blocks/.
Usage: extract_block.py <report.md> <out.yaml>"""
import sys, re, os
src, out = sys.argv[1], sys.argv[2]
txt = open(src, encoding='utf-8', errors='replace').read()
blocks = re.findall(r'```yaml\s*\n(.*?)\n```', txt, re.S)
if not blocks:
    blocks = re.findall(r'```\s*\n(stage:.*?)\n```', txt, re.S)
if not blocks:
    print(f'FAIL no fenced yaml block in {src}'); sys.exit(2)
body = blocks[-1]
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w').write(body.rstrip() + '\n')
try:
    import yaml
    d = yaml.safe_load(body)
    if not isinstance(d, dict) or 'stage' not in d:
        print(f'FAIL parsed but no stage key in {src}'); sys.exit(3)
    print(f"OK {out}  stage={d.get('stage')} status={d.get('status')} keys={len(d)}")
except ImportError:
    print(f'OK {out} (pyyaml absent, not validated)')
except Exception as e:
    print(f'FAIL yaml parse error in {src}: {e}'); sys.exit(4)
