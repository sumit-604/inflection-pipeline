# ============================================================================
# register_watchlist_feed_task.ps1
#
# One-shot installer for the "Watchlist Feed Download (every 4h)" Windows
# scheduled task. Right-click this file → "Run with PowerShell" (as Admin).
#
# Idempotent — re-running it removes the old task and re-creates it with the
# current settings, so it's safe to run any time you want to update.
#
# What it creates:
#   Task name:  Watchlist Feed Download (every 4h)
#   Folder:     \ConcallPipeline\   (creates the folder if absent)
#   Trigger:    Daily, start 00:55, repeat every 4 hours, indefinitely
#               → fires at 00:55, 04:55, 08:55, 12:55, 16:55, 20:55
#   Action:     C:\ConcallPipeline\Daily Concall Intelligence\watchlist_feed_download.bat
#   Working dir: C:\ConcallPipeline\Daily Concall Intelligence
#   Run as:     current user, highest privileges, wakes the PC, runs on battery
# ============================================================================

$ErrorActionPreference = "Stop"

# --- Self-elevate if not running as admin ---------------------------------------
$me = New-Object Security.Principal.WindowsPrincipal `
        ([Security.Principal.WindowsIdentity]::GetCurrent())
if (-not $me.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "Not running as Administrator — re-launching elevated..." -ForegroundColor Yellow
    Start-Process powershell.exe `
        "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" `
        -Verb RunAs
    exit
}

# --- Config -------------------------------------------------------------------
$TaskName   = "Watchlist Feed Download (every 4h)"
$TaskPath   = "\ConcallPipeline\"          # subfolder inside Task Scheduler Library
$BatPath    = "C:\ConcallPipeline\Daily Concall Intelligence\watchlist_feed_download.bat"
$WorkingDir = "C:\ConcallPipeline\Daily Concall Intelligence"

Write-Host ""
Write-Host "Registering Windows scheduled task..." -ForegroundColor Cyan
Write-Host "  Name:         $TaskName"
Write-Host "  Folder:       $TaskPath"
Write-Host "  Script:       $BatPath"
Write-Host "  Working dir:  $WorkingDir"
Write-Host ""

# --- Sanity check that the .bat exists ----------------------------------------
if (-not (Test-Path $BatPath)) {
    Write-Host "ERROR: $BatPath does not exist." -ForegroundColor Red
    Write-Host "Make sure watchlist_feed_download.bat is in the project folder." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# --- Remove existing task if present (so this is idempotent) ------------------
$existing = Get-ScheduledTask -TaskName $TaskName -TaskPath $TaskPath -ErrorAction SilentlyContinue
if ($existing) {
    Write-Host "Existing task found — removing it first..." -ForegroundColor Yellow
    Unregister-ScheduledTask -TaskName $TaskName -TaskPath $TaskPath -Confirm:$false
}

# --- Build the action: run the .bat, with the working directory set so the ---
# --- script's relative paths (.env, results_downloads_feed/) resolve. ---------
$action = New-ScheduledTaskAction `
    -Execute $BatPath `
    -WorkingDirectory $WorkingDir

# --- Build the trigger: today at 00:55, repeat every 4 hours forever ----------
$startTime = (Get-Date -Hour 0 -Minute 55 -Second 0)
$trigger = New-ScheduledTaskTrigger -Daily -At $startTime
$trigger.Repetition = (New-ScheduledTaskTrigger `
    -Once -At $startTime `
    -RepetitionInterval (New-TimeSpan -Hours 4) `
    -RepetitionDuration ([TimeSpan]::MaxValue) `
    ).Repetition

# --- Settings: allow battery, wake PC, restart on failure, 1h limit -----------
$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -WakeToRun `
    -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Hours 1) `
    -RestartCount 2 `
    -RestartInterval (New-TimeSpan -Minutes 5) `
    -MultipleInstances IgnoreNew

# --- Principal: run as current user, highest privileges, only when logged on -
# (Logged-on mode avoids the password prompt and is the simplest reliable path
# for an interactive workstation. Switch to S4U if you want it to run when
# logged out — see the README comment block at the bottom of this script.)
$principal = New-ScheduledTaskPrincipal `
    -UserId "$env:USERDOMAIN\$env:USERNAME" `
    -LogonType Interactive `
    -RunLevel Highest

# --- Register -----------------------------------------------------------------
Register-ScheduledTask `
    -TaskName $TaskName `
    -TaskPath $TaskPath `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -Principal $principal `
    -Description "Downloads new screener.in watchlist announcements every 4 hours, 5 minutes before the Claude analysis task fires." `
  | Out-Null

Write-Host ""
Write-Host "✓ Task registered." -ForegroundColor Green
Write-Host ""

# --- Show what got created ----------------------------------------------------
$task = Get-ScheduledTask -TaskName $TaskName -TaskPath $TaskPath
$info = Get-ScheduledTaskInfo -TaskName $TaskName -TaskPath $TaskPath

Write-Host "Verification:"
Write-Host ("  State:         {0}" -f $task.State)
Write-Host ("  Next run:      {0}" -f $info.NextRunTime)
Write-Host ("  Last run:      {0}" -f $info.LastRunTime)
Write-Host ""

Write-Host "Test it now? This will run the .bat once immediately." -ForegroundColor Cyan
$reply = Read-Host "Type 'y' and Enter to run, anything else to skip"
if ($reply -eq 'y') {
    Start-ScheduledTask -TaskName $TaskName -TaskPath $TaskPath
    Write-Host "Task started. Watch the log at:" -ForegroundColor Green
    Write-Host "  $WorkingDir\watchlist_feed_download.log"
}

Write-Host ""
Write-Host "Done. Open Task Scheduler → Task Scheduler Library → ConcallPipeline" -ForegroundColor Green
Write-Host "to see and manage it."
Read-Host "Press Enter to close"

# ============================================================================
# OPTIONAL: run even when logged out
# ============================================================================
# To make the task fire when no one is logged on, change LogonType above to
# 'S4U' (Service-for-User — doesn't need stored credentials but requires
# "Log on as batch job" rights). Or use 'Password' and Register-ScheduledTask
# will prompt for your password once. Interactive (the current setting) is
# the simplest and works fine as long as you stay logged in.
# ============================================================================
