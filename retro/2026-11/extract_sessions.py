#!/usr/bin/env python3
"""Pull per-company results excerpts from Claude Code session history.

Source B of the 2026-11 results census. Reads every .jsonl under the Claude
Code projects folder, keeps only user and assistant TEXT (tool calls, tool
results and thinking are skipped), tags each session with its date and
folder, and writes per-company excerpts where results, guidance, margin,
delay, order book or a miss is discussed.

Nothing is sent anywhere. The script only reads .jsonl files and writes
markdown and CSV under --out.

Usage (Windows):
    python retro\\2026-11\\extract_sessions.py
Usage (any OS, explicit paths):
    python retro/2026-11/extract_sessions.py \\
        --projects-dir ~/.claude/projects \\
        --aliases retro/2026-11/aliases.json \\
        --out retro/2026-11/session_excerpts

Outputs under --out:
    <TICKER>.md      excerpts for that company, oldest session first
    sessions.csv     one row per session: date, folder, file, messages, hits
    summary.txt      counts for sources.md
"""
import argparse
import csv
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent

# A message is kept only when it names a company AND one of these topics.
TOPIC_PATTERNS = [
    r"\bresults?\b", r"\bguidance\b", r"\bguided\b", r"\bmargins?\b",
    r"\bdelay(?:s|ed)?\b", r"\bdeferr?(?:ed|al)\b", r"\bslipp(?:ed|age)\b",
    r"\border[- ]?book\b", r"\border inflow\b", r"\bmiss(?:ed|es)?\b",
    r"\bbeat\b", r"\bshortfall\b", r"\bbelow (?:our )?(?:base|guidance|estimate)",
    r"\bQ4\s?FY\s?26\b", r"\bQ1\s?FY\s?27\b", r"\bQ2\s?FY\s?27\b",
    r"\bH1\s?FY\s?27\b", r"\bH2\s?FY\s?26\b", r"\bFY\s?26\b", r"\bFY\s?27\b",
    r"\bconcall\b", r"\bEBITDA\b", r"\bPAT\b", r"\brevenue\b",
]
TOPIC_RE = re.compile("|".join(TOPIC_PATTERNS), re.IGNORECASE)

WINDOW = 700        # characters kept each side of a company mention
MAX_EXCERPT = 2400  # hard cap per excerpt
MAX_PER_SESSION_PER_TICKER = 12


def default_projects_dir():
    home = os.environ.get("USERPROFILE") or os.path.expanduser("~")
    return Path(home) / ".claude" / "projects"


def load_aliases(path):
    """aliases.json maps TICKER -> list of names or fragments to search."""
    with open(path, encoding="utf-8") as fh:
        raw = json.load(fh)
    compiled = {}
    for ticker, names in raw.items():
        terms = {ticker}
        terms.update(n for n in names if n and len(n) >= 4)
        pattern = "|".join(
            r"(?<![A-Za-z0-9])" + re.escape(t) + r"(?![A-Za-z0-9])"
            for t in sorted(terms, key=len, reverse=True)
        )
        compiled[ticker] = re.compile(pattern, re.IGNORECASE)
    return compiled


def message_text(record):
    """Return (role, text) for a user or assistant text message, else None."""
    role = record.get("type")
    if role not in ("user", "assistant"):
        return None
    if record.get("isMeta") or record.get("isSidechain"):
        return None
    content = (record.get("message") or {}).get("content")
    parts = []
    if isinstance(content, str):
        parts.append(content)
    elif isinstance(content, list):
        for block in content:
            # Only plain text. tool_use, tool_result and thinking are skipped.
            if isinstance(block, dict) and block.get("type") == "text":
                parts.append(block.get("text") or "")
    text = "\n".join(p for p in parts if p).strip()
    if not text:
        return None
    # Skip harness noise that is stored as user text.
    if text.startswith("<system-reminder>") or text.startswith("<command-"):
        return None
    if text.startswith("<local-command-") or text.startswith("Caveat:"):
        return None
    return role, text


