@echo off
REM fetch_announcements.bat — daily 05:00. Downloads every Screener watchlist
REM announcement since the last successful run (announcements\last_run.txt)
REM into ONE folder: announcements\<since>_to_<now>\ with INDEX.md.
REM Replaces the 4-hourly watchlist_feed_download.bat (disabled 03-Oct-2026).
cd /d "C:\ConcallPipeline\Daily Concall Intelligence"
echo. >> fetch_announcements.log
echo === Run started at %date% %time% === >> fetch_announcements.log
"C:\Users\SUMIT SHARMA\AppData\Local\Python\pythoncore-3.14-64\python.exe" -u fetch_announcements.py >> fetch_announcements.log 2>&1
echo === Run completed at %date% %time% === >> fetch_announcements.log
