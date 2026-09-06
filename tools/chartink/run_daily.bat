@echo off
REM Daily Chartink chain. Called by Windows Task Scheduler.
REM Register it with tools/chartink/schedule_task.ps1.
REM
REM   1. fetch_chartink.py  downloads every dashboard tile into data\chartink\
REM   2. consolidate.py     folds those into a few analysis CSVs
REM   3. digest.py          writes the dated markdown digest
REM
REM Exit code 0 means the whole chain succeeded. Any other code means a step
REM failed; read data\chartink\_collector.log for the reason.

setlocal

set "PYEXE=C:\Users\SUMIT SHARMA\AppData\Local\Python\pythoncore-3.14-64\python.exe"
set "REPO=C:\Users\SUMIT SHARMA\repos\inflection-pipeline"
set "TOOLS=%REPO%\tools\chartink"

cd /d "%REPO%" || exit /b 9

"%PYEXE%" "%TOOLS%\fetch_chartink.py" %*
set "RC=%ERRORLEVEL%"
if not "%RC%"=="0" (
    echo fetch_chartink.py failed with %RC%, not consolidating stale data.
    exit /b %RC%
)

"%PYEXE%" "%TOOLS%\consolidate.py"
if not "%ERRORLEVEL%"=="0" exit /b %ERRORLEVEL%

"%PYEXE%" "%TOOLS%\digest.py"
if not "%ERRORLEVEL%"=="0" exit /b %ERRORLEVEL%

REM The facts sheet the nightly brief is written from. Reads the 34 table
REM CSVs for the latest trade date under data\chartink\csv\<date>\.
"%PYEXE%" "%TOOLS%\facts.py"
if not "%ERRORLEVEL%"=="0" exit /b %ERRORLEVEL%

REM Render the browser-readable pages. The brief is written later by the
REM Claude task, which re-renders afterwards.
"%PYEXE%" "%TOOLS%\render_html.py"
if not "%ERRORLEVEL%"=="0" exit /b %ERRORLEVEL%

exit /b 0
