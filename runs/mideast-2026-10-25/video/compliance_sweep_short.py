import re, sys
text = open(sys.argv[1], encoding="utf-8").read()
banned = [
    r"\bI\b", r"\bI'm\b", r"\bwe\b", r"\bwe're\b", r"\bour\b", r"\byou\b", r"\byour\b",
    r"\bbuy\b", r"\bsell\b", r"target price", r"\bsynthetic\b", r"\bAI voice\b", r"\bguaranteed\b",
]
required = ["90%", "70%"]   # Short: only the facts the Short uses
hits = 0
for pat in banned:
    for m in re.finditer(pat, text, flags=re.IGNORECASE):
        line = text.count("\n", 0, m.start()) + 1
        print(f"BANNED '{m.group(0)}' at line {line}")
        hits += 1
for word in required:
    if word not in text:
        print(f"MISSING required fact text: {word}")
        hits += 1
print(f"compliance hits: {hits}")
sys.exit(1 if hits else 0)
