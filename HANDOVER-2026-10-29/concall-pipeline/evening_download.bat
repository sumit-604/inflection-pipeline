@echo off
cd /d "C:\ConcallPipeline\Daily Concall Intelligence"
echo. >> evening_download.log
echo === Run started at %date% %time% === >> evening_download.log
"C:\Users\SUMIT SHARMA\AppData\Local\Python\pythoncore-3.14-64\python.exe" download_today.py --auto --batch=evening >> evening_download.log 2>&1 || echo WARNING: downloader exited with an error at %date% %time% >> evening_download.log
"C:\Users\SUMIT SHARMA\AppData\Local\Python\pythoncore-3.14-64\python.exe" download_announcements.py --auto --batch=evening >> evening_download.log 2>&1 || echo WARNING: downloader exited with an error at %date% %time% >> evening_download.log
echo === Run completed at %date% %time% === >> evening_download.log