# ./helper_functions/export-context.ps1
# Экспортирует код модуля для вставки в AI чат

param(
    [string]$Module,
    
    [switch]$IncludeTests,
    [switch]$IncludeSchemas,
    [switch]$Frontend,
    [switch]$Full,
    [switch]$Core,
    [switch]$Stores,
    [switch]$VerboseOutput,
    [string]$OutputFile = "$PSScriptRoot\context.md"
)

if (-not $Module -and -not $Core -and -not $Stores) {
    Write-Host "ERROR: Specify -Module, -Core or -Stores" -ForegroundColor Red
    Write-Host ""
    Write-Host "Examples:" -ForegroundColor Yellow
    Write-Host "  .\export-context.ps1 -Module users"
    Write-Host "  .\export-context.ps1 -Module users -Full"
    Write-Host "  .\export-context.ps1 -Core"
    Write-Host "  .\export-context.ps1 -Stores"
    exit 1
}

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$projectRoot = Split-Path $PSScriptRoot -Parent

$content = @()
$filesAdded = 0
$totalLines = 0

function Add-FileContent {
    param(
        [string]$FilePath, 
        [string]$Label, 
        [string]$Lang = "python"
    )
    
    if (Test-Path $FilePath) {
        $fileText = [System.IO.File]::ReadAllText($FilePath, [System.Text.Encoding]::UTF8)
        $lineCount = ($fileText -split "`n").Count
        
        $script:content += "### $Label"
        $script:content += "*Lines: $lineCount*"
        $script:content += ""
        $script:content += "``````$Lang"
        $script:content += $fileText
        $script:content += "``````"
        $script:content += ""
        
        $script:filesAdded++
        $script:totalLines += $lineCount
        
        if ($VerboseOutput) {
            Write-Host "  + $Label ($lineCount lines)" -ForegroundColor Gray
        }
        return $true
    }
    return $false
}

# Header
$exportType = if ($Core) { "Core" } elseif ($Stores) { "Stores" } else { $Module }
$content += "# AI Context Export: ``$exportType``"
$content += ""
$content += "> Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
$content += ""

$flags = @()
if ($Full) { $flags += "Full" }
elseif ($Frontend) { $flags += "Frontend" }
else { $flags += "Backend" }
if ($IncludeSchemas) { $flags += "+Schemas" }
if ($IncludeTests) { $flags += "+Tests" }
$content += "> Mode: $($flags -join ' ')"
$content += ""
$content += "---"
$content += ""

# Core files
if ($Core) {
    $content += "## CORE"
    $content += ""
    
    $corePath = Join-Path $projectRoot "backend/app/core"
    
    if (Test-Path $corePath) {
        $coreFiles = @("config.py", "db.py", "security.py")
        
        foreach ($file in $coreFiles) {
            $filePath = Join-Path $corePath $file
            Add-FileContent -FilePath $filePath -Label "core/$file" -Lang "python"
        }
        
        Get-ChildItem -Path $corePath -Filter "*.py" -File | 
            Where-Object { $_.Name -notin ($coreFiles + @("__init__.py")) } |
            ForEach-Object {
                Add-FileContent -FilePath $_.FullName -Label "core/$($_.Name)" -Lang "python"
            }
    }
    
    $mainPath = Join-Path $projectRoot "backend/app/main.py"
    Add-FileContent -FilePath $mainPath -Label "main.py" -Lang "python"
}

# All stores
if ($Stores) {
    $content += "## STORES"
    $content += ""
    
    $storesPath = Join-Path $projectRoot "frontend/app/stores"
    
    if (Test-Path $storesPath) {
        Get-ChildItem -Path $storesPath -Filter "*.js" -File | 
            Sort-Object Name |
            ForEach-Object {
                Add-FileContent -FilePath $_.FullName -Label $_.Name -Lang "javascript"
            }
    }
}

