<#
.SYNOPSIS
  Clean leftover Anaconda/Conda folders, remove conda init blocks from PowerShell profiles,
  and remove CMD AutoRun that references conda. Backs up rather than immediately deleting by default.

.NOTES
  Save as clean_anaconda.ps1 and run in PowerShell (Admin recommended).
#>

# --- config ---
$timestamp = (Get-Date).ToString('yyyyMMdd_HHmmss')
$backupRoot = Join-Path -Path $env:USERPROFILE -ChildPath "AnacondaBackup_$timestamp"
$logFile = Join-Path -Path $env:USERPROFILE -ChildPath "clean_anaconda_$timestamp.log"

$folderCandidates = @(
    "$env:USERPROFILE\anaconda3",
    "$env:USERPROFILE\.conda",
    "$env:USERPROFILE\.anaconda_backup",
    "$env:USERPROFILE\AppData\Local\conda",
    "$env:USERPROFILE\AppData\Local\Continuum",
    "$env:USERPROFILE\AppData\Local\anaconda3",
    "C:\Users\$env:USERNAME\anaconda3",   # extra safe explicit
    "C:\ProgramData\Anaconda3",
    "D:\ProgramData\anaconda3",
    "C:\ProgramData\anaconda3",
    "$env:USERPROFILE\AppData\Roaming\jupyter",
    "$env:USERPROFILE\AppData\Roaming\pip"
)

# PowerShell profile paths object:
$profiles = @{
    AllUsersAllHosts = $PROFILE.AllUsersAllHosts
    AllUsersCurrentHost = $PROFILE.AllUsersCurrentHost
    CurrentUserAllHosts = $PROFILE.CurrentUserAllHosts
    CurrentUserCurrentHost = $PROFILE.CurrentUserCurrentHost
}

# Logging helper
function Log {
    param($msg)
    $line = ("[{0}] {1}" -f (Get-Date), $msg)
    Add-Content -Path $logFile -Value $line
    Write-Host $msg
}

