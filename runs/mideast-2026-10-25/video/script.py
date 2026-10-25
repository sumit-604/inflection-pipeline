"""Middle East war explainer - narration, captions and on-screen text, copied word for word from the job.

SCENES: (id, title, bg_colour_name, narration, [on-screen labels])
- narration is BOTH the voiced text and the burned-in caption text (the voice engine gets respellings
  through synth.py's pronunciation table; captions keep the normal spelling).
- labels are the on-screen text from the job (kept for the sweep / documentation; the drawing code is in long.js).
"""
BG = {"navy": "#16202A", "sand": "#F4EFE6", "teal": "#0F4C4C", "orange": "#B4481A", "olive": "#4A5D23", "plum": "#5B2A4E", "slate": "#2F4A6D"}

SCENES = [
 (1, "HOOK", "navy",
  "An oil price near one hundred and seventeen dollars. Two blockades at sea. And a possible new strike on Iran within weeks. Keerti Sharma's research explains it all, in plain words.",
  ["The Middle East war, in plain words"]),
 (2, "WHY IT STARTED", "sand",
  "It began with uranium. The same machines that make fuel for power plants can also make fuel for a bomb. Power plants need about five percent. Iran reached sixty percent. Bombs need ninety. America and Israel do not trust Iran to stop. Iran says enriching uranium is its legal right.",
  ["5% power fuel | 60% Iran | 90% bomb grade", "5% power plant fuel", "60% Iran reached here", "90% bomb grade", "Never a nuclear weapon", "Our right to enrich"]),
 (3, "HOW WE GOT HERE", "teal",
  "In 2015, Iran signed a deal that capped its enrichment. In 2018, America walked out of that deal. Iran then pushed enrichment higher. In June 2025 came a twelve-day war. On the twenty-eighth of February 2026, America and Israel struck Iran again, and its Supreme Leader was killed. Iran answered by blocking the Strait of Hormuz.",
  ["2015: Nuclear deal", "2018: US leaves the deal", "June 2025: 12-day war", "28 Feb 2026: US and Israel strike Iran", "Since then: Hormuz blocked"]),
 (4, "MORE THAN ONE MOTIVE", "orange",
  "The official reason is nuclear. But analysts point to more. Before the war, China bought almost all of Iran's oil. Hitting Iran also hits China's cheap supply. Control of Hormuz gives huge power over world energy. And Israel had wanted this war for years. Critics and supporters still argue over which reason mattered most.",
  ["Nuclear fears", "China's cheap oil", "Control of Hormuz", "Israel's goals"]),
 (5, "TWO BLOCKADES", "olive",
  "Today there are two blockades. Iran attacks and mines tankers in the Strait of Hormuz. America stops Iran's own oil ships. In September, Iran sold no oil at all from its ports. Oil prices have jumped to their highest level since April.",
  ["Iran blocks the sea", "The US blocks Iran", "$116.72 Brent, 23 Oct"]),
 (6, "THE SAUDI FRONT", "plum",
  "The fight has also moved to Saudi Arabia. Yemen's Houthis, backed by Iran, are firing missiles at Saudi airports and oil sites. Their main target is a pipeline that lets Saudi oil skip Hormuz. Iran cannot beat the American navy. So it makes the Gulf pay.",
  ["Target: Saudi Arabia's bypass pipeline"]),
 (7, "UNDER THE SEA", "slate",
  "There is a hidden risk under the sea. Iran has threatened internet cables in Hormuz if it is attacked again. The bigger danger is the Red Sea, which carries over ninety percent of the data between Europe and Asia. About sixty percent of India's internet traffic goes that way. The world would not go dark. But internet could get slower and costlier.",
  ["Red Sea: over 90% of Europe-Asia data", "60% of India's internet goes west", "Permit needed"]),
 (8, "INSIDE IRAN", "navy",
  "Inside Iran, the economy is breaking. One dollar now costs about twenty-seven lakh rials. Prices have almost doubled in a year. Petrol queues are long before winter. But the streets are quiet. Last winter's protests were crushed by force. The economy is breaking. The regime is not.",
  ["27 lakh rials = 1 dollar", "~90% price rise in a year", "Zero oil sold from ports in September"]),
 (9, "THE ELECTION WINDOW", "sand",
  "America votes on the third of November. If Trump's party loses Congress, he still stays president until 2029. Removing him would need sixty-seven senators, which is very unlikely. But after the vote, the pressure of oil prices on his party eases. That opens a window for a new strike, before the new Congress sits in January.",
  ["27 Oct: Israel votes", "3 Nov: US midterms", "window", "Removal needs 67 of 100 senators", "Window: Nov to Jan"]),
 (10, "THE ODDS", "teal",
  "So what happens next? Keerti Sharma's research sees a new strike within a year as likely, about seventy percent. The most likely path is a short strike on missiles and drones, then a deal. The danger is that Iran decides how short a war stays. If it hits Gulf oil plants in return, oil could go above one hundred and fifty dollars.",
  ["A short strike, then a deal: 35%", "A long siege, no deal: 27%", "Big escalation, oil above $150: 15%", "A deal with no new strikes: 13%", "Iran's regime cracks: 10%",
   "New strike within a year: about 70%. Judgment-based estimates, not market prices."]),
 (11, "WHY INDIA SHOULD CARE", "orange",
  "For India, this is personal. About forty percent of India's crude oil, sixty percent of its natural gas imports and ninety percent of its cooking gas come through Hormuz. A long siege means higher fuel and gas costs through the winter.",
  ["Through Hormuz: 40% of crude | 60% of LNG | 90% of cooking gas", "40% of crude", "60% of LNG", "90% of cooking gas"]),
 (12, "CLOSE", "navy",
  "Watch the dates. Israel votes on the twenty-seventh of October. America votes on the third of November. For more research in plain words, follow Keerti Sharma.",
  ["Keerti Sharma | @Keerti__Sharma", "For learning only. Not investment advice."]),
]

# The job writes "Through Hormuz: 40% of crude | 60% of LNG | 90% of cooking gas" and the sweep needs "60%" and "40%"; the
# three numbers pop up one at a time so they are drawn as three separate labels.

# ---------------- Short (1080x1920) ----------------
SHORT_SCENES = [
 (1, "hook", "navy", "Oil is near one hundred and seventeen dollars. Here is why, in under a minute.", ["Oil at $117. Why?"]),
 (2, "two blockades", "sand", "Iran attacks tankers in the Strait of Hormuz. America blocks Iran's own oil. Iran sold no oil from its ports in September.", ["Two blockades at sea"]),
 (3, "saudi pipeline", "teal", "Yemen's Houthis are hitting Saudi airports and the pipeline that lets Saudi oil skip Hormuz.", ["War moves to Saudi Arabia"]),
 (4, "calendar and odds", "orange", "After America's election on the third of November, a new strike on Iran looks likely. Keerti Sharma's research puts it at about seventy percent within a year.", ["3 Nov", "Strike within a year: about 70%"]),
 (5, "india kitchen", "olive", "For India, ninety percent of cooking gas comes through Hormuz. A long siege means costlier fuel this winter.", ["90% of India's cooking gas comes via Hormuz"]),
 (6, "end card", "plum", "Follow Keerti Sharma for research in plain words.", ["Follow @Keerti__Sharma"]),
]
