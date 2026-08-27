# export-structure.ps1
# Запуск:
# .\export-structure.ps1
# .\export-structure.ps1 -IncludeDeploy
# .\export-structure.ps1 -IncludeLineCounts
# .\export-structure.ps1 -IncludeDeploy -IncludeLineCounts

param(
    [switch]$IncludeDeploy,
    [switch]$IncludeLineCounts
)

function Format-FileEntry {
    param(
        [System.IO.FileInfo]$File,
        [string]$ProjectRoot,
        [switch]$IncludeLineCounts
    )

    $relativePath = $File.FullName.Replace("$ProjectRoot\", "").Replace("\", "/")

    if ($IncludeLineCounts) {
        try {
            $lines = [System.Linq.Enumerable]::Count([System.IO.File]::ReadLines($File.FullName))
            return "$relativePath ($lines lines)"
        }
        catch {
            return "$relativePath (?)"
        }
    }

    return $relativePath
}

$projectRoot = Split-Path $PSScriptRoot -Parent
$outputFile = "$PSScriptRoot\project_structure.md"

$output = @()
$output += '# Project Structure'
$output += ''
$output += ('> Generated: ' + (Get-Date -Format 'yyyy-MM-dd HH:mm'))
$output += ''
$output += '---'

# ==========================
# BACKEND
# ==========================

$output += ''
$output += '## AI Backend'
$output += ''
$output += '```'

$backendFiles = Get-ChildItem -Path "$projectRoot/backend" -Recurse -File |
    Where-Object {
        $_.FullName -notmatch "\\(migrations|uploads|__pycache__|\.pytest_cache)\\" -and
        $_.Extension -ne ".pyc" -and
        $_.Name -notin @("alembic.ini", "ALEMBIC_README.md")
    } |
    ForEach-Object {
        Format-FileEntry -File $_ -ProjectRoot $projectRoot -IncludeLineCounts:$IncludeLineCounts
    } |
    Sort-Object

$backendFiles | ForEach-Object { $output += $_ }

$output += '```'
$output += ''
$output += ('*Files: ' + $backendFiles.Count + '*')

# ==========================
# FRONTEND
# ==========================

$output += ''
$output += '---'
$output += ''
$output += '## Frontend'

$frontendDirs = @(
    'components',
    'pages',
    'utils',
    'layouts',
    'composables',
    'stores',
    'middleware',
    'plugins',
    'data'
)

foreach ($dir in $frontendDirs) {

    $path = "$projectRoot/frontend/app/$dir"

    if (Test-Path $path) {

        $files = Get-ChildItem -Path $path -Recurse -File |
            ForEach-Object {
                Format-FileEntry -File $_ -ProjectRoot $projectRoot -IncludeLineCounts:$IncludeLineCounts
            } |
            Sort-Object

        if ($files.Count -gt 0) {

            $output += ''
            $output += ('### ' + $dir)
            $output += ''
            $output += '```'

            $files | ForEach-Object { $output += $_ }

            $output += '```'
            $output += ('*Files: ' + $files.Count + '*')
        }
    }
}

# ==========================
# DEPLOY
# ==========================

if ($IncludeDeploy) {

    $output += ''
    $output += '---'
    $output += ''
    $output += '## Deploy'
    $output += ''
    $output += '```'

    $deployFiles = Get-ChildItem -Path "$projectRoot/deploy" -Recurse -File |
        Where-Object {
            $_.Extension -ne ".md"
        } |
        ForEach-Object {
            Format-FileEntry -File $_ -ProjectRoot $projectRoot -IncludeLineCounts:$IncludeLineCounts
        } |
        Sort-Object

    $deployFiles | ForEach-Object { $output += $_ }

    $output += '```'
    $output += ''
    $output += ('*Files: ' + $deployFiles.Count + '*')
}

$output | Set-Content $outputFile -Encoding UTF8

Write-Host ""
Write-Host "Structure saved to $outputFile" -ForegroundColor Green

if ($IncludeLineCounts) {
    Write-Host "Line counts included." -ForegroundColor Cyan
}