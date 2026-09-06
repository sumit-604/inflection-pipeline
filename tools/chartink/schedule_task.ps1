# Register the daily Chartink collector with Windows Task Scheduler.
#
# Runs as the current user. No administrator rights are needed.
#
#   Register:    powershell -ExecutionPolicy Bypass -File tools\chartink\schedule_task.ps1
#   Change time: ... schedule_task.ps1 -Time 18:30
#   Remove:      ... schedule_task.ps1 -Remove
#   Check:       Get-ScheduledTask -TaskName 'Chartink Daily Collector'
#
# The task runs Monday to Friday. It wakes the machine if it is asleep, and it
# runs as soon as the machine is next on if a run was missed.

param(
    [string]$Time = "21:00",
    [string]$PushTime = "22:15",
    [string]$TaskName = "Chartink Daily Collector",
    [string]$PushTaskName = "Chartink Data Push",
    [switch]$Remove
)

$ErrorActionPreference = "Stop"

$repo = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$bat  = Join-Path $PSScriptRoot "run_daily.bat"
$push = Join-Path $PSScriptRoot "push_data.bat"

if ($Remove) {
    foreach ($name in @($TaskName, $PushTaskName)) {
        if (Get-ScheduledTask -TaskName $name -ErrorAction SilentlyContinue) {
            Unregister-ScheduledTask -TaskName $name -Confirm:$false
            Write-Host "Removed scheduled task '$name'."
        } else {
            Write-Host "No scheduled task named '$name'."
        }
    }
    return
}

if (-not (Test-Path $bat)) {
    throw "Cannot find $bat"
}

$action = New-ScheduledTaskAction -Execute $bat -WorkingDirectory $repo

$trigger = New-ScheduledTaskTrigger -Weekly `
    -DaysOfWeek Monday, Tuesday, Wednesday, Thursday, Friday `
    -At $Time

$settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -WakeToRun `
    -DontStopOnIdleEnd `
    -ExecutionTimeLimit (New-TimeSpan -Hours 1) `
    -MultipleInstances IgnoreNew `
    -RestartCount 3 `
    -RestartInterval (New-TimeSpan -Minutes 15)

if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
}

Register-ScheduledTask -TaskName $TaskName `
    -Action $action -Trigger $trigger -Settings $settings `
    -Description "Collects Chartink dashboard breadth data into data\chartink\ each weekday." | Out-Null

Write-Host "Registered '$TaskName': weekdays at $Time."

# Second task: commit and push data\chartink after the brief is written.
# The Claude task writes the brief at 21:30; this runs well after it.
$pushAction  = New-ScheduledTaskAction -Execute $push -WorkingDirectory $repo
$pushTrigger = New-ScheduledTaskTrigger -Weekly `
    -DaysOfWeek Monday, Tuesday, Wednesday, Thursday, Friday -At $PushTime
$pushSettings = New-ScheduledTaskSettingsSet -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 15) -MultipleInstances IgnoreNew

if (Get-ScheduledTask -TaskName $PushTaskName -ErrorAction SilentlyContinue) {
    Unregister-ScheduledTask -TaskName $PushTaskName -Confirm:$false
}
Register-ScheduledTask -TaskName $PushTaskName `
    -Action $pushAction -Trigger $pushTrigger -Settings $pushSettings `
    -Description "Commits and pushes data\chartink\ to GitHub each weekday, in a data-only commit." | Out-Null

Write-Host "Registered '$PushTaskName': weekdays at $PushTime."
Write-Host "Run now with:  Start-ScheduledTask -TaskName '$TaskName'   or   '$PushTaskName'"
Write-Host "Log:           $repo\data\chartink\_collector.log"
