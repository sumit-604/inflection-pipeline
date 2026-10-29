@echo off
REM ---------------------------------------------------------------------------
REM watchlist_feed_download_DEBUG.bat
REM
REM DEBUG / FIRST-RUN MODE. Use this once to confirm the pipeline works:
REM   - Browser opens VISIBLY (so you can watch the login + scrape)
REM   - Output appears in the console in real time (NOT to a log file)
REM   - Window stays open at the end (so you can read the summary)
REM
REM Double-click to run. Wait 60-120 seconds for the first prints to appear —
REM playwright starts a fresh Chromium browser which takes a few seconds.
REM
REM Once this works, use watchlist_feed_download.bat (the headless, logged
REM version) for the scheduled task.
REM ---------------------------------------------------------------------------

cd /d "C:\ConcallPipeline\Daily Concall Intelligence"
echo.
echo ================================================================
echo  Watchlist Feed Download — DEBUG MODE (visible browser)
echo  Be patient. First output appears in 30-60 seconds.
echo  DO NOT close this window until you see "SUMMARY:" line.
echo ================================================================
echo.
REM No --auto flag = browser opens visibly so you can watch it work
python -u download_feed.py
echo.
echo ================================================================
echo  Run finished. Review the output above.
echo ================================================================
pause
