#!/usr/bin/env bash
# Dry check for instruction and tooling changes (operator ruling 2026-10-03).
# Run it before merging any PR that touches .claude/, prompts/, frameworks/
# or tools/. It reads files and toggles the sparse checkout; it edits nothing.
#
# Usage:  tools/dry_check.sh            # all four checks
#         tools/dry_check.sh 1 2        # only the named checks
#
# Check 1  Frontmatter: agents, commands and skills parse; agent model and
#          effort are valid; commands pin no model; prompts and section-1b
#          reference chunks read as UTF-8.
# Check 2  Path references in agents, commands, skills and prompts resolve.
#          Run-relative paths resolve against the reference run below.
# Check 3  Sparse session: tools/sparse_session.sh <reference run> leaves
#          every path the four pipeline commands read on disk; --off then
#          restores a clean full tree. Needs a clean working tree.
# Check 4  Load-bearing anchors exist (orchestrator 7A, fttcp disk writes and
#          part 6), and the token-meter mod validates and passes its tests.
#
# Exit 0 when every check run passes, 1 otherwise.
set -uo pipefail
cd "$(git rev-parse --show-toplevel)"
REF_RUN="${DRY_CHECK_RUN:-runs/taaltech-2026-09-10}"
CHECKS=("$@"); [ "${#CHECKS[@]}" -eq 0 ] && CHECKS=(1 2 3 4)
declare -A RESULT

check1() {
python3 - <<'EOF'
import glob, re, sys
try:
    import yaml
except ImportError:
    sys.exit("PyYAML missing: pip install -q pyyaml")
# Commands whose "Usage:" description line is not strict YAML. Claude Code
# reads them leniently; they are warnings, not failures.
PRE = {'compost', 'finalize', 'fttcp', 'run-pipeline', 'run-quarterly', 'step1'}
MODELS = {'claude-opus-5-5', 'claude-sonnet-5-5', 'haiku'}
EFFORTS = {'low', 'medium', 'high', 'xhigh', 'max'}
fails, warns, n = [], [], 0
files = sorted(glob.glob('.claude/agents/*.md') + glob.glob('.claude/commands/*.md')
               + glob.glob('.claude/skills/*/SKILL.md'))
for f in files:
    n += 1
    m = re.match(r'---\n(.*?)\n---\n', open(f, encoding='utf-8').read(), re.S)
    if not m:
        fails.append(f'{f}: no frontmatter'); continue
    try:
        d = yaml.safe_load(m.group(1)) or {}
    except Exception as e:
        d = {}
        for line in m.group(1).split('\n'):
            if ':' in line and not line.startswith(' '):
                k, v = line.split(':', 1); d[k.strip()] = v.strip()
        msg = f'{f}: strict YAML: ' + str(e).split('\n')[0]
        (warns if f.split('/')[-1][:-3] in PRE else fails).append(msg)
    if '/agents/' in f:
        if d.get('model') not in MODELS: fails.append(f'{f}: model {d.get("model")}')
        if 'effort' in d and d['effort'] not in EFFORTS: fails.append(f'{f}: effort {d["effort"]}')
        if d.get('model') == 'haiku' and 'effort' in d: fails.append(f'{f}: effort set on haiku')
        for k in ('name', 'description', 'tools'):
            if not d.get(k): fails.append(f'{f}: missing {k}')
    elif '/commands/' in f:
        if not d.get('description'): fails.append(f'{f}: missing description')
        if 'model' in d: fails.append(f'{f}: command pins a model')
    elif not d.get('name') or not d.get('description'):
        fails.append(f'{f}: skill missing name or description')
pr = 0
for f in sorted(glob.glob('prompts/*.md') + glob.glob('.claude/skills/section-1b/references/*.md')):
    pr += 1
    try: open(f, encoding='utf-8').read()
    except Exception: fails.append(f'{f}: not UTF-8')
print(f'  frontmatter files: {n}; prompt and reference files read: {pr}')
for w in warns: print('  warn (pre-existing):', w)
for x in fails: print('  FAIL:', x)
sys.exit(1 if fails else 0)
EOF
}

