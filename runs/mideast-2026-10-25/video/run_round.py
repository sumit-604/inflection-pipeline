"""run_round.py <round> "<what changed>" - one round of the loop: timeline -> counters -> audio -> draft render -> dead air -> compliance -> stills.
Appends one line to run-log.md with the six counter values (long | short). Final renders are made by build_final.sh only after a round reads all zeros."""
import json, pathlib, subprocess, sys, time
HERE = pathlib.Path(__file__).resolve().parent; OUT = HERE / "out"
def sh(cmd, check=False):
    r = subprocess.run(cmd, shell=True, cwd=HERE, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr)
def main():
    rnd, note = sys.argv[1], sys.argv[2]; t0 = time.time(); res = {}
    sh("python3 assemble.py build long && python3 assemble.py build short && python3 make_captions.py")
    for fmt in ("long", "short"):
        rc, out = sh(f"python3 counters.py {fmt} --sfx"); print(out)
        c = json.loads((OUT / f"counters_{fmt}.json").read_text()); res[fmt] = dict(c)
        sh(f"python3 assemble.py mix {fmt} && python3 audio_final.py norm {fmt}")
        t = time.time(); fd = f"frames_draft_{fmt}"; sh(f"rm -rf {fd}; mkdir -p {fd}")
        rc, o = sh(f"python3 render.py frames {fmt} 4 1 {fd}"); print(o.strip().splitlines()[-1])
        rc, o = sh(f"python3 render.py mux {fmt} out/audio_{fmt}_norm.wav out/draft_{fmt}.mp4 {fd}"); 
        if rc: res[fmt]["errors"] += 1; print("mux error", o[-300:])
        rc, o = sh(f"python3 deadair_check.py out/draft_{fmt}.mp4"); print(o.strip()); res[fmt]["deadair"] = int(o.strip().splitlines()[-1].split(":")[1])
        sw = "compliance_sweep.py captions.txt" if fmt == "long" else "compliance_sweep_short.py captions_short.txt"
        rc, o = sh(f"python3 {sw}"); print(o.strip()); res[fmt]["compliance"] = int(o.strip().splitlines()[-1].split(":")[1])
        rc, o = sh(f"python3 contrast.py {fmt} {10 if fmt == 'long' else 5}"); print(o.strip().splitlines()[0]); res[fmt]["contrast_fail"] = 0 if rc == 0 else 1
        sh(f"rm -rf {fd}")
    sh("python3 render.py firsts long; python3 render.py sheet long 24; python3 render.py firsts short; python3 render.py sheet short 12")
    f = lambda r: f"outside={r['outside']} overlap={r['overlap']} caption_hold={r['hold']} deadair={r['deadair']} compliance={r['compliance']} errors={r['errors']}"
    line = f"| {rnd} | {note} | LONG {f(res['long'])} | SHORT {f(res['short'])} | contrast fails long/short {res['long']['contrast_fail']}/{res['short']['contrast_fail']} |"
    log = HERE / "run-log.md"
    if not log.exists(): log.write_text("# Run log (one line per round; six counters: text outside frame, text overlap, caption/on-screen hold, dead air, compliance hits, runtime errors)\n\n| round | what changed | long video | Short | extra |\n|---|---|---|---|---|\n")
    with open(log, "a") as fh: fh.write(line + "\n")
    print(line); print(f"round took {time.time() - t0:.0f}s")
if __name__ == "__main__": main()