# Backend module
if ($Module -and ((-not $Frontend) -or $Full)) {
    $modulePath = Join-Path $projectRoot "backend/app/modules/$Module"
    
    if (Test-Path $modulePath) {
        $content += "## BACKEND: ``$Module``"
        $content += ""
        
        if ($VerboseOutput) {
            Write-Host "Backend module: $modulePath" -ForegroundColor Cyan
        }
        
        # Models
        $modelsPath = Join-Path $modulePath "models.py"
        Add-FileContent -FilePath $modelsPath -Label "models.py" -Lang "python"
        
        # Enums
        $enumsPath = Join-Path $modulePath "enums.py"
        Add-FileContent -FilePath $enumsPath -Label "enums.py" -Lang "python"
        
        # Schemas
        if ($IncludeSchemas) {
            $schemasPath = Join-Path $modulePath "schemas.py"
            Add-FileContent -FilePath $schemasPath -Label "schemas.py" -Lang "python"
        }
        
        # Routers
        $routersPath = Join-Path $modulePath "routers.py"
        $routerPath = Join-Path $modulePath "router.py"
        Add-FileContent -FilePath $routersPath -Label "routers.py" -Lang "python"
        Add-FileContent -FilePath $routerPath -Label "router.py" -Lang "python"
        
        # Utils
        $utilsPath = Join-Path $modulePath "utils.py"
        $utilPath = Join-Path $modulePath "util.py"
        Add-FileContent -FilePath $utilsPath -Label "utils.py" -Lang "python"
        Add-FileContent -FilePath $utilPath -Label "util.py" -Lang "python"
        
        # Extra py files (including subdirectories)
        $excludeFiles = @("__init__.py", "models.py", "enums.py", "router.py", "routers.py", "util.py", "utils.py", "schemas.py")
        
        # Файлы в корне модуля (кроме уже обработанных)
        Get-ChildItem -Path $modulePath -Filter "*.py" -File | 
            Where-Object { $_.Name -notin $excludeFiles } |
            ForEach-Object {
                Add-FileContent -FilePath $_.FullName -Label $_.Name -Lang "python"
            }
        
        # Файлы во вложенных директориях
        Get-ChildItem -Path $modulePath -Directory | 
            Where-Object { $_.Name -ne "__pycache__" } |
            ForEach-Object {
                $subDir = $_
                $subDirName = $subDir.Name
                
                $content += "### $subDirName/"
                $content += ""
                
                Get-ChildItem -Path $subDir.FullName -Filter "*.py" -Recurse -File |
                    Where-Object { $_.Name -ne "__init__.py" } |
                    Sort-Object FullName |
                    ForEach-Object {
                        $relativePath = $_.FullName.Replace("$modulePath\", "").Replace("\", "/")
                        Add-FileContent -FilePath $_.FullName -Label $relativePath -Lang "python"
                    }
            }
        
        # Tests
        if ($IncludeTests) {
            $testsPath = Join-Path $modulePath "tests"
            if (Test-Path $testsPath) {
                $content += "### Tests"
                $content += ""
                
                Get-ChildItem -Path $testsPath -Filter "*.py" -File |
                    Where-Object { $_.Name -ne "__init__.py" } |
                    ForEach-Object {
                        Add-FileContent -FilePath $_.FullName -Label "tests/$($_.Name)" -Lang "python"
                    }
            }
        }
    }
    else {
        $content += "> Backend module ``$Module`` not found"
        $content += ""
        
        $modulesPath = Join-Path $projectRoot "backend/app/modules"
        if (Test-Path $modulesPath) {
            $available = Get-ChildItem -Path $modulesPath -Directory | 
                Where-Object { $_.Name -ne "__pycache__" } |
                ForEach-Object { $_.Name }
            
            $content += "> Available: ``$($available -join '``, ``')``"
            $content += ""
        }
    }
}

# Frontend
if ($Module -and ($Frontend -or $Full)) {
    $content += "---"
    $content += ""
    $content += "## FRONTEND: ``$Module``"
    $content += ""
    
    # Store
    $content += "### Store"
    $content += ""
    
    $storesPath = Join-Path $projectRoot "frontend/app/stores"
    $storeVariants = @(
        "$Module.js",
        "$($Module.ToLower()).js",
        "$($Module -replace 's$','').js"
    ) | Select-Object -Unique
    
    $storeFound = $false
    foreach ($storeName in $storeVariants) {
        $storePath = Join-Path $storesPath $storeName
        if (Test-Path $storePath) {
            Add-FileContent -FilePath $storePath -Label $storeName -Lang "javascript"
            $storeFound = $true
            break
        }
    }
    
    if (-not $storeFound) {
        $content += "> *No store found*"
        $content += ""
    }
    
    # Components
    $content += "### Components"
    $content += ""
    
    $componentsBase = Join-Path $projectRoot "frontend/app/components"
    
    $componentDirs = @(
        $Module,
        $Module.ToLower(),
        (Get-Culture).TextInfo.ToTitleCase($Module.ToLower())
    ) | Select-Object -Unique
    
    $componentsFound = $false
    foreach ($dirName in $componentDirs) {
        $compPath = Join-Path $componentsBase $dirName
        if (Test-Path $compPath) {
            Get-ChildItem -Path $compPath -Filter "*.vue" -Recurse -File | 
                Sort-Object FullName |
                ForEach-Object {
                    $relativePath = $_.FullName.Replace("$componentsBase\", "").Replace("\", "/")
                    Add-FileContent -FilePath $_.FullName -Label $relativePath -Lang "vue"
                    $componentsFound = $true
                }
            break
        }
    }
    
    if (-not $componentsFound) {
        $content += "> *No components found*"
        $content += ""
    }
    
    # Pages
    $content += "### Pages"
    $content += ""
    
    $pagesPath = Join-Path $projectRoot "frontend/app/pages"
    $pagesFound = $false
    
    if (Test-Path $pagesPath) {
        $modulePageDir = Join-Path $pagesPath $Module.ToLower()
        
        if (Test-Path $modulePageDir) {
            Get-ChildItem -Path $modulePageDir -Filter "*.vue" -Recurse -File |
                ForEach-Object {
                    $relativePath = $_.FullName.Replace("$pagesPath\", "").Replace("\", "/")
                    Add-FileContent -FilePath $_.FullName -Label "pages/$relativePath" -Lang "vue"
                    $pagesFound = $true
                }
        }
        
        $singlePage = Join-Path $pagesPath "$($Module.ToLower()).vue"
        if (Test-Path $singlePage) {
            Add-FileContent -FilePath $singlePage -Label "pages/$($Module.ToLower()).vue" -Lang "vue"
            $pagesFound = $true
        }
    }
    
    if (-not $pagesFound) {
        $content += "> *No pages found*"
        $content += ""
    }
}

# Summary
$content += "---"
$content += ""
$content += "## Summary"
$content += ""
$content += "| Metric | Value |"
$content += "|:-------|------:|"
$content += "| Files exported | $filesAdded |"
$content += "| Total lines | $totalLines |"
$content += "| Estimated tokens | ~$([math]::Round($totalLines * 1.3)) |"
$content += ""

# Save
$utf8NoBom = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllLines($OutputFile, $content, $utf8NoBom)

$size = [math]::Round((Get-Item $OutputFile).Length / 1KB, 1)

Write-Host ""
Write-Host "Done: $OutputFile" -ForegroundColor Green
Write-Host "Files: $filesAdded | Lines: $totalLines | Size: $size KB" -ForegroundColor Cyan