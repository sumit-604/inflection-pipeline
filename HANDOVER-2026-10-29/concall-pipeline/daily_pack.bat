@echo off
REM daily_pack.bat — copies yesterday's watchlist feed PDFs (05:30 to 05:30)
REM into daily_pack\<YYYY-MM-DD>\ with INDEX.md. Scheduled daily at 05:15,
REM after the 04:55 feed download.
cd /d "C:\ConcallPipeline\Daily Concall Intelligence"
echo === Run started at %date% %time% === >> daily_pack.log
"C:\Users\SUMIT SHARMA\AppData\Local\Python\pythoncore-3.14-64\python.exe" -u daily_pack.py >> daily_pack.log 2>&1
echo === Run completed at %date% %time% === >> daily_pack.log