# Admin check
function Test-IsAdmin {
    $id = [Security.Principal.WindowsIdentity]::GetCurrent()
    $p = New-Object Security.Principal.WindowsPrincipal($id)
    return $p.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

# Remove conda block from a file (back up first)
function Remove-CondaBlockFromProfile {
    param($path)
    if (-not (Test-Path $path)) {
        Log "Profile file not found: $path"
        return
    }
    try {
        $backup = "$path.bak.$timestamp"
        Copy-Item -Path $path -Destination $backup -Force
        Log "Backed up profile: $path -> $backup"
        $content = Get-Content -Raw -LiteralPath $path
        # remove standard conda initialize block (DOTALL)
        $new = [Regex]::Replace($content, '(?s)# >>> conda initialize >>>.*?# <<< conda initialize <<<', '')
        # also remove stray 'conda activate base' lines
        $new = [Regex]::Replace($new, '^\s*conda\s+activate\s+base\s*$','', [Text.RegularExpressions.RegexOptions]::Multiline)
        Set-Content -LiteralPath $path -Value $new -Force
        Log "Removed conda initialize block (if existed) from: $path"
    } catch {
        Log "ERROR editing profile $path : $_"
    }
}

# Backup or delete folders
function Process-Folder {
    param($path, $action) # action: 'backup' or 'delete'
    if (-not (Test-Path $path)) {
        Log "Not found: $path"
        return
    }
    try {
        if ($action -eq 'backup') {
            if (-not (Test-Path $backupRoot)) { New-Item -ItemType Directory -Path $backupRoot | Out-Null }
            $dest = Join-Path -Path $backupRoot -ChildPath ([IO.Path]::GetFileName($path))
            # avoid name collisions
            if (Test-Path $dest) { $dest = $dest + "_$timestamp" }
            Log "Moving: $path -> $dest"
            Move-Item -LiteralPath $path -Destination $dest -Force
            Log "Moved $path to $dest"
        } else {
            Log "Removing permanently: $path"
            Remove-Item -LiteralPath $path -Recurse -Force -ErrorAction Stop
            Log "Removed: $path"
        }
    } catch {
        Log "ERROR processing folder $path : $_"
    }
}

# Remove AutoRun registry entry if it references conda/anaconda
function Clean-CmdAutoRun {
    $regPath = "HKCU:\Software\Microsoft\Command Processor"
    try {
        $entry = (Get-ItemProperty -Path $regPath -Name AutoRun -ErrorAction SilentlyContinue).AutoRun
        if ($null -ne $entry) {
            if ($entry -match '(conda|anaconda|activate)') {
                $backupReg = Join-Path -Path $backupRoot -ChildPath "autorun_reg_$timestamp.txt"
                if (-not (Test-Path $backupRoot)) { New-Item -ItemType Directory -Path $backupRoot | Out-Null }
                $entry | Out-File -FilePath $backupReg -Encoding utf8
                Log "Backed up AutoRun value to $backupReg"
                Remove-ItemProperty -Path $regPath -Name AutoRun -ErrorAction Stop
                Log "Removed AutoRun registry entry referencing conda/anaconda."
            } else {
                Log "AutoRun exists but does not reference conda/anaconda. Skipping."
            }
        } else {
            Log "No AutoRun registry entry found under $regPath"
        }
    } catch {
        Log "ERROR checking/removing registry AutoRun: $_"
    }
}

# Start script
"----------------------------------------" | Out-File -FilePath $logFile
Log "Starting Anaconda cleanup script."
Log "Backup root: $backupRoot"
if (-not (Test-IsAdmin)) {
    Log "WARNING: Not running as Administrator. Some locations (ProgramData) or registry keys may fail to change."
    Write-Host ""
    Write-Host "It is recommended to run PowerShell as Administrator for full cleanup."
    Write-Host ""
}

# Show found folders
$found = @()
foreach ($f in $folderCandidates) {
    if (Test-Path $f) { $found += (Resolve-Path $f).Path }
}
if ($found.Count -eq 0) {
    Log "No common Anaconda folders found in the scan list."
} else {
    Log "Found the following existing Anaconda/conda folders:"
    $found | ForEach-Object { Log "  $_" }
}

# Ask user what to do if anything found
if ($found.Count -gt 0) {
    Write-Host ""
    $choice = Read-Host "Choose action: (B)ackup/move to backup folder (recommended)  (D)elete permanently  (C)ancel"
    switch ($choice.ToUpper()) {
        'B' { $action = 'backup' }
        'D' { $action = 'delete' }
        default {
            Log "User cancelled. Exiting without touching folders."
            Write-Host "No changes made. Check log at $logFile"
            exit 0
        }
    }

    foreach ($p in $found) {
        Process-Folder -path $p -action $action
    }

    Log "Folder processing complete."
} else {
    Log "No folders to backup/delete."
}

# Clean PowerShell profiles
Log "Inspecting PowerShell profiles..."
foreach ($k in $profiles.Keys) {
    $p = $profiles[$k]
    if ($p) {
        if (Test-Path $p) {
            Remove-CondaBlockFromProfile -path $p
        } else {
            Log "Profile not present: $p"
        }
    }
}

# Search for any .ps1 files under Documents containing 'conda' and show to user
Log "Searching Documents for .ps1 files mentioning 'conda'..."
$matches = Get-ChildItem "$env:USERPROFILE\Documents" -Include *.ps1 -Recurse -ErrorAction SilentlyContinue |
    Select-String -Pattern "conda" |
    Select Path, LineNumber, Line -ErrorAction SilentlyContinue

if ($matches) {
    Log "Found references to 'conda' in the following files under Documents:"
    $matches | ForEach-Object { Log "  $($_.Path):$($_.LineNumber) -> $($_.Line.Trim())" }
    Log "Please open and inspect these files manually and remove any 'conda activate' lines if desired."
} else {
    Log "No .ps1 references to 'conda' found under Documents."
}

# Clean registry AutoRun for cmd.exe if referencing conda
Clean-CmdAutoRun

Log "Cleanup finished. Review log at: $logFile"
Write-Host ""
Write-Host "DONE. Log written to: $logFile"
if (Test-Path $backupRoot) { Write-Host "Backup/moved folders (if any) are in: $backupRoot" }
