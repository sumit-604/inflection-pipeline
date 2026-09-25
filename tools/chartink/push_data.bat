@echo off
REM Commit and push tonight's Chartink data. Called by Windows Task Scheduler
REM after the brief is written. Touches only data\chartink\, in its own commit,
REM so pipeline work and market data never share a commit.
REM
REM The collector and the brief write into the main checkout (REPO), which may
REM sit on any run branch. The commit is made in a separate worktree (DATAWT)
REM that always tracks origin/main, so the data lands on main whatever branch
REM REPO holds. DATAWT is a sparse checkout of data\chartink only, which keeps
REM it small and clear of the long file names under runs\.
REM
REM Files are copied REPO -> DATAWT, never deleted, so a file main has and the
REM current branch lacks is kept.
REM
REM Exit 0 when there was nothing new or the push succeeded. Non-zero on a
REM failure; nothing is lost, the next run copies and pushes again.

setlocal
set "REPO=C:\Users\SUMIT SHARMA\repos\inflection-pipeline"
set "DATAWT=C:\Users\SUMIT SHARMA\repos\ip-chartink-main"
set "GIT=git"
cd /d "%REPO%" || exit /b 9

REM The trade date is the newest folder under data\chartink\csv. That is
REM locale-proof, unlike %DATE%, and it names the data rather than the clock.
set "TRADE="
for /f "delims=" %%d in ('dir /b /ad /o-n "%REPO%\data\chartink\csv" 2^>nul') do (
    if not defined TRADE set "TRADE=%%d"
)
if not defined TRADE set "TRADE=unknown-date"

%GIT% fetch -q origin main || exit /b 7

REM Create the data worktree on first use.
if not exist "%DATAWT%\.git" (
    %GIT% worktree prune
    %GIT% worktree add -q --no-checkout --detach "%DATAWT%" origin/main || exit /b 6
    %GIT% -C "%DATAWT%" sparse-checkout set --no-cone /data/chartink/ || exit /b 6
)

REM Start from the current origin/main every night.
%GIT% -C "%DATAWT%" reset -q --hard origin/main || exit /b 7

REM Copy new and changed files. Rendered HTML and the run log are git-ignored.
robocopy "%REPO%\data\chartink" "%DATAWT%\data\chartink" /E /XF *.html _collector.log /R:1 /W:1 /NFL /NDL /NJH /NJS /NP >nul
if %ERRORLEVEL% GEQ 8 exit /b 8

cd /d "%DATAWT%" || exit /b 9
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
%GIT% pull -q --rebase origin main
if not "%ERRORLEVEL%"=="0" exit /b 4
%GIT% push -q origin HEAD:main
if not "%ERRORLEVEL%"=="0" exit /b 5

:done
for /f %%h in ('%GIT% rev-parse --short HEAD') do echo push_data: pushed %%h to main
exit /b 0
