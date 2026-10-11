"""Shorts: hook and end line text (voiced by synth.py, same voice as the long video) and the picks.
SCENES uses the same row format as script.py so compliance_sweep.py can run on this file too.
picks = (scene, row) pairs cut from the long MP4. payoff = (scene, row, seconds after row start) for the hook frame."""
N = "Narrator"
END_CAPTION, END_SPOKEN = "Full video on the channel.", "Full video on the channel."

SHORTS = [
 dict(n=1, file="capillary-short-1-points.mp4", hook="Who runs your reward points?", spoken="Who runs your reward points?",
      picks=[(1, 0), (1, 1), (1, 2), (2, 0), (2, 2), (2, 3), (2, 4)], payoff=(1, 0, 4.6)),
 dict(n=2, file="capillary-short-2-paid-first.mp4", hook="This software company gets paid first.", spoken="This software company gets paid first.",
      picks=[(2, 1), (2, 5), (2, 6), (3, 0), (3, 1), (3, 2), (3, 3)], payoff=(3, 2, 5.5)),
 dict(n=3, file="capillary-short-3-one-client.mp4", hook="One client. ₹99 crore. And warrants.", spoken="One client. Ninety nine crore. And warrants.",
      picks=[(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)], payoff=(4, 3, 4.5)),
 dict(n=4, file="capillary-short-4-bought-growth.mp4", hook="Forty percent growth. Most of it bought.", spoken="Forty percent growth. Most of it bought.",
      picks=[(5, 1), (5, 3), (5, 4), (5, 5), (6, 0), (6, 2), (6, 3), (6, 4)], payoff=(6, 2, 3.0)),
 dict(n=5, file="capillary-short-5-staircase.mp4", hook="₹0.6 crore to ₹20 crore in a year.", spoken="Zero point six crore to twenty crore in a year.",
      picks=[(7, 0), (7, 1), (7, 2), (7, 3)], payoff=(7, 2, 9.0)),
 dict(n=6, file="capillary-short-6-four-checks.mp4", hook="Four checks before November.", spoken="Four checks before November.",
      picks=[(13, 0), (13, 1), (13, 2), (13, 3), (13, 4), (13, 5)], payoff=(13, 5, 8.6)),
]

SCENES = []
for s in SHORTS:
    SCENES.append((100 + s["n"], "Short %d" % s["n"], [(N, s["hook"], s["spoken"]), (N, END_CAPTION, END_SPOKEN)], "Short", None))
