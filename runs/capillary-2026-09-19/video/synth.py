"""synth.py - Kokoro TTS (kokoro-onnx, v1.0), one WAV per sentence.
Usage: python synth.py [script.py] [wav_dir]
Voices: Narrator af_heart 1.1 | Meera bf_emma 1.05 | Ramesh am_michael 1.0
Pronunciations are forced with the IPA overrides below (phoneme input, is_phonemes=True)."""
import hashlib, importlib.util, json, pathlib, re, sys
import numpy as np, soundfile as sf
from kokoro_onnx import Kokoro

HERE = pathlib.Path(__file__).resolve().parent
ASSETS = HERE / "assets"
VOICES = {"Narrator": ("af_heart", 1.1, "en-us"), "Meera": ("bf_emma", 1.05, "en-gb"), "Ramesh": ("am_michael", 1.0, "en-us")}

# IPA overrides from the job. NOTE: Kokoro's vocabulary has no 'ɭ', so Bengaluru uses 'l' (reported in the delivery notes).
IPA = {
 "keerti": "kˈiːɾti", "sharma's": "ʃˈʌɾmɑːz", "sharma": "ʃˈʌɾmɑː", "crore": "kɹˈoːɹ", "meera": "mˈiːɾɑː", "ramesh": "ɾəmˈeːʃ",
 "capillary": "kəpˈɪləɹi", "capillary's": "kəpˈɪləɹiz", "aira": "ˈaɪɹə", "kognitiv": "kˈɒɡnɪtɪv",
 "sessionm": "sˈɛʃən ˈɛm", "optum": "ˈɑːptəm", "bengaluru": "bˈeŋɡəluːɾu", "e bit da": "ˈiː bˈɪt dˈɑː",
}
LETTERS = {"A": "ˈeɪ", "E": "ˈiː", "F": "ˈɛf", "G": "dʒˈiː", "I": "ˈaɪ", "K": "kˈeɪ", "M": "ˈɛm", "O": "ˈoʊ", "P": "pˈiː", "S": "ˈɛs", "U": "jˈuː", "Y": "wˈaɪ"}
OVERRIDE_RE = re.compile(r"(?<![\w'])(Keerti|Sharma's|Sharma|crore|Meera|Ramesh|Capillary's|Capillary|aiRA|Kognitiv|SessionM|Optum|Bengaluru|E bit da|(?-i:(?:[A-Z] )+[A-Z]))(?![\w'])", re.I)

def split_sentences(text):
    return [s for s in re.split(r"(?<=[.?!])\s+(?=[A-Z])", text.strip()) if s]

def to_phonemes(k, text, lang):
    out, pos = [], 0
    def plain(seg):
        seg = seg.strip()
        if seg: out.append(k.tokenizer.phonemize(seg, lang))
    for m in OVERRIDE_RE.finditer(text):
        plain(text[pos:m.start()])
        w = m.group(1)
        if w.lower() in IPA: out.append(IPA[w.lower()])
        else: out.append(" ".join(LETTERS[c] for c in w.split()))
        pos = m.end()
    plain(text[pos:])
    return " ".join(out)

def trim(a, sr, thr=0.004, keep=0.02):
    idx = np.where(np.abs(a) > thr)[0]
    if len(idx) == 0: return a
    s, e = max(0, idx[0] - int(keep * sr)), min(len(a), idx[-1] + int(keep * sr))
    return a[s:e]

def load_script(path):
    spec = importlib.util.spec_from_file_location("script", path); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod

def main():
    script = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else HERE / "script.py")
    wavdir = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else HERE / "wav"); wavdir.mkdir(exist_ok=True)
    mod = load_script(script)
    k = Kokoro(str(ASSETS / "kokoro-v1.0.onnx"), str(ASSETS / "voices-v1.0.bin"))
    man, path = {}, wavdir / "manifest.json"
    if path.exists(): man = json.loads(path.read_text())
    for sc in mod.SCENES:
        sid = sc[0]
        for ri, row in enumerate(sc[2]):
            spk = row[0]
            if spk not in VOICES: continue
            voice, speed, lang = VOICES[spk]
            for pi, sent in enumerate(split_sentences(row[2])):
                name = f"s{sid:02d}_r{ri:02d}_p{pi}"
                ph = to_phonemes(k, sent, lang)
                key = hashlib.sha1(f"{voice}|{speed}|{ph}".encode()).hexdigest()
                wav = wavdir / (name + ".wav")
                if not (wav.exists() and man.get(name, {}).get("key") == key):
                    a, sr = k.create(ph, voice, speed=speed, lang=lang, is_phonemes=True)
                    a = trim(a.astype(np.float32), sr)
                    sf.write(wav, a, sr)
                    print("synth", name, f"{len(a)/sr:.2f}s", sent[:60])
                a, sr = sf.read(wav)
                man[name] = {"key": key, "dur": len(a) / sr, "speaker": spk, "text": sent, "phonemes": ph, "scene": sid, "row": ri, "part": pi}
    path.write_text(json.dumps(man, indent=1, ensure_ascii=False))
    tot = sum(v["dur"] for v in man.values())
    print(f"{len(man)} sentence WAVs, {tot:.1f}s of speech in total")

if __name__ == "__main__":
    main()
