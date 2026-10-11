"""Capillary Technologies - Business Decoded #6. Narration, captions and cues.

Row format: (speaker, caption_text, spoken_text)
  - caption_text is burned in (digits and the rupee sign kept)
  - spoken_text is what Kokoro is given (numbers spelled out, initialisms spaced)
  - speaker "Source" / "Card" rows are on-screen text only (never voiced)
Scene 11 figures come ONLY from scene11_values.json, written by fill_scene11.py
from scenario-rebuild-page64.md. Line 7.4 is chosen by the filing check
(fact-check-verified.md): reported consolidated PAT for the June 2026 quarter was a loss.
"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
V = json.loads((HERE / "scene11_values.json").read_text(encoding="utf-8"))

_ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
_TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()

def say_int(n):
    if n < 20: return _ONES[n]
    if n < 100: return _TENS[n // 10] + ("" if n % 10 == 0 else " " + _ONES[n % 10])
    if n < 1000:
        r = n % 100
        return _ONES[n // 100] + " hundred" + ("" if r == 0 else " and " + say_int(r))
    r = n % 1000
    return say_int(n // 1000) + " thousand" + ("" if r == 0 else (" and " + say_int(r) if r < 100 else " " + say_int(r)))

def fmt(n): return f"{n:,}"

R27, R30 = V["REV27"], V["REV30"]
E27, E30 = V["EBITDA"][0], V["EBITDA"][3]
P27, P30 = V["PAT"][0], V["PAT"][3]
BEAR30, BULL30 = V["BEAR_PAT"][3], V["BULL_PAT"][3]

N, M, R = "Narrator", "Meera", "Ramesh"

# Line 7.4: chosen by the Q1 FY27 filing check (consolidated PAT, quarter ended 30-Jun-2026 = Rs (95.52) mn, a loss).
LINE_7_4 = "The headline result for that quarter showed a loss, because of a one-off fraud charge. The operating line kept rising."

SCENES = [
 (1, "Points at the till", [
   (N, "A shopper buys a coffee, and her phone buzzes: forty reward points.",
       "A shopper buys a coffee, and her phone buzzes: forty reward points."),
   (N, "Behind those points sits software most shoppers never hear of.",
       "Behind those points sits software most shoppers never hear of."),
   (N, "Capillary Technologies, from Bengaluru, runs it for brands around the world.",
       "Capillary Technologies, from Bengaluru, runs it for brands around the world."),
   (N, "In one year, its quarterly operating profit went from under ₹1 crore to about ₹20 crore.",
       "In one year, its quarterly operating profit went from under one crore to about twenty crore."),
   (M, "So the points business is booming?", "So the points business is booming?"),
   (N, "Partly. Keerti Sharma's research shows what grew, what was bought, and what still has to be proven.",
       "Partly. Keerti Sharma's research shows what grew, what was bought, and what still has to be proven."),
   ("Card", "Capillary Technologies · Business Decoded #6"),
 ], "Acted", None),

 (2, "What Capillary sells", [
   (N, "A brand pays Capillary to run its loyalty programme: who earns points, which offers go out, and what each customer bought.",
       "A brand pays Capillary to run its loyalty programme: who earns points, which offers go out, and what each customer bought."),
   (N, "The brand pays every year, on contracts that usually run three to seven years.",
       "The brand pays every year, on contracts that usually run three to seven years."),
   (N, "At each customer, Capillary's system plugs into about nine other systems: tills, apps, websites and payments.",
       "At each customer, Capillary's system plugs into about nine other systems: tills, apps, websites and payments."),
   (R, "Once we are wired in, moving out is a big project for the brand.",
       "Once we are wired in, moving out is a big project for the brand."),
   (N, "That is why only about five in a hundred customers leave in a year.",
       "That is why only about five in a hundred customers leave in a year."),
   (M, "So it's like rent, paid by the brand?", "So it's like rent, paid by the brand?"),
   (N, "Close. Rent, often paid in advance.", "Close. Rent, often paid in advance."),
 ], "Acted", None),

 (3, "Cash comes first", [
   (N, "Many customers pay for the year up front, so the cash arrives before the revenue is booked.",
       "Many customers pay for the year up front, so the cash arrives before the revenue is booked."),
   (N, "EBITDA means profit before interest, tax, depreciation and amortisation.",
       "E bit da means profit before interest, tax, depreciation and amortisation."),
   (N, "In FY26, Capillary's cash from operations was about 1.4 times its adjusted EBITDA.",
       "In F Y twenty six, Capillary's cash from operations was about one point four times its adjusted E bit da."),
   (N, "For a growing software company, that is a healthy sign.",
       "For a growing software company, that is a healthy sign."),
   ("Source", "Capillary Annual Report FY26 (contract liabilities, p.233) · Q4 FY26 investor presentation, May-2026"),
 ], "Data", None),

 (4, "One very large client", [
   (N, "One customer stands out: Optum, part of America's UnitedHealth group.",
       "One customer stands out: Optum, part of America's UnitedHealth group."),
   (N, "Capillary's revenue from Optum rose from about ₹12 crore in FY24 to about ₹99 crore in FY25.",
       "Capillary's revenue from Optum rose from about twelve crore in F Y twenty four to about ninety nine crore in F Y twenty five."),
   # COMPLIANCE CHANGE: job text says "the right to buy Capillary shares later"; "buy" is a banned word.
   (N, "Capillary also gave Optum warrants: the right to purchase Capillary shares later.",
       "Capillary also gave Optum warrants: the right to purchase Capillary shares later."),
   (N, "The accounts treat that as a discount: about ₹21 crore comes off revenue this year, and about ₹31 crore a year after that.",
       "The accounts treat that as a discount: about twenty one crore comes off revenue this year, and about thirty one crore a year after that."),
   (N, "The current contract runs to early 2029.", "The current contract runs to early twenty twenty nine."),
   (M, "And after that?", "And after that?"),
   (N, "Nobody knows yet. That date is on Keerti Sharma's watch list.",
       "Nobody knows yet. That date is on Keerti Sharma's watch list."),
   ("Source", "Capillary Red Herring Prospectus, Nov-2025 (pp.71-73)"),
 ], "Acted", None),

 (5, "Growth that was bought", [
   (N, "Capillary has also grown by buying other loyalty software companies.",
       "Capillary has also grown by buying other loyalty software companies."),
   (N, "It bought Kognitiv out of a US bankruptcy, and SessionM from Mastercard in May 2026.",
       "It bought Kognitiv out of a U S bankruptcy, and SessionM from Mastercard in May twenty twenty six."),
   (N, "The prices were low. In earlier deals, Capillary kept about two thirds of the revenue it bought.",
       "The prices were low. In earlier deals, Capillary kept about two thirds of the revenue it bought."),
   (N, "But the bought businesses earn very little: about ₹20 crore of EBITDA, management says.",
       "But the bought businesses earn very little: about twenty crore of E bit da, management says."),
   (R, "Our plan is to lift that to about ₹130 crore by FY30.",
       "Our plan is to lift that to about one hundred and thirty crore by F Y thirty."),
   (N, "That plan is management's. It is not yet in the numbers.",
       "That plan is management's. It is not yet in the numbers."),
   ("Source", "Capillary RHP, Nov-2025 (pp.281-283) · Investor Day presentation p.64, 14-May-2026"),
 ], "Acted", None),

 (6, "Two growth numbers", [
   (N, "In the June 2026 quarter, revenue grew more than forty percent from a year earlier.",
       "In the June twenty twenty six quarter, revenue grew more than forty percent from a year earlier."),
   (N, "Take out the bought businesses, the Optum account and currency gains.",
       "Take out the bought businesses, the Optum account and currency gains."),
   (N, "Keerti Sharma estimates the core grew about eleven to thirteen percent.",
       "Keerti Sharma estimates the core grew about eleven to thirteen percent."),
   (M, "So most of the jump was bought?", "So most of the jump was bought?"),
   (N, "Most of it. The core grows steadily. The bought part has to be fixed.",
       "Most of it. The core grows steadily. The bought part has to be fixed."),
   ("Source", "Q1 FY27 results and presentation, Aug-2026 · core growth: Keerti Sharma estimate, 10-Oct-2026"),
 ], "Data", None),

 (7, "The profit staircase", [
   (N, "Now the part that changed.", "Now the part that changed."),
   (N, "This is operating profit, after staff share costs and depreciation, leaving out interest on the IPO cash and one-off items.",
       "This is operating profit, after staff share costs and depreciation, leaving out interest on the I P O cash and one-off items."),
   (N, "₹0.6 crore. ₹0.7 crore. Then ₹7.4 crore, ₹12.5 crore, and ₹20.3 crore in the June quarter.",
       "Zero point six crore. Zero point seven crore. Then seven point four crore, twelve point five crore, and twenty point three crore in the June quarter."),
   (N, LINE_7_4, LINE_7_4),
   ("Source", "Capillary investor presentations, Q1 FY26 to Q1 FY27 (operating EBIT = adjusted EBITDA minus ESOP minus D&A) · Keerti Sharma calculation"),
 ], "Data", None),

 (8, "Return on the money tied up", [
   (N, "Now measure that profit against the money tied up in the business, leaving out spare cash.",
       "Now measure that profit against the money tied up in the business, leaving out spare cash."),
   (N, "One and a half percent in FY25. Under four percent in FY26. About thirteen and a half percent at the June quarter's pace.",
       "One and a half percent in F Y twenty five. Under four percent in F Y twenty six. About thirteen and a half percent at the June quarter's pace."),
   (N, "One strong quarter is a start, not a trend.", "One strong quarter is a start, not a trend."),
   (M, "How many quarters make a trend?", "How many quarters make a trend?"),
   (N, "Keerti Sharma's test is above ten percent for two quarters in a row.",
       "Keerti Sharma's test is above ten percent for two quarters in a row."),
   ("Source", "Capillary Q1 FY27 investor presentation pp.26, 28-29 · Keerti Sharma calculation, 10-Oct-2026"),
 ], "Data", None),

 (9, "The AI add-on", [
   (N, "Capillary also sells an AI assistant called aiRA, which writes offers and campaigns for brand teams.",
       "Capillary also sells an A I assistant called aiRA, which writes offers and campaigns for brand teams."),
   (N, "In August, management said 26 customers were using it, but fewer than 10 were paying.",
       "In August, management said twenty six customers were using it, but fewer than ten were paying."),
   (N, "It is early. Keerti Sharma's numbers give it no weight.",
       "It is early. Keerti Sharma's numbers give it no weight."),
 ], "Partly acted", None),

 (10, "The case against", [
   (N, "Now the case against.", "Now the case against."),
   (N, "First, the core grows at about eleven to thirteen percent, steady but not fast.",
       "First, the core grows at about eleven to thirteen percent, steady but not fast."),
   (N, "Second, one client is large, its contract ends in early 2029, and the warrant discount runs until then.",
       "Second, one client is large, its contract ends in early twenty twenty nine, and the warrant discount runs until then."),
   (N, "Third, the profit plan for the bought businesses is still a plan.",
       "Third, the profit plan for the bought businesses is still a plan."),
   (N, "Fourth, Capillary competes with large global loyalty firms for the same brands.",
       "Fourth, Capillary competes with large global loyalty firms for the same brands."),
   (N, "In the June quarter, Capillary booked a fraud loss of about ₹33 crore at a SessionM unit in the Czech Republic, and a KPMG forensic review is under way; details are in the description.",
       "In the June quarter, Capillary booked a fraud loss of about thirty three crore at a SessionM unit in the Czech Republic, and a K P M G forensic review is under way; details are in the description."),
 ], "Paper", None),

 (11, "The next four years", [
   (N, "Here is Keerti Sharma's base case for the next four years.",
       "Here is Keerti Sharma's base case for the next four years."),
   (N, f"Revenue grows from about ₹{fmt(R27)} crore this year to about ₹{fmt(R30)} crore by FY30.",
       f"Revenue grows from about {say_int(R27)} crore this year to about {say_int(R30)} crore by F Y thirty."),
   (N, f"Adjusted EBITDA rises from about ₹{E27} crore to about ₹{E30} crore, a margin of about thirty one percent.",
       f"Adjusted E bit da rises from about {say_int(E27)} crore to about {say_int(E30)} crore, a margin of about thirty one percent."),
   (N, f"Operating profit after tax goes from about ₹{P27} crore this year to about ₹{P30} crore by FY30.",
       f"Operating profit after tax goes from about {say_int(P27)} crore this year to about {say_int(P30)} crore by F Y thirty."),
   (N, "That path depends on the bought businesses improving on management's timeline.",
       "That path depends on the bought businesses improving on management's timeline."),
   (N, f"If the fix stalls, FY30 profit is nearer ₹{BEAR30} crore. If it runs faster, nearer ₹{BULL30} crore.",
       f"If the fix stalls, F Y thirty profit is nearer {say_int(BEAR30)} crore. If it runs faster, nearer {say_int(BULL30)} crore."),
   ("Source", "Estimate · Keerti Sharma research · as of 10-Oct-2026 · not company guidance. Operating PAT excludes treasury income and one-offs; tax at 25%."),
 ], "Data", None),

 (12, "How to value it", [
   (N, "How would one value a business like this? Take operating profit a year ahead, and multiply it.",
       "How would one value a business like this? Take operating profit a year ahead, and multiply it."),
   (N, "The multiple depends on three things: how steady the growth is, whether cash comes first, and how hard the product is to replace.",
       "The multiple depends on three things: how steady the growth is, whether cash comes first, and how hard the product is to replace."),
   (N, "Capillary scores well on the last two. Growth is where it still has to prove itself.",
       "Capillary scores well on the last two. Growth is where it still has to prove itself."),
 ], "Paper", None),

 (13, "Check it yourself", [
   (N, "Four things to check, all in public filings.", "Four things to check, all in public filings."),
   (M, "One: the November results. Is the return on money tied up above ten percent again?",
       "One: the November results. Is the return on money tied up above ten percent again?"),
   (M, "Two: growth without Optum and currency. Steady near eleven to thirteen percent, or slipping?",
       "Two: growth without Optum and currency. Steady near eleven to thirteen percent, or slipping?"),
   (M, "Three: by March 2027, are SessionM and Kognitiv making real money, or still breaking even?",
       "Three: by March twenty twenty seven, are SessionM and Kognitiv making real money, or still breaking even?"),
   (M, "Four: the KPMG report. What did it find?", "Four: the K P M G report. What did it find?"),
   (N, "And the story is wrong if existing customers spend less for two quarters in a row, or the bought businesses still break even by March 2027.",
       "And the story is wrong if existing customers spend less for two quarters in a row, or the bought businesses still break even by March twenty twenty seven."),
 ], "Acted", None),

 (14, "Close", [
   (N, "Every reward point earns Capillary a small fee.", "Every reward point earns Capillary a small fee."),
   (N, "The question is not whether brands need this software. It is whether the bought businesses can earn like the core.",
       "The question is not whether brands need this software. It is whether the bought businesses can earn like the core."),
   (N, "Watch the profit, not just the growth.", "Watch the profit, not just the growth."),
 ], "Acted", None),
]

# Sub-sentence cue phrases (searched in the SPOKEN text of the row). Used for on-screen changes
# that must land on a named word: (scene, row_index) -> [phrases]
CUES = {
 (1, 0): ["forty reward points"],
 (2, 0): ["who earns points", "which offers go out", "what each customer"],
 (2, 2): ["tills", "apps", "websites", "payments"],
 (3, 2): ["about one point four"],
 (4, 1): ["twelve crore", "ninety nine crore"],
 (4, 3): ["twenty one crore", "thirty one crore"],
 (5, 1): ["Kognitiv", "SessionM"],
 (6, 1): ["bought businesses", "Optum", "currency"],
 (7, 2): ["Zero point six", "Zero point seven", "seven point four", "twelve point five", "twenty point three"],
 (8, 1): ["One and a half", "Under four", "About thirteen"],
 (9, 1): ["twenty six", "fewer than ten"],
 (11, 5): ["nearer " + say_int(BEAR30), "nearer " + say_int(BULL30)],
 (12, 1): ["how steady", "whether cash", "how hard"],
 (12, 2): ["Capillary scores", "Growth is where"],
 (13, 5): ["existing customers", "or the bought"],
}

TITLE_CARD = "Capillary Technologies · Business Decoded #6"

if __name__ == "__main__":
    import re
    for sc in SCENES:
        for row in sc[2]:
            if row[0] in ("Source", "Card"): continue
            assert not re.search(r"[0-9₹%]", row[2]), (sc[0], row[2])
    print("script.py ok:", sum(1 for s in SCENES for r in s[2] if r[0] not in ("Source", "Card")), "voiced lines")
