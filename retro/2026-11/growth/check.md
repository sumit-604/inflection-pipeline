# 20-row check

An independent checker read 20 random scored rows from the PDF page images. It did not see the earlier figures. Growth was then recomputed by the same script. A row matches when the two growth figures agree within 0.5 percentage points.

**Result: 19 of 20 matched as first published. After the fix below, 20 of 20 match.**

The one mismatch was BBOX Q2/H1 FY27. The figures copied from the filing were the same in both reads. The script was wrong: it read the cell `- (line 4 prints "-")` for share of associates as 4, and subtracted it. The parser now reads only the figure at the start of a cell, and a bare dash is zero.

The same fix changed four lender rows, where the treasury cell held two figures (fair value changes and derecognition gains). The rule is now: remove net gain on fair value changes only. Rows changed: AYE Q2, SATIN Q1, SATIN Q2, POONAWALLA Q2. No other row changed.

Sample: random draw (seed 20261117) from scored rows that have a PDF on this machine.

| ticker | period | growth as first published | checker's growth | result | growth after fix | PDF page |
|---|---|---|---|---|---|---|
| FABTECH | Q4 FY26 | +20.5% | +20.5% | MATCH | +20.5% | 7 |
| KELTECH | Q2/H1 FY27 | +65.2% | +65.2% | MATCH | +65.2% | 5 |
| ANAWIL | Q2/H1 FY27 | +583.6% | +583.6% | MATCH | +583.6% | 4 |
| KPL | Q1 FY27 | +100.4% | +100.4% | MATCH | +100.4% | 8 |
| ASTRAMICRO | Q2/H1 FY27 | +156.3% | +156.3% | MATCH | +156.3% | 9 |
| GUFICBIO | Q2/H1 FY27 | +48.0% | +48.0% | MATCH | +48.0% | 2 |
| SOUTHWEST | Q1 FY27 | +494.8% | +494.8% | MATCH | +494.8% | 12 |
| NETWEB | Q2/H1 FY27 | +313.1% | +313.1% | MATCH | +313.1% | 3 |
| PAISALO | Q2/H1 FY27 | +23.2% | +23.2% | MATCH | +23.2% | 5 |
| 544516 | Q2/H1 FY27 | +115.8% | +115.8% | MATCH | +115.8% | 11 |
| 544272 | Q2/H1 FY27 | +11.3% | +11.3% | MATCH | +11.3% | 3 |
| PAUSHAK | Q1 FY27 | +15.4% | +15.4% | MATCH | +15.4% | 2 |
| WEWORK | Q2/H1 FY27 | +41.7% | +41.7% | MATCH | +41.7% | 9 |
| MTARTECH | Q2/H1 FY27 | +3497.2% | +3497.2% | MATCH | +3497.2% | 2 |
| CNL | Q4 FY26 | +87.9% | +87.9% | MATCH | +87.9% | 17 |
| BBOX | Q2/H1 FY27 | +16.6% | +22.0% | DIFFERENT | +22.0% | 6 |
| STLTECH | Q1 FY27 | +4800.0% | +4800.0% | MATCH | +4800.0% | 4 |
| PREMEXPLN | Q4 FY26 | -171.2% | -171.2% | MATCH | -171.2% | 15 |
| 544657 | Q2/H1 FY27 | -20.1% | -20.1% | MATCH | -20.1% | 4 |
| ECOSMOBLTY | Q2/H1 FY27 | +13.4% | +13.4% | MATCH | +13.4% | 8 |