def excerpts_for(text, regex):
    """Windows of text around each company mention that also hit a topic."""
    out, last_end = [], -1
    for match in regex.finditer(text):
        start = max(0, match.start() - WINDOW)
        end = min(len(text), match.end() + WINDOW)
        if start < last_end:      # overlaps the previous window
            continue
        chunk = text[start:end]
        if not TOPIC_RE.search(chunk):
            continue
        out.append(chunk[:MAX_EXCERPT].strip())
        last_end = end
    return out


def scan_file(path, aliases):
    """Return (meta, {ticker: [(timestamp, role, excerpt)]})."""
    meta = {"first_ts": "", "cwd": "", "messages": 0, "bad_lines": 0}
    hits = defaultdict(list)
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                meta["bad_lines"] += 1
                continue
            if not isinstance(record, dict):
                continue
            ts = record.get("timestamp") or ""
            if ts and not meta["first_ts"]:
                meta["first_ts"] = ts
            if record.get("cwd") and not meta["cwd"]:
                meta["cwd"] = record["cwd"]
            got = message_text(record)
            if not got:
                continue
            role, text = got
            meta["messages"] += 1
            if not TOPIC_RE.search(text):
                continue
            for ticker, regex in aliases.items():
                if len(hits[ticker]) >= MAX_PER_SESSION_PER_TICKER:
                    continue
                if not regex.search(text):
                    continue
                for chunk in excerpts_for(text, regex):
                    if len(hits[ticker]) >= MAX_PER_SESSION_PER_TICKER:
                        break
                    hits[ticker].append((ts, role, chunk))
    return meta, hits


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--projects-dir", type=Path, default=default_projects_dir())
    parser.add_argument("--aliases", type=Path, default=HERE / "aliases.json")
    parser.add_argument("--out", type=Path, default=HERE / "session_excerpts")
    parser.add_argument("--since", default="2026-04-01",
                        help="skip sessions that start before this date")
    args = parser.parse_args()

    if not args.projects_dir.is_dir():
        sys.exit(f"NOT FOUND: {args.projects_dir} (no Claude Code session history here)")
    aliases = load_aliases(args.aliases)
    args.out.mkdir(parents=True, exist_ok=True)

    files = sorted(args.projects_dir.rglob("*.jsonl"))
    per_ticker = defaultdict(list)
    rows = []
    for path in files:
        folder = path.parent.relative_to(args.projects_dir).as_posix()
        try:
            meta, hits = scan_file(path, aliases)
        except OSError as err:
            rows.append(["", folder, path.name, 0, 0, f"UNREADABLE {err}"])
            continue
        date = meta["first_ts"][:10]
        if date and date < args.since:
            rows.append([date, folder, path.name, meta["messages"], 0, "before --since"])
            continue
        total = sum(len(v) for v in hits.values())
        rows.append([date, folder, path.name, meta["messages"], total,
                     ",".join(sorted(t for t, v in hits.items() if v))])
        for ticker, items in hits.items():
            for ts, role, chunk in items:
                per_ticker[ticker].append((ts or date, folder, path.name, role, chunk))

    for ticker, items in per_ticker.items():
        items.sort(key=lambda item: item[0])
        with open(args.out / f"{ticker}.md", "w", encoding="utf-8") as fh:
            fh.write(f"# {ticker} session excerpts\n\n")
            fh.write("Source: Claude Code session history. User and assistant text only.\n")
            fh.write("These are chat excerpts, not filed evidence.\n\n")
            for ts, folder, name, role, chunk in items:
                fh.write(f"## {ts[:10]} | {role} | {folder}/{name}\n\n")
                fh.write(chunk.replace("\r", "") + "\n\n")

    with open(args.out / "sessions.csv", "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["date", "folder", "file", "text_messages", "excerpts", "tickers_or_note"])
        writer.writerows(sorted(rows))

    summary = (
        f"projects dir: {args.projects_dir}\n"
        f"session files found: {len(files)}\n"
        f"sessions with at least one excerpt: {sum(1 for r in rows if r[4])}\n"
        f"companies with excerpts: {len(per_ticker)}\n"
        f"excerpts written: {sum(len(v) for v in per_ticker.values())}\n"
    )
    (args.out / "summary.txt").write_text(summary, encoding="utf-8")
    print(summary, end="")


if __name__ == "__main__":
    main()
