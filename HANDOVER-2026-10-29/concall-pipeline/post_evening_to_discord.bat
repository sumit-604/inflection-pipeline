@echo off
REM ============================================================
REM post_evening_to_discord.bat
REM   Wraps `python post_to_discord.py evening` with logging.
REM   Wire this into Windows Task Scheduler (Action) instead of
REM   calling python.exe directly so failures leave a forensic
REM   trail.
REM
REM   Logs:      logs\post_evening_YYYY-MM-DD.log
REM   Exit code: propagates to Task Scheduler
REM ============================================================
setlocal EnableExtensions EnableDelayedExpansion

REM --- always run from the project root ---
cd /d "C:\ConcallPipeline\Daily Concall Intelligence"
if not exist "logs" mkdir "logs"

REM --- ISO timestamp via PowerShell (wmic is deprecated on Win11 23H2+) ---
for /f "usebackq delims=" %%I in (`powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd"`) do set "TODAY=%%I"
for /f "usebackq delims=" %%I in (`powershell -NoProfile -Command "Get-Date -Format HH:mm:ss"`) do set "NOW=%%I"

set "LOGFILE=logs\post_evening_!TODAY!.log"

echo. >> "!LOGFILE!"
echo ============================================================ >> "!LOGFILE!"
echo === Run started !TODAY! !NOW! === >> "!LOGFILE!"
echo === User: %USERNAME%   Host: %COMPUTERNAME% === >> "!LOGFILE!"
echo === Action: python.exe post_to_discord.py evening === >> "!LOGFILE!"
echo ============================================================ >> "!LOGFILE!"

"C:\Users\SUMIT SHARMA\AppData\Local\Python\pythoncore-3.14-64\python.exe" post_to_discord.py evening >> "!LOGFILE!" 2>&1
set "RC=!ERRORLEVEL!"

for /f "usebackq delims=" %%I in (`powershell -NoProfile -Command "Get-Date -Format HH:mm:ss"`) do set "DONE=%%I"
echo. >> "!LOGFILE!"
echo === Run finished !DONE! with exit code !RC! === >> "!LOGFILE!"
echo. >> "!LOGFILE!"

endlocal & exit /b %RC%
