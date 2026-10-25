"""make_captions.py - writes captions.txt (long) and captions_short.txt for compliance_sweep.py from the caption pages that are actually burned in
(out/timeline_*.json), plus the on-screen labels that carry a figure.
Why labels are included: the sweep's required fact strings (116.72, 27 lakh, 67, 35% ...) appear only on screen; the narration speaks them in words.
Speech-bubble text and other labels without a figure are not in the swept file; scan_labels.py scans ALL visual labels for the banned words separately."""
import json, pathlib, re
import script as S
HERE = pathlib.Path(__file__).resolve().parent
def write(fmt, scenes, out):
    T = json.loads((HERE / "out" / f"timeline_{fmt}.json").read_text()); lines = ["# CAPTIONS (burned-in, = narration), one page per line"]
    for c in T["captions"]: lines.append(" ".join(c["lines"]))
    lines.append("# ON-SCREEN LABELS THAT CARRY A FIGURE")
    for sc in scenes:
        for lab in sc[4]:
            if re.search(r"\d", lab): lines.append(lab)
    (HERE / out).write_text("\n".join(lines) + "\n", encoding="utf-8"); print("wrote", out, len(lines), "lines")
write("long", S.SCENES, "captions.txt"); write("short", S.SHORT_SCENES, "captions_short.txt")
