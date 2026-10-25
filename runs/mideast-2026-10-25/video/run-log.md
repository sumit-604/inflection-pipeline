# Run log (one line per round; six counters: text outside frame, text overlap, caption/on-screen hold, dead air, compliance hits, runtime errors)

Pre-round fixes (before the formal loop; counters had been run by hand on early builds): the first counter pass found 1 held-too-briefly text in the long video
("Permit needed", 0.8 s of 1.1 s) and 1 in the Short (the odds line), and the pixel contrast check found 6 text runs at 3.91:1 (#F08A4B on teal, scenes 3 and 10).
All three were fixed before round 1 (earlier sign, earlier odds line, dark cards behind the accent numbers). Round 1 below is the first full draft with drafts rendered.
Looking at the first-frame stills after round 2 found a real bug the counters had missed: the first frame of a scene rendered the previous scene (scene edges were rounded to 4 decimals).
The scene-boundary check was then added to counter 6.

| round | what changed | long video | Short | extra |
|---|---|---|---|---|
| 1 | first full draft: 12 scenes + 6-scene Short, drafts rendered full size | LONG outside=0 overlap=0 caption_hold=0 deadair=0 compliance=0 errors=0 | SHORT outside=0 overlap=0 caption_hold=0 deadair=0 compliance=0 errors=0 | contrast fails long/short 0/0 |
| 2 | scene 10 chart frame from second 0, caption band drawn per page, centred text snapped to whole pixels, kitchen refactor | LONG outside=0 overlap=0 caption_hold=0 deadair=0 compliance=0 errors=0 | SHORT outside=0 overlap=0 caption_hold=0 deadair=0 compliance=0 errors=0 | contrast fails long/short 0/0 |
| 3 | fixed scene-boundary frame bug (first frame of a scene showed the previous scene; edges now whole frames + boundary check in counter 6); caption timing: forward solver, pages no longer cross cuts unless the hold rule forces it | LONG outside=0 overlap=0 caption_hold=0 deadair=0 compliance=0 errors=0 | SHORT outside=0 overlap=0 caption_hold=0 deadair=0 compliance=0 errors=0 | contrast fails long/short 0/0 |
| 4 | Short only: "3 Nov" centred inside its circle, Short re-rendered and re-checked (long video unchanged from round 3, final build run after round 3) | LONG unchanged: all six counters 0 | SHORT outside=0 overlap=0 caption_hold=0 deadair=0 compliance=0 errors=0 | contrast fails short 0 |
