"""pronunciation_times.py - where in the final long video each respelled word is spoken, so a person can listen to them.
Writes pronunciation-check.md (time = estimated start of the word, from phoneme-proportional word timing)."""
import json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
T = json.loads((HERE / "out" / "timeline_long.json").read_text())
WORDS = {"Keerti": "KEER-tee", "Sharma": "SHAR-maa", "Sharma's": "SHAR-maa", "Hormuz": "hor-MOOZ", "Houthis": "HOO-thees", "Yanbu": "YAN-boo", "rials": "ree-AHLS", "lakh": "laakh"}
rows = {}
for sc in T["scenes"]:
    for s in sc["sentences"]:
        for w in s["words"]:
            k = re.sub(r"[,.]$", "", w["w"])
            if k in WORDS: rows.setdefault(k, []).append((w["t0"], sc["id"]))
out = ["# Words to listen to (long video)", "", "Respelling sent to the voice engine, then every place the word is spoken (m:ss.s, scene).", "",
       "Not in the narration, so not spoken: Khamenei, Netanyahu, LNG, LPG, Bab al-Mandab (these appear only as text, or not at all).", ""]
for k, v in rows.items():
    out.append(f"- {k} ({WORDS[k]}): " + ", ".join(f"{int(t // 60)}:{t % 60:04.1f} (scene {sc})" for t, sc in v))
(HERE / "pronunciation-check.md").write_text("\n".join(out) + "\n"); print("\n".join(out))
