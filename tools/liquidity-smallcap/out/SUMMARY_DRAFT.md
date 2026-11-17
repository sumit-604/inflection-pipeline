# Draft: which money measure leads small caps

Months tested: 2023-02 to 2026-10. Numbers only; write SUMMARY.md from this.

Best lead: net LAF (banking-system cash with the RBI), 2 month(s) ahead, r +0.11 on 43 months (95% bar 0.30; does not clear it; sign as expected).

Each measure at its best lead (lag 1 to 3):
- net LAF (banking-system cash with the RBI): lag 2, r +0.11, n 43, below bar, right sign
- the 3-month CD rate (what banks pay for 3-month money): lag 1, r -0.08, n 44, below bar, right sign
- the NSE + BSE MTF book (broker loans to buy shares): lag 3, r -0.00, n 42, below bar, wrong sign
- the NSE-only MTF book: lag 3, r -0.02, n 42, below bar, wrong sign

Rolling 12-month windows where the link ran the wrong way:
- net_laf (lag 2): 2023-11 to 2023-12, 2024-03 to 2024-10, 2025-12
- cd_3m (lag 1): 2026-04 to 2026-10
- mtf_combined (lag 3): 2023-11 to 2024-06, 2024-08 to 2024-09, 2025-05 to 2025-06, 2025-10 to 2026-09
- mtf_nse (lag 3): 2023-11 to 2024-06, 2024-08 to 2024-09, 2025-05 to 2026-09

Gaps: see data/gaps.md.
