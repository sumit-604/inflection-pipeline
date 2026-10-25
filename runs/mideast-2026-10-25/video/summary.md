# mideast video 2026-10-25: summary

## Why it stopped
The finish line was reached. In round 3 all six counters read zero for the long video and for the Short. Round 4 re-checked the Short after one small edit. Four rounds in total. The loop did not hit the 5-round limit.

## What is done
| file | length | size | format |
|---|---|---|---|
| mideast-explainer-long.mp4 | 3:15.23 (5857 frames) | 17.7 MB | 1920x1080, 30 fps constant, H.264 yuv420p, AAC 48 kHz |
| mideast-explainer-short.mp4 | 0:36.60 (1098 frames) | 3.1 MB | 1080x1920, 30 fps constant, H.264 yuv420p, AAC 48 kHz |
| mideast-thumbnail.png | | 81 KB | 1280x720 |

- Final counters (see run-log.md): text outside frame 0, text overlap 0, caption and on-screen hold 0, dead air 0 (run on both final MP4s), compliance hits 0, runtime errors 0.
- Loudness on the decoded MP4s: long -14.0 LUFS, true peak -1.4 dBTP. Short -14.0 LUFS, true peak -1.5 dBTP.
- Extra check, not one of the six: text contrast measured on rendered pixels, worst 4.72:1 (limit 4.5:1).
- Frame times checked: every frame step is exactly 1/30 s.
- Captions are the narration word for word. No caption or narration change was forced by a compliance rule, so the change list is empty.
- Year digits (2015, 2018, 2025, 2026, 2029) stay as digits in captions. The voice gets the spoken form ("twenty twenty-nine"). Without this the voice said "two thousand".

## What is still failing, or not as the job asked
1. **The Short is 36.6 s, not about 55 s.** Scene length comes from the narration plus 0.4 s, and the six Short lines are short. I did not pad it. Longer narration is needed to reach 55 s.
2. **The video manual was not found.** youtube-video-manual-v2-0 is not in the repo (I searched main, the kissht, trualt and capillary video branches, and all remote branch file lists). I followed the job text only.
3. **The kissht and trualt branches hold no video programs.** I reused the capillary programs from main (synth.py with its phoneme-override method, the render and mux approach, the timeline idea). The video page, counters, captions solver, audio mix and scenes are new.
4. **No music bed.** No music file exists in the repo. Earlier videos used generated tones only. This video has narration plus small generated sound effects (pop, tick, ping, whoosh), each placed one frame after its visual event.
5. **I could not listen to the voice.** I checked the speech with a speech-to-text pass: 93.7% of narration words match. The misses are numerals, "Keerti" (a name the model does not know), "rials" heard as "reals", and one "Hormuz" heard as "hormones". A person must listen at the times in `pronunciation-check.md`. Yanbu, Khamenei, Netanyahu, LNG and LPG are never spoken, so only the other respellings apply.
6. **Caption timing is not exactly on the speech.** Narration runs about 0.3 s per word, and the hold rule needs 0.3 s per word plus 0.5 s per page. Pages therefore start up to 0.7 s early or 0.85 s late. In long scenes 7, 10 and 11 and in Short scenes 1 and 2 the last caption page stays up to 1 s into the next scene.
7. **The compliance sweep file is built, not raw.** The sweep needs "116.72", "27 lakh", "67" and others. The narration only says these in words. `captions.txt` therefore holds the burned-in caption pages plus the on-screen labels that carry a figure. The speech-bubble line "Our right to enrich" is not in that file. `scan_labels.py` scans every label: the only banned-word hit is that "Our", which the job allows in on-screen text. The Short sweep (`compliance_sweep_short.py`) checks only 90% and 70%, the facts the Short uses.
8. **Accent colour.** #F08A4B on the teal, olive, plum and slate backgrounds is only 3.9:1 or less. I put those numbers on dark cards so contrast passes 4.5:1. Nothing else about the colour rotation changed.
9. **Fonts.** Archivo and IBM Plex Sans are the Google Fonts files, saved locally and loaded with display=block. No network is used at render time.
10. **Not machine-checked:** the hero-move rules (one hero move per shot, secondary moves 50 to 70% as far, 100 to 200 ms later). I designed the scenes to follow them. No counter measures them.
11. **Facts.** Every number comes from the job's fact sheet. I did not verify the events behind them.

## Choices worth a look
- Scene 2 shows the three gauge labels (5% power plant fuel, 60% Iran reached here, 90% bomb grade) but not the one-line summary from the job.
- Scene 3 has six dots for six sentences. The dot for "Iran then pushed enrichment higher" has an up arrow and no label, as the job lists five labels.
- The Brent counter in scene 5 counts up from $0.00 to $116.72. The values on the way are not claims.
- Extra on-screen words not in the job: map labels (Iran, Strait of Hormuz, Red Sea, Bab al-Mandab, Saudi Arabia, Yemen, Yanbu, India, Europe), "3 Jan: new Congress" and "window" in scene 9, and two date chips in scene 12.
- The Short has no disclaimer line, because the job gives none for it.
- Banned items: the first render used none that I found. The price counter changes its text for 1.7 s, as the job asked.
- A bug the counters missed: the first frame of each scene showed the previous scene. A boundary check now sits in counter 6.

## Total rounds
4 (see run-log.md).

## The one change that would make the next video cheaper
Keep this folder as a shared video kit in the repo (framework, counters, caption solver, audio steps, check scripts) next to the video manual. The next video would then only need a new script and scenes.
