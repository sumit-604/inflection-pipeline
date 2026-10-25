"""scan_labels.py - runs the compliance_sweep banned patterns over EVERY on-screen label and over every narration line (not just the swept file)."""
import re, sys
import script as S
banned = [r"\bI\b", r"\bI'm\b", r"\bwe\b", r"\bwe're\b", r"\bour\b", r"\byou\b", r"\byour\b", r"\bbuy\b", r"\bsell\b", r"target price", r"\bsynthetic\b", r"\bAI voice\b", r"\bguaranteed\b"]
hits = []
for name, scenes in (("long", S.SCENES), ("short", S.SHORT_SCENES)):
    for sc in scenes:
        for kind, txt in [("narration", sc[3])] + [("label", l) for l in sc[4]]:
            for p in banned:
                if re.search(p, txt, re.I): hits.append((name, sc[0], kind, p, txt))
for h in hits: print("HIT", h)
nar = [h for h in hits if h[2] == "narration"]
print(f"banned hits in narration: {len(nar)}; in on-screen labels: {len(hits) - len(nar)} (only 'Our' inside on-screen text is allowed by the job)")
sys.exit(1 if nar or any(h[3] != r"\bour\b" for h in hits) else 0)
