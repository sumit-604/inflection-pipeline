"""synth.py - Kokoro TTS (kokoro-onnx), voice af_heart at speed 1.05, one WAV per sentence.
Usage: python synth.py            (long video  -> wav/)
       python synth.py short      (the Short   -> wav_short/)
Pronunciations: the job's respellings are sent to the engine as phoneme overrides (the same IPA-override
method earlier videos used); captions keep the normal spelling because they come from script.py, not from here.
  Keerti KEER-tee | Sharma SHAR-maa | Hormuz hor-MOOZ | Houthis HOO-thees | Khamenei kha-meh-NAY
  Netanyahu net-an-YAH-hoo | Yanbu YAN-boo | rial(s) ree-AHL(S) | lakh laakh | LNG L N G | LPG L P G"""
import hashlib, json, pathlib, re, sys
import numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
import script as S

HERE = pathlib.Path(__file__).resolve().parent
ASSETS = HERE / "assets"
VOICE, SPEED, LANG = "af_heart", 1.05, "en-us"

IPA = {
 "keerti": "kˈiːɾti", "sharma's": "ʃˈɑːɾmɑːz", "sharma": "ʃˈɑːɾmɑː",
 "hormuz": "hɔːɹmˈuːz", "houthis": "hˈuːθiːz", "khamenei": "kɑːmɛnˈeɪ", "netanyahu": "nɛtɐnjˈɑːhuː",
 "yanbu": "jˈænbuː", "rial": "ɹiːˈɑːl", "rials": "ɹiːˈɑːlz", "lakh": "lˈɑːk",
}
LETTERS = {"L": "ˈɛl", "N": "ˈɛn", "G": "dʒˈiː", "P": "pˈiː"}
OVERRIDE_RE = re.compile(r"(?<![\w'])(Keerti|Sharma's|Sharma|Hormuz|Houthis|Khamenei|Netanyahu|Yanbu|rials|rial|lakh|LNG|LPG)(?![\w'])", re.I)

# Years are written as digits in the captions; the voice gets the spoken form (otherwise it says "two thousand and ...").
YEARS = {"2015": "twenty fifteen", "2018": "twenty eighteen", "2025": "twenty twenty-five", "2026": "twenty twenty-six", "2029": "twenty twenty-nine"}

def spoken_form(text):
    return re.sub(r"\b(20\d\d)\b", lambda m: YEARS[m.group(1)], text)

def split_sentences(text):
    return [s for s in re.split(r"(?<=[.?!])\s+(?=[A-Z])", text.strip()) if s]

def to_phonemes(k, text, lang=LANG):
    text = spoken_form(text)
    out, pos = [], 0
    def plain(seg):
        seg = seg.strip()
        if seg: out.append(k.tokenizer.phonemize(seg, lang))
    for m in OVERRIDE_RE.finditer(text):
        plain(text[pos:m.start()])
        w = m.group(1)
        if w.lower() in IPA: out.append(IPA[w.lower()])
        else: out.append(" ".join(LETTERS[c] for c in w.upper()))
        pos = m.end()
    plain(text[pos:])
    return " ".join(out)

def trim(a, sr, thr=0.004, keep=0.02):
    idx = np.where(np.abs(a) > thr)[0]
    if len(idx) == 0: return a
    return a[max(0, idx[0] - int(keep * sr)): min(len(a), idx[-1] + int(keep * sr))]

def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "long"
    scenes = S.SHORT_SCENES if which == "short" else S.SCENES
    wavdir = HERE / ("wav_short" if which == "short" else "wav"); wavdir.mkdir(exist_ok=True)
    k = Kokoro(str(ASSETS / "kokoro-v1.0.onnx"), str(ASSETS / "voices-v1.0.bin"))
    man, path = {}, wavdir / "manifest.json"
    if path.exists(): man = json.loads(path.read_text())
    for sc in scenes:
        sid, text = sc[0], sc[3]
        for pi, sent in enumerate(split_sentences(text)):
            name = f"s{sid:02d}_p{pi}"
            ph = to_phonemes(k, sent)
            key = hashlib.sha1(f"{VOICE}|{SPEED}|{ph}".encode()).hexdigest()
            wav = wavdir / (name + ".wav")
            if not (wav.exists() and man.get(name, {}).get("key") == key):
                a, sr = k.create(ph, VOICE, speed=SPEED, lang=LANG, is_phonemes=True)
                a = trim(a.astype(np.float32), sr)
                sf.write(wav, a, sr)
                print("synth", name, f"{len(a)/sr:.2f}s", sent[:60])
            a, sr = sf.read(wav)
            man[name] = {"key": key, "dur": len(a) / sr, "text": sent, "phonemes": ph, "scene": sid, "part": pi}
    path.write_text(json.dumps(man, indent=1, ensure_ascii=False))
    print(f"{len(man)} sentence WAVs, {sum(v['dur'] for v in man.values()):.1f}s of speech in total")

if __name__ == "__main__":
    main()