check2() {
REF_RUN="$REF_RUN" python3 - <<'EOF'
import collections, glob, os, re, sys
RUN = os.environ['REF_RUN']
# Paths the instructions name but no reference run holds by design: Phase 2
# and 3 outputs written later, operator files, quarterly intermediates, and
# the screen list the collector reads on the operator's machine.
EXPECTED = [r'fttcp-', r'notion-payload\.md$', r'provenance\.yaml$', r'expectation-ledger\.md$',
            r'operator-notes\.md$', r'fulltext\.md$', r'structured\.md$', r'companies\.txt$']
files = sorted(glob.glob('.claude/agents/*.md') + glob.glob('.claude/commands/*.md')
               + glob.glob('.claude/skills/**/*.md', recursive=True) + glob.glob('prompts/*.md'))
pat = re.compile(r'(?<![\w/.<{-])((?:\.claude|frameworks|prompts|tools|audits|companies|runs|outputs|inputs|verifiers|canary|screens|data)/[\w./<>{}*-]+|[\w.-]+\.(?:md|py|sh|yaml|yml|txt|json))')
BASES = ['frameworks', 'prompts', '.claude/agents', '.claude/commands', '.claude/hooks', 'tools',
         'tools/collector', '.claude/skills/section-1b', '.claude/skills/section-1b/references',
         'verifiers', '.']
refs = collections.defaultdict(list)
for f in files:
    for i, line in enumerate(open(f, encoding='utf-8'), 1):
        for m in pat.finditer(line):
            refs[m.group(1).rstrip('.,;:)`\'"')].append(f'{f}:{i}')
def missing(p):
    if re.search(r'[<>{}*]', p):
        if p.startswith('runs/') and '/' in p[5:]:
            tail = re.sub(r'^runs/[^/]+/', '', p)
            return not re.search(r'[<>{}*]', tail) and not os.path.exists(os.path.join(RUN, tail))
        return False
    if p.startswith(('outputs/', 'inputs/')): return not os.path.exists(os.path.join(RUN, p))
    if os.path.exists(p): return False
    if p.startswith('references/'): return not os.path.exists('.claude/skills/section-1b/' + p)
    if '/' not in p:
        if any(os.path.exists(os.path.join(b, p)) for b in BASES): return False
        return not glob.glob(os.path.join(RUN, '**', p), recursive=True)
    return True
bad, expected = [], 0
for p, locs in sorted(refs.items()):
    if not missing(p): continue
    if any(re.search(e, p) for e in EXPECTED): expected += 1; continue
    bad.append(f'{p}  ({locs[0]}{" +%d" % (len(locs) - 1) if len(locs) > 1 else ""})')
print(f'  distinct paths: {len(refs)}; expected absences: {expected}; unresolved: {len(bad)}')
for b in bad: print('  FAIL:', b)
sys.exit(1 if bad else 0)
EOF
}

