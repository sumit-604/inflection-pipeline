"""
holdings_table.py — the holdings price table that opens REVIEW.md.

Inputs in <run>/deep/:
  out/*.md       analysts' DATA blocks; each in-master company carries a
                 `levels: {json}` line copied from Notion (see COMPANY_ANALYST.md)
  prices.json    this run's prices (refresh_prices.py)
  review_spec/price_history.json   earlier runs' prices (the "last run" baseline)

Output: <run>/deep/assembly/holdings.md   (stitch_review.py puts it at the top)

A holding is a company whose levels line says "held": true.
Crossing rules, between the last run's price and this run's price:
  stop and exit lines: crossed when the price falls to or through the line
  trim steps:          crossed when the price rises to or through the step
A crossing is shown in bold. With no earlier screener reading, the baseline is
the Notion on-file price, and the table says so. A price that was not
refreshed is never tested: the Notion price is shown and marked STALE.

Usage: python holdings_table.py "<run folder>"
"""

import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
HISTORY_FILE = os.path.join(ROOT, "review_spec", "price_history.json")
LEVELS = re.compile(r"^levels:\s*(\{.*\})\s*$", re.M)


def load(path, default):
    try:
        return json.load(open(path, encoding="utf-8"))
    except (OSError, ValueError):
        return default


def nums(v):
    """A level field as a list of numbers (null, one number or a list)."""
    if v is None:
        return []
    vals = v if isinstance(v, list) else [v]
    out = []
    for x in vals:
        try:
            out.append(float(str(x).replace(",", "")))
        except ValueError:
            pass
    return out


def money(v):
    return "" if v is None else f"₹{v:,.2f}".rstrip("0").rstrip(".")


def levels_by_company(run):
    found, bad = {}, []
    for path in sorted(glob.glob(os.path.join(run, "deep", "out", "*.md"))):
        for raw in LEVELS.findall(open(path, encoding="utf-8").read()):
            try:
                lv = json.loads(raw)
                found[lv["company"]] = lv
            except (ValueError, KeyError):
                bad.append(f"{os.path.basename(path)}: {raw[:60]}")
    return found, bad


def baseline(name, run_name, lv, hist):
    earlier = [h for h in hist.get(name, []) if h.get("run") != run_name]
    if earlier:
        h = earlier[-1]
        return h["price"], f"{h['source']} {h['read_at'][:16]}"
    if lv.get("onfile_price") is not None:
        p = nums(lv["onfile_price"])
        if p:
            return p[0], f"Notion on file {lv.get('onfile_date') or 'undated'}"
    return None, "no earlier price"


def crossings(prev, cur, lv, since_text="since last run"):
    """(bold flags, plain notes) for every stop, trim and exit level."""
    flags, notes = [], []
    for kind, down in (("stop", True), ("exit", True), ("trim", False)):
        for x in nums(lv.get(kind)):
            beyond_now = cur <= x if down else cur >= x
            if not beyond_now:
                if prev is not None and (prev <= x if down else prev >= x):
                    notes.append(f"back {'above' if down else 'below'} {kind} {money(x)}")
                continue
            word = "below" if down else "above"
            if prev is None:
                flags.append(f"{word} {kind} {money(x)} (no earlier price to date the cross)")
            elif (prev > x) if down else (prev < x):
                flags.append(f"CROSSED {kind} {money(x)} {since_text}")
            else:
                notes.append(f"still {word} {kind} {money(x)}")
    return flags, notes


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    run = os.path.abspath(sys.argv[1])
    run_name = os.path.basename(run)
    lv_all, bad = levels_by_company(run)
    prices = {p["company"]: p for p in load(os.path.join(run, "deep", "prices.json"), [])}
    hist = load(HISTORY_FILE, {})

    held = sorted((lv for lv in lv_all.values() if lv.get("held") is True),
                  key=lambda lv: lv["company"].lower())
    rows, n_flag, n_stale = [], 0, 0
    for lv in held:
        name = lv["company"]
        p = prices.get(name, {})
        if p.get("status") == "OK":
            cur = p["price"]
            price_cell = f"{money(cur)}<br>{p['source']}, {p['read_at'][:16]}"
            prev, base = baseline(name, run_name, lv, hist)
            # First screener reading: the cross is dated from the Notion price, not a run.
            since_text = (f"since {base}" if base.startswith("Notion") else "since last run")
            flags, notes = crossings(prev, cur, lv, since_text)
            since = f"{money(prev)} ({base})" if prev is not None else base
        else:
            n_stale += 1
            onfile = nums(lv.get("onfile_price"))
            why = "; ".join(p.get("errors", [])) or "no price record for this run"
            price_cell = (f"**PRICE NOT REFRESHED** ({why})<br>"
                          + (f"STALE: {money(onfile[0])} Notion on file {lv.get('onfile_date') or 'undated'}"
                             if onfile else "no Notion price on file"))
            flags, notes, since = [], ["levels not tested: no fresh price"], ""
        if flags:
            n_flag += 1
        flag_cell = "<br>".join([f"**{f}**" for f in flags] + notes)
        lv_note = lv.get("note") or ""
        rows.append("| " + " | ".join([
            f"**{name}**" if flags else name,
            price_cell,
            money(nums(lv.get("avg_cost"))[0]) if nums(lv.get("avg_cost")) else "NOT FOUND",
            " / ".join(filter(None, [
                f"entry {money(nums(lv.get('entry_max'))[0])}" if nums(lv.get("entry_max")) else "",
                f"MoS {money(nums(lv.get('mos'))[0])}" if nums(lv.get("mos")) else ""])) or "NOT FOUND",
            ", ".join(money(x) for x in nums(lv.get("stop"))) or "none on file",
            ", ".join(money(x) for x in nums(lv.get("trim"))) or "none on file",
            ", ".join(money(x) for x in nums(lv.get("exit"))) or "none on file",
            since,
            flag_cell or "no line crossed",
            lv_note.replace("|", "/"),
        ]) + " |")

    not_held = sorted(set(lv_all) - {lv["company"] for lv in held})
    out = ["## Holdings price table", "",
           f"Holdings in this run: {len(held)}. Lines crossed since last run (bold): {n_flag}. "
           f"Prices not refreshed: {n_stale}. Prices from screener.in unless the row says otherwise. "
           "Buy price, entry, MoS, stop, trim and exit come from Notion as copied by the analysts. "
           "Stops and exits are tested for a fall through the line, trims for a rise through it.", ""]
    if rows:
        out += ["| Holding | Current price | Buy price | Entry / MoS | Stop | Trim steps | Exit | "
                "Last run price | Since last run | Level notes |",
                "|---|---|---|---|---|---|---|---|---|---|"] + rows
    else:
        out.append("No holdings among today's companies.")
    if bad:
        out += ["", "Levels lines that could not be read: " + "; ".join(bad)]
    out.append("")
    asm = os.path.join(run, "deep", "assembly")
    os.makedirs(asm, exist_ok=True)
    open(os.path.join(asm, "holdings.md"), "w", encoding="utf-8").write("\n".join(out))
    print(f"HOLDINGS: levels_lines={len(lv_all)} held={len(held)} flagged={n_flag} "
          f"stale={n_stale} unreadable={len(bad)} not_held={len(not_held)}")


if __name__ == "__main__":
    main()
