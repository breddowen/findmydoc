# ./helper_functions/search-code.ps1
# Использование: .\search-code.ps1 "functionName"

param(
    [string]$SearchTerm = "",
    [switch]$BuildIndex
)

$projectRoot = Split-Path $PSScriptRoot -Parent
$indexFile = "$PSScriptRoot\code_index.md"

function Build-Index {
    $output = @()
    $output += '# Code Index'
    $output += ''
    $output += ('> Generated: ' + (Get-Date -Format 'yyyy-MM-dd HH:mm'))
    $output += ''
    $output += '---'
    
    # Python
    $output += ''
    $output += '## Python Functions and Classes'
    $output += ''
    $output += '| File | Line | Type | Name |'
    $output += '|:-----|:-----|:-----|:-----|'
    
    Get-ChildItem -Path "$projectRoot/backend" -Recurse -Include "*.py" | 
        Where-Object { $_.FullName -notmatch "\\(__pycache__|migrations|\.pytest_cache)\\" } |
        ForEach-Object {
            $file = $_.FullName.Replace("$projectRoot\", "").Replace("\", "/")
            $lineNum = 0
            Get-Content $_.FullName | ForEach-Object {
                $lineNum++
                if ($_ -match "^\s*(def|class|async def)\s+(\w+)") {
                    $type = $matches[1]
                    $name = $matches[2]
                    $output += ('| `' + $file + '` | ' + $lineNum + ' | `' + $type + '` | **' + $name + '** |')
                }
            }
        }
    
    # Routes
    $output += ''
    $output += '## API Routes'
    $output += ''
    $output += '| File | Line | Method | Path |'
    $output += '|:-----|:-----|:-------|:-----|'
    
    Get-ChildItem -Path "$projectRoot/backend" -Recurse -Include "*.py" | 
        Where-Object { $_.FullName -notmatch "\\(__pycache__|migrations|\.pytest_cache)\\" } |
        ForEach-Object {
            $file = $_.FullName.Replace("$projectRoot\", "").Replace("\", "/")
            $lineNum = 0
            Get-Content $_.FullName | ForEach-Object {
                $lineNum++
                if ($_ -match '@(router|app)\.(get|post|put|delete|patch)\s*\([''"]([^''"]+)') {
                    $method = $matches[2].ToUpper()
                    $path = $matches[3]
                    $output += ('| `' + $file + '` | ' + $lineNum + ' | **' + $method + '** | `' + $path + '` |')
                }
            }
        }
    
    # Vue
    $output += ''
    $output += '## Vue Components'
    $output += ''
    $output += '| Component Path |'
    $output += '|:---------------|'
    
    Get-ChildItem -Path "$projectRoot/frontend" -Recurse -Include "*.vue" |
        Where-Object { $_.FullName -notmatch "\\(node_modules|\.nuxt|dist)\\" } |
        ForEach-Object {
            $file = $_.FullName.Replace("$projectRoot\", "").Replace("\", "/")
            $output += ('| `' + $file + '` |')
        }
    
    # JS Exports
    $output += ''
    $output += '## JS Exports'
    $output += ''
    $output += '| File | Line | Export |'
    $output += '|:-----|:-----|:-------|'
    
    Get-ChildItem -Path "$projectRoot/frontend" -Recurse -Include "*.js","*.ts" |
        Where-Object { $_.FullName -notmatch "\\(node_modules|\.nuxt|dist)\\" } |
        ForEach-Object {
            $file = $_.FullName.Replace("$projectRoot\", "").Replace("\", "/")
            $lineNum = 0
            Get-Content $_.FullName | ForEach-Object {
                $lineNum++
                if ($_ -match "^\s*export\s+(const|function|async function|default function)\s+(\w+)") {
                    $output += ('| `' + $file + '` | ' + $lineNum + ' | **' + $matches[2] + '** |')
                }
            }
        }
    
    # Pinia Stores
    $output += ''
    $output += '## Pinia Stores'
    $output += ''
    
    $storesPath = "$projectRoot/frontend/app/stores"
    if (Test-Path $storesPath) {
        Get-ChildItem -Path $storesPath -Filter "*.js" |
            ForEach-Object {
                $storeName = $_.BaseName
                $output += ('### `' + $storeName + '`')
                $output += ''
                $output += '| Action/Getter |'
                $output += '|:--------------|'
                
                Get-Content $_.FullName | ForEach-Object {
                    if ($_ -match "^\s*(async\s+)?(\w+)\s*\(") {
                        $funcName = $matches[2]
                        if ($funcName -notmatch "^(if|for|while|switch|function|return)$") {
                            $output += ('| `' + $funcName + '` |')
                        }
                    }
                }
                $output += ''
            }
    }
    
    $output | Set-Content $indexFile -Encoding UTF8
    Write-Host "Index built: $indexFile" -ForegroundColor Green
}

if ($BuildIndex -or $SearchTerm -eq "") {
    Build-Index
}

if ($SearchTerm -ne "") {
    Write-Host ""
    Write-Host "Searching for: $SearchTerm" -ForegroundColor Cyan
    Write-Host ""
    
    if (-not (Test-Path $indexFile)) {
        Build-Index
    }
    
    $results = Select-String -Path $indexFile -Pattern $SearchTerm
    
    if ($results) {
        $results | ForEach-Object { Write-Host $_.Line }
        Write-Host ""
        Write-Host "Found: $($results.Count) matches" -ForegroundColor Green
    } else {
        Write-Host "No matches found" -ForegroundColor Yellow
    }
}