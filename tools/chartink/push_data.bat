@echo off
REM Commit and push tonight's Chartink data. Called by Windows Task Scheduler
REM after the brief is written. Touches only data\chartink\, in its own commit,
REM so pipeline work and market data never share a commit.
REM
REM Exit 0 when there was nothing new or the push succeeded. Non-zero on a
REM failed push; the commit stays local and goes up on the next run.

setlocal
set "REPO=C:\Users\SUMIT SHARMA\repos\inflection-pipeline"
set "GIT=git"
cd /d "%REPO%" || exit /b 9

REM The trade date is the newest folder under data\chartink\csv. That is
REM locale-proof, unlike %DATE%, and it names the data rather than the clock.
set "TRADE="
for /f "delims=" %%d in ('dir /b /ad /o-n "%REPO%\data\chartink\csv" 2^>nul') do (
    if not defined TRADE set "TRADE=%%d"
)
if not defined TRADE set "TRADE=unknown-date"

REM Stage only the data tree. Rendered HTML and the run log are git-ignored.
%GIT% add -A -- data\chartink
%GIT% diff --cached --quiet -- data\chartink
if "%ERRORLEVEL%"=="0" (
    echo push_data: nothing new under data\chartink.
    exit /b 0
)

%GIT% commit -q -m "chartink data: %TRADE%" -- data\chartink
if not "%ERRORLEVEL%"=="0" exit /b 3

REM Push. If the remote moved, rebase our data commit on top and retry once.
%GIT% push -q origin HEAD:main
if "%ERRORLEVEL%"=="0" goto done
%GIT% pull -q --rebase --autostash origin main
if not "%ERRORLEVEL%"=="0" exit /b 4
%GIT% push -q origin HEAD:main
if not "%ERRORLEVEL%"=="0" exit /b 5

:done
for /f %%h in ('%GIT% rev-parse --short HEAD') do echo push_data: pushed %%h
exit /b 0
