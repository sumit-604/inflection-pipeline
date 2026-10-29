@echo off
REM One-off concall transcript backfill.
REM Downloads any transcripts on screener.in's concalls page dated 2026-10-06
REM or newer, into downloads\<pub_date>\morning\. Adjust the --since date
REM below if you want a different cutoff.
cd /d "C:\ConcallPipeline\Daily Concall Intelligence"
echo === Backfill started at %date% %time% ===
"C:\Users\SUMIT SHARMA\AppData\Local\Python\pythoncore-3.14-64\python.exe" download_backfill_win.py --since 2026-10-06 --batch morning
echo === Backfill finished at %date% %time% ===
pause
