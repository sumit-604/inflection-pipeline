#!/usr/bin/env bash
# Full build for the Capillary video. Run from this folder. Needs ffmpeg, Playwright Chromium, pip: kokoro-onnx soundfile scipy pillow.
set -euo pipefail
python3 fetch_assets.py                 # Kokoro model + fonts into ./assets
python3 fill_scene11.py                 # scene 11 values from scenario-rebuild-page64.md (stops on a mismatch)
python3 compliance_sweep.py script.py video.html
python3 compliance_sweep.py shorts.py video.html
python3 synth.py                        # one WAV per sentence (wav/)
python3 synth.py shorts.py wav_shorts   # Short hooks and end lines
python3 assemble.py                     # timeline.js, out/audio.wav, out/listen_times.json
python3 render.py frames 4              # frames/
mkdir -p out/final
python3 render.py mux out/final/capillary-bd06.mp4
python3 make_xclip.py out/final/capillary-bd06.mp4 out/final/capillary-x-clip.mp4
python3 thumbnail.py out/final/capillary-thumbnail-A.png
python3 shorts_build.py out/final/capillary-bd06.mp4 out/final
python3 render.py contact && cp out/contact-sheet.png out/final/
python3 deadair_check.py out/final/*.mp4
