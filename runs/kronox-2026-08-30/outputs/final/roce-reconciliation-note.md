# KRONOX ROCE definitional reconciliation (standing item, load-bearing for Section 1B Pillar 1)

Ferried from Claude web 2026-08-30. Resolves the 32% vs 70% gap from the KRONOX AR FY26 balance sheet and P&L. All figures Rs lakh, AR FY26 (year ended 31-Mar-2026), source anchors below. This is a phase-3 Pillar 1 input, not a phase-1 verdict change.

## Components (AR FY26, standalone)
- PBT: 3,730.2 (P&L, l.10830) | Finance cost: 11.4 (l.10793) | Other income: 519.4 (Note 23, l.10787)
- EBIT (PBT + finance cost): 3,741.6
- Operating EBIT (PBT + finance cost - other income): 3,222.2
- Total Equity: 11,612.7 (l.10713) | Total Borrowings: 160.7 (Note 14/16, l.11929)
- Total Assets: 12,752.3 | Total Current Liabilities: 1,036.8 (l.11925)
- Cash & equivalents (Note 9): 274.6 | Current bank balances/FDs (Note 10): 4,599.5
- Non-current Other Financial Assets (Note 5, incl. long-term deposits): 1,864.3 | Non-current Investments (Note 4): 2.5
- Cash + FD + investments (non-operating financial assets): ~6,740.9 (~Rs 67.4cr); B02/B03 anchored the FD book alone at Rs 64.535cr

## Two ROCE bases, both arithmetically correct
1. ROCE, capital employed INCLUDING cash/FD (pipeline basis):
   EBIT 3,741.6 / (Equity 11,612.7 + Borrowings 160.7 = 11,773.4) = 31.8%  ~= pipeline 32.22%.
   (Equivalently Total Assets - Current Liabilities = 11,715.5 -> 31.9%.)
2. ROIC, capital employed EXCLUDING cash/FD/investments (third-party basis):
   EBIT 3,741.6 / (11,773.4 - 6,453 [Rs 64.53cr]) = 5,320.4 -> 70.3%  ~= third-party 70.8%.
   (Strip the full 6,740.9 -> 5,032.5 -> 74.3%.)

## Conclusion
The entire 32% <-> 70% gap is one thing: the treatment of ~Rs 64.5-67.4cr of cash, fixed deposits and investments in capital employed. That pile is ~55% of equity and ~57% of capital employed. Include it -> ~32%; net it out -> ~70%. Operating-EBIT variants (stripping the Rs 5.19cr other income, mostly FD interest) land ROIC at ~60-64%; the third-party 70.8% keeps other income in EBIT and nets all cash from the base.

## Ruling required at phase 3 (Pillar 1)
- Set the capital-employed convention (net cash or not) ONCE, consistently, per the strategy's Section 1B convention.
- CONVERTER TAG BINDS: 09b/B04 place KRONOX as a commodity converter; per CLAUDE.md + v3.7 Amendment 17, spot-year ROCE and rupee-denominated WC trends must NOT feed Section 1B/FTTCP for a converter. So the Pillar 1 base is a normalised/durable ROCE on a fixed capital-employed convention, not the FY26 spot number on either basis.
- At KRONOX the operator's note stands: the chosen basis moves the converter multiple materially (~23.6x vs ~42x). Resolve the convention before setting any Pillar 1 base.
- INDOBORAX half of the gap (filed 17.13% vs modelled ROIC ~35-38%) is the same cash-in-capital-employed mechanism; resolve it in the Indo Borax run, not here (entities valued separately per the entity-count gate).
