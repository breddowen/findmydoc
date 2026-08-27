# ./helper_functions/export-imports.ps1
# Экспортирует внутренние импорты проекта (без внешних библиотек)

param(
    [string]$OutputFile = "$PSScriptRoot\imports.md",
    [switch]$PythonOnly,
    [switch]$JSOnly,
    [switch]$VerboseOutput
)

$projectRoot = Split-Path $PSScriptRoot -Parent

$output = @()
$output += '# Project Imports Map'
$output += ''
$output += ('> Generated: ' + (Get-Date -Format 'yyyy-MM-dd HH:mm'))
$output += ''
$output += '> Internal imports only (excluding external libraries)'
$output += ''
$output += '---'

$filesProcessed = 0
$totalImports = 0

# ============================================
# Python Files
# ============================================
if (-not $JSOnly) {
    $output += ''
    $output += '## Python Imports'
    $output += ''
    
    Get-ChildItem -Path "$projectRoot/backend" -Recurse -Filter "*.py" |
        Where-Object { 
            $_.FullName -notmatch "\\(__pycache__|migrations|\.pytest_cache|venv|\.venv)\\" -and
            $_.Name -ne "__init__.py"
        } |
        Sort-Object FullName |
        ForEach-Object {
            $relativePath = $_.FullName.Replace("$projectRoot\", "").Replace("\", "/")
            $fileContent = [System.IO.File]::ReadAllText($_.FullName, [System.Text.Encoding]::UTF8)
            
            $internalImports = @()
            $lines = $fileContent -split "`r?`n"
            $multilineImport = ""
            $inMultiline = $false
            
            foreach ($line in $lines) {
                $trimmed = $line.Trim()
                
                # Если мы внутри многострочного импорта
                if ($inMultiline) {
                    $multilineImport += "`n" + $line.TrimEnd()
                    
                    # Проверяем закрытие скобки
                    if ($trimmed -match '\)') {
                        # Проверяем, является ли это внутренним импортом
                        if ($multilineImport -match '^from\s+(\.+[\w.]*)\s+import' -or 
                            $multilineImport -match '^from\s+(app|backend)[\w.]*\s+import') {
                            $internalImports += $multilineImport
                        }
                        $multilineImport = ""
                        $inMultiline = $false
                    }
                    continue
                }
                
                # Начало многострочного импорта
                if ($trimmed -match '^from\s+.+\s+import\s+\(' -and $trimmed -notmatch '\)') {
                    $multilineImport = $line.TrimEnd()
                    $inMultiline = $true
                    continue
                }
                
                # Однострочные импорты
                # Относительные импорты (from . или from .. или from ...)
                if ($trimmed -match '^from\s+(\.+[\w.]*)\s+import') {
                    $internalImports += $line.TrimEnd()
                }
                # Абсолютные импорты из app.* или backend.*
                elseif ($trimmed -match '^from\s+(app|backend)[\w.]*\s+import') {
                    $internalImports += $line.TrimEnd()
                }
                elseif ($trimmed -match '^import\s+(app|backend)[\w.]*') {
                    $internalImports += $line.TrimEnd()
                }
            }
            
            if ($internalImports.Count -gt 0) {
                $output += "### ./$relativePath"
                $output += ''
                $output += '```python'
                $internalImports | ForEach-Object { $output += $_ }
                $output += '```'
                $output += ''
                
                $script:filesProcessed++
                $script:totalImports += $internalImports.Count
                
                if ($VerboseOutput) {
                    Write-Host "  + $relativePath ($($internalImports.Count) imports)" -ForegroundColor Gray
                }
            }
        }
}

# ============================================
# JavaScript/Vue Files
# ============================================
if (-not $PythonOnly) {
    $output += ''
    $output += '---'
    $output += ''
    $output += '## JavaScript/Vue Imports'
    $output += ''
    
    Get-ChildItem -Path "$projectRoot/frontend" -Recurse -Include "*.js","*.ts","*.vue" |
        Where-Object { 
            $_.FullName -notmatch "\\(node_modules|\.nuxt|dist|\.output)\\" 
        } |
        Sort-Object FullName |
        ForEach-Object {
            $relativePath = $_.FullName.Replace("$projectRoot\", "").Replace("\", "/")
            $fileContent = [System.IO.File]::ReadAllText($_.FullName, [System.Text.Encoding]::UTF8)
            
            $internalImports = @()
            $lines = $fileContent -split "`r?`n"
            
            # Для Vue файлов обрабатываем построчно, ищем <script> секцию
            $inScript = $false
            $multilineImport = ""
            $inMultiline = $false
            
            foreach ($line in $lines) {
                $trimmed = $line.Trim()
                
                # Для Vue - отслеживаем <script> блок
                if ($_.Extension -eq ".vue") {
                    if ($trimmed -match '<script[^>]*>') {
                        $inScript = $true
                        continue
                    }
                    if ($trimmed -match '</script>') {
                        $inScript = $false
                        continue
                    }
                    if (-not $inScript) {
                        continue
                    }
                }
                
                # Если внутри многострочного импорта
                if ($inMultiline) {
                    $multilineImport += "`n" + $line.TrimEnd()
                    
                    # Проверяем окончание импорта (закрывающая кавычка или `)
                    if ($trimmed -match '["\x27`]' -and $trimmed -notmatch '^\s*//') {
                        # Извлекаем путь из всего импорта
                        if ($multilineImport -match '["\x27`]([^"\x27`]+)["\x27`]\s*$') {
                            $importPath = $matches[1]
                            if ($importPath -match '^(\.|@/|~/)') {
                                $internalImports += $multilineImport
                            }
                        }
                        $multilineImport = ""
                        $inMultiline = $false
                    }
                    continue
                }
                
                # Начало многострочного импорта (есть import, но нет закрывающей кавычки на той же строке)
                if ($trimmed -match '^import\s+' -and $trimmed -notmatch 'from\s+["\x27`][^"\x27`]+["\x27`]') {
                    # Проверяем, есть ли путь на этой же строке
                    if ($trimmed -match 'from\s+["\x27`]') {
                        $multilineImport = $line.TrimEnd()
                        $inMultiline = $true
                        continue
                    }
                }
                
                # Однострочные импорты
                if ($trimmed -match '^import\s+.*from\s+["\x27`]([^"\x27`]+)["\x27`]') {
                    $importPath = $matches[1]
                    if ($importPath -match '^(\.|@/|~/)') {
                        $internalImports += $line.TrimEnd()
                    }
                }
                # import './style.css' или import 'file'
                elseif ($trimmed -match '^import\s+["\x27`]([^"\x27`]+)["\x27`]') {
                    $importPath = $matches[1]
                    if ($importPath -match '^(\.|@/|~/)') {
                        $internalImports += $line.TrimEnd()
                    }
                }
            }
            
            if ($internalImports.Count -gt 0) {
                $output += "### ./$relativePath"
                $output += ''
                $output += '```javascript'
                $internalImports | ForEach-Object { $output += $_ }
                $output += '```'
                $output += ''
                
                $script:filesProcessed++
                $script:totalImports += $internalImports.Count
                
                if ($VerboseOutput) {
                    Write-Host "  + $relativePath ($($internalImports.Count) imports)" -ForegroundColor Gray
                }
            }
        }
}

# ============================================
# Summary
# ============================================
$output += '---'
$output += ''
$output += '## Summary'
$output += ''
$output += "| Metric | Value |"
$output += "|:-------|------:|"
$output += "| Files with imports | $filesProcessed |"
$output += "| Total internal imports | $totalImports |"
$output += ''

# ============================================
# Save
# ============================================
$utf8NoBom = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllLines($OutputFile, $output, $utf8NoBom)

$size = [math]::Round((Get-Item $OutputFile).Length / 1KB, 1)

Write-Host ""
Write-Host "Done: $OutputFile" -ForegroundColor Green
Write-Host "Files: $filesProcessed | Imports: $totalImports | Size: $size KB" -ForegroundColor Cyan