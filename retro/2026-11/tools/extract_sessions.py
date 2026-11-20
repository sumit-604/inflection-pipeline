#!/usr/bin/env python3
"""Pull per-company excerpts out of Claude Code session history.

Reads every .jsonl under ~/.claude/projects (or --projects DIR). Keeps only
user-typed and assistant-written text: tool calls, tool results, thinking and
attachments are skipped. Each session is tagged with its first timestamp and
its project folder. A paragraph is saved for a company when it names the
company (alias match) AND mentions one of the topics: results, guidance,
margin, delay, order book, miss.

Usage:
  python extract_sessions.py --aliases aliases.json --out session_excerpts
  aliases.json = {"TICKER": ["alias one", "ALIAS2", ...], ...}
    - aliases written in ALL CAPS are matched case-sensitively as whole words
      (use this for short tickers such as LT, AYE, IKS);
    - other aliases are matched case-insensitively as whole words.
Outputs:
  <out>/<TICKER>.md         excerpts, grouped by session
  <out>/_sessions.tsv       one line per session read (date, folder, file, msgs, hits)
  <out>/_summary.json       counts
No transcript text is printed to stdout.
"""
import argparse, json, os, re, sys, collections

TOPIC = re.compile(
    r"\b(results?|guidance|guided|guide[sd]?|margins?|delay(ed|s)?|defer(red|ral)?|slip(ped|page)?|"
    r"order\s*book|order\s*inflow|backlog|miss(ed|es)?|shortfall|below\s+(our|base|estimate)|"
    r"beat|in[- ]line|base[- ]case|q[1-4]\s*fy\s*2?[67]|h[12]\s*fy\s*2?[67]|ebitda|pat)\b", re.I)
MAX_PARA = 900          # characters kept per paragraph
MAX_PER_SESSION = 12    # paragraphs per company per session
MAX_PER_COMPANY = 150   # paragraphs per company overall


def texts(obj):
    """Yield (role, text) for user/assistant text blocks only."""
    t = obj.get("type")
    if t not in ("user", "assistant"):
        return
    if obj.get("isMeta") or obj.get("isCompactSummary"):
        return
    msg = obj.get("message") or {}
    c = msg.get("content")
    if isinstance(c, str):
        yield t, c
    elif isinstance(c, list):
        for b in c:
            if isinstance(b, dict) and b.get("type") == "text" and b.get("text"):
                yield t, b["text"]
            # tool_use, tool_result, thinking, image: skipped on purpose


def compile_aliases(aliases):
    out = {}
    for tk, al in aliases.items():
        pats = []
        for a in set(al):
            a = a.strip()
            if len(a) < 2:
                continue
            if a.isupper() or re.fullmatch(r"[A-Z0-9&\-]+", a):
                pats.append(re.compile(r"(?<![A-Za-z0-9])" + re.escape(a) + r"(?![A-Za-z0-9])"))
            else:
                pats.append(re.compile(r"(?<![A-Za-z0-9])" + re.escape(a) + r"(?![A-Za-z0-9])", re.I))
        out[tk] = pats
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--projects", default=os.path.join(os.path.expanduser("~"), ".claude", "projects"))
    ap.add_argument("--aliases", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    pats = compile_aliases(json.load(open(a.aliases, encoding="utf-8")))
    os.makedirs(a.out, exist_ok=True)
    hits = collections.defaultdict(list)      # ticker -> [(date, folder, file, role, para)]
    seen = collections.defaultdict(set)
    sessions = []
    nfiles = 0
    for root, dirs, files in os.walk(a.projects, onerror=lambda e: None):
        for fn in files:
            if not fn.endswith(".jsonl"):
                continue
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, a.projects)
            folder = rel.split(os.sep)[0]
            nfiles += 1
            date, nmsg, nhit = "", 0, 0
            per = collections.Counter()
            try:
                fh = open(path, encoding="utf-8", errors="replace")
            except OSError:
                continue
            with fh:
                for line in fh:
                    if '"type":"user"' not in line and '"type":"assistant"' not in line \
                       and '"type": "user"' not in line and '"type": "assistant"' not in line:
                        continue
                    try:
                        o = json.loads(line)
                    except Exception:
                        continue
                    if not date and o.get("timestamp"):
                        date = o["timestamp"][:10]
                    for role, text in texts(o):
                        nmsg += 1
                        if text.lstrip().startswith(("<system-reminder", "<command-", "<local-command", "<task-notification")):
                            continue
                        for para in re.split(r"\n\s*\n", text):
                            p = para.strip()
                            if len(p) < 25 or not TOPIC.search(p):
                                continue
                            for tk, pl in pats.items():
                                if per[tk] >= MAX_PER_SESSION or len(hits[tk]) >= MAX_PER_COMPANY:
                                    continue
                                if any(x.search(p) for x in pl):
                                    key = p[:200]
                                    if key in seen[tk]:
                                        continue
                                    seen[tk].add(key)
                                    hits[tk].append((date or o.get("timestamp", "")[:10], folder, rel, role, p[:MAX_PARA]))
                                    per[tk] += 1
                                    nhit += 1
            sessions.append((date, folder, rel, nmsg, nhit))
    for tk, rows in hits.items():
        rows.sort()
        with open(os.path.join(a.out, f"{tk}.md"), "w", encoding="utf-8") as f:
            f.write(f"# {tk} - session-history excerpts\n\n")
            last = None
            for date, folder, rel, role, p in rows:
                if rel != last:
                    f.write(f"\n## {date} | {folder}\nfile: {rel}\n\n")
                    last = rel
                f.write(f"- [{role}] " + p.replace("\n", "\n  ") + "\n\n")
    with open(os.path.join(a.out, "_sessions.tsv"), "w", encoding="utf-8") as f:
        f.write("date\tfolder\tfile\ttext_messages\thits\n")
        for s in sorted(sessions):
            f.write("\t".join(map(str, s)) + "\n")
    summ = {"jsonl_files": nfiles,
            "sessions_with_text": sum(1 for s in sessions if s[3]),
            "sessions_with_hits": sum(1 for s in sessions if s[4]),
            "companies_with_excerpts": len(hits),
            "excerpts": sum(len(v) for v in hits.values())}
    json.dump(summ, open(os.path.join(a.out, "_summary.json"), "w"), indent=1)
    print(json.dumps(summ))


if __name__ == "__main__":
    main()