check3() {
  if [ -n "$(git status --short)" ]; then
    echo "  FAIL: working tree not clean; commit first, then re-run check 3"; return 1
  fi
  if [ "$(git config --get core.sparseCheckout)" = "true" ]; then
    echo "  FAIL: tree is already sparse; run tools/sparse_session.sh --off first"; return 1
  fi
  local rc=0
  tools/sparse_session.sh "$REF_RUN" | tail -1 | sed 's/^/  sparse tree: /'
  REF_RUN="$REF_RUN" python3 - <<'EOF' || rc=1
import glob, os, re, sys
RUN = os.environ['REF_RUN']
CMDS = {'/run-pipeline': ['.claude/commands/run-pipeline.md', 'prompts/00-orchestrator.md'],
        '/fttcp': ['.claude/commands/fttcp.md'],
        '/finalize': ['.claude/commands/finalize.md'],
        '/run-quarterly': ['.claude/commands/run-quarterly.md', 'prompts/quarterly-00-orchestrator.md']}
pat = re.compile(r'(?<![\w/.<{-])((?:\.claude|frameworks|prompts|tools|audits|companies|runs|outputs|inputs|verifiers)/[\w./<>{}*-]+)')
fail = False
for cmd, fs in CMDS.items():
    miss = set()
    for f in fs:
        for i, line in enumerate(open(f, encoding='utf-8'), 1):
            for m in pat.finditer(line):
                p = m.group(1).rstrip('.,;:)`\'"')
                if p.startswith('runs/') and not p.startswith('runs/_template'):
                    tail = re.sub(r'^runs/[^/]+/', '', p)
                    if re.search(r'[<>{}*]', tail): continue
                    p = os.path.join(RUN, tail)
                elif re.search(r'[<>{}*]', p): continue
                if p.startswith(('outputs/', 'inputs/')): p = os.path.join(RUN, p)
                if not os.path.exists(p) and not glob.glob(p): miss.add(f'{p} ({f}:{i})')
    fail = fail or bool(miss)
    print(f'  {cmd}: ' + ('all paths on disk' if not miss else f'{len(miss)} missing'))
    for x in sorted(miss): print('    missing:', x)
tpl = 'runs/_template/outputs/expectation-ledger.md'
print(f'  {tpl}: ' + ('present' if os.path.exists(tpl) else 'MISSING'))
fail = fail or not os.path.exists(tpl)
print(f'  session-cost.md files: {len(glob.glob("runs/*/session-cost.md"))}; '
      f'manifests: {len(glob.glob("runs/*/manifest.yaml"))}; companies: {len(glob.glob("companies/*.md"))}')
sys.exit(1 if fail else 0)
EOF
  tools/sparse_session.sh --off >/dev/null
  local disk tracked
  disk=$(find runs -type f | wc -l); tracked=$(git ls-files runs | wc -l)
  echo "  after --off: $disk files on disk under runs/, $tracked tracked"
  [ "$disk" -eq "$tracked" ] || { echo "  FAIL: full tree not restored"; rc=1; }
  [ -z "$(git status --short)" ] || { echo "  FAIL: git status not clean after --off"; rc=1; }
  return $rc
}

check4() {
  local rc=0
  grep -q "^## 7A. RESUME FROM DISK" prompts/00-orchestrator.md \
    || { echo "  FAIL: orchestrator section 7A missing"; rc=1; }
  grep -q "to DISK and not only" .claude/commands/fttcp.md \
    || { echo "  FAIL: fttcp disk-write rule missing"; rc=1; }
  grep -q "^6\. \*\*MANAGEMENT VISION AND ACTION" .claude/commands/fttcp.md \
    || { echo "  FAIL: fttcp part 6 missing"; rc=1; }
  if command -v claude >/dev/null; then
    claude plugin validate tools/mods/token-meter >/dev/null 2>&1 \
      && echo "  token-meter: validate ok" || { echo "  FAIL: token-meter validate"; rc=1; }
    claude plugin test tools/mods/token-meter 2>&1 | tail -1 | sed 's/^/  token-meter test: /'
    claude plugin test tools/mods/token-meter >/dev/null 2>&1 || { echo "  FAIL: token-meter tests"; rc=1; }
  else
    echo "  FAIL: claude CLI not on PATH; token-meter not checked"; rc=1
  fi
  return $rc
}

overall=0
for c in "${CHECKS[@]}"; do
  echo "Check $c"
  if "check$c"; then RESULT[$c]=PASS; else RESULT[$c]=FAIL; overall=1; fi
done
echo
for c in "${CHECKS[@]}"; do echo "Check $c: ${RESULT[$c]}"; done
exit $overall
