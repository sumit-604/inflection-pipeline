# Manual drops

`fpi_equity_monthly.csv`: monthly net FPI equity investment from NSDL
(https://www.fpi.nsdl.co.in/web/Reports/Yearwise.aspx?RptType=6), columns
`month` (YYYY-MM) and `fpi_equity_net_inr_cr` (INR crore, equity, net).
The cloud shell cannot reach NSDL. Operator: save the yearly tables locally
as this one CSV, commit it, then run `python fetch.py` and `python run.py`.
