# Breadth Brief Framework v1.1

The specification for the nightly Indian market breadth brief. The scheduled
Claude session reads this file, the facts sheet and the prior brief, then
writes the brief. A human can follow it the same way.

Operator: Sumit Sharma. Data: two public Chartink dashboards, 34 table tiles,
collected at 21:00 IST each weekday into `data/chartink/csv/<date>/`.

## 1. Inputs, in this order

1. `data/chartink/analysis/facts/latest.md`. The facts sheet. Every number
   used in the brief comes from here. It is arithmetic over the 34 files:
   regime readings with percentiles, index and sector tables, each screener's
   size and mix and leaders, shareholding shifts, and cross-list confluence.
2. `data/chartink/analysis/briefs/latest.md`, the previous brief, for
   continuity: what it said to watch, and what those things did.
3. `data/chartink/analysis/market_breadth_daily.csv` only if a number is
   needed that the facts sheet does not carry. One row per date, so the
   history of any breadth line (the March low, the April thrust days, the May
   shock, the July range) can be read from it.

Do not read the 34 raw CSVs. Do not read `data/chartink/mbm-swing-ka-sultan/`
or `market-breadth-analysis/`.

## 2. What the brief is

A description of what the Indian stock market is doing under the surface,
written as a story in plain words, for someone who holds for months (the
investor) and someone who holds for days (the trader). It says where the
market stands, which parts are leading and which are breaking, who is buying,
and what the reader should watch or do differently because of it.

It is long. 3,000 to 5,000 words of prose. It has at least 30 numbered
points, each a short paragraph, split between the trader and the investor.
It ends with what would change the read, on both sides.

It is not advice to buy or sell anything. It names setups the data favours
and setups the data penalises, in the language of conditions. The operator
decides. The brief surfaces.

## 3. Voice

**Operator ruling, 2026-09-06.** Write the way you would explain the market
to a smart friend who does not trade. A story, not a table of numbers and not
compressed jargon. On the same day the operator rejected a short digest as
"shallow" and a numbers-dense long brief as "too complex, too many numbers".
Long and plain is the target. The reference that landed is
`data/chartink/analysis/briefs/2026-09-04.md`. Match its register.

Simplified Technical English. One idea per sentence, 20 words or fewer.
Active voice. No em-dashes or en-dashes; use a full stop or comma. No hedging
filler (arguably, somewhat, essentially, significantly). No AI tells: no "not
just X but Y", no participial openers, no robust, holistic, seamless,
landscape, journey, ecosystem. Plain word over jargon. When a Chartink term
must appear, say what it means in words in the same sentence.

Numbers. Use a number only when it carries the point, then one number,
rounded to what a reader can hold: "about half the market", "seven in ten",
"1,014 against 1,254", "up about nine percent". No percentiles in the prose.
No 1d/5d/20d triples. Every number used still traces to the facts sheet. The
full figures live in the appendix, `<date>-appendix.md`, a copy of the facts
sheet; the brief links to it once, in the opening note.

Paragraphs, not bullet lists of metrics. No tables in the brief. Bold is used
only for the numbered point titles.

Explain the why in market terms when the data shows it (parts makers leading
while car makers fall; jewellers rising with gold). Never invent a news reason.
Claude Code has no web access; say so once in the opening note.

## 4. Structure, in this order

Front matter for the renderer:

```
---
title: "Market Breadth Brief"
subtitle: "<Weekday>, <YYYY-MM-DD> trade date · written <YYYY-MM-DD> · for Sumit Sharma"
---
```

Then a top heading `# Market read, <D Month YYYY>` and an opening note of two
short paragraphs: where the files came from and how many of 34 were present,
where the numbers are (the appendix link), that no news is checked, and that
this is description not advice.

Then these sections, with these headings:

### The picture in one paragraph

One paragraph. What the market is, right now, in the simplest true words.
The barbell, the base, the split, whichever the data shows. This paragraph is
copied into the digest page, so it must stand alone.

### Where the market stands

Three to five paragraphs. The layers by size (large, mid, small) against
their trend lines. The recent history in story form: the last shock, the
range, how long the base has held. What share of the market is in an uptrend
and whether that is high or low for this history. What the week's last
sessions did, and whether the volume behind them was ordinary or a thrust.
Fear, from the VIX, and any cross-asset tension the facts sheet shows.

### What the sectors say

One short paragraph per sector that matters tonight: the clear leader,
leaders that are tired, the sector that broke this week, the index-versus-
breadth mismatches (an index up on a few names), sectors turning up from the
bottom, and the weakest across every horizon. Tie index moves to sector
breadth in words.

### What is leading

What the screens are catching, as groups not lists: how many stocks at yearly
highs and of what size, which sub-industries moved together, which pairs are
split (parts makers versus car makers, fibre cable versus power cable), where
large-cap momentum sits, and whether there is froth (penny stocks at highs,
count of ten-percent days). Name a stock only when it is the example that
makes the group visible.

### Who is buying

Three paragraphs from the shareholding files: the foreign-money theme, the
domestic-institution theme, and where retail is crowding. State the zero-prior
caveat once in plain words. Never treat low institutional holding as a risk;
retail holding that rose after a big move is a different point, and that one
may be made.

### Thirty points (or more)

`### For the trader` then `### For the investor`. Each point is a bold title
sentence followed by two to four plain sentences: what is happening, why it
matters, and what would change it. At least 15 on each side. Number them
straight through.

Trader points cover: whether the bounce is proven, the swing-vote reading,
whether shorting works, the parabolic tail, sector pairs and spreads, the
large-cap group turning, index-versus-breadth traps, froth and size, both
extremes growing, and the early turns with volume.

Investor points cover: base versus trend, the quality end versus the tail,
the barbell, whether the base is eroding under a strong top, long-run strength
and weakness by sector, sectors turning from the bottom, leaders tiring,
foreign and domestic money themes, promoter buying at highs, retail crowding
as supply, persistence with institutional confirmation, where large-cap
momentum lives, cross-asset warnings, cheap fear, and any pipeline names from
`companies/*.md` that appear on tonight's lists (memory to weigh, never
evidence).

### What would change this read

Two paragraphs. What would make the constructive view fail. What would make
the cautious view fail. Each names the reading in words and the level in one
rounded number.

## 5. Rules the writer must not break

- Every number used traces to the facts sheet, or to the history CSV.
- No buy, sell, hold, target or stop instruction on any named stock.
- Sector and screen level setups may be called favoured or penalised.
- A missing file marks the sections that depend on it, in words. It does not
  stop the brief.
- Zero-prior shareholding rows are named as such, once, and never counted as
  a rise.
- The prior brief is context, never evidence. Tonight's numbers win.
- No news reasons invented. No web access.
- At least 30 points. Prose only. No tables. No landing lines.

## 6. Output

Write to `data/chartink/analysis/briefs/<trade date>.md`, then copy to
`briefs/latest.md`. Copy the facts sheet to `briefs/<trade date>-appendix.md`
with the heading `# Market Breadth Brief: Data Appendix, <trade date>`. Put
"The picture in one paragraph" below the marker in the digest file. Then run
`python tools/chartink/render_html.py`.
