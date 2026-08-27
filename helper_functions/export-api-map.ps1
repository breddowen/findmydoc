# ./helper_functions/export-api-map.ps1


param(
    [switch]$IncludeSchemas,
    [string]$OutputFile = "$PSScriptRoot\api_map.md"
)

$projectRoot = Split-Path $PSScriptRoot -Parent

$output = @()
$output += '# API ENDPOINTS MAP'
$output += ''
$output += ('> Generated: ' + (Get-Date -Format 'yyyy-MM-dd HH:mm'))
$output += ''
$output += '---'

Get-ChildItem -Path "$projectRoot/backend/app/modules" -Recurse -Filter "*.py" |
    Where-Object { $_.Name -match "^router" } |
    ForEach-Object {
        $module = $_.Directory.Name
        $modulePath = $_.Directory.FullName
        $filePath = $_.FullName
        
        # Относительный путь от backend
        $relativePath = $filePath.Replace("$projectRoot\backend\", "").Replace("\", "/")
        
        $output += ''
        $output += ('## ' + $module.ToUpper())
        $output += ''
        $output += ('# ./' + $relativePath)
        $output += ''
        $output += '| Method | Endpoint | Handler |'
        $output += '|:-------|:---------|:--------|'
        
        $fileContent = Get-Content $filePath -Raw -Encoding UTF8
        
        # Prefix роутера
        $prefixPattern = 'APIRouter\s*\(\s*prefix\s*=\s*["\x27]([^"\x27]*)["\x27]'
        $prefixMatch = [regex]::Match($fileContent, $prefixPattern)
        $routerPrefix = ""
        if ($prefixMatch.Success) {
            $routerPrefix = $prefixMatch.Groups[1].Value
        }
        
        # Роуты
        $routePattern = '@router\.(get|post|put|delete|patch)\s*\(\s*["\x27]([^"\x27]*)["\x27]'
        $routeMatches = [regex]::Matches($fileContent, $routePattern, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
        
        foreach ($rm in $routeMatches) {
            $method = $rm.Groups[1].Value.ToUpper()
            $path = $rm.Groups[2].Value
            
            if ($path -eq "") {
                if ($routerPrefix -eq "") {
                    $displayPath = "/"
                } else {
                    $displayPath = $routerPrefix
                }
            } else {
                $displayPath = $path
            }
            
            $decoratorEnd = $rm.Index + $rm.Length
            $remainingLength = $fileContent.Length - $decoratorEnd
            $searchLength = [Math]::Min(500, $remainingLength)
            
            $funcName = "[unknown]"
            if ($searchLength -gt 0) {
                $searchArea = $fileContent.Substring($decoratorEnd, $searchLength)
                $funcPattern = '\)\s*(#[^\n]*)?\s*(async\s+)?def\s+(\w+)\s*\('
                $funcMatch = [regex]::Match($searchArea, $funcPattern, [System.Text.RegularExpressions.RegexOptions]::Singleline)
                if ($funcMatch.Success) {
                    $funcName = $funcMatch.Groups[3].Value
                }
            }
            
            $output += ('| **' + $method + '** | `' + $displayPath + '` | `' + $funcName + '()` |')
        }
        
        if ($routeMatches.Count -eq 0) {
            $output += '| - | *No routes found* | - |'
        }
        
        # ============================================
        # SCHEMAS
        # ============================================
        if ($IncludeSchemas) {
            $schemasPath = Join-Path $modulePath "schemas.py"
            
            if (Test-Path $schemasPath) {
                $schemasRelativePath = $schemasPath.Replace("$projectRoot\backend\", "").Replace("\", "/")
                
                $output += ''
                $output += ('# ./' + $schemasRelativePath)
                $output += ''
                
                $schemasContent = Get-Content $schemasPath -Raw -Encoding UTF8
                $classPattern = 'class\s+(\w+)\s*\(([^)]+)\):'
                $classMatches = [regex]::Matches($schemasContent, $classPattern)
                
                foreach ($cm in $classMatches) {
                    $className = $cm.Groups[1].Value
                    $baseClass = $cm.Groups[2].Value.Trim()
                    
                    $output += ('**`' + $className + '`** <- *' + $baseClass + '*')
                    
                    # Получаем тело класса
                    $classPos = $cm.Index + $cm.Length
                    $nextClassMatch = [regex]::Match($schemasContent.Substring($classPos), 'class\s+\w+')
                    
                    if ($nextClassMatch.Success) {
                        $classBody = $schemasContent.Substring($classPos, $nextClassMatch.Index)
                    } else {
                        $classBody = $schemasContent.Substring($classPos)
                    }
                    
                    # Извлекаем поля
                    $fieldPattern = '^\s{4}(\w+)\s*:\s*([^\n=]+)'
                    $fieldMatches = [regex]::Matches($classBody, $fieldPattern, [System.Text.RegularExpressions.RegexOptions]::Multiline)
                    
                    $hasFields = $false
                    foreach ($fm in $fieldMatches) {
                        $fieldName = $fm.Groups[1].Value
                        $fieldType = $fm.Groups[2].Value.Trim()
                        
                        if ($fieldName -notin @("class", "model", "Config", "model_config")) {
                            if (-not $hasFields) {
                                $output += ''
                                $output += '| Field | Type |'
                                $output += '|:------|:-----|'
                                $hasFields = $true
                            }
                            $output += ('| `' + $fieldName + '` | `' + $fieldType + '` |')
                        }
                    }
                    
                    $output += ''
                }
            }
        }
        
        $output += '---'
    }

# Убираем последний ---
if ($output[-1] -eq '---') {
    $output = $output[0..($output.Length - 2)]
}

$output | Set-Content $OutputFile -Encoding UTF8
Write-Host "API map saved to $OutputFile" -ForegroundColor Green

if ($IncludeSchemas) {
    Write-Host "Schemas included under each module!" -ForegroundColor Cyan
}