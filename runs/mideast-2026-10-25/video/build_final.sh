#!/usr/bin/env bash
# Full build for the Middle East explainer. Run from this folder. Needs ffmpeg, Playwright Chromium, pip: kokoro-onnx soundfile scipy pillow shapely numpy.
# Run only after a round of run_round.py has read all zeros.
set -euo pipefail
python3 fetch_assets.py
python3 build_map.py
python3 synth.py && python3 synth.py short
python3 assemble.py build long && python3 assemble.py build short
python3 make_captions.py
python3 counters.py long --sfx && python3 counters.py short --sfx
python3 assemble.py mix long && python3 assemble.py mix short
TP=${TP:--1.5}
python3 audio_final.py norm long $TP && python3 audio_final.py norm short $TP
rm -rf frames frames_short; mkdir -p frames frames_short out/final
python3 render.py frames long 4 1 frames
python3 render.py frames short 4 1 frames_short
python3 render.py mux long out/audio_long_norm.wav out/final/mideast-explainer-long.mp4 frames
python3 render.py mux short out/audio_short_norm.wav out/final/mideast-explainer-short.mp4 frames_short
python3 thumbnail.py out/final/mideast-thumbnail.png
python3 deadair_check.py out/final/mideast-explainer-long.mp4
python3 deadair_check.py out/final/mideast-explainer-short.mp4
python3 compliance_sweep.py captions.txt && python3 compliance_sweep_short.py captions_short.txt
python3 audio_final.py measure out/final/mideast-explainer-long.mp4; python3 audio_final.py measure out/final/mideast-explainer-short.mp4
